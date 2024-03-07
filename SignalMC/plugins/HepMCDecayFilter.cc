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
using namespace HepMC;


//
// class decleration
//

class HepMCDecayFilter : public edm::stream::EDFilter<> {
public:
  explicit HepMCDecayFilter(const edm::ParameterSet&);
  ~HepMCDecayFilter();


  virtual bool filter(edm::Event&, const edm::EventSetup&);
private:
  // ----------memeber function----------------------

  // ----------member data ---------------------------

  std::string label_;
  std::vector<int> particleIDs_;
  edm::EDGetTokenT<edm::HepMCProduct> token_;
//  double decayRadius_;
//  edm::InputTag src_;
//  edm::EDGetTokenT<reco::CandidateView> srcToken_;
//  edm::ESHandle<ParticleDataTable> pdt_;

};


HepMCDecayFilter::HepMCDecayFilter(const edm::ParameterSet& iConfig)
{
  //here do whatever other initialization is needed
  vector<int> defpid;
  defpid.push_back(0);
  particleIDs_ = iConfig.getUntrackedParameter< vector<int> >("ParticleIDs",defpid);
  token_ = consumes<edm::HepMCProduct>(edm::InputTag(iConfig.getUntrackedParameter("moduleLabel",std::string("generator"))));
  cout << "HepMCDecayFilter:  Will require that the decay vertex for the decay of" << endl;
  for (uint i=0; i<particleIDs_.size(); i++) {
    cout << "  " << particleIDs_.at(i) << endl;
  }

}


HepMCDecayFilter::~HepMCDecayFilter()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


// ------------ method called to skim the data  ------------
bool HepMCDecayFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace std;
  using namespace HepMC;

  // Get HepMC info
  edm::Handle<HepMCProduct> evt;
  iEvent.getByToken(token_, evt);

  Handle<reco::GenParticleCollection > genParticles;
  //   iEvent.getByLabel(genParticleTag_,genParticles);
  iEvent.getByLabel("genParticles",genParticles);
  
  HepMC::GenVertex* inVertex = nullptr;
  bool pass = false;

  const HepMC::GenEvent * generated_event = evt->GetEvent();
  cout << generated_event->particles_size() <<endl;
  for(HepMC::GenEvent::particle_const_iterator  genparticle = generated_event->particles_begin();
      genparticle != generated_event->particles_end();
      genparticle++){
      int pdgId = (*genparticle)->pdg_id();
      //cout << pdgId  << endl;
      //if(pdgId == 1000024) cout << "chargino found" << endl;
      if(abs(pdgId) == 1000022){
	inVertex = (*genparticle)->production_vertex();
  	if( fabs((*genparticle)->momentum().eta())<1.5 ){
	  pass = true;
	  cout << "decay found" << endl; 
        }
        if(inVertex != nullptr) cout <<"InVertex caught" <<endl;
      }
  }

  return pass;

} // end bool HepMCDecayFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)



//define this as a plug-in
DEFINE_FWK_MODULE(HepMCDecayFilter);
