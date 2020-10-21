#ifndef TRACK_COLLECTION_ANALYZER
#define TRACK_COLLECTION_ANALYZER

#include "TTree.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

#define TRACK_CLASS reco::Track

using namespace std;

class TrackCollectionAnalyzer : public edm::EDAnalyzer {
	public:
		explicit TrackCollectionAnalyzer(const edm::ParameterSet &);
		~TrackCollectionAnalyzer();
	private:
		void analyze(const edm::Event &, const edm::EventSetup &);

		edm::InputTag generalTracks_;
		edm::InputTag packedCandidates_;
		edm::InputTag lostTracks_;
		edm::InputTag isolatedTracks_;

		edm::InputTag gt2pc_;
		edm::InputTag gt2lt_;

		edm::InputTag genParticles_;

		edm::EDGetTokenT<vector<TRACK_CLASS> > generalTracksToken_;
		edm::EDGetTokenT<pat::PackedCandidateCollection> packedCandidatesToken_;
		edm::EDGetTokenT<pat::PackedCandidateCollection> lostTracksToken_;
		edm::EDGetTokenT<vector<pat::IsolatedTrack> > isolatedTracksToken_;

		edm::EDGetTokenT<edm::Association<pat::PackedCandidateCollection> > gt2pcToken_;
      	edm::EDGetTokenT<edm::Association<pat::PackedCandidateCollection> > gt2ltToken_;

      	edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

      	edm::Service<TFileService> fs_;
      	TTree * tree_;

      	vector<bool> isInPackedCandidates;
      	vector<bool> isInLostTracks;
      	vector<bool> isInIsolatedTracks;

      	vector<double> px, py, pz;
      	vector<double> vx, vy, vz;
      	vector<double> dzError;
      	vector<int> charge;

      	vector<double> genMatchDR;
      	vector<int> genMatchID;
};

TrackCollectionAnalyzer::TrackCollectionAnalyzer(const edm::ParameterSet &cfg) :
	generalTracks_   (cfg.getParameter<edm::InputTag>("tracks")),
	packedCandidates_(cfg.getParameter<edm::InputTag>("packedCandidates")),
	lostTracks_      (cfg.getParameter<edm::InputTag>("lostTracks")),
	isolatedTracks_  (cfg.getParameter<edm::InputTag>("isolatedTracks")),
	gt2pc_           (cfg.getParameter<edm::InputTag>("packedCandidates")),
	gt2lt_           (cfg.getParameter<edm::InputTag>("lostTracks")),
	genParticles_    (cfg.getParameter<edm::InputTag>("genParticles"))
{
	generalTracksToken_    = consumes<vector<TRACK_CLASS> >          (generalTracks_);
	packedCandidatesToken_ = consumes<pat::PackedCandidateCollection>(packedCandidates_);
	lostTracksToken_       = consumes<pat::PackedCandidateCollection>(lostTracks_);
	isolatedTracksToken_   = consumes<vector<pat::IsolatedTrack> >   (isolatedTracks_);

	gt2pcToken_ = consumes<edm::Association<pat::PackedCandidateCollection> >(gt2pc_);
	gt2ltToken_ = consumes<edm::Association<pat::PackedCandidateCollection> >(gt2lt_);

	genParticlesToken_ = consumes<vector<reco::GenParticle> >(genParticles_);

	tree_ = fs_->make<TTree>("tree", "tree");

	tree_->Branch("isInPackedCandidates", &isInPackedCandidates);
	tree_->Branch("isInLostTracks", &isInLostTracks);
	tree_->Branch("isInIsolatedTracks", &isInIsolatedTracks);

	tree_->Branch("px", &px);
	tree_->Branch("py", &py);
	tree_->Branch("pz", &pz);

	tree_->Branch("vx", &vx);
	tree_->Branch("vy", &vy);
	tree_->Branch("vz", &vz);
	tree_->Branch("dzError", &dzError);

	tree_->Branch("charge", &charge);

	tree_->Branch("genMatchDR", &genMatchDR);
	tree_->Branch("genMatchID", &genMatchID);
}

