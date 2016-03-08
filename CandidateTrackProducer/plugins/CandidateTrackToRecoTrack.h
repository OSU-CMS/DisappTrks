#ifndef CANDIDATE_TRACK_TO_RECO_TRACK

#define CANDIDATE_TRACK_TO_RECO_TRACK

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

using namespace std;

class CandidateTrackToRecoTrack : public edm::EDProducer {
   public:
      explicit CandidateTrackToRecoTrack (const edm::ParameterSet &);
      ~CandidateTrackToRecoTrack ();

   private:
      void produce (edm::Event &, const edm::EventSetup &);

      edm::InputTag tracks_;
      edm::EDGetTokenT<vector<CandidateTrack> > tracksToken_;
};

#endif
