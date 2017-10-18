#ifndef GEN_Z_PT_ANALYZER

#define GEN_Z_PT_ANALYZER

#include <vector>
#include <algorithm>
#include <iostream>

#include "TH1D.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/View.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

using std::min;
using namespace std;

class GenZPtAnalyzer : public edm::EDAnalyzer
{
 public:
  GenZPtAnalyzer (const edm::ParameterSet &);
  virtual ~GenZPtAnalyzer ();
  void beginJob () {};
  void analyze (const edm::Event &, const edm::EventSetup &);
  void endJob () {};

 private:
  edm::InputTag genParticles_;
  edm::EDGetTokenT<edm::View<reco::GenParticle> > genParticlesToken_;

  std::map<std::string, TH1D *> oneDHists_;
  edm::Service<TFileService> fs_;

  void getFinalZ (const edm::View<reco::GenParticle> &, const reco::GenParticle *) const;
  const reco::GenParticle * const getFinalZ (const edm::View<reco::GenParticle> &) const;
  bool isFinalZ (const reco::GenParticle &) const;
};

#endif
