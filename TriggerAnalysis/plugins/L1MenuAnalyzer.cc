#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"


#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "DataFormats/L1TGlobal/interface/GlobalExtBlk.h"
#include "L1Trigger/L1TGlobal/interface/L1TGlobalUtil.h"

#include <vector>
#include <string>
#include <iostream>

using namespace edm;
using namespace std;
using namespace l1t;

/****************************************************************************
 Simple example on how to access the L1 decision via  l1t::L1TGlobalUtil
 To make things easier it uses HLTPrescaleProvider to obtain the  
 l1t::L1TGlobalUtil object

 note, its very important that you run with the correct global tag as it
 retrieves the menu from this

 

 author Sam  Harper (RAL), 2019
*****************************************************************************/

class L1MenuAnalyzer : public edm::EDAnalyzer {
 
public:
  explicit L1MenuAnalyzer(const edm::ParameterSet& iConfig);
  ~L1MenuAnalyzer(){}
  
private:
  virtual void beginJob(){}
  virtual void beginRun(const edm::Run&, const edm::EventSetup&) override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endRun(const edm::Run&, EventSetup const&) override;
  virtual void endJob(){}

  L1TGlobalUtil* gtUtil_;
  std::vector<int> decisionCount_;
  std::vector<int> intermCount_;
  std::vector<int> finalCount_;

  InputTag algInputTag_;
  InputTag extInputTag_;
  edm::EDGetTokenT<BXVector<GlobalAlgBlk>> algToken_;
  edm::EDGetTokenT<BXVector<GlobalExtBlk>> extToken_;

  int finalOrCount;
};



L1MenuAnalyzer::L1MenuAnalyzer(const edm::ParameterSet& iConfig)
{
  algInputTag_ = iConfig.getParameter<InputTag>("AlgInputTag");
  extInputTag_ = iConfig.getParameter<InputTag>("ExtInputTag");
  algToken_ = consumes<BXVector<GlobalAlgBlk>>(algInputTag_);
  extToken_ = consumes<BXVector<GlobalExtBlk>>(extInputTag_);

  l1t::UseEventSetupIn useEventSetupIn = l1t::UseEventSetupIn::Run;
  useEventSetupIn = l1t::UseEventSetupIn::RunAndEvent;

  gtUtil_ = new L1TGlobalUtil(iConfig, consumesCollector(), *this, algInputTag_, extInputTag_, useEventSetupIn);
  finalOrCount = 0;

  if (false) {
    std::string preScaleFileName = iConfig.getParameter<std::string>("psFileName");
    unsigned int preScColumn = iConfig.getParameter<int>("psColumn");
    gtUtil_->OverridePrescalesAndMasks(preScaleFileName, preScColumn);
  }
}

//we need to initalise the menu each run (menu can and will change on run boundaries)
void L1MenuAnalyzer::beginRun(const edm::Run& iRun,const edm::EventSetup& setup)
{
  decisionCount_.clear();
  intermCount_.clear();
  finalCount_.clear();

  finalOrCount = 0;
  gtUtil_->retrieveL1Setup(setup);

  int size = gtUtil_->decisionsInitial().size();
  decisionCount_.resize(size);
  intermCount_.resize(size);
  finalCount_.resize(size);
}

