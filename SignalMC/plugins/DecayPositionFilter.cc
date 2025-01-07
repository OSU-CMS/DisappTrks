// Filter that returns true iff the event contains exactly 2 status 3 particles
// that have a PDG ID with absolute value that matches the value in the input list,
// with a sum pt greater than the input value.

// Follow examples from:
// https://cmssdt.cern.ch/SDT/lxr/source/GeneratorInterface/GenFilters/src/MCParticlePairFilter.cc?v=CMSSW_5_3_12
// https://cmssdt.cern.ch/SDT/lxr/source/GeneratorInterface/GenFilters/src/TotalKinematicsFilter.cc?v=CMSSW_5_3_12

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
//#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH2D.h"
#include "TH1D.h"
#include "TLorentzVector.h"

#include <ext/algorithm>
#include <iostream>


using namespace edm;
using namespace std;
using namespace reco;


//
// class decleration
//

class DecayPositionFilter : public edm::stream::EDFilter<> {
public:
  explicit DecayPositionFilter(const edm::ParameterSet&);
  ~DecayPositionFilter();


  virtual bool filter(edm::Event&, const edm::EventSetup&);
private:
  // ----------memeber function----------------------

  // ----------member data ---------------------------

  std::string label_;
  std::vector<int> particleIDs_;
  std::vector<double> decayRadius_;
  std::vector<double> maxDeltaR_;
//  edm::InputTag src_;
//  edm::EDGetTokenT<reco::CandidateView> srcToken_;
//  edm::ESHandle<ParticleDataTable> pdt_;

};


DecayPositionFilter::DecayPositionFilter(const edm::ParameterSet& iConfig) :
  label_(iConfig.getUntrackedParameter("moduleLabel",std::string("generator")))
{
  //here do whatever other initialization is needed
  vector<int> defpid;
  defpid.push_back(0);
  vector<double> defradius;
  defradius.push_back(0);
  vector<double> defdR;
  defdR.push_back(0);
  particleIDs_ = iConfig.getUntrackedParameter< vector<int> >("ParticleIDs",defpid);
  decayRadius_ = iConfig.getUntrackedParameter< vector<double> >("DecayRadius", defradius);
  maxDeltaR_ = iConfig.getUntrackedParameter< vector<double> >("maxDeltaR", defdR);

  cout << "DecayPositionFilter:  Will require that the decay vertex at " << decayRadius_.at(0)
       << " for the decay of" << endl;
  for (uint i=0; i<particleIDs_.size(); i++) {
    cout << "  " << particleIDs_.at(i) << endl;
  }

}


DecayPositionFilter::~DecayPositionFilter()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


// ------------ method called to skim the data  ------------
bool DecayPositionFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace std;

//  Handle<reco::CandidateView> particles;
//  iEvent.getByToken(srcToken_, particles );
//  iSetup.getData( pdt_ );

/*  for(CandidateView::const_iterator p  = particles->begin();
      p != particles->end();
      p ++) {
      cout <<"pdgID: "<< p->pdgId() << "     mass: " <<  p->mass() <<endl;    

  }*/
