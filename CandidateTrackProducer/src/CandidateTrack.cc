#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "TMath.h"

CandidateTrack::CandidateTrack () :
  caloEMDRp3_                    (INVALID_VALUE),
  caloHadDRp3_                   (INVALID_VALUE),
  caloEMDRp5_                    (INVALID_VALUE),
  caloHadDRp5_                   (INVALID_VALUE),
  caloNewEMDRp5_                 (INVALID_VALUE),
  caloNewHadDRp5_                (INVALID_VALUE),
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
                                const vector<reco::Track> &tracks) :
  reco::Track (track),
  caloEMDRp3_                    (INVALID_VALUE),
  caloHadDRp3_                   (INVALID_VALUE),
  caloEMDRp5_                    (INVALID_VALUE),
  caloHadDRp5_                   (INVALID_VALUE),
  caloNewEMDRp5_                 (INVALID_VALUE),
  caloNewHadDRp5_                (INVALID_VALUE),
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

const double
CandidateTrack::caloTotNoPU (double dR, RhoType rhoType, CaloType caloType) const
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
  
  double rawCaloTot = 0.0;
  switch (caloType) {
  case Sum:
    if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
      rawCaloTot = caloNewDRp3();
    } else rawCaloTot = caloNewDRp5();
    break;
  case EM:
    if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
      rawCaloTot = caloNewEMDRp3();
    } else rawCaloTot = caloNewEMDRp5();
    break;
  case Had:
    if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
      rawCaloTot = caloNewHadDRp3();
    } else rawCaloTot = caloNewHadDRp5();
    break; 
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

      if (noPU && fabs( track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ()))
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
