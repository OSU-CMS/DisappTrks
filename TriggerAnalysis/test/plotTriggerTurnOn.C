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

#define NBINS 30
#define YMAX 1.5

using namespace std;

void invert (TH1D * const);
template<class T> void setStyle (T * const, const int, const int, const int = 1);
double normCDF (double *, double *);
void foldHistogram (TH1D *, bool);
void logSpace (const unsigned, const double, const double, vector<double> &);

void
plot (const string &mass, const string &ctau, const string &metTrigger, const string &metTriggerLabel = "", const bool useHLTUser = false, const bool effOnL1 = false, const bool useCaloMET = false, const bool doFit = true)
{
  gStyle->SetOptStat (0);

  TFile *fin;
  map<string, TH1D *> triggerEfficiencyNumerator, triggerEfficiencyDenominator;
  string histName = (useCaloMET ? "caloMetPt" : "metPt");
  string suffix = (useHLTUser ? "_User" : "");
  string  metNumeratorDir    =  (effOnL1  ?  "MuMETNoMETL1SeedPlotter"                 :  "MuMETNoMETPlotter");
  string  metDenominatorDir  =  (effOnL1  ?  "MuMETNoMETPlotter/hltL1sL1ETM60ORETM70"  :  "MuMETNoMETNoTriggerPlotter");

  fin = TFile::Open (("AMSB_chargino" + mass + "GeV_ctau" + ctau + "cm_step4" + suffix + ".root").c_str ());
  //fin = TFile::Open (("AMSB_chargino" + mass + "GeV_ctau" + ctau + "cm_step4_missHitsMid.root").c_str ());
  triggerEfficiencyNumerator["WJets_MET"] = (TH1D *) fin->Get (("TriggerEfficiency/" + metNumeratorDir + "/" + metTrigger + "/Met Plots/" + histName).c_str ());
  triggerEfficiencyNumerator.at ("WJets_MET")->SetDirectory (0);
  triggerEfficiencyDenominator["WJets_MET"] = (TH1D *) fin->Get (("TriggerEfficiency/" + metDenominatorDir + "/Met Plots/" + histName).c_str ());
  triggerEfficiencyDenominator.at ("WJets_MET")->SetDirectory (0);
  triggerEfficiencyNumerator["WJets_MuonPt"] = (TH1D *) fin->Get (("TriggerEfficiency/MuMETNoMuonPtPlotter/" + metTrigger + "/Muon Plots/muonPt").c_str ());
  triggerEfficiencyNumerator.at ("WJets_MuonPt")->SetDirectory (0);
  triggerEfficiencyDenominator["WJets_MuonPt"] = (TH1D *) fin->Get (("TriggerEfficiency/MuMETNoMuonPtNoTriggerPlotter/" + metTrigger + "/Muon Plots/muonPt").c_str ());
  triggerEfficiencyDenominator.at ("WJets_MuonPt")->SetDirectory (0);
  fin->Close ();

  map<string, TGraphAsymmErrors *> triggerEfficiency;
  for (map<string, TH1D *>::const_iterator design = triggerEfficiencyNumerator.begin (); design != triggerEfficiencyNumerator.end (); design++)
    {
      TH1D *numerator = NULL, *denominator = NULL;
      vector<double> bins;
      logSpace (NBINS, 1.0, 3.0, bins);
      numerator = (TH1D *) triggerEfficiencyNumerator.at (design->first)->Rebin (bins.size () - 1, "triggerEfficiencyNumerator", bins.data ());
      denominator = (TH1D *) triggerEfficiencyDenominator.at (design->first)->Rebin (bins.size () - 1, "triggerEfficiencyDenominator", bins.data ());
      //numerator = (TH1D *) triggerEfficiencyNumerator.at (design->first)->Clone ("triggerEfficiencyNumerator");
      //denominator = (TH1D *) triggerEfficiencyDenominator.at (design->first)->Clone ("triggerEfficiencyDenominator");
      triggerEfficiency[design->first] = new TGraphAsymmErrors (numerator, denominator, "cp");
      triggerEfficiency.at (design->first)->SetName ("triggerEfficiency");
      triggerEfficiency.at (design->first)->GetYaxis ()->SetTitle ((effOnL1 ? "trigger efficiency on L1" : "trigger efficiency"));
      if (design->first == "WJets_MET")
        {
          setStyle (triggerEfficiency.at (design->first), kBlack, 20);
          triggerEfficiency.at (design->first)->GetXaxis ()->SetTitle (useCaloMET ? "uncorrected calo. E_{T}^{miss} [GeV]" : "PF E_{T}^{miss} [GeV]");
        }
      else if (design->first == "WJets_MuonPt")
        {
          setStyle (triggerEfficiency.at (design->first), kBlack, 20);
          triggerEfficiency.at (design->first)->GetXaxis ()->SetTitle ("track p_{T} [GeV]");
        }
    }

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

  TPaveText *pt3 = new TPaveText(0.160401,0.768657,0.342105,0.863184,"brNDC");
  pt3->SetBorderSize(0);
  pt3->SetFillStyle(0);
  pt3->SetTextFont(42);
  pt3->SetTextSize(0.0349127);
  pt3->SetTextAlign(12);
  pt3->AddText((metTriggerLabel == "" ? metTrigger : metTriggerLabel).c_str ());
  pt3->AddText(("AMSB #chi_{1}^{#pm} (" + mass + " GeV, " + ctau + " cm)").c_str ());

  TPaveText *pt4 = new TPaveText(0.160401,0.725124,0.343358,0.855721,"brNDC");
  //TPaveText *pt4 = new TPaveText(0.16792,0.664179,0.350877,0.829602,"brNDC");
  pt4->SetBorderSize(0);
  pt4->SetFillStyle(0);
  pt4->SetTextFont(42);
  pt4->SetTextSize(0.0349127);
  pt4->SetTextAlign(12);
  pt4->AddText("HLT_MET75_IsoTrk50_v1");
  //pt4->AddText("missing middle hits cut off");
  pt4->AddText(("AMSB #chi_{1}^{#pm} (" + mass + " GeV, " + ctau + " cm)").c_str ());
  pt4->AddText((metTriggerLabel == "" ? metTrigger : metTriggerLabel).c_str ());

  TCanvas *c1 = new TCanvas("c1", "c1",561,482,800,830);
  gStyle->SetOptFit(1);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  c1->Range(0.644391,-0.1480839,3.167468,1.19299);
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

  TCanvas *c2 = new TCanvas("c2", "c2",561,482,800,830);
  gStyle->SetOptFit(1);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  c2->Range(0.644391,-0.1480839,3.167468,1.19299);
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

  TGraphAsymmErrors *WJets_MET = NULL, *WJets_MuonPt = NULL;

  c1->cd ();
  (WJets_MET = (TGraphAsymmErrors *) triggerEfficiency.at ("WJets_MET")->Clone ())->Draw ("ap");
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  WJets_MET->GetYaxis ()->SetRangeUser (0.0, YMAX);

  c2->cd ();
  (WJets_MuonPt = (TGraphAsymmErrors *) triggerEfficiency.at ("WJets_MuonPt")->Clone ())->Draw ("ap");
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt4->Clone ()->Draw ("same");
  WJets_MuonPt->GetYaxis ()->SetRangeUser (0.0, YMAX);

  TLine *l = new TLine (1.0e1, 1.0, 1.1e3, 1.0);
  l->SetLineWidth (3);
  l->SetLineStyle (2);

  c1->cd ();
  l->SetX1 (WJets_MET->GetXaxis ()->GetXmin ());
  l->SetX2 (WJets_MET->GetXaxis ()->GetXmax ());
  l->Clone ()->Draw ("same");

  c2->cd ();
  l->SetX1 (WJets_MuonPt->GetXaxis ()->GetXmin ());
  l->SetX2 (WJets_MuonPt->GetXaxis ()->GetXmax ());
  l->Clone ()->Draw ("same");

  if (!doFit)
    return;

  TF1 *f0 = new TF1 ("f0", normCDF, 1.0e1, 1.0e3, 4),
      *f1 = new TF1 ("f1", normCDF, 1.0e1, 1.0e3, 4);

  f0->SetParameter (0, 75.0);
  f0->SetParameter (1, 25.0);
  f0->FixParameter (2, 0.85 - 0.2);
  f0->FixParameter (3, 0.24);
  f1->SetParameter (0, 50.0);
  f1->SetParameter (1, 1.0);
  f1->FixParameter (2, 0.7);
  f1->FixParameter (3, 0.0);

  for (unsigned i = 0; i < 100; i++)
    triggerEfficiency.at ("WJets_MET")->Fit (f0, "emrq0");
  for (unsigned i = 0; i < 100; i++)
    triggerEfficiency.at ("WJets_MuonPt")->Fit (f1, "emrq0");

  f0->ReleaseParameter (2);
  f0->ReleaseParameter (3);
  f1->ReleaseParameter (2);
  f1->ReleaseParameter (3);

  for (unsigned i = 0; i < 100; i++)
    triggerEfficiency.at ("WJets_MET")->Fit (f0, "emrq0");
  triggerEfficiency.at ("WJets_MET")->Fit (f0, "emr0");
  for (unsigned i = 0; i < 100; i++)
    triggerEfficiency.at ("WJets_MuonPt")->Fit (f1, "emrq0");
  triggerEfficiency.at ("WJets_MuonPt")->Fit (f1, "emr0");

  stringstream ss0, ss1;

  TPaveText *pt5 = new TPaveText(0.159148,0.689055,0.342105,0.774876,"brNDC");
  pt5->SetBorderSize(0);
  pt5->SetFillStyle(0);
  pt5->SetTextFont(42);
  pt5->SetTextSize(0.0349127);
  pt5->SetTextAlign(12);
  ss0.str ("");
  ss0 << "#mu: (" << setprecision (3) << f0->GetParameter (0) << " #pm " << setprecision (2) << f0->GetParError (0) << ") GeV";
  pt5->AddText(ss0.str ().c_str ());
  ss0.str ("");
  ss0 << "#sigma: (" << setprecision (3) << f0->GetParameter (1) << " #pm " << setprecision (2) << f0->GetParError (1) << ") GeV";
  pt5->AddText(ss0.str ().c_str ());

  TPaveText *pt6 = new TPaveText(0.602757,0.773632,0.764411,0.855721,"brNDC");
  pt6->SetBorderSize(0);
  pt6->SetFillStyle(0);
  pt6->SetTextFont(42);
  pt6->SetTextSize(0.0349127);
  pt6->SetTextAlign(12);
  ss1.str ("");
  ss1 << "#mu: (" << setprecision (3) << f1->GetParameter (0) << " #pm " << setprecision (2) << f1->GetParError (0) << ") GeV";
  pt6->AddText(ss1.str ().c_str ());
  ss1.str ("");
  ss1 << "#sigma: (" << setprecision (3) << f1->GetParameter (1) << " #pm " << setprecision (2) << f1->GetParError (1) << ") GeV";
  pt6->AddText(ss1.str ().c_str ());

  f0->SetLineWidth (3);
  f1->SetLineWidth (3);

  c1->cd ();
  f0->Clone ()->Draw ("same");
  pt5->Clone ()->Draw ("same");
  c2->cd ();
  f1->Clone ()->Draw ("same");
  pt6->Clone ()->Draw ("same");
}

