#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

#include "TROOT.h" 
#include "TFile.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TStyle.h"
#include "TGraphAsymmErrors.h"
#include "TF1.h"
#include "TMath.h"

#define YMAX 1.5

using namespace std;

template<class T> void setStyle (T * const, const int, const int, const int = 1);

void
plot ()
{
  gStyle->SetOptStat (0);

  gROOT->SetBatch();


  TH1D *denominator, *numerator, *numeratorNoPU;
  TH2D *caloTot, *passCaloTot, *passCaloTotNoPU;   

  TFile *fin;
  fin = TFile::Open ("test.root");
  denominator = (TH1D *) fin->Get ("PUDependence/nVertices");
  denominator->SetDirectory (0);
  numerator = (TH1D *) fin->Get ("PUDependence/isoTrack");
  numerator->SetDirectory (0);
  numeratorNoPU = (TH1D *) fin->Get ("PUDependence/isoNoPUTrack");
  numeratorNoPU->SetDirectory (0);
  caloTot = (TH2D *) fin->Get ("PUDependence/caloTot");
  caloTot->SetDirectory(0);
  passCaloTot = (TH2D *) fin->Get ("PUDependence/passCaloTot");
  passCaloTot->SetDirectory(0);
  passCaloTotNoPU = (TH2D *) fin->Get ("PUDependence/passCaloTotNoPU");
  passCaloTotNoPU->SetDirectory(0);
  fin->Close ();

  denominator->Rebin (4);
  numerator->Rebin (4);
  numeratorNoPU->Rebin (4);
  passCaloTot->Rebin(4);
  passCaloTotNoPU->Rebin(4);  

  TGraphAsymmErrors *puDependence, *puDependenceNoPU;
  puDependence = new TGraphAsymmErrors (numerator, denominator, "cp");
  puDependenceNoPU = new TGraphAsymmErrors (numeratorNoPU, denominator, "cp");
  puDependence->GetYaxis ()->SetTitle ("track iso. efficiency");
  puDependenceNoPU->GetYaxis ()->SetTitle ("track iso. efficiency");
  puDependence->GetXaxis ()->SetTitle ("number of primary vertices");
  puDependenceNoPU->GetXaxis ()->SetTitle ("number of primary vertices");

  setStyle (puDependence, kBlack, 24);
  setStyle (puDependenceNoPU, kBlack, 20);

  TGraphAsymmErrors *caloPuDependence, *caloPuDependenceNoPU;
  caloPuDependence = new TGraphAsymmErrors (passCaloTot, denominator, "cp");
  caloPuDependenceNoPU = new TGraphAsymmErrors (passCaloTotNoPU, denominator, "cp");
  caloPuDependence->GetYaxis ()->SetTitle ("E_{calo} < 10 GeV. efficiency");
  caloPuDependenceNoPU->GetYaxis ()->SetTitle ("E_{calo} < 10 GeV efficiency");
  caloPuDependence->GetXaxis ()->SetTitle ("number of primary vertices");
  caloPuDependenceNoPU->GetXaxis ()->SetTitle ("number of primary vertices");

  setStyle (caloPuDependence, kBlack, 24);
  setStyle (caloPuDependenceNoPU, kBlack, 20);

  TPaveText *pt1 = new TPaveText(0.229323,0.859453,0.581454,0.906716,"brNDC");
  pt1->SetBorderSize(0);
  pt1->SetFillStyle(0);
  pt1->SetTextFont(62);
  pt1->SetTextSize(0.0374065);
  pt1->AddText("CMS Simulation Preliminary");

  TPaveText *pt2 = new TPaveText(0.827068,0.92928,0.942356,0.977667,"brNDC");
  pt2->SetBorderSize(0);
  pt2->SetFillStyle(0);
  pt2->SetTextFont(42);
  pt2->SetTextSize(0.0374065);
  pt2->AddText("13 TeV");

  TPaveText *pt3 = new TPaveText(0.161654,0.787313,0.31203,0.880597,"brNDC");
  pt3->SetBorderSize(0);
  pt3->SetFillStyle(0);
  pt3->SetTextFont(42);
  pt3->SetTextSize(0.0349127);
  pt3->SetTextAlign(12);
  pt3->AddText("AMSB #tilde{#chi}_{1}^{#pm} (700 GeV, 1000 cm)");

  TLegend *leg = new TLegend (0.155388,0.726368,0.338346,0.809701,NULL,"brNDC");
  leg->SetBorderSize(0);
  leg->SetTextSize(0.0349127);
  leg->SetFillStyle(0);
  leg->AddEntry (puDependence, "without pileup subtraction", "p");
  leg->AddEntry (puDependenceNoPU, "with pileup subtraction", "p");

  TCanvas *c1 = new TCanvas("c1", "c1",565,246,800,830);
  gStyle->SetOptFit(1);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  c1->Range(0.644391,-0.1480839,3.167468,1.19299);
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetTickx(1);
  c1->SetTicky(1);
  c1->SetLeftMargin(0.122807);
  c1->SetRightMargin(0.0501253);
  c1->SetTopMargin(0.068408);
  c1->SetBottomMargin(0.0982587);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);

  map<string, TGraphAsymmErrors *> clones;

  c1->cd ();
  (clones["puDependence"] = (TGraphAsymmErrors *) puDependence->Clone ())->Draw ("ap");
  (clones["puDependenceNoPU"] = (TGraphAsymmErrors *) puDependenceNoPU->Clone ())->Draw ("p same");
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  clones.at ("puDependence")->GetYaxis ()->SetRangeUser (0.0, YMAX);
  clones.at ("puDependenceNoPU")->GetYaxis ()->SetRangeUser (0.0, YMAX);

  TLine *l = new TLine (0.0, 1.0, 100.0, 1.0);
  l->SetLineWidth (3);
  l->SetLineStyle (2);

  c1->cd ();
  l->SetX1 (min (clones.at ("puDependence")->GetXaxis ()->GetXmin (), clones.at ("puDependenceNoPU")->GetXaxis ()->GetXmin ()));
  l->SetX2 (max (clones.at ("puDependence")->GetXaxis ()->GetXmax (), clones.at ("puDependenceNoPU")->GetXaxis ()->GetXmax ()));
  l->Clone ()->Draw ("same");

  c1->SaveAs("puDependence.pdf[");  // start file
  c1->SaveAs("puDependence.pdf");   // add a page 

  c1->Clear();  
  c1->SetRightMargin(0.15);  
  caloTot->Draw("colz");  
  c1->SaveAs("puDependence.pdf");   // add a page 

  (clones["caloPuDependence"] = (TGraphAsymmErrors *) caloPuDependence->Clone ())->Draw ("ap");
  (clones["caloPuDependenceNoPU"] = (TGraphAsymmErrors *) caloPuDependenceNoPU->Clone ())->Draw ("p same");
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  clones.at ("caloPuDependence")->GetYaxis ()->SetRangeUser (0.0, YMAX);
  clones.at ("caloPuDependenceNoPU")->GetYaxis ()->SetRangeUser (0.0, YMAX);


  c1->cd ();
  l->SetX1 (min (clones.at ("caloPuDependence")->GetXaxis ()->GetXmin (), clones.at ("caloPuDependenceNoPU")->GetXaxis ()->GetXmin ()));
  l->SetX2 (max (clones.at ("caloPuDependence")->GetXaxis ()->GetXmax (), clones.at ("caloPuDependenceNoPU")->GetXaxis ()->GetXmax ()));
  l->Clone ()->Draw ("same");

  c1->SaveAs("puDependence.pdf");   // add a page 


  c1->SaveAs("puDependence.pdf]");   // close file 

}

template<class T> void
setStyle (T * const h, const int color, const int markerStyle, const int lineStyle)
{
  h->SetMarkerStyle (markerStyle);
  h->SetLineStyle (lineStyle);
  h->SetMarkerSize (1.5);
  h->SetLineWidth (1);
  h->SetMarkerColor (color);
  h->SetLineColor (color);

  h->GetXaxis ()->SetLabelSize (0.04);
  h->GetXaxis ()->SetTitleSize (0.04);
  h->GetXaxis ()->SetTitleOffset (1.0);

  h->GetYaxis ()->SetLabelSize (0.04);
  h->GetYaxis ()->SetTitleSize (0.04);
  h->GetYaxis ()->SetTitleOffset (1.5);
  h->GetYaxis ()->SetRangeUser (0.0, YMAX);
}
