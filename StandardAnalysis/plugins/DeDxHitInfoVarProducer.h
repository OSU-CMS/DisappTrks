#ifndef DEDX_HIT_INFO_VAR_PRODUCER
#define DEDX_HIT_INFO_VAR_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/TrackReco/interface/DeDxData.h"
#include "DataFormats/TrackReco/interface/DeDxHitInfo.h"
#include "RecoTracker/DeDx/interface/DeDxTools.h"

class DeDxHitInfoVarProducer : public EventVariableProducer {
public:
  DeDxHitInfoVarProducer(const edm::ParameterSet &);
  ~DeDxHitInfoVarProducer() {};

private:
  void AddVariables(const edm::Event &, const edm::EventSetup &, const edm::EventSetup &);

  edm::EDGetTokenT<reco::DeDxHitInfoAss> isoTrk2dedxHitInfoToken_;
  edm::EDGetTokenT<vector<osu::Track> > tracksToken_;
};

#endif
