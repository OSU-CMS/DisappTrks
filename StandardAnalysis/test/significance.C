#include <iostream>
#include <iomanip>
#include <vector>
using std::cout;
using std::endl;

#include "TROOT.h"
#include "TCanvas.h"
#include "TChain.h"
#include "TCut.h"
#include "TF1.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2F.h"
#include "THStack.h"
#include "TLegend.h"
#include "TLine.h"
#include "TPaveText.h"
#include "TStopwatch.h"
#include "TString.h"
#include "TStyle.h"
#include "TTree.h"

//#include "/afs/cern.ch/user/w/wulsin/root/tdrstyle.C"

#ifndef __CINT__
#endif

// ----------------------------------------------
// -- Global variables                         --
// -- Set these when running randomCommands(). --
// ----------------------------------------------
TString inDir_ = "sigStudies/inputPlots/";
TString outdir = "sigStudies/outputPlots/";
TCanvas* can;

// -------------------------
// -- Function prototypes --
// -------------------------
void significance();
void getSig();

// -------------------------
// -- Functions           --
// -------------------------

void significance() {



  cout << "Beginning significance()." << endl;


  system("mkdir -p " + outdir);

  can = new TCanvas("can", "can");
  can->Print(outdir+"significance.ps[");

  can->SetRightMargin(0.13);
  can->SetLogx(1);

  getSig();

  // Close the output file
  can->Print(outdir+"significance.ps]");
  system("ps2pdf " + outdir+"significance.ps");
  system("mv significance.pdf " + outdir);

  cout << "Wrote plots to:  " << outdir << "significance.pdf" << endl;


}

