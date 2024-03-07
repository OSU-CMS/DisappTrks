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

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include <iostream>

#include "TLorentzVector.h"

using namespace edm;
using namespace std;



//
// class decleration
//

class MCParticlePairSumPtFilter : public edm::stream::EDFilter<> {
public:
  explicit MCParticlePairSumPtFilter(const edm::ParameterSet&);
  ~MCParticlePairSumPtFilter();


  virtual bool filter(edm::Event&, const edm::EventSetup&);
private:
  // ----------memeber function----------------------

  // ----------member data ---------------------------

  std::string label_;
  std::vector<int> particleIDs_;
  double minSumPt_;


};


MCParticlePairSumPtFilter::MCParticlePairSumPtFilter(const edm::ParameterSet& iConfig) :
  label_(iConfig.getUntrackedParameter("moduleLabel",std::string("generator")))
{
  //here do whatever other initialization is needed
  vector<int> defpid;
  defpid.push_back(0);
  particleIDs_ = iConfig.getUntrackedParameter< vector<int> >("ParticleIDs",defpid);
  minSumPt_ = iConfig.getUntrackedParameter< double >("MinSumPt", 0.);

  cout << "MCParticlePairSumPtFilter:  Will require that the vector sum pT is greater than " << minSumPt_
       << " GeV for all status 3 particles with |PDG ID| matching: " << endl;
  for (uint i=0; i<particleIDs_.size(); i++) {
    cout << "  " << particleIDs_.at(i) << endl;
  }

}


MCParticlePairSumPtFilter::~MCParticlePairSumPtFilter()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


// ------------ method called to skim the data  ------------
bool MCParticlePairSumPtFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  // Gather information on the reco::GenParticle collection
  // edm::Handle<reco::GenParticleCollection> genParticles;
  // iEvent.getByLabel(src_, genParticles );

  Handle<HepMCProduct> evt;
  iEvent.getByLabel(label_, evt);

  int nPart = 0;

  TLorentzVector p4Tot;  // sum pT of selected particles

 const HepMC::GenEvent * myGenEvent = evt->GetEvent();
 for ( HepMC::GenEvent::particle_const_iterator p = myGenEvent->particles_begin();
       p != myGenEvent->particles_end(); ++p ) {

    if ( (*p)->status() != 3) continue;  // only consider status 3 particles
    int pdgIdAbs = abs((*p)->pdg_id());
    if (find(particleIDs_.begin(), particleIDs_.end(), pdgIdAbs) == particleIDs_.end()) continue;  // The pdgIdAbs is not contained in the vector.

    nPart++;
    TLorentzVector p4((*p)->momentum().px(),
                      (*p)->momentum().py(),
                      (*p)->momentum().pz(),
                      (*p)->momentum().e());
    p4Tot += p4;

  }  // end loop over genParticles

  if (nPart!=2) {
    cout << "Warning [MCParticlePairSumPtFilter::filter]:  event contains " << nPart
         << " particles with status 3 that match the input PDG ID list; returning false."
         << endl;
    return false;
  }

  bool pass = (p4Tot.Pt() > minSumPt_);
  return pass;

} // end bool MCParticlePairSumPtFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)



//define this as a plug-in
DEFINE_FWK_MODULE(MCParticlePairSumPtFilter);
