#include "TLorentzVector.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisappTrks/CandidateTrackProducer/plugins/TagProbeFilter.h"

template<Flavor T>
TagProbeFilter<T>::TagProbeFilter (const edm::ParameterSet& iConfig) :
  triggers_   (iConfig.getParameter<edm::InputTag> ("triggers")),
  trigObjs_   (iConfig.getParameter<edm::InputTag> ("triggerObjects")),
  vertices_   (iConfig.getParameter<edm::InputTag> ("vertices")),
  met_        (iConfig.getParameter<edm::InputTag> ("met")),
  electrons_  (iConfig.getParameter<edm::InputTag> ("electrons")),
  muons_      (iConfig.getParameter<edm::InputTag> ("muons")),
  tracks_     (iConfig.getParameter<edm::InputTag> ("tracks")),
  triggerNames_     (iConfig.getParameter<vector<string> > ("triggerNames")),
  dataTakingPeriod_ (iConfig.getParameter<string> ("dataTakingPeriod"))
{
  assert(dataTakingPeriod_ == "2017" || dataTakingPeriod_ == "2018");

  is2017_ = (dataTakingPeriod_ == "2017");

  triggersToken_  = consumes<edm::TriggerResults> (triggers_);
  trigObjsToken_  = consumes<vector<pat::TriggerObjectStandAlone> > (trigObjs_);
  metToken_       = consumes<vector<pat::MET> > (met_);
  verticesToken_  = consumes<vector<reco::Vertex> > (vertices_);
  electronsToken_ = consumes<vector<pat::Electron> > (electrons_);
  muonsToken_     = consumes<vector<pat::Muon> > (muons_);
  tracksToken_    = consumes<vector<reco::Track> > (tracks_);
}

template<Flavor T>
TagProbeFilter<T>::~TagProbeFilter ()
{
}

template<Flavor T> bool
TagProbeFilter<T>::filter (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<edm::TriggerResults> triggers;
  event.getByToken (triggersToken_, triggers);

  edm::Handle<vector<pat::TriggerObjectStandAlone> > trigObjs;
  event.getByToken (trigObjsToken_, trigObjs);

  edm::Handle<vector<pat::MET> > met;
  event.getByToken (metToken_, met);

  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken (verticesToken_, vertices);

  edm::Handle<vector<pat::Electron> > electrons;
  event.getByToken (electronsToken_, electrons);

  edm::Handle<vector<pat::Muon> > muons;
  event.getByToken (muonsToken_, muons);

  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken (tracksToken_, tracks);

  //////////////////////////////

  if(!passesTrigger (event, *triggers)) return false;

  vector<pat::Electron> tagElectrons;
  vector<pat::Muon> tagMuons;
  selectTags (event,
              *triggers,
              *trigObjs,
              vertices->at (0), 
              *electrons, *muons,
              tagElectrons, tagMuons);
  if (tagElectrons.size() == 0 && tagMuons.size() == 0) return false;

  vector<reco::Track> probeTracks;
  selectProbes (vertices->at (0), *tracks, probeTracks);
  if (probeTracks.size() == 0) return false;

  return filterDecision (tagElectrons, tagMuons, met->at (0), probeTracks);
}

template<Flavor T> bool
TagProbeFilter<T>::passesTrigger (const edm::Event &event, const edm::TriggerResults &triggers) const
{
  bool triggerDecision = triggerNames_.empty() ? true : false;
  const edm::TriggerNames &triggerNames = event.triggerNames (triggers);

  for (unsigned i = 0; i < triggerNames.size (); i++)
    {
      string name = triggerNames.triggerName (i);
      bool pass = triggers.accept (i);
      for (const auto &trigger : triggerNames_)
        {
          if (name.find (trigger) == 0)
            triggerDecision = triggerDecision || pass;
        }
    }

  return triggerDecision;
}

template<Flavor T> void
TagProbeFilter<T>::selectTags (const edm::Event &event,
                               const edm::TriggerResults &triggers,
                               const vector<pat::TriggerObjectStandAlone> &trigObjs,
                               const reco::Vertex &vertex,
                               const vector<pat::Electron> &electrons,
                               const vector<pat::Muon> &muons,
                               vector<pat::Electron> &tagElectrons,
                               vector<pat::Muon> &tagMuons)
{
  return;
}

