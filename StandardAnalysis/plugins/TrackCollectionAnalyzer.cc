#ifndef TRACK_COLLECTION_ANALYZER
#define TRACK_COLLECTION_ANALYZER

#include "TTree.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TLorentzVector.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Framework/interface/stream/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "Geometry/RPCGeometry/interface/RPCGeometry.h"
#include "CondFormats/EcalObjects/interface/EcalChannelStatus.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "CondFormats/DataRecord/interface/EcalChannelStatusRcd.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

using namespace std;

class TrackCollectionAnalyzer : public edm::stream::EDAnalyzer<> {
public:
    explicit TrackCollectionAnalyzer(const edm::ParameterSet &);
    ~TrackCollectionAnalyzer();

private:
    void analyze(const edm::Event &, const edm::EventSetup &);

    const bool disappearingTrackSelection(const CandidateTrack &, 
                                          const reco::Vertex &,
                                          const vector<pat::Jet> &,
                                          const vector<pat::Electron> &,
                                          const vector<pat::Muon> &,
                                          const vector<pat::Tau> &,
                                          const double trackIso) const;

    const bool disappearingTrackSelection_Nm2(const CandidateTrack &track,
                                              const reco::Vertex &pv,
                                              const vector<pat::Jet> &jets,
                                              const vector<pat::Electron> &electrons,
                                              const vector<pat::Muon> &muons,
                                              const vector<pat::Tau> &taus) const;

    const double getTrackIsolation(const CandidateTrack &,
                                   const edm::Handle<vector<reco::Track> > &,
                                   const vector<pat::IsolatedTrack> &,
                                   const edm::Association<pat::PackedCandidateCollection> &,
                                   const edm::Association<pat::PackedCandidateCollection> &,
                                   const edm::Handle<pat::PackedCandidateCollection> &,   
                                   const edm::Handle<pat::PackedCandidateCollection> &,
                                   const bool,
                                   const bool) const;

    vector<pat::Electron> getTagElectrons(const edm::Event &event,
                                          const edm::TriggerResults &triggers,
                                          const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                          const reco::Vertex &vertex,
                                          const vector<pat::Electron> &electrons);

    vector<pat::Muon> getTagMuons(const edm::Event &event,
                                  const edm::TriggerResults &triggers,
                                  const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                  const reco::Vertex &vertex,
                                  const vector<pat::Muon> &muons);

    const bool isProbeTrack(const CandidateTrack& track, const double dRMinJet, const double trackIso) const;   

    bool isTagProbeElectron(const vector<pat::Electron> tagElectrons,
                            const vector<pat::Muon> tagMuons,
                            const pat::MET &met,
                            const vector<reco::Track> probeTracks) const;

    bool isTagProbeMuon(const vector<pat::Electron> tagElectrons,
                            const vector<pat::Muon> tagMuons,
                            const pat::MET &met,
                            const vector<reco::Track> probeTracks) const;

    const unsigned int isTagProbeElePair(const CandidateTrack &probe, const pat::Electron &tag) const;

    const unsigned int isTagProbeMuonPair(const CandidateTrack &probe, const pat::Muon &tag) const;

    const double MinDRtoJet(const vector<pat::Jet> &jets, const CandidateTrack &track) const;

    const double GetEcaloAOD(const CandidateTrack &track, const EBRecHitCollection &EBRecHits, const EERecHitCollection &EERecHits, const HBHERecHitCollection &HBHERecHits, double dR) const;

    const double GetECALMINIAOD(const CandidateTrack &track, const EcalRecHitCollection &miniEBRecHits, const EcalRecHitCollection & miniEERecHits, const double dR) const;
	
    const double GetHCALMINIAOD(const CandidateTrack &track, const HBHERecHitCollection & miniHBHERecHits, const HBHERecHitCollection & miniHCALRecHits, const double dR, bool eGamma) const;
    const double GetEcaloHFHO(const CandidateTrack &track, const HFRecHitCollection & miniHFRecHits, const HORecHitCollection & miniHORecHits, const double dR) const;   
    
    const double GetPFEnergy(const CandidateTrack &track, const edm::Handle<pat::PackedCandidateCollection> &packedCandidates, const int pdgID, const double dR) const;
    
    const math::XYZVector getPosition(const DetId& id) const;

    void getGeometries(const edm::EventSetup &setup);

    edm::InputTag candidateTracks_;
    edm::InputTag generalTracks_;
    edm::InputTag packedCandidates_;
    edm::InputTag lostTracks_;
    edm::InputTag isolatedTracks_;

    edm::InputTag gt2pc_;
    edm::InputTag gt2lt_;

    edm::InputTag genParticles_;

    edm::InputTag vertices_, electrons_, muons_, taus_, jets_;

    edm::InputTag triggers_;
    edm::InputTag trigObjs_;
    
    const string dataTakingPeriod_;

    edm::InputTag EBRecHits_, EERecHits_, ESRecHits_;
    edm::InputTag HBHERecHits_;

    edm::InputTag miniEBRecHits_, miniEERecHits_;

    edm::EDGetTokenT<vector<CandidateTrack> > candidateTracksToken_;
    edm::EDGetTokenT<vector<reco::Track> > generalTracksToken_;
    edm::EDGetTokenT<pat::PackedCandidateCollection> packedCandidatesToken_;
    edm::EDGetTokenT<pat::PackedCandidateCollection> lostTracksToken_;
    edm::EDGetTokenT<vector<pat::IsolatedTrack> > isolatedTracksToken_;

    edm::EDGetTokenT<edm::Association<pat::PackedCandidateCollection> > gt2pcToken_;
    edm::EDGetTokenT<edm::Association<pat::PackedCandidateCollection> > gt2ltToken_;

    edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

    edm::EDGetTokenT<vector<reco::Vertex> >  verticesToken_;
    edm::EDGetTokenT<vector<pat::Electron> > electronsToken_;
    edm::EDGetTokenT<vector<pat::Muon> >     muonsToken_;
    edm::EDGetTokenT<vector<pat::Tau> >      tausToken_;
    edm::EDGetTokenT<vector<pat::Jet> >      jetsToken_;

    edm::EDGetTokenT<edm::TriggerResults> triggersToken_;
    edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > trigObjsToken_;

    edm::EDGetTokenT<EBRecHitCollection>         EBRecHitsToken_;
    edm::EDGetTokenT<EERecHitCollection>         EERecHitsToken_;
    edm::EDGetTokenT<ESRecHitCollection>         ESRecHitsToken_;
    edm::EDGetTokenT<HBHERecHitCollection>       HBHERecHitsToken_;

    edm::EDGetTokenT<EcalRecHitCollection> miniEBRecHitsToken_;
    edm::EDGetTokenT<EcalRecHitCollection> miniEERecHitsToken_;
    
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)    
    edm::EDGetTokenT<EcalRecHitCollection> miniESRecHitsToken_;
    edm::EDGetTokenT<HBHERecHitCollection> miniHBHERecHitsToken_;
    edm::EDGetTokenT<HBHERecHitCollection> miniHCALRecHitsToken_;
    edm::EDGetTokenT<HFRecHitCollection> miniHFRecHitsToken_;
    edm::EDGetTokenT<HORecHitCollection> miniHORecHitsToken_;
