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
  const Int_t nbinsMu = 2;
  int nbinsTot = nbins + nbinsMu;  

  // Get values from Spreadsheet  

  //  char *samples[nbins] = {"W+jets", "TTbar", "Single top", "Z+jets", "Diboson", "Z#rightarrownunu", "E_{T}^{miss} trigger total"};
  TString samples[nbins] = {"W#rightarrowl#nu", "TTbar", "Single top", "Z#rightarrowll", "Diboson", "Z#rightarrow#nu#nu", "E_{T}^{miss} trigger total"};  

  //  TString samplesMu[nbinsMu] = {"Z#rightarrowll", "W#rightarrowl#nu", "Total, MC", "Total, data"};  
  TString samplesMu[nbinsMu] = {"Z#rightarrow#mu#mu, MC", "Z#rightarrow#mu#mu, data"};  

  // W+jets	Ttbar	singletop	Z+jets	Diboson	Z->nunu	Total, Met trig
  // 6.90E-06	6.29E-06	2.36E-05	3.75E-06	6.92E-06	6.17E-06	6.73E-06
  // 1.37E-06	2.36E-06	1.81E-05	3.75E-06	3.39E-06	2.30E-06	1.08E-06
  Float_t fakeRates   [nbins] = {6.90E-06, 6.29E-06, 2.36E-05, 3.75E-06, 6.92E-06, 6.17E-06, 6.73E-06}; 
  Float_t fakeRatesErr[nbins] = {1.37E-06, 2.36E-06, 1.81E-05, 3.75E-06, 3.39E-06, 2.30E-06, 1.08E-06};  

  // Zmumu total MC	Zmumu data
  // 6.70E-06	1.12E-05
  // 9.31E-07	6.44E-06

  Float_t fakeRatesMu   [nbinsMu] = {5.74E-06, 1.12E-05}; 
  Float_t fakeRatesMuErr[nbinsMu] = {8.47E-07, 6.33E-06};  

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
  // grFakesMet->SetMinimum(1.e-7);
  // grFakesMet->SetMaximum(1.e-2);
  grFakesMet->SetMinimum(0);
  grFakesMet->SetMaximum(5.e-5);
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
  leg2.AddEntry(grFakesMet, "nominal selection, no E_{T}^{miss} cut", "pl");  
  leg2.AddEntry(grFakesMu, "Z#rightarrow#mu#mu selection", "pl");  
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


