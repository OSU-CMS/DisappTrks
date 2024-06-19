#ifndef TRIGGER_EFFICIENCY
#define TRIGGER_EFFICIENCY

#include <string>
#include <map>
#include <vector>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/MuonReco/interface/Muon.h"

#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

using namespace std;

class EventDisplays : public edm::stream::EDFilter<>
{
  public:
    EventDisplays (const edm::ParameterSet &);
    ~EventDisplays ();

    bool filter (edm::Event &, const edm::EventSetup &);

  private:
    edm::InputTag  mets_;
    edm::InputTag  caloMETs_;
    edm::InputTag  muons_;
    edm::InputTag  genParticles_;
    edm::InputTag  jets_;
};

#endif
