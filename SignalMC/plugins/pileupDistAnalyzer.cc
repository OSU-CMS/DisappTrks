#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "TH1D.h"
#include <iostream>

class PileupDistAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
    explicit PileupDistAnalyzer(const edm::ParameterSet &cfg) :
        pileupToken_(consumes<std::vector<PileupSummaryInfo>>(cfg.getParameter<edm::InputTag>("pileupInfoTag")))
    {
        usesResource("TFileService");
    }

    void beginJob() override {
        std::cout << "PileupDistAnalyzer::beginJob() called" << std::endl;
        edm::Service<TFileService> fs;
        pileupHist_ = fs->make<TH1D>("pileup", "True number of interactions;numTrueInteractions;Events", 100, 0, 100);
    }

    void analyze(const edm::Event &event, const edm::EventSetup &setup) override {
        edm::Handle<std::vector<PileupSummaryInfo>> pileupInfos;
        event.getByToken(pileupToken_, pileupInfos);

        if (!pileupInfos.isValid()) {
            std::cout << "ERROR: PileupSummaryInfo handle is not valid!" << std::endl;
            return;
        }
        for (const auto &pv : *pileupInfos) {
            if (pv.getBunchCrossing() == 0) {
                pileupHist_->Fill(pv.getTrueNumInteractions());
                break;
            }
        }
    }

private:
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> pileupToken_;
    TH1D *pileupHist_;
};

DEFINE_FWK_MODULE(PileupDistAnalyzer);
