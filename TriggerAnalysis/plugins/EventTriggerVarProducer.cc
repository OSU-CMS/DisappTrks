#include "EventTriggerVarProducer.h"

EventTriggerVarProducer::EventTriggerVarProducer(const edm::ParameterSet &cfg) : EventVariableProducer(cfg) {
  tokenJets_        = consumes<vector<TYPE(jets)> >(collections_.getParameter<edm::InputTag>("jets"));
  tokenTracks_      = consumes<vector<TYPE(tracks)> >(collections_.getParameter<edm::InputTag>("tracks"));
  tokenMuons_       = consumes<vector<pat::Muon> >(collections_.getParameter<edm::InputTag>("muons"));
  tokenVertices_    = consumes<vector<reco::Vertex> >(collections_.getParameter<edm::InputTag>("primaryvertexs"));
  tokenTriggerBits_ = consumes<edm::TriggerResults>(collections_.getParameter<edm::InputTag>("triggers"));
  tokenTriggerObjs_ = consumes<vector<pat::TriggerObjectStandAlone> >(collections_.getParameter<edm::InputTag>("trigobjs"));
  tokenGenParticles_ = consumes<vector<reco::GenParticle> >(collections_.getParameter<edm::InputTag>("mcparticles"));
}

void EventTriggerVarProducer::AddVariables(const edm::Event &event) {

  // Leading jet eta
  // first jet is always leading jet (https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/PhysicsTools/PatAlgos/plugins/PATJetProducer.cc#L406)

  edm::Handle<vector<TYPE(jets)> > jets;
  if(!event.getByToken(tokenJets_, jets)) {
    clog << "ERROR:  Could not find jets collection." << endl;
    return;
  }

  double etaJetLeading = jets->size() ? jets->at(0).eta() : -999.;

  // Pass HLT_MET75_IsoTrk50_v

  edm::Handle<edm::TriggerResults> triggerBits;
  if(!event.getByToken(tokenTriggerBits_, triggerBits)) {
    clog << "ERROR:  Could not find triggerBits collection." << endl;
    return;
  }
  const edm::TriggerNames &triggerNames = event.triggerNames(*triggerBits);

  bool passesMainTrigger = false;
  for(unsigned i = 0; i < triggerNames.size(); i++) {
      string name = triggerNames.triggerName(i);
      if(name.find("HLT_MET75_IsoTrk50_v") == 0) passesMainTrigger |= triggerBits->accept(i);
  }

  // Pass hltMET75
  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByToken(tokenTriggerObjs_, triggerObjs);

  bool passesTriggerFilter = false;
  for(auto triggerObj : *triggerObjs) {
    triggerObj.unpackPathNames(triggerNames);
    for(const auto &filterLabel : triggerObj.filterLabels()) {
      if(filterLabel == "hltMET75") {
        passesTriggerFilter = true;
        break;
      }
    }
    if(passesTriggerFilter) break;
  }

  // Match to HLT track

  edm::Handle<vector<TYPE(tracks)> > tracks;
  bool hasTracks = event.getByToken(tokenTracks_, tracks);

  edm::Handle<vector<TYPE(muons)> > muons;
  event.getByToken(tokenMuons_, muons);

  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken(tokenVertices_, vertices);
  const reco::Vertex &pv = vertices->at(0);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  bool isMC = event.getByToken(tokenGenParticles_, genParticles);

  const pat::TriggerObjectStandAlone &isoTrk = getHLTObj(triggerNames, *triggerObjs, "hltTrk50Filter");

  bool anyTrackMatchToHLTTrack = false;
  vector<const TYPE(tracks)*> selectedTracks;
  if(hasTracks) {
    for(const auto &track : *tracks) {
        bool goodTrack = isMC ? isGoodTrack(track, pv, *tracks, *genParticles) : isGoodTrack(track, pv, *tracks);
        if(!goodTrack) continue;
        selectedTracks.push_back (&track);
        if(deltaR(track, isoTrk) < 0.1) anyTrackMatchToHLTTrack = true;
      }
      sort(selectedTracks.begin(),
           selectedTracks.end(),
           [](const TYPE(tracks) *a, const TYPE(tracks) *b) -> bool { return (a->pt() > b->pt()); });
  }

  bool anyMuonMatchToHLTTrack = false;
  vector<const pat::Muon*> selectedMuons;
  for(const auto &muon : *muons) {
    bool goodMuon = isGoodMuon(muon, pv, *muons);
    if(!goodMuon) continue;
    selectedMuons.push_back(&muon);
    if(deltaR(muon, isoTrk) < 0.1) anyMuonMatchToHLTTrack = true;
  }
  sort(selectedMuons.begin(),
       selectedMuons.end(),
       [](const pat::Muon *a, const pat::Muon *b) -> bool { return (a->pt() > b->pt()); });

   bool leadTrackMatchToHLTTrack = hasTracks ? (selectedTracks.size() > 0 && deltaR(*selectedTracks.at(0), isoTrk) < 0.1) : false;
   bool leadMuonMatchToHLTTrack  = (selectedMuons.size() > 0 && deltaR(*selectedMuons.at(0), isoTrk) < 0.1);

  // Insert event variables

  (*eventvariables)["etaJetLeading"] = etaJetLeading;
  (*eventvariables)["passesMainTrigger"] = passesMainTrigger;
  (*eventvariables)["passesTriggerFilter"] = passesTriggerFilter;

  (*eventvariables)["leadTrackMatchToHLTTrack"] = leadTrackMatchToHLTTrack;
  (*eventvariables)["anyTrackMatchToHLTTrack"] = anyTrackMatchToHLTTrack;

  (*eventvariables)["leadMuonMatchToHLTTrack"] = leadMuonMatchToHLTTrack;
  (*eventvariables)["anyMuonMatchToHLTTrack"] = anyMuonMatchToHLTTrack;

}

