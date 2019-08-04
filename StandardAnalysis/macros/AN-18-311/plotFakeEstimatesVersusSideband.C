const bool run2017 = true;

void go2017() {
  TH1D * h4 = new TH1D("h4", "h4;sideband lower bound |d_{xy}| [cm];fake track estimate", 10, 0, 0.5);
  TH1D * h5 = new TH1D("h5", "h5;sideband lower bound |d_{xy}| [cm];fake track estimate", 10, 0, 0.5);
  TH1D * h6 = new TH1D("h6", "h6;sideband lower bound |d_{xy}| [cm];fake track estimate", 10, 0, 0.5);

  double values_4[9] = {9.6, 11.2, 12.5, 9.7, 10.3, 13.6, 8.4, 11.6, 14.0};
  double errors_4[9] = {1.2, 1.5, 1.9, 2.1, 2.5, 3.1, 2.5, 3.0, 3.3};

  cout << "Differences in stdev for NLayers4:" << endl;
  for(int i = 0; i < 9; i++) {
    h4->SetBinContent(i+2, values_4[i]);
    h4->SetBinError(i+2, errors_4[i]);

    double meanError = 0.82;
    double diff = (values_4[i] - 11.22) / TMath::Hypot(meanError, errors_4[i]);
    cout << "\t" << i << " -- " << diff << endl;
  }

  TLine * mean4 = new TLine(0, 11.22, 0.5, 11.22);
  TBox *  err4 = new TBox(0, 11.22 - 0.82, 0.5, 11.22 + 0.82);

  double values_5[9] = {0.7, 2.12, 0.29, 0.89, 1.22, 1.4, 0.0, 1.6, 0.0};
  double errors_5[9] = {0.31, 0.64, 0.29, 0.63, 0.86, 1.0, 0.87, 1.1, 0.89};

  cout << "Differences in stdev for NLayers5:" << endl;
  for(int i = 0; i < 9; i++) {
    h5->SetBinContent(i+2, values_5[i]);
    h5->SetBinError(i+2, errors_5[i]);

    double meanError = (values_5[i] > 0.91) ? 0.26 : 0.22;
    double diff = (values_5[i] - 0.91) / TMath::Hypot(meanError, errors_5[i]);
    cout << "\t" << i << " -- " << diff << endl;
  }

  TLine * mean5 = new TLine(0, 0.91, 0.5, 0.91);
  TBox  * err5 = new TBox(0, 0.91 - 0.22, 0.5, 0.91 + 0.26);

  double values_6[9] = {0.14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  double errors_6[9] = {0.14, 0.22, 0.33, 0.50, 0.69, 0.82, 0.87, 0.88, 0.89};

  cout << "Differences in stdev for NLayers6plus:" << endl;
  for(int i = 0; i < 9; i++) {
    h6->SetBinContent(i+2, values_6[i]);
    h6->SetBinError(i+2, errors_6[i]);

    double meanError = (values_6[i] > 0.02) ? 0.22 : 0.02;
    double diff = (values_6[i] - 0.02) / TMath::Hypot(meanError, errors_6[i]);
    cout << "\t" << i << " -- " << diff << endl;
  }

  TLine * mean6 = new TLine(0, 0.02, 0.5, 0.02);
  TBox * err6 = new TBox(0, 0.02 - 0.02, 0.5, 0.02 + 0.22);

  h4->GetYaxis()->SetRangeUser(5e-2, 20);
  h4->GetYaxis()->SetTitleOffset(1.0);

  h4->SetLineColor(kRed);
  h5->SetLineColor(8);
  h6->SetLineColor(kBlue);

  mean4->SetLineColor(kRed);
  mean5->SetLineColor(8);
  mean6->SetLineColor(kBlue);

  err4->SetLineColor(kRed);
  err5->SetLineColor(8);
  err6->SetLineColor(kBlue);

  err4->SetFillColor(kRed);
  err5->SetFillColor(8);
  err6->SetFillColor(kBlue);

  err4->SetFillStyle(3002);
  err5->SetFillStyle(3002);
  err6->SetFillStyle(3002);

  h4->SetMarkerColor(kRed);
  h5->SetMarkerColor(8);
  h6->SetMarkerColor(kBlue);

  h4->SetMarkerStyle(20);
  h5->SetMarkerStyle(20);
  h6->SetMarkerStyle(20);

  mean4->SetLineWidth(3);
  mean5->SetLineWidth(3);
  mean6->SetLineWidth(3);

  TCanvas * can = new TCanvas("c1", "c1", 10, 10, 800, 800);
  can->SetLogy(true);

  h4->Draw("e1");
  h5->Draw("e1 same");
  h6->Draw("e1 same");

  mean4->Draw("same");
  mean5->Draw("same");
  mean6->Draw("same");

  err4->Draw("same");
  err5->Draw("same");
  err6->Draw("same");

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

  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, "41.4 fb^{-1} (13 TeV)");
}

