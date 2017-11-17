#include "DisappTrks/BackgroundEstimation/plugins/EventL1ETMProducer.h"

template<class T>
EventL1ETMProducer<T>::EventL1ETMProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenTriggers_ = consumes<edm::TriggerResults> (collections_.getParameter<edm::InputTag> ("triggers"));
  tokenTriggerObjects_ = consumes<vector<pat::TriggerObjectStandAlone> > (collections_.getParameter<edm::InputTag> ("trigobjs"));
  tokenTags_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));

  tagCollection_ = cfg.getParameter<string> ("tagCollection");
  filterCategories_ = cfg.getParameter<vector<string> > ("filterCategories");
  for (const auto &filterCategory : filterCategories_)
    {
      trigObjCollections_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "Collections");
      trigObjFilterPrefixes_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "FilterPrefixes");
    }
  additionalCollections_ = cfg.getParameter<vector<string> > ("additionalCollections");
  additionalFilters_ = cfg.getParameter<vector<string> > ("additionalFilters");

  l1Threshold_ = 10000.0;
}

template<class T>
EventL1ETMProducer<T>::~EventL1ETMProducer ()
{
}

template<class T> void
EventL1ETMProducer<T>::beginRun (const edm::Run &run, const edm::EventSetup &setup)
{
  edm::ESHandle<L1GtTriggerMenu> menuRcd;
  setup.get<L1GtTriggerMenuRcd>().get (menuRcd) ;
  const AlgorithmMap &menu = menuRcd->gtAlgorithmMap ();

  edm::ESHandle<L1GtTriggerMask> maskRcd;
  setup.get<L1GtTriggerMaskAlgoTrigRcd>().get (maskRcd);
  const vector<unsigned> &mask = maskRcd->gtTriggerMask ();

  int lowestThreshold = -1;
  for (const auto &algorithm : menu)
    {
      const string &algorithmName = algorithm.first;
      if (algorithmName.find ("L1_ETM") != 0 || algorithmName.length () > 9)
        continue;
      const int algorithmThreshold = atoi (algorithmName.substr (6).c_str ());
      const int algorithmBit = algorithm.second.algoBitNumber ();

      const int algorithmMask = mask.at (algorithmBit);

      if (!algorithmMask)
        continue;
      if (lowestThreshold < 0 || algorithmThreshold < lowestThreshold)
        lowestThreshold = algorithmThreshold;
    }

  l1Threshold_ = lowestThreshold;
  clog << "L1 THRESHOLD: " << l1Threshold_ << " GeV" << endl;
}

