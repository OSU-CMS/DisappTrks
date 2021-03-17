// -*- C++ -*-
//
// Package:    TriggerAnalysis/HLTrigVarProducer
// Class:      HLTrigVarProducer
//
/*
 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Kai Wei
//         Created:  Sun, 21 Feb 2021 09:16:39 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

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
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/L1Trigger/interface/L1EtMissParticleFwd.h"
#include "DataFormats/L1Trigger/interface/L1EtMissParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

//
// class declaration
//
using namespace std;
using namespace pat;
class HLTrigVarProducer : public edm::EDAnalyzer {
   public:
      explicit HLTrigVarProducer(const edm::ParameterSet&);
      ~HLTrigVarProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
      bool getHLTObj(const edm::Event &event,
                     const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                     const edm::TriggerResults &triggerBits,
                     const string &collection,
                     vector<pat::TriggerObjectStandAlone> &objVector) const;
      bool isGoodTrack(const pat::IsolatedTrack &track,
                       const reco::Vertex &pv,
                       const vector<pat::IsolatedTrack> &tracks) const;

   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;


      // ----------member data ---------------------------
      edm::EDGetTokenT<vector<pat::MET> > tokenMET_;
      edm::EDGetTokenT<vector<pat::IsolatedTrack> > tokenTracks_;
      edm::EDGetTokenT<vector<l1extra::L1EtMissParticle> > tokenL1MET_;
      edm::EDGetTokenT<vector<pat::Photon> > tokenPhoton_;
      edm::EDGetTokenT<edm::TriggerResults> tokenTriggerBits_;
      edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjs_;
      edm::EDGetTokenT<vector<reco::Vertex> > tokenVertices_;
      //edm::EDGetTokenT<vector<reco::GenParticle> > tokenGenParticles_;

      std::vector<string> triggerNames;
      std::map<string, bool> triggerFires;
      //used to select what tracks to read from configuration file

  TH1D *metPt;
  TH1D *l1metPt;
  TH1D *hltmetPt;
  TH2D *pfMetVsHltMet;
  TH2D *pfMetVsL1Met;
  TH1D *photonPt;
  TH1D *nPhoton;
  TH2D *metPtVsphotonPt;
  TH2D *hltmetPtVsphotonPt;
  TH2D *hltmetPtVshltegammaCandPt;
  TH2D *MET105IsoTrk50vsPhoton;
  TH1D *nHltegammaCands;
  TH1D *hltegammaCandPt;

  TTree *tree_;
  double bMetPt = 0.0;
  double bHltmetPt = 0.0;
  double bHltmetcleanPt = 0.0;
  double bPhotonPt = 0.0;
  int    bnPhoton = 0;
  int    bnHltegammaCands = 0;
  double bHltegammaCandPt = 0.0;
  int    bfireMET105IsoTrk50 = 0;
  int    bfireHLTPhoton20 = 0;
  int    bfireHLTPhoton33 = 0;
  int    bfireHLTPhoton50 = 0;
  int    bfireHLTPhoton75 = 0;
  int    bfireHLTPhoton90 = 0;
  int    bfireHLTPhoton120 = 0;
  int    bfireHLTPhoton150 = 0;
  int    bfireHLTPhoton175 = 0;
  int    bfireHLTPhoton200 = 0;
  int    bfireHLTPhoton110EB = 0;
  int    bfirePFJet15  =  0;
  int    bfirePFJet25  =  0;
  int    bfirePFJet40  =  0;
  int    bfirePFJet60  =  0;
  int    bfirePFJet80  =  0;
  int    bfirePFJet140  =  0;
  int    bfirePFJet200  =  0;
  int    bfirePFJet260  =  0;
  int    bfirePFJet320  =  0;
  int    bfirePFJet400  =  0;
  int    bfirePFJet450  =  0;
  int    bfirePFJet500  =  0;
  int    bfirePFJet550  =  0;
  int    bfirePFJetFwd15  =  0;
  int    bfirePFJetFwd25  =  0;
  int    bfirePFJetFwd40  =  0;
  int    bfirePFJetFwd60  =  0;
  int    bfirePFJetFwd80  =  0;
  int    bfirePFJetFwd140  =  0;
  int    bfirePFJetFwd200  =  0;
  int    bfirePFJetFwd260  =  0;
  int    bfirePFJetFwd320  =  0;
  int    bfirePFJetFwd400  =  0;
  int    bfirePFJetFwd450  =  0;
  int    bfirePFJetFwd500  =  0;
  int    bfireIsoTrk50Filter = 0;
  double bOfflineIsoTrkPt = -1.0;
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
HLTrigVarProducer::HLTrigVarProducer(const edm::ParameterSet& cfg)
{
  tokenMET_          = consumes<vector<pat::MET> >(cfg.getParameter<edm::InputTag>("mets"));
  //tokenL1MET_        = consumes<vector<l1extra::L1EtMissParticle> >(cfg.getParameter<edm::InputTag>("l1mets"));
  tokenVertices_     = consumes<vector<reco::Vertex> >(cfg.getParameter<edm::InputTag>("primaryvertexs"));
  tokenTracks_       = consumes<vector<pat::IsolatedTrack> >(cfg.getParameter<edm::InputTag>("tracks"));
  tokenPhoton_       = consumes<vector<pat::Photon> >(cfg.getParameter<edm::InputTag>("photons"));
  tokenTriggerBits_  = consumes<edm::TriggerResults>(cfg.getParameter<edm::InputTag>("triggers"));
  tokenTriggerObjs_  = consumes<vector<pat::TriggerObjectStandAlone> >(cfg.getParameter<edm::InputTag>("trigobjs"));
  //tokenGenParticles_ = consumes<vector<reco::GenParticle> >(cfg.getParameter<edm::InputTag>("mcparticles"));
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  //use variable binning for met histograms (determined empirically)

  float bins[] = {0, 25, 50, 75, 100, 125, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
  int binnum = 15;

  metPt = fs->make<TH1D>("met" , "met pT; MET [GeV}", 100 , -0.5 ,499.5);
  l1metPt = fs->make<TH1D>("l1met" , "l1 met pT; L1 MET [GeV]", 100 , -0.5 ,499.5);
  hltmetPt = fs->make<TH1D>("hltMet" , "HLT MET pT; hltMET [GeV]", 100 , -0.5 ,499.5);
  pfMetVsL1Met = fs->make<TH2D>("pfMetVsL1Met" , "pfMet vs L1 MET; L1 MET [GeV]; PF MET [GeV]", 100, -0.5, 499.5, 100, -0.5, 499.5);
  photonPt = fs->make<TH1D>("photon" , "photon pT; Photon pT [GeV]", 100 , -0.5 ,499.5);
  nPhoton = fs->make<TH1D>("nPhoton" , "Num of photon; nPhoton", 10 , -0.5 , 9.5);
  nHltegammaCands = fs->make<TH1D>("nHltegammaCands" , "Num of hltEgammaCands; nEGammaCand", 10 , -0.5 , 9.5);
  hltegammaCandPt = fs->make<TH1D>("hltEgammaCandPt" , "hltEgammaCand pT; hltEGammaCand pT [GeV]", 100 , -0.5 ,499.5);
  metPtVsphotonPt = fs->make<TH2D>("metPtVsphotonPt", "pfMet vs photon pT; PF MET [GeV]; Photon pT [GeV]", 100, -0.5, 499.5, 100, -0.5, 499.5);
  hltmetPtVsphotonPt = fs->make<TH2D>("hltmetPtVsphotonPt", "hltMet vs photon  pT; hltMET [GeV]; Photon  pT [GeV]", 100, -0.5, 499.5, 100, -0.5, 499.5);
  hltmetPtVshltegammaCandPt = fs->make<TH2D>("hltmetPtVshltegammaCandPt", "hltMet vs hltEgammaCand pT; hltMET [GeV]; hltEGammaCand pT [GeV]",100, -0.5, 499.5, 100, -0.5, 499.5);
  MET105IsoTrk50vsPhoton = fs->make<TH2D>("MET105IsoTrk50vsPhoton", "HLT Cov Table; HLT_MET105_IsoTrk50; HLT_Photon200 || HLT_Photonn110EB",2,-0.5,1.5,2,-0.5,1.5);

  tree_ = fs->make<TTree>("tree", "tree");
  tree_->Branch("MetPt", &bMetPt);
  tree_->Branch("hltMetPt", &bHltmetPt);
  tree_->Branch("hltMetCleanPt", &bHltmetcleanPt);
  tree_->Branch("PhotonPt", &bPhotonPt);
  tree_->Branch("nPhoton", &bnPhoton);
  tree_->Branch("nHLTEgammaCands", &bnHltegammaCands);
  tree_->Branch("HLTEgammaCandPt", &bHltegammaCandPt);
  tree_->Branch("fireMET105IsoTrk50", &bfireMET105IsoTrk50);
  tree_->Branch("fireHLTPhoton20", &bfireHLTPhoton20); 
  tree_->Branch("fireHLTPhoton33", &bfireHLTPhoton33); 
  tree_->Branch("fireHLTPhoton50", &bfireHLTPhoton50); 
  tree_->Branch("fireHLTPhoton75", &bfireHLTPhoton75); 
  tree_->Branch("fireHLTPhoton90", &bfireHLTPhoton90); 
  tree_->Branch("fireHLTPhoton120", &bfireHLTPhoton120); 
  tree_->Branch("fireHLTPhoton150", &bfireHLTPhoton150); 
  tree_->Branch("fireHLTPhoton175", &bfireHLTPhoton175); 
  tree_->Branch("fireHLTPhoton200", &bfireHLTPhoton200); 
  tree_->Branch("fireHLTPhoton110EB", &bfireHLTPhoton110EB);
  tree_->Branch("fireHLTPFJet15", &bfirePFJet15);
  tree_->Branch("fireHLTPFJet25", &bfirePFJet25);
  tree_->Branch("fireHLTPFJet40", &bfirePFJet40);
  tree_->Branch("fireHLTPFJet60", &bfirePFJet60);
  tree_->Branch("fireHLTPFJet80", &bfirePFJet80);
  tree_->Branch("fireHLTPFJet140", &bfirePFJet140);
  tree_->Branch("fireHLTPFJet200", &bfirePFJet200);
  tree_->Branch("fireHLTPFJet260", &bfirePFJet260);
  tree_->Branch("fireHLTPFJet320", &bfirePFJet320);
  tree_->Branch("fireHLTPFJet400", &bfirePFJet400);
  tree_->Branch("fireHLTPFJet450", &bfirePFJet450);
  tree_->Branch("fireHLTPFJet500", &bfirePFJet500);
  tree_->Branch("fireHLTPFJet550", &bfirePFJet550);
  tree_->Branch("fireHLTPFJetFwd15", &bfirePFJetFwd15);
  tree_->Branch("fireHLTPFJetFwd25", &bfirePFJetFwd25);
  tree_->Branch("fireHLTPFJetFwd40", &bfirePFJetFwd40);
  tree_->Branch("fireHLTPFJetFwd60", &bfirePFJetFwd60);
  tree_->Branch("fireHLTPFJetFwd80", &bfirePFJetFwd80);
  tree_->Branch("fireHLTPFJetFwd140", &bfirePFJetFwd140);
  tree_->Branch("fireHLTPFJetFwd200", &bfirePFJetFwd200);
  tree_->Branch("fireHLTPFJetFwd260", &bfirePFJetFwd260);
  tree_->Branch("fireHLTPFJetFwd320", &bfirePFJetFwd320);
  tree_->Branch("fireHLTPFJetFwd400", &bfirePFJetFwd400);
  tree_->Branch("fireHLTPFJetFwd450", &bfirePFJetFwd450);
  tree_->Branch("fireHLTPFJetFwd500", &bfirePFJetFwd500);
  tree_->Branch("fireIsoTrk50Filter", &bfireIsoTrk50Filter);
  tree_->Branch("offlineIsoTrkPt", &bOfflineIsoTrkPt);
}


HLTrigVarProducer::~HLTrigVarProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
HLTrigVarProducer::analyze(const edm::Event& event, const edm::EventSetup& setup)
{
    using namespace std;
  
    edm::Handle<vector<reco::Vertex> > vertices;
    event.getByToken(tokenVertices_, vertices);
    const reco::Vertex &pv = vertices->at(0);

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
 
    bOfflineIsoTrkPt = selectedTracks.empty() ? -1.0 : selectedTracks.at(0)->pt();


    edm::Handle<vector<pat::MET> > mets;
    event.getByToken (tokenMET_, mets);
    metPt->Fill(mets->at(0).pt());
    bMetPt = mets->at(0).pt();
    //edm::Handle<vector<l1extra::L1EtMissParticle> > l1mets;
    //event.getByToken (tokenL1MET_, l1mets);
    //l1metPt->Fill(l1mets->at(0).pt());

    //pfMetVsL1Met->Fill(mets->at(0).pt(),l1mets->at(0).pt());

    double photonPtMax = 0.0;
    edm::Handle<vector<pat::Photon> > photons;
    event.getByToken (tokenPhoton_, photons);
    if (photons->size() > 0){
      nPhoton->Fill(photons->size());
      bnPhoton = photons->size();
      for (const auto &photon: *photons ){
        photonPt->Fill(photon.pt());
        if (photon.pt() > photonPtMax) {
          photonPtMax = photon.pt();
        }
      }
    } else {
      nPhoton->Fill(0);
      photonPt->Fill(0.0);
      bnPhoton = 0;
    }
    bPhotonPt = photonPtMax;
    metPtVsphotonPt->Fill(mets->at(0).pt(),photonPtMax);  
       
 
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;

    if(!event.getByToken(tokenTriggerBits_, triggerBits)) {
      clog << "ERROR:  Could not find triggerBits collection." << endl;
      return;
    }
    event.getByToken(tokenTriggerObjs_, triggerObjs);

    for(auto triggerObj : *triggerObjs) {
//#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
      triggerObj.unpackNamesAndLabels(event, *triggerBits);
//#else
//      triggerObj.unpackPathNames(allTriggerNames);
//#endif
    }

    const edm::TriggerNames &allTriggerNames = event.triggerNames(*triggerBits);

    for(auto name : triggerNames) triggerFires[name] = false;

    int MET105IsoTrk50_Fired = 0;
    int HLTPhoton20_Fired = 0;
    int HLTPhoton33_Fired = 0;
    int HLTPhoton50_Fired = 0;
    int HLTPhoton75_Fired = 0;
    int HLTPhoton90_Fired = 0;
    int HLTPhoton120_Fired = 0;
    int HLTPhoton150_Fired = 0;
    int HLTPhoton175_Fired = 0;
    int HLTPhoton200_Fired = 0;
    int HLTPhoton110EB_Fired = 0;
    int HLTPFJet15_Fired = 0;
    int HLTPFJet25_Fired = 0;
    int HLTPFJet40_Fired = 0;
    int HLTPFJet60_Fired = 0;
    int HLTPFJet80_Fired = 0;
    int HLTPFJet140_Fired = 0;
    int HLTPFJet200_Fired = 0;
    int HLTPFJet260_Fired = 0;
    int HLTPFJet320_Fired = 0;
    int HLTPFJet400_Fired = 0;
    int HLTPFJet450_Fired = 0;
    int HLTPFJet500_Fired = 0;
    int HLTPFJet550_Fired = 0;
    int HLTPFJetFwd15_Fired = 0;
    int HLTPFJetFwd25_Fired = 0;
    int HLTPFJetFwd40_Fired = 0;
    int HLTPFJetFwd60_Fired = 0;
    int HLTPFJetFwd80_Fired = 0;
    int HLTPFJetFwd140_Fired = 0;
    int HLTPFJetFwd200_Fired = 0;
    int HLTPFJetFwd260_Fired = 0;
    int HLTPFJetFwd320_Fired = 0;
    int HLTPFJetFwd400_Fired = 0;
    int HLTPFJetFwd450_Fired = 0;
    int HLTPFJetFwd500_Fired = 0;
    for(unsigned i = 0; i < allTriggerNames.size(); i++) {
      string thisName = allTriggerNames.triggerName(i);
      //cout << "TriggerName: " << thisName << endl;
      for(auto name : triggerNames) {
        if(thisName.find(name) == 0) {
          triggerFires[name] |= triggerBits->accept(i);
          break;
        }
      }
      if (thisName.find("HLT_MET105_IsoTrk50") ==  0 ){
        MET105IsoTrk50_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon20_") == 0 ){
        HLTPhoton20_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon33_") == 0 ){
        HLTPhoton33_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon50_") == 0 ){
        HLTPhoton50_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon75_") == 0 ){
        HLTPhoton75_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon90_") == 0 ){
        HLTPhoton90_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon120_") == 0 ){
        HLTPhoton120_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon150_") == 0 ){
        HLTPhoton150_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon175_") == 0 ){
        HLTPhoton175_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon200_") == 0 ){
        HLTPhoton200_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon110EB_TightID_TightIso_v") == 0 ){
        HLTPhoton110EB_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet15_") == 0 ){
        HLTPFJet15_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet25_") == 0 ){
        HLTPFJet25_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet40_") == 0 ){
        HLTPFJet40_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet60_") == 0 ){
        HLTPFJet60_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet80_") == 0 ){
        HLTPFJet80_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet140_") == 0 ){
        HLTPFJet140_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet200_") == 0 ){
        HLTPFJet200_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet260_") == 0 ){
        HLTPFJet260_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet320_") == 0 ){
        HLTPFJet320_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet400_") == 0 ){
        HLTPFJet400_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet450_") == 0 ){
        HLTPFJet450_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet500_") == 0 ){
        HLTPFJet500_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJet550_") == 0 ){
        HLTPFJet550_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd15_") == 0 ){
        HLTPFJetFwd15_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd25_") == 0 ){
        HLTPFJetFwd25_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd40_") == 0 ){
        HLTPFJetFwd40_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd60_") == 0 ){
        HLTPFJetFwd60_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd80_") == 0 ){
        HLTPFJetFwd80_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd140_") == 0 ){
        HLTPFJetFwd140_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd200_") == 0 ){
        HLTPFJetFwd200_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd260_") == 0 ){
        HLTPFJetFwd260_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd320_") == 0 ){
        HLTPFJetFwd320_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd400_") == 0 ){
        HLTPFJetFwd400_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd450_") == 0 ){
        HLTPFJetFwd450_Fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_PFJetFwd500_") == 0 ){
        HLTPFJetFwd500_Fired |= triggerBits->accept(i);
      }
    }
    bfireMET105IsoTrk50 =  MET105IsoTrk50_Fired;
    bfireHLTPhoton20 = HLTPhoton20_Fired;
    bfireHLTPhoton33 = HLTPhoton33_Fired;
    bfireHLTPhoton50 = HLTPhoton50_Fired;
    bfireHLTPhoton75 = HLTPhoton75_Fired;
    bfireHLTPhoton90 = HLTPhoton90_Fired;
    bfireHLTPhoton120 = HLTPhoton120_Fired;
    bfireHLTPhoton150 = HLTPhoton150_Fired;
    bfireHLTPhoton175 = HLTPhoton175_Fired;
    bfireHLTPhoton200 = HLTPhoton200_Fired;
    bfireHLTPhoton110EB = HLTPhoton110EB_Fired;
    bfirePFJet15 = HLTPFJet15_Fired;
    bfirePFJet25 = HLTPFJet25_Fired;
    bfirePFJet40 = HLTPFJet40_Fired;
    bfirePFJet60 = HLTPFJet60_Fired;
    bfirePFJet80 = HLTPFJet80_Fired;
    bfirePFJet140 = HLTPFJet140_Fired;
    bfirePFJet200 = HLTPFJet200_Fired;
    bfirePFJet260 = HLTPFJet260_Fired;
    bfirePFJet320 = HLTPFJet320_Fired;
    bfirePFJet400 = HLTPFJet400_Fired;
    bfirePFJet450 = HLTPFJet450_Fired;
    bfirePFJet500 = HLTPFJet500_Fired;
    bfirePFJet550 = HLTPFJet550_Fired;
    bfirePFJetFwd15 = HLTPFJetFwd15_Fired;
    bfirePFJetFwd25 = HLTPFJetFwd25_Fired;
    bfirePFJetFwd40 = HLTPFJetFwd40_Fired;
    bfirePFJetFwd60 = HLTPFJetFwd60_Fired;
    bfirePFJetFwd80 = HLTPFJetFwd80_Fired;
    bfirePFJetFwd140 = HLTPFJetFwd140_Fired;
    bfirePFJetFwd200 = HLTPFJetFwd200_Fired;
    bfirePFJetFwd260 = HLTPFJetFwd260_Fired;
    bfirePFJetFwd320 = HLTPFJetFwd320_Fired;
    bfirePFJetFwd400 = HLTPFJetFwd400_Fired;
    bfirePFJetFwd450 = HLTPFJetFwd450_Fired;
    bfirePFJetFwd500 = HLTPFJetFwd500_Fired;
 
    vector<pat::TriggerObjectStandAlone> isoTrks;
    bool passesHLTTrk50Filter = getHLTObj(event, *triggerObjs, *triggerBits, "hltTrk50Filter", isoTrks);
    bfireIsoTrk50Filter =  0|passesHLTTrk50Filter;
   
    //cout << "MET_IsoTrk_fired" << MET_IsoTrk_fired << "  Photon_fired" << Photon_fired << endl;
    MET105IsoTrk50vsPhoton->Fill(bfireMET105IsoTrk50,bfireHLTPhoton200 | bfireHLTPhoton110EB);   

    vector<pat::TriggerObjectStandAlone> hltEgammaCands;
    double hltEgammaPtMax = -1.0;
    getHLTObj(event, *triggerObjs, *triggerBits, "hltEgammaCandidates", hltEgammaCands);
    if(hltEgammaCands.size() > 0){
      for(const auto &hltEgamma: hltEgammaCands){
        if (hltEgamma.pt() > hltEgammaPtMax){
          hltEgammaPtMax = hltEgamma.pt();
        }
        hltegammaCandPt->Fill(hltEgamma.pt());
      }
      nHltegammaCands->Fill(hltEgammaCands.size());
      bnHltegammaCands = hltEgammaCands.size();
    }
    else {
      nHltegammaCands->Fill(0);
      hltegammaCandPt->Fill(-1.0);
      bnHltegammaCands = 0;
    }
    bHltegammaCandPt = hltEgammaPtMax;
   
    vector<pat::TriggerObjectStandAlone> hltMets;
    getHLTObj(event, *triggerObjs, *triggerBits, "hltMet", hltMets);
    if(hltMets.size() > 0){
      hltmetPt->Fill(hltMets.at(0).pt());
      hltmetPtVsphotonPt->Fill(hltMets.at(0).pt(),photonPtMax);
      hltmetPtVshltegammaCandPt->Fill(hltMets.at(0).pt(),hltEgammaPtMax);
      bHltmetPt = hltMets.at(0).pt();
    }
    else {
      hltmetPt->Fill(-1.0);
      bHltmetPt =-1.0;
      hltmetPtVsphotonPt->Fill(-1.0,photonPtMax);
      hltmetPtVshltegammaCandPt->Fill(-1.0,hltEgammaPtMax);
    }
    vector<pat::TriggerObjectStandAlone> hltMetCleans;
    getHLTObj(event, *triggerObjs, *triggerBits, "hltMetClean", hltMetCleans);
    if(hltMetCleans.size() > 0){
      bHltmetcleanPt = hltMetCleans.at(0).pt();
    }
    else {
      bHltmetcleanPt = -1.0;
    }
    
    tree_->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void
HLTrigVarProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
HLTrigVarProducer::endJob()
{
  //  l1metEff = (TH1D*) l1metPt->Clone("l1metEff");
  //  l1metEff->Divide(metPt);
  //  l1metEff->Write();

}

// ------------ method called when starting to processes a run  ------------
/*
void
HLTrigVarProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
HLTrigVarProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
HLTrigVarProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
HLTrigVarProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HLTrigVarProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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

bool HLTrigVarProducer::getHLTObj(const edm::Event &event,
                                  const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                  const edm::TriggerResults &triggerBits,
                                  const string &collection,
                                  vector<pat::TriggerObjectStandAlone> &objVector) const {

  // Finds the leading trigger object from "collection::HLT" and sets "obj" to it
  // Returns true if it found any "collection::HLT", and false if not

  double leadingPt = -1.0;
  pat::TriggerObjectStandAlone obj;

  for(auto triggerObj : triggerObjs) {

//#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, triggerBits);
//#else
//    triggerObj.unpackPathNames(event.triggerNames(triggerBits));
//#endif

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

bool HLTrigVarProducer::isGoodTrack(const pat::IsolatedTrack &track,
                                    const reco::Vertex &pv,
                                    const vector<pat::IsolatedTrack> &tracks) const {

#if DATA_FORMAT == MINI_AOD_2017
  bool result = (fabs(track.eta()) < 2.5 &&
                 track.isHighPurityTrack() && // bfrancis: is this what we want to do? replaces normalizedChi2 < 10.0
                 fabs(track.dxy()) < 0.2 &&
                 fabs(track.dz()) < 0.5 &&
                 track.hitPattern().numberOfValidPixelHits() >= 1 &&
                 track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                 track.pfIsolationDR03().chargedHadronIso() / track.pt() < 0.01); // replaces trackIsoNoPUDRp3/pt
#else
  bool result = (fabs(track.eta()) < 2.5 &&
                 track.normalizedChi2() < 10.0 &&
                 fabs(track.dxy(pv.position())) < 0.2 &&
                 fabs(track.dz(pv.position())) < 0.5 &&
                 track.hitPattern().numberOfValidPixelHits() >= 1 &&
                 track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                 track.trackIsoNoPUDRp3() / track.pt() < 0.01);
#endif

  return result;
}
//define this as a plug-in
DEFINE_FWK_MODULE(HLTrigVarProducer);