void go2018() {

  TH1D * h4 = new TH1D("h4", "h4;sideband lower bound |d_{xy}| [cm];fake track estimate", 10, 0, 0.5);
  TH1D * h5 = new TH1D("h5", "h5;sideband lower bound |d_{xy}| [cm];fake track estimate", 10, 0, 0.5);
  TH1D * h6 = new TH1D("h6", "h6;sideband lower bound |d_{xy}| [cm];fake track estimate", 10, 0, 0.5);

  double values_4[9] = {6.63, 8.2, 11.3, 8.8, 5.1, 10.2, 7.1, 12.5, 8.9};
  double errors_4[9] = {0.95, 1.2, 1.8, 1.9, 1.6, 2.4, 2.0, 2.7, 2.3};

  cout << "Differences in stdev for NLayers4:" << endl;
  for(int i = 0; i < 9; i++) {
    h4->SetBinContent(i+2, values_4[i]);
    h4->SetBinError(i+2, errors_4[i]);

    double meanError = 0.65;
    double diff = (values_4[i] - 8.75) / TMath::Hypot(meanError, errors_4[i]);
    cout << "\t" << i << " -- " << diff << endl;
  }

  TLine * mean4 = new TLine(0, 8.75, 0.5, 8.75);
  TBox *  err4 = new TBox(0, 8.75 - 0.65, 0.5, 8.75 + 0.65);

  double values_5[9] = {0.68, 0.37, 0.28, 0.8, 1.53, 0.0, 0.0, 0.59, 0.59};
  double errors_5[9] = {0.3, 0.26, 0.28, 0.57, 0.88, 0.65, 0.67, 0.59, 0.59};

  cout << "Differences in stdev for NLayers5:" << endl;
  for(int i = 0; i < 9; i++) {
    h5->SetBinContent(i+2, values_5[i]);
    h5->SetBinError(i+2, errors_5[i]);

    double meanError = (values_5[i] > 0.54) ? 0.19 : 0.16;
    double diff = (values_5[i] - 0.54) / TMath::Hypot(meanError, errors_5[i]);
    cout << "\t" << i << " -- " << diff << endl;
  }

  TLine * mean5 = new TLine(0, 0.54, 0.5, 0.54);
  TBox  * err5 = new TBox(0, 0.54 - 0.16, 0.5, 0.54 + 0.19);

  double values_6[9] = {0.0, 0.0, 0.55, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  double errors_6[9] = {0.15, 0.21, 0.39, 0.46, 0.58, 0.65, 0.67, 0.68, 0.68};

  cout << "Differences in stdev for NLayers6plus:" << endl;
  for(int i = 0; i < 9; i++) {
    h6->SetBinContent(i+2, values_6[i]);
    h6->SetBinError(i+2, errors_6[i]);

    double meanError = (values_6[i] > 0.06) ? 0.18 : 0.04;
    double diff = (values_6[i] - 0.06) / TMath::Hypot(meanError, errors_6[i]);
    cout << "\t" << i << " -- " << diff << endl;
  }

  TLine * mean6 = new TLine(0, 0.06, 0.5, 0.06);
  TBox * err6 = new TBox(0, 0.06 - 0.04, 0.5, 0.06 + 0.18);

  h4->GetYaxis()->SetRangeUser(1e-2, 20);
  h4->GetYaxis()->SetTitleOffset(1.0);

  h4->SetLineColor(kRed);
  h5->SetLineColor(8);
  h6->SetLineColor(kBlue);

  mean4->SetLineColor(kRed);
  mean5->SetLineColor(8);
  mean6->SetLineColor(kBlue);

  err4->SetLineColor(kRed);
  err5->SetLineColor(8);
  err6->SetLineColor(kBlue);

  err4->SetFillColor(kRed);
  err5->SetFillColor(8);
  err6->SetFillColor(kBlue);

  err4->SetFillStyle(3002);
  err5->SetFillStyle(3002);
  err6->SetFillStyle(3002);

  h4->SetMarkerColor(kRed);
  h5->SetMarkerColor(8);
  h6->SetMarkerColor(kBlue);

  h4->SetMarkerStyle(20);
  h5->SetMarkerStyle(20);
  h6->SetMarkerStyle(20);

  mean4->SetLineWidth(3);
  mean5->SetLineWidth(3);
  mean6->SetLineWidth(3);

  TCanvas * can = new TCanvas("c1", "c1", 10, 10, 800, 800);
  can->SetLogy(true);

  h4->Draw("e1");
  h5->Draw("e1 same");
  h6->Draw("e1 same");

  mean4->Draw("same");
  mean5->Draw("same");
  mean6->Draw("same");

  err4->Draw("same");
  err5->Draw("same");
  err6->Draw("same");

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

  prelim->DrawLatex(0.105, 0.925, "CMS Preliminary");
  run->DrawLatex(0.9, 0.93, "28.0 fb^{-1} (13 TeV)"); // ABC = 27982.4409675/pb
}

void plotFakeEstimatesVersusSideband() {

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);

  if(run2017) go2017();
  else go2018();
}