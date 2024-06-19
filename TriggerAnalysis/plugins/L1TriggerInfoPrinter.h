#ifndef L1_TRIGGER_INFO_PRINTER
#define L1_TRIGGER_INFO_PRINTER

#include <iostream>
#include <sstream>
#include <string>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

#include "FWCore/Framework/interface/stream/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"

using namespace std;

class L1TriggerInfoPrinter : public edm::stream::EDAnalyzer<>
{
  public:
    L1TriggerInfoPrinter (const edm::ParameterSet &);
    ~L1TriggerInfoPrinter ();

    void analyze (const edm::Event &, const edm::EventSetup &);

  private:
    edm::InputTag l1GtReadoutRecord_;
    const edm::ESGetToken<L1GtTriggerMenu, L1GtTriggerMenuRcd> tok_l1gt_;
    edm::EDGetTokenT<L1GlobalTriggerReadoutRecord> tok_gtRec_;
};

#endif
