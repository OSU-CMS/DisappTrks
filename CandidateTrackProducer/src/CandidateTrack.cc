#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

CandidateTrack::CandidateTrack () : 
  caloEMDeltaRp3_  (numeric_limits<int>::min()), 
  caloHadDeltaRp3_ (numeric_limits<int>::min()),    
  caloEMDeltaRp5_  (numeric_limits<int>::min()),  
  caloHadDeltaRp5_ (numeric_limits<int>::min())  
{
}

CandidateTrack::CandidateTrack (const reco::Track &track) :
  reco::Track (track), 
  caloEMDeltaRp3_  (numeric_limits<int>::min()), 
  caloHadDeltaRp3_ (numeric_limits<int>::min()),    
  caloEMDeltaRp5_  (numeric_limits<int>::min()),  
  caloHadDeltaRp5_ (numeric_limits<int>::min())  
{

  // initialize variables to unphysical defaults


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


const double
CandidateTrack::caloEMDeltaRp3 () const
{
  return this->caloEMDeltaRp3_;
}

const double
CandidateTrack::caloHadDeltaRp3 () const
{
  return this->caloHadDeltaRp3_;
}

const double
CandidateTrack::caloTotDeltaRp3 () const
{
  return this->caloEMDeltaRp3_ + this->caloHadDeltaRp3_;
}

const double
CandidateTrack::caloEMDeltaRp5 () const
{
  return this->caloEMDeltaRp5_;
}

const double
CandidateTrack::caloHadDeltaRp5 () const
{
  return this->caloHadDeltaRp5_;
}

const double
CandidateTrack::caloTotDeltaRp5 () const
{
  return this->caloEMDeltaRp5_ + this->caloHadDeltaRp5_;
}