template<class T> void
EventL1ETMProducer<T>::AddVariables (const edm::Event &event)
{
  edm::Handle<edm::TriggerResults> triggers;
  event.getByToken (tokenTriggers_, triggers);

  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjects;
  event.getByToken (tokenTriggerObjects_, triggerObjects);

  edm::Handle<vector<T> > tags;
  event.getByToken (tokenTags_, tags);

  if (!triggers.isValid () || !triggerObjects.isValid () || !tags.isValid ())
    return;

  const pat::TriggerObjectStandAlone *hltTag = anatools::getMatchedTriggerObject (event, *triggers, tags->at (0), *triggerObjects, tagCollection_, "");
  map<string, vector<const pat::TriggerObjectStandAlone *> > hltFilterObjects;
  int n = -1;
  for (const auto &filterCategory : filterCategories_)
    {
      const vector<string> &collections = trigObjCollections_.at (filterCategory);
      const vector<string> &filterPrefixes = trigObjFilterPrefixes_.at (filterCategory);

      if (n < 0)
        n = collections.size ();

      vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects[filterCategory];

      for (int i = 0; i < n; i++)
        {
          const string &collection = collections.at (i);
          const string &filterPrefix = filterPrefixes.at (i);

          anatools::getTriggerObjectsByFilterPrefix (event, *triggers, *triggerObjects, collection, filterPrefix, objs);
        }
    }

  map<string, vector<bool> > filterDecisions, filterDecisionsUp;
  for (const auto &filterCategory : filterCategories_)
    {
      vector<bool> &filterDecision = filterDecisions[filterCategory];
      vector<bool> &filterDecisionUp = filterDecisionsUp[filterCategory];

      const vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects.at (filterCategory);

      for (int i = 0; i < n; i++)
        {
          bool flag, flagUp;

          const pat::TriggerObjectStandAlone *tag = hltTag;
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

              const double modifiedMissingEnergy = getModifiedMissingEnergy (x, y, false);
              const double modifiedMissingEnergyUp = getModifiedMissingEnergy (x, y, false, 10.0);
              flag = (modifiedMissingEnergy > l1Threshold_);
              flagUp = (modifiedMissingEnergyUp > l1Threshold_);
            }

          filterDecision.push_back (flag);
          filterDecisionUp.push_back (flagUp);
        }
    }

  bool passes = false, passesUp = false;
  for (int i = 0; i < n; i++)
    {
      bool triggerPasses = true, triggerPassesUp = true;
      for (const auto &filterCategory : filterCategories_)
        {
          triggerPasses = triggerPasses && filterDecisions.at (filterCategory).at (i);
          triggerPassesUp = triggerPassesUp && filterDecisionsUp.at (filterCategory).at (i);
        }
      passes = passes || triggerPasses;
      passesUp = passesUp || triggerPassesUp;
    }

  (*eventvariables)["l1Threshold"] = l1Threshold_;
  (*eventvariables)[eventVariableName ()] = passes;
  (*eventvariables)[eventVariableName () + "Up"] = passesUp;

  for (unsigned i = 0; i < additionalCollections_.size (); i++)
    (*eventvariables)["passes_" + additionalFilters_.at (i)] = anatools::triggerObjectExists (event, *triggers, *triggerObjects, additionalCollections_.at (i), additionalFilters_.at (i));
}

template<class T> const string
EventL1ETMProducer<T>::tagCollectionParameter () const
{
  return "";
}

template<> const string
EventL1ETMProducer<osu::Electron>::tagCollectionParameter () const
{
  return "electrons";
}

template<> const string
EventL1ETMProducer<osu::Muon>::tagCollectionParameter () const
{
  return "muons";
}

template<> const string
EventL1ETMProducer<osu::Tau>::tagCollectionParameter () const
{
  return "taus";
}

template<class T> const string
EventL1ETMProducer<T>::eventVariableName () const
{
  return "";
}

template<> const string
EventL1ETMProducer<osu::Electron>::eventVariableName () const
{
  return "passesL1ETMWithoutElectron";
}

template<> const string
EventL1ETMProducer<osu::Muon>::eventVariableName () const
{
  return "passesL1ETMWithoutMuon";
}

template<> const string
EventL1ETMProducer<osu::Tau>::eventVariableName () const
{
  return "passesL1ETMWithoutTau";
}

template<class T> const double
EventL1ETMProducer<T>::getModifiedMissingEnergy (const TVector2 &x, const TVector2 &y, const bool muonsCountedAsVisible, const double shift) const
{
  TVector2 z;
  z.SetMagPhi (shift, y.Phi ());
  return (x + y - z).Mod ();
}

template<> const double
EventL1ETMProducer<osu::Muon>::getModifiedMissingEnergy (const TVector2 &x, const TVector2 &y, const bool muonsCountedAsVisible, const double shift) const
{
  TVector2 z;
  z.SetMagPhi (shift, y.Phi ());
  if (muonsCountedAsVisible)
    return (x + y - z).Mod ();
  return x.Mod ();
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronL1ETMProducer);
DEFINE_FWK_MODULE(EventMuonL1ETMProducer);
DEFINE_FWK_MODULE(EventTauL1ETMProducer);
