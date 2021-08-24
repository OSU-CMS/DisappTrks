#include "TLorentzVector.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisappTrks/ToyModels/plugins/TrainingPreselectionSkim.h"


TrainingPreselectionSkim::TrainingPreselectionSkim (const edm::ParameterSet& iConfig) :

  dataTakingPeriod_ (iConfig.getParameter<string> ("dataTakingPeriod")),
  tracks_ (iConfig.getParameter<edm::InputTag> ("tracks"))

{
  //assert(dataTakingPeriod_ == "2017");

  is2017_ = (dataTakingPeriod_ == "2017");

  tracksToken_ = consumes<vector<reco::Track> > (tracks_);
}

TrainingPreselectionSkim::~TrainingPreselectionSkim ()
{
}

bool TrainingPreselectionSkim::filter (edm::Event &event, const edm::EventSetup &setup)
{

  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken(tracksToken_, tracks);

  //////////////////////////////
  
  for(const auto &track : *tracks){

    //std::cout << "Looking at track" << std::endl;

    bool inTOBCrack = (fabs(track.dz()) < 0.5 && fabs(M_PI_2 - track.theta()) < 1.0e-3);
    bool inECALCrack = (fabs(track.eta()) >= 1.42 && fabs(track.eta()) <= 1.65);
    bool inDTWheelGap = (fabs(track.eta()) >= 0.15 && fabs(track.eta()) <= 0.35);
    bool inCSCTransitionRegion = (fabs(track.eta()) >= 1.55 && fabs(track.eta()) <= 1.85);

    if(!(fabs(track.eta()) <= 2.4)) continue;
    if(!(track.pt() >= 55)) continue;
    if(!(track.hitPattern().numberOfValidPixelHits() >= 4)) continue;
    if(!(track.hitPattern().numberOfValidHits() >= 4)) continue;
    if(!(track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0)) continue;
    if(!(track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0)) continue;
    if(inTOBCrack || inECALCrack || inDTWheelGap || inCSCTransitionRegion) continue;
  
    return true;
  }

  return false;
}

DEFINE_FWK_MODULE(TrainingPreselectionSkim);

