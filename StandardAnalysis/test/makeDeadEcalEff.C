//---------------------------------------------------------------
// File and Version Information:
// $Id: makeFakeTrkRatePlot,v 1.5 2012/04/27 18:13:21 wulsin Exp $
//
// Description:
//    Makes plot of signal region optimization, for q=2/3 and q=1/3.
//
// Usage:
//     root -l -b -q 'makeDeadEcalEff.C+' |& tee makeDeadEcalEff.log
//
//     Or:
//     root [0] .x makeDeadEcalEff  
//
//     Or:
//     root [0] .L makeDeadEcalEff+  
//     root [1] makeDeadEcalEff
//
//   
// Author List:
//      Wells Wulsin <wulsin.1@osu.edu>
//
// Copyright Information:
//      Copyright (C) 2012         OSU
//
// Revision History
//	20120101  Created. 
//---------------------------------------------------------------
#include <iostream>  
using std::cout;
using std::endl;

#include "TAxis.h" 
#include "TCanvas.h" 
#include "TFrame.h" 
#include "TH1F.h" 
#include "TLegend.h" 
#include "TLine.h"  
#include "TGraph.h" 
#include "TGraphAsymmErrors.h" 
#include "TGraphErrors.h" 
#include "TPaveText.h"
#include "TStyle.h"  

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
void makeDeadEcalEff();

// -------------------------
// -- Functions           --
// -------------------------
void makeDeadEcalEff() {
   
  gStyle->SetOptStat(0);  
  TCanvas *c1 = new TCanvas("c1","A Simple Graph with error bars",200,10,700,500);
  
  const Int_t nbins = 6;

  TString lifetime = "0.5";
  //   TString lifetime = "1";
   //   TString lifetime = "5";

   Float_t masses      [nbins] = {103, 164, 246, 328, 408, 488};  
   Float_t effOld0p5ns [nbins] = {0.884, 0.958, 0.889, 0.895, 0.897, 0.909}; 
   Float_t effDPG0p5ns [nbins] = {0.877, 0.958, 0.894, 0.884, 0.901, 0.888};  // Federico's DPG map 

   Float_t effOld1ns   [nbins] = {0.896, 0.93, 0.912, 0.944, 0.918, 0.914}; 
   Float_t effDPG1ns   [nbins] = {0.899, 0.92, 0.912, 0.926, 0.90, 0.901};  // Federico's DPG map 

   Float_t effOld5ns   [nbins] = {0.921, 0.938, 0.942, 0.92, 0.936, 0.942}; 
   Float_t effDPG5ns   [nbins] = {0.909, 0.913, 0.934, 0.911, 0.93, 0.936};  // Federico's DPG map 

   Float_t* effOld;
   Float_t* effDPG; 

   if (lifetime=="0p5") {
     effOld = effOld0p5ns;
     effDPG = effDPG0p5ns;
   }

   if (lifetime=="1") {
     effOld = effOld1ns;
     effDPG = effDPG1ns;
   }

   if (lifetime=="5") {
     effOld = effOld5ns;
     effDPG = effDPG5ns;
   }

   for (int i=0; i<nbins; i++) {
     effOld[i] = 1.0 - effOld[i];
     effDPG[i] = 1.0 - effDPG[i];
   }

   TGraph *grEffOld = new TGraph(nbins, masses, effOld);  
   TGraph *grEffDPG = new TGraph(nbins, masses, effDPG);  

   grEffOld->SetMarkerStyle(21); // 21:  square  
   grEffOld->SetMarkerSize(0.8);
   grEffOld->SetMarkerColor(kBlue);
   grEffOld->SetLineWidth(2);  
   grEffOld->SetMinimum(0);
   grEffOld->SetMaximum(0.25);
   //  grEffOld->SetTitle(";chargino mass;efficiency of dead ECAL veto"); 
   grEffOld->SetTitle(";chargino mass;1 - #epsilon"); 
   grEffOld->Draw("AP");
   //   grEffOld->Draw("P");

   grEffDPG->SetMarkerStyle(26); // 26:  hollow triangle 
   grEffDPG->SetMarkerSize(0.8);
   grEffDPG->SetMarkerColor(kRed);
   grEffDPG->SetLineWidth(2);  
   grEffDPG->Draw("P, same");

  TLine l;
  l.SetLineColor(kRed);
  l.DrawLine(2.5,1.0,6.5,1.0); 
  TLegend leg2(0.50,0.6,0.85,0.8);
  leg2.AddEntry(grEffOld, "old map ("      + lifetime + " ns)", "pl");  
  leg2.AddEntry(grEffDPG, "ECAL DPG map (" + lifetime + " ns)", "pl");  
  leg2.SetBorderSize(0);
  leg2.SetFillStyle(1001);
  leg2.SetFillColor(kWhite);
  leg2.SetBorderSize(0);
  leg2.SetTextFont(gStyle->GetTitleFont());
  leg2.Draw();


  TPaveText* pt = new TPaveText(0.50, 0.82, 0.90, 0.88, "NDC");
  pt->SetFillStyle(0);
  pt->SetBorderSize(0);
  pt->SetTextFont(gStyle->GetTitleFont());
  pt->AddText("CMS Preliminary, #sqrt{s} = 8 TeV");
  //  pt->Draw();


  c1->SetLogy(0);
  c1->Print("deadEcalEff" + lifetime + "ns.pdf");  
  c1->Clear();

  return;

} 


