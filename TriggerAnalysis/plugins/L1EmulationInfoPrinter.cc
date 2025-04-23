// -*- C++ -*-
//
// Package:    TriggerAnalysis/L1EmulationInfoPrinter
// Class:      L1EmulationInfoPrinter
//
/*
 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Kai Wei
//         Created:  Wed, 17 Jun 2021 03:08:39 GMT
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
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/L1Trigger/interface/L1EtMissParticleFwd.h"
#include "DataFormats/L1Trigger/interface/L1EtMissParticle.h"
#include "DataFormats/L1Trigger/interface/EtSum.h"
#include "DataFormats/L1Trigger/interface/Jet.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

#include "DataFormats/L1TGlobal/interface/GlobalObjectMapFwd.h"
#include "DataFormats/L1TGlobal/interface/GlobalObjectMap.h"
#include "DataFormats/L1TGlobal/interface/GlobalObjectMapRecord.h"
#include "DataFormats/L1TGlobal/interface/GlobalObject.h"
#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

//
// class declaration
//
using namespace std;
using namespace pat;
using namespace l1t;
using namespace reco;
class L1EmulationInfoPrinter : public edm::stream::EDAnalyzer<> {
   public:
      explicit L1EmulationInfoPrinter(const edm::ParameterSet&);
      ~L1EmulationInfoPrinter();
      bool passJetTightLepVeto(const reco::PFJet &jet) const;

   private:
      void beginJob();
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      void endJob();


      // ----------member data ---------------------------
      edm::EDGetTokenT<reco::VertexCollection> tokenVertices_;
      edm::EDGetTokenT<edm::TriggerResults> tokenTriggerBits_;
      edm::EDGetTokenT<L1GlobalTriggerReadoutRecord> tokenL1GtBits_;
      edm::EDGetTokenT<l1t::EtSumBxCollection> tokenL1SumEt_;
      edm::EDGetTokenT<l1t::JetBxCollection> tokenL1Jets_;
      edm::EDGetTokenT<GlobalObjectMapRecord> tokenl1GtObjectMap_;

      edm::EDGetTokenT<reco::PFMETCollection> tokenPFMET_;
      edm::EDGetTokenT<reco::PFJetCollection> tokenPFJets_;
      edm::EDGetTokenT<reco::MuonCollection> tokenRecoMuons_;

      edm::InputTag algInputTag_;
      edm::EDGetTokenT<GlobalAlgBlkBxCollection> algToken_;

      std::vector<string> algoNames;
      std::map<string, bool> algoFired;
      //used to select what tracks to read from configuration file
  private:
      // output file
      edm::Service<TFileService> fs_;
      // tree
      TTree* tree_;
      bool                 isGoodPV;          
      double               L1ETMHFPt;
      double               L1ETMHFPhi;
      std::vector<double>  L1JetPt;
      std::vector<double>  L1JetPhi;
      std::vector<double>  L1dPhiJetMet;
      double               L1HTT;
      double               PFMetPt;
      double               PFMetNoMuPt;
      double               PFMetNoMuPhi;
      std::vector<double>  PFJetPt;
      std::vector<double>  PFJetEta;
      std::vector<double>  PFJetPhi;
      std::vector<double>  PFJetTightLepVeto;
      bool                 passL1EmuSelection;
      bool                 passOfflineSelection;
/*
      TBranch              *b_L1ETMHFPt;
      TBranch              *b_L1ETMHFPhi;
      TBranch              *b_L1JetPt;
      TBranch              *b_L1JetPhi;
      TBranch              *b_L1dPhiJetMet;
      TBranch              *b_L1HTT;
      TBranch              *b_PFMetPt;
      TBranch              *b_PFMetNoMuPt;
      TBranch              *b_PFJetPt;
      TBranch              *b_PFJetEta;
      TBranch              *b_PFJetPhi;
      TBranch              *b_passL1EmuSelection;
      TBranch              *b_passOfflineSelection;*/
      double l1ETMHFThreshold_;
      double l1HTTThreshold_;
      double l1JetPtThreshold_;
      double dPhi_l1ETM_l1Jet_min_;
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
L1EmulationInfoPrinter::L1EmulationInfoPrinter(const edm::ParameterSet& cfg)
{
  tokenTriggerBits_  = consumes<edm::TriggerResults>(cfg.getParameter<edm::InputTag>("triggers"));
  tokenL1GtBits_     = consumes<L1GlobalTriggerReadoutRecord>(cfg.getParameter<edm::InputTag>("l1GtBits"));
  tokenL1SumEt_        = consumes<l1t::EtSumBxCollection>(cfg.getParameter<edm::InputTag>("sumEt"));
  tokenL1Jets_         = consumes<l1t::JetBxCollection>(cfg.getParameter<edm::InputTag>("jets"));
  tokenl1GtObjectMap_   = consumes<GlobalObjectMapRecord>(cfg.getParameter<edm::InputTag>("L1ObjectMapInputTag"));
  algInputTag_       = cfg.getParameter<edm::InputTag>("AlgInputTag");
  algToken_          = consumes<GlobalAlgBlkBxCollection>(algInputTag_);

  //  For RECO collections
  tokenVertices_   = consumes<reco::VertexCollection>(cfg.getParameter<edm::InputTag>("vertices"));
  tokenPFMET_      = consumes<reco::PFMETCollection>(cfg.getParameter<edm::InputTag>("pfMet"));
  tokenPFJets_     = consumes<reco::PFJetCollection>(cfg.getParameter<edm::InputTag>("pfJets"));
  tokenRecoMuons_  = consumes<reco::MuonCollection>(cfg.getParameter<edm::InputTag>("recoMuons"));

  l1ETMHFThreshold_       = cfg.getUntrackedParameter<double>("l1etmhfThreshold");
  l1HTTThreshold_         = cfg.getUntrackedParameter<double>("l1httThreshold");
  l1JetPtThreshold_       = cfg.getUntrackedParameter<double>("l1jetThreshold");
  dPhi_l1ETM_l1Jet_min_   = cfg.getUntrackedParameter<double>("mindPhiETMHFJet");

   //now do what ever initialization is needed
   tree_ = fs_->make<TTree>("L1EmuTree", "L1EmuTree");
   tree_->Branch("isGoodPV", &isGoodPV);
   tree_->Branch("L1ETMHFPt", &L1ETMHFPt);
   tree_->Branch("L1ETMHFPhi", &L1ETMHFPhi);
   tree_->Branch("L1JetPt", &L1JetPt);
   tree_->Branch("L1JetPhi", &L1JetPhi);
   tree_->Branch("L1dPhiJetMet", &L1dPhiJetMet);
   tree_->Branch("L1HTT", &L1HTT);
   tree_->Branch("PFMetPt", &PFMetPt);
   tree_->Branch("PFMetNoMuPt", &PFMetNoMuPt);
   tree_->Branch("PFMetNoMuPhi", &PFMetNoMuPhi);
   tree_->Branch("PFJetPt", &PFJetPt);
   tree_->Branch("PFJetEta", &PFJetEta);
   tree_->Branch("PFJetPhi", &PFJetPhi);
   tree_->Branch("PFJetTightLepVeto",&PFJetTightLepVeto);
   tree_->Branch("passL1EmuSelection", &passL1EmuSelection);
   tree_->Branch("passOfflineSelection", &passOfflineSelection);

}


