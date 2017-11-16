#include "DisappTrks/BackgroundEstimation/plugins/EventMETTriggerProducer.h"

template<class T>
EventMETTriggerProducer<T>::EventMETTriggerProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenTriggers_ = consumes<edm::TriggerResults> (collections_.getParameter<edm::InputTag> ("triggers"));
  tokenTriggerObjects_ = consumes<vector<pat::TriggerObjectStandAlone> > (collections_.getParameter<edm::InputTag> ("trigobjs"));
  tokenTags_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));

  filterCategories_ = cfg.getParameter<vector<string> > ("filterCategories");
  for (const auto &filterCategory : filterCategories_)
    {
      trigObjCollections_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "Collections");
      trigObjThresholds_[filterCategory] = cfg.getParameter<vector<double> > (filterCategory + "Thresholds");
      trigObjJetsForTag_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "JetsForTag");
      muonsCountedAsVisible_[filterCategory] = cfg.getParameter<bool> (filterCategory + "MuonsCountedAsVisible");
    }
  additionalCollections_ = cfg.getParameter<vector<string> > ("additionalCollections");
  additionalFilters_ = cfg.getParameter<vector<string> > ("additionalFilters");
  metAndIsoTrk_ = cfg.getParameter<int> ("metAndIsoTrk");
}

template<class T>
EventMETTriggerProducer<T>::~EventMETTriggerProducer ()
{
}

template<class T> void
EventMETTriggerProducer<T>::AddVariables (const edm::Event &event)
{
  edm::Handle<edm::TriggerResults> triggers;
  event.getByToken (tokenTriggers_, triggers);

  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjects;
  event.getByToken (tokenTriggerObjects_, triggerObjects);

  edm::Handle<vector<T> > tags;
  event.getByToken (tokenTags_, tags);

  if (!triggers.isValid () || !triggerObjects.isValid () || !tags.isValid ())
    return;

  const pat::TriggerObjectStandAlone *hltTag = anatools::getMatchedTriggerObject (event, *triggers, tags->at (0), *triggerObjects, tagCollection (), "");
  map<string, vector<const pat::TriggerObjectStandAlone *> > hltFilterObjects, hltJetsForTag;
  int n = -1;
  for (const auto &filterCategory : filterCategories_)
    {
      const vector<string> &collections = trigObjCollections_.at (filterCategory);
      const vector<string> &jetsForTag = trigObjJetsForTag_.at (filterCategory);

      if (n < 0)
        n = collections.size ();

      vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects[filterCategory];
      vector<const pat::TriggerObjectStandAlone *> &jets = hltJetsForTag[filterCategory];

      for (int i = 0; i < n; i++)
        {
          const string &collection = collections.at (i);
          const string &jetForTag = jetsForTag.at (i);

          anatools::getTriggerObjects (event, *triggers, *triggerObjects, collection, "", objs);
          jets.push_back (anatools::getMatchedTriggerObject (event, *triggers, tags->at (0), *triggerObjects, jetForTag, ""));
        }
    }

  map<string, vector<bool> > filterDecisions, filterDecisionsUp;
  for (const auto &filterCategory : filterCategories_)
    {
      vector<bool> &filterDecision = filterDecisions[filterCategory];
      vector<bool> &filterDecisionUp = filterDecisionsUp[filterCategory];

      const vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects.at (filterCategory);
      const vector<const pat::TriggerObjectStandAlone *> &jets = hltJetsForTag.at (filterCategory);
      const vector<double> &thresholds = trigObjThresholds_.at (filterCategory);

      for (int i = 0; i < n; i++)
        {
          bool flag, flagUp;

          const pat::TriggerObjectStandAlone *tag = (trigObjJetsForTag_.at (filterCategory).at (i) == "" ? hltTag : jets.at (i));
          const pat::TriggerObjectStandAlone *obj = objs.at (i);

          TVector2 x, y;
          if (!tag)
            y.Set (0.0, 0.0);
          else
            y.Set (tag->px (), tag->py ());
          if (!obj && trigObjCollections_.at (filterCategory).at (i) == "")
            flag = flagUp = true;
          else
            {
              if (!obj)
                x.Set (0.0, 0.0);
              else
                x.Set (obj->px (), obj->py ());

              const double threshold = thresholds.at (i);
              const double modifiedMissingEnergy = getModifiedMissingEnergy (x, y, muonsCountedAsVisible_.at (filterCategory));
              const double modifiedMissingEnergyUp = getModifiedMissingEnergy (x, y, muonsCountedAsVisible_.at (filterCategory), 10.0);
              flag = (modifiedMissingEnergy > threshold);
              flagUp = (modifiedMissingEnergyUp > threshold);
            }

          filterDecision.push_back (flag);
          filterDecisionUp.push_back (flagUp);
        }
    }

  bool passes = false, passesUp = false,
       passesMETAndIsoTrk = false, passesMETAndIsoTrkUp = false;
  for (int i = 0; i < n; i++)
    {
      bool triggerPasses = true, triggerPassesUp = true;
      for (const auto &filterCategory : filterCategories_)
        {
          triggerPasses = triggerPasses && filterDecisions.at (filterCategory).at (i);
          triggerPassesUp = triggerPassesUp && filterDecisionsUp.at (filterCategory).at (i);
        }
      if (metAndIsoTrk_ != i)
        {
          passes = passes || triggerPasses;
          passesUp = passesUp || triggerPassesUp;
        }
      else
        {
          passesMETAndIsoTrk = passesMETAndIsoTrk || triggerPasses;
          passesMETAndIsoTrkUp = passesMETAndIsoTrkUp || triggerPassesUp;
        }
    }

  (*eventvariables)[eventVariableName ()] = passes;
  (*eventvariables)[eventVariableName () + "Up"] = passesUp;
  (*eventvariables)[metAndIsoTrkEventVariableName ()] = passesMETAndIsoTrk;
  (*eventvariables)[metAndIsoTrkEventVariableName () + "Up"] = passesMETAndIsoTrkUp;
  (*eventvariables)[eventVariableName () + "Ternary"] = (!passes && !passesMETAndIsoTrk ? 0 : (!passes && passesMETAndIsoTrk ? 1 : 2));
  (*eventvariables)[eventVariableName () + "TernaryUp"] = (!passesUp && !passesMETAndIsoTrkUp ? 0 : (!passesUp && passesMETAndIsoTrkUp ? 1 : 2));

  for (int i = 0; i < additionalCollections_.size (); i++)
    (*eventvariables)["passes_" + additionalFilters_.at (i)] = anatools::triggerObjectExists (event, *triggers, *triggerObjects, additionalCollections_.at (i), additionalFilters_.at (i));

  double l1ETM = INVALID_VALUE;
  (*eventvariables)["passesL1ETM"] = anatools::passesL1ETM (event, *triggers, *triggerObjects, l1ETM);
  (*eventvariables)["l1ETM"] = l1ETM;
}