//  cout << "moew" << endl;
  bool pass = false;
  // Get gen-level vertex
  Handle<SimVertexContainer> simvertices;
  //   event.getByToken(simverticesToken_, simvertices);
  iEvent.getByLabel("g4SimHits", simvertices);

  // Simulated tracks (i.e. GEANT particles).
  Handle<SimTrackContainer> simtracks;
  iEvent.getByLabel("g4SimHits", simtracks);

  // truth particles (i.e. genParticlePlusGeant particles).
  Handle<vector<reco::GenParticle>> genparticleplusgeants;
  iEvent.getByLabel("genParticlePlusGeant", genparticleplusgeants);

  int nGoodDecayVertex = 0; // Flag for chargino decay position
  int nsimVertex = 0;       // counter for all simVertex

  bool isInBarrel = false;
  bool isInMiniEndCap = false;
  bool isInEndCap = false;
  bool isInMSGC = false;
  bool find_chi = false;
  bool find_muon =false;
  if( simvertices.isValid() && genparticleplusgeants.isValid() ) {
//    cout << "moew1" << endl;

    // Iterator to loop over GenParticle for dR selection
    TLorentzVector v_chargino,v_muon;
    for(const auto &genparticleplusgeant : *genparticleplusgeants){
      if(abs(genparticleplusgeant.pdgId())==1000024){
        v_chargino.SetPtEtaPhiM(genparticleplusgeant.pt(),genparticleplusgeant.eta(),genparticleplusgeant.phi(),genparticleplusgeant.mass());
        std::cout << genparticleplusgeant.pt() << std::endl;;
        find_chi=true;
      }
      if(abs(genparticleplusgeant.pdgId())==13){
        find_muon = true;
        v_muon.SetPtEtaPhiM(genparticleplusgeant.pt(),genparticleplusgeant.eta(),genparticleplusgeant.phi(),genparticleplusgeant.mass());
        break;
      }
      if( find_chi==true && find_muon==true ) break;
    }

/*    for (SimTrackContainer::const_iterator isimtrk = simtracks->begin();
             isimtrk != simtracks->end(); ++isimtrk) {
      if(abs(isimtrk->type())==1000024){
        find_chi=true;
        v_chargino.SetPtEtaPhiM(isimtrk->trackerSurfaceMomentum().pt(),isimtrk->trackerSurfaceMomentum().eta(),isimtrk->trackerSurfaceMomentum().phi(),isimtrk->trackerSurfaceMomentum().mass());
      }
    }
*/


    if(v_chargino.DeltaR(v_muon) > maxDeltaR_.at(0)) return false;
    std::cout << v_chargino.Pt() << ";" << v_chargino.Eta() << ";" << v_chargino.Phi() << ";" << v_chargino.M() << endl;
    std::cout << v_muon.Pt() << ";" << v_muon.Eta() << ";" << v_muon.Phi() << ";" << v_muon.M() << endl;
    std::cout << v_chargino.DeltaR(v_muon) << "/" << maxDeltaR_.at(0)  << std::endl;    
//    std::cout << "Yes" << std::endl;


    // Iterator to loop over all simVertex
    for(SimVertexContainer::const_iterator ivtx = simvertices->begin();
        ivtx != simvertices->end(); ++ivtx) {

      nsimVertex++;
      //  Check if the vertex as parent track
      if( !(ivtx->noParent())){


//        cout << "moew2" << endl;
	// Now note that vtx.parentIndex() is NOT an index, it's a track id, so I have to search for it
	unsigned int idx = ivtx->parentIndex();
        if ( ivtx->processType() < 200 ) continue;
	for (SimTrackContainer::const_iterator isimtrk = simtracks->begin();
             isimtrk != simtracks->end(); ++isimtrk) {
	  if (isimtrk->trackId() != idx) continue;
//          cout << "moew3" << endl;
	  int trkType = isimtrk->type();   // Get the pdgID of the track
//          cout << "parent pdgID is: "  << trkType << endl;
//          if (abs(trkType)==13) cout << "muon found" <<endl;
           
          if (abs(trkType)==1000024 ) {      
         /*   cout << "Found vertex with parent with type:  " << trkType
                 << " and position: perp = " << ivtx->position().rho()
                 << ", z = " << ivtx->position().z()
                 << ", trackId = " << isimtrk->trackId()
                 << endl;*/
            nGoodDecayVertex++;
           // bool Vertex_in_layer = false;
            if( // Barrel strip 
                ( ivtx->position().rho() > 21.70 && ivtx->position().rho() < 24.90 && fabs(ivtx->position().z()) < 30.197) ||  // Layer 1
                ( ivtx->position().rho() > 30.45 && ivtx->position().rho() < 33.65 && fabs(ivtx->position().z()) < 32.112) ||  // Layer 2
                ( ivtx->position().rho() > 39.15 && ivtx->position().rho() < 42.35 && fabs(ivtx->position().z()) < 67.846) ||  // Layer 3
                ( ivtx->position().rho() > 47.90 && ivtx->position().rho() < 51.10 && fabs(ivtx->position().z()) < 68.979) ||  // Layer 4
                ( ivtx->position().rho() > 56.60 && ivtx->position().rho() < 59.80 && fabs(ivtx->position().z()) < 69.722)     // Layer 5
              ){
	      isInBarrel = true;
            }
            if( // Mini EndCap
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 35.40 && fabs( fabs(ivtx->position().z()) - 51.8 ) < 0.5 ) ||    // Disk 1
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 35.40 && fabs( fabs(ivtx->position().z()) - 63.4 ) < 0.5 ) ||    // Disk 2
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 35.40 && fabs( fabs(ivtx->position().z()) - 75.0 ) < 0.5 )       // Disk 3
              ){
	      isInMiniEndCap = true;
            }
            if( // EndCap
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 95.2 ) < 0.5 ) ||    // Disk A1
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 104.2 ) < 0.5 ) ||    // Disk A2
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 114.7 ) < 0.5 ) ||    // Disk A3
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 129.3 ) < 0.5 ) ||    // Disk A4
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 144.1 ) < 0.5 ) ||    // Disk A5
                ( ivtx->position().rho() > 21.8 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 163.0 ) < 0.5 ) ||    // Disk A6

                ( ivtx->position().rho() > 28.5 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 182.3 ) < 0.5 ) ||    // Disk B1
                ( ivtx->position().rho() > 28.5 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 206.8 ) < 0.5 ) ||    // Disk B2

                ( ivtx->position().rho() > 39.0 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 231.9 ) < 0.5 ) ||    // Disk C1
                ( ivtx->position().rho() > 39.0 && ivtx->position().rho() < 60.80 && fabs( fabs(ivtx->position().z()) - 263.8 ) < 0.5 )       // Disk C2
              ){
	      isInEndCap = true;
            }
            if( // MSGC
                ( fabs( ivtx->position().z() ) < 120.5  && fabs( fabs(ivtx->position().rho()) - 74.7 ) < 1.5 ) ||    // Layer 1
                ( fabs( ivtx->position().z() ) < 120.5  && fabs( fabs(ivtx->position().rho()) - 82.7 ) < 1.5 ) ||    // Layer 2
                ( fabs( ivtx->position().z() ) < 120.5  && fabs( fabs(ivtx->position().rho()) - 90.7 ) < 1.5 ) ||    // Layer 3
                ( fabs( ivtx->position().z() ) < 120.5  && fabs( fabs(ivtx->position().rho()) - 98.7 ) < 1.5 ) ||    // Layer 4
                ( fabs( ivtx->position().z() ) < 120.5  && fabs( fabs(ivtx->position().rho()) - 106.7 ) < 1.5 ) ||   // Layer 5
                ( fabs( ivtx->position().z() ) < 120.5  && fabs( fabs(ivtx->position().rho()) - 114.7 ) < 1.5 )      // Layer 6
              ){
	      isInMSGC = true;
            }


             if ( isInBarrel || isInMiniEndCap || isInEndCap || isInMSGC ){
	      pass = true;
              cout << "In the layer!!" << endl;
              break;
	    }
	  }
        }
      }
    }
  }
  

  return pass;

} // end bool DecayPositionFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)



//define this as a plug-in
DEFINE_FWK_MODULE(DecayPositionFilter);
