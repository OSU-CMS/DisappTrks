//---------------------------------------------------------------
// File and Version Information:
// $Id: copyPUFiles.C,v 1.1 2012/03/19 14:23:10 wulsin Exp $
//
// Description:
// Copy histograms from one root file to another.
//
// Usage:
//     root -l -b -q 'copyPUFiles.C+' |& tee copyPUFiles.log
//
//     Or:
//     root [0] .x copyPUFiles.C
//
//     Or:
//     root [0] .L copyPUFiles.C+
//     root [1] copyPUFiles
//
//
// Author List:
//      Wells Wulsin <wulsin.1@osu.edu>
//
// Copyright Information:
//      Copyright (C) 2012         OSU
//
// Revision History
//20120101  Created.
//---------------------------------------------------------------
#include <iostream>
using std::cout;
using std::endl;

#include "TCanvas.h"
#include "TFile.h"
#include "TH1.h"
#include "TString.h"

#ifndef __CINT__
#endif

// -------------------------
// -- Execution history   --
// -------------------------

// -------------------------
// -- Global variables    --
// -------------------------

// -------------------------
// -- Function prototypes --
// -------------------------
void copyPUFiles();
void copyOneFile(TFile* fin, TFile* fout, TString histname);

// -------------------------
// -- Functions           --
// -------------------------
void copyPUFiles() {
  cout << "CopyPUFiles world." << endl;

  TString dirCmssw = "/home/jbrinson/DisTrack/mainAN/AnTemp/CMSSW_6_1_2/src/";
  //  TFile *fin  = new TFile(dirCmssw+"DisappTrks/StandardAnalysis/data/pu_disappTrks.root", "READ");
  TFile *fin  = new TFile(dirCmssw+"DisappTrks/StandardAnalysis/test/condor/mGrav75K/pu.root", "READ");
  TFile *fout = new TFile(dirCmssw+"OSUT3Analysis/Configuration/data/pu.root", "UPDATE");

  copyOneFile(fin, fout, "AMSB_mGrav75K_0p5ns_Reco");
  copyOneFile(fin, fout, "AMSB_mGrav75K_1ns_Reco");
  copyOneFile(fin, fout, "AMSB_mGrav75K_5ns_Reco");

  //copyOneFile(fin, fout, "AMSB_mGrav32K_0p5ns_Reco");
  //copyOneFile(fin, fout, "AMSB_mGrav32K_1ns_Reco");
  //copyOneFile(fin, fout, "AMSB_mGrav32K_5ns_Reco");

  //  copyOneFile(fin, fout, "WJetsToLNu_Reco");
  //copyOneFile(fin, fout, "DYJetsToLL_Reco");

  //copyOneFile(fin, fout, "QCD_0to5_Reco");
  //copyOneFile(fin, fout, "QCD_5to15_Reco");
  //copyOneFile(fin, fout, "QCD_30to50_Reco");
  //copyOneFile(fin, fout, "QCD_80to120_Reco");
  //copyOneFile(fin, fout, "QCD_120to170_Reco");
  //copyOneFile(fin, fout, "QCD_170to300_Reco");
  //copyOneFile(fin, fout, "QCD_300to470_Reco");
  //copyOneFile(fin, fout, "QCD_470to600_Reco");
  // copyOneFile(fin, fout, "QCD_600to800_Reco");
  //copyOneFile(fin, fout, "QCD_800to1000_Reco");
  //copyOneFile(fin, fout, "QCD_1000to1400_Reco");
  //copyOneFile(fin, fout, "QCD_1400to1800_Reco");
  //copyOneFile(fin, fout, "QCD_1800_Reco");


  fin ->Close();
  fout->Close();

  return;

}

void copyOneFile(TFile* fin, TFile* fout, TString histname) {

  cout << "Copying histogram " << histname << endl;

  TH1* h;
  fin->GetObject(histname, h);
  if (!h) {
    cout << "Could not find hist named " << histname << endl;
    return;
  }
  fout->cd();
  if (histname!=h->GetName()) {
    h->SetName(histname);
    cout << "Resetting name to be = " << h->GetName()
         << endl;
  }
  // cout << "Debug:  name = " << h->GetName()
  //      << "; title = " << h->GetTitle()
  //      << endl;
  h->Write();

}








