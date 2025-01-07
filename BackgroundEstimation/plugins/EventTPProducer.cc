#include "DisappTrks/BackgroundEstimation/plugins/EventTPProducer.h"

#define M_Z (91.1876)

template<class T, class... Args>
EventTPProducer<T, Args...>::EventTPProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  doFilter_ (cfg.getParameter<bool> ("doFilter")),
  doLooseFilter_ (cfg.getParameter<bool> ("doLooseFilter")),
  doSSFilter_ (cfg.getParameter<bool> ("doSSFilter")),
  doLooseSSFilter_ (cfg.getParameter<bool> ("doLooseSSFilter")),
  doJetFilter_ (cfg.getParameter<bool> ("doJetFilter")),
  triggerCollectionName_ (cfg.getParameter<string> ("triggerCollectionName")),
  triggerFilterName_ (cfg.getParameter<string> ("triggerFilterName")),
  triggerMatchingDR_ (cfg.getParameter<double> ("triggerMatchingDR")),
  probeTagMatchingDR_ (cfg.getParameter<double> ("probeTagMatchingDR"))
{
  tokenTags_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));
  tokenProbes_ = consumes<vector<osu::Track> > (collections_.getParameter<edm::InputTag> ("tracks"));
  tokenJets_ = consumes<vector<pat::Jet> > (collections_.getParameter<edm::InputTag> ("jets"));
  tokenPFCands_ = consumes<vector<pat::PackedCandidate> > (collections_.getParameter<edm::InputTag> ("pfCandidates"));
  tokenTriggerBits_  = consumes<edm::TriggerResults>(collections_.getParameter<edm::InputTag>("triggers"));
  tokenTriggerObjs_  = consumes<vector<pat::TriggerObjectStandAlone> >(collections_.getParameter<edm::InputTag>("trigobjs"));
}

template<class T, class... Args>
EventTPProducer<T, Args...>::~EventTPProducer ()
{
}