#endif 

    const edm::ESGetToken<CaloGeometry, CaloGeometryRecord> caloGeomToken_;
    const edm::ESGetToken<CSCGeometry, MuonGeometryRecord> cscGeomToken_;
    const edm::ESGetToken<DTGeometry, MuonGeometryRecord> dtGeomToken_;
    const edm::ESGetToken<RPCGeometry, MuonGeometryRecord> rpcGeomToken_;

    const edm::ESGetToken<EcalChannelStatus, EcalChannelStatusRcd> ecalStatToken_;
    const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopoToken_;

    edm::ESHandle<CaloGeometry> caloGeometry_;
    edm::ESHandle<CSCGeometry>  cscGeometry_;
    edm::ESHandle<DTGeometry>   dtGeometry_;
    edm::ESHandle<RPCGeometry>  rpcGeometry_;

    edm::ESHandle<EcalChannelStatus> ecalStatus_;
    edm::ESHandle<TrackerTopology> trackerTopology_;

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0) 
    edm::InputTag miniESRecHits_;
    edm::InputTag miniHBHERecHits_, miniHCALRecHits_, miniHFRecHits_, miniHORecHits_;
#endif

    edm::Service<TFileService> fs_;
    TTree * tree_;

    vector<bool> isInPackedCandidates;
    vector<bool> isInLostTracks;
    vector<bool> isInIsolatedTracks;
    vector<int> TagProbeElectron;
    vector<int> TagProbeMuon;

    vector<double> pt, eta, phi;
    vector<double> vx, vy, vz;
    vector<double> d0Error, dzError;
    vector<int> charge;

    vector<double> trackIsoNoPUDRp3;
    vector<double> trackIsoNoPUDRp3_aodOnly;

    vector<bool> passesSelection;

    vector<double> genMatchDR;
    vector<int> genMatchID;

    bool is2017_;
    bool hcalRecHits_;

    vector<double> ecaloDR0p5;
    vector<double> ecaloDR0p3;
    vector<double> ecaloDR0p7;

    vector<double> miniECALDR0p3;
    vector<double> miniECALDR0p5;
    vector<double> miniECALDR0p7;

    vector<double> miniHCALDR0p3;
    vector<double> miniHCALDR0p5;
    vector<double> miniHCALDR0p7;

    vector<double> miniHBHEDR0p3;
    vector<double> miniHBHEDR0p5;
    vector<double> miniHBHEDR0p7;

    vector<double> miniEcaloHFHO;

    vector<double> pcEDR0p3;
    vector<double> pcEDR0p5;
    vector<double> pcEDR0p7;

    vector<double> pcEDR0p5_quark;
    vector<double> pcEDR0p5_gamma;
    vector<double> pcEDR0p5_pi;
    vector<double> pcEDR0p5_WZ;
    vector<double> pcEDR0p5_mu;
    vector<double> pcEDR0p5_ele;

    vector<double> dRToClosestTagElectron;
    vector<double> dRToClosestElectron;

    vector<double> dRToClosestTagMuon;
    vector<double> dRToClosestMuon;
    
    vector<int> disTracks;
};

TrackCollectionAnalyzer::TrackCollectionAnalyzer(const edm::ParameterSet &cfg) :
    candidateTracks_ (cfg.getParameter<edm::InputTag>("candidateTracks")),
    generalTracks_   (cfg.getParameter<edm::InputTag>("generalTracks")),
    packedCandidates_(cfg.getParameter<edm::InputTag>("packedCandidates")),
    lostTracks_      (cfg.getParameter<edm::InputTag>("lostTracks")),
    isolatedTracks_  (cfg.getParameter<edm::InputTag>("isolatedTracks")),
    gt2pc_           (cfg.getParameter<edm::InputTag>("packedCandidates")),
    gt2lt_           (cfg.getParameter<edm::InputTag>("lostTracks")),
    genParticles_    (cfg.getParameter<edm::InputTag>("genParticles")),
    vertices_        (cfg.getParameter<edm::InputTag>("vertices")),
    electrons_       (cfg.getParameter<edm::InputTag>("electrons")),
    muons_           (cfg.getParameter<edm::InputTag>("muons")),
    taus_            (cfg.getParameter<edm::InputTag>("taus")),
    jets_            (cfg.getParameter<edm::InputTag>("jets")),
    triggers_     (cfg.getParameter<edm::InputTag> ("triggers")),
    trigObjs_     (cfg.getParameter<edm::InputTag> ("triggerObjects")),
    dataTakingPeriod_ (cfg.getParameter<string> ("dataTakingPeriod")),
    EBRecHits_     (cfg.getParameter<edm::InputTag> ("EBRecHits")),
    EERecHits_     (cfg.getParameter<edm::InputTag> ("EERecHits")),
    ESRecHits_     (cfg.getParameter<edm::InputTag> ("ESRecHits")),
    HBHERecHits_   (cfg.getParameter<edm::InputTag> ("HBHERecHits")),
    miniEBRecHits_ (cfg.getParameter<edm::InputTag> ("miniEBRecHits")),
    miniEERecHits_ (cfg.getParameter<edm::InputTag> ("miniEERecHits")),
    caloGeomToken_(esConsumes<CaloGeometry, CaloGeometryRecord>()),
    cscGeomToken_(esConsumes<CSCGeometry, MuonGeometryRecord>()),
    dtGeomToken_(esConsumes<DTGeometry, MuonGeometryRecord>()),
    rpcGeomToken_(esConsumes<RPCGeometry, MuonGeometryRecord>()),
    ecalStatToken_(esConsumes<EcalChannelStatus, EcalChannelStatusRcd>()),
    trackerTopoToken_(esConsumes<TrackerTopology, TrackerTopologyRcd>())
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)
        ,
        miniESRecHits_ (cfg.getParameter<edm::InputTag> ("miniESRecHits")),
        miniHBHERecHits_ (cfg.getParameter<edm::InputTag> ("miniHBHERecHits")),
        miniHCALRecHits_ (cfg.getParameter<edm::InputTag> ("miniHCALRecHits")),
        miniHFRecHits_ (cfg.getParameter<edm::InputTag> ("miniHFRecHits")),
        miniHORecHits_ (cfg.getParameter<edm::InputTag> ("miniHORecHits"))
