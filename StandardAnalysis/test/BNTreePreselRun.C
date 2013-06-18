//---------------------------------------------------------------
// File and Version Information:
// $Id: BNTreePreselRun.C,v 1.2 2013/06/14 16:06:27 wulsin Exp $
//
// Description:
//    Prints one line of text.  To be used as template for 
//    writing new programs.  
//    To copy to a new file, do:
//    cp BNTreePreselRun.C newName.C
//    Then search & replace "BNTreePreselRun" for "newName".  
//
// Usage:
//     root -l -b -q 'BNTreePreselRun.C+' |& tee BNTreePreselRun.log
//
//     Or:
//     root [0] .x BNTreePreselRun.C  
//
//     Or:
//     root [0] .L BNTreePreselRun.C+  
//     root [1] BNTreePreselRun

#include <iomanip>  
#include <iostream>  
#include <vector>
#include "BNTreePresel.C"  


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
void BNTreePreselRun(TString condorDir="", 
	       TString dataset="",
	       TString chainName="",
	       int condorJobNum = -1);  // for default, -1, chain Trees from all files together  


// -------------------------
// -- Functions           --
// -------------------------
void BNTreePreselRun(TString condorDir, 
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

  BNTreePresel t(ch);  
  if (condorJobNum >= 0) {  
    t.Loop(condorDir + "/" + dataset + "/hist_" + condorJobNumStr + ".root");  
  } else {
    t.Loop(condorDir + "/" + dataset + ".root");  
  }
  
}  // void BNTreePreselRun(TString condorDir) {  


