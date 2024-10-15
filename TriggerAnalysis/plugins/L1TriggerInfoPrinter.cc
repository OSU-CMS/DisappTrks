#include "DisappTrks/TriggerAnalysis/plugins/L1TriggerInfoPrinter.h"

L1TriggerInfoPrinter::L1TriggerInfoPrinter (const edm::ParameterSet &cfg) :
  l1GtReadoutRecord_ (cfg.getParameter<edm::InputTag> ("l1GtReadoutRecord")),
  tok_l1gt_ (esConsumes<L1GtTriggerMenu, L1GtTriggerMenuRcd>())
{
  tok_gtRec_ = consumes<L1GlobalTriggerReadoutRecord> (l1GtReadoutRecord_);
}

L1TriggerInfoPrinter::~L1TriggerInfoPrinter ()
{
}

void
L1TriggerInfoPrinter::analyze (const edm::Event &iEvent, const edm::EventSetup &iSetup)
{
  stringstream ss;
  ss.str ("");

  edm::ESHandle<L1GtTriggerMenu> menuRcd;
  // iSetup.get<L1GtTriggerMenuRcd>().get(menuRcd) ;
  menuRcd = iSetup.getHandle(tok_l1gt_);
  const L1GtTriggerMenu* menu = menuRcd.product();
  const AlgorithmMap& bitMap = menu->gtAlgorithmMap();
  ss<<" Number of algorithms in L1 GT menu: "<<bitMap.size()<<endl;

  edm::Handle<L1GlobalTriggerReadoutRecord> gtRecord;
  iEvent.getByToken(tok_gtRec_, gtRecord);

  ss<<"================================================================================"<<endl;
  ss<<" Printing L1GlobalTriggerReadoutRecord..."<<endl;
  ss<<"--------------------------------------------------------------------------------"<<endl;
  ss<<(*gtRecord)<<endl;
  ss<<"--------------------------------------------------------------------------------"<<endl;
  gtRecord->printGtDecision(ss);
  ss<<"--------------------------------------------------------------------------------"<<endl;
  gtRecord->printTechnicalTrigger(ss);
  ss<<"--------------------------------------------------------------------------------"<<endl;
  gtRecord->print(ss);
  ss<<"================================================================================"<<endl;

  if (!gtRecord.isValid()) {
    ss<<" No L1 trigger record "<<endl;
  } else {

    const DecisionWord dWord = gtRecord->decisionWord();
    ss<<" Size of decision word from readout record: "<<dWord.size()<<endl;

    if (dWord.empty()) {
      ss<<" No decision word from readout record "<<endl;
    } else {
      for (CItAlgo itAlgo = bitMap.begin(); itAlgo != bitMap.end(); itAlgo++) {
        bool decision=menu->gtAlgorithmResult(itAlgo->first,dWord);
        /*if(decision == 1)*/ ss<<" Trigger "<<itAlgo->first<<" "<<(decision ? "PASSES" : "FAILS")<<endl;
      }

    }
  }

  edm::LogInfo("L1TriggerInfoPrinter")<<ss.str ();
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(L1TriggerInfoPrinter);