template<class T> const string
EventMETTriggerProducer<T>::tagCollectionParameter () const
{
  return "";
}

template<> const string
EventMETTriggerProducer<osu::Electron>::tagCollectionParameter () const
{
  return "electrons";
}

template<> const string
EventMETTriggerProducer<osu::Muon>::tagCollectionParameter () const
{
  return "muons";
}

template<> const string
EventMETTriggerProducer<osu::Tau>::tagCollectionParameter () const
{
  return "taus";
}

template<class T> const string
EventMETTriggerProducer<T>::eventVariableName () const
{
  return "";
}

template<> const string
EventMETTriggerProducer<osu::Electron>::eventVariableName () const
{
  return "passesMETTriggersWithoutElectron";
}

template<> const string
EventMETTriggerProducer<osu::Muon>::eventVariableName () const
{
  return "passesMETTriggersWithoutMuon";
}

template<> const string
EventMETTriggerProducer<osu::Tau>::eventVariableName () const
{
  return "passesMETTriggersWithoutTau";
}

template<class T> const string
EventMETTriggerProducer<T>::metAndIsoTrkEventVariableName () const
{
  return "";
}

template<> const string
EventMETTriggerProducer<osu::Electron>::metAndIsoTrkEventVariableName () const
{
  return "passetMETAndIsoTrkWithoutElectron";
}

template<> const string
EventMETTriggerProducer<osu::Muon>::metAndIsoTrkEventVariableName () const
{
  return "passetMETAndIsoTrkWithoutMuon";
}

template<> const string
EventMETTriggerProducer<osu::Tau>::metAndIsoTrkEventVariableName () const
{
  return "passetMETAndIsoTrkWithoutTau";
}

template<class T> const string
EventMETTriggerProducer<T>::tagCollection () const
{
  return "";
}

template<> const string
EventMETTriggerProducer<osu::Electron>::tagCollection () const
{
  return "hltEgammaCandidates::HLT";
}

template<> const string
EventMETTriggerProducer<osu::Muon>::tagCollection () const
{
  return "hltL3MuonCandidates::HLT";
}

template<> const string
EventMETTriggerProducer<osu::Tau>::tagCollection () const
{
  return "hltSelectedPFTausTrackPt30AbsOrRelIsolation::HLT";
}

template<class T> const string
EventMETTriggerProducer<T>::tagFilter () const
{
  return "";
}

template<> const string
EventMETTriggerProducer<osu::Electron>::tagFilter () const
{
  return "hltEle25erWPTightGsfTrackIsoFilter";
}

template<> const string
EventMETTriggerProducer<osu::Muon>::tagFilter () const
{
  return "hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09";
}

template<> const string
EventMETTriggerProducer<osu::Tau>::tagFilter () const
{
  return "hltPFTau50TrackPt30LooseAbsOrRelIso";
}

template<class T> const double
EventMETTriggerProducer<T>::getModifiedMissingEnergy (const TVector2 &x, const TVector2 &y, const bool muonsCountedAsVisible, const double shift) const
{
  TVector2 z;
  z.SetMagPhi (shift, y.Phi ());
  return (x + y - z).Mod ();
}

template<> const double
EventMETTriggerProducer<osu::Muon>::getModifiedMissingEnergy (const TVector2 &x, const TVector2 &y, const bool muonsCountedAsVisible, const double shift) const
{
  TVector2 z;
  z.SetMagPhi (shift, y.Phi ());
  if (muonsCountedAsVisible)
    return (x + y - z).Mod ();
  return x.Mod ();
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronMETTriggerProducer);
DEFINE_FWK_MODULE(EventMuonMETTriggerProducer);
DEFINE_FWK_MODULE(EventTauMETTriggerProducer);