#endif
{
    //assert(dataTakingPeriod_ == "2017" || dataTakingPeriod_ == "2018");
    is2017_ = (dataTakingPeriod_ == "2017");

    triggersToken_     = consumes<edm::TriggerResults>           (triggers_);
    trigObjsToken_     = consumes<vector<pat::TriggerObjectStandAlone> > (trigObjs_);
    candidateTracksToken_  = consumes<vector<CandidateTrack> >       (candidateTracks_);
    generalTracksToken_    = consumes<vector<reco::Track> >          (generalTracks_);
    packedCandidatesToken_ = consumes<pat::PackedCandidateCollection>(packedCandidates_);
    lostTracksToken_       = consumes<pat::PackedCandidateCollection>(lostTracks_);
    isolatedTracksToken_   = consumes<vector<pat::IsolatedTrack> >   (isolatedTracks_);

    gt2pcToken_ = consumes<edm::Association<pat::PackedCandidateCollection> >(gt2pc_);
    gt2ltToken_ = consumes<edm::Association<pat::PackedCandidateCollection> >(gt2lt_);

    genParticlesToken_ = consumes<vector<reco::GenParticle> >(genParticles_);

    verticesToken_     = consumes<vector<reco::Vertex> > (vertices_);
    electronsToken_    = consumes<vector<pat::Electron> >(electrons_);
    muonsToken_        = consumes<vector<pat::Muon> >    (muons_);
    tausToken_         = consumes<vector<pat::Tau> >     (taus_);
    jetsToken_         = consumes<vector<pat::Jet> >     (jets_);

    EBRecHitsToken_     = consumes<EBRecHitCollection>       (EBRecHits_);
    EERecHitsToken_     = consumes<EERecHitCollection>       (EERecHits_);
    ESRecHitsToken_     = consumes<ESRecHitCollection>       (ESRecHits_);
    HBHERecHitsToken_   = consumes<HBHERecHitCollection>     (HBHERecHits_);

    miniEBRecHitsToken_ = consumes<EcalRecHitCollection> (miniEBRecHits_);
    miniEERecHitsToken_ = consumes<EcalRecHitCollection> (miniEERecHits_);
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)        
    miniESRecHitsToken_ = consumes<EcalRecHitCollection> (miniESRecHits_);
    miniHBHERecHitsToken_ = consumes<HBHERecHitCollection> (miniHBHERecHits_);
    miniHCALRecHitsToken_ = consumes<HBHERecHitCollection> (miniHCALRecHits_);
    miniHFRecHitsToken_ = consumes<HFRecHitCollection> (miniHFRecHits_);
    miniHORecHitsToken_ = consumes<HORecHitCollection> (miniHORecHits_);    
#endif    
    
    tree_ = fs_->make<TTree>("tree", "tree");

    tree_->Branch("isInPackedCandidates", &isInPackedCandidates);
    tree_->Branch("isInLostTracks", &isInLostTracks);
    tree_->Branch("isInIsolatedTracks", &isInIsolatedTracks);
    tree_->Branch("isTagProbeElectron", &TagProbeElectron);
    tree_->Branch("isTagProbeMuon", &TagProbeMuon);

    tree_->Branch("pt", &pt);
    tree_->Branch("eta", &eta);
    tree_->Branch("phi", &phi);

    tree_->Branch("vx", &vx);
    tree_->Branch("vy", &vy);
    tree_->Branch("vz", &vz);
    tree_->Branch("d0Error", &d0Error);
    tree_->Branch("dzError", &dzError);

    tree_->Branch("charge", &charge);

    tree_->Branch("trackIsoNoPUDRp3", &trackIsoNoPUDRp3);
    tree_->Branch("trackIsoNoPUDRp3_aodOnly", &trackIsoNoPUDRp3_aodOnly);

    tree_->Branch("passesSelection", &passesSelection);

    tree_->Branch("genMatchDR", &genMatchDR);
    tree_->Branch("genMatchID", &genMatchID);

    tree_->Branch("ecaloDR0p3", &ecaloDR0p3);
    tree_->Branch("ecaloDR0p5", &ecaloDR0p5);
    tree_->Branch("ecaloDR0p7", &ecaloDR0p7);

    tree_->Branch("miniECALDR0p3", &miniECALDR0p3);
    tree_->Branch("miniECALDR0p5", &miniECALDR0p5);
    tree_->Branch("miniECALDR0p7", &miniECALDR0p7);

    tree_->Branch("miniHCALDR0p3", &miniHCALDR0p3);
    tree_->Branch("miniHCALDR0p5", &miniHCALDR0p5);
    tree_->Branch("miniHCALDR0p7", &miniHCALDR0p7);

    tree_->Branch("miniHBHEDR0p3", &miniHBHEDR0p3);
    tree_->Branch("miniHBHEDR0p5", &miniHBHEDR0p5);
    tree_->Branch("miniHBHEDR0p7", &miniHBHEDR0p7);

    tree_->Branch("miniEcaloHFHO", &miniEcaloHFHO);

    tree_->Branch("pcEDR0p3", &pcEDR0p3);
    tree_->Branch("pcEDR0p5", &pcEDR0p5);
    tree_->Branch("pcEDR0p7", &pcEDR0p7);

    tree_->Branch("pcEDR0p5_ele", &pcEDR0p5_ele);
    tree_->Branch("pcEDR0p5_mu", &pcEDR0p5_mu);
    tree_->Branch("pcEDR0p5_pi", &pcEDR0p5_pi);
    tree_->Branch("pcEDR0p5_WZ", &pcEDR0p5_WZ);
    tree_->Branch("pcEDR0p5_gamma", &pcEDR0p5_gamma);
    tree_->Branch("pcEDR0p5_quark", &pcEDR0p5_quark);


    tree_->Branch("deltaRToClosestTagElectron", &dRToClosestTagElectron);
    tree_->Branch("deltaRToClosestElectron", &dRToClosestElectron);

    tree_->Branch("deltaRToClosestTagMuon", &dRToClosestTagMuon);
    tree_->Branch("deltaRToClosestMuon", &dRToClosestMuon);

    tree_->Branch("disTracks", &disTracks);
}

TrackCollectionAnalyzer::~TrackCollectionAnalyzer() 
{
}

void TrackCollectionAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
    edm::Handle<edm::TriggerResults> triggers;
    edm::Handle<vector<pat::TriggerObjectStandAlone> > trigObjs;
    edm::Handle<vector<CandidateTrack> >        candidateTracks;
    edm::Handle<vector<reco::Track> >           generalTracks;
    edm::Handle<pat::PackedCandidateCollection> packedCandidates;   
    edm::Handle<pat::PackedCandidateCollection> lostTracks; 
    edm::Handle<vector<pat::IsolatedTrack> >    isolatedTracks;

    edm::Handle<edm::Association<pat::PackedCandidateCollection> > gt2pc;
    edm::Handle<edm::Association<pat::PackedCandidateCollection> > gt2lt;

    edm::Handle<vector<reco::GenParticle> > genParticles;

    edm::Handle<vector<reco::Vertex> > vertices;
    edm::Handle<vector<pat::Electron> > electrons;
    edm::Handle<vector<pat::Muon> > muons;
    edm::Handle<vector<pat::Tau> > taus;
    edm::Handle<vector<pat::Jet> > jets;

    edm::Handle<EBRecHitCollection> EBRecHits;
    edm::Handle<EERecHitCollection> EERecHits;
    edm::Handle<ESRecHitCollection> ESRecHits;
    edm::Handle<HBHERecHitCollection> HBHERecHits;

    edm::Handle<EcalRecHitCollection> miniEERecHits;
    edm::Handle<EcalRecHitCollection> miniEBRecHits;

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)        
    edm::Handle<EcalRecHitCollection> miniESRecHits;
    edm::Handle<HBHERecHitCollection> miniHBHERecHits;
    edm::Handle<HBHERecHitCollection> miniHCALRecHits;
    edm::Handle<HFRecHitCollection> miniHFRecHits;
    edm::Handle<HORecHitCollection> miniHORecHits;
