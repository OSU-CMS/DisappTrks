#include "DataFormats/Math/interface/deltaR.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

#include "OSUT3Analysis/AnaTools/interface/CMSSWVersion.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

CandidateTrack::CandidateTrack () :
  caloEMDRp3_                    (INVALID_VALUE),
  caloHadDRp3_                   (INVALID_VALUE),
  caloEMDRp5_                    (INVALID_VALUE),
  caloHadDRp5_                   (INVALID_VALUE),
  caloNewEMDRp5_                 (INVALID_VALUE),
  caloNewHadDRp5_                (INVALID_VALUE),
  deltaRToClosestElectron_       (INVALID_VALUE),
  deltaRToClosestVetoElectron_   (INVALID_VALUE),
  deltaRToClosestLooseElectron_  (INVALID_VALUE),
  deltaRToClosestMediumElectron_ (INVALID_VALUE),
  deltaRToClosestTightElectron_  (INVALID_VALUE),
  deltaRToClosestMuon_           (INVALID_VALUE),
  deltaRToClosestLooseMuon_      (INVALID_VALUE),
  deltaRToClosestMediumMuon_     (INVALID_VALUE),
  deltaRToClosestTightMuon_      (INVALID_VALUE),
  deltaRToClosestTau_            (INVALID_VALUE),
  deltaRToClosestTauHad_         (INVALID_VALUE),
  rhoPUCorr_                     (INVALID_VALUE),
  rhoPUCorrCalo_                 (INVALID_VALUE),
  rhoPUCorrCentralCalo_          (INVALID_VALUE),
  trackIsoDRp3_                  (INVALID_VALUE),
  trackIsoDRp5_                  (INVALID_VALUE),
  trackIsoNoPUDRp3_              (INVALID_VALUE),
  trackIsoNoPUDRp5_              (INVALID_VALUE),
  trackIsoNoFakesDRp3_           (INVALID_VALUE),
  trackIsoNoFakesDRp5_           (INVALID_VALUE),
  trackIsoNoPUNoFakesDRp3_       (INVALID_VALUE),
  trackIsoNoPUNoFakesDRp5_       (INVALID_VALUE),
  trackIsoOldNoPUDRp3_           (INVALID_VALUE),
  trackIsoOldNoPUDRp5_           (INVALID_VALUE)
{
}

CandidateTrack::CandidateTrack (const reco::Track &track) :
  reco::Track (track),
  caloEMDRp3_                    (INVALID_VALUE),
  caloHadDRp3_                   (INVALID_VALUE),
  caloEMDRp5_                    (INVALID_VALUE),
  caloHadDRp5_                   (INVALID_VALUE),
  caloNewEMDRp5_                 (INVALID_VALUE),
  caloNewHadDRp5_                (INVALID_VALUE),
  deltaRToClosestElectron_       (INVALID_VALUE),
  deltaRToClosestVetoElectron_   (INVALID_VALUE),
  deltaRToClosestLooseElectron_  (INVALID_VALUE),
  deltaRToClosestMediumElectron_ (INVALID_VALUE),
  deltaRToClosestTightElectron_  (INVALID_VALUE),
  deltaRToClosestMuon_           (INVALID_VALUE),
  deltaRToClosestLooseMuon_      (INVALID_VALUE),
  deltaRToClosestMediumMuon_     (INVALID_VALUE),
  deltaRToClosestTightMuon_      (INVALID_VALUE),
  deltaRToClosestTau_            (INVALID_VALUE),
  deltaRToClosestTauHad_         (INVALID_VALUE),
  rhoPUCorr_                     (INVALID_VALUE),
  rhoPUCorrCalo_                 (INVALID_VALUE),
  rhoPUCorrCentralCalo_          (INVALID_VALUE),
  trackIsoDRp3_                  (INVALID_VALUE),
  trackIsoDRp5_                  (INVALID_VALUE),
  trackIsoNoPUDRp3_              (INVALID_VALUE),
  trackIsoNoPUDRp5_              (INVALID_VALUE),
  trackIsoNoFakesDRp3_           (INVALID_VALUE),
  trackIsoNoFakesDRp5_           (INVALID_VALUE),
  trackIsoNoPUNoFakesDRp3_       (INVALID_VALUE),
  trackIsoNoPUNoFakesDRp5_       (INVALID_VALUE),
  trackIsoOldNoPUDRp3_           (INVALID_VALUE),
  trackIsoOldNoPUDRp5_           (INVALID_VALUE)
{
}

