#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <utility>

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

void plot(const TString dir, const TString file,
          const unsigned int rebinFactorMet,
          const unsigned int rebinFactorTracks,
          const TString datasetLabel, const TString lumiLabel,
          const bool useMet90Trigger = false,
          const bool isMC = false,
          const bool doFit = true) {

  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);
  gStyle->SetOptTitle(0);

  TFile * fin;

  TString metHistName = "Met Plots/metNoMuLogX";
  TString trackHistName = isMC ? "Eventvariable Plots/leadTrackPt" : "Eventvariable Plots/leadMuonPt";

  TString metNumeratorDir = "METLegNumerator";
  TString metDenominatorDir = "METLegDenominator";

  TString trackNumeratorDir = isMC ? "TrackLegNumeratorWithTracksNoTrig" : "TrackLegNumeratorWithMuons";
  TString trackDenominatorDir = isMC ? "TrackLegDenominatorWithTracksNoTrig" : "TrackLegDenominatorWithMuons";

  if(useMet90Trigger) {
    metNumeratorDir = "MET90LegNumerator";

    trackNumeratorDir += "Met90";
    trackDenominatorDir += "Met90";

  }

  fin = TFile::Open(dir + "/" + file + ".root");

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
  trackBackgroundHist->GetXaxis()->SetTitle(isMC ? "Track p_{T} [GeV]" : "Muon p_{T} [GeV]");

  trackEfficiency->SetName("trackTriggerEfficiency");
  setStyle(trackEfficiency, kBlack, 20);

  trackBackgroundHist->Draw();
  trackEfficiency->Draw("P");
  pt_cmsPrelim->Draw("same");
  pt_lumi->Draw("same");
  pt_trackLeg->Draw("same");
  oneLine->Draw("same");

  TF1 * f0 = new TF1("f0", normCDF, 1.0e1, 1.0e3, 4);
  TF1 * f1 = new TF1("f1", normCDF, 1.0e1, 1.0e3, 4);

  TPaveText * pt_metFit = new TPaveText(0.159148, 0.689055, 0.342105, 0.774876, "brNDC");
  TPaveText * pt_trackFit = new TPaveText(0.160804,0.665423,0.322864,0.746269,"brNDC");

  if(doFit) {

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
  }

  c1->cd();
  if(doFit) {
    f0->SetNpx(10000);
    f0->Draw("same");
    pt_metFit->Draw("same");
  }
  TString metLegPlotName = dir + "/" + file + "_metLegEfficiency.pdf";
  if(useMet90Trigger) metLegPlotName = dir + "/" + file + "_metLegEfficiency_met90.pdf";
  c1->SaveAs(metLegPlotName);

  c2->cd();
  if(doFit) {
    f1->SetNpx(10000);
    f1->Draw("same");
    pt_trackFit->Draw("same");
  }
  TString trackLegPlotName = dir + "/" + file + "_trackLegEfficiency.pdf";
  if(useMet90Trigger) trackLegPlotName = dir + "/" + file + "_trackLegEfficiency_met90.pdf";
  c2->SaveAs(trackLegPlotName);

  TString outputFileName = dir + "/" + file + "_triggerEfficiencies.root";
  if(useMet90Trigger) outputFileName = dir + "/" + file + "_triggerEfficiencies_met90.root";
  TFile * fOutput = new TFile(outputFileName, "RECREATE");
  metEfficiency->Write("metLeg");
  if(doFit) {
    f0->Write("metLeg_fit");
    f1->Write("trackLeg_fit");
  }
  trackEfficiency->Write("trackLeg");
  fOutput->Close();

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