#endif

    event.getByToken (triggersToken_, triggers);
    event.getByToken (trigObjsToken_, trigObjs);
    event.getByToken(candidateTracksToken_,  candidateTracks);
    event.getByToken(generalTracksToken_,    generalTracks);
    event.getByToken(packedCandidatesToken_, packedCandidates);
    event.getByToken(lostTracksToken_,       lostTracks);
    event.getByToken(isolatedTracksToken_,   isolatedTracks);

    event.getByToken(gt2pcToken_, gt2pc);
    event.getByToken(gt2ltToken_, gt2lt);

    event.getByToken(genParticlesToken_, genParticles);

    event.getByToken(verticesToken_, vertices);
    event.getByToken(electronsToken_, electrons);
    event.getByToken(muonsToken_, muons);
    event.getByToken(tausToken_, taus);
    event.getByToken(jetsToken_, jets);

    event.getByToken(EBRecHitsToken_, EBRecHits);
    event.getByToken(EERecHitsToken_, EERecHits);
    event.getByToken(ESRecHitsToken_, ESRecHits);
    event.getByToken(HBHERecHitsToken_, HBHERecHits);

    event.getByToken(miniEERecHitsToken_, miniEERecHits);
    event.getByToken(miniEBRecHitsToken_, miniEBRecHits);

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)        
    event.getByToken(miniESRecHitsToken_, miniESRecHits);
    event.getByToken(miniHBHERecHitsToken_, miniHBHERecHits);
    event.getByToken(miniHCALRecHitsToken_, miniHCALRecHits);
    event.getByToken(miniHFRecHitsToken_, miniHFRecHits);
    event.getByToken(miniHORecHitsToken_, miniHORecHits);
#endif

    isInPackedCandidates.clear();
    isInLostTracks.clear();
    isInIsolatedTracks.clear();
    TagProbeElectron.clear();
    TagProbeMuon.clear();

    pt.clear();
    eta.clear();
    phi.clear();

    vx.clear();
    vy.clear();
    vz.clear();
    d0Error.clear();
    dzError.clear();

    charge.clear();

    trackIsoNoPUDRp3.clear();
    trackIsoNoPUDRp3_aodOnly.clear();

    passesSelection.clear();

    genMatchDR.clear();
    genMatchID.clear();

    ecaloDR0p3.clear();
    ecaloDR0p5.clear();
    ecaloDR0p7.clear();

    miniECALDR0p3.clear();
    miniECALDR0p5.clear();
    miniECALDR0p7.clear();

    miniHCALDR0p3.clear();
    miniHCALDR0p5.clear();
    miniHCALDR0p7.clear();

    miniHBHEDR0p3.clear();
    miniHBHEDR0p5.clear();
    miniHBHEDR0p7.clear();

    miniEcaloHFHO.clear();

    pcEDR0p3.clear();
    pcEDR0p5.clear();
    pcEDR0p7.clear();

    pcEDR0p5_ele.clear();
    pcEDR0p5_mu.clear();
    pcEDR0p5_gamma.clear();
    pcEDR0p5_WZ.clear();
    pcEDR0p5_quark.clear();
    pcEDR0p5_pi.clear();

    dRToClosestTagElectron.clear();
    dRToClosestElectron.clear();

    dRToClosestTagMuon.clear();
    dRToClosestMuon.clear();

    disTracks.clear();

    getGeometries(setup);

    //bool saveEvent = false;

    const reco::Vertex &pv = vertices->at(0);

    vector<pat::Electron> tagElectrons = getTagElectrons(event, *triggers, *trigObjs, pv, *electrons);
    vector<pat::Muon> tagMuons = getTagMuons(event, *triggers, *trigObjs, pv, *muons);


    for(const auto &track : *candidateTracks) {

        if(track.pt() < 20) continue;

        double dRMinJet = MinDRtoJet(*jets, track);

        double trackIso = 0.0;
        for(const auto &t : *candidateTracks) {
            if(fabs(track.dz(t.vertex())) > 3.0 * hypot(track.dzError(), t.dzError())) continue;
            double dR = deltaR(track, t);
            if(dR < 0.3 && dR > 1.0e-12) trackIso += t.pt();
        }

        bool this_inPackedCandidates = false;
        for(const auto& pc : *packedCandidates) {
            double dR = deltaR(track, pc);
            if(dR < 0.001) {
                this_inPackedCandidates = true;
                break;
            }
        }
        isInPackedCandidates.push_back(this_inPackedCandidates);

        bool this_inLostTracks = false;
        for(const auto& lt : *lostTracks) {
            double dR = deltaR(track, lt);
            if(dR < 0.001) {
                this_inLostTracks = true;
                break;
            }
        }
        isInLostTracks.push_back(this_inLostTracks);

        bool this_isInIsolatedTracks = false;
        for(const auto& isoTrack : *isolatedTracks) {
            double dR = deltaR(track, isoTrack);
            if(dR < 0.001) {
                this_isInIsolatedTracks = true;
                break;
            }
        }
        isInIsolatedTracks.push_back(this_isInIsolatedTracks);

        pt.push_back(track.pt());
        eta.push_back(track.eta());
        phi.push_back(track.phi());

        vx.push_back(track.vx());
        vy.push_back(track.vy());
        vz.push_back(track.vz());
        d0Error.push_back(track.d0Error());
        dzError.push_back(track.dzError());

        charge.push_back(track.charge());

        trackIsoNoPUDRp3.push_back(
            getTrackIsolation(track,
                              generalTracks,
                              *isolatedTracks,
                              *gt2pc,
                              *gt2lt,
                              packedCandidates,
                              lostTracks,
                              true, true));
;
            
        trackIsoNoPUDRp3_aodOnly.push_back(
            getTrackIsolation(track,
                              generalTracks,
                              *isolatedTracks,
                              *gt2pc,
                              *gt2lt,
                              packedCandidates,
                              lostTracks,
                              true, false));

        bool trackPassesSelection = disappearingTrackSelection(track, vertices->at(0), *jets, *electrons, *muons, *taus, trackIso);
      
        passesSelection.push_back(trackPassesSelection);

        if(track.pt()  < 55) {
            disTracks.push_back(1);
            std::cout << "Track pt: " << track.pt() << std::endl;
        }
        else if(fabs(track.eta()) > 2.1){
            std::cout << "Track eta: " << track.eta() << std::endl;
            disTracks.push_back(2);
        }
        else if(fabs(track.dz()) > 0.5 && fabs(M_PI_2 - track.theta()) > 1.0e-3){
            std::cout << "track dz: " << track.dz() << std::endl;
            disTracks.push_back(3);
        }
        else if(fabs(track.eta()) >= 1.42 && fabs(track.eta()) <= 1.65){
            std::cout << "bad eta region" << std::endl;
            disTracks.push_back(4);
        }
        else if(fabs(track.eta()) >= 0.15 && fabs(track.eta()) <= 0.35){
            std::cout << "bad eta region" << std::endl;
            disTracks.push_back(5);
        }
        else if(fabs(track.eta()) >= 1.55 && fabs(track.eta()) <= 1.85){
            std::cout << "bad eta region" << std::endl;
            disTracks.push_back(6);
        }
        else if(track.hitPattern().numberOfValidPixelHits() < 4){
            std::cout << "Pixel hits: " << track.hitPattern().numberOfValidPixelHits() << std::endl;
            disTracks.push_back(7);
        }
        else if(track.hitPattern().numberOfValidHits() < 4){
            std::cout << "Valid hits: " << track.hitPattern().numberOfValidHits() << std::endl;
            disTracks.push_back(8);
        }
        else if(track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) != 0){
            std::cout << "Missing inner hits: " << track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) << std::endl;
            disTracks.push_back(9);
        }
        else if(track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) != 0){
            std::cout << "Missing middle hits: " << track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) << std::endl;
            disTracks.push_back(10);
        }
        else if(trackIso / track.pt() >= 0.05){
            std::cout << "Track iso: " << trackIso / track.pt() << std::endl;
            disTracks.push_back(11);
        }
        else if(fabs(((track.vx() - pv.x()) * track.py() - (track.vy() - pv.y()) * track.px()) / track.pt()) >= 0.02){
            std::cout << "Track d0: " << fabs(((track.vx() - pv.x()) * track.py() - (track.vy() - pv.y()) * track.px()) / track.pt()) << std::endl;
            disTracks.push_back(12);
        }
        else if(fabs(track.vz() - pv.z() -((track.vx() - pv.x()) * track.px() + (track.vy() - pv.y()) * track.py()) * track.pz() / track.pt() / track.pt()) >= 0.5){
            std::cout << "Track dz: " << fabs(track.vz() - pv.z() - ((track.vx() - pv.x()) * track.px() + (track.vy() - pv.y()) * track.py()) * track.pz() / track.pt() / track.pt()) << std::endl;
            disTracks.push_back(13);
        }
        else{
            std::cout << "Track passes first round of disappearing track selection " << std::endl;
            disTracks.push_back(14);
        }

        //if(trackPassesSelection) saveEvent = true; 

        double this_genMatchDR = -1;
        int this_genMatchID = 0;

        if(genParticles.isValid()) {
            for(const auto& genParticle : *genParticles) {
                if(!genParticle.isPromptFinalState() && !genParticle.isDirectPromptTauDecayProductFinalState()) {
                    continue;
                }
                double dR = deltaR(track, genParticle);
                if(this_genMatchDR < 0 || dR < this_genMatchDR) {
                    this_genMatchID = genParticle.pdgId();
                    this_genMatchDR = dR;
                }
            }
        }

        double deltaRToClosestTagElectron = -1;
        int track_isProbeEleTrack = 0b00;
        //if(isProbeTrack(track, dRMinJet, trackIso)) {
          for(const auto &tag : tagElectrons) {
            double thisDR = deltaR(tag, track);
            if(deltaRToClosestTagElectron < 0 || thisDR < deltaRToClosestTagElectron) {
              deltaRToClosestTagElectron = thisDR;
            }
            track_isProbeEleTrack |= isTagProbeElePair(track, tag);
            if(track_isProbeEleTrack != 0b00) break;
            //if(track_isProbeTrack == 0b01 || track_isProbeTrack == 0b10) saveEvent = true;
            //track.isTagProbeTauToElectron |= isTagProbeTauToElePair(track, tag, met);
          }
        //}

        double deltaRToClosestElectron = -1;
        for(const auto &electron : *electrons) {
           double thisDR = deltaR(electron, track);
           if(deltaRToClosestElectron < 0 || thisDR < deltaRToClosestElectron) deltaRToClosestElectron = thisDR;
        }
        
        dRToClosestTagElectron.push_back(deltaRToClosestTagElectron);
        dRToClosestElectron.push_back(deltaRToClosestElectron);

        double deltaRToClosestTagMuon = -1;
        int track_isProbeMuonTrack = 0b00;
        //if(isProbeTrack(track, dRMinJet, trackIso)) {
          for(const auto &tag : tagMuons) {
            double thisDR = deltaR(tag, track);
            if(deltaRToClosestTagMuon < 0 || thisDR < deltaRToClosestTagMuon) {
              deltaRToClosestTagMuon = thisDR;
            }
            track_isProbeMuonTrack |= isTagProbeMuonPair(track, tag);
            if(track_isProbeMuonTrack != 0b00) break;
          }

        double deltaRToClosestMuon = -1;
        for(const auto &muon : *muons) {
           double thisDR = deltaR(muon, track);
           if(deltaRToClosestMuon < 0 || thisDR < deltaRToClosestMuon) deltaRToClosestMuon = thisDR;
        }
        
        dRToClosestTagMuon.push_back(deltaRToClosestTagMuon);
        dRToClosestMuon.push_back(deltaRToClosestMuon);


        ecaloDR0p3.push_back(GetEcaloAOD(track, *EBRecHits, *EERecHits, *HBHERecHits, 0.3));
        ecaloDR0p5.push_back(GetEcaloAOD(track, *EBRecHits, *EERecHits, *HBHERecHits, 0.5));
        ecaloDR0p7.push_back(GetEcaloAOD(track, *EBRecHits, *EERecHits, *HBHERecHits, 0.7));

        miniECALDR0p3.push_back(GetECALMINIAOD(track, *miniEBRecHits, *miniEERecHits, 0.3));
        miniECALDR0p5.push_back(GetECALMINIAOD(track, *miniEBRecHits, *miniEERecHits, 0.5));
        miniECALDR0p7.push_back(GetECALMINIAOD(track, *miniEBRecHits, *miniEERecHits, 0.7));

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)    
        miniHBHEDR0p3.push_back(GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.3, true));
        miniHBHEDR0p5.push_back(GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.5, true));
        miniHBHEDR0p7.push_back(GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.7, true));

        miniHCALDR0p3.push_back(GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.3, false));
        miniHCALDR0p5.push_back(GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.5, false));
        miniHCALDR0p7.push_back(GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.7, false));

        std::cout << "HCAL: " << GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.5, true) << " " << GetHCALMINIAOD(track, *miniHBHERecHits, *miniHCALRecHits, 0.5, false) << std::endl;

        miniEcaloHFHO.push_back(GetEcaloHFHO(track, *miniHFRecHits, *miniHORecHits, 0.5));
