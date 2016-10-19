#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

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

const int NBINS = 100;

const double xlo = 9.0;
const double xhi = 1100.0;

const double ylo = 0.0;
const double yhi = 1.5;

using namespace std;

void invert(TH1D * const);
template<class T> void setStyle(T * const, const int, const int, const int = 1);
double normCDF(double *, double *);
void foldHistogram(TH1D *, bool);
void logSpace(const unsigned, const double, const double, vector<double> &);

void plot(const TString file,
          const unsigned int rebinFactorMet,
          const unsigned int rebinFactorTracks,
          const TString datasetLabel, const TString lumiLabel,
          const bool useTracks = false,
          const bool doFit = true) {

  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);
  gStyle->SetOptTitle(0);

  TFile * fin;

  TString metHistName = "Met Plots/metNoMu";
  TString trackHistName = useTracks ? "Eventvariable Plots/leadTrackPt" : "Eventvariable Plots/leadMuonPt";

  TString metNumeratorDir = "METLegNumerator";
  TString metDenominatorDir = "METLegDenominator";

  TString trackNumeratorDir = useTracks ? "TrackLegNumeratorWithTracksLeadHLTMatch" : "TrackLegNumeratorWithMuonsLeadHLTMatch";
  TString trackDenominatorDir = useTracks ? "TrackLegDenominatorWithTracks" : "TrackLegDenominatorWithMuons";

  fin = TFile::Open(file);

  TH1D * metNumerator =(TH1D*)fin->Get(metNumeratorDir + "Plotter/" + metHistName);
  TH1D * metDenominator =(TH1D*)fin->Get(metDenominatorDir + "Plotter/" + metHistName);

  TH1D * trackNumerator =(TH1D*)fin->Get(trackNumeratorDir + "Plotter/" + trackHistName);
  TH1D * trackDenominator =(TH1D*)fin->Get(trackDenominatorDir + "Plotter/" + trackHistName);

  metNumerator->SetDirectory(0);
  metDenominator->SetDirectory(0);
  trackNumerator->SetDirectory(0);
  trackDenominator->SetDirectory(0);

  fin->Close();

