#include "DataFormats/Math/interface/deltaR.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

// FIXME:  Once OSUT3Analysis works with ROOT6, i.e., releases > CMSSW_7_4_5_ROOT5,
// then uncomment the following line:
// #include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
// and remove these two lines:
#define INVALID_VALUE (numeric_limits<int>::min ())
#define IS_INVALID(x) (x <= INVALID_VALUE + 1)


CandidateTrack::CandidateTrack () :
  caloEMDRp3_               (INVALID_VALUE),
  caloHadDRp3_              (INVALID_VALUE),
  caloEMDRp5_               (INVALID_VALUE),
  caloHadDRp5_              (INVALID_VALUE),
  caloNewEMDRp5_            (INVALID_VALUE),
  caloNewHadDRp5_           (INVALID_VALUE),
  deltaRToClosestElectron_  (INVALID_VALUE),
  deltaRToClosestVetoElectron_  (INVALID_VALUE),
  deltaRToClosestLooseElectron_  (INVALID_VALUE),
  deltaRToClosestMediumElectron_  (INVALID_VALUE),
  deltaRToClosestTightElectron_  (INVALID_VALUE),
  deltaRToClosestMuon_      (INVALID_VALUE),
  deltaRToClosestLooseMuon_      (INVALID_VALUE),
  deltaRToClosestMediumMuon_      (INVALID_VALUE),
  deltaRToClosestTightMuon_      (INVALID_VALUE),
  deltaRToClosestTau_       (INVALID_VALUE),
  deltaRToClosestTauHad_    (INVALID_VALUE),
  rhoPUCorr_                (INVALID_VALUE),
  rhoPUCorrCalo_            (INVALID_VALUE),
  rhoPUCorrCentralCalo_     (INVALID_VALUE),
  trackIsoDRp3_             (INVALID_VALUE),
  trackIsoDRp5_             (INVALID_VALUE),
  trackIsoNoPUDRp3_         (INVALID_VALUE),
  trackIsoNoPUDRp5_         (INVALID_VALUE)
{
}

CandidateTrack::CandidateTrack (const reco::Track &track) :
  reco::Track (track),
  caloEMDRp3_               (INVALID_VALUE),
  caloHadDRp3_              (INVALID_VALUE),
  caloEMDRp5_               (INVALID_VALUE),
  caloHadDRp5_              (INVALID_VALUE),
  caloNewEMDRp5_            (INVALID_VALUE),
  caloNewHadDRp5_           (INVALID_VALUE),
  deltaRToClosestElectron_  (INVALID_VALUE),
  deltaRToClosestVetoElectron_  (INVALID_VALUE),
  deltaRToClosestLooseElectron_  (INVALID_VALUE),
  deltaRToClosestMediumElectron_  (INVALID_VALUE),
  deltaRToClosestTightElectron_  (INVALID_VALUE),
  deltaRToClosestMuon_      (INVALID_VALUE),
  deltaRToClosestLooseMuon_      (INVALID_VALUE),
  deltaRToClosestMediumMuon_      (INVALID_VALUE),
  deltaRToClosestTightMuon_      (INVALID_VALUE),
  deltaRToClosestTau_       (INVALID_VALUE),
  deltaRToClosestTauHad_    (INVALID_VALUE),
  rhoPUCorr_                (INVALID_VALUE),
  rhoPUCorrCalo_            (INVALID_VALUE),
  rhoPUCorrCentralCalo_     (INVALID_VALUE),
  trackIsoDRp3_             (INVALID_VALUE),
  trackIsoDRp5_             (INVALID_VALUE),
  trackIsoNoPUDRp3_         (INVALID_VALUE),
  trackIsoNoPUDRp5_         (INVALID_VALUE)
{
}

