#include "DisappTrks/StandardAnalysis/plugins/EventTimeAnalyzer.h"

EventTimeAnalyzer::EventTimeAnalyzer (const edm::ParameterSet &cfg) :
  runTimeInS_ (0.0)
{
  TH1::SetDefaultSumw2();
  oneDHists_["eventTime"] = fs_->make<TH1D> ("eventTime", ";unix time [s]", 10000, 1451606400, 1483228799);
  oneDHists_["runNumber"] = fs_->make<TH1D> ("runNumber", ";run number", 10887, 273158, 284045);
  oneDHists_["rateVsRunNumber"] = fs_->make<TH1D> ("rateVsRunNumber", ";run number;event rate [Hz]", 10887, 273158, 284045);
}

EventTimeAnalyzer::~EventTimeAnalyzer ()
{
}

void
EventTimeAnalyzer::beginRun (const edm::Run &run, const edm::EventSetup &setup)
{
  runTimeInS_ = run.endTime ().unixTime () - run.beginTime ().unixTime ();
}

void
EventTimeAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  oneDHists_["eventTime"]->Fill (event.time ().unixTime ());
  oneDHists_["runNumber"]->Fill (event.id ().run ());
  oneDHists_["rateVsRunNumber"]->Fill (event.id ().run (), runTimeInS_ ? (1.0 / runTimeInS_) : 0.0);
}

DEFINE_FWK_MODULE (EventTimeAnalyzer);
