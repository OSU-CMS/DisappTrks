//---------------------------------------------------------------
// File and Version Information:
// $Id: BNTreeMonojetRun.C,v 1.2 2013/06/19 08:52:29 wulsin Exp $
//
// Description:
//
// Usage:
//     root -l -b -q 'BNTreeMonojetRun.C+' |& tee BNTreeMonojetRun.log
//
//     Or:
//     root [0] .x BNTreeMonojetRun.C  
//
//     Or:
//     root [0] .L BNTreeMonojetRun.C+  
//     root [1] BNTreeMonojetRun

#include <iomanip>  
#include <iostream>  
#include <vector>
#include "BNTreeMonojet.C"  


#include "TChain.h"  
#include "TString.h"  


// -------------------------
// -- Execution history   --
// -------------------------


// -------------------------
// -- Global variables    --
// -------------------------


// -------------------------
// -- Function prototypes --
// -------------------------
void BNTreeMonojetRun(TString condorDir="", 
	       TString dataset="",
	       TString chainName="",
	       int condorJobNum = -1);  // for default, -1, chain Trees from all files together  


// -------------------------
// -- Functions           --
// -------------------------
void BNTreeMonojetRun(TString condorDir, 
	       TString dataset,
	       TString chainName,
	       int condorJobNum) {  

  TChain* ch = 0;
  TString condorJobNumStr = TString(Form("%d", condorJobNum));  // convert int to TString 

  if (chainName!="") {
    ch = new TChain(chainName);
    if (condorJobNum >= 0) {  
      ch->Add(condorDir + "/" + dataset + "/hist_" + condorJobNumStr + ".root");  
    } else {
      ch->Add(condorDir + "/" + dataset + "/hist*root");  
    }
  } 

  BNTree t(ch);  
  if (condorJobNum >= 0) {  
    t.Loop(condorDir + "/" + dataset + "/hist_" + condorJobNumStr + ".root");  
  } else {
    t.Loop(condorDir + "/" + dataset + ".root");  
  }
  
}  // void BNTreeMonojetRun(TString condorDir) {  