CandidateTrack::CandidateTrack (const reco::Track &track, const vector<reco::Track> &tracks, const vector<pat::Electron> &electrons, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus, const reco::BeamSpot &beamspot, const vector<reco::Vertex> &vertices, const edm::Handle<vector<reco::Conversion> > &conversions) :
  reco::Track (track),
  caloEMDRp3_              (INVALID_VALUE),
  caloHadDRp3_             (INVALID_VALUE),
  caloEMDRp5_              (INVALID_VALUE),
  caloHadDRp5_             (INVALID_VALUE),
  caloNewEMDRp5_           (INVALID_VALUE),
  caloNewHadDRp5_          (INVALID_VALUE),
  deltaRToClosestElectron_ (getMinDeltaR (electrons)),
  deltaRToClosestVetoElectron_ (vertices.size () ? getMinDeltaRToVetoElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestLooseElectron_ (vertices.size () ? getMinDeltaRToLooseElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestMediumElectron_ (vertices.size () ? getMinDeltaRToMediumElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestTightElectron_ (vertices.size () ? getMinDeltaRToTightElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestMuon_     (getMinDeltaR (muons)),
  deltaRToClosestLooseMuon_     (getMinDeltaRToLooseMuon (muons)),
  deltaRToClosestMediumMuon_     (getMinDeltaRToMediumMuon (muons)),
  deltaRToClosestTightMuon_     (vertices.size () ? getMinDeltaRToTightMuon (muons, vertices.at (0)) : INVALID_VALUE),
  deltaRToClosestTau_      (getMinDeltaR (taus)),
  deltaRToClosestTauHad_   (getMinDeltaRToTauHad (taus)),
  rhoPUCorr_               (INVALID_VALUE),
  rhoPUCorrCalo_           (INVALID_VALUE),
  rhoPUCorrCentralCalo_    (INVALID_VALUE),
  trackIsoDRp3_            (getTrackIsolation (track, tracks, false, 0.3)),
  trackIsoDRp5_            (getTrackIsolation (track, tracks, false, 0.5)),
  trackIsoNoPUDRp3_        (getTrackIsolation (track, tracks, true, 0.3)),
  trackIsoNoPUDRp5_        (getTrackIsolation (track, tracks, true, 0.5))
{
}

CandidateTrack::~CandidateTrack ()
{
}

template<class T> const double
CandidateTrack::getMinDeltaR (const vector<T> &objects) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToTauHad (const vector<pat::Tau> &objects) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (object.tauID ("decayModeFinding") < 0.5 || object.tauID ("againstElectronLooseMVA6") < 0.5 || object.tauID ("againstMuonLoose3") < 0.5)
      // See references:
      // https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID
      // https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToVetoElectron (const vector<pat::Electron> &objects, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!passesVetoID (object, beamspot, vertex, conversions))
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToLooseElectron (const vector<pat::Electron> &objects, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!passesLooseID (object, beamspot, vertex, conversions))
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToMediumElectron (const vector<pat::Electron> &objects, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!passesMediumID (object, beamspot, vertex, conversions))
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToTightElectron (const vector<pat::Electron> &objects, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!passesTightID (object, beamspot, vertex, conversions))
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToLooseMuon (const vector<pat::Muon> &objects) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!object.isLooseMuon ())
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToMediumMuon (const vector<pat::Muon> &objects) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!object.isMediumMuon ())
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const double
CandidateTrack::getMinDeltaRToTightMuon (const vector<pat::Muon> &objects, const reco::Vertex &vertex) const
{
  double minDeltaR = INVALID_VALUE;

  for (const auto &object : objects)
    {
      if (!object.isTightMuon (vertex))
        continue;
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const int
CandidateTrack::numberOfTrackerHits () const
{
  return this->hitPattern ().trackerLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfPixelHits () const
{
  return this->hitPattern ().pixelLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfStripHits () const
{
  return this->hitPattern ().stripLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfPixelBarrelHits () const
{
  return this->hitPattern ().pixelBarrelLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfPixelEndcapHits () const
{
  return this->hitPattern ().pixelEndcapLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfStripTIBHits () const
{
  return this->hitPattern ().stripTIBLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfStripTIDHits () const
{
  return this->hitPattern ().stripTIDLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfStripTOBHits () const
{
  return this->hitPattern ().stripTOBLayersWithMeasurement ();
}

const int
CandidateTrack::numberOfStripTECHits () const
{
  return this->hitPattern ().stripTECLayersWithMeasurement ();
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

const int
CandidateTrack::missingTrackerHits () const
{
  return (this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingPixelHits () const
{
  return (this->hitPattern ().pixelLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().pixelLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().pixelLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingStripHits () const
{
  return (this->hitPattern ().stripLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingPixelBarrelHits () const
{
  return (this->hitPattern ().pixelBarrelLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().pixelBarrelLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().pixelBarrelLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingPixelEndcapHits () const
{
  return (this->hitPattern ().pixelEndcapLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().pixelEndcapLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().pixelEndcapLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingStripTIBHits () const
{
  return (this->hitPattern ().stripTIBLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTIBLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTIBLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingStripTIDHits () const
{
  return (this->hitPattern ().stripTIDLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTIDLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTIDLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingStripTOBHits () const
{
  return (this->hitPattern ().stripTOBLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTOBLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTOBLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::missingStripTECHits () const
{
  return (this->hitPattern ().stripTECLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTECLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTECLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedTrackerHits () const
{
  return (this->hitPattern ().trackerLayersWithMeasurement ()
        + this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedPixelHits () const
{
  return (this->hitPattern ().pixelLayersWithMeasurement ()
        + this->hitPattern ().pixelLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().pixelLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().pixelLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedStripHits () const
{
  return (this->hitPattern ().stripLayersWithMeasurement ()
        + this->hitPattern ().stripLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedPixelBarrelHits () const
{
  return (this->hitPattern ().pixelBarrelLayersWithMeasurement ()
        + this->hitPattern ().pixelBarrelLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().pixelBarrelLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().pixelBarrelLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedPixelEndcapHits () const
{
  return (this->hitPattern ().pixelEndcapLayersWithMeasurement ()
        + this->hitPattern ().pixelEndcapLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().pixelEndcapLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().pixelEndcapLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedStripTIBHits () const
{
  return (this->hitPattern ().stripTIBLayersWithMeasurement ()
        + this->hitPattern ().stripTIBLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTIBLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTIBLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedStripTIDHits () const
{
  return (this->hitPattern ().stripTIDLayersWithMeasurement ()
        + this->hitPattern ().stripTIDLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTIDLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTIDLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedStripTOBHits () const
{
  return (this->hitPattern ().stripTOBLayersWithMeasurement ()
        + this->hitPattern ().stripTOBLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTOBLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTOBLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const int
CandidateTrack::expectedStripTECHits () const
{
  return (this->hitPattern ().stripTECLayersWithMeasurement ()
        + this->hitPattern ().stripTECLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS)
        + this->hitPattern ().stripTECLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS)
        + this->hitPattern ().stripTECLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
}

const double
CandidateTrack::caloEMDRp3 () const
{
  return this->caloEMDRp3_;
}

const double
CandidateTrack::caloHadDRp3 () const
{
  return this->caloHadDRp3_;
}

const double
CandidateTrack::caloTotDRp3 () const
{
  return this->caloEMDRp3_ + this->caloHadDRp3_;
}

const double
CandidateTrack::caloEMDRp5 () const
{
  return this->caloEMDRp5_;
}

const double
CandidateTrack::caloHadDRp5 () const
{
  return this->caloHadDRp5_;
}

const double
CandidateTrack::caloNewEMDRp5 () const
{
  return this->caloNewEMDRp5_;
}

const double
CandidateTrack::caloNewHadDRp5 () const
{
  return this->caloNewHadDRp5_;
}

const double
CandidateTrack::caloTotDRp5 () const
{
  return this->caloEMDRp5_ + this->caloHadDRp5_;
}

const double
CandidateTrack::caloNewDRp5 () const
{
  return this->caloNewEMDRp5_ + this->caloNewHadDRp5_;
}

const double
CandidateTrack::caloTotNoPUDRp3 () const
{
  return caloTotNoPU(0.3);
}

const double
CandidateTrack::caloTotNoPUDRp4 () const
{
  return caloTotNoPU(0.4);
}

const double
CandidateTrack::caloTotNoPUDRp5 () const
{
  return caloTotNoPU(0.5, CandidateTrack::All);
}

const double
CandidateTrack::caloTotNoPUDRp5Calo () const
{
  return caloTotNoPU(0.5, CandidateTrack::Calo);
}

const double
CandidateTrack::caloTotNoPUDRp5CentralCalo () const
{
  return caloTotNoPU(0.5, CandidateTrack::CentralCalo);
}

const double
CandidateTrack::caloNewNoPUDRp5CentralCalo () const
{
  return caloTotNoPU(0.5, CandidateTrack::CentralCalo, true);
}

const double
CandidateTrack::caloTotNoPU (double dR, RhoType rhoType, bool useNewCalc) const
{
  // For reference, see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Accessing_PF_Isolation_from_AN1
  double rho;
  switch (rhoType) {
  case All:
    rho = rhoPUCorr();
    break;
  case Calo:
    rho = rhoPUCorrCalo();
    break;
  case CentralCalo:
    rho = rhoPUCorrCentralCalo();
    break;
  default:
    throw cms::Exception("FatalError") << "Unkown or not implemented rho type requested, type:" << rhoType;
  }

  double rawCaloTot = caloTotDRp5();
  if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
    rawCaloTot = caloTotDRp3();
  }
  if (useNewCalc) {
    rawCaloTot = caloNewDRp5();
  }
  double caloCorr = rho * TMath::Pi() * pow(dR, 2);  // Define effective area as pi*r^2, where r is radius of DeltaR cone.
  double caloTotNoPUDRp5 = TMath::Max(0., rawCaloTot - caloCorr);
  return caloTotNoPUDRp5;
}

const double
CandidateTrack::deltaRToClosestElectron () const
{
  if (IS_INVALID (this->deltaRToClosestElectron_))
    return MAX_DR;
  return this->deltaRToClosestElectron_;
}

const double
CandidateTrack::deltaRToClosestVetoElectron () const
{
  if (IS_INVALID (this->deltaRToClosestVetoElectron_))
    return MAX_DR;
  return this->deltaRToClosestVetoElectron_;
}

const double
CandidateTrack::deltaRToClosestLooseElectron () const
{
  if (IS_INVALID (this->deltaRToClosestLooseElectron_))
    return MAX_DR;
  return this->deltaRToClosestLooseElectron_;
}

const double
CandidateTrack::deltaRToClosestMediumElectron () const
{
  if (IS_INVALID (this->deltaRToClosestMediumElectron_))
    return MAX_DR;
  return this->deltaRToClosestMediumElectron_;
}

const double
CandidateTrack::deltaRToClosestTightElectron () const
{
  if (IS_INVALID (this->deltaRToClosestTightElectron_))
    return MAX_DR;
  return this->deltaRToClosestTightElectron_;
}

const double
CandidateTrack::deltaRToClosestMuon () const
{
  if (IS_INVALID (this->deltaRToClosestMuon_))
    return MAX_DR;
  return this->deltaRToClosestMuon_;
}

const double
CandidateTrack::deltaRToClosestLooseMuon () const
{
  if (IS_INVALID (this->deltaRToClosestLooseMuon_))
    return MAX_DR;
  return this->deltaRToClosestLooseMuon_;
}

const double
CandidateTrack::deltaRToClosestMediumMuon () const
{
  if (IS_INVALID (this->deltaRToClosestMediumMuon_))
    return MAX_DR;
  return this->deltaRToClosestMediumMuon_;
}

const double
CandidateTrack::deltaRToClosestTightMuon () const
{
  if (IS_INVALID (this->deltaRToClosestTightMuon_))
    return MAX_DR;
  return this->deltaRToClosestTightMuon_;
}

const double
CandidateTrack::deltaRToClosestTau () const
{
  if (IS_INVALID (this->deltaRToClosestTau_))
    return MAX_DR;
  return this->deltaRToClosestTau_;
}

const double
CandidateTrack::deltaRToClosestTauHad () const
{
  if (IS_INVALID (this->deltaRToClosestTauHad_))
    return MAX_DR;
  return this->deltaRToClosestTauHad_;
}

const double
CandidateTrack::rhoPUCorr () const
{
  return this->rhoPUCorr_;
}

const double
CandidateTrack::rhoPUCorrCalo () const
{
  return this->rhoPUCorrCalo_;
}

const double
CandidateTrack::rhoPUCorrCentralCalo () const
{
  return this->rhoPUCorrCentralCalo_;
}

const double
CandidateTrack::trackIsoDRp3 () const
{
  return this->trackIsoDRp3_;
}

const double
CandidateTrack::trackIsoDRp5 () const
{
  return this->trackIsoDRp5_;
}

const double
CandidateTrack::trackIsoNoPUDRp3 () const
{
  return this->trackIsoNoPUDRp3_;
}

const double
CandidateTrack::trackIsoNoPUDRp5 () const
{
  return this->trackIsoNoPUDRp5_;
}

const double
CandidateTrack::getTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      /*if (noPU && track.normalizedChi2 () > 20.0)
        continue;
      if (noPU && track.hitPattern ().pixelLayersWithMeasurement () < 2)
        continue;
      if (noPU && track.hitPattern ().trackerLayersWithMeasurement () < 5)
        continue;
      if (noPU && fabs (track.d0 () / track.d0Error ()) > 5.0)
        continue;*/
      if (noPU && track.dz (t.vertex ()) > 3.0 * hypot (track.dzError (), t.dzError ()))
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

const double
CandidateTrack::energyOfElectron () const
{
  return energyGivenMass (0.000510998928);
}

const double
CandidateTrack::energyOfMuon () const
{
  return energyGivenMass (0.1056583715);
}

const double
CandidateTrack::energyOfTau () const
{
  return energyGivenMass (1.77686);
}

const double
CandidateTrack::energyOfPion () const
{
  return energyGivenMass (0.13957018);
}

const double
CandidateTrack::energyOfProton () const
{
  return energyGivenMass (0.938272046);
}

const double
CandidateTrack::energyGivenMass (const double mass) const
{
  return sqrt (this->px () * this->px () + this->py () * this->py () + this->pz () * this->pz () + mass * mass);
}

bool
CandidateTrack::passesVetoID (const pat::Electron &electron, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0114
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.0152
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.216
           && electron.hadronicOverEm ()                                                                     <   0.181
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.207
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0564
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.472
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0352
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.0113
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.237
           && electron.hadronicOverEm ()                                                                     <   0.116
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.174
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.222
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.921
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  3
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  return false;
}

bool
CandidateTrack::passesLooseID (const pat::Electron &electron, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0103
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.0105
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.115
           && electron.hadronicOverEm ()                                                                     <   0.104
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.102
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0261
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.41
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0301
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00814
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.182
           && electron.hadronicOverEm ()                                                                     <   0.0897
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.126
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.118
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.822
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  return false;
}

bool
CandidateTrack::passesMediumID (const pat::Electron &electron, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0101
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.0103
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0336
           && electron.hadronicOverEm ()                                                                     <   0.0876
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.0174
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0118
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.373
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0283
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00733
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.114
           && electron.hadronicOverEm ()                                                                     <   0.0678
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.0898
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0739
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.602
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  return false;
}

bool
CandidateTrack::passesTightID (const pat::Electron &electron, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0101
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00926
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0336
           && electron.hadronicOverEm ()                                                                     <   0.0597
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.012
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0111
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.0466
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0279
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00724
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0918
           && electron.hadronicOverEm ()                                                                     <   0.0615
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.00999
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0351
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.417
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  return false;
}
