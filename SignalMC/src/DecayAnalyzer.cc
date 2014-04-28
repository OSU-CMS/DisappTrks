// -*- C++ -*-
//
// Package:    DecayAnalyzer
// Class:      DecayAnalyzer
// 
/**\class DecayAnalyzer DecayAnalyzer.cc Demo/DecayAnalyzer/src/DecayAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Howard Wells Wulsin,42 2-034,+41227662377,
//         Created:  Thu Mar  6 13:08:46 CET 2014
// $Id$
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

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH2D.h"
#include "TH1D.h"
#include "TLorentzVector.h"

#include <ext/algorithm>  // For sorting?  

//
// class declaration
//

using namespace std;  


class DecayAnalyzer : public edm::EDAnalyzer {
   public:
      explicit DecayAnalyzer(const edm::ParameterSet&);
      ~DecayAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

  TH1D *hCharginoSumPt;

  TH1D* hnVtxCharginoToNeutralino;  
  TH1D* hnVtxCharginoParent;
  TH1D* hnGenCharginoTot;
  TH1D* hnGenCharginoSel;

  TH1D* hnCharginoNoDecay;
  TH1D* hMissingVtx;  
  TH1D* hnumdgt;  

  TH1D* hvxy; 		
  TH1D* hvx; 		
  TH1D* hvy; 		
  TH1D* hvz; 		
  TH2D* hvxyz; 	
  TH1D* hdecayVxy; 	
  TH1D* hdecayVx; 	
  TH1D* hdecayVy; 	
  TH1D* hdecayVz; 	
  TH2D* hdecayVxyz; 	
  TH2D* hdecayVxyzWide; 	
  TH1D* hdecayLength; 	
  TH1D* hctau; 	

  TH1D* hdaughter0Id;
  TH1D* hdaughter0E;
  TH1D* hdaughter1Id;
  TH1D* hdaughter1E;
  TH1D* hEDiff; 

  TH1D* hCharginoPt;

  TH1D* hGenEta;
  TH1D* hGenEtaSel;
  TH1D* hGenEtaFoundVtx; 


  edm::InputTag genParticleTag_;  

  bool isParticleGun_;  
  double MaxEta_;  


  struct LessById {
    bool operator()(const SimTrack &tk1, const SimTrack &tk2) const { return tk1.trackId() < tk2.trackId(); }
    bool operator()(const SimTrack &tk1, unsigned int    id ) const { return tk1.trackId() < id;            }
    bool operator()(unsigned int     id, const SimTrack &tk2) const { return id            < tk2.trackId(); }
  };
  
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
DecayAnalyzer::DecayAnalyzer(const edm::ParameterSet& iConfig)


{

  genParticleTag_ = iConfig.getParameter<edm::InputTag>("genParticleTag");
  isParticleGun_  = iConfig.getUntrackedParameter<bool>("isParticleGun", false);  
  MaxEta_         = iConfig.getUntrackedParameter<double>("MaxEta", 2.5);  
  
  
  //now do what ever initialization is needed
  edm::Service<TFileService> fs;  
  hCharginoSumPt = fs->make<TH1D>("hCharginoSumPt" , ";p_{T}^{#chi#chi}" , 100 , 0 , 500 );
  hCharginoPt = fs->make<TH1D>("hCharginoPt" , ";#chi^{#pm} p_{T} [GeV]" , 100, 0, 500);  
  hnVtxCharginoToNeutralino = fs->make<TH1D>("hnVtxCharginoToNeutralino" , ";# vertices with #chi^{#pm} parent and #chi^{0} daughter" , 10 , -0.5 , 9.5 );
  hnVtxCharginoParent = fs->make<TH1D>("hnVtxCharginoParent" , ";# vertices with #chi^{#pm} parent" , 10 , -0.5 , 9.5 );
  hnGenCharginoTot = fs->make<TH1D>("hnGenCharginoTot" , ";# total generated #chi^{#pm}" , 10 , -0.5 , 9.5 );
  hnGenCharginoSel = fs->make<TH1D>("hnGenCharginoSel" , ";# selected generated #chi^{#pm}" , 10 , -0.5 , 9.5 );
  hMissingVtx = fs->make<TH1D>("hMissingVtx" , ";# missing #chi^{#pm} vertices" , 10 , -0.5 , 9.5 );
  hGenEta = fs->make<TH1D>("hGenEta" , ";#eta, generated #chi^{#pm}" , 100 , -7, 7);
  hGenEtaSel = fs->make<TH1D>("hGenEtaSel" , ";#eta, selected #chi^{#pm}" , 100 , -7, 7);
  hGenEtaFoundVtx = fs->make<TH1D>("hGenEtaFoundVtx" ,    ";#eta, generated #chi^{#pm} with decay vertex" , 100 , -7, 7);

  hnCharginoNoDecay = fs->make<TH1D>("hnCharginoNoDecay" ,    ";# generated #chi^{#pm} with no decay" , 10 , -0.5 , 9.5 );
  hnumdgt = fs->make<TH1D>("hnumdgt" ,    ";# daughters of #chi^{#pm}" , 10 , -0.5 , 9.5 );

  hvxy = fs->make<TH1D>("hvxy", "vxy", 100, 0, 5);
  hvx = fs->make<TH1D>("hvx", "vx", 100, 0, 5);
  hvy = fs->make<TH1D>("hvy", "vy", 100, 0, 5);
  hvz = fs->make<TH1D>("hvz", "vz", 100, 0, 50);
  hvxyz = fs->make<TH2D>("hvxyz", ";vz;vxy", 100, 0, 50, 100, 0, 5);
  hdecayVxy = fs->make<TH1D>("hdecayVxy", "decayVxy", 100, 0, 1000);
  hdecayVx = fs->make<TH1D>("hdecayVx", "decayVx", 100, 0, 1000);
  hdecayVy = fs->make<TH1D>("hdecayVy", "decayVy", 100, 0, 1000);
  hdecayVz = fs->make<TH1D>("hdecayVz", "decayVz", 100, 0, 1500);
  hdecayVxyz = fs->make<TH2D>("hdecayVxyz",  "Position of #chi^{#pm}#rightarrow#chi^{0}#pi^{#pm} decay ;|z| [cm];|#rho| [cm]" , 100, 0, 1500, 100, 0, 1000);
  hdecayVxyzWide = fs->make<TH2D>("hdecayVxyzWide",  "Position of #chi^{#pm}#rightarrow#chi^{0}#pi^{#pm} decay ;|z| [cm];|#rho| [cm]" , 100, 0, 3000, 100, 0, 1500);
  hdecayLength = fs->make<TH1D>("hdecayLength", "decayLength", 100, 0, 1000);
  hctau = fs->make<TH1D>("ctau", ";c#tau [cm]", 100, 0, 1000); 
//   hctauDiffSmall = fs->make<TH1D>("hctauDiffSmall", ";c#tau [cm]", 100, 0, 1000); 
//   hctauDiffLarge = fs->make<TH1D>("hctauDiffLarge", ";c#tau [cm]", 100, 0, 1000); 
  
  hdaughter0Id = fs->make<TH1D>("hdaughter0Id", ";daughter 0 PDG ID", 100, 1000020, 1000030); 
  hdaughter1Id = fs->make<TH1D>("hdaughter1Id", ";daughter 1 PDG ID", 100, 200, 220);  
  hdaughter0E  = fs->make<TH1D>("hdaughter0E",  ";daughter 0 energy [GeV]", 100, 0, 1000);  
  hdaughter1E  = fs->make<TH1D>("hdaughter1E", ";daughter 1 energy [GeV]", 100, 0, 500);  
  hEDiff       = fs->make<TH1D>("hEDiff", ";(total daughters' energy) - (chargino energy) [GeV]", 100, -150, 150);  
//   hEDiffSmall  = fs->make<TH1D>("hEDiffSmall", ";(total daughters' energy) - (chargino energy) [GeV]", 100, -150, 150);  
//   hEDiffLarge  = fs->make<TH1D>("hEDiffLarge", ";(total daughters' energy) - (chargino energy) [GeV]", 100, -150, 150);  

}


DecayAnalyzer::~DecayAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}




//
// member functions
//

// ------------ method called for each event  ------------
void
DecayAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   Handle<reco::GenParticleCollection > genParticles;
   iEvent.getByLabel(genParticleTag_,genParticles); 
   //   iEvent.getByLabel("genParticles",genParticles);

   TLorentzVector pTot(0,0,0,0);  
   int nGenCharginoTot = 0;  
   int nCharginoNoDecay = 0;  
   int nGenCharginoSel = 0; 
   int nVtxCharginoToNeutralino = 0;  

   double vxy;
   double vx;
   double vy;
   double vz;
   double decayVxy;
   double decayVx;
   double decayVy;
   double decayVz;
   double decayLength;
   double ctau;  

   cout << "checking gen particles, size = " << genParticles->size() << endl;  


   if (genParticles.isValid()) {
     for( size_t k = 0; k < genParticles->size(); k++ ){
       const reco::Candidate & mcParticle = (*genParticles)[k];

       int status = mcParticle.status();
       int pdgId  = mcParticle.pdgId();
       int numdgt = mcParticle.numberOfDaughters();

       // copy code from BEANmaker.cc:
       if (!isParticleGun_) {
	 if (!((mcParticle.status()==3 &&                // BNstop must be from a status 3 particle, either:  
		(abs (mcParticle.pdgId ()) == 1000006 || // stop, 
		 abs (mcParticle.pdgId ()) == 1000015 || // stau, 
		 abs (mcParticle.pdgId ()) == 1000024))))  // or chargino 
	   continue;
       } else {
	 if (!((mcParticle.status()==1 &&                // particle gun particle should be status 1  
		(abs (mcParticle.pdgId ()) == 1000006 || // stop, 
		 abs (mcParticle.pdgId ()) == 1000015 || // stau, 
		 abs (mcParticle.pdgId ()) == 1000024))))  // or chargino 
	   continue;
       }

//        if (!(abs(pdgId)==1000022 ||
//              abs(pdgId)==1000024)) continue;

//        if (!(status==3)) continue;  

       nGenCharginoTot++;   

       hGenEta->Fill(mcParticle.eta());
       if (fabs(mcParticle.eta()) > MaxEta_) continue;  
       
       nGenCharginoSel++;
       hGenEtaSel->Fill(mcParticle.eta());
       
       cout << "Found gen particle with:  "
	    << " pt = " << mcParticle.pt()
	    << ", eta = " << mcParticle.eta()
	    << ", status=" << status 
	    << "; pdgId=" << pdgId
	    << "; numdgt=" << numdgt << endl;
       TLorentzVector p4(mcParticle.px(), 
			 mcParticle.py(), 
			 mcParticle.pz(), 
			 mcParticle.energy());  
       pTot += p4;  

       hCharginoPt->Fill(p4.Pt());  

       vx = mcParticle.vx();
       vy = mcParticle.vy();
       vz = mcParticle.vz();
       vxy = sqrt(vx*vx + vy*vy);

       const reco::Candidate *mother   = &mcParticle;
       const reco::Candidate *daughter = &mcParticle;

       // Descend the decay chain until no daughters have the same PDG ID as mcParticle.                                                                                                               
       while (true) {
	 bool foundDauSamePdgId = false;
	 for (uint i=0; i<daughter->numberOfDaughters(); i++) {
	   if (daughter->daughter(i)->pdgId() == mcParticle.pdgId()) {
	     foundDauSamePdgId = true;
	     mother = daughter;
	     daughter = daughter->daughter(i);
	     break;
	   }
	 }
	 if (!foundDauSamePdgId) break;
       }
       // Now daughter has no daughters with the same PDG ID as mcParticle.                                                                                                                            
       // Next choose the daughter with the outermost production vertex, in case there are multiple vertices
       // (e.g., an electron delta ray can produce a vertex before the decay vertex)  
       double radiusLastVtx = -99;  
       int idxDauLastVtx = -99;  
       for (uint i=0; i<daughter->numberOfDaughters(); i++) {
	 double testVx = daughter->daughter(i)->vx();  
	 double testVy = daughter->daughter(i)->vy();  
	 double testVz = daughter->daughter(i)->vz();  
	 double radius = sqrt(testVx*testVx + testVy*testVy + testVz*testVz);  
	 if (radius > radiusLastVtx) {
	   radiusLastVtx = radius;
	   idxDauLastVtx = i;
	 } 
       } 
       if (idxDauLastVtx>=0) {
	 mother = daughter;
	 daughter = daughter->daughter(idxDauLastVtx);
       } 

       // old:  
//        while (daughter->numberOfDaughters () &&          // Find the daughter that is                                                                                                                  
// 	      (daughter->status () == 3 ||               // not status 3                                                                                                                               
// 	       daughter->pdgId() == mcParticle.pdgId())  // and has different pdgId                                                                                                                    
// 	      )  daughter = daughter->daughter (0);


       if (daughter->pdgId()!=1000022 && 
	   abs(daughter->pdgId())!=211) {
	 cout << "DebuggingWarning:  will skip event with daughter PDG ID = " << daughter->pdgId()
	      << " and chargino ID = " << mcParticle.pdgId() << endl;  
	 continue; 
       }

       hGenEtaFoundVtx->Fill(mcParticle.eta());  
       nVtxCharginoToNeutralino++;        

       double daughter0Id = -99;
       double daughter0E  = -99;
       double daughter1Id = -99;
       double daughter1E  = -99;
       double daughterTotE  = 0;  
       
       decayVx = daughter->vx ();
       decayVy = daughter->vy ();
       decayVz = daughter->vz ();
       decayVxy = sqrt(decayVx*decayVx + decayVy*decayVy);

       TVector3 source (mcParticle.vx (), mcParticle.vy (), mcParticle.vz ()),
	 sink (daughter->vx (), daughter->vy (), daughter->vz ());

       cout << "Debug:  BNstop particle pdg id = " << mcParticle.pdgId()
	    << ", status = " << mcParticle.status()
	    << ", pt = " << mcParticle.pt()
	    << ", eta = " << mcParticle.eta()
	    << ", num daughters = " << mcParticle.numberOfDaughters()
	    << endl
	    << "  production:  "
	    << "  vx = " << mcParticle.vx ()
	    << "  vy = " << mcParticle.vy ()
	    << "  vz = " << mcParticle.vz ()
	    << endl
	    << "  decay:  "
	    << "  vx = " << daughter->vx ()
	    << "  vy = " << daughter->vy ()
	    << "  vz = " << daughter->vz ()
	    << endl
	    << "  daughter PDG ID:  " << daughter->pdgId()
	    << ", status = " << daughter->status()
	    << ", pt = " << daughter->pt()
	    << ", eta = " << daughter->eta()
	    << endl
	    << "  mother PDG ID:  " << mother->pdgId()
	    << ", status:  " << mother->status()
	    << ", numdau:  " << mother->numberOfDaughters()
 	    << endl;
       for (uint i=0; i<mother->numberOfDaughters(); i++) {
 	 cout << "  Mother has daughter " << i << ": " << mother->daughter(i)->pdgId() << endl;
       }
       
       if (source==sink) {
	 // Set to non-physical values if no daughters are found                                                                                                                                       
	 decayLength  = -99;
	 ctau         = -99;
// 	 betaAtDecay  = -99;
// 	 gammaAtDecay = -99;
	 decayVx  = -99;
	 decayVy  = -99;
	 decayVz  = -99;
	 decayVxy = -99;
       } else { 
	 decayLength = (sink - source).Mag ();
	 ctau = (sink - source).Mag () / (mcParticle.p4 ().Beta () * mcParticle.p4 ().Gamma ());
       }

       hvxy->Fill(fabs(vxy));
       hvx->Fill(fabs(vx));
       hvy->Fill(fabs(vy));
       hvz->Fill(fabs(vz));
       hvxyz->Fill(fabs(vz), fabs(vxy));
       hdecayVxy->Fill(fabs(decayVxy));
       hdecayVx->Fill(fabs(decayVx));
       hdecayVy->Fill(fabs(decayVy));
       hdecayVz->Fill(fabs(decayVz));
       hdecayVxyz->Fill(fabs(decayVz), fabs(decayVxy));
       hdecayVxyzWide->Fill(fabs(decayVz), fabs(decayVxy));
       hdecayLength->Fill(decayLength);
       hctau->Fill(ctau);  
       hnumdgt->Fill(numdgt);  

       if (decayLength==0) {
	 cout << "Warning:  found particle " << pdgId 
	      << " with decayLength = " << decayLength
	      << ", status = " << status
	      << ", numdgt = " << numdgt
	      << endl;  
	 nCharginoNoDecay++;  
       }

       if( (mcParticle.numberOfDaughters()>=1) ){
	 daughter0Id = mcParticle.daughter(0)->pdgId();
	 daughter0E  = mcParticle.daughter(0)->energy();
	 daughterTotE += daughter0E;
	 cout << "Debug:  daughter0Id = " << mcParticle.daughter(0)->pdgId()
	      << ", status = " << mcParticle.daughter(0)->status()
	      << ", pt = " <<     mcParticle.daughter(0)->pt()
	      << ", eta = " <<    mcParticle.daughter(0)->eta()
	      << ", vx = " << mcParticle.daughter(0)->vx()
	      << ", vy = " << mcParticle.daughter(0)->vy()
	      << ", vz = " << mcParticle.daughter(0)->vz()
	      << endl;


	 if( (mcParticle.numberOfDaughters()>=2) ){
	   daughter1Id = mcParticle.daughter(1)->pdgId();
	   daughter1E  = mcParticle.daughter(1)->energy();
	   daughterTotE += daughter1E;

	   cout << "Debug:  daughter1Id = " << mcParticle.daughter(1)->pdgId()
		<< ", status = " << mcParticle.daughter(1)->status()
		<< ", pt = " <<        mcParticle.daughter(1)->pt()
		<< ", eta = " <<       mcParticle.daughter(1)->eta()
		<< ", vx = " << mcParticle.daughter(1)->vx()
		<< ", vy = " << mcParticle.daughter(1)->vy()
		<< ", vz = " << mcParticle.daughter(1)->vz()
		<< endl;

	 }
       }

       hdaughter0Id->Fill(daughter0Id);
       hdaughter0E ->Fill(daughter0E);
       hdaughter1Id->Fill(fabs(daughter1Id));
       hdaughter1E ->Fill(daughter1E);
       if (decayLength!=0) {
	 hEDiff      ->Fill(daughterTotE - mcParticle.energy());  
       }
       cout << "Debug:  daughter0E = " << daughter0E
	    << ", daughter1E = " << daughter1E
	    << ", mother EE = " << mcParticle.energy() 
	    << ", mother status = " << mcParticle.status() 
	    << ", |daughter0Id| = 1e6 + " << fabs(daughter0Id) - 1e6
	    << ", daughter0 status = " << mcParticle.daughter(0)->status() 
	    << ", daughter1Id = " << daughter1Id
	    << ", Ediff = " << daughterTotE - mcParticle.energy()
	    << endl;  
     }

   }  

   hCharginoSumPt->Fill(pTot.Pt());
   hnVtxCharginoToNeutralino->Fill(nVtxCharginoToNeutralino); 
   hnGenCharginoTot->Fill(nGenCharginoTot);  
   hnGenCharginoSel->Fill(nGenCharginoSel);  
   hnCharginoNoDecay->Fill(nCharginoNoDecay);  
   hMissingVtx->Fill(nGenCharginoSel - nVtxCharginoToNeutralino);  

   cout << "Found" 
	<< " nVtxCharginoToNeutralino = " << nVtxCharginoToNeutralino
	<< ", missingVtx = " << nGenCharginoSel - nVtxCharginoToNeutralino
	<< ", nGenCharginoTot = " << nGenCharginoTot
	<< ", nGenCharginoSel = " << nGenCharginoSel
	<< endl;

   cout << "Debugging:  missingVtx = " << nGenCharginoSel - nVtxCharginoToNeutralino << endl;  



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
DecayAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DecayAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
DecayAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DecayAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DecayAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DecayAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DecayAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DecayAnalyzer);
