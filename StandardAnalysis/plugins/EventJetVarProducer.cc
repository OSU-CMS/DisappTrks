#ifndef EVENT_JET_VAR_PRODUCER
#define EVENT_JET_VAR_PRODUCER  

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DataFormats/VertexReco/interface/Vertex.h"



class EventJetVarProducer : public EventVariableProducer
   {
    public:
        EventJetVarProducer (const edm::ParameterSet &);
	~EventJetVarProducer ();

    private:
	void AddVariables(const edm::Event &);
	edm::EDGetTokenT<vector<TYPE(jets)> > token_;
  };





EventJetVarProducer::EventJetVarProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  token_ = consumes<vector<TYPE(jets)> > (collections_.getParameter<edm::InputTag> ("jets"));
}

EventJetVarProducer::~EventJetVarProducer() {}

void
EventJetVarProducer::AddVariables (const edm::Event &event) {

  edm::Handle<vector<TYPE(jets)> > jets;
  if (!event.getByToken (token_, jets)) {
    cout << "ERROR:  Could not find jets collection." << endl; 
    return;
  } 

  int nJets = 0; 
  double dijetMaxDeltaPhi = -999.;  
  int idx1 = -1;
  for (const auto &jet1 : *jets) {
    idx1++;  
    if (!(jet1.pt() > 30))         continue;
    if (!(fabs(jet1.eta()) < 4.5)) continue;
    int idx2 = -1; 
    for (const auto &jet2 : *jets) {
      idx2++;  
      if (idx2 <= idx1)              continue;  // Avoid double-counting.  
      if (!(jet2.pt() > 30))         continue;
      if (!(fabs(jet2.eta()) < 4.5)) continue;
      double dPhi = fabs(deltaPhi(jet1.phi(), jet2.phi()));  
      if (dPhi > dijetMaxDeltaPhi) {
	dijetMaxDeltaPhi = dPhi; 
      }  
    }
    nJets++;  
  }

  (*eventvariables)["nJets"]            = nJets;
  (*eventvariables)["dijetMaxDeltaPhi"] = dijetMaxDeltaPhi; 

}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventJetVarProducer);


#endif

