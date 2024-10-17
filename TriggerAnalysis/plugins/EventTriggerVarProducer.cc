#include "EventTriggerVarProducer.h"

EventTriggerVarProducer::EventTriggerVarProducer(const edm::ParameterSet &cfg) : EventVariableProducer(cfg) {
  tokenJets_         = consumes<vector<TYPE(jets)> >(collections_.getParameter<edm::InputTag>("jets"));
  tokenTracks_       = consumes<vector<TYPE(tracks)> >(collections_.getParameter<edm::InputTag>("tracks"));
  tokenMuons_        = consumes<vector<pat::Muon> >(collections_.getParameter<edm::InputTag>("muons"));
  tokenVertices_     = consumes<vector<reco::Vertex> >(collections_.getParameter<edm::InputTag>("primaryvertexs"));
  tokenTriggerBits_  = consumes<edm::TriggerResults>(collections_.getParameter<edm::InputTag>("triggers"));
  tokenTriggerObjs_  = consumes<vector<pat::TriggerObjectStandAlone> >(collections_.getParameter<edm::InputTag>("trigobjs"));
  tokenGenParticles_ = consumes<vector<reco::GenParticle> >(collections_.getParameter<edm::InputTag>("mcparticles"));

  triggerNames = cfg.getParameter<vector<string> >("triggerNames");
  filterNames  = cfg.getParameter<vector<string> >("filterNames");

  signalTriggerNames = cfg.getParameter<vector<string> >("signalTriggerNames");
}