#endif

        pcEDR0p3.push_back(GetPFEnergy(track, packedCandidates, -1, 0.3));
        pcEDR0p5.push_back(GetPFEnergy(track, packedCandidates, -1, 0.5));
        pcEDR0p7.push_back(GetPFEnergy(track, packedCandidates, -1, 0.7));

        pcEDR0p5_ele.push_back(GetPFEnergy(track, packedCandidates, 11, 0.5));
        pcEDR0p5_mu.push_back(GetPFEnergy(track, packedCandidates, 13, 0.5));
        pcEDR0p5_pi.push_back(GetPFEnergy(track, packedCandidates, 211, 0.5));
        pcEDR0p5_gamma.push_back(GetPFEnergy(track, packedCandidates, 22, 0.5));
        pcEDR0p5_WZ.push_back(GetPFEnergy(track, packedCandidates, 23, 0.5));
        pcEDR0p5_quark.push_back(GetPFEnergy(track, packedCandidates, 1, 0.5));

        TagProbeElectron.push_back(track_isProbeEleTrack);
        TagProbeMuon.push_back(track_isProbeMuonTrack);

        genMatchDR.push_back(this_genMatchDR);
        genMatchID.push_back(this_genMatchID);
    }

    //if(saveEvent) tree_->Fill();
    
    tree_->Fill();

}