template<class T, class... Args> void
EventTPProducer<T, Args...>::AddVariables (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<T> > tags;
  event.getByToken (tokenTags_, tags);

  edm::Handle<vector<osu::Track> > probes;
  event.getByToken (tokenProbes_, probes);

  if (!tags.isValid () || !probes.isValid ())
    return;

  edm::Handle<vector<pat::Jet> > jets;
  event.getByToken (tokenJets_, jets);

  edm::Handle<vector<pat::PackedCandidate> > pfCands;
  event.getByToken (tokenPFCands_, pfCands);

  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByToken(tokenTriggerObjs_, triggerObjs);

  edm::Handle<edm::TriggerResults> triggerBits;
  if(!event.getByToken(tokenTriggerBits_, triggerBits)) {
    clog << "ERROR:  Could not find triggerBits collection." << endl;
    return;
  }

  unsigned nGoodTPPairs = 0, 
           nProbesPassingVeto = 0, 
           nProbesPassingLooseVeto = 0, 
           nProbesFiringTrigger = 0,
           nProbesMatchingTag = 0,
           nProbesFiringTriggerMatchingTag = 0;
  unsigned nGoodSSTPPairs = 0, 
           nSSProbesPassingVeto = 0, 
           nSSProbesPassingLooseVeto = 0, 
           nSSProbesFiringTrigger = 0,
           nSSProbesMatchingTag = 0,
           nSSProbesFiringTriggerMatchingTag = 0;
  unsigned nGoodTagJetPairs = 0, nGoodTagPFCHPairs = 0;

  vector<double> masses,
                 tagJetMasses, jetChargedHadronEnergyFractions, jetNeutralHadronEnergyFractions,
                 tagPFCHMasses, pfchRelIsos;
  vector<int> chargeProducts;

  for (const auto &tag : *tags)
    {
      for (const auto &probe : *probes)
        {
          double mass = 0.0;
          bool isGoodInvMass = goodInvMass (tag, probe, mass),
               isGoodTPPair = isGoodInvMass && (tag.charge () * probe.charge () < 0.0),
               isGoodSSTPPair = isGoodInvMass && (tag.charge () * probe.charge () > 0.0),
               isProbePassingVeto = passesVeto (probe),
               isProbePassingLooseVeto = passesLooseVeto (probe),
               isProbeFiringTrigger = firesTrigger (event, *triggerObjs, *triggerBits, probe),
               isProbeAlsoTag = matchedToTag(probe, *tags);

          if(isGoodTPPair) {
            nGoodTPPairs++;
            if(isProbePassingVeto)      nProbesPassingVeto++;
            if(isProbePassingLooseVeto) nProbesPassingLooseVeto++;
            if(isProbeFiringTrigger)    nProbesFiringTrigger++;
            if(isProbeAlsoTag)          nProbesMatchingTag++;
            if(isProbeFiringTrigger && isProbeAlsoTag) nProbesFiringTriggerMatchingTag++;
          }

          if(isGoodSSTPPair) {
            nGoodSSTPPairs++;
            if(isProbePassingVeto)      nSSProbesPassingVeto++;
            if(isProbePassingLooseVeto) nSSProbesPassingLooseVeto++;
            if(isProbeFiringTrigger)    nSSProbesFiringTrigger++;
            if(isProbeAlsoTag)          nSSProbesMatchingTag++;
            if(isProbeFiringTrigger && isProbeAlsoTag) nSSProbesFiringTriggerMatchingTag++;
          }

          if (isGoodTPPair || isGoodSSTPPair)
            {
              masses.push_back (mass);
              chargeProducts.push_back (tag.charge () * probe.charge ());
            }
        }

      if (jets.isValid ())
        {
          for (const auto &probe : *jets)
            {
              double mass = 0.0,
                     hadronEnergyFraction = probe.chargedHadronEnergyFraction () + probe.neutralHadronEnergyFraction ();
              bool isGoodInvMass = goodInvMass (tag, probe, mass),
                   isGoodHadronEnergyFraction = (hadronEnergyFraction < 0.1),
                   isTightLepVeto = anatools::jetPassesTightLepVeto (probe),
                   isFiducial = (fabs (probe.eta ()) < 2.4),
                   isNotMatchedToMuon = !jetMatchedToMuon (probe, *pfCands);

              (isGoodInvMass && isGoodHadronEnergyFraction && isTightLepVeto && isFiducial && isNotMatchedToMuon) && nGoodTagJetPairs++;

              if (isGoodHadronEnergyFraction && isTightLepVeto && isFiducial && isNotMatchedToMuon)
                {
                  tagJetMasses.push_back (mass);
                  jetChargedHadronEnergyFractions.push_back (probe.chargedHadronEnergyFraction ());
                  jetNeutralHadronEnergyFractions.push_back (probe.neutralHadronEnergyFraction ());
                }
            }
        }

      if (pfCands.isValid ())
        {
          for (const auto &probe : *pfCands)
            {
              if (probe.charge () == 0 || abs (probe.pdgId ()) < 100.0)
                continue;
              double mass = 0.0,
                     relIso = getTrackIsolation (probe, *pfCands, 0.3) / probe.pt ();
              bool isGoodInvMass = goodInvMass (tag, probe, mass),
                   isGoodRelIso = (relIso < 0.05);

              (isGoodInvMass && isGoodRelIso) && nGoodTagPFCHPairs++;

              if (isGoodRelIso)
                {
                  tagPFCHMasses.push_back (mass);
                  pfchRelIsos.push_back (relIso);
                }
            }
        }
    }

  (*eventvariables)["nGoodTPPairs"] = nGoodTPPairs;
  (*eventvariables)["nProbesPassingVeto"] = nProbesPassingVeto;
  (*eventvariables)["nProbesPassingLooseVeto"] = nProbesPassingLooseVeto;
  (*eventvariables)["nProbesFiringTrigger"] = nProbesFiringTrigger;
  (*eventvariables)["nProbesMatchingTag"] = nProbesMatchingTag;
  (*eventvariables)["nProbesFiringTriggerMatchingTag"] = nProbesFiringTriggerMatchingTag;

  (*eventvariables)["nGoodSSTPPairs"] = nGoodSSTPPairs;
  (*eventvariables)["nSSProbesPassingVeto"] = nSSProbesPassingVeto;
  (*eventvariables)["nSSProbesPassingLooseVeto"] = nSSProbesPassingLooseVeto;
  (*eventvariables)["nSSProbesFiringTrigger"] = nSSProbesFiringTrigger;
  (*eventvariables)["nSSProbesMatchingTag"] = nSSProbesMatchingTag;
  (*eventvariables)["nSSProbesFiringTriggerMatchingTag"] = nSSProbesFiringTriggerMatchingTag;

  (*eventvariables)["nGoodTagJetPairs"] = nGoodTagJetPairs;
  (*eventvariables)["nGoodTagPFCHPairs"] = nGoodTagPFCHPairs;

  bool tagJetMassNearZ = false;
  for (unsigned i = 0; i < 10; i++)
    {
      stringstream ss;

      ss.str ("");
      ss << i;
      (*eventvariables)["tagProbeMass_" + ss.str ()] = (masses.size () > i ? masses.at (i) : INVALID_VALUE);
      (*eventvariables)["tagProbeChargeProduct_" + ss.str ()] = (chargeProducts.size () > i ? chargeProducts.at (i) : INVALID_VALUE);
      (*eventvariables)["tagJetMass_" + ss.str ()] = (tagJetMasses.size () > i ? tagJetMasses.at (i) : INVALID_VALUE);
      (*eventvariables)["jetChargedHadronEnergyFraction_" + ss.str ()] = (jetChargedHadronEnergyFractions.size () > i ? jetChargedHadronEnergyFractions.at (i) : INVALID_VALUE);
      (*eventvariables)["jetNeutralHadronEnergyFraction_" + ss.str ()] = (jetNeutralHadronEnergyFractions.size () > i ? jetNeutralHadronEnergyFractions.at (i) : INVALID_VALUE);
      (*eventvariables)["tagPFCHMass_" + ss.str ()] = (tagPFCHMasses.size () > i ? tagPFCHMasses.at (i) : INVALID_VALUE);
      (*eventvariables)["pfchRelIso_" + ss.str ()] = (pfchRelIsos.size () > i ? pfchRelIsos.at (i) : INVALID_VALUE);

      tagJetMassNearZ = (tagJetMassNearZ || (fabs ((*eventvariables)["tagJetMass_" + ss.str ()] - 95.0) < 10.0));
    }

  if (doFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = (nProbesPassingVeto > 0);
  if (doSSFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = (nSSProbesPassingVeto > 0);
  if (doLooseFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = (nProbesPassingLooseVeto > 0);
  if (doLooseSSFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = (nSSProbesPassingLooseVeto > 0);
  if (doJetFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = tagJetMassNearZ;
}

template<class T, class... Args> const string
EventTPProducer<T, Args...>::tagCollectionParameter () const
{
  return "";
}

template<> const string
EventTPProducer<osu::Electron>::tagCollectionParameter () const
{
  return "electrons";
}

template<> const string
EventTPProducer<osu::Muon>::tagCollectionParameter () const
{
  return "muons";
}

template<> const string
EventTPProducer<osu::Electron, osu::Tau>::tagCollectionParameter () const
{
  return "electrons";
}

template<> const string
EventTPProducer<osu::Muon, osu::Tau>::tagCollectionParameter () const
{
  return "muons";
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const osu::Track &probe, double &m) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfElectron ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfMuon ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfPion ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfPion ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const pat::Jet &probe, double &m) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const pat::PackedCandidate &probe, double &m) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::passesVeto (const osu::Track &probe) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFElectron () > 0.15
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM
  bool passes = probe.deltaRToClosestElectron () > 0.15
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
  bool passes = probe.deltaRToClosestElectron () > 0.15
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestElectron () > 0.15
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#endif

  return passes;
}

template<> bool
EventTPProducer<osu::Electron>::passesLooseVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestVetoElectron () > 0.15
#if DATA_FORMAT == MINI_AOD_2017
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
#elif DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
#else
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
#endif
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
  return passes;
}

template<class T, class... Args> template<class T0> bool
EventTPProducer<T, Args...>::matchedToTag (const osu::Track &probe, const vector<T0> &tags) const
{
  for (const auto &tag : tags) {
    if (deltaR (probe, tag) < probeTagMatchingDR_) return true;
  }
  return false;
}

template<> bool
EventTPProducer<osu::Muon>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM || DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
  bool passes = probe.deltaRToClosestMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;          
#endif

  return passes;
}

