//---------------------------------------------------------------
// File and Version Information:
// $Id: makeFakeTrkRatePlot,v 1.5 2012/04/27 18:13:21 wulsin Exp $
//
// Description:
//    Makes plot of signal region optimization, for q=2/3 and q=1/3.
//
// Usage:
//     root -l -b -q 'makeFakeTrkRatePlot.C+' |& tee makeFakeTrkRatePlot.log
//
//     Or:
//     root [0] .x makeFakeTrkRatePlot  
//
//     Or:
//     root [0] .L makeFakeTrkRatePlot+  
//     root [1] makeFakeTrkRatePlot
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
void makeFakeTrkRatePlot();

// -------------------------
// -- Functions           --
// -------------------------
void makeFakeTrkRatePlot() {
   
  gStyle->SetOptStat(0);  
  TCanvas *c1 = new TCanvas("c1","A Simple Graph with error bars",200,10,700,500);
  
  const Int_t nbins = 7;
  const Int_t nbinsMu = 1;
  int nbinsTot = nbins + nbinsMu;  

  // Get values from Spreadsheet  

  //  char *samples[nbins] = {"W+jets", "TTbar", "Single top", "Z+jets", "Diboson", "Z#rightarrownunu", "E_{T}^{miss} trigger total"};
  TString samples[nbins] = {"W#rightarrowl#nu", "TTbar", "Single top", "Z#rightarrowll", "Diboson", "Z#rightarrow#nu#nu", "Total MC"};  

  //  TString samplesMu[nbinsMu] = {"Z#rightarrowll", "W#rightarrowl#nu", "Total, MC", "Total, data"};  
  TString samplesMu[nbinsMu] = {"Total MC"};  

  //                             W+jets       Ttbar   singletop	Z+jets	Diboson	  Z->nunu     Total
  Float_t fakeRates   [nbins] = {6.78E-05, 6.04E-05, 7.09E-05, 0.00E+00, 6.05E-05, 6.88E-05, 6.72E-05}; 
  Float_t fakeRatesErr[nbins] = {5.00E-06, 9.17E-06, 3.87E-05, 1.97E-04, 3.56E-05, 8.87E-06, 4.26E-06};  

  // Zmumu total MC	
  Float_t fakeRatesMu   [nbinsMu] = {6.39E-05}; 
  Float_t fakeRatesMuErr[nbinsMu] = {2.93E-06};  

  TH1F *grFakesMet = new TH1F("grFakesMet", "", nbinsTot, 0, nbinsTot); 
  TH1F *grFakesMu  = new TH1F("grFakesMu",  "", nbinsTot, 0, nbinsTot); 

  for (int i=1;i<=nbins;i++) {
    grFakesMet->SetBinContent(i, fakeRates   [i-1]);  
    grFakesMet->SetBinError  (i, fakeRatesErr[i-1]); 
    grFakesMet->GetXaxis()->SetBinLabel(i,samples[i-1]);
  }

  grFakesMet->SetMarkerStyle(21); // 21:  square  
  grFakesMet->SetMarkerSize(0.8);
  grFakesMet->SetMarkerColor(kBlue);
  grFakesMet->SetLineWidth(2);  
  grFakesMet->SetMinimum(0);
  grFakesMet->SetMaximum(2.5e-4);
  grFakesMet->SetTitle(";;P^{fake}");
  //  grFakesMet->Draw("ALP");
  grFakesMet->Draw("P");

  for (int i=nbins+1;i<=nbins+nbinsMu;i++) {
    grFakesMu->SetBinContent(i, fakeRatesMu   [i-1-nbins]);  
    grFakesMu->SetBinError  (i, fakeRatesMuErr[i-1-nbins]); 
    grFakesMet->GetXaxis()->SetBinLabel(i,samplesMu[i-1-nbins]);
  }

  grFakesMu->SetMarkerStyle(21); // 21:  square  
  grFakesMu->SetMarkerSize(0.8);
  grFakesMu->SetMarkerColor(kRed);
  grFakesMu->SetLineColor(kRed);  
  grFakesMu->SetLineWidth(2);  
  grFakesMu->Draw("P,same");


  TLegend leg2(0.50,0.6,0.85,0.8);
  leg2.AddEntry(grFakesMet, "Search sample", "pl");  
  leg2.AddEntry(grFakesMu, "Z#rightarrow#mu#mu double-tag sample", "pl");  
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
  pt->AddText("CMS Simulation, #sqrt{s} = 8 TeV");
  pt->Draw();


  c1->SetLogy(0);
  c1->Print("fakeTrkRates.pdf");  
  c1->Clear();

  return;

} 