void compare(vector< pair<TString, TString> > filesAndLegends, TString legendHeader,
             TString outputFilePrefix, bool isMC = false) {

  vector<TFile*> openFiles;
  vector<TGraphAsymmErrors*> graphs_met;
  vector<TGraphAsymmErrors*> graphs_tracks;

  TLegend * leg = new TLegend(0.2, 0.6, 0.55, 0.85, legendHeader, "brNDC");
  leg->SetFillColor(0);
  leg->SetTextSize(0.028);

  for(unsigned int i = 0; i < filesAndLegends.size(); i++) {
    openFiles.push_back(new TFile(filesAndLegends[i].first));
    graphs_met.push_back((TGraphAsymmErrors*)openFiles[i]->Get("metLeg"));
    graphs_tracks.push_back((TGraphAsymmErrors*)openFiles[i]->Get("trackLeg"));

    leg->AddEntry(graphs_met[i], filesAndLegends[i].second, "L");
  }

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
  metBackgroundHist->Draw();

  for(unsigned int i = 0; i < filesAndLegends.size(); i++) {
    graphs_met[i]->SetLineColor(i+1);
    graphs_met[i]->SetMarkerColor(i+1);
    graphs_met[i]->SetMarkerSize(0.5);
    graphs_met[i]->SetLineWidth(2);
    graphs_met[i]->Draw("L same");
  }
  leg->Draw("same");

  c1->SaveAs("compareMetLeg_" + outputFilePrefix + ".pdf");

  c2->cd();

  TH1D * trackBackgroundHist = new TH1D("trackBackgroundHist", "trackBackgroundHist", 1, xlo, xhi);
  trackBackgroundHist->GetYaxis()->SetTitle("Trigger Efficiency");
  trackBackgroundHist->GetYaxis()->SetRangeUser(ylo, yhi);
  trackBackgroundHist->GetXaxis()->SetTitle(isMC ? "Track p_{T} [GeV]" : "Muon p_{T} [GeV]");
  trackBackgroundHist->Draw();

  for(unsigned int i = 0; i < filesAndLegends.size(); i++) {
    graphs_tracks[i]->SetLineColor(i+1);
    graphs_tracks[i]->SetMarkerColor(i+1);
    graphs_tracks[i]->SetMarkerSize(0.5);
    graphs_tracks[i]->SetLineWidth(2);
    graphs_tracks[i]->Draw("L same");
  }
  leg->Draw("same");

  c2->SaveAs("compareTrackLeg_" + outputFilePrefix + ".pdf");

  for(unsigned int i = 0; i < filesAndLegends.size(); i++) {
    openFiles[i]->Close();
  }

}

void plotTriggerTurnOn() {

  double lumi_2015D = 2669.752;

  // Prompt JSONs

  double lumi_2016B = 5733.079;
  double lumi_2016C = 2573.399;
  double lumi_2016D = 4071.484;
  double lumi_2016E = 4009.132;
  double lumi_2016F = 3092.106;
  double lumi_2016G = 7540.488;
  double lumi_2016H = 8390.540 + 215.149;

  double lumi_2016 = lumi_2016B + lumi_2016C + lumi_2016D + lumi_2016E + lumi_2016F + lumi_2016G + lumi_2016H;

  // plot(directory, fileName,
  //      rebinFactorMet, rebinFactorTracks,
  //      datasetLabel, lumiLabel,
  //      useMet90Trigger = false
  //      isMC = false,
  //      doFit = true)

  // 2016 BC

  plot("condor/2016_final/triggerEfficiency", "SingleMu_2016BC",
       10, 10,
       "2016 B+C", Form("%.2f fb^{-1}, 13 TeV", lumi_2016B + lumi_2016C),
       false,
       false,
       false);

  // HLT_MET90_IsoTrk50_v
  plot("condor/2016_final/triggerEfficiency", "SingleMu_2016BC",
      10, 10,
      "2016 B+C", Form("%.2f fb^{-1}, 13 TeV", lumi_2016B + lumi_2016C),
      true, // use met90
      false,
      false);

  // 2016 DEFGH

  plot("condor/2016_final/triggerEfficiency", "SingleMu_2016DEFGH",
       10, 10,
       "2016 D-H", Form("%.2f fb^{-1}, 13 TeV", lumi_2016D + lumi_2016E + lumi_2016F + lumi_2016G + lumi_2016H),
       false,
       false,
       false);

  // HLT_MET90_IsoTrk50_v
  plot("condor/2016_final/triggerEfficiency", "SingleMu_2016DEFGH",
      10, 10,
      "2016 D-H", Form("%.2f fb^{-1}, 13 TeV", lumi_2016D + lumi_2016E + lumi_2016F + lumi_2016G + lumi_2016H),
      true, // use met90
      false,
      false);

  // Now compare files as desired

  vector< pair<TString, TString> > filesAndLegends;

  // compare MET75 to MET90 in BC
  filesAndLegends.push_back(make_pair("condor/2016_final/triggerEfficiency/SingleMu_2016BC_triggerEfficiencies.root", "HLT_MET75_IsoTrk50_v*"));
  filesAndLegends.push_back(make_pair("condor/2016_final/triggerEfficiency/SingleMu_2016BC_triggerEfficiencies_met90.root", "HLT_MET90_IsoTrk50_v*"));
  compare(filesAndLegends, "SingleMu 2016 B+C", "BC_75to90");

  filesAndLegends.clear();

  // compare MET75 to MET90 in DEFG
  filesAndLegends.push_back(make_pair("condor/2016_final/triggerEfficiency/SingleMu_2016DEFGH_triggerEfficiencies.root", "HLT_MET75_IsoTrk50_v*"));
  filesAndLegends.push_back(make_pair("condor/2016_final/triggerEfficiency/SingleMu_2016DEFGH_triggerEfficiencies_met90.root", "HLT_MET90_IsoTrk50_v*"));
  compare(filesAndLegends, "SingleMu 2016 D-H", "DEFG_75to90");

  filesAndLegends.clear();

}
