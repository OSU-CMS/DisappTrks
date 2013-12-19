//---------------------------------------------------------------
// File and Version Information:
// $Id: makeXSecPlot.C,v 1.2 2013/01/04 14:06:31 wulsin Exp $
//
// Description:
//    Makes plot of cross-section versus mass. 
//    Shows expected, observes, and theoretical values.  
//    Template copied from $ROOTSYS/tutorials/graphs/gerrors.C.  
//
// Usage:
//     root -l -b -q 'makeXSecPlot.C+' | tee makeXSecPlot.log
//
//     Or:
//     root [0] .x makeXSecPlot.C  
//
//     Or:
//     root [0] .L makeXSecPlot.C+  
//     root [1] makeXSecPlot
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
#include "TLegend.h" 
#include "TGraph.h" 
#include "TGraphAsymmErrors.h" 
#include "TGraphErrors.h" 
#include "TPaveText.h"
#include "TStyle.h"

#include "/afs/cern.ch/user/w/wulsin/root/tdrstyle.C"   

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
void makeXSecPlot();
void setAxes(TGraphAsymmErrors* gr);  

// -------------------------
// -- Functions           --
// -------------------------
void makeXSecPlot() {

  setTDRStyle(); 
  gStyle->SetPadRightMargin(0.05);
  gStyle->SetPadTopMargin(0.1);
  gStyle->SetPadBottomMargin(0.15);
 

  TCanvas *c1 = new TCanvas("c1","A Simple Graph with error bars",200,10,700,500);
  
  const Int_t nbins = 4;
  // Get values from tab:limits, in results.tex.  
  Float_t m                [nbins]  = {  103.6, 164.3, 328.3, 488.6 };  // mass points
  Float_t mErr             [nbins]  = {     0,      0,      0,      0};  // for now assume 0 error on mass
  Float_t noErr            [nbins]  = {     0,      0,      0,      0};  // no errors  


  // To get theory cross sections, follow instructions on:
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012#GEN_only_jobs
  // Units are picobarns.  
  // m3/2 = 32 TeV: chargino+neutralino = 6.6 pb; chargino+chargino = 4.0; total = 11 pb
  // m3/2 = 50 TeV: chargino+neutralino = 1.3 pb; chargino+chargino = 0.61 pb; total = 2.0 pb
  // m3/2 = 100 TeV: chargino+neutralino = 70 fb; chargino+chargino = 31 fb; total = 101 fb
  // m3/2 = 150 TeV: chargino+neutralino = 9.9 fb; chargino+chargino = 4.7 fb; total = 15 fb 


  Float_t xsecThytau5ns   [nbins]  = {      11,         2,    0.101,      0.015};  
  Float_t xsecThytau5nsErr[nbins]  = {       0,         0,        0,          0};  // FIXME: for now assume 0 error on cross section

  Float_t xsecThytau1ns   [nbins]  = {      11,         2,    0.101,      0.015};  
  Float_t xsecThytau1nsErr[nbins]  = {       0,         0,        0,          0};  // FIXME: for now assume 0 error on cross section

  Float_t xsecThytau0p5ns   [nbins]  = {      11,         2,    0.101,      0.015};  
  Float_t xsecThytau0p5nsErr[nbins]  = {        0,        0,         0,          0};  // FIXME: for now assume 0 error on cross section

  // Obtain results by running: 
  // /afs/cern.ch/user/w/wulsin/public/disappTrk/limitCodeV2/CMSSW_5_3_2_patch4/src/StatisticalTools/RooStatsRoutines/root> 
  //  root -l -b -q 'readResults.C+' | & tee readResults.log 
  // Get values for expected and observed limits from AN-12-400, 
  // Table \ref{tab:limits} in results.tex.    
  Float_t xsecObstau0p5ns   [nbins]  = {0.142822,  0.197887,  0.571474,  0.182755};    
  Float_t xsecObstau0p5nsErr[nbins]  = {     0,      0,      0,      0};  // FIXME: for now assume 0 error on cross section

  Float_t xsecObstau1ns   [nbins]  = {0.160485,  0.0646986,  0.0609179,  0.0664116};    
  Float_t xsecObstau1nsErr[nbins]  = {     0,      0,      0,      0};  // FIXME: for now assume 0 error on cross section

  Float_t xsecObstau5ns   [nbins]  = {0.155414,  0.025171,  0.0266395,  0.0609179};    
  Float_t xsecObstau5nsErr[nbins]  = {     0,      0,      0,      0};  // FIXME: for now assume 0 error on cross section

  Float_t xsecExptau0p5ns          [nbins]  = { 0.14994,  0.201865,  0.533682,  0.188514};    
  Float_t xsecExptau0p5nsBand2SigHi[nbins]  = { 0.255397,  0.370649,  0.9809,  0.349636};    
  Float_t xsecExptau0p5nsBand1SigHi[nbins]  = { 0.226708,  0.30788,  0.84749,  0.287201};    
  Float_t xsecExptau0p5nsBand2SigLo[nbins]  = { 0.0891604,  0.117447,  0.292366,  0.10928};    
  Float_t xsecExptau0p5nsBand1SigLo[nbins]  = { 0.109606,  0.150675,  0.380982,  0.137251};    

  Float_t xsecExptau1ns          [nbins]  = {0.165654,  0.0672073,  0.0639195,  0.0687877};    
  Float_t xsecExptau1nsBand2SigHi[nbins]  = { 0.286315,  0.130783,  0.113725,  0.127305};    
  Float_t xsecExptau1nsBand1SigHi[nbins]  = { 0.249477,  0.101475,  0.091481,  0.1004};    
  Float_t xsecExptau1nsBand2SigLo[nbins]  = { 0.120554,  0.0493467,  0.0450687,  0.0422638};    
  Float_t xsecExptau1nsBand1SigLo[nbins]  = { 0.127255,  0.0520503,  0.0461514,  0.0506969};    


  Float_t xsecExptau5ns          [nbins]  = { 0.159247,  0.0257887,  0.027362,  0.0639195};    
  Float_t xsecExptau5nsBand2SigHi[nbins]  = { 0.295831,  0.0466699,  0.0492391,  0.113725};    
  Float_t xsecExptau5nsBand1SigHi[nbins]  = { 0.245272,  0.0370808,  0.0387608,  0.091481};    
  Float_t xsecExptau5nsBand2SigLo[nbins]  = { 0.0925721,  0.0157938,  0.0167346,  0.0450687};    
  Float_t xsecExptau5nsBand1SigLo[nbins]  = { 0.118912,  0.0239069,  0.0217266,  0.0461514};    




  Float_t xsecExptau5nsErr1SigHi[nbins]; 
  Float_t xsecExptau5nsErr1SigLo[nbins];  
  Float_t xsecExptau5nsErr2SigHi[nbins]; 
  Float_t xsecExptau5nsErr2SigLo[nbins];  

  Float_t xsecExptau1nsErr1SigHi[nbins]; 
  Float_t xsecExptau1nsErr1SigLo[nbins];  
  Float_t xsecExptau1nsErr2SigHi[nbins]; 
  Float_t xsecExptau1nsErr2SigLo[nbins];  

  Float_t xsecExptau0p5nsErr1SigHi[nbins]; 
  Float_t xsecExptau0p5nsErr1SigLo[nbins];  
  Float_t xsecExptau0p5nsErr2SigHi[nbins]; 
  Float_t xsecExptau0p5nsErr2SigLo[nbins];  

  for (int i=0; i<nbins; i++) { 
    xsecExptau5nsErr1SigHi[i] =   xsecExptau5nsBand1SigHi[i] - xsecExptau5ns[i]; 
    xsecExptau5nsErr1SigLo[i] = -(xsecExptau5nsBand1SigLo[i] - xsecExptau5ns[i]); 
    xsecExptau5nsErr2SigHi[i] =   xsecExptau5nsBand2SigHi[i] - xsecExptau5ns[i]; 
    xsecExptau5nsErr2SigLo[i] = -(xsecExptau5nsBand2SigLo[i] - xsecExptau5ns[i]); 

    xsecExptau1nsErr1SigHi[i] =   xsecExptau1nsBand1SigHi[i] - xsecExptau1ns[i]; 
    xsecExptau1nsErr1SigLo[i] = -(xsecExptau1nsBand1SigLo[i] - xsecExptau1ns[i]); 
    xsecExptau1nsErr2SigHi[i] =   xsecExptau1nsBand2SigHi[i] - xsecExptau1ns[i]; 
    xsecExptau1nsErr2SigLo[i] = -(xsecExptau1nsBand2SigLo[i] - xsecExptau1ns[i]); 

    xsecExptau0p5nsErr1SigHi[i] =   xsecExptau0p5nsBand1SigHi[i] - xsecExptau0p5ns[i]; 
    xsecExptau0p5nsErr1SigLo[i] = -(xsecExptau0p5nsBand1SigLo[i] - xsecExptau0p5ns[i]); 
    xsecExptau0p5nsErr2SigHi[i] =   xsecExptau0p5nsBand2SigHi[i] - xsecExptau0p5ns[i]; 
    xsecExptau0p5nsErr2SigLo[i] = -(xsecExptau0p5nsBand2SigLo[i] - xsecExptau0p5ns[i]); 
  }


  TGraphAsymmErrors *grExptau5ns = new TGraphAsymmErrors(nbins, m, xsecExptau5ns, mErr, mErr, xsecExptau5nsErr1SigLo, xsecExptau5nsErr1SigHi);  
  TGraphAsymmErrors *grExptau1ns = new TGraphAsymmErrors(nbins, m, xsecExptau1ns, mErr, mErr, xsecExptau1nsErr1SigLo, xsecExptau1nsErr1SigHi);  
  TGraphAsymmErrors *grExptau0p5ns = new TGraphAsymmErrors(nbins, m, xsecExptau0p5ns, mErr, mErr, xsecExptau0p5nsErr1SigLo, xsecExptau0p5nsErr1SigHi);  
  TGraphErrors *grObstau5ns = new TGraphErrors(nbins, m, xsecObstau5ns, mErr, xsecObstau5nsErr);  
  TGraphErrors *grObstau1ns = new TGraphErrors(nbins, m, xsecObstau1ns, mErr, xsecObstau1nsErr);  
  TGraphErrors *grObstau0p5ns = new TGraphErrors(nbins, m, xsecObstau0p5ns, mErr, xsecObstau0p5nsErr);  
  TGraphErrors *grThytau5ns = new TGraphErrors(nbins, m, xsecThytau5ns, mErr, xsecThytau5nsErr);  
  TGraphErrors *grThytau1ns = new TGraphErrors(nbins, m, xsecThytau1ns, mErr, xsecThytau1nsErr);  
  TGraphErrors *grThytau0p5ns = new TGraphErrors(nbins, m, xsecThytau0p5ns, mErr, xsecThytau0p5nsErr);  
  grExptau5ns->SetMarkerStyle(21); // 21:  square  
  grExptau1ns->SetMarkerStyle(21); // 21:  square  
  grExptau0p5ns->SetMarkerStyle(21);
  grObstau5ns->SetMarkerStyle(23); // 23:  triangle
  grObstau1ns->SetMarkerStyle(23); // 23:  triangle
  grObstau0p5ns->SetMarkerStyle(23);
  grThytau5ns->SetMarkerStyle(20); // 20:  circle  
  grThytau1ns->SetMarkerStyle(20); // 20:  circle  
  grThytau0p5ns->SetMarkerStyle(20);

  // grExptau1ns->SetMarkerSize(0);
  // grExptau0p5ns->SetMarkerSize(0);
  // grObstau1ns->SetMarkerSize(0);  
  // grObstau0p5ns->SetMarkerSize(0);

  grExptau5ns->SetMarkerColor(kBlue);
  grObstau5ns->SetMarkerColor(kBlue);
  grThytau5ns->SetMarkerColor(kBlue);
  grExptau1ns->SetMarkerColor(kBlue);
  grObstau1ns->SetMarkerColor(kBlue);
  grThytau1ns->SetMarkerColor(kBlue);
  grExptau0p5ns->SetMarkerColor(kRed);
  grObstau0p5ns->SetMarkerColor(kRed);
  grThytau0p5ns->SetMarkerColor(kRed);

  grThytau5ns->SetLineColor(kRed);
  grThytau1ns->SetLineColor(kRed);
  grThytau0p5ns->SetLineColor(kRed);

  grThytau5ns->SetLineStyle(kDotted);
  grThytau1ns->SetLineStyle(kDotted);
  grThytau0p5ns->SetLineStyle(kDotted);  

  grExptau5ns->SetLineStyle(2);
  grExptau1ns->SetLineStyle(2);
  grExptau0p5ns->SetLineStyle(2);

  grThytau5ns->SetLineWidth(2);
  grThytau1ns->SetLineWidth(2);
  grThytau0p5ns->SetLineWidth(2);
  grObstau5ns->SetLineWidth(2);
  grObstau1ns->SetLineWidth(2);
  grObstau0p5ns->SetLineWidth(2);
  grExptau5ns->SetLineWidth(2);
  grExptau1ns->SetLineWidth(2);
  grExptau0p5ns->SetLineWidth(2);
  
  setAxes(grExptau5ns);
  setAxes(grExptau1ns);
  setAxes(grExptau0p5ns);
  grExptau0p5ns->SetMaximum(2); 
  // grExptau1ns->SetMaximum(5.e-1); 

  grExptau0p5ns->SetTitle(";m_{#chi} (GeV);#sigma (pp #rightarrow #chi #chi) (pb), #tau = 0.5 ns");
  grExptau1ns  ->SetTitle(";m_{#chi} (GeV);#sigma (pp #rightarrow #chi #chi) (pb), #tau = 1 ns");
  grExptau5ns  ->SetTitle(";m_{#chi} (GeV);#sigma (pp #rightarrow #chi #chi) (pb), #tau = 5 ns");

  
  TGraph *bandtau5nsErr1Sig = new TGraph(2*nbins);
  TGraph *bandtau5nsErr2Sig = new TGraph(2*nbins);
  TGraph *bandtau1nsErr1Sig = new TGraph(2*nbins);
  TGraph *bandtau1nsErr2Sig = new TGraph(2*nbins);
  TGraph *bandtau0p5nsErr1Sig = new TGraph(2*nbins);
  TGraph *bandtau0p5nsErr2Sig = new TGraph(2*nbins);

  for (int i=0; i<nbins; i++) {
    bandtau5nsErr1Sig->SetPoint(i,       m[i],         xsecExptau5nsBand1SigHi[i]);
    bandtau5nsErr2Sig->SetPoint(i,       m[i],         xsecExptau5nsBand2SigHi[i]);
    bandtau1nsErr1Sig->SetPoint(i,       m[i],         xsecExptau1nsBand1SigHi[i]);
    bandtau1nsErr2Sig->SetPoint(i,       m[i],         xsecExptau1nsBand2SigHi[i]);
    bandtau0p5nsErr1Sig->SetPoint(i,       m[i],         xsecExptau0p5nsBand1SigHi[i]);
    bandtau0p5nsErr2Sig->SetPoint(i,       m[i],         xsecExptau0p5nsBand2SigHi[i]);
  }
  for (int i=0; i<nbins; i++) {
    bandtau5nsErr1Sig->SetPoint(i+nbins, m[nbins-i-1], xsecExptau5nsBand1SigLo[nbins-i-1]);
    bandtau5nsErr2Sig->SetPoint(i+nbins, m[nbins-i-1], xsecExptau5nsBand2SigLo[nbins-i-1]);
    bandtau1nsErr1Sig->SetPoint(i+nbins, m[nbins-i-1], xsecExptau1nsBand1SigLo[nbins-i-1]);
    bandtau1nsErr2Sig->SetPoint(i+nbins, m[nbins-i-1], xsecExptau1nsBand2SigLo[nbins-i-1]);
    bandtau0p5nsErr1Sig->SetPoint(i+nbins, m[nbins-i-1], xsecExptau0p5nsBand1SigLo[nbins-i-1]);
    bandtau0p5nsErr2Sig->SetPoint(i+nbins, m[nbins-i-1], xsecExptau0p5nsBand2SigLo[nbins-i-1]);
  }
  bandtau5nsErr1Sig->SetPoint(2*nbins,   m[0], xsecExptau5nsBand1SigHi[0]); 
  bandtau5nsErr2Sig->SetPoint(2*nbins,   m[0], xsecExptau5nsBand2SigHi[0]); 
  bandtau1nsErr1Sig->SetPoint(2*nbins,   m[0], xsecExptau1nsBand1SigHi[0]); 
  bandtau1nsErr2Sig->SetPoint(2*nbins,   m[0], xsecExptau1nsBand2SigHi[0]); 
  bandtau0p5nsErr1Sig->SetPoint(2*nbins,   m[0], xsecExptau0p5nsBand1SigHi[0]); 
  bandtau0p5nsErr2Sig->SetPoint(2*nbins,   m[0], xsecExptau0p5nsBand2SigHi[0]); 

  bandtau5nsErr1Sig->SetFillColor(kGreen);
  bandtau1nsErr1Sig->SetFillColor(kGreen);
  bandtau0p5nsErr1Sig->SetFillColor(kGreen);
  bandtau5nsErr2Sig->SetFillColor(kYellow);
  bandtau1nsErr2Sig->SetFillColor(kYellow);
  bandtau0p5nsErr2Sig->SetFillColor(kYellow);

  bandtau0p5nsErr1Sig->SetLineStyle(2);  
  bandtau0p5nsErr2Sig->SetLineStyle(2);  
  bandtau0p5nsErr1Sig->SetLineWidth(2);  
  bandtau0p5nsErr2Sig->SetLineWidth(2);  


  //  grExptau1ns->Draw("ALP");
  for (int i=0; i<nbins; i++) {
    grExptau0p5ns->SetPointError(i, 0, 0, 0, 0);
    grExptau1ns->SetPointError(i, 0, 0, 0, 0);
    grExptau5ns->SetPointError(i, 0, 0, 0, 0);
  }

  TPaveText* pt = new TPaveText(0.55, 0.82, 0.95, 0.88, "NDC");  
  pt->SetFillStyle(0);
  pt->SetBorderSize(0);
  pt->SetTextFont(gStyle->GetTitleFont());
  pt->AddText("CMS Preliminary, 16.6 fb^{-1} at #sqrt{s} = 8 TeV");

  c1->SetLogy(1);
  c1->Update();
  

  // ********************************
  // Make plot for tau = 0.5ns.  
  // ********************************
    
  grExptau0p5ns->Draw("ALP");
  bandtau0p5nsErr2Sig->Draw("f, same");
  bandtau0p5nsErr1Sig->Draw("f, same");
  grExptau0p5ns->Draw("CP, same"); 
  grObstau0p5ns->Draw("CP, same");
  grThytau0p5ns->Draw("C, same");  
  pt->Draw();

  TLegend leg1(0.49, 0.20, 0.93, 0.45); 
  leg1.AddEntry(grThytau0p5ns, "Pythia 6.4", "l");
  leg1.AddEntry(grObstau0p5ns, "observed 95% C.L.", "l");
  leg1.AddEntry(bandtau0p5nsErr1Sig, "expected 95% C.L. #pm1 #sigma", "lf");
  leg1.AddEntry(bandtau0p5nsErr2Sig, "expected 95% C.L. #pm2 #sigma", "lf");
  leg1.SetTextFont(gStyle->GetTitleFont());
  leg1.SetBorderSize(0);
  leg1.SetFillStyle(1001);
  leg1.SetFillColor(kWhite);
  leg1.Draw();
  
  // FIXME:  Write out plots to directory:  
  // plots/AN-11-530/  
  c1->Print("XSec-tau0p5ns.pdf");  
  c1->Clear();

  // ********************************
  // Make plot for tau = 1ns.  
  // ********************************
  grExptau1ns->Draw("ALP");
  bandtau1nsErr2Sig->Draw("f, same");
  bandtau1nsErr1Sig->Draw("f, same");
  grExptau1ns->Draw("CP, same");
  grObstau1ns->Draw("CP, same");
  grThytau1ns->Draw("C, same");

  TLegend leg2(0.49, 0.56, 0.93, 0.81);
  leg2.AddEntry(grThytau1ns, "Pythia 6.4", "l");  
  leg2.AddEntry(grObstau1ns, "observed 95% C.L.", "l");
  leg2.AddEntry(bandtau0p5nsErr1Sig, "expected 95% C.L. #pm1 #sigma", "lf");
  leg2.AddEntry(bandtau0p5nsErr2Sig, "expected 95% C.L. #pm2 #sigma", "lf");
  leg2.SetTextFont(gStyle->GetTitleFont());
  leg2.SetBorderSize(0);
  leg2.SetFillStyle(0);
  leg2.Draw();
  pt->Draw();
  
  c1->Print("XSec-tau1ns.pdf");  
  c1->Clear();


  // ********************************
  // Make plot for tau = 5ns.  
  // ********************************
  grExptau5ns->Draw("ALP");
  bandtau5nsErr2Sig->Draw("f, same");
  bandtau5nsErr1Sig->Draw("f, same");
  grExptau5ns->Draw("CP, same");
  grObstau5ns->Draw("CP, same");
  grThytau5ns->Draw("C, same");

  TLegend leg3(0.49, 0.56, 0.93, 0.81);
  leg3.AddEntry(grThytau5ns, "Pythia 6.4", "l");  
  leg3.AddEntry(grObstau5ns, "observed 95% C.L.", "l");
  leg3.AddEntry(bandtau0p5nsErr1Sig, "expected 95% C.L. #pm1 #sigma", "lf");
  leg3.AddEntry(bandtau0p5nsErr2Sig, "expected 95% C.L. #pm2 #sigma", "lf");
  leg3.SetTextFont(gStyle->GetTitleFont());
  leg3.SetBorderSize(0);
  leg3.SetFillStyle(0);
  leg3.Draw();
  pt->Draw();
  
  c1->Print("XSec-tau5ns.pdf");  
  c1->Clear();



  // ********************************
  // Make combined plot.  
  // ********************************
  grExptau1ns->Draw("ALP");
  bandtau1nsErr2Sig->Draw("f, same");
  bandtau1nsErr1Sig->Draw("f, same");
  grExptau1ns->Draw("CP, same");
  grObstau1ns->Draw("CP, same");

  grExptau0p5ns->Draw("LP, same");
  bandtau0p5nsErr2Sig->Draw("f, same");
  bandtau0p5nsErr1Sig->Draw("f, same");
  
  grExptau0p5ns->Draw("CP, same"); 
  grObstau0p5ns->Draw("CP, same");

  grThytau0p5ns->SetLineColor(kBlue);  
  grThytau0p5ns->SetLineStyle(4);  
  grThytau0p5ns->Draw("C, same");
  grThytau1ns->Draw("C, same");

  //  TLegend leg5(0.49, 0.56, 0.93, 0.81);
  TLegend leg5(0.44, 0.46, 0.93, 0.76);
  leg5.AddEntry(grThytau1ns, "L_{2/3}", "l");  
  leg5.AddEntry(grThytau0p5ns, "L_{1/3}", "l");  
  leg5.AddEntry(grObstau1ns, "observed 95% C.L.", "l");
  leg5.AddEntry(bandtau0p5nsErr1Sig, "expected 95% C.L. #pm1 #sigma", "lf");
  leg5.AddEntry(bandtau0p5nsErr2Sig, "expected 95% C.L. #pm2 #sigma", "lf");
  leg5.SetTextFont(gStyle->GetTitleFont());
  leg5.SetBorderSize(0);
  leg5.SetFillStyle(0);

  //  leg5.Draw();  /// comment out for referee response
  pt->Draw();

  TPaveText* pt2b = new TPaveText(0.18, 0.22, 0.28, 0.28, "NDC");
  pt2b->SetFillStyle(0);
  pt2b->SetBorderSize(0);
  pt2b->SetTextFont(gStyle->GetTitleFont());
  pt2b->AddText("q = 2/3");

  TPaveText* pt3b = new TPaveText(0.18, 0.48, 0.28, 0.54, "NDC");
  pt3b->SetFillStyle(0);
  pt3b->SetBorderSize(0);
  pt3b->SetTextFont(gStyle->GetTitleFont());
  pt3b->AddText("q = 1/3");
//   pt2b->Draw(); // comment out for PRL referee response
//   pt3b->Draw(); // comment out for PRL referee response

  
  c1->Print("XSec.pdf");  
  c1->Clear();

  cout << "Copy plots with this command: " << endl
       << "   scp XSec-*.pdf wulsin@lxplus.cern.ch:~/docs/cmsdocs/notes/AN-12-400/trunk/figures/" << endl  
       << "or: cp XSec-*.pdf                       ~/docs/cmsdocs/notes/AN-12-400/trunk/figures/" << endl;  

  return;

} 


void setAxes(TGraphAsymmErrors* gr) { 

   gr->SetMaximum(2); 
   //   gr->SetMinimum(0);
   gr->SetMinimum(0.01);

   gr->GetXaxis()->SetTitleOffset(1.2);
   gr->GetYaxis()->SetTitleOffset(1.0);
   
   gr->GetXaxis()->SetLimits(100,500);  
   
} 