CandidateTrack::CandidateTrack (const reco::Track &track, 
                                const vector<reco::Track> &tracks, 
                                const vector<pat::Electron> &electrons, 
                                const vector<pat::Muon> &muons, 
                                const vector<pat::Tau> &taus, 
                                const reco::BeamSpot &beamspot, 
                                const vector<reco::Vertex> &vertices, 
                                const edm::Handle<vector<reco::Conversion> > &conversions) :
  reco::Track (track),
  caloEMDRp3_                    (INVALID_VALUE),
  caloHadDRp3_                   (INVALID_VALUE),
  caloEMDRp5_                    (INVALID_VALUE),
  caloHadDRp5_                   (INVALID_VALUE),
  caloNewEMDRp5_                 (INVALID_VALUE),
  caloNewHadDRp5_                (INVALID_VALUE),
  deltaRToClosestElectron_       (getMinDeltaR (electrons)),
  deltaRToClosestVetoElectron_   (vertices.size () ? getMinDeltaRToVetoElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestLooseElectron_  (vertices.size () ? getMinDeltaRToLooseElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestMediumElectron_ (vertices.size () ? getMinDeltaRToMediumElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestTightElectron_  (vertices.size () ? getMinDeltaRToTightElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestMuon_           (getMinDeltaR (muons)),
  deltaRToClosestLooseMuon_      (getMinDeltaRToLooseMuon (muons)),
  deltaRToClosestMediumMuon_     (getMinDeltaRToMediumMuon (muons)),
  deltaRToClosestTightMuon_      (vertices.size () ? getMinDeltaRToTightMuon (muons, vertices.at (0)) : INVALID_VALUE),
  deltaRToClosestTau_            (getMinDeltaR (taus)),
  deltaRToClosestTauHad_         (getMinDeltaRToTauHad (taus)),
  rhoPUCorr_                     (INVALID_VALUE),
  rhoPUCorrCalo_                 (INVALID_VALUE),
  rhoPUCorrCentralCalo_          (INVALID_VALUE),
  trackIsoDRp3_                  (getTrackIsolation (track, tracks, false, false, 0.3)),
  trackIsoDRp5_                  (getTrackIsolation (track, tracks, false, false, 0.5)),
  trackIsoNoPUDRp3_              (getTrackIsolation (track, tracks, true, false, 0.3)),
  trackIsoNoPUDRp5_              (getTrackIsolation (track, tracks, true, false, 0.5)),
  trackIsoNoFakesDRp3_           (getTrackIsolation (track, tracks, false, true, 0.3)),
  trackIsoNoFakesDRp5_           (getTrackIsolation (track, tracks, false, true, 0.5)),
  trackIsoNoPUNoFakesDRp3_       (getTrackIsolation (track, tracks, true, true, 0.3)),
  trackIsoNoPUNoFakesDRp5_       (getTrackIsolation (track, tracks, true, true, 0.5)),
  trackIsoOldNoPUDRp3_           (getOldTrackIsolation (track, tracks, true, 0.3)),
  trackIsoOldNoPUDRp5_           (getOldTrackIsolation (track, tracks, true, 0.5))
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

const double
CandidateTrack::caloTotNoPU (double dR, RhoType rhoType) const
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

  double rawCaloTot = caloNewDRp5();
  if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
    rawCaloTot = caloNewDRp3();
  }
  double caloCorr = rho * TMath::Pi() * dR * dR;  // Define effective area as pi*r^2, where r is radius of DeltaR cone.
  double caloTotNoPU = TMath::Max(0., rawCaloTot - caloCorr);
  return caloTotNoPU;
}

const double
CandidateTrack::getTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const bool noFakes, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      if (noFakes && t.normalizedChi2 () > 20.0)
        continue;
      if (noFakes && t.hitPattern ().pixelLayersWithMeasurement () < 2)
        continue;
      if (noFakes && t.hitPattern ().trackerLayersWithMeasurement () < 5)
        continue;
      if (noFakes && fabs (t.d0 () / t.d0Error ()) > 5.0)
        continue;

      if (noPU && track.dz (t.vertex ()) > 3.0 * hypot (track.dzError (), t.dzError ()))
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

const double
CandidateTrack::getOldTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      if (noPU && track.normalizedChi2 () > 20.0)
        continue;
      if (noPU && track.hitPattern ().pixelLayersWithMeasurement () < 2)
        continue;
      if (noPU && track.hitPattern ().trackerLayersWithMeasurement () < 5)
        continue;
      if (noPU && fabs (track.d0 () / track.d0Error ()) > 5.0)
        continue;
      if (noPU && track.dz (t.vertex ()) > 3.0 * hypot (track.dzError (), t.dzError ()))
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)     <=  2
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  3
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  3
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#endif
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
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
           && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#else
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#endif
           && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  return false;
}
