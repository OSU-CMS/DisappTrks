const int plotNum = 1;

void plotPileup() {

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

  TFile * fin = new TFile("../../data/pu_disappTrks_run2.root");

  TH1D * h_2018 = (TH1D*)fin->Get("data2018");
  TH1D * h_2018_up = (TH1D*)fin->Get("data2018Up");
  TH1D * h_2018_down = (TH1D*)fin->Get("data2018Down");
  TH1D * h_mc = (TH1D*)fin->Get("mc2018_23May2019");

  h_2018->Scale(1.0 / h_2018->Integral());
  h_2018_up->Scale(1.0 / h_2018_up->Integral());
  h_2018_down->Scale(1.0 / h_2018_down->Integral());
  h_mc->Scale(1.0 / h_mc->Integral());

  h_2018->SetLineColor(kBlack);
  h_2018_up->SetLineColor(kRed);
  h_2018_down->SetLineColor(kBlue);
  h_mc->SetLineColor(kBlack);

  h_2018->SetMarkerStyle(20);
  h_2018->SetMarkerColor(kBlack);

  h_2018_up->SetLineStyle(2);
  h_2018_down->SetLineStyle(2);

  h_mc->SetLineWidth(3);
  h_2018_up->SetLineWidth(3);
  h_2018_down->SetLineWidth(3);

  h_2018->GetYaxis()->SetTitle("number of events [arb. norm.]");
  h_2018->GetXaxis()->SetTitle("number of interactions");

  TCanvas * can = new TCanvas("c1", "c1", 800, 800);

  if(plotNum == 0) {
  	h_2018->Draw("e1");
  	h_mc->Draw("hist same");
  }
  else {
  	h_2018->Draw("e1");
  	h_2018_up->Draw("hist same");
  	h_2018_down->Draw("hist same");
  }

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

  TLegend * leg = new TLegend(0.6, 0.7, 0.85, 0.85, "", "brNDC");
  leg->SetBorderSize(0);
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetTextSize(0.035);
  leg->SetTextFont(42);
  if(plotNum == 0) {
  	leg->AddEntry(h_2018, "2018 data", "ELP");
  	leg->AddEntry(h_mc, "2018 MC (102X)", "L");
  }
  else {
  	leg->AddEntry(h_2018, "nominal", "ELP");
  	leg->AddEntry(h_2018_down, "scaled down", "ELP");
  	leg->AddEntry(h_2018_up, "scaled up", "ELP");

  }

  leg->Draw("same");
  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, "13 TeV");


}