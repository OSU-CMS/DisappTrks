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
  trackIsoOldNoPUDRp5_           (INVALID_VALUE),
  matchedAnything_               (INVALID_VALUE)
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
  trackIsoOldNoPUDRp5_           (INVALID_VALUE),
  matchedAnything_               (INVALID_VALUE)
{
}

CandidateTrack::CandidateTrack (const reco::Track &track, 
                                const vector<reco::Track> &tracks, 
                                const vector<pat::Electron> &electrons, 
                                const vector<pat::Muon> &muons, 
                                const vector<pat::Tau> &taus, 
                                const reco::BeamSpot &beamspot, 
                                const vector<reco::Vertex> &vertices, 
                                const edm::Handle<vector<reco::Conversion> > &conversions,
                                const pat::PackedCandidateCollection &PackedCandidates,
                                const pat::PackedCandidateCollection &LostTracks,
                                const vector<pat::IsolatedTracks> &IsolatedTracks) :
  reco::Track (track),
  caloEMDRp3_                    (INVALID_VALUE),
  caloHadDRp3_                   (INVALID_VALUE),
  caloEMDRp5_                    (INVALID_VALUE),
  caloHadDRp5_                   (INVALID_VALUE),
  caloNewEMDRp5_                 (INVALID_VALUE),
  caloNewHadDRp5_                (INVALID_VALUE),
  deltaRToClosestElectron_       (getMinDeltaR (electrons)),
  deltaRToClosestVetoElectron_   (!vertices.empty () ? getMinDeltaRToVetoElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestLooseElectron_  (!vertices.empty () ? getMinDeltaRToLooseElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestMediumElectron_ (!vertices.empty () ? getMinDeltaRToMediumElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestTightElectron_  (!vertices.empty () ? getMinDeltaRToTightElectron (electrons, beamspot, vertices.at (0), conversions) : INVALID_VALUE),
  deltaRToClosestMuon_           (getMinDeltaR (muons)),
  deltaRToClosestLooseMuon_      (getMinDeltaRToLooseMuon (muons)),
  deltaRToClosestMediumMuon_     (getMinDeltaRToMediumMuon (muons)),
  deltaRToClosestTightMuon_      (!vertices.empty () ? getMinDeltaRToTightMuon (muons, vertices.at (0)) : INVALID_VALUE),
  deltaRToClosestTau_            (getMinDeltaR (taus)),
  deltaRToClosestTauHad_         (getMinDeltaRToTauHad (taus)),
  rhoPUCorr_                     (INVALID_VALUE),
  rhoPUCorrCalo_                 (INVALID_VALUE),
  rhoPUCorrCentralCalo_          (INVALID_VALUE),
  trackIsoDRp3_                  (getTrackIsolation (track, tracks, false, false, 0.3)),
  trackIsoDRp5_                  (getTrackIsolation (track, tracks, false, false, 0.5)),
  //trackIsoNoPUDRp3_              (getTrackIsolationExtraInfoNoDoubles (track, tracks, true, false, 0.3, 1.0e-12, PackedCandidates)),
  trackIsoNoPUDRp3_              (getTrackIsolation (track, tracks, true, false, 0.3)),
  trackIsoNoPUDRp5_              (getTrackIsolation (track, tracks, true, false, 0.5)),
  trackIsoNoFakesDRp3_           (getTrackIsolation (track, tracks, false, true, 0.3)),
  trackIsoNoFakesDRp5_           (getTrackIsolation (track, tracks, false, true, 0.5)),
  trackIsoNoPUNoFakesDRp3_       (getTrackIsolation (track, tracks, true, true, 0.3)),
  trackIsoNoPUNoFakesDRp5_       (getTrackIsolation (track, tracks, true, true, 0.5)),
  trackIsoOldNoPUDRp3_           (getOldTrackIsolation (track, tracks, true, 0.3)),
  trackIsoOldNoPUDRp5_           (getOldTrackIsolation (track, tracks, true, 0.5)),
  matchedAnything_               (findAnyMatchAndPrint (track, tracks, PackedCandidates, LostTracks, IsolatedTracks))
{
}

CandidateTrack::~CandidateTrack ()
{
}

const bool
CandidateTrack::findAnyMatchAndPrint (const reco::Track &track, const vector<reco::Track> &tracks, const pat::PackedCandidateCollection &pc, const pat::PackedCandidateCollection &lt, const vector<pat::IsolatedTrack> &it, const double outerDeltaR, const double innerDeltaR) const
{
  cout << "Inside my findAnyMatchAndPrint function" << endl;



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
  case EM:
    if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
      rawCaloTot = caloNewEMDRp3();
    } else rawCaloTot = caloNewEMDRp5();
  case Had:
    if (dR < 0.4) {  // Only treat two cases:  0.5 and 0.3.
      rawCaloTot = caloNewHadDRp3();
    } else rawCaloTot = caloNewHadDRp5();  
  }
  
  double caloCorr = rho * TMath::Pi() * dR * dR;  // Define effective area as pi*r^2, where r is radius of DeltaR cone.
  double caloTotNoPU = TMath::Max(0., rawCaloTot - caloCorr);
  return caloTotNoPU;
}

const double
CandidateTrack::getTrackIsolationExtraInfoNoDoubles (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const bool noFakes, const double outerDeltaR, const double innerDeltaR, const pat::PackedCandidateCollection &pc) const
{
  double sumPt = 0.0;
  
  bool print = false;
  if (noPU && !noFakes && outerDeltaR==0.3) print=true;
  if (print) cout << endl << "==============================" << endl << "CandidateTrack Head Track :: pt=" << track.pt() << ", eta=" << track.eta() << ", phi=" << track.phi() << endl << "---------------------------" << endl;
  if (print) cout << "Tracks inside cone:" << endl;

  for (const auto &t : tracks) {
      double dR0 = deltaR (track, t);
      //bool printPT0 = false;
      //if (t.pt() > 1.0) printPT0 = true;
      if (print && dR0 < outerDeltaR && dR0 > innerDeltaR){
        bool matchedAndIncluded = false;
        bool matched0 = false;
        for (auto &candidateMatch : pc) {
          double dRMatch = deltaR (t.eta(), t.phi(), candidateMatch.eta(), candidateMatch.phi());
          if (dRMatch < 0.0001){
            matched0 = true;
            int id = std::abs(candidateMatch.pdgId());
            bool matchIDIncluded = false;
            //if (id == 211 || id == 130 || id == 22) matchIDIncluded = true;
            if (id == 211) matchIDIncluded = true;
            if (!(fabs(track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ())) && (matchIDIncluded)) {
                matchedAndIncluded = true;
                break;
            }
          }
        }
        if (!matchedAndIncluded) {
          cout << "\tTrack w/ pt=" << t.pt() << ", eta=" << t.eta() << ", phi=" << t.phi() << ", dR=" << dR0 << endl;
          cout << "\t-- dz=" << track.dz (t.vertex()) << ", 3sigZ=" << 3.0 * hypot (track.dzError (), t.dzError ()) << endl;
          bool passedOURisolation = !(fabs(track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ()));
          if (passedOURisolation){
            cout << "\t----Passed OUR isolation calc: " << passedOURisolation << endl << "\t------but not included in pfIsolation" << endl;
          } else {
            if (matched0) {
              cout << "\t----Passed OUR isolation calc: " << passedOURisolation << endl << "\t------but found a match in pfIsolation" << endl;
            } else {
              cout << "\t----Passed OUR isolation calc: " << passedOURisolation << endl << "\t------and found NO match in pfIsolation" << endl;
            }
          }
          //cout << "\t----Passed OUR isolation calc: " << passedOURisolation << endl;
          //if (passedOURisolation) cout << "\t------but not in pfIsolation" << endl;
   //     if (track.dz(t.vertex()) < .1) {
   //       cout << "\t----In PF iso calc (if IDed as ChHad), placed in ChHad" << endl;
   //     } else {
   //       cout << "\t----In PF iso calc (if IDed as ChHad), placed in PU" << endl;
   //     }
        }
      }


      if (noFakes && t.normalizedChi2 () > 20.0)
        continue;
      if (noFakes && t.hitPattern ().pixelLayersWithMeasurement () < 2)
        continue;
      if (noFakes && t.hitPattern ().trackerLayersWithMeasurement () < 5)
        continue;
      if (noFakes && fabs (t.d0 () / t.d0Error ()) > 5.0)
        continue;

      if (noPU && fabs(track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ()))
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
  }
  if (print) cout << "Total CandidateTrack Isolation: " << sumPt << endl << "-----------------------------" <<  endl;
    
  if (print){
    float sumPFPt = 0.0;
    bool found = false;
    //just print out the primary track for which we are getting the isolation
    //for(pat::PackedCandidateCollection::const_iterator pf_it0 = pc->begin(); pf_it0 != pc->end(); pf_it0++){
    for (auto &candidate0 : pc) {
      float dR0 = deltaR (track.eta(), track.phi(), candidate0.eta(), candidate0.phi());
      if (dR0 < 0.0001) {
        cout << "IsolatedTrack Head Track :: pt=" << candidate0.pt() << ", eta=" << candidate0.eta() << ", phi=" << candidate0.phi() << ", dR=" << dR0 << endl << "---------------------------" << endl;
        cout << "PF Candidates inside cone:" << endl;
        found = true;
        break;
      }
    } 
    if (!found) cout << "IsolatedTrack Head Track match to candidate/general head track not found::" << endl << "---------------------------" << endl;
    for (auto &candidate : pc) {
      float dZ = fabs(candidate.dz());
      float dR1 = deltaR(track.eta(), track.phi(), candidate.eta(), candidate.phi());
      float pt = candidate.p4().pt();
      if (dR1 > 0.0001 && dR1 < 0.3) {
        bool matchedAndIncluded = false;
        bool matched = false;
        for (const auto &t2 : tracks) {
          double dRMatch = deltaR (t2.eta(), t2.phi(), candidate.eta(), candidate.phi());
          if (dRMatch < 0.0001){
            matched = true;
            //int id = std::abs(candidate.pdgId());
            //bool matchIDIncluded = false;
            //if (id == 211 || id == 130 || id == 22) matchIDIncluded = true;
            //if (id == 211) matchIDIncluded = true;
            if (!(fabs(track.dz (t2.vertex ())) > 3.0 * hypot (track.dzError (), t2.dzError ()))) {
                matchedAndIncluded = true;
                break;
            }
          }
        }
        int id = std::abs(candidate.pdgId());
        if (id != 130 && id !=22) {
          if (!matchedAndIncluded) cout << "\tpf candidate w/ pt=" << candidate.pt() << ", eta=" << candidate.eta() << ", phi=" << candidate.phi() << ", dR=" << dR1 << endl;
          if (!matchedAndIncluded) cout << "\t-- dz=" << dZ << endl;
          if (!matchedAndIncluded && !matched) cout << "\t---NO matching generalTrack found" << endl;
        }
        //if (candidate.hasTrackDetails()){
        //  cout << "\t----Would have passed OUR isolation calc (dz<3sig): " << !(track.dz (candidate.vertex ()) > 3.0 * hypot (track.dzError (), candidate.dzError ())) << endl;
        //} else cout << "\t----dzError not available, OUR isolation calc = ??" << endl;
        if (id==211){
          if (dZ < 0.1) {
            if (!matchedAndIncluded) cout << "\t----In PF isolation in ChHad" << endl;
            sumPFPt += pt;
          } else {
            if (!matchedAndIncluded) cout << "\t----In PF isolation in puChHad" << endl;
            sumPFPt += pt;
          }
          if (!matchedAndIncluded && matched) cout << "\t------matched, but OUR isolation said NO" << endl;
        } else if (id==130) {}//cout << "\t----In PF isolation  in NuHad (not included)" << endl;
        else if (id==22) {}//cout << "\t----In PF isolation in Photon (not included)" << endl;
        else {
          if (!matchedAndIncluded) cout << "\t----NOT COUNTED IN PF ISOLATION (ID=" << id << ")" << endl;
        }
      }
    }
    if (print) cout << "Total IsolatedTrack PFIsolation (ChHad + puChHad): " << sumPFPt << endl;
    if (print) cout << "==============================" << endl;
  }


  return sumPt;
}

  



const double
CandidateTrack::getTrackIsolationExtraInfo (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const bool noFakes, const double outerDeltaR, const double innerDeltaR, const pat::PackedCandidateCollection &pc) const
{
  double sumPt = 0.0;
  
  bool print = false;
  if (noPU && !noFakes && outerDeltaR==0.3) print=true;
  if (print) cout << endl << "==============================" << endl << "CandidateTrack Head Track :: pt=" << track.pt() << ", eta=" << track.eta() << ", phi=" << track.phi() << endl << "---------------------------" << endl;
  if (print) cout << "Tracks inside cone:" << endl;

  for (const auto &t : tracks) {
      double dR0 = deltaR (track, t);
      if (print && dR0 < outerDeltaR && dR0 > innerDeltaR){
        cout << "\tTrack w/ pt=" << t.pt() << ", eta=" << t.eta() << ", phi=" << t.phi() << ", dR=" << dR0 << endl;
        cout << "\t-- dz=" << track.dz (t.vertex()) << ", 3sigZ=" << 3.0 * hypot (track.dzError (), t.dzError ()) << endl;
        cout << "\t----Passed OUR isolation calc: " << !(fabs(track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ())) << endl;
        if (track.dz(t.vertex()) < .1) {
          cout << "\t----In PF iso calc (if IDed as ChHad), placed in ChHad" << endl;
        } else {
          cout << "\t----In PF iso calc (if IDed as ChHad), placed in PU" << endl;
        }
      }


      if (noFakes && t.normalizedChi2 () > 20.0)
        continue;
      if (noFakes && t.hitPattern ().pixelLayersWithMeasurement () < 2)
        continue;
      if (noFakes && t.hitPattern ().trackerLayersWithMeasurement () < 5)
        continue;
      if (noFakes && fabs (t.d0 () / t.d0Error ()) > 5.0)
        continue;

      if (noPU && fabs(track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ()))
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
  }
  if (print) cout << "Total CandidateTrack Isolation: " << sumPt << endl << "-----------------------------" <<  endl;
    
  if (print){
    float sumPFPt = 0.0;
    //just print out the primary track for which we are getting the isolation
    //for(pat::PackedCandidateCollection::const_iterator pf_it0 = pc->begin(); pf_it0 != pc->end(); pf_it0++){
    for (auto &candidate0 : pc) {
      float dR0 = deltaR (track.eta(), track.phi(), candidate0.eta(), candidate0.phi());
      if (dR0 < 0.0001) {
        cout << "IsolatedTrack Head Track :: pt=" << candidate0.pt() << ", eta=" << candidate0.eta() << ", phi=" << candidate0.phi() << ", dR=" << dR0 << endl << "---------------------------" << endl;
        cout << "Tracks inside cone:" << endl;
        break;
      }
    } 
    //for(pat::PackedCandidateCollection::const_iterator pf_it = pc->begin(); pf_it != pc->end(); pf_it++){
    for (auto &candidate : pc) {
      float dZ = fabs(candidate.dz());
      //double dR1 = deltaR(pf_main->p4(), pf_it->p4())
      float dR1 = deltaR(track.eta(), track.phi(), candidate.eta(), candidate.phi());
      float pt = candidate.p4().pt();
      if (dR1 > 0.0001 && dR1 < 0.3) {
        cout << "\tTrack w/ pt=" << candidate.pt() << ", eta=" << candidate.eta() << ", phi=" << candidate.phi() << ", dR=" << dR1 << endl;
        cout << "\t-- dz=" << dZ << endl;
        if (candidate.hasTrackDetails()){
          cout << "\t----Would have passed OUR isolation calc (dz<3sig): " << !(track.dz (candidate.vertex ()) > 3.0 * hypot (track.dzError (), candidate.dzError ())) << endl;
        } else cout << "\t----dzError not available, OUR isolation calc = ??" << endl;
        int id = std::abs(candidate.pdgId());
        if (id==211){
          if (dZ < 0.1) {
            cout << "\t----In PF isolation in ChHad" << endl;
            sumPFPt += pt;
          } else {
            cout << "\t----In PF isolation in puChHad" << endl;
            sumPFPt += pt;
          }
        } else if (id==130) cout << "\t----In PF isolation  in NuHad" << endl;
        else if (id==22) cout << "\t----In PF isolation in Photon" << endl;
        else cout << "\t----NOT COUNTED IN PF ISOLATION (ID=" << id << ")" << endl;
      }
    }
     cout << "Total IsolatedTrack PFIsolation (ChHad + puChHad): " << sumPFPt << endl;
    cout << "==============================" << endl;
  }


  return sumPt;
}

const double
CandidateTrack::getTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const bool noFakes, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;
  
  bool print = false;
  //if (noPU && !noFakes && outerDeltaR==0.3) print=true;
  if (print) cout << endl << "==============================" << endl << "Head Track :: pt=" << track.pt() << ", eta=" << track.eta() << ", phi=" << track.phi() << endl << "---------------------------" << endl;
  if (print) cout << "Tracks inside cone:" << endl;

  for (const auto &t : tracks)
    {
      double dR0 = deltaR (track, t);
      if (print && dR0 < outerDeltaR && dR0 > innerDeltaR){
        cout << "\tTrack w/ pt=" << t.pt() << ", eta=" << t.eta() << ", phi=" << t.phi() << ", dR=" << dR0 << endl;
        cout << "\t-- dz=" << track.dz (t.vertex()) << ", 3sigZ=" << 3.0 * hypot (track.dzError (), t.dzError ()) << endl;
        cout << "\t----Passed OUR isolation calc: " << !(track.dz (t.vertex ()) > 3.0 * hypot (track.dzError (), t.dzError ())) << endl;
        if (track.dz(t.vertex()) < .1) {
          cout << "\t----In PF iso calc (if IDed as ChHad), placed in ChHad" << endl;
        } else {
          cout << "\t----In PF iso calc (if IDed as ChHad), placed in PU" << endl;
        }
      }


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
    if (print) cout << "Total CandidateTrack Isolation: " << sumPt << endl << "-----------------------------" <<  endl;


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