template<> bool
EventTPProducer<osu::Muon>::passesLooseVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestLooseMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;          
  return passes;
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFChHad () > 0.15
             && probe.dRMinJet () > 0.5
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#endif

  return passes;
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::passesLooseVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestVetoElectron () > 0.15
#if DATA_FORMAT == MINI_AOD_2017
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
#elif DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
#else
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
#endif
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
  return passes;
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFChHad () > 0.15
             && probe.dRMinJet () > 0.5
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#endif

  return passes;
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::passesLooseVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestLooseMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;          
  return passes;
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::firesTrigger (const edm::Event &event,
                                           const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                                           const edm::TriggerResults &triggerBits,
                                           const osu::Track &probe) const
{
  for(auto triggerObj : triggerObjs) {

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,2,0)
    triggerObj.unpackNamesAndLabels(event, triggerBits);
#else
    triggerObj.unpackPathNames(event.triggerNames(triggerBits));
#endif

    if(triggerObj.collection() == (triggerCollectionName_)) {
      for(const auto &thisFilterName : triggerObj.filterLabels()) {
        if(thisFilterName == triggerFilterName_) {
          if(deltaR(probe, triggerObj) < triggerMatchingDR_) return true;
        }
      }
    }

  }

  return false;
}

template<class T, class... Args> template<class T0> const double
EventTPProducer<T, Args...>::getTrackIsolation (const T0 &track, const vector<T0> &tracks, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      if (!t.charge ())
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::jetMatchedToMuon (const pat::Jet &jet, const vector<pat::PackedCandidate> &pfCands) const
{
  for (const auto &pfCand : pfCands)
    {
      if (abs (pfCand.pdgId ()) != 13)
        continue;
      if (deltaR (jet, pfCand) < 0.4)
        return true;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronTPProducer);
DEFINE_FWK_MODULE(EventMuonTPProducer);
DEFINE_FWK_MODULE(EventTauToElectronTPProducer);
DEFINE_FWK_MODULE(EventTauToMuonTPProducer);