const bool 
TrackCollectionAnalyzer::disappearingTrackSelection(
    const CandidateTrack        &track, 
    const reco::Vertex          &pv,
    const vector<pat::Jet>      &jets,
    const vector<pat::Electron> &electrons,
    const vector<pat::Muon>     &muons,
    const vector<pat::Tau>      &taus,
    const double trackIso) const {

    // d0 wrt pv (2d) = (vertex - pv) cross p / |p|
    double d0 = ((track.vx() - pv.x()) * track.py() - (track.vy() - pv.y()) * track.px()) / track.pt(); 
  
    // dz wrt pv (2d) = (v_z - pv_z) - p_z * [(vertex - pv) dot p / |p|^2]
    double dz = track.vz() - pv.z() -
      ((track.vx() - pv.x()) * track.px() + (track.vy() - pv.y()) * track.py()) * track.pz() / track.pt() / track.pt();

    bool passes = (track.pt() > 55 &&
                   fabs(track.eta()) < 2.1 &&
                   // skip fiducial selections
                   !(fabs(track.dz()) < 0.5 && fabs(M_PI_2 - track.theta()) < 1.0e-3) &&
                   !(fabs(track.eta()) >= 1.42 && fabs(track.eta()) <= 1.65) &&
                   !(fabs(track.eta()) >= 0.15 && fabs(track.eta()) <= 0.35) &&
                   !(fabs(track.eta()) >= 1.55 && fabs(track.eta()) <= 1.85) &&
                   track.hitPattern().numberOfValidPixelHits() >= 4 &&
                   track.hitPattern().numberOfValidHits() >= 4 &&
                   track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                   track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                   // track isolation under study
                   trackIso / track.pt() < 0.05 &&
                   fabs(d0) < 0.02 &&
                   fabs(dz) < 0.5);
    
    if(!passes) return false;

    std::cout << "Track passes first disappearing track selections" << std::endl;

    double deltaRToClosestElectron = -1;
    for(const auto &electron : electrons) {
      double thisDR = deltaR(electron, track);
      if(deltaRToClosestElectron < 0 || thisDR < deltaRToClosestElectron) deltaRToClosestElectron = thisDR;
    }
    //if(fabs(deltaRToClosestElectron) <= 0.15) return false;

    double deltaRToClosestMuon = -1;
    for(const auto &muon : muons) {
      double thisDR = deltaR(muon, track);
      if(deltaRToClosestMuon < 0 || thisDR < deltaRToClosestMuon) deltaRToClosestMuon = thisDR;
    }
    //if(fabs(deltaRToClosestMuon) <= 0.15) return false;

    double deltaRToClosestTauHad = -1;
    for(const auto &tau : taus) {
      if(tau.isTauIDAvailable("againstElectronLooseMVA5")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA5") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else if(tau.isTauIDAvailable("againstElectronLooseMVA6")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA6") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else {
        continue;
      }

      double thisDR = deltaR(tau, track);
      if(deltaRToClosestTauHad < 0 || thisDR < deltaRToClosestTauHad) deltaRToClosestTauHad = thisDR;
    }
    if(fabs(deltaRToClosestTauHad) <= 0.15) return false;

    double dRMinJet = -1;
    for(const auto &jet : jets) {
      if(jet.pt() > 30 &&
         fabs(jet.eta()) < 4.5 &&
         anatools::jetPassesTightLepVeto(jet) // This automatically uses the correct jet ID criteria
        ) {
        double dR = deltaR(track, jet);
        if(dRMinJet < 0 || dR < dRMinJet) dRMinJet = dR;
      }
    }
    if(fabs(dRMinJet) <= 0.5) return false;

    if(track.missingOuterHits_() < 3) return false;
    if(track.hitPattern().trackerLayersWithMeasurement() < 4) return false;

    return true;
}

const bool 
TrackCollectionAnalyzer::disappearingTrackSelection_Nm2(
    const CandidateTrack        &track, 
    const reco::Vertex          &pv,
    const vector<pat::Jet>      &jets,
    const vector<pat::Electron> &electrons,
    const vector<pat::Muon>     &muons,
    const vector<pat::Tau>      &taus) const {

    // d0 wrt pv (2d) = (vertex - pv) cross p / |p|
    double d0 = ((track.vx() - pv.x()) * track.py() - (track.vy() - pv.y()) * track.px()) / track.pt(); 
  
    // dz wrt pv (2d) = (v_z - pv_z) - p_z * [(vertex - pv) dot p / |p|^2]
    double dz = track.vz() - pv.z() -
      ((track.vx() - pv.x()) * track.px() + (track.vy() - pv.y()) * track.py()) * track.pz() / track.pt() / track.pt();

    bool passes = (track.pt() > 55 &&
                   fabs(track.eta()) < 2.1 &&
                   // skip fiducial selections
                   !(fabs(track.dz()) < 0.5 && fabs(M_PI_2 - track.theta()) < 1.0e-3) &&
                   !(fabs(track.eta()) >= 1.42 && fabs(track.eta()) <= 1.65) &&
                   !(fabs(track.eta()) >= 0.15 && fabs(track.eta()) <= 0.35) &&
                   !(fabs(track.eta()) >= 1.55 && fabs(track.eta()) <= 1.85) &&
                   track.hitPattern().numberOfValidPixelHits() >= 4 &&
                   track.hitPattern().numberOfValidHits() >= 4 &&
                   track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                   track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                   //track.missingInnerHits_() == 0 &&
                   //track.missingMiddleHits_() == 0 &&
                   // track isolation under study
                   fabs(d0) < 0.02 &&
                   fabs(dz) < 0.5);

    if(!passes) return false;

    double deltaRToClosestElectron = -1;
    for(const auto &electron : electrons) {
      double thisDR = deltaR(electron, track);
      if(deltaRToClosestElectron < 0 || thisDR < deltaRToClosestElectron) deltaRToClosestElectron = thisDR;
    }
    //if(fabs(deltaRToClosestElectron) <= 0.15) return false;

    double deltaRToClosestMuon = -1;
    for(const auto &muon : muons) {
      double thisDR = deltaR(muon, track);
      if(deltaRToClosestMuon < 0 || thisDR < deltaRToClosestMuon) deltaRToClosestMuon = thisDR;
    }
    if(fabs(deltaRToClosestMuon) <= 0.15) return false;

    double deltaRToClosestTauHad = -1;
    for(const auto &tau : taus) {
      if(tau.isTauIDAvailable("againstElectronLooseMVA5")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA5") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else if(tau.isTauIDAvailable("againstElectronLooseMVA6")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA6") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else {
        continue;
      }

      double thisDR = deltaR(tau, track);
      if(deltaRToClosestTauHad < 0 || thisDR < deltaRToClosestTauHad) deltaRToClosestTauHad = thisDR;
    }
    if(fabs(deltaRToClosestTauHad) <= 0.15) return false;

    double dRMinJet = -1;
    for(const auto &jet : jets) {
      if(jet.pt() > 30 &&
         fabs(jet.eta()) < 4.5 &&
         anatools::jetPassesTightLepVeto(jet) // This automatically uses the correct jet ID criteria
        ) {
        double dR = deltaR(track, jet);
        if(dRMinJet < 0 || dR < dRMinJet) dRMinJet = dR;
      }
    }
    if(fabs(dRMinJet) <= 0.5) return false;

    //if(track.missingOuterHits_() < 3) return false;
    if(track.hitPattern().trackerLayersWithMeasurement() < 4) return false;

    return true;
}