template<> void
TagProbeFilter<ELECTRON>::selectTags (const edm::Event &event,
                                      const edm::TriggerResults &triggers,
                                      const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                      const reco::Vertex &vertex,
                                      const vector<pat::Electron> &electrons,
                                      const vector<pat::Muon> &muons,
                                      vector<pat::Electron> &tagElectrons,
                                      vector<pat::Muon> &tagMuons)
{
  for(const auto &electron : electrons) {
    if(electron.pt() <= (is2017_ ? 35 : 32)) continue;

    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           electron,
                                           trigObjs,
                                           "hltEgammaCandidates::HLT", 
                                           (is2017_ ? "hltEle35noerWPTightGsfTrackIsoFilter" : "hltEle32WPTightGsfTrackIsoFilter"))) {
      continue; // cutElectronMatchToTrigObj
    }

    if(fabs(electron.eta()) >= 2.1) continue;
    if(!electron.electronID(is2017_ ? "cutBasedElectronID-Fall17-94X-V1-tight" : "cutBasedElectronID-Fall17-94X-V2-tight")) continue;
    
    if(fabs(electron.superCluster()->eta()) <= 1.479) {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.05) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.10) continue;
    }
    else {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.10) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.20) continue;
    }

    tagElectrons.push_back(electron);
  }
}

template<> void
TagProbeFilter<MUON>::selectTags (const edm::Event &event,
                                  const edm::TriggerResults &triggers,
                                  const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                  const reco::Vertex &vertex,
                                  const vector<pat::Electron> &electrons,
                                  const vector<pat::Muon> &muons,
                                  vector<pat::Electron> &tagElectrons,
                                  vector<pat::Muon> &tagMuons)
{
  for(const auto &muon : muons) {
    if(muon.pt() <= (is2017_ ? 29 : 26)) continue;
    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           muon,
                                           trigObjs,
                                           (is2017_ ? "hltIterL3MuonCandidates::HLT" : "hltL3MuonCandidates::HLT"),
                                           (is2017_ ? "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07" : "hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09"))) {
      continue; // cutMuonMatchToTrigObj
    }
    if(fabs(muon.eta()) >= 2.1) continue;
    if(!muon.isTightMuon(vertex)) continue;

    double muIso = muon.pfIsolationR04().sumChargedHadronPt;
    muIso += max(0.0, muon.pfIsolationR04().sumNeutralHadronEt + muon.pfIsolationR04().sumPhotonEt - 0.5 * muon.pfIsolationR04().sumPUPt);
    if(muIso / muon.pt() >= 0.15) continue;

    tagMuons.push_back(muon);
  }
}

template<> void
TagProbeFilter<TAUTOELECTRON>::selectTags (const edm::Event &event,
                                           const edm::TriggerResults &triggers,
                                           const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                           const reco::Vertex &vertex,
                                           const vector<pat::Electron> &electrons,
                                           const vector<pat::Muon> &muons,
                                           vector<pat::Electron> &tagElectrons,
                                           vector<pat::Muon> &tagMuons)
{
  for(const auto &electron : electrons) {
    if(electron.pt() <= (is2017_ ? 35 : 32)) continue;
    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           electron,
                                           trigObjs,
                                           "hltEgammaCandidates::HLT", 
                                           (is2017_ ? "hltEle35noerWPTightGsfTrackIsoFilter" : "hltEle32WPTightGsfTrackIsoFilter"))) {
      continue; // cutElectronMatchToTrigObj
    }
    if(fabs(electron.eta()) >= 2.1) continue;
    if(!electron.electronID(is2017_ ? "cutBasedElectronID-Fall17-94X-V1-tight" : "cutBasedElectronID-Fall17-94X-V2-tight")) continue;
    
    if(fabs(electron.superCluster()->eta()) <= 1.479) {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.05) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.10) continue;
    }
    else {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.10) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.20) continue;
    }

    tagElectrons.push_back(electron);
  }
}