L1EmulationInfoPrinter::~L1EmulationInfoPrinter()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
L1EmulationInfoPrinter::analyze(const edm::Event& event, const edm::EventSetup& setup)
{
    using namespace std;
  
    edm::Handle<reco::VertexCollection> vertices;
    event.getByToken(tokenVertices_, vertices);

    if (!vertices.isValid()) {
      edm::LogWarning("L1EmulationInfoPrinter") << "invalid collection: Vertices " << std::endl;
    }
    isGoodPV = false;
    const reco::Vertex &pv = vertices->at(0);
    isGoodPV = pv.isValid() > 0 &&
               pv.ndof() >= 4 && 
               fabs (pv.z()) < 24.0 && 
               sqrt (pv.x() * pv.x() + pv.y() * pv.y()) < 2.0;

    /*
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<L1GlobalTriggerReadoutRecord > l1gtBits;

    event.getByToken(tokenL1GtBits_, l1gtBits);

    if(l1gtBits.isValid()){
      cout << "Valid L1 global trigger bits found..." <<  endl;
      const TechnicalTriggerWord& gtTechnicalTriggerWord  =  l1gtBits->technicalTriggerWord();
      const DecisionWord& gtDecisionWord = l1gtBits->decisionWord(); 
      cout << "nTechnicalTrigger:" << gtTechnicalTriggerWord.size() << endl;
      cout << "nDecisionWord:" << gtDecisionWord.size() << endl;
    }

    edm::Handle<GlobalObjectMapRecord> gtObjectMapRecord;
    event.getByToken(tokenl1GtObjectMap_, gtObjectMapRecord);
    edm::Handle<GlobalAlgBlkBxCollection> alg;
    event.getByToken(algToken_, alg);

    if (!gtObjectMapRecord.isValid()) {
     std::cout << " Warning: GlobalObjectMapRecord with input tag " 
                                   << " requested in configuration, but not found in the event." << std::endl;
 
     return;
    }
 
    const std::vector<GlobalObjectMap>& objMaps = gtObjectMapRecord->gtObjectMap();
 
    std::cout << "\nHLTL1Seed"
                            << "\n--------------------------------------------------------------------------------------"
                               "-------------------------------"<< std::endl;
 
    std::cout
         << "\n\tAlgorithms in L1TriggerObjectMapRecord and GT results ( emulated | initial | prescaled | final ) "
         << std::endl;
 
    std::cout << "\n\tmap"
                            << "\tAlgoBit" << std::setw(40) << "algoName"
                            << "\t (emul|ini|pre|fin)" << std::endl;
 
    std::cout << "----------------------------------------------------------------------------------------"
                               "-----------------------------" << std::endl;
 
    for (size_t imap = 0; imap < objMaps.size(); imap++) {
      int bit = objMaps[imap].algoBitNumber();  //  same as bit from L1T Menu

      int emulDecision = objMaps[imap].algoGtlResult();
 
      // For bx=0 , get 0th AlgoBlock, so in BXvector at(bx=0,i=0)
      int initDecision = (alg->at(0, 0)).getAlgoDecisionInitial(bit);
      int presDecision = (alg->at(0, 0)).getAlgoDecisionInterm(bit);
      int finlDecision = (alg->at(0, 0)).getAlgoDecisionFinal(bit);
 
      if (emulDecision != initDecision) {
        std::cout << "L1T decision (emulated vs. unpacked initial) is not the same:"
                               << "\n\tbit = " << std::setw(3) << bit << std::setw(40) << objMaps[imap].algoName()
                               << "\t emulated decision = " << emulDecision
                               << "\t unpacked initial decision = " << initDecision
                               << "\nThis should not happen. Include the L1TGtEmulCompare module in the sequence."
                               << std::endl;
      }
 
      std::cout << "\t" << std::setw(3) << imap << "\tbit = " << std::setw(3) << bit << std::setw(40)
                             << objMaps[imap].algoName() << "\t (  " << emulDecision << " | " << initDecision << " | "
                             << presDecision << " | " << finlDecision << " ) ";
    }
    std::cout << endl;
    */
    L1ETMHFPt    = -1;
    L1ETMHFPhi   = 9.9;
    L1HTT        = -1;
    PFMetPt      = -1;
    PFMetNoMuPt  = -1;
    PFMetNoMuPhi = 9.9;
    
    PFJetPt.clear();
    PFJetEta.clear();
    PFJetPhi.clear();
    L1JetPt.clear();
    L1JetPhi.clear();
    L1dPhiJetMet.clear();
    PFJetTightLepVeto.clear();
    passL1EmuSelection = false;
    passOfflineSelection = false;

    int bunchCrossing = 0;

    edm::Handle<l1t::EtSumBxCollection> l1EtSums;
    event.getByToken(tokenL1SumEt_, l1EtSums);

    if(l1EtSums.isValid()){
      for (auto etSum = l1EtSums->begin(bunchCrossing); etSum != l1EtSums->end(bunchCrossing); ++etSum) {
        double et = etSum->et();
        double phi = etSum->phi();

        switch (etSum->getType()) {
          case l1t::EtSum::EtSumType::kMissingEtHF:
            L1ETMHFPt = et;
            L1ETMHFPhi = phi;
            break;
          case l1t::EtSum::EtSumType::kTotalHt:
            L1HTT = et;
          default:
            break;
        }
      }
    }
    //std::cout << "l1ETMHF:" << L1ETMHFPt << "\tl1ETMHFPhi:" << L1ETMHFPhi << "\tl1HTT:" << L1HTT <<std::endl;

    edm::Handle<l1t::JetBxCollection> l1Jets;
    event.getByToken(tokenL1Jets_, l1Jets);

    if (!l1Jets.isValid()) {
      edm::LogWarning("L1TStage2CaloLayer2Offline") << "invalid collection: L1 jets " << std::endl;
      return;
    }

    for (auto jet = l1Jets->begin(bunchCrossing); jet != l1Jets->end(bunchCrossing); ++jet) {
        L1JetPt.push_back(jet->pt());
        L1JetPhi.push_back(jet->phi());
        double currentDeltaPhi = fabs(deltaPhi(jet->phi(), L1ETMHFPhi));
        L1dPhiJetMet.push_back(currentDeltaPhi);
        if (L1HTT > l1HTTThreshold_ && L1ETMHFPt > l1ETMHFThreshold_ && jet->pt() > l1JetPtThreshold_ && currentDeltaPhi > dPhi_l1ETM_l1Jet_min_){
          passL1EmuSelection = true;
        }
    }

    edm::Handle<reco::PFMETCollection> pfMET;
    edm::Handle<reco::PFJetCollection> pfJets;
    edm::Handle<reco::MuonCollection>  recoMuons;

    event.getByToken(tokenPFMET_, pfMET);
    event.getByToken(tokenPFJets_, pfJets);
    event.getByToken(tokenRecoMuons_, recoMuons);

    PFMetPt = pfMET->front().pt();
    TVector2 metNoMuVec(pfMET->front().px(), pfMET->front().py());
    for (auto muon = recoMuons->begin(); muon != recoMuons->end(); ++muon) {
      TVector2 muonVec(muon->px(), muon->py());
      metNoMuVec += muonVec;
    }
    PFMetNoMuPt = metNoMuVec.Mod();
    PFMetNoMuPhi = metNoMuVec.Phi();

    bool passJetSeletion = false;
    double leadingJetPhi = 9.9;
    double leadingJetPt  = -1.0;

    for (auto jet = pfJets->begin(); jet != pfJets->end(); ++jet) {
      if (jet->et() > leadingJetPt) {
        leadingJetPt  = jet->et();
        leadingJetPhi = jet->phi();
      }
      PFJetPt.push_back(jet->et());
      PFJetEta.push_back(jet->eta());
      PFJetPhi.push_back(jet->phi());
      bool jetTightLepVeto = passJetTightLepVeto(*jet);
      PFJetTightLepVeto.push_back(jetTightLepVeto);
      if (jet->et() > 110 && fabs(jet->eta()) < 2.4 && jetTightLepVeto && PFMetNoMuPt > 120) {
        passJetSeletion = true;
      }
    }
    bool passLeadingJetMetPhi = leadingJetPhi > 5.0 ? true : fabs(deltaPhi(PFMetNoMuPhi,leadingJetPhi)) > 0.5;
    passOfflineSelection = passJetSeletion && passLeadingJetMetPhi && isGoodPV;

    tree_->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void
L1EmulationInfoPrinter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
L1EmulationInfoPrinter::endJob()
{
  //  l1ETMHFEff = (TH1D*) l1ETMHFPt->Clone("l1ETMHFEff");
  //  l1ETMHFEff->Divide(metPt);
  //  l1ETMHFEff->Write();

}

// ------------ method called when starting to processes a run  ------------
/*
void
L1EmulationInfoPrinter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
L1EmulationInfoPrinter::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
L1EmulationInfoPrinter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
L1EmulationInfoPrinter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

/*
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
L1EmulationInfoPrinter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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

bool L1EmulationInfoPrinter::getHLTObj(const edm::Event &event,
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

bool L1EmulationInfoPrinter::isGoodTrack(const pat::IsolatedTrack &track,
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
}*/

bool L1EmulationInfoPrinter::passJetTightLepVeto(const reco::PFJet& jet) const {
  bool result = anatools::jetPassesTightLepVeto(jet); // This automatically uses the correct jet ID criteria
  return result;
}
//define this as a plug-in
DEFINE_FWK_MODULE(L1EmulationInfoPrinter);
