// -*- C++ -*-
//
// Package:    TriggerAnalysis/HLTrigEffAnalyzer
// Class:      HLTrigEffAnalyzer
//
/*
 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Kai Wei
//         Created:  Thu, 2 Sep 2021 02:08:46 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

//
// class declaration
//
using namespace std;
using namespace pat;
class HLTrigEffAnalyzer : public edm::stream::EDAnalyzer<> {
   public:
      explicit HLTrigEffAnalyzer(const edm::ParameterSet&);
      ~HLTrigEffAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
      bool getHLTObj(const edm::Event &event,
                     const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                     const edm::TriggerResults &triggerBits,
                     const string &collection,
                     vector<pat::TriggerObjectStandAlone> &objVector) const;
      bool isGoodPV(const reco::Vertex &pv) const;
      bool isGoodTrack(const pat::IsolatedTrack &track,
                       const reco::Vertex &pv,
                       const vector<pat::IsolatedTrack> &tracks) const;
      bool isValidJet(const pat::Jet &jet) const;
      double maxJetDeltaPhi(const vector<pat::Jet> &jets) const;
      bool passJetTightLepVeto(const pat::Jet &jet) const;

   private:
      void beginJob();
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      void endJob();


      // ----------member data ---------------------------
      edm::EDGetTokenT<vector<pat::MET> > tokenMET_;
      edm::EDGetTokenT<vector<pat::IsolatedTrack> > tokenTracks_;
      edm::EDGetTokenT<vector<pat::Photon> > tokenPhotons_;
      edm::EDGetTokenT<vector<pat::PackedCandidate> > tokenPFCandidates_;
      edm::EDGetTokenT<vector<pat::Jet> > tokenJets_;
      edm::EDGetTokenT<edm::TriggerResults> tokenTriggerBits_;
      edm::EDGetTokenT<edm::TriggerResults> tokenSecTriggerBits_;
      edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjs_;
      edm::EDGetTokenT<vector<reco::Vertex> > tokenVertices_;
      //edm::EDGetTokenT<vector<reco::GenParticle> > tokenGenParticles_;

      std::string triggerName;
      //std::map<string, bool> triggerFires;
      //used to select what tracks to read from configuration file

  TTree *tree_;
  bool        hasGoodPV;
  bool        hasGoodJet;
  double      maxJetsDPhi;
  double      dPhi_Jet_METNoMu;
  double      MetPt;
  double      MetNoMuPt;
  double      MetNoMuPhi;
  std::vector<double> JetPt;
  std::vector<double> JetEta;
  std::vector<bool>   JetTightLepVeto;
  bool        fireTrigger;
  double      offlineIsoTrkPt;
  bool        offlineSelection;
  bool        offlineSelection_NoMETNoMu;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HLTrigEffAnalyzer::HLTrigEffAnalyzer(const edm::ParameterSet& cfg)
{
  tokenMET_          = consumes<vector<pat::MET> >(cfg.getParameter<edm::InputTag>("mets"));
  tokenVertices_     = consumes<vector<reco::Vertex> >(cfg.getParameter<edm::InputTag>("primaryvertexs"));
  tokenTracks_       = consumes<vector<pat::IsolatedTrack> >(cfg.getParameter<edm::InputTag>("tracks"));
  tokenPFCandidates_ = consumes<vector<pat::PackedCandidate> >(cfg.getParameter<edm::InputTag>("pfCandidates"));
  tokenJets_         = consumes<vector<pat::Jet> >(cfg.getParameter<edm::InputTag>("jets"));
  tokenTriggerBits_  = consumes<edm::TriggerResults>(cfg.getParameter<edm::InputTag>("triggers"));
  tokenSecTriggerBits_  = consumes<edm::TriggerResults>(cfg.getParameter<edm::InputTag>("secondaryTriggers"));
  tokenTriggerObjs_  = consumes<vector<pat::TriggerObjectStandAlone> >(cfg.getParameter<edm::InputTag>("trigobjs"));
  triggerName        = cfg.getParameter<std::string >("triggerName");
  //tokenGenParticles_ = consumes<vector<reco::GenParticle> >(cfg.getParameter<edm::InputTag>("mcparticles"));
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  
  //use variable binning for met histograms (determined empirically)
  //float bins[] = {0, 25, 50, 75, 100, 125, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
  //int binnum = 15;

  tree_ = fs->make<TTree>("tree", "tree");
  tree_->Branch("hasGoodPV", &hasGoodPV);
  tree_->Branch("hasGoodJet", &hasGoodJet);
  tree_->Branch("maxJetsDPhi", &maxJetsDPhi);
  tree_->Branch("dPhi_Jet_METNoMu", &dPhi_Jet_METNoMu);
  tree_->Branch("MetPt", &MetPt);
  tree_->Branch("MetNoMuPt", &MetNoMuPt);
  tree_->Branch("JetPt", &JetPt);
  tree_->Branch("JetEta", &JetEta);
  tree_->Branch("JetTightLepVeto", &JetTightLepVeto);
  tree_->Branch("fireTrigger", &fireTrigger);
  tree_->Branch("offlineIsoTrkPt", &offlineIsoTrkPt);
  tree_->Branch("offlineSelection", &offlineSelection);
  tree_->Branch("offlineSelection_NoMETNoMu", &offlineSelection_NoMETNoMu);
}


HLTrigEffAnalyzer::~HLTrigEffAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
HLTrigEffAnalyzer::analyze(const edm::Event& event, const edm::EventSetup& setup)
{
    using namespace std;
 
    // Get PrimaryVertex 
    edm::Handle<vector<reco::Vertex> > vertices;
    event.getByToken(tokenVertices_, vertices);
    const reco::Vertex &pv = vertices->at(0);

    hasGoodPV = isGoodPV(pv);

    //edm::Handle<vector<reco::GenParticle> > genParticles;
    //bool isMC = event.getByToken(tokenGenParticles_, genParticles);

    edm::Handle<vector<pat::IsolatedTrack> > tracks;
    bool hasTracks = event.getByToken(tokenTracks_, tracks);

    vector<const pat::IsolatedTrack*> selectedTracks;
    if(hasTracks) {
      for(const auto &track : *tracks) {
        bool goodTrack = isGoodTrack(track, pv, *tracks);
        if(!goodTrack) continue;
        selectedTracks.push_back (&track);
      }
      sort(selectedTracks.begin(),
           selectedTracks.end(),
           [](const pat::IsolatedTrack *a, const pat::IsolatedTrack *b) -> bool { return (a->pt() > b->pt()); });
    }
 
    offlineIsoTrkPt = selectedTracks.empty() ? -1.0 : selectedTracks.at(0)->pt();

    edm::Handle<vector<pat::PackedCandidate> > pfCandidates;
    event.getByToken (tokenPFCandidates_, pfCandidates);
    edm::Handle<vector<pat::MET> > mets;
    event.getByToken (tokenMET_, mets);
    const pat::MET met = mets->at(0);
    
    MetPt = met.pt();
 
    TVector2 metNoMu(met.px (), met.py ());
    for (const auto &pfCandidate : *pfCandidates) {
      if (abs (pfCandidate.pdgId ()) != 13) continue;
      TVector2 muon (pfCandidate.px (), pfCandidate.py ());
      metNoMu += muon;
    }
    MetNoMuPt = metNoMu.Mod();
    MetNoMuPhi = metNoMu.Phi();


    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<edm::TriggerResults> sectriggerBits;
    edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;

    if(!event.getByToken(tokenTriggerBits_, triggerBits)) {
      clog << "ERROR:  Could not find triggerBits collection." << endl;
      return;
    }
    if(!event.getByToken(tokenSecTriggerBits_, sectriggerBits)) {
      clog << "ERROR:  Could not find triggerBits collection." << endl;
      return;
    }
    event.getByToken(tokenTriggerObjs_, triggerObjs);

    for(auto triggerObj : *triggerObjs) {
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
      triggerObj.unpackNamesAndLabels(event, *triggerBits);
#else
      triggerObj.unpackPathNames(allTriggerNames);
#endif
    }

    const edm::TriggerNames &allTriggerNames = event.triggerNames(*triggerBits);
    const edm::TriggerNames &allSecTriggerNames = event.triggerNames(*sectriggerBits);


    int TriggerFired = 0;
    for(unsigned i = 0; i < allSecTriggerNames.size(); i++) {
      string thisName = allSecTriggerNames.triggerName(i);
      cout << "PathName:" << thisName  <<  " Decision:" << sectriggerBits->accept(i)<< endl;
      if (thisName.find(triggerName) ==  0 ){
        TriggerFired |= sectriggerBits->accept(i);
      }
    }

    for(unsigned i = 0; i < allTriggerNames.size(); i++) {
      string thisName = allTriggerNames.triggerName(i);
      cout << "TriggerName: " << thisName << endl;
    }
    fireTrigger = TriggerFired;

    edm::Handle<vector<pat::Jet> > jets;
    event.getByToken(tokenJets_, jets);

    JetPt.clear();
    JetEta.clear();
    JetTightLepVeto.clear();

    hasGoodJet = false;
    double leadingJetPt = -1.0;
    double leadingJetPhi = -9.9;
    for (auto jet = jets->begin(); jet != jets->end(); ++jet) {
      if (jet->et() > leadingJetPt) {
        leadingJetPhi = jet->phi();
      }
      JetPt.push_back(jet->et());
      JetEta.push_back(jet->eta());
      bool jetTightLepVeto = passJetTightLepVeto(*jet);
      JetTightLepVeto.push_back(jetTightLepVeto);
      if (jet->et() > 110 && fabs(jet->eta()) < 2.4 && jetTightLepVeto) {
        hasGoodJet = true;
      }
    }
    if (leadingJetPhi < -4.0){
      dPhi_Jet_METNoMu = -1.0;
    }
    else{
      dPhi_Jet_METNoMu = fabs(deltaPhi(leadingJetPhi, MetNoMuPhi));
    }
    

    maxJetsDPhi =  maxJetDeltaPhi(*jets);
   
    if (hasGoodPV && hasGoodJet && maxJetsDPhi < 2.5 && maxJetsDPhi >= 0.0 && dPhi_Jet_METNoMu > 0.5){
      offlineSelection_NoMETNoMu = true;
    } 
    else{
      offlineSelection_NoMETNoMu = false;
    }
    offlineSelection = offlineSelection_NoMETNoMu && (MetNoMuPt > 120);  
 
    tree_->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void
HLTrigEffAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
HLTrigEffAnalyzer::endJob()
{
  //  l1metEff = (TH1D*) l1metPt->Clone("l1metEff");
  //  l1metEff->Divide(metPt);
  //  l1metEff->Write();

}

// ------------ method called when starting to processes a run  ------------
/*
void
HLTrigEffAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
HLTrigEffAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
HLTrigEffAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
HLTrigEffAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HLTrigEffAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

bool HLTrigEffAnalyzer::getHLTObj(const edm::Event &event,
                                  const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                  const edm::TriggerResults &triggerBits,
                                  const string &collection,
                                  vector<pat::TriggerObjectStandAlone> &objVector) const {

  // Finds the leading trigger object from "collection::HLT" and sets "obj" to it
  // Returns true if it found any "collection::HLT", and false if not

  double leadingPt = -1.0;
  pat::TriggerObjectStandAlone obj;

  for(auto triggerObj : triggerObjs) {

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, triggerBits);
#else
    triggerObj.unpackPathNames(event.triggerNames(triggerBits));
#endif

    if(triggerObj.collection() == (collection + "::HLT")) {
      obj = triggerObj;
      objVector.push_back(obj);
      if(triggerObj.pt() > leadingPt) {
        leadingPt = obj.pt();
      }

    }
  }

  return (leadingPt > 0.0);
}

bool HLTrigEffAnalyzer::isGoodPV(const reco::Vertex &pv) const {
  bool isGoodPV = pv.isValid() > 0 &&
                  pv.ndof() >= 4 && 
                  fabs (pv.z()) < 24.0 && 
                  sqrt (pv.x() * pv.x() + pv.y() * pv.y()) < 2.0;
  return isGoodPV;
}

bool HLTrigEffAnalyzer::isGoodTrack(const pat::IsolatedTrack &track,
                                    const reco::Vertex &pv,
                                    const vector<pat::IsolatedTrack> &tracks) const {

//#if DATA_FORMAT == MINI_AOD_2017
  bool result = (fabs(track.eta()) < 2.5 &&
                 track.isHighPurityTrack() && // bfrancis: is this what we want to do? replaces normalizedChi2 < 10.0
                 fabs(track.dxy()) < 0.2 &&
                 fabs(track.dz()) < 0.5 &&
                 track.hitPattern().numberOfValidPixelHits() >= 1 &&
                 track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                 track.pfIsolationDR03().chargedHadronIso() / track.pt() < 0.01); // replaces trackIsoNoPUDRp3/pt
  return result;
}

bool HLTrigEffAnalyzer::isValidJet(const pat::Jet& jet) const {
  if (!(jet.pt() > 30))         return false;
  if (!(fabs(jet.eta()) < 4.5)) return false;
  if (!passJetTightLepVeto (jet)) return false;

  return true;
}

double HLTrigEffAnalyzer::maxJetDeltaPhi(const vector<pat::Jet> &jets) const{
  double maxJetDeltaPhi = -1.0;
  if (jets.size() < 2) return maxJetDeltaPhi;
  for (auto jet = jets.begin(); jet != jets.end(); ++jet){
    if (!isValidJet(*jet)) continue;
    for (auto jet2 = std::next(jet); jet2 != jets.end(); ++jet2){
      if (!isValidJet(*jet2)) continue;
      double DeltaPhi = fabs(deltaPhi(jet->phi(),jet2->phi()));
      maxJetDeltaPhi = maxJetDeltaPhi > DeltaPhi ? maxJetDeltaPhi : DeltaPhi;
    } 
  }
  return maxJetDeltaPhi;
}

bool HLTrigEffAnalyzer::passJetTightLepVeto(const pat::Jet& jet) const {
  bool result = anatools::jetPassesTightLepVeto(jet); // This automatically uses the correct jet ID criteria
  return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLTrigEffAnalyzer);
