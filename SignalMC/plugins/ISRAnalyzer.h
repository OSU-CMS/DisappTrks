#ifndef ISR_ANALYZER
#define ISR_ANALYZER

#include <map>
#include <vector>

#include "TLorentzVector.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/EDGetToken.h"

#include "TH1D.h"

using namespace std;

class ISRAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
  public:
    ISRAnalyzer (const edm::ParameterSet &);
    ~ISRAnalyzer ();

    void analyze (const edm::Event &, const edm::EventSetup &);

  private:
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;

    edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

    edm::Service<TFileService> fs_;
    map<string, TH1D *> oneDHists_;
};

#endif
