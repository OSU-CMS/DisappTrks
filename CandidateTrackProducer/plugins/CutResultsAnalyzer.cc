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

#include "DisappTrks/CandidateTrackProducer/interface/CutResult.h"

using namespace std;

class CutResultsAnalyzer : public edm::stream::EDAnalyzer<> {
  public:
    CutResultsAnalyzer(const edm::ParameterSet &);
    ~CutResultsAnalyzer();

    void beginRun(const edm::Run &, const edm::EventSetup &);
    void analyze(const edm::Event &, const edm::EventSetup &) {}

  private:
    edm::Service<TFileService> fs_;
    
    TH1D * cutFlow_;
    TH1D * selection_;

    const edm::InputTag cutResultsTag_;

    edm::Handle<CutResults> cutResults_;
    edm::EDGetTokenT<CutResults> cutResultsToken_;
};

CutResultsAnalyzer::CutResultsAnalyzer(const edm::ParameterSet &cfg) : 
  cutResultsTag_(cfg.getParameter<edm::InputTag>("skimName"))
{
  cutResultsToken_ = consumes<CutResults, edm::InRun>(cutResultsTag_);

  TH1::SetDefaultSumw2();
  cutFlow_ = fs_->make<TH1D>("cutFlow", "skim cut flow", 10, 0, 10);
  selection_ = fs_->make<TH1D>("selection", "skim selection", 10, 0, 10);
}

CutResultsAnalyzer::~CutResultsAnalyzer() {}

void CutResultsAnalyzer::beginRun(const edm::Run &run, const edm::EventSetup &setup) {
  run.getByToken<CutResults>(cutResultsToken_, cutResults_);

  int iBin = 0;
  for(const auto &result : *cutResults_) {
    iBin++;

    if(cutFlow_->GetBinContent(iBin) == 0) {
      cutFlow_->GetXaxis()->SetBinLabel(iBin, (TString)(result.name));
      selection_->GetXaxis()->SetBinLabel(iBin, (TString)(result.name));
    }

    cutFlow_->SetBinContent(iBin, result.cumulativePassCount);
    cutFlow_->SetBinError(iBin, sqrt(result.cumulativePassCount));

    selection_->SetBinContent(iBin, result.accumulativePassCount);
    selection_->SetBinError(iBin, sqrt(result.accumulativePassCount));
  }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CutResultsAnalyzer);

#endif