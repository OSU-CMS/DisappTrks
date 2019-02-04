#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif

#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "RooGenericPdf.h"
#include "RooFormulaVar.h"
#include "RooFFTConvPdf.h"
#include "RooPlot.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "TH1.h"

using namespace RooFit;

enum {
  kEle2015,
  kEle2016BC,
  kEle2016DEFGH,
  kMu2015,
  kMu2016BC,
  kMu2016DEFGH,
  kNumCases
};

const TString directories[kNumCases] = {
  "/data/users/hart/condor/2015/stenson/electronBackground/SingleEle_2015D.root",
  "/data/users/hart/condor/2016_final_prompt/stenson/electronBackground/SingleEle_2016BC.root",
  "/data/users/hart/condor/2016_final_prompt/stenson/electronBackground/SingleEle_2016DEFGH.root",
  "/data/users/hart/condor/2015/stenson/muonBackground/SingleMu_2015D.root",
  "/data/users/hart/condor/2016_final_prompt/stenson/muonBackground/SingleMu_2016BC.root",
  "/data/users/hart/condor/2016_final_prompt/stenson/muonBackground/SingleMu_2016DEFGH.root"
};

const double maxYields[kNumCases] = {
  350000., // 338122 events
  700000., // 674985 events
  1.7e6,   // 1.67782e+06 events
  1.e6,    // 850231 events
  2.e6,    // 1.81361e+06 events
  7.e6    // 6.56916e+06 events
};
  
void zPeakFit(const int version = kEle2015) {
  
  TFile * input = new TFile(directories[version], "READ");
  TString plotDirectory = (version >= kMu2015) ? "ZtoMuProbeTrkPlotter/Track-muon Plots/" : "ZtoEleProbeTrkPlotter/Track-electron Plots/";
  TH1D * h_invmass = (TH1D*)input->Get(plotDirectory + "invMassNearZ");

  RooRealVar x("x", (version >= kMu2015) ? "M(#mu, probe track)" : "M(e, probe track)", 80, 100, "GeV");
  RooDataHist data("data", "dataset", x, h_invmass);

  ///////////////////////
  // background models
  ///////////////////////
  
  // RooCMSShape
  RooRealVar aBkg("aBkg", "aBkg", 85.0, 80.0, 90.0, "GeV"); // RooCMSShape (fixed)
  RooRealVar bBkg("bBkg", "bBkg", 0.22, 0.0, 0.5); // RooCMSShape (fixed)
  RooRealVar c("c", "c", 0.12, 0.0, 2.0); // RooCMSShape (fixed)
  RooRealVar zMass("bkgd peak", "zMass", 91., 80, 100, "GeV");
  RooCMSShape background("background", "background", x, aBkg, bBkg, c, zMass);
  RooRealVar backgroundYield("bkgd events", "bkgd events", 0.25 * maxYields[version], 0.0, maxYields[version]);
  
  ///////////////////////
  // signal/peak models
  ///////////////////////
  
  // Breit-Wigner for peak
  RooRealVar mRes("m_{Z^{0}}", "Z^{0} resonance mass", 90.9, 88.0, 92.0, "GeV");
  RooRealVar Gamma("#Gamma", "#Gamma", 2.0, 0.0, 3.2, "GeV");
  RooBreitWigner bw("bw", "Breit-Wigner Distribution", x, mRes, Gamma);

  // Crystal Ball for resolution
  RooRealVar cbmean("cb_mean", "cbmean", 0.0, -0.5, 0.5);
  RooRealVar cbsigma("cb_sigma", "cbsigma", 1.6, 0.8, 2.4);
  RooRealVar cbsig("signal events", "cbsignal", 0.75 * maxYields[version], 0.0, maxYields[version]);
  RooRealVar n("n", "n", 50.0, 0.0, 150.0);
  RooRealVar alpha("alpha", "alpha", 0.6, 0.2, 1.0);
  RooCBShape cball("cball", "Crystal Ball", x, cbmean, cbsigma, alpha, n);

  // Convolution of Breit-Wigner and Crystal Ball
  RooFFTConvPdf bw_cball("bw_cball", "Convolution", x, bw, cball);
  RooRealVar bw_cball_yield("signal events", "signal events", 0.75 * maxYields[version], 0.0, maxYields[version]);

  // Addition of bw_cball and linear
  RooAddPdf totalPDF("totalPDF", "totalPDF", RooArgList(background, bw_cball), RooArgList(backgroundYield, bw_cball_yield));

  // fit to data
  totalPDF.fitTo(data, Extended(kTRUE));

  // plot the results
  TCanvas * can = new TCanvas("can", "can", 10, 10, 1200, 800);
  
  RooPlot * xframe = x.frame(Title("Breit-Wigner #otimes Crystal Ball signal plus 2nd order polynomial background"));
  xframe->SetTitle("");
  totalPDF.paramOn(xframe, Format("NE", AutoPrecision(2)), Layout(0.6, 0.98, 0.95));
  data.plotOn(xframe, Name("data"), LineColor(kBlack));
  totalPDF.plotOn(xframe, Name("model"), LineColor(kBlue));
  totalPDF.plotOn(xframe, Components(background), LineColor(kRed), DrawOption("F"), FillColor(kRed));
  xframe->Draw();

  xframe->GetYaxis()->SetTitleOffset(1.3);

  can->SaveAs("plot.pdf");

  // print the contamination explicitly
  double fit_total = bw_cball_yield.getVal() + backgroundYield.getVal();
  double fit_total_error = TMath::Hypot(bw_cball_yield.getError(), backgroundYield.getError());

  double contamination = backgroundYield.getVal() / fit_total;
  double contamination_error = contamination * TMath::Hypot(backgroundYield.getError() / backgroundYield.getVal(), fit_total_error / fit_total);

  cout << endl << endl << "Fit value for background contamination: " << contamination << " +/- " << contamination_error << " %" << endl << endl;

  cout << "Fit chi2/ndof: " << xframe->chiSquare("model", "data", 12) << endl << endl;
  
}