/*
  vector<double> bins;
  logSpace(NBINS, 1.0, 3.0, bins);

  metNumerator->Rebin(bins.size() - 1, "metLegNumerator", bins.data());
  metDenominator->Rebin(bins.size() - 1, "metLegDenominator", bins.data());

  trackNumerator->Rebin(bins.size() - 1, "trackLegNumerator", bins.data());
  trackDenominator->Rebin(bins.size() - 1, "trackLegDenominator", bins.data);
*/

  metNumerator->Rebin(rebinFactorMet);
  metDenominator->Rebin(rebinFactorMet);

  trackNumerator->Rebin(rebinFactorTracks);
  trackDenominator->Rebin(rebinFactorTracks);

  TGraphAsymmErrors * metEfficiency = new TGraphAsymmErrors(metNumerator, metDenominator, "cp");
  TGraphAsymmErrors * trackEfficiency = new TGraphAsymmErrors(trackNumerator, trackDenominator, "cp");

  TPaveText * pt_cmsPrelim = new TPaveText(0.132832, 0.859453, 0.486216, 0.906716, "brNDC");
  pt_cmsPrelim->SetBorderSize(0);
  pt_cmsPrelim->SetFillStyle(0);
  pt_cmsPrelim->SetTextFont(62);
  pt_cmsPrelim->SetTextSize(0.0374065);
  pt_cmsPrelim->AddText("CMS Preliminary");

  TPaveText * pt_lumi = new TPaveText(0.744361,0.92928,0.860902,0.977667,"brNDC");
  pt_lumi->SetBorderSize(0);
  pt_lumi->SetFillStyle(0);
  pt_lumi->SetTextFont(42);
  pt_lumi->SetTextSize(0.0374065);
  pt_lumi->AddText(lumiLabel);

  TPaveText * pt_metLeg = new TPaveText(0.160401,0.768657,0.342105,0.863184,"brNDC");
  pt_metLeg->SetBorderSize(0);
  pt_metLeg->SetFillStyle(0);
  pt_metLeg->SetTextFont(42);
  pt_metLeg->SetTextSize(0.0349127);
  pt_metLeg->SetTextAlign(12);
  pt_metLeg->AddText("hltMET75");
  pt_metLeg->AddText(datasetLabel);

  TPaveText * pt_trackLeg = new TPaveText(0.160401,0.768657,0.342105,0.863184,"brNDC");
  pt_trackLeg->SetBorderSize(0);
  pt_trackLeg->SetFillStyle(0);
  pt_trackLeg->SetTextFont(42);
  pt_trackLeg->SetTextSize(0.0349127);
  pt_trackLeg->SetTextAlign(12);
  pt_trackLeg->AddText("HLT_MET75_IsoTrk50_v*");
  pt_trackLeg->AddText(datasetLabel);
  pt_trackLeg->AddText("hltMET75 applied");

  TLine * oneLine = new TLine(xlo, 1.0, xhi, 1.0);
  oneLine->SetLineWidth(3);
  oneLine->SetLineStyle(2);

  TCanvas * c1 = new TCanvas("c1", "c1", 561, 482, 800, 830);
  c1->Range(0.644391, -0.1480839, 3.167468, 1.19299);
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetLogx();
  c1->SetTickx(1);
  c1->SetTicky(1);
  c1->SetLeftMargin(0.122807);
  c1->SetRightMargin(0.05012531);
  c1->SetTopMargin(0.06947891);
  c1->SetBottomMargin(0.1104218);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);

  TCanvas * c2 = new TCanvas("c2", "c2", 561, 482, 800, 830);
  c2->Range(0.644391, -0.1480839, 3.167468, 1.19299);
  c2->SetFillColor(0);
  c2->SetBorderMode(0);
  c2->SetBorderSize(2);
  c2->SetLogx();
  c2->SetTickx(1);
  c2->SetTicky(1);
  c2->SetLeftMargin(0.122807);
  c2->SetRightMargin(0.05012531);
  c2->SetTopMargin(0.06947891);
  c2->SetBottomMargin(0.1104218);
  c2->SetFrameFillStyle(0);
  c2->SetFrameBorderMode(0);
  c2->SetFrameFillStyle(0);
  c2->SetFrameBorderMode(0);

  c1->cd();

  TH1D * metBackgroundHist = new TH1D("metBackgroundHist", "metBackgroundHist", 1, xlo, xhi);
  metBackgroundHist->GetYaxis()->SetTitle("Trigger Efficiency");
  metBackgroundHist->GetYaxis()->SetRangeUser(ylo, yhi);
  metBackgroundHist->GetXaxis()->SetTitle("PF E_{T}^{miss} (no muons) [GeV]");

  metEfficiency->SetName("metTriggerEfficiency");
  setStyle(metEfficiency, kBlack, 20);

  metBackgroundHist->Draw();
  metEfficiency->Draw("P");
  pt_cmsPrelim->Draw("same");
  pt_lumi->Draw("same");
  pt_metLeg->Draw("same");
  oneLine->Draw("same");

  c2->cd();

  TH1D * trackBackgroundHist = new TH1D("trackBackgroundHist", "trackBackgroundHist", 1, xlo, xhi);
  trackBackgroundHist->GetYaxis()->SetTitle("Trigger Efficiency");
  trackBackgroundHist->GetYaxis()->SetRangeUser(ylo, yhi);
  trackBackgroundHist->GetXaxis()->SetTitle(useTracks ? "Track p_{T} [GeV]" : "Muon p_{T} [GeV]");

  trackEfficiency->SetName("trackTriggerEfficiency");
  setStyle(trackEfficiency, kBlack, 20);

  trackBackgroundHist->Draw();
  trackEfficiency->Draw("P");
  pt_cmsPrelim->Draw("same");
  pt_lumi->Draw("same");
  pt_trackLeg->Draw("same");
  oneLine->Draw("same");

  if (!doFit) return;

  TF1 * f0 = new TF1("f0", normCDF, 1.0e1, 1.0e3, 4);
  TF1 * f1 = new TF1("f1", normCDF, 1.0e1, 1.0e3, 4);

  f0->SetParameter(0, 75.0);
  f0->SetParLimits(0, 1.0e1, 1.0e3);
  f0->SetParameter(1, 5.0);
  f0->FixParameter(2, 0.99);
  f0->SetParLimits(2, 0.0, 1.0);
  f0->FixParameter(3, 0.01);
  f0->SetParLimits(3, 0.0, 1.0);

  f1->SetParameter(0, 50.0);
  f1->SetParLimits(0, 1.0e1, 1.0e3);
  f1->SetParameter(1, 1.0);
  f1->FixParameter(2, 0.85);
  f1->SetParLimits(2, 0.0, 1.0);
  f1->FixParameter(3, 0.0);
  f1->SetParLimits(3, 0.0, 1.0);

  for(unsigned i = 0; i < 100; i++) metEfficiency->Fit(f0, "emrq0");
  for(unsigned i = 0; i < 100; i++) trackEfficiency->Fit(f1, "emrq0");

  f0->ReleaseParameter(2);
  f0->ReleaseParameter(3);
  f1->ReleaseParameter(2);
  f1->ReleaseParameter(3);

  for(unsigned i = 0; i < 100; i++) metEfficiency->Fit(f0, "emrq0");
  metEfficiency->Fit(f0, "emr0");

  for(unsigned i = 0; i < 100; i++) trackEfficiency->Fit(f1, "emrq0");
  trackEfficiency->Fit(f1, "emr0");

  TPaveText * pt_metFit = new TPaveText(0.159148, 0.689055, 0.342105, 0.774876, "brNDC");
  pt_metFit->SetBorderSize(0);
  pt_metFit->SetFillStyle(0);
  pt_metFit->SetTextFont(42);
  pt_metFit->SetTextSize(0.0349127);
  pt_metFit->SetTextAlign(12);

  stringstream ss;
  ss.str("");
  ss << "#mu: (" << setprecision(3) << f0->GetParameter(0)
     << " #pm " << setprecision(2) << f0->GetParError(0)
     << ") GeV";
  pt_metFit->AddText(ss.str().c_str());

  ss.str("");
  ss << "#sigma: (" << setprecision(3) << f0->GetParameter(1)
     << " #pm " << setprecision(2) << f0->GetParError(1)
     << ") GeV";
  pt_metFit->AddText(ss.str().c_str());

  TPaveText * pt_trackFit = new TPaveText(0.160804,0.665423,0.322864,0.746269,"brNDC");
  pt_trackFit->SetBorderSize(0);
  pt_trackFit->SetFillStyle(0);
  pt_trackFit->SetTextFont(42);
  pt_trackFit->SetTextSize(0.0349127);
  pt_trackFit->SetTextAlign(12);

  ss.str("");
  ss << "#mu: (" << setprecision(3) << f1->GetParameter(0)
     << " #pm " << setprecision(2) << f1->GetParError(0)
     << ") GeV";
  pt_trackFit->AddText(ss.str().c_str());

  ss.str("");
  ss << "#sigma: (" << setprecision(3) << f1->GetParameter(1)
     << " #pm " << setprecision(2) << f1->GetParError(1)
     << ") GeV";
  pt_trackFit->AddText(ss.str().c_str());

  f0->SetLineWidth(3);
  f1->SetLineWidth(3);

  c1->cd();
  f0->SetNpx(10000);
  f0->Draw("same");
  pt_metFit->Draw("same");
  c1->SaveAs("condor/trigEff80X/metLeg.pdf");

  c2->cd();
  f1->SetNpx(10000);
  f1->Draw("same");
  pt_trackFit->Draw("same");
  c2->SaveAs("condor/trigEff80X/trackLeg.pdf");

}

