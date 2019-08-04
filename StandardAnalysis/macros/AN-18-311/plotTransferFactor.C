void getObjects(bool isMu, bool is2017, TH1D *& h, TH1D *& h_func) {
  TString fileName = "fakeTrackBkgdEstimate_zTo";
  fileName += TString(isMu ? "MuMu" : "EE") + "_";
  fileName += TString(is2017 ? "2017" : "2018ABC") + "_NLayers4.root";

  TFile * fInput = new TFile(fileName, "READ");
  h = (TH1D*)fInput->Get("d0");
  TF1 * func = (TF1*)fInput->Get("d0_fit");

  h->SetDirectory(0);

  h->Rebin(4);
  h_func = (TH1D*)h->Clone(TString("d0_fit_hist_") + TString(is2017 ? "2017" : "2018"));
  h_func->SetDirectory(0);
  h_func->Reset();
  h_func->Add(func, 4.0);

  if(is2017) {
    h->SetLineColor(kBlack);
    h->SetMarkerColor(kBlack);
    h->SetMarkerStyle(20);

    h_func->SetLineColor(kBlack);
    h_func->SetLineWidth(2);
  }
  else {
    h->SetLineColor(kBlue);
    h->SetMarkerColor(kBlue);
    h->SetMarkerStyle(20);

    h_func->SetLineColor(kBlue);
    h_func->SetLineWidth(2);
  }
}

void plotTransferFactor() {

  bool isMu = true;

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);

  TH1D *h2017, *h2018;
  TH1D *func2017, *func2018;

  getObjects(isMu, true, h2017, func2017);
  getObjects(isMu, false, h2018, func2018);

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

  TCanvas * can = new TCanvas("c1", "c1", 10, 10, 800, 800);

  h2017->GetYaxis()->SetTitle("Entries / 0.04 cm");

  h2017->Draw("e");
  func2017->Draw("C same");
  //h2017->Draw("e same");

  h2018->Draw("e same");
  func2018->Draw("C same");

  TString lumiString = "41.5 + 28.0 fb^{-1} 13 TeV";
/*
  if(isMu && is2017) lumiString = "41.5"; // 41458.501
  else if(isMu)      lumiString = "6.89"; // 6894.77097127
  else if(is2017)    lumiString = "41.4"; // 41441.655
  else               lumiString = "6.69"; // 6688.523784
  lumiString += " fb^{-1} (13 TeV)";
*/

  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, lumiString);

  TLegend * leg = new TLegend(0.15, 0.7, 0.3, 0.85, isMu ? "Z#rightarrow#mu#mu" : "Z#rightarrowee", "brNDC");
  leg->SetBorderSize(0);
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetTextSize(0.035);
  leg->SetTextFont(42);
  leg->AddEntry(h2017, "2017", "LPE");
  leg->AddEntry(h2018, "2018", "LPE");
  leg->Draw("same");

  if(isMu) can->SaveAs("tf_ZtoMuMu.pdf");
  else can->SaveAs("tf_ZtoEE.pdf");

/*
  // also plot the NLayers5 channel for fun
  if(is2017) {
    TFile * input5 = new TFile(isMu ? "condor/hartCondor/2017/fakeTrackBackground_noD0/SingleMu_2017.root" : "condor/hartCondor/2017/fakeTrackSystematic_zToEE/SingleEle_2017.root");
    TH1D * h5 = (TH1D*)input5->Get(isMu ? "ZtoMuMuDisTrkNoD0CutNLayers5Plotter/Track-eventvariable Plots/trackd0WRTPV" : "ZtoEEDisTrkNoD0CutNLayers5Plotter/Track-eventvariable Plots/trackd0WRTPV");
    
    h5->SetLineColor(kBlack);
    h5->SetMarkerColor(kBlack);
    h5->SetMarkerStyle(20);
    h5->Rebin(4);
    h5->GetYaxis()->SetTitle("Entries / 0.04 cm");

    TH1D * func_h5 = (TH1D*)h5->Clone("func_h5");
    func_h5->Reset();

    double norm_4to5 = h5->Integral(0, -1) / h->Integral(0, -1);

    func_h5->Add(func, 4.0 * norm_4to5);

    func_h5->SetLineColor(kRed);
    func_h5->SetLineWidth(2);

    h5->Draw("e");
    func_h5->Draw("C same");
    h5->Draw("e same");

    prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
    run->DrawLatex(0.9, 0.93, lumiString);

    if(isMu) can->SaveAs("tf_ZtoMuMu_NLayers5.pdf");
    else can->SaveAs("tf_ZtoEE_NLayers5.pdf");
  }
*/

}