TrackCollectionAnalyzer::~TrackCollectionAnalyzer() 
{
}

void TrackCollectionAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
	edm::Handle<vector<TRACK_CLASS> >           generalTracks;
	edm::Handle<pat::PackedCandidateCollection> packedCandidates;	
	edm::Handle<pat::PackedCandidateCollection> lostTracks;	
	edm::Handle<vector<pat::IsolatedTrack> >   isolatedTracks;

	edm::Handle<edm::Association<pat::PackedCandidateCollection> > gt2pc;
	edm::Handle<edm::Association<pat::PackedCandidateCollection> > gt2lt;

	edm::Handle<vector<reco::GenParticle> > genParticles;

	event.getByToken(generalTracksToken_,    generalTracks);
	event.getByToken(packedCandidatesToken_, packedCandidates);
	event.getByToken(lostTracksToken_,       lostTracks);
	event.getByToken(isolatedTracksToken_,   isolatedTracks);

	event.getByToken(gt2pcToken_, gt2pc);
	event.getByToken(gt2ltToken_, gt2lt);

	event.getByToken(genParticlesToken_, genParticles);

	isInPackedCandidates.clear();
	isInLostTracks.clear();
	isInIsolatedTracks.clear();

	px.clear();
	py.clear();
	pz.clear();

	vx.clear();
	vy.clear();
	vz.clear();
	dzError.clear();

	charge.clear();

	genMatchDR.clear();
	genMatchID.clear();

	for(unsigned int i = 0; i < generalTracks->size(); i++) {

		const TRACK_CLASS &gentk = (*generalTracks)[i];
		//reco::TrackRef tkref = reco::TrackRef(generalTracks, i);
		edm::Ref<vector<TRACK_CLASS> > tkref = edm::Ref<vector<TRACK_CLASS> >(generalTracks, i);

		pat::PackedCandidateRef pcref = (*gt2pc)[tkref];
		pat::PackedCandidateRef ltref = (*gt2lt)[tkref];

		const pat::PackedCandidate &pfCand    = *(pcref.get());
		const pat::PackedCandidate &lostTrack = *(ltref.get());

		isInPackedCandidates.push_back(pcref.isNonnull() && pcref.id() == packedCandidates.id() && pfCand.charge() != 0);
		isInLostTracks.push_back(ltref.isNonnull() && ltref.id() == lostTracks.id() && lostTrack.charge() != 0);
		bool this_isInIsolatedTracks = false;

		for(const auto& isoTrack : *isolatedTracks) {
			double dR = deltaR(gentk, isoTrack);
			if(dR < 0.001) {
				this_isInIsolatedTracks = true;
				break;
			}
		}

		isInIsolatedTracks.push_back(this_isInIsolatedTracks);

		px.push_back(gentk.px());
		py.push_back(gentk.py());
		pz.push_back(gentk.pz());

		vx.push_back(gentk.vx());
		vy.push_back(gentk.vy());
		vz.push_back(gentk.vz());
		dzError.push_back(gentk.dzError());

		charge.push_back(gentk.charge());

		double this_genMatchDR = -1;
		int this_genMatchID = 0;

		if(genParticles.isValid()) {
			for(const auto& genParticle : *genParticles) {
				if(!genParticle.isPromptFinalState() && !genParticle.isDirectPromptTauDecayProductFinalState()) {
					continue;
				}
				double dR = deltaR(gentk, genParticle);
				if(this_genMatchDR < 0 || dR < this_genMatchDR) {
					this_genMatchID = genParticle.pdgId();
					this_genMatchDR = dR;
				}
			}
		}

		genMatchDR.push_back(this_genMatchDR);
		genMatchID.push_back(this_genMatchID);
	}

	tree_->Fill();

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackCollectionAnalyzer);

#endif