void EventTriggerVarProducer::AddVariables(const edm::Event &event, const edm::EventSetup &setup) {

  //////////////////////////////////////////////////////////////////////////////
  // Leading jet eta
  // first jet is always leading jet (https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/PhysicsTools/PatAlgos/plugins/PATJetProducer.cc#L406)
  //////////////////////////////////////////////////////////////////////////////

  edm::Handle<vector<TYPE(jets)> > jets;
  if(!event.getByToken(tokenJets_, jets)) {
    clog << "ERROR:  Could not find jets collection." << endl;
    return;
  }

  double etaJetLeading = jets->empty() ? -999. : jets->at(0).eta();

  //////////////////////////////////////////////////////////////////////////////
  // Passes individual triggers
  //////////////////////////////////////////////////////////////////////////////

  edm::Handle<edm::TriggerResults> triggerBits;
  if(!event.getByToken(tokenTriggerBits_, triggerBits)) {
    clog << "ERROR:  Could not find triggerBits collection." << endl;
    return;
  }
  const edm::TriggerNames &allTriggerNames = event.triggerNames(*triggerBits);

  for(auto name : triggerNames) triggerFires[name] = false;

  for(unsigned i = 0; i < allTriggerNames.size(); i++) {
      string thisName = allTriggerNames.triggerName(i);
      for(auto name : triggerNames) {
        if(thisName.find(name) == 0) {
          triggerFires[name] |= triggerBits->accept(i);
          break;
        }
      }
  }

  //////////////////////////////////////////////////////////////////////////////
  // Pass individual trigger filters
  //////////////////////////////////////////////////////////////////////////////


  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByToken(tokenTriggerObjs_, triggerObjs);

  for(auto name : filterNames) filterFires[name] = false;

  for(auto triggerObj : *triggerObjs) {
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, *triggerBits);
#else
    triggerObj.unpackPathNames(allTriggerNames);
#endif
    for(const auto &thisFilterName : triggerObj.filterLabels()) {
      for(auto name : filterNames) {
        if(name == thisFilterName) {
          filterFires[thisFilterName] = true;
          break;
        }
      }
      if(filterFires[thisFilterName]) continue;
    }
  }

  //////////////////////////////////////////////////////////////////////////////
  // Passes the Grand Or of signal triggers
  //////////////////////////////////////////////////////////////////////////////

  signalGrandOrFires = false;
  signalGrandOrFiresWithoutIsoTrk = false;

  for(unsigned i = 0; i < allTriggerNames.size(); i++) {
    string thisName = allTriggerNames.triggerName(i);
    for(auto name : signalTriggerNames) {
      if(thisName.find(name) == 0 && triggerBits->accept(i)) {
        signalGrandOrFires = true;
        if(thisName.find("_IsoTrk50_v") == std::string::npos) {
          signalGrandOrFiresWithoutIsoTrk = true;
          break;
        }
      }
    }
    if(signalGrandOrFires && signalGrandOrFiresWithoutIsoTrk) break;
  }

  //////////////////////////////////////////////////////////////////////////////
  // Match to HLT track
  //////////////////////////////////////////////////////////////////////////////

  edm::Handle<vector<TYPE(tracks)> > tracks;
  bool hasTracks = event.getByToken(tokenTracks_, tracks);

  edm::Handle<vector<TYPE(muons)> > muons;
  event.getByToken(tokenMuons_, muons);

  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken(tokenVertices_, vertices);
  const reco::Vertex &pv = vertices->at(0);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  bool isMC = event.getByToken(tokenGenParticles_, genParticles);

  pat::TriggerObjectStandAlone isoTrk;
  bool passesHLTTrk50Filter = getHLTObj(event, *triggerObjs, *triggerBits, "hltTrk50Filter", isoTrk);

  bool anyTrackMatchToHLTTrack = false;
  vector<const TYPE(tracks)*> selectedTracks;
  if(hasTracks) {
    for(const auto &track : *tracks) {
        bool goodTrack = isMC ? isGoodTrack(track, pv, *tracks, *genParticles) : isGoodTrack(track, pv, *tracks);
        if(!goodTrack) continue;
        selectedTracks.push_back (&track);
        if(passesHLTTrk50Filter && deltaR(track, isoTrk) < 0.1) anyTrackMatchToHLTTrack = true;
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
    if(passesHLTTrk50Filter && deltaR(muon, isoTrk) < 0.1) anyMuonMatchToHLTTrack = true;
  }
  sort(selectedMuons.begin(),
       selectedMuons.end(),
       [](const pat::Muon *a, const pat::Muon *b) -> bool { return (a->pt() > b->pt()); });

   //bool leadTrackMatchToHLTTrack = (!selectedTracks.empty() > 0 &&
   //                                 passesHLTTrk50Filter &&
   //                                 deltaR(*selectedTracks.at(0), isoTrk) < 0.1);
   //bool leadMuonMatchToHLTTrack  = (!selectedMuons.empty() > 0 &&
   //                                 passesHLTTrk50Filter &&
   //                                 deltaR(*selectedMuons.at(0), isoTrk) < 0.1);

   bool leadTrackMatchToHLTTrack = (!selectedTracks.empty() > 0 &&
                                    passesHLTTrk50Filter &&
                                    matchedToHLTObj(event, *triggerObjs, *triggerBits, "hltTrk50Filter", *selectedTracks.at(0))
                                    );
   bool leadMuonMatchToHLTTrack = (!selectedMuons.empty() > 0 &&
                                    passesHLTTrk50Filter &&
                                    matchedToHLTObj(event, *triggerObjs, *triggerBits, "hltTrk50Filter", *selectedMuons.at(0))
                                    );
                    

  //////////////////////////////////////////////////////////////////////////////
  // Lead muon and track pt
  //////////////////////////////////////////////////////////////////////////////

  double leadMuonPt = selectedMuons.empty() ? -1.0 : selectedMuons.at(0)->pt();
  double leadTrackPt = selectedTracks.empty() ? -1.0 : selectedTracks.at(0)->pt();

  //////////////////////////////////////////////////////////////////////////////
  // Online MET
  //////////////////////////////////////////////////////////////////////////////

  pat::TriggerObjectStandAlone hltMet;
  pat::TriggerObjectStandAlone hltMetClean;
  pat::TriggerObjectStandAlone hltPFMet;

  getHLTObj(event, *triggerObjs, *triggerBits, "hltMet", hltMet);
  getHLTObj(event, *triggerObjs, *triggerBits, "hltMetClean", hltMetClean);
  getHLTObj(event, *triggerObjs, *triggerBits, "hltPFMet", hltPFMet);

  double onlineMet = hltMet.pt();
  double onlineMetClean = hltMetClean.pt();
  double onlinePFMet = hltPFMet.pt();

  //////////////////////////////////////////////////////////////////////////////
  // Insert event variables
  //////////////////////////////////////////////////////////////////////////////

  for(const auto& trig : triggerFires) {
    (*eventvariables)["fires_" + trig.first] = trig.second;
  }

  for(const auto& filt : filterFires) {
    (*eventvariables)["fires_" + filt.first] = filt.second;
  }

  (*eventvariables)["passesGrandOrTrigger"] = signalGrandOrFires;
  (*eventvariables)["passesGrandOrTriggerWithoutIsoTrk"] = signalGrandOrFiresWithoutIsoTrk;

  (*eventvariables)["etaJetLeading"] = etaJetLeading;

  (*eventvariables)["leadTrackMatchToHLTTrack"] = leadTrackMatchToHLTTrack;
  (*eventvariables)["anyTrackMatchToHLTTrack"] = anyTrackMatchToHLTTrack;

  (*eventvariables)["leadMuonMatchToHLTTrack"] = leadMuonMatchToHLTTrack;
  (*eventvariables)["anyMuonMatchToHLTTrack"] = anyMuonMatchToHLTTrack;

  (*eventvariables)["leadMuonPt"] = leadMuonPt;
  (*eventvariables)["leadTrackPt"] = leadTrackPt;

  (*eventvariables)["hltMet"] = onlineMet;
  (*eventvariables)["hltMetClean"] = onlineMetClean;
  (*eventvariables)["hltPFMet"] = onlinePFMet;

  (*eventvariables)["passesHLTTrk50Filter"] = passesHLTTrk50Filter;

  selectedTracks.clear();
  selectedMuons.clear();

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

bool EventTriggerVarProducer::getHLTObj(const edm::Event &event,
                                        const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                        const edm::TriggerResults &triggerBits,
                                        const string &collection,
                                        pat::TriggerObjectStandAlone &obj) const {

  // Finds the leading trigger object from "collection::HLT" and sets "obj" to it
  // Returns true if it found any "collection::HLT", and false if not

  double leadingPt = -1.0;

  for(auto triggerObj : triggerObjs) {

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, triggerBits);
#else
    triggerObj.unpackPathNames(event.triggerNames(triggerBits));
#endif

    if(triggerObj.collection() == (collection + "::HLT")) {
      if(triggerObj.pt() > leadingPt) {
        obj = triggerObj;
        leadingPt = obj.pt();
      }

    }
  }

  return (leadingPt > 0.0);
}

