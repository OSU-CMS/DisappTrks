#ifndef EVENT_TIME_ANALYZER

#define EVENT_TIME_ANALYZER

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class EventTimeAnalyzer : public edm::EDAnalyzer {
   public:
      explicit EventTimeAnalyzer (const edm::ParameterSet &);
      ~EventTimeAnalyzer ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);
      void beginRun (const edm::Run &, const edm::EventSetup &);

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      double runTimeInS_;
};

#endif