const double
TrackCollectionAnalyzer::getTrackIsolation(
    const CandidateTrack &track,
    const edm::Handle<vector<reco::Track> > &allTracks,
    const vector<pat::IsolatedTrack> &isolatedTracks,
    const edm::Association<pat::PackedCandidateCollection> &gt2pc,
    const edm::Association<pat::PackedCandidateCollection> &gt2lt,
    const edm::Handle<pat::PackedCandidateCollection> &packedCandidates,
    const edm::Handle<pat::PackedCandidateCollection> &lostTracks,
    const bool noPU,
    const bool allowAnything) const
{
    double sumPt = 0.0;

    for(unsigned int i = 0; i < allTracks->size(); i++) {
        const reco::Track &gentk = (*allTracks)[i];
        if(noPU && fabs(track.dz(gentk.vertex())) > 3.0 * hypot(track.dzError(), gentk.dzError())) continue;

        if(!allowAnything) {
            edm::Ref<vector<reco::Track> > gentkref = edm::Ref<vector<reco::Track> >(allTracks, i);

            pat::PackedCandidateRef pcref = gt2pc[gentkref];
            pat::PackedCandidateRef ltref = gt2lt[gentkref];

            const pat::PackedCandidate &pfCand    = *(pcref.get());
            const pat::PackedCandidate &lostTrack = *(ltref.get());

            if(pcref.isNonnull() && pcref.id() == packedCandidates.id() && pfCand.charge() != 0) continue;
            if(ltref.isNonnull() && ltref.id() == lostTracks.id() && lostTrack.charge() != 0) continue;

            bool this_isInIsolatedTracks = false;
            for(const auto& isoTrack : isolatedTracks) {
                double dR = deltaR(gentk, isoTrack);
                if(dR < 0.001) {
                    this_isInIsolatedTracks = true;
                    break;
                }
            }
            if(this_isInIsolatedTracks) continue;
        }

        double dR = deltaR(track, gentk);
        if(dR < 0.3 && dR > 1.0e-12) sumPt += gentk.pt ();
    }

    return sumPt;
}

bool
TrackCollectionAnalyzer::isTagProbeMuon(const vector<pat::Electron> tagElectrons,
                                     const vector<pat::Muon> tagMuons,
                                     const pat::MET &met,
                                     const vector<reco::Track> probeTracks) const
{
  // cutTrkMuonVeto
  // cutTrkTauHadVeto
  // cutTrkEcalo

  for(const auto &muon : tagMuons) {
    TLorentzVector t(muon.px(), muon.py(), muon.pz(), muon.energy());
    for(const auto &track : probeTracks) {
      TLorentzVector p(track.px(), 
                       track.py(), 
                       track.pz(), 
                       sqrt(track.px() * track.px() + 
                            track.py() * track.py() + 
                            track.pz() * track.pz() + 
                            0.1056583715 * 0.1056583715));

      if(fabs((t + p).M() - 91.1876) >= 10.0) continue; // cutEleTrkInvMass80To100
      if(muon.charge() * track.charge() >= 0) continue; // cutEleTrkOS

      return true;
    }
  }

  return false;
}

bool
TrackCollectionAnalyzer::isTagProbeElectron(const vector<pat::Electron> tagElectrons,
                                         const vector<pat::Muon> tagMuons,
                                         const pat::MET &met,
                                         const vector<reco::Track> probeTracks) const
{
  // cutTrkMuonVeto
  // cutTrkTauHadVeto

  for(const auto &electron : tagElectrons) {
    TLorentzVector t(electron.px(), electron.py(), electron.pz(), electron.energy());
    for(const auto &track : probeTracks) {
      TLorentzVector p(track.px(), 
                       track.py(), 
                       track.pz(), 
                       sqrt(track.px() * track.px() + 
                            track.py() * track.py() + 
                            track.pz() * track.pz() + 
                            0.000510998928 * 0.000510998928));

      if(fabs((t + p).M() - 91.1876) >= 10.0) continue; // cutEleTrkInvMass80To100
      if(electron.charge() * track.charge() >= 0) continue; // cutEleTrkOS
      return true;
    }
  }
  return false;
}

const bool
TrackCollectionAnalyzer::isProbeTrack(const CandidateTrack& track, const double dRMinJet, const double trackIso) const
{
  
  if(track.pt() <= 30 ||
     fabs(track.eta()) >= 2.1 ||
     // skip fiducial selections
     track.hitPattern().numberOfValidPixelHits() < 4 ||
     track.hitPattern().numberOfValidHits() < 4 ||
     track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) != 0 ||
     track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) != 0 || 
     trackIso / track.pt() >= 0.05 ||
     fabs(track.d0()) >= 0.02 ||
     fabs(track.dz()) >= 0.5 ||
     // skip lepton vetoes
     fabs(dRMinJet) <= 0.5) {
    return false;
  }

  return true;
}

vector<pat::Muon>
TrackCollectionAnalyzer::getTagMuons (const edm::Event &event,
                                const edm::TriggerResults &triggers,
                                const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                const reco::Vertex &vertex,
                                const vector<pat::Muon> &muons)
{
  vector<pat::Muon> tagMuons;

  for(const auto &muon : muons) {
    if(muon.pt() <= (is2017_ ? 29 : 26)) continue;
    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           muon,
                                           trigObjs,
                                          (is2017_ ? "hltIterL3MuonCandidates::HLT" : "hltIterL3MuonCandidates::HLT"),
                                          (is2017_ ? "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07" : "hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered"))) {
        continue; // cutMuonMatchToTrigObj
    }
    if(fabs(muon.eta()) >= 2.1) continue;
    if(!muon.isTightMuon(vertex)) continue;
    double muIso = muon.pfIsolationR04().sumChargedHadronPt;
    muIso += max(0.0, muon.pfIsolationR04().sumNeutralHadronEt + muon.pfIsolationR04().sumPhotonEt - 0.5 * muon.pfIsolationR04().sumPUPt);
    if(muIso / muon.pt() >= 0.15) continue;
    tagMuons.push_back(muon);
  }

  return tagMuons;
}

vector<pat::Electron>
TrackCollectionAnalyzer::getTagElectrons(const edm::Event &event,
                                           const edm::TriggerResults &triggers,
                                           const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                           const reco::Vertex &vertex,
                                           const vector<pat::Electron> &electrons)
{
  vector<pat::Electron> tagElectrons;

  for(const auto &electron : electrons) {
    if(electron.pt() <= (is2017_ ? 35 : 32)) continue;

    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           electron,
                                           trigObjs,
                                           "hltEgammaCandidates::HLT", 
                                           (is2017_ ? "hltEle35noerWPTightGsfTrackIsoFilter" : "hltEle32WPTightGsfTrackIsoFilter"))) {
      continue; // cutElectronMatchToTrigObj
    }

    if(fabs(electron.eta()) >= 2.1) continue;
    if(!electron.electronID(is2017_ ? "cutBasedElectronID-Fall17-94X-V1-tight" : "cutBasedElectronID-Fall17-94X-V2-tight")) continue;
    
    if(fabs(electron.superCluster()->eta()) <= 1.479) {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.05) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.10) continue;
    }
    else {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.10) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.20) continue;
    }

    tagElectrons.push_back(electron);
  }

  return tagElectrons;
}

