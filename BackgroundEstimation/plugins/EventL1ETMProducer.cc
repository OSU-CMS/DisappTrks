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
      trigObjFilterSubstrings_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "FilterSubstrings");
      trigObjFilterSubstringsToReject_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "FilterSubstringsToReject");
    }
  additionalCollections_ = cfg.getParameter<vector<string> > ("additionalCollections");
  additionalFilters_ = cfg.getParameter<vector<string> > ("additionalFilters");

  extractL1Prescales (cfg.getParameter<edm::FileInPath> ("l1Prescales").fullPath ());
}

template<class T>
EventL1ETMProducer<T>::~EventL1ETMProducer ()
{
}

template<class T> void
EventL1ETMProducer<T>::beginRun (const edm::Run &run, const edm::EventSetup &setup)
{
  l1Prescales_ = l1PrescalesForAllRuns_.at (run.run ());
  sort (l1Prescales_.begin (), l1Prescales_.end (), [] (const L1Seed &a, const L1Seed &b) -> bool { return (a.threshold () < b.threshold ()); });

/*  edm::ESHandle<L1GtTriggerMenu> menuRcd;
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

  l1Threshold_ = lowestThreshold;*/
}

template<class T> void
EventL1ETMProducer<T>::AddVariables (const edm::Event &event, const edm::EventSetup &setup)
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
      const vector<string> &filterSubstrings = trigObjFilterSubstrings_.at (filterCategory);
      const vector<string> &filterSubstringsToReject = trigObjFilterSubstringsToReject_.at (filterCategory);

      if (n < 0)
        n = collections.size ();

      vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects[filterCategory];

      for (int i = 0; i < n; i++)
        {
          const string &collection = collections.at (i);
          const string &filterSubstring = filterSubstrings.at (i);

          anatools::getTriggerObjectsByFilterSubstring (event, *triggers, *triggerObjects, collection, filterSubstring, objs, filterSubstringsToReject);
        }
    }

  map<string, vector<double> > filterDecisions, filterDecisionsUp;
  for (const auto &filterCategory : filterCategories_)
    {
      vector<double> &filterDecision = filterDecisions[filterCategory];
      vector<double> &filterDecisionUp = filterDecisionsUp[filterCategory];

      const vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects.at (filterCategory);

      for (int i = 0; i < n; i++)
        {
          double flag, flagUp;

          const pat::TriggerObjectStandAlone *tag = hltTag;
          const pat::TriggerObjectStandAlone *obj = objs.at (i);

          TVector2 x, y;
          if (!tag)
            y.Set (0.0, 0.0);
          else
            y.Set (tag->px (), tag->py ());
          if (!obj && trigObjCollections_.at (filterCategory).at (i) == "")
            flag = flagUp = 1;
          else
            {
              if (!obj)
                x.Set (0.0, 0.0);
              else
                x.Set (obj->px (), obj->py ());

              const double modifiedMissingEnergy = getModifiedMissingEnergy (x, y, false);
              const double modifiedMissingEnergyUp = getModifiedMissingEnergy (x, y, false, 10.0);

              flag = getL1Prescale (modifiedMissingEnergy);
              flagUp = getL1Prescale (modifiedMissingEnergyUp);
            }

          filterDecision.push_back (flag);
          filterDecisionUp.push_back (flagUp);
        }
    }

  for (int i = 0; i < n; i++)
    {
      stringstream ss ("");
      ss << i;
      for (const auto &filterCategory : filterCategories_)
        {
          (*eventvariables)[filterCategory + "Prescale_" + ss.str ()] = filterDecisions.at (filterCategory).at (i);
          (*eventvariables)[filterCategory + "PrescaleUp_" + ss.str ()] = filterDecisionsUp.at (filterCategory).at (i);
        }
    }

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

template<class T> void
EventL1ETMProducer<T>::extractL1Prescales (const string &l1Prescales)
{
  l1PrescalesForAllRuns_.clear ();
  ifstream fin (l1Prescales);

  string line;
  while (getline (fin, line))
    {
      stringstream ssLine (line);
      string word = "", key = "";
      int run, threshold;
      double prescale;
      while (getline (ssLine, word, ' '))
        {
          if (word.length () > 0 && word.back () == ':')
            {
              stringstream ssWord (word);
              getline (ssWord, key, ':');
            }
          else
            {
              if (key == "run")
                run = atoi (word.c_str ());
              if (key == "threshold")
                threshold = atoi (word.c_str ());
              if (key == "average_prescale")
                prescale = atof (word.c_str ());
            }
        }
      if (!l1PrescalesForAllRuns_.count (run))
        l1PrescalesForAllRuns_[run];
      l1PrescalesForAllRuns_.at (run).emplace_back (threshold, prescale);
    }
}

template<class T> double
EventL1ETMProducer<T>::getL1Prescale (const double etm) const
{
  if (etm < l1Prescales_.at (0).threshold ())
    return 0.0;
  double lowestL1Prescale = -1.0;
  for (unsigned i = 0; i < l1Prescales_.size (); i++)
    {
      int threshold = l1Prescales_.at (i).threshold ();
      double prescale = l1Prescales_.at (i).prescale ();
      if (etm < threshold)
        break;
      if (prescale > 0.0 && (lowestL1Prescale < 0.0 || prescale < lowestL1Prescale))
        lowestL1Prescale = prescale;
    }
  if (lowestL1Prescale < 0.0)
    lowestL1Prescale = 0.0;
  return lowestL1Prescale;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronL1ETMProducer);
DEFINE_FWK_MODULE(EventMuonL1ETMProducer);
DEFINE_FWK_MODULE(EventTauL1ETMProducer);
