#ifndef EVENT_GENJET_VAR_PRODUCER
#define EVENT_GENJET_VAR_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"

class EventGenJetVarProducer : public EventVariableProducer {
public:
  EventGenJetVarProducer(const edm::ParameterSet &);
  ~EventGenJetVarProducer() {};

private:
  void AddVariables(const edm::Event &);

  edm::InputTag genJetsTag_;
  edm::EDGetTokenT<reco::GenJetCollection> genJetsToken_;
};

#endif
