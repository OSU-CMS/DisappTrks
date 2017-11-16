#ifndef EVENT_MET_TRIGGER_PRODUCER
#define EVENT_MET_TRIGGER_PRODUCER

#include <vector>

#include "TVector2.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

template<class T> class EventMETTriggerProducer : public EventVariableProducer
{
  public:
    EventMETTriggerProducer (const edm::ParameterSet &);
    ~EventMETTriggerProducer ();

  private:
    void AddVariables(const edm::Event &);
    edm::EDGetTokenT<edm::TriggerResults> tokenTriggers_;
    edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjects_;
    edm::EDGetTokenT<vector<T> > tokenTags_;

    vector<string> filterCategories_;
    map<string, vector<string> > trigObjCollections_;
    map<string, vector<double> > trigObjThresholds_;
    map<string, vector<string> > trigObjJetsForTag_;
    map<string, bool> muonsCountedAsVisible_;

    vector<string> additionalCollections_;
    vector<string> additionalFilters_;
    int metAndIsoTrk_;

    const string tagCollectionParameter () const;
    const string eventVariableName () const;
    const string metAndIsoTrkEventVariableName () const;
    const string tagCollection () const;
    const string tagFilter () const;
    const double getModifiedMissingEnergy (const TVector2 &, const TVector2 &, const bool, const double = 0.0) const;
};

typedef EventMETTriggerProducer<osu::Electron> EventElectronMETTriggerProducer;
typedef EventMETTriggerProducer<osu::Muon> EventMuonMETTriggerProducer;
typedef EventMETTriggerProducer<osu::Tau> EventTauMETTriggerProducer;

#endif
