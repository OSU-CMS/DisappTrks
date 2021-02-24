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


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;


      // ----------member data ---------------------------
      edm::EDGetTokenT<vector<pat::MET> > tokenMET_;
      edm::EDGetTokenT<vector<l1extra::L1EtMissParticle> > tokenL1MET_;
      edm::EDGetTokenT<vector<pat::Photon> > tokenPhoton_;
      edm::EDGetTokenT<edm::TriggerResults> tokenTriggerBits_;
      edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjs_;

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
  TH2D *MET105IsoTrk50vsPhoton20;
  TH1D *nHltegammaCands;
  TH1D *hltegammaCandPt;

  TTree *tree_;
  double bMetPt = 0.0;
  double bHltmetPt = 0.0;
  double bPhotonPt = 0.0;
  int    bnPhoton = 0;
  int    bnHltegammaCands = 0;
  double bHltegammaCandPt = 0.0;
  int    bfireMET105IsoTrk50 = 0;
  int    bfirePhoton20 = 0;
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
  tokenPhoton_       = consumes<vector<pat::Photon> >(cfg.getParameter<edm::InputTag>("photons"));
  tokenTriggerBits_  = consumes<edm::TriggerResults>(cfg.getParameter<edm::InputTag>("triggers"));
  tokenTriggerObjs_  = consumes<vector<pat::TriggerObjectStandAlone> >(cfg.getParameter<edm::InputTag>("trigobjs"));
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
  MET105IsoTrk50vsPhoton20 = fs->make<TH2D>("MET105IsoTrk50vsPhoton20", "HLT Cov Table; HLT_MET105_IsoTrk50; HLT_Photon20",2,-0.5,1.5,2,-0.5,1.5);

  tree_ = fs->make<TTree>("tree", "tree");
  tree_->Branch("MetPt", &bMetPt);
  tree_->Branch("hltMetPt", &bHltmetPt);
  tree_->Branch("PhotonPt", &bPhotonPt);
  tree_->Branch("nPhoton", &bnPhoton);
  tree_->Branch("nHLTEgammaCands", &bnHltegammaCands);
  tree_->Branch("HLTEgammaCandPt", &bHltegammaCandPt);
  tree_->Branch("fireMET105IsoTrk50", &bfireMET105IsoTrk50);
  tree_->Branch("firePhoton20", &bfirePhoton20); 
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

    int MET_IsoTrk_fired  = 0;
    int Photon_fired  = 0;
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
        MET_IsoTrk_fired |= triggerBits->accept(i);
      }
      if (thisName.find("HLT_Photon20") == 0 ){
        Photon_fired |= triggerBits->accept(i);
      }
    }
    bfireMET105IsoTrk50 = MET_IsoTrk_fired;
    bfirePhoton20 = Photon_fired;   
    //cout << "MET_IsoTrk_fired" << MET_IsoTrk_fired << "  Photon_fired" << Photon_fired << endl;
    MET105IsoTrk50vsPhoton20->Fill(MET_IsoTrk_fired,Photon_fired);   

    vector<pat::TriggerObjectStandAlone> hltEgammaCands;
    double hltEgammaPtMax = 0.0;
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
      hltegammaCandPt->Fill(0.0);
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
      hltmetPt->Fill(0.0);
      bHltmetPt = 0.0;
      hltmetPtVsphotonPt->Fill(0.0,photonPtMax);
      hltmetPtVshltegammaCandPt->Fill(0.0,hltEgammaPtMax);
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

//define this as a plug-in
DEFINE_FWK_MODULE(HLTrigVarProducer);
