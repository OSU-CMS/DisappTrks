void plotHEMmetPhi() {

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

  TFile * f_A = new TFile("MET_2018A.root");
  TFile * f_CD = new TFile("MET_2018CD.root");

  TH1D * h_met_A  = (TH1D*)f_A->Get("BasicSelectionPlotter/Met Plots/metPhi");
  TH1D * h_met_CD = (TH1D*)f_CD->Get("BasicSelectionPlotter/Met Plots/metPhi");

  TH2D * h_jet_A  = (TH2D*)f_A->Get("BasicSelectionPlotter/Jet Plots/jetEtaPhi");
  TH2D * h_jet_CD = (TH2D*)f_CD->Get("BasicSelectionPlotter/Jet Plots/jetEtaPhi");

  h_met_A->Scale(1. / 14024.1765055);
  h_met_CD->Scale(1. / 38637.7627244);

  h_met_A->SetLineColor(kBlack);
  h_met_CD->SetLineColor(kRed);

  h_met_A->GetYaxis()->SetTitle("Events / pb^{-1}");
  h_met_A->GetYaxis()->SetRangeUser(0, 8);

  TCanvas * can = new TCanvas("c1", "c1", 800, 800);

  h_met_A->Draw("hist");
  h_met_CD->Draw("hist same");

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

  TLegend * leg = new TLegend(0.6, 0.7, 0.85, 0.85, "Basic selection", "brNDC");
  leg->SetBorderSize(0);
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetTextSize(0.035);
  leg->SetTextFont(42);
  leg->AddEntry(h_met_A, "2018 A", "L");
  leg->AddEntry(h_met_CD, "2018 CD", "L");

  leg->Draw("same");
  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, "13 TeV");

  can->SaveAs("hem_metPhi.pdf");

  can->SetLogz(true);

  h_jet_A->GetZaxis()->SetLabelSize(0.03);
  h_jet_A->Draw("colz");
  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, "14.0 fb^{-1} (13 TeV)");
  run->DrawLatex(0.75, 0.85, "MET_2018A");
  can->SaveAs("hem_jetPhi_2018A.pdf");

  h_jet_CD->GetZaxis()->SetLabelSize(0.03);
  h_jet_CD->Draw("colz");
  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, "38.6 fb^{-1} (13 TeV)");
  run->DrawLatex(0.75, 0.85, "MET_2018CD");
  can->SaveAs("hem_jetPhi_2018CD.pdf");
}