bool EventTriggerVarProducer::genMatched(const TYPE(tracks) &track,
                                         const vector<reco::GenParticle> &genParticles,
                                         const int pdgId,
                                         const int status,
                                         const double maxDeltaR) const {
  for(const auto &genParticle : genParticles) {
      if(abs(genParticle.pdgId()) != abs (pdgId)) continue;
      if(genParticle.status() != status) break;
      if(deltaR(track, genParticle) > maxDeltaR) continue;
      return true;
    }
  return false;
}

bool EventTriggerVarProducer::genMatched(const pat::Muon &muon,
                                         const vector<reco::GenParticle> &genParticles,
                                         const int pdgId,
                                         const int status,
                                         const double maxDeltaR) const {
  for(const auto &genParticle : genParticles) {
      if(abs(genParticle.pdgId()) != abs (pdgId)) continue;
      if(genParticle.status() != status) break;
      if(deltaR(muon, genParticle) > maxDeltaR) continue;
      return true;
    }
  return false;
}

const pat::TriggerObjectStandAlone & EventTriggerVarProducer::getHLTObj(const edm::TriggerNames &triggerNames,
                                                                        const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                                                        const string &collection) const {
  unsigned i = 0, leadingIndex = 0;
  double leadingPt = -1.0;
  for(auto triggerObj : triggerObjs) {
      triggerObj.unpackPathNames(triggerNames);
      if(triggerObj.collection() == (collection + "::HLT")) {
          if(triggerObj.pt() > leadingPt) {
              leadingIndex = i;
              leadingPt = triggerObj.pt ();
            }
        }
      i++;
    }

  return triggerObjs.at(leadingIndex);
}

bool EventTriggerVarProducer::isGoodTrack(const TYPE(tracks) &track,
                                          const reco::Vertex &pv,
                                          const vector<TYPE(tracks)> &tracks,
                                          const vector<reco::GenParticle> &genParticles) const {

  return (isGoodTrack(track, pv, tracks) &&
          (genParticles.size() == 0 || genMatched(track, genParticles, 1000024, 3, 0.1)));

}

bool EventTriggerVarProducer::isGoodTrack(const TYPE(tracks) &track,
                                          const reco::Vertex &pv,
                                          const vector<TYPE(tracks)> &tracks) const {
  if(fabs(track.eta()) < 2.5 &&
     track.normalizedChi2() < 10.0 &&
     fabs(track.dxy(pv.position())) < 0.2 &&
     fabs(track.dz(pv.position())) < 0.5 &&
     track.hitPattern().numberOfValidPixelHits() >= 1 &&
     track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
     track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
     track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
     track.trackIsoNoPUDRp3() / track.pt() < 0.01) {
       return true;
     }

     return false;
}

bool EventTriggerVarProducer::isGoodMuon(const pat::Muon &muon,
                                         const reco::Vertex &pv,
                                         const vector<pat::Muon> &muons) const {

  double muonIso = muon.pfIsolationR04().sumChargedHadronPt;
  muonIso += max(0., muon.pfIsolationR04().sumNeutralHadronEt +
                     muon.pfIsolationR04().sumPhotonEt -
                     0.5 * muon.pfIsolationR04().sumPUPt);

  if(fabs(muon.eta()) < 2.1 &&
     muon.pt() > 25.0 &&
     muon.isGlobalMuon() &&
     muon.isPFMuon() &&
     muon.globalTrack()->normalizedChi2() < 10.0 &&
     muon.globalTrack()->hitPattern().numberOfValidMuonHits() > 0 &&
     muon.numberOfMatchedStations() > 1 &&
     fabs(muon.muonBestTrack()->dxy(pv.position())) < 0.2 &&
     fabs(muon.muonBestTrack()->dz(pv.position())) < 0.5 &&
     muon.innerTrack()->hitPattern().numberOfValidPixelHits() > 0 &&
     muon.innerTrack()->hitPattern().trackerLayersWithMeasurement() > 5 &&
     muon.innerTrack()->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
     muon.innerTrack()->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
     muonIso / muon.pt() < 0.15) {
       return true;
     }

   return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventTriggerVarProducer);