void getSig(){

    TFile* fSig0p5ns     = new TFile(inDir_+"AMSB_mGrav50K_0p5ns_Reco.root", "READ");
    TFile* fSig1ns       = new TFile(inDir_+"AMSB_mGrav50K_1ns_Reco.root", "READ");
    TFile* fSig5ns       = new TFile(inDir_+"AMSB_mGrav50K_5ns_Reco.root", "READ");

    TFile* fBkgd         = new TFile(inDir_+"Background.root", "READ");

  TH1D* hCaloSig0p5ns;
  TH1D* hCaloSig1ns;
  TH1D* hCaloSig5ns;

  TH1D* hCaloBkgd;
  TH1D* hCaloSignif0p5ns = new TH1D("hCaloSignif0p5ns",          "Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (PU corr.)", 100, 0,100 );
  TH1D* hCaloSignif1ns = new TH1D("hCaloSignif1ns",          "Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (PU corr.)", 100, 0,100 );
  TH1D* hCaloSignif5ns = new TH1D("hCaloSignif5ns",          "Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (PU corr.)", 100, 0,100 );

  TH1D* hPtSig0p5ns;
  TH1D* hPtSig1ns;
  TH1D* hPtSig5ns;

  TH1D* hPtBkgd;

  TH1D* hPtSignif0p5ns = new TH1D("hPtSignif0p5ns",          "Track Transverse Momentum; p_{T} [GeV]", 100, 0,500 );
  TH1D* hPtSignif1ns   = new TH1D("hPtSignif1ns",          "Track Transverse Momentum; p_{T} [GeV]", 100, 0,500 );
  TH1D* hPtSignif5ns   = new TH1D("hPtSignif5ns",          "Track Transverse Momentum; p_{T} [GeV]", 100, 0,500 );

  fSig0p5ns    ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/caloTot_RhoCorr", hCaloSig0p5ns);
  fSig1ns      ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/caloTot_RhoCorr", hCaloSig1ns);
  fSig5ns      ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/caloTot_RhoCorr", hCaloSig5ns);
  fBkgd        ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/caloTot_RhoCorr", hCaloBkgd);

  fSig0p5ns    ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/trackPt", hPtSig0p5ns);
  fSig1ns      ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/trackPt", hPtSig1ns);
  fSig5ns      ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/trackPt", hPtSig5ns);
  fBkgd        ->GetObject("OSUAnalysis/PreSelectionPMissingWithTrigJetMet/trackPt", hPtBkgd);

  if (!hCaloSig0p5ns) { cout << "Error:  hist hCaloSig0p5ns not found." << endl; return; }
  if (!hCaloSig1ns)   { cout << "Error:  hist hCaloSig1ns not found."   << endl; return; }
  if (!hCaloSig5ns)   { cout << "Error:  hist hCaloSig5ns not found."   << endl; return; }
  if (!hPtSig0p5ns)   { cout << "Error:  hist hPtSig0p5ns not found."   << endl; return; }
  if (!hPtSig1ns)     { cout << "Error:  hist hPtSig1ns not found."     << endl; return; }
  if (!hPtSig5ns)     { cout << "Error:  hist hPtSig5ns not found."     << endl; return; }
  if (!hPtBkgd)       { cout << "Error:  hist hPtBkgd  not found."      << endl; return; }

  for (int i=0; i<(hCaloBkgd->GetNbinsX()); i++){
    double intS = hCaloSig0p5ns ->Integral(1, i);
    double intB = hCaloBkgd->Integral(1, i);
    double significance = intS / sqrt(intS + intB);

    hCaloSignif0p5ns->SetBinContent(i, significance);
  }

  for (int i=0; i<(hCaloBkgd->GetNbinsX()); i++){
    double intS = hCaloSig1ns ->Integral(1, i);
    double intB = hCaloBkgd->Integral(1, i);
    double significance = intS / sqrt(intS + intB);

    hCaloSignif1ns->SetBinContent(i, significance);
  }

  for (int i=0; i<(hCaloBkgd->GetNbinsX()); i++){
    double intS = hCaloSig5ns ->Integral(1, i);
    double intB = hCaloBkgd->Integral(1, i);
    double significance = intS / sqrt(intS + intB);

    hCaloSignif5ns->SetBinContent(i, significance);
  }

  for (int i=0; i<(hPtBkgd->GetNbinsX()); i++){
    double intS = hPtSig0p5ns ->Integral(i, 100);
    double intB = hPtBkgd->Integral(i, 100);
    double significance = intS / sqrt(intS + intB);

    hPtSignif0p5ns->SetBinContent(i, significance);
  }

  for (int i=0; i<(hPtBkgd->GetNbinsX()); i++){
    double intS = hPtSig1ns ->Integral(i, 100);
    double intB = hPtBkgd->Integral(i, 100);
    double significance = intS / sqrt(intS + intB);

    hPtSignif1ns->SetBinContent(i, significance);
  }

  for (int i=0; i<(hPtBkgd->GetNbinsX()); i++){
    double intS = hPtSig5ns ->Integral(i, 100);
    double intB = hPtBkgd->Integral(i, 100);
    double significance = intS / sqrt(intS + intB);

    hPtSignif5ns->SetBinContent(i, significance);
  }

  hCaloSignif0p5ns->SetLineColor(1);
  hCaloSig0p5ns->SetLineColor(2);
  hCaloBkgd->SetLineColor(4);

  hPtSignif0p5ns->SetLineColor(1);
  hPtSig0p5ns->SetLineColor(2);
  hPtBkgd->SetLineColor(4);


  hCaloSignif1ns->SetLineColor(1);
  hCaloSig1ns->SetLineColor(2);
  hCaloBkgd->SetLineColor(4);

  hPtSignif1ns->SetLineColor(1);
  hPtSig1ns->SetLineColor(2);
  hPtBkgd->SetLineColor(4);

  hCaloSignif5ns->SetLineColor(1);
  hCaloSig5ns->SetLineColor(2);
  hCaloBkgd->SetLineColor(4);

  hPtSignif5ns->SetLineColor(1);
  hPtSig5ns->SetLineColor(2);
  hPtBkgd->SetLineColor(4);


  TLegend *leg0p5 = new TLegend(0.65,0.5,0.95,0.7);
  leg0p5->SetFillColor(0);

  leg0p5->AddEntry(hCaloSig0p5ns,"#chi^{#pm}_{1}, #tau = 0.5ns");
  leg0p5->AddEntry(hCaloBkgd,"Total Background");
  leg0p5->AddEntry(hCaloSignif0p5ns,"#sigma = S/#sqrt{S+B}");

  TLegend *leg1 = new TLegend(0.65,0.5,0.95,0.7);
  leg1->SetFillColor(0);

  leg1->AddEntry(hCaloSig1ns,"#chi^{#pm}_{1}, #tau = 1ns");
  leg1->AddEntry(hCaloBkgd,"Total Background");
  leg1->AddEntry(hCaloSignif1ns,"#sigma = S/#sqrt{S+B}");


  TLegend *leg5 = new TLegend(0.65,0.5,0.95,0.7);
  leg5->SetFillColor(0);

  leg5->AddEntry(hCaloSig5ns,"#chi^{#pm}_{1}, #tau = 5ns");
  leg5->AddEntry(hCaloBkgd,"Total Background");
  leg5->AddEntry(hCaloSignif5ns,"#sigma = S/#sqrt{S+B}");


  can.SetLogx(0);
  hCaloSignif0p5ns->Draw("");
  hCaloBkgd->Draw("same");
  hCaloSig0p5ns->Draw("same");
  leg0p5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hCaloSig0p5ns->Draw("");
  hCaloSignif0p5ns->Draw("same");
  hCaloBkgd->Draw("same");
  leg0p5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();


  hCaloSignif1ns->Draw("");
  hCaloBkgd->Draw("same");
  hCaloSig1ns->Draw("same");
  leg1->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hCaloSig1ns->Draw("");
  hCaloSignif1ns->Draw("same");
  hCaloBkgd->Draw("same");
  leg1->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hCaloSignif5ns->Draw("");
  hCaloBkgd->Draw("same");
  hCaloSig5ns->Draw("same");
  leg5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hCaloSig5ns->Draw("");
  hCaloSignif5ns->Draw("same");
  hCaloBkgd->Draw("same");
  leg5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hPtSignif0p5ns->Draw("");
  hPtBkgd->Draw("same");
  hPtSig0p5ns->Draw("same");
  leg0p5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hPtBkgd->Draw("");
  hPtSignif0p5ns->Draw("same");
  hPtSig0p5ns->Draw("same");
  leg0p5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hPtSignif1ns->Draw("");
  hPtBkgd->Draw("same");
  hPtSig1ns->Draw("same");
  leg1->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hPtBkgd->Draw("");
  hPtSignif1ns->Draw("same");
  hPtSig1ns->Draw("same");
  leg1->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hPtSignif5ns->Draw("");
  hPtBkgd->Draw("same");
  hPtSig5ns->Draw("same");
  leg5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  hPtBkgd->Draw("");
  hPtSignif5ns->Draw("same");
  hPtSig5ns->Draw("same");
  leg5->Draw("same");
  can->Print(outdir+"significance.ps");
  can.Clear();

  cout << "Integral for hCaloSig0p5ns = " << hCaloSig0p5ns->Integral() << endl;
  cout << "Integral for hCaloSig1ns = "   << hCaloSig1ns->Integral()   << endl;
  cout << "Integral for hCaloSig5ns = "   << hCaloSig5ns->Integral()   << endl;
  cout << "Integral for hCaloBkgd = "     << hCaloBkgd->Integral()     << endl << endl;

  cout << "Integral for hPtSig0p5ns = "   << hPtSig0p5ns->Integral()   << endl;
  cout << "Integral for hPtSig1ns = "     << hPtSig1ns->Integral()     << endl;
  cout << "Integral for hPtSig5ns = "     << hPtSig5ns->Integral()     << endl;
  cout << "Integral for hPtBkgd = "       << hPtBkgd->Integral()       << endl << endl;



}