void
invert (TH1D * const h)
{
  for (int i = 0; i <= h->GetXaxis ()->GetNbins () + 1; i++)
    {
      double content = h->GetBinContent (i),
             error = h->GetBinError (i);

      h->SetBinContent (i, 1.0 - content);
      h->SetBinError (i, error);
    }
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
  h->GetXaxis ()->SetTitleOffset (1.25);

  h->GetYaxis ()->SetLabelSize (0.04);
  h->GetYaxis ()->SetTitleSize (0.04);
  h->GetYaxis ()->SetTitleOffset (1.5);
  h->GetYaxis ()->SetRangeUser (0.0, YMAX);
}

double
normCDF (double *x, double *par)
{
  return (0.5 * par[2] * (1.0 + TMath::Erf ((x[0] - par[0]) / (sqrt (2) * par[1]))) + par[3]);
}
  
void
foldHistogram (TH1D *h, bool zeroNegative)
{
  for (int i = 1; i <= h->GetXaxis ()->GetNbins (); i++)
    {
      double x = h->GetXaxis ()->GetBinCenter (i),
             content = h->GetBinContent (i),
             negContent = h->GetBinContent (h->GetXaxis ()->FindBin (-x)),
             error = h->GetBinError (i),
             negError = h->GetBinError (h->GetXaxis ()->FindBin (-x));
      if (x < 0.0)
        continue;
      else
        {
          h->SetBinContent (i, content + negContent);
          h->SetBinError (i, hypot (error, negError));
        }
    }
  for (int i = 1; zeroNegative && i <= h->GetXaxis ()->GetNbins (); i++)
    {
      double x = h->GetXaxis ()->GetBinCenter (i);
      if (x < 0.0)
        h->SetBinContent (i, 0.0);
        h->SetBinError (i, 1.0e-12);
    }
}

void
logSpace (const unsigned n, const double a, const double b, vector<double> &bins)
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}