void L1MenuAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  Handle<BXVector<GlobalAlgBlk>> alg;
  iEvent.getByToken(algToken_, alg);

  Handle<BXVector<GlobalExtBlk>> ext;
  iEvent.getByToken(extToken_, ext);

  LogDebug("l1t|Global") << "retrieved L1 GT data blocks" << endl;

  if (true) {
    //Fill the L1 result maps
    gtUtil_->retrieveL1(iEvent, iSetup, algToken_);

    LogDebug("l1t|Global") << "retrieved L1 data from GT Util" << endl;

    // grab the map for the final decisions
    const std::vector<std::pair<std::string, bool>> initialDecisions = gtUtil_->decisionsInitial();
    const std::vector<std::pair<std::string, bool>> intermDecisions = gtUtil_->decisionsInterm();
    const std::vector<std::pair<std::string, bool>> finalDecisions = gtUtil_->decisionsFinal();
    const std::vector<std::pair<std::string, int>> prescales = gtUtil_->prescales();
    const std::vector<std::pair<std::string, std::vector<int>>> masks = gtUtil_->masks();

    if ((decisionCount_.size() != gtUtil_->decisionsInitial().size()) ||
        (intermCount_.size() != gtUtil_->decisionsInterm().size()) ||
        (finalCount_.size() != gtUtil_->decisionsFinal().size())) {
      LogError("l1t|Global") << "gtUtil sizes inconsistent across run." << endl;
      return;
    }

    if (true) {
      cout << "\n===================================== Trigger Results for BX=0 "
              "=============================================\n"
           << endl;
      cout << "    Bit                  Algorithm Name                  Init    aBXM  Final   PS Factor     Num Bx "
              "Masked"
           << endl;
      cout << "========================================================================================================"
              "===="
           << endl;
    }
    for (unsigned int i = 0; i < initialDecisions.size(); i++) {
      // get the name and trigger result
      std::string name = (initialDecisions.at(i)).first;
      //if (name == "NULL")
      //  continue;

      bool resultInit = (initialDecisions.at(i)).second;

      // get prescaled and final results (need some error checking here)
      bool resultInterm = (intermDecisions.at(i)).second;
      bool resultFin = (finalDecisions.at(i)).second;

      // get the prescale and mask (needs some error checking here)
      double prescale = (prescales.at(i)).second;
      std::vector<int> mask = (masks.at(i)).second;

      if (resultInit)
        decisionCount_[i]++;
      if (resultInterm)
        intermCount_[i]++;
      if (resultFin)
        finalCount_[i]++;

      //cout << i << " " << decisionCount_[i] << "\n";

      if (true) {
        cout << std::dec << setfill(' ') << "   " << setw(5) << i << "   " << setw(40) << name.c_str() << "   "
             << setw(7) << resultInit << setw(7) << resultInterm << setw(7) << resultFin << setw(10) << prescale
             << setw(11) << mask.size() << endl;
      }
    }
    bool finOR = gtUtil_->getFinalOR();
    if (finOR)
      finalOrCount++;
    if (true) {
      cout << "                                                                FinalOR = " << finOR << endl;
      cout << "========================================================================================================"
              "==="
           << endl;
    }
  }

  if (true) {
    //int i = 0; // now now just printing BX=0...
    for (int i = -2; i <=  2; i++) {
      // Dump the coutput record
      cout << " ------ Bx= " << i << " ext ----------" << endl;
      if (ext.isValid()) {
        if (i >= ext->getFirstBX() && i <= ext->getLastBX()) {
          for (std::vector<GlobalExtBlk>::const_iterator extBlk = ext->begin(i); extBlk != ext->end(i); ++extBlk) {
            extBlk->print(cout);
            cout << std::dec;
          }
        } else {
          cout << "No Ext Conditions stored for this bx " << i << endl;
        }
      } else {
        LogError("L1TGlobalSummary") << "No ext Data in this event " << endl;
      }

      // Dump the coutput record
      cout << " ------ Bx= " << i << " alg ----------" << endl;
      if (alg.isValid()) {
        if (i >= alg->getFirstBX() && i <= alg->getLastBX()) {
          for (std::vector<GlobalAlgBlk>::const_iterator algBlk = alg->begin(i); algBlk != alg->end(i); ++algBlk) {
            algBlk->print(cout);
            cout << std::dec;
          }
        } else {
          cout << "No Alg Decisions stored for this bx " << i << endl;
        }
      } else {
        LogError("L1TGlobalSummary") << "No alg Data in this event " << endl;
      }
    }
  }

}

void L1MenuAnalyzer::endRun(Run const&, EventSetup const&) {
  if (true) {
    LogVerbatim out("L1TGlobalSummary");
    if (gtUtil_->valid()) {
      out << "==================  L1 Trigger Report  "
             "=====================================================================\n";
      out << '\n';
      out << " L1T menu Name   : " << gtUtil_->gtTriggerMenuName() << '\n';
      out << " L1T menu Version: " << gtUtil_->gtTriggerMenuVersion() << '\n';
      out << " L1T menu Comment: " << gtUtil_->gtTriggerMenuComment() << '\n';
      out << '\n';
      out << "    Bit                  Algorithm Name                  Init    PScd  Final   PS Factor     Num Bx "
             "Masked\n";
      out << "========================================================================================================="
             "===\n";
      auto const& prescales = gtUtil_->prescales();
      auto const& masks = gtUtil_->masks();
      for (unsigned int i = 0; i < prescales.size(); i++) {
        // get the prescale and mask (needs some error checking here)
        int resultInit = decisionCount_[i];
        int resultPre = intermCount_[i];
        int resultFin = finalCount_[i];

        auto const& name = prescales.at(i).first;
        if (name != "NULL") {
          double prescale = prescales.at(i).second;
          auto const& mask = masks.at(i).second;
          out << std::dec << setfill(' ') << "   " << setw(5) << i << "   " << setw(40) << name << "   " << setw(7)
              << resultInit << setw(7) << resultPre << setw(7) << resultFin << setw(10) << prescale << setw(11)
              << mask.size() << '\n';
        }
      }
      out << "                                                      Final OR Count = " << finalOrCount << '\n';
      out << "========================================================================================================="
             "===\n";
    } else {
      out << "==================  No Level-1 Trigger menu  "
             "===============================================================\n";
    }
  }
}


//define this as a plug-in
DEFINE_FWK_MODULE(L1MenuAnalyzer);