bool EventTriggerVarProducer::matchedToHLTObj(const edm::Event &event,
                                              const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                              const edm::TriggerResults &triggerBits,
                                              const string &collection,
                                              const pat::Muon &muon) const {
  double dR = -1.0;
  for(auto triggerObj : triggerObjs) {

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, triggerBits);
#else
    triggerObj.unpackPathNames(event.triggerNames(triggerBits));
#endif

    if(triggerObj.collection() == (collection + "::HLT") or triggerObj.collection() == (collection + "::RECO")) {
      if(deltaR(triggerObj, muon) < 0.1) {
        dR = deltaR(triggerObj, muon);
        break;
      }
    }
  }

  return (dR > 0.0);
}

bool EventTriggerVarProducer::matchedToHLTObj(const edm::Event &event,
                                              const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                              const edm::TriggerResults &triggerBits,
                                              const string &collection,
                                              const TYPE(tracks) &iso) const {
  double dR = -1.0;
  for(auto triggerObj : triggerObjs) {

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, triggerBits);
#else
    triggerObj.unpackPathNames(event.triggerNames(triggerBits));
#endif

    if(triggerObj.collection() == (collection + "::HLT") or triggerObj.collection() == (collection + "::RECO")) {
      if(deltaR(triggerObj, iso) < 0.1) {
        dR = deltaR(triggerObj, iso);
        break;
      }
    }
  }

  return (dR > 0.0);
}

bool EventTriggerVarProducer::isGoodTrack(const TYPE(tracks) &track,
                                          const reco::Vertex &pv,
                                          const vector<TYPE(tracks)> &tracks,
                                          const vector<reco::GenParticle> &genParticles) const {

  return (isGoodTrack(track, pv, tracks) &&
          (genParticles.empty() || genMatched(track, genParticles, 1000024, 3, 0.1)));

}

bool EventTriggerVarProducer::isGoodTrack(const TYPE(tracks) &track,
                                          const reco::Vertex &pv,
                                          const vector<TYPE(tracks)> &tracks) const {

#if DATA_FORMAT == MINI_AOD_2017
  bool result = (fabs(track.eta()) < 2.5 &&
                 track.isHighPurityTrack() && // bfrancis: is this what we want to do? replaces normalizedChi2 < 10.0
                 fabs(track.dxy()) < 0.2 &&
                 fabs(track.dz()) < 0.5 &&
                 track.hitPattern().numberOfValidPixelHits() >= 1 &&
                 track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                 track.pfIsolationDR03().chargedHadronIso() / track.pt() < 0.01); // replaces trackIsoNoPUDRp3/pt

#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM || DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM // Verification needed !
  bool result = (fabs(track.eta()) < 2.5 &&
                 track.isHighPurityTrack() && 
                 fabs(track.dxy()) < 0.2 &&
                 fabs(track.dz()) < 0.5 &&
                 track.hitPattern().numberOfValidPixelHits() >= 1 &&
                 track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                 track.pfIsolationDR03().chargedHadronIso() / track.pt() < 0.01);
#else
  bool result = (fabs(track.eta()) < 2.5 &&
                 track.normalizedChi2() < 10.0 &&
                 fabs(track.dxy(pv.position())) < 0.2 &&
                 fabs(track.dz(pv.position())) < 0.5 &&
                 track.hitPattern().numberOfValidPixelHits() >= 1 &&
                 track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
                 track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
                 track.trackIsoNoPUDRp3() / track.pt() < 0.01);
#endif

  return result;
}

bool EventTriggerVarProducer::isGoodMuon(const pat::Muon &muon,
                                         const reco::Vertex &pv,
                                         const vector<pat::Muon> &muons) const {

  double muonIso = muon.pfIsolationR04().sumChargedHadronPt;
  muonIso += max(0., muon.pfIsolationR04().sumNeutralHadronEt +
                     muon.pfIsolationR04().sumPhotonEt -
                     0.5 * muon.pfIsolationR04().sumPUPt);

  if(fabs(muon.eta()) < 2.1 &&
     muon.pt() > 26.0 &&
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
