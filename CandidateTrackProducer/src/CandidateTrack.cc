#include "DataFormats/Math/interface/deltaR.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

CandidateTrack::CandidateTrack () :
  caloEMDeltaRp3_          (numeric_limits<int>::min ()),
  caloHadDeltaRp3_         (numeric_limits<int>::min ()),
  caloEMDeltaRp5_          (numeric_limits<int>::min ()),
  caloHadDeltaRp5_         (numeric_limits<int>::min ()),
  deltaRToClosestElectron_ (numeric_limits<int>::min ()),
  deltaRToClosestMuon_     (numeric_limits<int>::min ()),
  deltaRToClosestTau_      (numeric_limits<int>::min ()),
  trackIsolationDeltaRp3_  (numeric_limits<int>::min ()),
  trackIsolationDeltaRp5_  (numeric_limits<int>::min ())
{
}

CandidateTrack::CandidateTrack (const reco::Track &track) :
  reco::Track (track),
  caloEMDeltaRp3_          (numeric_limits<int>::min ()),
  caloHadDeltaRp3_         (numeric_limits<int>::min ()),
  caloEMDeltaRp5_          (numeric_limits<int>::min ()),
  caloHadDeltaRp5_         (numeric_limits<int>::min ()),
  deltaRToClosestElectron_ (numeric_limits<int>::min ()),
  deltaRToClosestMuon_     (numeric_limits<int>::min ()),
  deltaRToClosestTau_      (numeric_limits<int>::min ()),
  trackIsolationDeltaRp3_  (numeric_limits<int>::min ()),
  trackIsolationDeltaRp5_  (numeric_limits<int>::min ())
{
}

CandidateTrack::CandidateTrack (const reco::Track &track, const vector<reco::Track> &tracks, const vector<pat::Electron> &electrons, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus) :
  reco::Track (track),
  caloEMDeltaRp3_          (numeric_limits<int>::min ()),
  caloHadDeltaRp3_         (numeric_limits<int>::min ()),
  caloEMDeltaRp5_          (numeric_limits<int>::min ()),
  caloHadDeltaRp5_         (numeric_limits<int>::min ()),
  deltaRToClosestElectron_ (getMinDeltaR (electrons)),
  deltaRToClosestMuon_     (getMinDeltaR (muons)),
  deltaRToClosestTau_      (getMinDeltaR (taus)),
  trackIsolationDeltaRp3_  (getTrackIsolation (track, tracks, 0.3)),
  trackIsolationDeltaRp5_  (getTrackIsolation (track, tracks, 0.5))
{
}

CandidateTrack::~CandidateTrack ()
{
}

template<class T> const double
CandidateTrack::getMinDeltaR (const vector<T> &objects) const
{
  double minDeltaR = numeric_limits<int>::min ();

  for (const auto &object : objects)
    {
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
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

const double
CandidateTrack::deltaRToClosestElectron () const
{
  return this->deltaRToClosestElectron_;
}

const double
CandidateTrack::deltaRToClosestMuon () const
{
  return this->deltaRToClosestMuon_;
}

const double
CandidateTrack::deltaRToClosestTau () const
{
  return this->deltaRToClosestTau_;
}

const double
CandidateTrack::trackIsolationDeltaRp3 () const
{
  return this->trackIsolationDeltaRp3_;
}

const double
CandidateTrack::trackIsolationDeltaRp5 () const
{
  return this->trackIsolationDeltaRp5_;
}

const double
CandidateTrack::getTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}