const unsigned int
TrackCollectionAnalyzer::isTagProbeMuonPair(const CandidateTrack &probe, const pat::Muon &tag) const 
{
  TLorentzVector t(tag.px(), tag.py(), tag.pz(), tag.energy());
  TLorentzVector p(probe.px(), 
                   probe.py(), 
                   probe.pz(), 
                   sqrt(probe.px() * probe.px() + 
                        probe.py() * probe.py() + 
                        probe.pz() * probe.pz() + 
                        0.1056583715 * 0.1056583715)); // energyofMuon()

  if(fabs((t + p).M() - 91.1876) >= 10.0) return 0b00;
  return (tag.charge() * probe.charge() < 0) ? 0b01 : 0b10;
}

const unsigned int
TrackCollectionAnalyzer::isTagProbeElePair(const CandidateTrack &probe, const pat::Electron &tag) const 
{
  TLorentzVector t(tag.px(), tag.py(), tag.pz(), tag.energy());
  TLorentzVector p(probe.px(), 
                   probe.py(), 
                   probe.pz(), 
                   sqrt(probe.px() * probe.px() + 
                        probe.py() * probe.py() + 
                        probe.pz() * probe.pz() + 
                        0.000510998928 * 0.000510998928)); // energyOfElectron()

  if(fabs((t + p).M() - 91.1876) >= 10.0) return 0b00;
  return (tag.charge() * probe.charge() < 0) ? 0b01 : 0b10;
}

const double 
TrackCollectionAnalyzer::MinDRtoJet(const vector<pat::Jet> &jets, const CandidateTrack &track) const
{

    double dRMinJet = -1;
    for(const auto &jet : jets) {
      if(jet.pt() > 30 &&
         fabs(jet.eta()) < 4.5 &&
         anatools::jetPassesTightLepVeto(jet) // This automatically uses the correct jet ID criteria
        ) {
        double dR = deltaR(track, jet);
        if(dRMinJet < 0 || dR < dRMinJet) dRMinJet = dR;
      }
    }
    return dRMinJet;
}

const double
TrackCollectionAnalyzer::GetEcaloAOD(const CandidateTrack &track, const EBRecHitCollection &EBRecHits, const EERecHitCollection &EERecHits, const HBHERecHitCollection &HBHERecHits, double dR) const
{

  double trackEcalo = 0;

  //Add the ecal endcap rec hits
  for(const auto &hit : EERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy();
  }
  
  //add the ecal barrel rec hits
  for(const auto &hit : EBRecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy(); 
  }

  //add the hcal barrel rec hits
  for(const auto &hit : HBHERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy();
  }
  
  return trackEcalo;
}

const double
TrackCollectionAnalyzer::GetECALMINIAOD(const CandidateTrack &track, 
					const EcalRecHitCollection &miniEBRecHits, 
					const EcalRecHitCollection & miniEERecHits, 
					const double dR) const
{

  double trackEcalo = 0;

  //Add the ecal barrel rec hits
  for(const auto &hit : miniEBRecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy();
  }

  //Add the ecal endcap rec hits
  for(const auto &hit : miniEERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy();
  }

  return trackEcalo;

}

const double 
TrackCollectionAnalyzer::GetHCALMINIAOD(const CandidateTrack &track, 
                                        const HBHERecHitCollection & miniHBHERecHits,
                                        const HBHERecHitCollection & miniHCALRecHits,
                                        const double dR,
                                        bool eGamma) const
{

  double trackEcalo = 0;

  if(eGamma){
    for(const auto &hit : miniHBHERecHits){
      math::XYZVector pos = getPosition(hit.detid());
      double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
      if(dR2 < dR) trackEcalo += hit.energy();
    }
  }

  if(!eGamma){
    for(const auto &hit : miniHCALRecHits){
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
      if(dR2 < dR) trackEcalo += hit.energy();
    }
  }

  return trackEcalo;
}

const double
TrackCollectionAnalyzer::GetEcaloHFHO(const CandidateTrack &track,
                                      const HFRecHitCollection & miniHFRecHits, 
                                      const HORecHitCollection & miniHORecHits, 
                                      const double dR) const
{
  double trackEcalo = 0;

  for(const auto &hit : miniHFRecHits){
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy();
  }

  for(const auto &hit : miniHORecHits){
    math::XYZVector pos = getPosition(hit.detid());
    double dR2 = deltaR2(pos.eta(), pos.phi(), track.eta(), track.phi());
    if(dR2 < dR) trackEcalo += hit.energy();
  }

  return trackEcalo;
}

const double
TrackCollectionAnalyzer::GetPFEnergy(const CandidateTrack &track, const edm::Handle<pat::PackedCandidateCollection> &packedCandidates, const int pdgID, const double dR) const
{
  double pcEnergy = 0;

  for(const auto &pc : *packedCandidates){
    if(pdgID != -1 && fabs(pc.pdgId()) != pdgID){
      bool saveParticle = false;
      if(pdgID == 23 && fabs(pc.pdgId()) == 24) saveParticle = true;
      if(pdgID == 1 && fabs(pc.pdgId()) <= 6 && fabs(pc.pdgId()) > 0) saveParticle = true;
      if(!saveParticle) continue;
    }
    double this_dR = deltaR(track, pc);
    if(this_dR > dR || this_dR < 0.001) continue;
    pcEnergy += pc.energy();
  }

  return pcEnergy;

}

const math::XYZVector 
TrackCollectionAnalyzer::getPosition(const DetId& id) const
{
   if(!caloGeometry_->getSubdetectorGeometry(id) || !caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id) ) {
      throw cms::Exception("FatalError") << "Failed to access geometry for DetId: " << id.rawId();
      return math::XYZVector(0,0,0);
   }
   const GlobalPoint idPosition = caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id)->getPosition();
   math::XYZVector idPositionRoot(idPosition.x(), idPosition.y(), idPosition.z());
   return idPositionRoot;
}

void
TrackCollectionAnalyzer::getGeometries(const edm::EventSetup &setup) {
  // setup.get<CaloGeometryRecord>().get(caloGeometry_);
  caloGeometry_ = setup.getHandle(caloGeomToken_);
  if(!caloGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find CaloGeometryRecord in event!\n";

  // setup.get<MuonGeometryRecord>().get(cscGeometry_);
  cscGeometry_ = setup.getHandle(cscGeomToken_);
  if(!cscGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find MuonGeometryRecord (CSC) in event!\n";

  // setup.get<MuonGeometryRecord>().get(dtGeometry_);
  dtGeometry_ = setup.getHandle(dtGeomToken_);
  if(!dtGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find MuonGeometryRecord (DT) in event!\n";

  // setup.get<MuonGeometryRecord>().get(rpcGeometry_);
  rpcGeometry_ = setup.getHandle(rpcGeomToken_);
  if(!rpcGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find MuonGeometryRecord (RPC) in event!\n";

  // setup.get<EcalChannelStatusRcd>().get(ecalStatus_);
  // setup.get<TrackerTopologyRcd>().get(trackerTopology_);
  ecalStatus_ = setup.getHandle(ecalStatToken_);
  trackerTopology_ = setup.getHandle(trackerTopoToken_);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackCollectionAnalyzer);

#endif