void invert(TH1D * const h) {
  for(int i = 0; i <= h->GetXaxis()->GetNbins() + 1; i++) {
      double content = h->GetBinContent(i);
      double error = h->GetBinError(i);

      h->SetBinContent(i, 1.0 - content);
      h->SetBinError(i, error);
    }
}

template<class T> void setStyle(T * const h, const int color, const int markerStyle, const int lineStyle) {
  h->SetMarkerStyle(markerStyle);
  h->SetLineStyle(lineStyle);
  h->SetMarkerSize(1.5);
  h->SetLineWidth(1);
  h->SetMarkerColor(color);
  h->SetLineColor(color);

  h->GetXaxis()->SetLabelSize(0.04);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetXaxis()->SetTitleOffset(1.25);

  h->GetYaxis()->SetLabelSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.5);
  h->GetYaxis()->SetRangeUser(ylo, yhi);
}

double normCDF(double * x, double * par) {
  return(0.5 * par[2] * (1.0 + TMath::Erf((x[0] - par[0]) / (sqrt(2) * par[1]))) + par[3]);
}

void foldHistogram(TH1D * h, bool zeroNegative) {
  for(int i = 1; i <= h->GetXaxis()->GetNbins(); i++) {
      double x = h->GetXaxis()->GetBinCenter(i),
             content = h->GetBinContent(i),
             negContent = h->GetBinContent(h->GetXaxis()->FindBin(-x)),
             error = h->GetBinError(i),
             negError = h->GetBinError(h->GetXaxis()->FindBin(-x));
      if(x < 0.0) continue;
      else {
        h->SetBinContent(i, content + negContent);
        h->SetBinError(i, hypot(error, negError));
      }
    }

  for(int i = 1; zeroNegative && i <= h->GetXaxis()->GetNbins(); i++) {
      double x = h->GetXaxis()->GetBinCenter(i);
      if(x < 0.0) {
        h->SetBinContent(i, 0.0);
        h->SetBinError(i, 1.0e-12);
      }
    }
}

void logSpace(const unsigned n, const double a, const double b, vector<double> &bins) {

  double step =(b - a) /((double) n);

  bins.clear();
  for(double i = a; i < b + 0.5 * step; i += step)
    bins.push_back(pow(10.0, i));
}

void plotTriggerTurnOnForData() {

  plot("condor/trigEff80X/SingleMu_2016.root", 10, 10, "2016 B-G", "28.6 fb^{-1}, 13 TeV");

}
