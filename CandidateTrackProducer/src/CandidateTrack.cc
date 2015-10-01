#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

CandidateTrack::CandidateTrack ()
{
}

CandidateTrack::CandidateTrack (const reco::Track &track) :
  reco::Track (track)
{
}

CandidateTrack::~CandidateTrack ()
{
}

const int
CandidateTrack::missingInnerHits () const
{
  return this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS);
}

const int
CandidateTrack::missingMiddleHits () const
{
  return this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS);
}

const int
CandidateTrack::missingOuterHits () const
{
  return this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS);
}
