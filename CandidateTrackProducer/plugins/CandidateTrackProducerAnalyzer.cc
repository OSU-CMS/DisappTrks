#ifndef CUT_RESULTS_ANALYZER
#define CUT_RESULTS_ANALYZER

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Framework/interface/stream/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "TH1D.h"
#include "TString.h"

#include <iostream>

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

using namespace std;

class CandidateTrackProducerAnalyzer : public edm::stream::EDAnalyzer<>
{
public:
  CandidateTrackProducerAnalyzer(const edm::ParameterSet &);
  ~CandidateTrackProducerAnalyzer();

  void beginRun(const edm::Run &, const edm::EventSetup &) {}
  void analyze(const edm::Event &, const edm::EventSetup &);

private:
  edm::Service<TFileService> fs_;

  const edm::InputTag candTrkTag_;

  edm::Handle<vector<CandidateTrack>> candTrks_;
  edm::EDGetTokenT<vector<CandidateTrack>> candTrkToken_;

  map<string, TH1D *> oneDHists_;
};

CandidateTrackProducerAnalyzer::CandidateTrackProducerAnalyzer(const edm::ParameterSet &cfg) : candTrkTag_(cfg.getParameter<edm::InputTag>("candTrk"))
{
  candTrkToken_ = consumes<vector<CandidateTrack>>(candTrkTag_);

  TH1::SetDefaultSumw2();
  oneDHists_["candTrkEcalo_"] = fs_->make<TH1D>("candTrkEcalo", "candidate track Ecalo", 15, 0, 100);
  oneDHists_["candTrkNOuterHits_"] = fs_->make<TH1D>("candTrkNOuterHits", "candidate track number of outer hits", 31, -0.5, 30.5);
  oneDHists_["candTrkEcaloNLayers4_"] = fs_->make<TH1D>("candTrkEcaloNLayers4", "candidate track Ecalo - NLayers = 4", 15, 0, 100);
  oneDHists_["candTrkNOuterHitsNLayers4_"] = fs_->make<TH1D>("candTrkNOuterHitsNLayers4", "candidate track number of outer hits - NLayers = 4", 31, -0.5, 30.5);
  oneDHists_["candTrkEcaloNLayers5_"] = fs_->make<TH1D>("candTrkEcaloNLayers5", "candidate track Ecalo - NLayers = 5", 15, 0, 100);
  oneDHists_["candTrkNOuterHitsNLayers5_"] = fs_->make<TH1D>("candTrkNOuterHitsNLayers5", "candidate track number of outer hits - NLayers = 5", 31, -0.5, 30.5);
  oneDHists_["candTrkEcaloNLayersPlus6_"] = fs_->make<TH1D>("candTrkEcaloNLayersPlus6", "candidate track Ecalo - NLayers >= 6", 15, 0, 100);
  oneDHists_["candTrkNOuterHitsNLayersPlus6_"] = fs_->make<TH1D>("candTrkNOuterHitsNLayersPlus6", "candidate track number of outer hits - NLayers >= 6", 31, -0.5, 30.5);
}

CandidateTrackProducerAnalyzer::~CandidateTrackProducerAnalyzer() {}

void CandidateTrackProducerAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<CandidateTrack>> candTrks_;
  event.getByToken(candTrkToken_, candTrks_);

  for (const auto &candTrk_ : *candTrks_)
  {

    // oneDHists_.at("candTrkEcalo_")->Fill(candTrk_.caloNewNoPUDRp5CentralCalo());
    // oneDHists_.at("candTrkNOuterHits_")->Fill(candTrk_.hitAndTOBDrop_bestTrackMissingOuterHits);

    if (candTrk_.caloNewNoPUDRp5CentralCalo() < 10.0)
    {
      // oneDHists_.at("candTrkNOuterHits_")->Fill(candTrk_.hitAndTOBDrop_bestTrackMissingOuterHits());
      // if (candTrk_.hitPattern().trackerLayersWithMeasurement() == 4)
      //   oneDHists_.at("candTrkNOuterHitsNLayers4_")->Fill(candTrk_.hitAndTOBDrop_bestTrackMissingOuterHits());
      // if (candTrk_.hitPattern().trackerLayersWithMeasurement() == 5)
      //   oneDHists_.at("candTrkNOuterHitsNLayers5_")->Fill(candTrk_.hitAndTOBDrop_bestTrackMissingOuterHits());
      // if (candTrk_.hitPattern().trackerLayersWithMeasurement() >= 6)
      //   oneDHists_.at("candTrkNOuterHitsNLayersPlus6_")->Fill(candTrk_.hitAndTOBDrop_bestTrackMissingOuterHits());
      oneDHists_.at("candTrkNOuterHits_")->Fill(candTrk_.missingOuterHits_());
      if (candTrk_.hitPattern().trackerLayersWithMeasurement() == 4)
        oneDHists_.at("candTrkNOuterHitsNLayers4_")->Fill(candTrk_.missingOuterHits_());
      if (candTrk_.hitPattern().trackerLayersWithMeasurement() == 5)
        oneDHists_.at("candTrkNOuterHitsNLayers5_")->Fill(candTrk_.missingOuterHits_());
      if (candTrk_.hitPattern().trackerLayersWithMeasurement() >= 6)
        oneDHists_.at("candTrkNOuterHitsNLayersPlus6_")->Fill(candTrk_.missingOuterHits_());
    }
    // if (candTrk_.hitAndTOBDrop_bestTrackMissingOuterHits() >= 3)
    if (candTrk_.missingOuterHits_() >= 3)
    {
      oneDHists_.at("candTrkEcalo_")->Fill(candTrk_.caloNewNoPUDRp5CentralCalo());
      if (candTrk_.hitPattern().trackerLayersWithMeasurement() == 4)
        oneDHists_.at("candTrkEcaloNLayers4_")->Fill(candTrk_.caloNewNoPUDRp5CentralCalo());
      if (candTrk_.hitPattern().trackerLayersWithMeasurement() == 5)
        oneDHists_.at("candTrkEcaloNLayers5_")->Fill(candTrk_.caloNewNoPUDRp5CentralCalo());
      if (candTrk_.hitPattern().trackerLayersWithMeasurement() >= 6)
        oneDHists_.at("candTrkEcaloNLayersPlus6_")->Fill(candTrk_.caloNewNoPUDRp5CentralCalo());
    }
  }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CandidateTrackProducerAnalyzer);

#endif