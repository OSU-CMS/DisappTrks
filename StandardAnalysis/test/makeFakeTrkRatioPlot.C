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
#include "TLine.h"  
#include "TGraph.h" 
#include "TGraphAsymmErrors.h" 
#include "TGraphErrors.h" 
#include "TPaveText.h"
#include "TStyle.h"  
#include "TString.h"  
#include "tables/fakeTrkRateRatioLL.h"  

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
void makeFakeTrkRatioPlot();

// -------------------------
// -- Functions           --
// -------------------------
void makeFakeTrkRatioPlot() {
  gROOT->SetBatch();

  std::string string(getenv("CMSSW_BASE"));
  std::string path("/src/DisappTrks/StandardAnalysis/python/tdrstyle.C");
  string+=path;
  char* pathToTdr = string.c_str();

  gROOT->LoadMacro(pathToTdr);
  gStyle->SetOptStat(0);  
  gStyle->SetPadLeftMargin  (0.15);
  gStyle->SetPadBottomMargin  (0.15);
  gStyle->SetPadRightMargin (0.05);
  gStyle->SetPadTickX       (1);
  gStyle->SetPadTickY       (1);
  setTDRStyle();   
  gStyle->SetNdivisions(7, "X");
  gStyle->SetNdivisions(504, "Y");
  gStyle->SetPadTopMargin   (0.07);
  gStyle->SetPadBottomMargin   (0.16);
  gStyle->SetPadLeftMargin   (0.16);
  gStyle->SetPadRightMargin   (0.06);
  gROOT->ForceStyle();
  TCanvas *c1 = new TCanvas("c1","A Simple Graph with error bars",200,10,600,600);
  //  TCanvas *c2 = new TCanvas("c2","A Simple Graph with error bars",200,10,700,500);
  //  TCanvas *c3 = new TCanvas("c3","A Simple Graph with error bars",200,10,700,500);  
  const Int_t nbins = 4;
  
  // Get values from Spreadsheet  
  
  //   //  char *samples[nbins] = {"W+jets", "TTbar", "Single top", "Z+jets", "Diboson", "Z#rightarrownunu", "E_{T}^{miss} trigger total"};
  //   TString samples[nbins] = {"W#rightarrowl#nu", "TTbar", "Single top", "Z#rightarrowll", "Diboson", "Z#rightarrow#nu#nu", "Total MC"};  
  
  //   //  TString samplesMu[nbinsMu] = {"Z#rightarrowll", "W#rightarrowl#nu", "Total, MC", "Total, data"};  
  //   TString samplesMu[nbinsMu] = {"Total MC"};  
  
  //   //                  nhits:            3            W+jets       Ttbar   singletop	Z+jets	Diboson	  Z->nunu     Total
  //   Float_t fakeRates   [nbins] = {6.78E-05, 6.04E-05, 7.09E-05, 0.00E+00, 6.05E-05, 6.88E-05, 6.72E-05}; 
  //   Float_t fakeRatesErr[nbins] = {5.00E-06, 9.17E-06, 3.87E-05, 1.97E-04, 3.56E-05, 8.87E-06, 4.26E-06};  
  
  
  TH1F *grFakesMet = new TH1F("grFakesMet", "", nbins, 2.5, 2.5+nbins);
  TH1F *grFakesMetEE = new TH1F("grFakesMetEE", "", nbins, 2.5, 2.5+nbins);
  TH1F *grFakesMetLL = new TH1F("grFakesMetLL", "", nbins, 2.5, 2.5+nbins);
  
  //   for (int i=1;i<=nbins;i++) {
  //     grFakesMet->SetBinContent(i, fakeRates   [i-1]);  
  //     grFakesMet->SetBinError  (i, fakeRatesErr[i-1]); 
  //     grFakesMet->GetXaxis()->SetBinLabel(i,samples[i-1]);
  //   }
  
  int ibin;
  int jbin;
  
  ibin = grFakesMet->FindBin(3); 
  grFakesMet->SetBinContent(ibin, 0.898);
  grFakesMet->SetBinError  (ibin, 0.169);
  ibin = grFakesMet->FindBin(4); 
  grFakesMet->SetBinContent(ibin, 1.103);
  grFakesMet->SetBinError  (ibin, 0.080);
  ibin = grFakesMet->FindBin(5);
  grFakesMet->SetBinContent(ibin, 0.856);
  grFakesMet->SetBinError  (ibin, 0.240);
  ibin = grFakesMet->FindBin(6); 
  grFakesMet->SetBinContent(ibin, 2.843);
  grFakesMet->SetBinError  (ibin, 1.614);
  
  grFakesMet->SetMarkerStyle(21); // 21:  square  
  grFakesMet->SetMarkerSize(0.8);
  grFakesMet->SetMarkerColor(kBlue);
  grFakesMet->SetLineWidth(2);  
  grFakesMet->SetMinimum(0);
  grFakesMet->SetMaximum(3.0);
  grFakesMet->SetTitle(";N_{hits} on candidate track;P^{fake}_{search}/P^{fake}_{Z#rightarrow#mu#mu}");
  grFakesMet->Draw("ALP");
  //  grFakesMet->Draw("P");
  
  TLine l;
  l.SetLineColor(kRed);
  l.DrawLine(2.5,1.0,6.5,1.0); 
  //   TLegend leg2(0.50,0.6,0.85,0.8);
  //   leg2.AddEntry(grFakesMet, "Disappearing track sample", "pl");  
  //   leg2.AddEntry(grFakesMu, "Z#rightarrow#mu#mu double-tag sample", "pl");  
  //   leg2.SetBorderSize(0);
  //   leg2.SetFillStyle(1001);
  //   leg2.SetFillColor(kWhite);
  //   leg2.SetBorderSize(0);
  //   leg2.SetTextFont(gStyle->GetTitleFont());
  //   leg2.Draw();
  
  
  TPaveText* pt = new TPaveText(0.50, 0.82, 0.90, 0.88, "NDC");
  pt->SetFillStyle(0);
  pt->SetBorderSize(0);
  pt->SetTextFont(gStyle->GetTitleFont());
  pt->AddText("CMS Preliminary, #sqrt{s} = 8 TeV");
  //  pt->Draw();
  
  
  //  c1->SetLogy(0);
  //c1->SaveAs("fakeTrkMuMu.pdf");  
  //c1->Clear();
  
  jbin = grFakesMetEE->FindBin(3);
  grFakesMetEE->SetBinContent(jbin, ratioEE_3);
  grFakesMetEE->SetBinError  (jbin, ratioErrEE_3);
  jbin = grFakesMetEE->FindBin(4);
  grFakesMetEE->SetBinContent(jbin, ratioEE_4);
  grFakesMetEE->SetBinError  (jbin, ratioErrEE_4);
  jbin = grFakesMetEE->FindBin(5);
  grFakesMetEE->SetBinContent(jbin, ratioEE_5);
  grFakesMetEE->SetBinError  (jbin, ratioErrEE_5);
  jbin = grFakesMetEE->FindBin(6);
  grFakesMetEE->SetBinContent(jbin, ratioEE_6);
  grFakesMetEE->SetBinError  (jbin, ratioErrEE_6);
  
  grFakesMetEE->SetMarkerStyle(21); // 21:  square                                                                                                                                                              
  grFakesMetEE->SetMarkerSize(0.8);
  grFakesMetEE->SetMarkerColor(kBlue);
  grFakesMetEE->SetLineWidth(2);
  grFakesMetEE->SetMinimum(0);
  grFakesMetEE->SetMaximum(3.0);
  grFakesMetEE->SetTitle(";N_{hits} on candidate track;P^{fake}_{search}/P^{fake}_{Z#rightarrow ee}");
  grFakesMetEE->Draw("ALP");                                                                                                                        
  //  grFakesMetEE->Draw("P");
  
  TLine l;
  l.SetLineColor(kRed);
  l.DrawLine(2.5,1.0,6.5,1.0);
  //   TLegend leg2(0.50,0.6,0.85,0.8);                                                                                                                                                                         
  //   leg2.AddEntry(grFakesMetEE, "Disappearing track sample", "pl");                                                                                                                                            
  //   leg2.AddEntry(grFakesMu, "Z#rightarrow#mu#mu double-tag sample", "pl");                                                                                                                                  
  //   leg2.SetBorderSize(0);                                                                                                                                                                                   
  //   leg2.SetFillStyle(1001);                                                                                                                                                                                 
  //   leg2.SetFillColor(kWhite);                                                                                                                                                                               
  //   leg2.SetBorderSize(0);                                                                                                                                                                                   
  //   leg2.SetTextFont(gStyle->GetTitleFont());                                                                                                                                                                
  //   leg2.Draw();                                                                                                                                                                                             
  
  
  TPaveText* pt = new TPaveText(0.6409396,0.9388112,0.9563758,0.9965035, "NDC");
  pt->SetFillStyle(0);
  pt->SetBorderSize(0);
  pt->SetTextFont(gStyle->GetTitleFont());
  //pt->AddText("CMS Preliminary, #sqrt{s} = 8 TeV");
  pt->AddText("19.5 fb^{-1} (8 TeV)");
  //  pt->Draw();                  

  //  TPaveText* pt2 = new TPaveText(0.50, 0.82, 0.90, 0.88, "NDC");
  TPaveText* pt2 = new TPaveText(0.1508621,0.8347458,0.5502874,0.8940678, "NDC");
  pt2->SetFillStyle(0);
  pt2->SetFillColor(0);
  pt2->SetBorderSize(0);
  pt2->SetTextFont(62);
  pt2->SetTextAlign(12);
  pt2->SetTextSize(0.07394366);
  //pt->AddText("CMS Preliminary, #sqrt{s} = 8 TeV");                                   
  pt2->AddText("CMS");
  //  pt->Draw();  

  //  TPaveText* pt2 = new TPaveText(0.50, 0.82, 0.90, 0.88, "NDC");                                                

  //  c2->SetLogy(0);
  //  c2->SaveAs("fakeTrkEE.pdf");
  //  c2->Clear();

  jbin = grFakesMetLL->FindBin(3);
  grFakesMetLL->SetBinContent(jbin, ratioLL_3);
  grFakesMetLL->SetBinError  (jbin, ratioErrLL_3);
  jbin = grFakesMetLL->FindBin(4);
  grFakesMetLL->SetBinContent(jbin, ratioLL_4);
  grFakesMetLL->SetBinError  (jbin, ratioErrLL_4);
  jbin = grFakesMetLL->FindBin(5);
  grFakesMetLL->SetBinContent(jbin, ratioLL_5);
  grFakesMetLL->SetBinError  (jbin, ratioErrLL_5);
  jbin = grFakesMetLL->FindBin(6);
  grFakesMetLL->SetBinContent(jbin, ratioLL_6);
  grFakesMetLL->SetBinError  (jbin, ratioErrLL_6);

  grFakesMetLL->SetMarkerStyle(21); // 21:  square
                                                                                                                                                                                                              
  grFakesMetLL->SetMarkerSize(0.8);
  grFakesMetLL->SetMarkerColor(kBlue);
  grFakesMetLL->SetLineWidth(2);
  grFakesMetLL->SetMinimum(0);
  grFakesMetLL->SetMaximum(3.0);
  grFakesMetLL->GetXaxis()->SetLabelSize(0.05);
  grFakesMetLL->GetXaxis()->SetTitleSize(0.06);
  grFakesMetLL->GetYaxis()->SetLabelSize(0.05);
  grFakesMetLL->GetYaxis()->SetTitleSize(0.08);
  grFakesMetLL->GetYaxis()->SetTitleOffset(0.81);
  grFakesMetLL->SetTitle(";N_{hits} on candidate track;P^{fake}_{search}/P^{fake}_{Z#rightarrow ll}");
  //    grFakesMetLL->Draw("ALP");
  grFakesMetLL->Draw("LEP");                                                                                                                                                                                
  pt->Draw("same");
  pt2->Draw("same");
  
  TLine l;
  l.SetLineColor(kRed);
  l.DrawLine(2.5,1.0,6.5,1.0);
  c1->SetLogy(0);
  c1->SaveAs("fakeTrkRatioLL.pdf");
  //c3->Clear();
  
  
  return;

} 


