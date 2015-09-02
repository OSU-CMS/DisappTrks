#ifndef ISR_ANALYZER
#define ISR_ANALYZER

#include <map>
#include <vector>

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1D.h"

using namespace std;

class ISRAnalyzer : public edm::EDAnalyzer
{
  public:
    ISRAnalyzer (const edm::ParameterSet &);
    ~ISRAnalyzer ();

    void analyze (const edm::Event &, const edm::EventSetup &);

  private:
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;

    edm::InputTag genParticles_;

    edm::Service<TFileService> fs_;
    map<string, TH1D *> oneDHists_;
};

#endif
