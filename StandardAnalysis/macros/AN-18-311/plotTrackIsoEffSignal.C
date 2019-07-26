// Figure 15
void plotTrackIsoEffSignal() {

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);

  gStyle->SetPalette (kColorPrintableOnGrey);
  //gStyle->SetPalette (kInvertedDarkBodyRadiator);

  gStyle->SetLabelSize (0.04, "X");
  gStyle->SetLabelSize (0.04, "Y");
  gStyle->SetTitleSize (0.04, "X");
  gStyle->SetTitleSize (0.04, "Y");
  gStyle->SetLabelOffset (0.005, "X");
  gStyle->SetLabelOffset (0.005, "Y");
  gStyle->SetTitleOffset (1.0, "X");
  gStyle->SetTitleOffset (1.0, "Y"); // durp 1.0 normally
  gStyle->SetNdivisions (505, "X");
  gStyle->SetNdivisions (505, "Y");
  gStyle->SetPadTickX (1);
  gStyle->SetPadTickY (1);
  gStyle->SetMarkerSize (1.5);

  TFile * f_total = new TFile("condor/2017/anFig15beforeIsoCut_v2/AMSB_chargino_700GeV_1000cm_94X.root");
  TFile * f_with = new TFile("condor/2017/anFig15withPUSub_v2/AMSB_chargino_700GeV_1000cm_94X.root");
  TFile * f_without = new TFile("condor/2017/anFig15withoutPUSub_v2/AMSB_chargino_700GeV_1000cm_94X.root");

  TH1D * h_total = (TH1D*)f_total->Get("IsoTrkSelectionPlotter/Eventvariable Plots/numPVReco");
  TH1D * h_with = (TH1D*)f_with->Get("IsoTrkSelectionPlotter/Eventvariable Plots/numPVReco");
  TH1D * h_without = (TH1D*)f_without->Get("IsoTrkSelectionPlotter/Eventvariable Plots/numPVReco");

  h_total->Rebin(5);
  h_with->Rebin(5);
  h_without->Rebin(5);


  for(int i = -1; i < h_total->GetNbinsX() + 1; i++) {
    if(h_with->GetBinContent(i+1) > h_total->GetBinContent(i+1)) {
        h_with->SetBinContent(i+1, h_total->GetBinContent(i+1));
	h_with->SetBinError(i+1, h_total->GetBinError(i+1));
    }
    if(h_without->GetBinContent(i+1) > h_total->GetBinContent(i+1)) {
        h_without->SetBinContent(i+1, h_total->GetBinContent(i+1));
	h_without->SetBinError(i+1, h_total->GetBinError(i+1));
    }
  }


  h_total->Draw();
  h_with->Draw("same");
  h_without->Draw("same");

  TGraphAsymmErrors * gr_with = new TGraphAsymmErrors(h_with, h_total);
  TGraphAsymmErrors * gr_without = new TGraphAsymmErrors(h_without, h_total);

  TCanvas * can = new TCanvas("c1", "c1", 800, 800);

  TLatex * prelim = new TLatex();
  prelim->SetNDC();
  prelim->SetTextAngle(0);
  prelim->SetTextFont(62);
  prelim->SetTextAlign(12);
  prelim->SetTextSize(0.04);

  TLatex * run = (TLatex*)prelim->Clone();
  run->SetTextFont(42);
  run->SetTextAlign(32);
  run->SetTextSize(0.035);

  TLegend * leg = new TLegend(0.35, 0.65, 0.7, 0.8, "AMSB #tilde{#chi}^{#pm} (700 GeV, 1000 cm)", "brNDC");
  leg->SetBorderSize(0);
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetTextSize(0.035);
  leg->SetTextFont(42);
  leg->AddEntry(gr_with, "With pileup subtraction", "P");
  leg->AddEntry(gr_without, "Without pileup subtraction", "P");

  TH1D * h_dummy = new TH1D("dummy", "dummy;number of primary vertices;track iso. efficiency", 1, 0, 50);
  h_dummy->GetYaxis()->SetRangeUser(0.5, 1.4);
  h_dummy->Draw();

  TLine * hline = new TLine(0, 1.0, 50, 1.0);
  hline->SetLineStyle(2);
  hline->SetLineColor(kBlack);
  hline->Draw("same");

  gr_with->SetLineColor(kBlack);
  gr_with->SetMarkerColor(kBlack);
  gr_with->SetMarkerStyle(20);

  gr_without->SetLineColor(kBlack);
  gr_without->SetMarkerColor(kBlack);
  gr_without->SetMarkerStyle(4);

  gr_with->Draw("LP");
  gr_without->Draw("LP");

  leg->Draw("same");
  prelim->DrawLatex(0.105, 0.925, "CMS Simulation Preliminary");
  run->DrawLatex(0.9, 0.93, "13 TeV");

  can->SaveAs("Fig15.pdf");
}
