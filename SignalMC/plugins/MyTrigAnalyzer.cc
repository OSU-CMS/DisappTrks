// -*- C++ -*-
//
// Package:    Demo/MyTrigAnalyzer
// Class:      MyTrigAnalyzer
// 
/**\class MyTrigAnalyzer MyTrigAnalyzer.cc Demo/MyTrigAnalyzer/plugins/MyTrigAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Jessica Brinson
//         Created:  Tue, 19 Aug 2014 13:15:39 GMT
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

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

//
// class declaration
//

class MyTrigAnalyzer : public edm::EDAnalyzer {
   public:
      explicit MyTrigAnalyzer(const edm::ParameterSet&);
      ~MyTrigAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
  edm::Handle<reco::PFMETCollection> mets;
  edm::Handle<reco::GenMETCollection> genMets;
  edm::Handle<reco::CaloMETCollection> hltmets;
  edm::Handle<reco::GenParticleCollection> genParts;
  edm::Handle<l1extra::L1EtMissParticleCollection> l1mets;


      // ----------member data ---------------------------
  edm::InputTag trackTags_; 
  edm::InputTag hltTrackTags_; 
  edm::InputTag muonTags_; 
  edm::InputTag genPartTags_;
  edm::InputTag metTags_;
  edm::InputTag genMetTags_;
  edm::InputTag hltmetTags_;
  edm::InputTag triggerResultsTag_;
  edm::EDGetToken hltmetToken_;
  bool trigOn_;
  edm::TriggerNames trigNames;
  edm::InputTag l1metTags_;

//used to select what tracks to read from configuration file
  TH1D * trackPt; 
  TH1D * trackRes; 
  TH1D * trackDeltaR; 
  TH1D * hltTrackPt; 
  TH1D * metPt; 
  TH1D * genMetPt; 
  TH1D * hltmetPt; 
  TH1D * l1metPt; 
  TH1D * trackEta; 
  TH2D * hltMetVsGenMet; 
  TH2D * pfMetVsGenMet; 
  TH2D * pfMetVsHltMet; 
  TH2D * pfMetVsL1Met; 
  TH2D * trackPtVsHltTrackPt; 
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
MyTrigAnalyzer::MyTrigAnalyzer(const edm::ParameterSet& iConfig)
 :
  trackTags_(iConfig.getUntrackedParameter<edm::InputTag>("tracks")),
  hltTrackTags_(iConfig.getUntrackedParameter<edm::InputTag>("hltTracks")),
  muonTags_(iConfig.getUntrackedParameter<edm::InputTag>("muons")),
  genPartTags_(iConfig.getUntrackedParameter<edm::InputTag>("genParts")),
  metTags_(iConfig.getUntrackedParameter<edm::InputTag>("mets")),
  genMetTags_(iConfig.getUntrackedParameter<edm::InputTag>("genMets")),
  hltmetTags_(iConfig.getUntrackedParameter<edm::InputTag>("hltmets")),
  triggerResultsTag_(iConfig.getUntrackedParameter<edm::InputTag>("triggerResults")),
  hltmetToken_(consumes<reco::CaloMETCollection>(iConfig.getUntrackedParameter<edm::InputTag>("hltmets"))),
  trigOn_(iConfig.getUntrackedParameter<bool>("trigOn")),
  l1metTags_(iConfig.getUntrackedParameter<edm::InputTag>("l1mets"))

{
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;
  //use variable binning for met histograms (determined empirically)

  float bins[] = {0, 25, 50, 75, 100, 125, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
 int binnum = 15;

trackPt = fs->make<TH1D>("pt" , "pT; track pT [GeV]" , 100 , 0 , 500 );
trackRes = fs->make<TH1D>("res" , "res; hlt track pT - track pT/ track pT [GeV]" , 100 , -5 , 5 );
trackDeltaR = fs->make<TH1D>("dR" , "dR; deltaR" , 100 , 0 , 5 );
hltTrackPt = fs->make<TH1D>("hltPt" , "pT; HLT track pT [GeV]" , 100 , 0 , 500 );
 metPt = fs->make<TH1D>("met" , "met pT; MET [GeV}" , binnum, bins );
 genMetPt = fs->make<TH1D>("genMet" , "gen met pT; GenMET [GeV]" , binnum, bins );
 hltmetPt = fs->make<TH1D>("hltmet" , "hlt met pT; hltMET [GeV]" , binnum, bins );
 l1metPt = fs->make<TH1D>("l1met" , "l1 met pT; L1 MET [GeV]" , binnum , bins );
 trackEta = fs->make<TH1D>("eta" , "eta; track  #eta" , 100 , -3.14 , 3.14 );
 hltMetVsGenMet = fs->make<TH2D>("hltMetVsGenMet" , "hltMet vs Gen MET; Gen MET [GeV]; hltMET [GeV]" , binnum , bins, binnum, bins );
 pfMetVsGenMet = fs->make<TH2D>("pfMetVsGenMet" , "pfMet vs Gen MET; Gen MET [GeV]; PF MET [GeV]" , binnum , bins, binnum, bins );
 pfMetVsHltMet = fs->make<TH2D>("pfMetVsHltMet" , "pfMet vs HLT MET; HLT MET [GeV]; PF MET [GeV]" , binnum , bins, binnum, bins );
 pfMetVsL1Met = fs->make<TH2D>("pfMetVsL1Met" , "pfMet vs L1 MET; L1 MET [GeV]; PF MET [GeV]" , binnum , bins, binnum, bins );
 trackPtVsHltTrackPt = fs->make<TH2D>("trackPtVsHltTrackPt" , "track pT vs HLT track pT; track pT [GeV]; HLT track pT [GeV]" , binnum , bins, binnum, bins );

}


MyTrigAnalyzer::~MyTrigAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MyTrigAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   using reco::TrackCollection;
   using reco::MuonCollection;
   using reco::PFMETCollection;
   using reco::GenMETCollection;
   using reco::CaloMETCollection;
   using l1extra::L1EtMissParticleCollection;
   using reco::GenParticleCollection;

    Handle<TrackCollection> tracks;
    Handle<TrackCollection> hltTracks;
    Handle<MuonCollection> muons;
    Handle<TriggerResults> hltresults;

    iEvent.getByLabel(trackTags_,tracks);
    iEvent.getByLabel(hltTrackTags_,hltTracks);
    iEvent.getByLabel(muonTags_,muons);
    iEvent.getByLabel(genPartTags_,genParts);
    iEvent.getByLabel(metTags_,mets);
    iEvent.getByLabel(genMetTags_,genMets);
    iEvent.getByLabel(triggerResultsTag_,hltresults);
    iEvent.getByLabel("hltL1extraParticles","MET", l1mets);
    if (trigOn_) iEvent.getByToken(hltmetToken_, hltmets);

    //list triggers included in file
    const edm::TriggerNames & trigNames = iEvent.triggerNames(*hltresults);
    unsigned int numTriggers = trigNames.size();

    for( unsigned int hltIndex=0; hltIndex<numTriggers-1; ++hltIndex ){
      std::string currentTrigName = trigNames.triggerName(hltIndex);
      std::cout << "Trigger = " << currentTrigName << std:: endl;
    }

    double ptMax = -99;
    double deltaRTemp = -99;
    double hltPtMax = -99;
    double etaTrk = -99;
    int numMu = 0;
    for(MuonCollection::const_iterator itMu = muons->begin();
        itMu != muons->end();
        ++itMu) {
      if (itMu->pt() < 50) continue;
      numMu++;
    }
        if (numMu == 0) {
    
    //fill met histograms
    metPt->Fill(mets->front().pt());
    std::cout<<"******************************************" << std::endl; 
   if (mets->front().pt() > 300) std::cout << "EVENT HAS > 300 MET: " << std:: endl; 
    std::cout << "PF MET in this event = " << mets->front().pt() << std::endl;
    genMetPt->Fill(genMets->front().pt());
    if (trigOn_)  hltmetPt->Fill(hltmets->front().pt());
    std::cout << "HLT MET in this event = " << hltmets->front().pt() << std::endl;
    l1metPt->Fill(l1mets->front().pt());
    std::cout << "L1 MET in this event = " << l1mets->front().pt() << std::endl;
    std::cout<<"******************************************" << std::endl; 
    hltMetVsGenMet->Fill( genMets->front().pt(), hltmets->front().pt());
    pfMetVsGenMet->Fill( genMets->front().pt(), mets->front().pt());
    pfMetVsHltMet->Fill( hltmets->front().pt(), mets->front().pt());
    pfMetVsL1Met->Fill( l1mets->front().pt(), mets->front().pt());

    for(TrackCollection::const_iterator itTrack = tracks->begin();
        itTrack != tracks->end();                      
        ++itTrack) {
      
      double ptTemp = itTrack->pt();
      if(ptTemp > ptMax) {
	ptMax = ptTemp;
	etaTrk = itTrack->eta();
	for(TrackCollection::const_iterator ithltTrack = hltTracks->begin();
	    ithltTrack != hltTracks->end();
	    ++ithltTrack) {
	  deltaRTemp = deltaR (itTrack->eta(), itTrack->phi(), ithltTrack->eta(), ithltTrack->phi());
	  if (deltaR (itTrack->eta(), itTrack->phi(), ithltTrack->eta(), ithltTrack->phi())< 0.005){
	  std::cout << "Track eta, phi = " << itTrack->eta() << ", " << itTrack->phi() << std::endl;
	  std::cout << "hlt Track eta, phi = " << ithltTrack->eta() << ", " << ithltTrack->phi() << std::endl;
	    std::cout << "DeltaR between track pT and hlt track pT = " << deltaR (itTrack->eta(), itTrack->phi(), ithltTrack->eta(), ithltTrack->phi()) << std::endl;
	    	    std::cout << "ptMax = " << ptMax<< std::endl;
	    hltPtMax = ithltTrack->pt();
	    std::cout << "hltPtMax = " << hltPtMax<< std::endl;
	    if (hltPtMax < 100 && ptMax > 100 ) std::cout << "PT MISMATCH" << std::endl;
	     }
	  
	}
      }
    }
    
    trackPt->Fill( ptMax );
    trackEta->Fill( etaTrk );
    trackDeltaR->Fill(deltaRTemp);    
    hltTrackPt->Fill( hltPtMax );
    trackPtVsHltTrackPt->Fill( ptMax, hltPtMax );
    trackRes->Fill( (hltPtMax - ptMax)/ptMax);
    }
#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
MyTrigAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MyTrigAnalyzer::endJob() 
{
  //  l1metEff = (TH1D*) l1metPt->Clone("l1metEff");
  //  l1metEff->Divide(metPt);
  //  l1metEff->Write();

}

// ------------ method called when starting to processes a run  ------------
/*
void 
MyTrigAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
MyTrigAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
MyTrigAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
MyTrigAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MyTrigAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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

//define this as a plug-in
DEFINE_FWK_MODULE(MyTrigAnalyzer);
