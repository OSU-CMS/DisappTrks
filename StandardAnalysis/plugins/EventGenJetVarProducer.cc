#include "EventGenJetVarProducer.h"

EventGenJetVarProducer::EventGenJetVarProducer(const edm::ParameterSet &cfg) : 
  EventVariableProducer(cfg) {
  	genJetsTag_ = edm::InputTag("slimmedGenJets");
  	genJetsToken_ = consumes<reco::GenJetCollection> (genJetsTag_);
}

void EventGenJetVarProducer::AddVariables(const edm::Event &event) {

	edm::Handle<reco::GenJetCollection> genJets;
	event.getByToken(genJetsToken_, genJets);

	int n = 0, n30 = 0, n50 = 0, n80 = 0, n100 = 0;
	double minPt = -1;

	for(const auto &jet : *genJets) {
		if(jet.pt() > minPt) minPt = jet.pt();

		n++;
		if(jet.pt() > 30) n30++;
		if(jet.pt() > 50) n50++;
		if(jet.pt() > 80) n80++;
		if(jet.pt() > 100) n100++;
	}

	(*eventvariables)["nGenJets"] = n;
	(*eventvariables)["nGenJets30"] = n30;
	(*eventvariables)["nGenJets50"] = n50;
	(*eventvariables)["nGenJets80"] = n80;
	(*eventvariables)["nGenJets100"] = n100;

	(*eventvariables)["minGenJetPt"] = minPt;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventGenJetVarProducer);