template<> void
TagProbeFilter<TAUTOMUON>::selectTags (const edm::Event &event,
                                       const edm::TriggerResults &triggers,
                                       const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                       const reco::Vertex &vertex,
                                       const vector<pat::Electron> &electrons,
                                       const vector<pat::Muon> &muons,
                                       vector<pat::Electron> &tagElectrons,
                                       vector<pat::Muon> &tagMuons)
{
  for(const auto &muon : muons) {
    if(muon.pt() <= (is2017_ ? 29 : 26)) continue;
    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           muon,
                                           trigObjs,
                                           (is2017_ ? "hltIterL3MuonCandidates::HLT" : "hltL3MuonCandidates::HLT"),
                                           (is2017_ ? "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07" : "hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09"))) {
      continue; // cutMuonMatchToTrigObj
    }
    if(fabs(muon.eta()) >= 2.1) continue;
    if(!muon.isTightMuon(vertex)) continue;

    double muIso = muon.pfIsolationR04().sumChargedHadronPt;
    muIso += max(0.0, muon.pfIsolationR04().sumNeutralHadronEt + muon.pfIsolationR04().sumPhotonEt - 0.5 * muon.pfIsolationR04().sumPUPt);
    if(muIso / muon.pt() >= 0.15) continue;

    tagMuons.push_back(muon);
  }
}

template<Flavor T> void
TagProbeFilter<T>::selectProbes (const reco::Vertex &vertex,
                                 const vector<reco::Track> &tracks,
                                 vector<reco::Track> &probeTracks)
{
  for(const auto &track : tracks) {

    if(track.pt() <= 30) continue; // cutTrkPt30
    if(fabs(track.eta()) >= 2.1) continue; // cutTrkEta

    // cutTrkEcalGapVeto
    // cutTrkEtaMuonIneff1
    // cutTrkEtaMuonIneff2
    // cutTrkTOBCrack

    // cutTrk2017LowEfficiencyRegion

    // cutTrkFiducialElectron
    // cutTrkFiducialMuon
    // cutTrkFiducialECAL

    if(track.hitPattern().numberOfValidPixelHits() < 4) continue; // cutTrkNValidPixelHitsSignal
    if(track.hitPattern().numberOfValidHits() < 4) continue; // cutTrkNValidHitsSignal
    if(track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) != 0) continue; // cutTrkNMissIn
    if(track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) != 0) continue; // cutTrkNMissMid
    if(getTrackIsolation(track, tracks, true, false, 0.3) / track.pt() < 0.05) continue; // cutTrkIso

    double trackD0WRTPV = ((track.vx() - vertex.x()) * track.py() - (track.vy() - vertex.y()) * track.px()) / track.pt();
    if(fabs(trackD0WRTPV) >= 0.02) continue;

    double trackDZWRTPV = (track.vz() - vertex.z()) - ((track.vx() - vertex.x()) * track.px() + (track.vy() - vertex.y()) * track.py()) / track.pt() * track.pz() / track.pt();
    if(fabs(trackDZWRTPV) >= 0.5) continue;

    // dRMinJet

    probeTracks.push_back(track);
  }
}

template<Flavor T> bool
TagProbeFilter<T>::filterDecision(const vector<pat::Electron> tagElectrons,
                                  const vector<pat::Muon> tagMuons,
                                  const pat::MET &met,
                                  const vector<reco::Track> probeTracks) const
{
  return true;
}

template<> bool
TagProbeFilter<ELECTRON>::filterDecision(const vector<pat::Electron> tagElectrons,
                                         const vector<pat::Muon> tagMuons,
                                         const pat::MET &met,
                                         const vector<reco::Track> probeTracks) const
{
  // cutTrkMuonVeto
  // cutTrkTauHadVeto

  for(const auto &electron : tagElectrons) {
    TLorentzVector t(electron.px(), electron.py(), electron.pz(), electron.energy());
    for(const auto &track : probeTracks) {
      TLorentzVector p(track.px(), 
                       track.py(), 
                       track.pz(), 
                       sqrt(track.px() * track.px() + 
                            track.py() * track.py() + 
                            track.pz() * track.pz() + 
                            0.000510998928 * 0.000510998928));

      if(fabs((t + p).M() - 91.1876) >= 10.0) continue; // cutEleTrkInvMass80To100
      if(electron.charge() * track.charge() >= 0) continue; // cutEleTrkOS

      return true;
    }
  }

  return false;
}

template<> bool
TagProbeFilter<MUON>::filterDecision(const vector<pat::Electron> tagElectrons,
                                     const vector<pat::Muon> tagMuons,
                                     const pat::MET &met,
                                     const vector<reco::Track> probeTracks) const
{
  // cutTrkMuonVeto
  // cutTrkTauHadVeto
  // cutTrkEcalo

  for(const auto &muon : tagMuons) {
    TLorentzVector t(muon.px(), muon.py(), muon.pz(), muon.energy());
    for(const auto &track : probeTracks) {
      TLorentzVector p(track.px(), 
                       track.py(), 
                       track.pz(), 
                       sqrt(track.px() * track.px() + 
                            track.py() * track.py() + 
                            track.pz() * track.pz() + 
                            0.1056583715 * 0.1056583715));

      if(fabs((t + p).M() - 91.1876) >= 10.0) continue; // cutEleTrkInvMass80To100
      if(muon.charge() * track.charge() >= 0) continue; // cutEleTrkOS

      return true;
    }
  }

  return false;
}

