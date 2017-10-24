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
      trigObjFilters_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "Filters");
      trigObjThresholds_[filterCategory] = cfg.getParameter<vector<double> > (filterCategory + "Thresholds");
      trigObjJetsForTag_[filterCategory] = cfg.getParameter<vector<string> > (filterCategory + "JetsForTag");
    }
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

  const pat::TriggerObjectStandAlone *hltTag = anatools::getMatchedTriggerObject (event, *triggers, tags->at (0), *triggerObjects, tagCollection (), tagFilter ());
  map<string, vector<const pat::TriggerObjectStandAlone *> > hltFilterObjects, hltJetsForTag;
  int n = -1;
  for (const auto &filterCategory : filterCategories_)
    {
      const vector<string> &collections = trigObjCollections_.at (filterCategory);
      const vector<string> &filters = trigObjFilters_.at (filterCategory);
      const vector<string> &jetsForTag = trigObjJetsForTag_.at (filterCategory);

      if (n < 0)
        n = collections.size ();

      vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects[filterCategory];
      vector<const pat::TriggerObjectStandAlone *> &jets = hltJetsForTag[filterCategory];

      for (int i = 0; i < n; i++)
        {
          const string &collection = collections.at (i);
          const string &filter = filters.at (i);
          const string &jetForTag = jetsForTag.at (i);

          anatools::getTriggerObjects (event, *triggers, *triggerObjects, collection, filter, objs);
          jets.push_back (anatools::getMatchedTriggerObject (event, *triggers, tags->at (0), *triggerObjects, jetForTag, ""));
        }
    }

  map<string, vector<bool> > filterDecisions;
  for (const auto &filterCategory : filterCategories_)
    {
      vector<bool> &filterDecision = filterDecisions[filterCategory];

      const vector<const pat::TriggerObjectStandAlone *> &objs = hltFilterObjects.at (filterCategory);
      const vector<const pat::TriggerObjectStandAlone *> &jets = hltJetsForTag.at (filterCategory);
      const vector<double> &thresholds = trigObjThresholds_.at (filterCategory);

      for (int i = 0; i < n; i++)
        {
          bool flag;

          const pat::TriggerObjectStandAlone *tag = (jets.at (i) ? jets.at (i) : hltTag);
          const pat::TriggerObjectStandAlone *obj = objs.at (i);
          if (!obj || !tag)
            {
              flag = true;
              continue;
            }
          const double threshold = thresholds.at (i);

          TVector2 x (obj->px (), obj->py ()),
                   y (tag->px (), tag->py ());
          flag = ((x + y).Mod () > threshold);

          filterDecision[i] = flag;
        }
    }

  bool passes = false;
  for (int i = 0; i < n; i++)
    {
      bool triggerPasses = true;
      for (const auto &filterCategory : filterCategories_)
        triggerPasses = triggerPasses && filterDecisions.at (filterCategory).at (i);
      passes = passes || triggerPasses;
    }

  (*eventvariables)[eventVariableName ()] = passes;
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

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronMETTriggerProducer);
DEFINE_FWK_MODULE(EventMuonMETTriggerProducer);
DEFINE_FWK_MODULE(EventTauMETTriggerProducer);
