#ifndef EVENT_L1_ETM_PRODUCER
#define EVENT_L1_ETM_PRODUCER

#include <vector>
#include <sstream>
#include <fstream>

#include "TVector2.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Run.h"

#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMask.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMaskAlgoTrigRcd.h"

#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

struct L1Seed : pair<int, double>
{
  L1Seed (const int &threshold, const double &prescale) :
    pair<int, double> (threshold, prescale)
    {
    }
  const int threshold () const { return this->first; }
  const double prescale () const { return this->second; }
};

template<class T> class EventL1ETMProducer : public EventVariableProducer
{
  public:
    EventL1ETMProducer (const edm::ParameterSet &);
    ~EventL1ETMProducer ();

  private:
    void AddVariables(const edm::Event &);
    void beginRun (const edm::Run &, const edm::EventSetup &);

    edm::EDGetTokenT<edm::TriggerResults> tokenTriggers_;
    edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjects_;
    edm::EDGetTokenT<vector<T> > tokenTags_;

    string tagCollection_;
    vector<string> filterCategories_;
    map<string, vector<string> > trigObjCollections_;
    map<string, vector<string> > trigObjFilterSubstrings_;

    vector<string> additionalCollections_;
    vector<string> additionalFilters_;

    map<int, vector<L1Seed> > l1PrescalesForAllRuns_;
    vector<L1Seed> l1Prescales_;

    const string tagCollectionParameter () const;
    const double getModifiedMissingEnergy (const TVector2 &, const TVector2 &, const bool, const double = 0.0) const;
    void extractL1Prescales (const string &);
    double getL1Prescale (const double) const;
};

typedef EventL1ETMProducer<osu::Electron> EventElectronL1ETMProducer;
typedef EventL1ETMProducer<osu::Muon> EventMuonL1ETMProducer;
typedef EventL1ETMProducer<osu::Tau> EventTauL1ETMProducer;

#endif
