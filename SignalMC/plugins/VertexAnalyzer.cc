// -*- C++ -*-
//
// Package:    DemoAnalyzer
// Class:      DemoAnalyzer
// 
/**\class DemoAnalyzer DemoAnalyzer.cc Demo/DemoAnalyzer/src/DemoAnalyzer.cc

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


class VertexAnalyzer : public edm::EDAnalyzer {
   public:
      explicit VertexAnalyzer(const edm::ParameterSet&);
      ~VertexAnalyzer();

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

  TH1D *hptChiChi;  

  TH1D* hnVtxCharginoToNeutralino;  
  TH1D* hnVtxCharginoParent;
  TH1D* hnGenCharginoTot;
  TH1D* hnGenCharginoSel;
  TH1D* hMissingVtx;  
  TH2D* hDecayPos;  
  TH2D* hDecayPosDiffSmall;  
  TH2D* hDecayPosDiffLarge;  
  TH1D* hEDiff;  
  TH1D* hEDiffSmall;  
  TH1D* hEDiffLarge;  
  TH1D* hGenEta;
  TH1D* hGenEtaSel;
  TH1D* hGenBetaGammaSel;
  TH1D* hGenPtSel;
  TH1D* hGenPSel;
  TH1D* hGenSignSel;
  TH1D* hGenSignFoundVtx;
  TH1D* hGenEtaFoundVtx;

  TH1D* hdecayLength;
  TH1D* hctau;
  TH1D* hctauWide;
  TH1D* hctauAtDecay; 
  TH1D* hctauAtDecayWide; 
  TH1D* hctauDiffSmall;
  TH1D* hctauDiffLarge;
  TH1D* hbeta; 
  TH1D* hgamma;  

  TH1D* hbetaGammaGen;    
  TH1D* hbetaGammaAtDecay;
  TH1D* hbetaGammaDiff;   
  TH1D* hctauRatio;   

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
VertexAnalyzer::VertexAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;  
  hptChiChi = fs->make<TH1D>("ptChiChi" , ";p_{T}^{#chi#chi}" , 100 , 0 , 500 );
  hnVtxCharginoToNeutralino = fs->make<TH1D>("hnVtxCharginoToNeutralino" , ";# vertices with #chi^{#pm} parent and #chi^{0} daughter" , 10 , -0.5 , 9.5 );
  hnVtxCharginoParent = fs->make<TH1D>("hnVtxCharginoParent" , ";# vertices with #chi^{#pm} parent" , 10 , -0.5 , 9.5 );
  hnGenCharginoTot = fs->make<TH1D>("hnGenCharginoTot" ,    ";# total generated #chi^{#pm}" , 10 , -0.5 , 9.5 );
  hnGenCharginoSel = fs->make<TH1D>("hnGenCharginoSel" ,    ";# selected generated #chi^{#pm}" , 10 , -0.5 , 9.5 );
  hMissingVtx = fs->make<TH1D>("hMissingVtx" ,    ";# missing #chi^{#pm} vertices" , 10 , -0.5 , 9.5 );
  hDecayPos = fs->make<TH2D>("hDecayPos" ,    "Position of #chi^{#pm}#rightarrow#chi^{0}#pi^{#pm} decay ;|z| [cm];|#rho| [cm]" , 100, 0, 1200, 100, 0, 800);
  hDecayPosDiffSmall = fs->make<TH2D>("hDecayPosDiffSmall" ,    "Position of #chi^{#pm}#rightarrow#chi^{0}#pi^{#pm} decay ;|z| [cm];|#rho| [cm] (small |#DeltaE|)" , 100, 0, 1200, 100, 0, 800);
  hDecayPosDiffLarge = fs->make<TH2D>("hDecayPosDiffLarge" ,    "Position of #chi^{#pm}#rightarrow#chi^{0}#pi^{#pm} decay ;|z| [cm];|#rho| [cm] (large |#DeltaE|)" , 100, 0, 1200, 100, 0, 800);
  hEDiff = fs->make<TH1D>("hEDiff" ,    ";(total daughters' energy) - (#chi^{#pm} energy)" , 100, -10, 10);  
  hEDiffSmall  = fs->make<TH1D>("hEDiffSmall", ";(total daughters' energy) - (chargino energy) [GeV] (small |#DeltaE|)", 100, -10, 10);
  hEDiffLarge  = fs->make<TH1D>("hEDiffLarge", ";(total daughters' energy) - (chargino energy) [GeV] (large |#DeltaE|)", 100, -10, 10);

  hdecayLength = fs->make<TH1D>("hdecayLength", "decayLength", 100, 0, 1000);
  hctau = fs->make<TH1D>("hctau", ";c#tau = L_{xyz} / (#beta#gamma)^{prod} [cm]", 100, 0, 1000);
  hctauWide = fs->make<TH1D>("hctauWide", ";c#tau = L_{xyz} / (#beta#gamma)^{prod} [cm]", 100, 0, 2000);
  hctauAtDecay = fs->make<TH1D>("hctauAtDecay", ";c#tau = L_{xyz} / (#beta#gamma)^{decay} [cm]", 100, 0, 1000);
  hctauAtDecayWide = fs->make<TH1D>("hctauAtDecayWide", ";c#tau = L_{xyz} / (#beta#gamma)^{decay} [cm]", 100, 0, 2000);
  hctauDiffSmall = fs->make<TH1D>("hctauDiffSmall", ";c#tau [cm] (small |#DeltaE|)", 100, 0, 1000);
  hctauDiffLarge = fs->make<TH1D>("hctauDiffLarge", ";c#tau [cm] (large |#DeltaE|)", 100, 0, 1000);
  hbeta = fs->make<TH1D>("hbeta", ";#beta", 110, 0, 1.1);
  hgamma = fs->make<TH1D>("hgamma", ";#gamma", 100, 0, 10);

  hbetaGammaGen     = fs->make<TH1D>("hbetaGammaGen", ";#beta#gamma (at production)", 100, 0, 10);
  hbetaGammaAtDecay = fs->make<TH1D>("hbetaGammaAtDecay", ";#beta#gamma (at decay)", 100, 0, 10);
  hbetaGammaDiff    = fs->make<TH1D>("hbetaGammaDiff", ";(#beta#gamma)^{decay} / (#beta#gamma)^{prod}", 100, 0.8, 1.2);
  hctauRatio        = fs->make<TH1D>("hctauRatio", ";(c#tau)^{decay} / (c#tau)^{prod}", 100, 0.8, 1.2);

  hGenEta = fs->make<TH1D>("hGenEta" ,    ";#eta, generated #chi^{#pm}" , 100 , -7, 7);
  hGenEtaSel = fs->make<TH1D>("hGenEtaSel" ,    ";#eta, selected #chi^{#pm}" , 100 , -7, 7);
  hGenPtSel  = fs->make<TH1D>("hGenPtSel" ,    ";p_{T} [GeV], selected #chi^{#pm}" , 100, 0, 500);  
  hGenPSel   = fs->make<TH1D>("hGenPSel" ,         ";p [GeV], selected #chi^{#pm}" , 100, 0, 500);  
  hGenSignSel   = fs->make<TH1D>("hGenSignSel" ,         ";sign of PDG ID, selected #chi^{#pm}" , 5, -2.5, 2.5); 
  hGenBetaGammaSel  = fs->make<TH1D>("hGenBetaGammaSel" ,    ";#beta #gamma, selected #chi^{#pm}" , 100, 0, 10);  
  hGenEtaFoundVtx = fs->make<TH1D>("hGenEtaFoundVtx" ,    ";#eta, generated #chi^{#pm} with decay vertex" , 100 , -7, 7);
  hGenSignFoundVtx   = fs->make<TH1D>("hGenSignFoundVtx" ,   ";sign of PDG ID, selected with found vtx #chi^{#pm}" , 5, -2.5, 2.5); 

}


VertexAnalyzer::~VertexAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}




//
// member functions
//

// ------------ method called for each event  ------------
void
VertexAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   Handle<reco::GenParticleCollection > genParticles;
   //   iEvent.getByLabel(genParticleTag_,genParticles); 
   iEvent.getByLabel("genParticles",genParticles);

   double MaxEta = 2.5;  

   TLorentzVector pTot(0,0,0,0);  
   int nGenCharginoTot = 0;  
   int nGenCharginoSel = 0;  
   if (genParticles.isValid()) {
     for( size_t k = 0; k < genParticles->size(); k++ ){
       const reco::Candidate & mcParticle = (*genParticles)[k];

       int status = mcParticle.status();
       int pdgId  = mcParticle.pdgId();
       int numdgt = mcParticle.numberOfDaughters();

       if (!(abs(pdgId)==1000022 ||
             abs(pdgId)==1000024)) continue;

       if (!(status==3)) continue;  

       cout << "Found gen particle with:  status=" << status << "; pdgId=" << pdgId
            << "; numdgt=" << numdgt
            << ", px = " << mcParticle.px()
            << ", py = " << mcParticle.py()
            << ", pz = " << mcParticle.pz()
            << ", energy = " << mcParticle.energy()
            << ", eta = " << mcParticle.eta()
            << endl;

       if (abs(pdgId)==1000024) {
	 nGenCharginoTot++;
         hGenEta->Fill(mcParticle.eta());
         if (fabs(mcParticle.eta()) < MaxEta) {
           nGenCharginoSel++;
	   hGenEtaSel->Fill(mcParticle.eta());
	   hGenPtSel ->Fill(mcParticle.pt());
	   hGenPSel  ->Fill(mcParticle.p());
	   hGenSignSel  ->Fill(pdgId / abs(pdgId));
	   hGenBetaGammaSel->Fill(mcParticle.p4().Beta() * mcParticle.p4().Gamma());
         }
       }

       TLorentzVector p4(mcParticle.px(), 
			 mcParticle.py(), 
			 mcParticle.pz(), 
			 mcParticle.energy());  
       pTot += p4;  
       
     }  

   }  

   hptChiChi->Fill(pTot.Pt());

   // For SimVertex / SimTrack analysis, follow example code from:
   // https://cmssdt.cern.ch/SDT/lxr/source/PhysicsTools/HepMCCandAlgos/plugins/GenPlusSimParticleProducer.cc
   
   // Get the associated vertices
   Handle<SimVertexContainer> simvertices;
   //   event.getByToken(simverticesToken_, simvertices);
   iEvent.getByLabel("g4SimHits", simvertices);

   // Simulated tracks (i.e. GEANT particles).
   Handle<SimTrackContainer> simtracks;
   iEvent.getByLabel("g4SimHits", simtracks);
   
   // // Need to check that SimTrackContainer is sorted; otherwise, copy and sort :-(
   // std::auto_ptr<SimTrackContainer> simtracksTmp;
   // const SimTrackContainer* simtracksSorted = &* simtracks;
   // if (!__gnu_cxx::is_sorted(simtracks->begin(), simtracks->end(), LessById())) {
   //   simtracksTmp.reset(new SimTrackContainer(*simtracks));
   //   std::sort(simtracksTmp->begin(), simtracksTmp->end(), LessById());
   //   simtracksSorted = &* simtracksTmp;
   // }
   
   int nVertices = 0;  
   int nSimTrk   = 0;  
   int nVtxCharginoParent = 0;  
   int nVtxCharginoToNeutralino = 0;  
   if (simvertices.isValid()) {
     //     for( size_t i = 0; i < simvertices->size(); i++ ){
     
     for (SimVertexContainer::const_iterator ivtx = simvertices->begin();
	  ivtx != simvertices->end(); ++ivtx) {
       
       nVertices++;  
       
       // Check if the vertex has a parent track (otherwise, we're lost)
       if (!(ivtx->noParent())) {
	 
	 // Now note that vtx.parentIndex() is NOT an index, it's a track id, so I have to search for it
	 unsigned int idx = ivtx->parentIndex();
	 for (SimTrackContainer::const_iterator isimtrk = simtracks->begin();
	      isimtrk != simtracks->end(); ++isimtrk) {
	   if (isimtrk->trackId() != idx) continue;  
	   int trkType = isimtrk->type();
	   
	   // SimTrackContainer::const_iterator it = std::lower_bound(simtracksSorted->begin(), simtracksSorted->end(), idx, LessById());
	   // if ((it != simtracksSorted->end()) && (it->trackId() == idx)) { //it is the parent sim track
	   //	   int trkType = it->type();
	   
	   if (abs(trkType)==1000024 ||
	       abs(trkType)==1000022) {
	     cout << "Found vertex with parent with type:  " << trkType 
		  << " and position: perp = " << ivtx->position().rho()
		  << ", z = " << ivtx->position().z()
		  << ", trackId = " << isimtrk->trackId()
		  << endl;  
	     if (abs(trkType)==1000024) nVtxCharginoParent++;  
	   }
	   
	 }
       }
     }
   }
   cout << "Found nVertices=" << nVertices 
	<< " and nVtxCharginoParent = " << nVtxCharginoParent
	<< endl;  

   for (SimTrackContainer::const_iterator isimtrk = simtracks->begin();
	isimtrk != simtracks->end(); ++isimtrk) {
     
     nSimTrk++;  
     // // Skip PYTHIA tracks.
     // if (isimtrk->genpartIndex() != -1) continue;

     int trkType = abs(isimtrk->type());
     
     if (trkType==1000024 ||
	 trkType==1000022) {
       cout << "Found track with type:  " << isimtrk->type()
	    << endl;  
     }
       if (!isimtrk->noVertex()) {
	 const SimVertex &vtx = (*simvertices)[isimtrk->vertIndex()];
	 if (trkType==1000024 ||
	     trkType==1000022) {
	   cout << "  and production vertex at perp = " << vtx.position().rho()
		<< ", z = " << vtx.position().z() 
		<< endl;  
	 }
	 
	 // Check if the vertex has a parent track (otherwise, we're lost)
	 if (!(vtx.noParent())) {
	   
	   // Now note that vtx.parentIndex() is NOT an index, it's a track id, so I have to search for it
	   unsigned int idx = vtx.parentIndex();
	   if (trkType==1000022) cout << "  Found a parent of 1000022 with index " << idx << endl;  
	   for (SimTrackContainer::const_iterator jsimtrk = simtracks->begin();  // loop over tracks to find parent  
		jsimtrk != simtracks->end(); ++jsimtrk) {
	     if (jsimtrk->trackId() != idx) continue;  
	     if (abs(jsimtrk->type())==1000024) {
	       cout << "  Found vertex with parent = " << jsimtrk->type()
		    << " and daughter = " << isimtrk->type()  
		    << " mother energy = " << jsimtrk->momentum().E()
		    << ", daughter energy = " << isimtrk->momentum().energy()  
		    << "  vertex at perp = " << vtx.position().rho()
		    << ", z = " << vtx.position().z() 
		    << endl;  	       
	       if (trkType==1000022 && fabs(jsimtrk->momentum().eta())<MaxEta) {  
		 double daughterTotE = 0;  
		 TLorentzVector p4DauTot(0,0,0,0);  
		 for (SimTrackContainer::const_iterator ksistrk = simtracks->begin();
		      ksistrk != simtracks->end(); ++ksistrk) {
		   // loop over all tracks to check which ones share a common vertex
		   if (ksistrk->vertIndex() == isimtrk->vertIndex()) {
		     daughterTotE += ksistrk->momentum().energy();  
		     p4DauTot += TLorentzVector(ksistrk->momentum().x(), 
						ksistrk->momentum().y(), 
						ksistrk->momentum().z(), 
						ksistrk->momentum().E());  
		     cout << "  Adding daughter energy " << ksistrk->momentum().energy()
			  << " for daughter " << ksistrk->type()
			  << endl;  
		   }		   
		 }  
		 cout << "  Found a chargino->neutralino decay vertex"
		      << ", with mother energy = " << jsimtrk->momentum().E()
		      << ", total daughter energy = " << daughterTotE  
		      << endl;  
		 const SimVertex &srcVtx = (*simvertices)[jsimtrk->vertIndex()];
		 TVector3 source (srcVtx.position().x(), srcVtx.position().y(), srcVtx.position().z());
		 TVector3 sink   (vtx.position().x(), vtx.position().y(), vtx.position().z());
		 double decayLength = (sink - source).Mag ();
		 double ctau = (sink - source).Mag () / (jsimtrk->momentum().Beta() * jsimtrk->momentum().Gamma());
		 double beta = jsimtrk->momentum().Beta();
		 double gamma = jsimtrk->momentum().Gamma();  
		 double EDiff = daughterTotE - jsimtrk->momentum().E();
		 double betaGammaAtDecay = p4DauTot.Beta() * p4DauTot.Gamma();  
		 double ctauAtDecay = (sink - source).Mag () / betaGammaAtDecay;  
		 double ctauRatio = ctauAtDecay / ctau;  
		 hEDiff->Fill(EDiff); 
		 hDecayPos->Fill(fabs(vtx.position().z()), fabs(vtx.position().rho()));  
		 hdecayLength->Fill(decayLength);  
		 hctau->Fill(ctau);
		 hctauWide->Fill(ctau);
		 hctauAtDecay->Fill(ctauAtDecay);
		 hctauAtDecayWide->Fill(ctauAtDecay);
		 hbeta->Fill(beta);
		 hgamma->Fill(gamma);  
		 hbetaGammaGen->Fill(beta * gamma);  
		 hbetaGammaAtDecay->Fill(betaGammaAtDecay);  
		 hbetaGammaDiff->Fill(betaGammaAtDecay / (beta*gamma));  
		 hctauRatio->Fill(ctauRatio);  
		 hGenSignFoundVtx->Fill(jsimtrk->type() / abs(jsimtrk->type()));  	   
		 if (fabs(EDiff) < 1.0) {
		   hctauDiffSmall->Fill(ctau);
		   hEDiffSmall->Fill(EDiff);  
		   hDecayPosDiffSmall->Fill(fabs(vtx.position().z()), fabs(vtx.position().rho()));  
		 } else {
		   hctauDiffLarge->Fill(ctau);
		   hEDiffLarge->Fill(EDiff);  
		   hDecayPosDiffLarge->Fill(fabs(vtx.position().z()), fabs(vtx.position().rho()));  
		 }
		 nVtxCharginoToNeutralino++; 
		 hGenEtaFoundVtx->Fill(jsimtrk->momentum().eta());     
	       }
	     }
	   }
	 }
	 //	 }
       }
   }

   cout << "Found nSimTrk=" << nSimTrk 
     //	<< "; simtracksSorted->size() = " << simtracksSorted->size() 
	<< " and nVtxCharginoToNeutralino = " << nVtxCharginoToNeutralino
	<< ", missingVtx = " << nGenCharginoSel - nVtxCharginoToNeutralino      
	<< ", nGenCharginoTot = " << nGenCharginoTot
	<< ", nGenCharginoSel = " << nGenCharginoSel
	<< endl;  
   cout << "Debugging:  missingVtx = " << nGenCharginoSel - nVtxCharginoToNeutralino <<endl; 



   hnVtxCharginoToNeutralino->Fill(nVtxCharginoToNeutralino);
   hnVtxCharginoParent->Fill(nVtxCharginoParent);
   hnGenCharginoTot->Fill(nGenCharginoTot);
   hnGenCharginoSel->Fill(nGenCharginoSel);
   hMissingVtx->Fill(nGenCharginoSel - nVtxCharginoToNeutralino);  

   // testing to create a seg fault!: 
//    TH1D* hBug = 0;
//    hBug->Fill(1.0);  

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
VertexAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
VertexAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
VertexAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
VertexAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
VertexAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
VertexAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
VertexAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(VertexAnalyzer);