template<> bool
TagProbeFilter<TAUTOELECTRON>::filterDecision(const vector<pat::Electron> tagElectrons,
                                              const vector<pat::Muon> tagMuons,
                                              const pat::MET &met,
                                              const vector<reco::Track> probeTracks) const
{
  // cutTrkMuonVeto
  // cutTrkTauHadVeto

  for(const auto &electron : tagElectrons) {
    TLorentzVector t(electron.px(), electron.py(), electron.pz(), electron.energy());
    for(const auto &track : probeTracks) {

      double dPhi = deltaPhi(electron.phi(), track.phi());
      if(sqrt(2.0 * electron.pt() * track.pt() * (1 - cos(dPhi))) >= 40) continue; // cutElectronLowMT

      TLorentzVector p(track.px(), 
                       track.py(), 
                       track.pz(), 
                       sqrt(track.px() * track.px() + 
                            track.py() * track.py() + 
                            track.pz() * track.pz() + 
                            0.000510998928 * 0.000510998928));

      double invMass = (t + p).M();
      if(invMass <= 91.1876 - 50 || invMass >= 91.1876 - 15) continue; // cutEleTrkInvMass40To75
      if(electron.charge() * track.charge() >= 0) continue; // cutEleTrkOS

      return true;
    }
  }

  return false;
}

template<> bool
TagProbeFilter<TAUTOMUON>::filterDecision(const vector<pat::Electron> tagElectrons,
                                          const vector<pat::Muon> tagMuons,
                                          const pat::MET &met,
                                          const vector<reco::Track> probeTracks) const
{
  // cutTrkElecVeto
  // cutTrkTauHadVeto

  for(const auto &muon : tagMuons) {
    TLorentzVector t(muon.px(), muon.py(), muon.pz(), muon.energy());
    for(const auto &track : probeTracks) {

      double dPhi = deltaPhi(muon.phi(), track.phi());
      if(sqrt(2.0 * muon.pt() * track.pt() * (1 - cos(dPhi))) >= 40) continue; // cutMuonLowMT

      TLorentzVector p(track.px(), 
                       track.py(), 
                       track.pz(), 
                       sqrt(track.px() * track.px() + 
                            track.py() * track.py() + 
                            track.pz() * track.pz() + 
                            0.1056583715 * 0.1056583715));

      double invMass = (t + p).M();
      if(invMass <= 91.1876 - 50 || invMass >= 91.1876 - 15) continue; // cutMuTrkInvMass40To75
      if(muon.charge() * track.charge() >= 0) continue; // cutMuTrkOS

      return true;
    }
  }

  return false;
}

template<Flavor T> const double
TagProbeFilter<T>::getTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const bool noFakes, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      if (noFakes && t.normalizedChi2 () > 20.0) continue;
      if (noFakes && t.hitPattern ().pixelLayersWithMeasurement () < 2) continue;
      if (noFakes && t.hitPattern ().trackerLayersWithMeasurement () < 5) continue;
      if (noFakes && fabs (t.d0 () / t.d0Error ()) > 5.0) continue;

      if (noPU && fabs( track.dz (t.vertex ())) > 3.0 * hypot (track.dzError (), t.dzError ())) continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR) sumPt += t.pt ();
    }

  return sumPt;
}

typedef TagProbeFilter<ELECTRON>      ElectronTagProbeFilter;
typedef TagProbeFilter<MUON>          MuonTagProbeFilter;
typedef TagProbeFilter<TAUTOELECTRON> TauToElectronTagProbeFilter;
typedef TagProbeFilter<TAUTOMUON>     TauToMuonTagProbeFilter;

DEFINE_FWK_MODULE (ElectronTagProbeFilter);
DEFINE_FWK_MODULE (MuonTagProbeFilter);
DEFINE_FWK_MODULE (TauToElectronTagProbeFilter);
DEFINE_FWK_MODULE (TauToMuonTagProbeFilter);
