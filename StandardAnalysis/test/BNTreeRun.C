//---------------------------------------------------------------
// File and Version Information:
// $Id: BNTreeRun.C,v 1.15 2012/07/09 08:06:02 wulsin Exp $
//
// Description:
//    Prints one line of text.  To be used as template for 
//    writing new programs.  
//    To copy to a new file, do:
//    cp BNTreeRun.C newName.C
//    Then search & replace "BNTreeRun" for "newName".  
//
// Usage:
//     root -l -b -q 'BNTreeRun.C+' |& tee BNTreeRun.log
//
//     Or:
//     root [0] .x BNTreeRun.C  
//
//     Or:
//     root [0] .L BNTreeRun.C+  
//     root [1] BNTreeRun

#include <iomanip>  
#include <iostream>  
#include <vector>
#include "BNTree.C"  


#include "TChain.h"  
#include "TString.h"  


// -------------------------
// -- Execution history   --
// -------------------------
// /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/analysisTemplateV2/CMSSW_5_3_8_patch1/src/DisappTrksT3ANTemp/StandardAnalysis/test > 
// root -l -b -q 'BNTreeRun.C+("condor/condor_2013_06_06_BNTreeTest/","ZZ","OSUAnalysis/WToMuSimple/BNTree_WToMuSimple")' 


// -------------------------
// -- Global variables    --
// -------------------------


// -------------------------
// -- Function prototypes --
// -------------------------
void BNTreeRun(TString condorDir="", 
	       TString dataset="",
	       TString chainName="");  


// -------------------------
// -- Functions           --
// -------------------------
void BNTreeRun(TString condorDir, 
	       TString dataset,
	       TString chainName) {  

  TChain* ch = 0;
  if (chainName!="") {
    ch = new TChain(chainName);     
    ch->Add(condorDir + "/" + dataset + "/hist*root");  
  }

  BNTree t(ch);  
  t.Loop(condorDir + "/" + dataset + ".root");  

}  // void BNTreeRun(TString condorDir) {  


