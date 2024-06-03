void createUncertainties()
{
    TFile *f = TFile::Open("LHEScalesPlot.root");
    TDirectory *dir = (TDirectory*)f->Get("genWeightsTable");
    dir->cd();
    TH1 *den1;
    TH1 *den2;
    TH1 *den3;
    dir->GetObject("wPSNW", den1);
    dir->GetObject("wScaleNW", den2);
    dir->GetObject("wPDFNW", den3);
    TH1 *num1;
    TH1 *num2;
    TH1 *num3;
    dir->GetObject("wPS", num1);
    dir->GetObject("wScale", num2);
    dir->GetObject("wPDF", num3);

    std::cout << num1->TH1::Integral() << std::endl;
    std::cout << den1->TH1::Integral() << std::endl;
    std::cout << num2->TH1::Integral() << std::endl;
    std::cout << den2->TH1::Integral() << std::endl;
    std::cout << num3->TH1::Integral() << std::endl;
    std::cout << den3->TH1::Integral() << std::endl;
    

    int marker = 20;
    const char *ylabel = "Trigger Efficiency";
    const char *xlabelnomu = "PF E_{T}^{miss, no mu}";

    TCanvas *c1 = new TCanvas("c1", "c1", 700, 700);
    TCanvas *c2 = new TCanvas("c2", "c2", 700, 700);
    TCanvas *c3 = new TCanvas("c3", "c3", 700, 700);

    TFile *file = new TFile("uncertainties.root", "RECREATE");
    TH1D *pEff1 = (TH1D*)num1->Clone("pEff1");
    pEff1->Divide(den1);
    pEff1->SetTitle("");
    pEff1->SetMarkerStyle(marker);
    pEff1->SetMinimum(0.0);
    pEff1->SetMaximum(1.5);
    pEff1->GetYaxis()->SetTitle(ylabel);
    pEff1->GetXaxis()->SetTitle(xlabelnomu);
    pEff1->GetYaxis()->SetTitleSize(0.04);
    pEff1->GetXaxis()->SetTitleSize(0.04);
    pEff1->GetYaxis()->SetLabelSize(0.04);
    pEff1->GetXaxis()->SetLabelSize(0.04);
    pEff1->GetXaxis()->SetLimits(-0.5, 3.5);
    c1->cd();
    pEff1->Draw("ap");
    c1->Write();
    c1->Print("uncPS.png");

    TH1D *pEff2 = (TH1D*)num2->Clone("pEff2");
    pEff2->Divide(den2);
    pEff2->SetTitle("");
    pEff2->SetMarkerStyle(marker);
    pEff2->SetMinimum(0.0);
    pEff2->SetMaximum(1.5);
    pEff2->GetYaxis()->SetTitle(ylabel);
    pEff2->GetXaxis()->SetTitle(xlabelnomu);
    pEff2->GetYaxis()->SetTitleSize(0.04);
    pEff2->GetXaxis()->SetTitleSize(0.04);
    pEff2->GetYaxis()->SetLabelSize(0.04);
    pEff2->GetXaxis()->SetLabelSize(0.04);
    pEff2->GetXaxis()->SetLimits(-0.5, 8.5);
    c2->cd();
    pEff2->Draw("ap");
    c2->Write();
    c2->Print("uncScale.png");

    TH1D *pEff3 = (TH1D*)num3->Clone("pEff3");
    pEff3->Divide(den3);
    pEff3->SetTitle("");
    pEff3->SetMarkerStyle(marker);
    pEff3->SetMinimum(0.0);
    pEff3->SetMaximum(1.5);
    pEff3->GetYaxis()->SetTitle(ylabel);
    pEff3->GetXaxis()->SetTitle(xlabelnomu);
    pEff3->GetYaxis()->SetTitleSize(0.04);
    pEff3->GetXaxis()->SetTitleSize(0.04);
    pEff3->GetYaxis()->SetLabelSize(0.04);
    pEff3->GetXaxis()->SetLabelSize(0.04);
    pEff3->GetXaxis()->SetLimits(-0.5, 100.5);
    c3->cd();
    pEff3->Draw("ap");
    c3->Write();
    c3->Print("uncPDF.png");

    f->Close();
    file->Close();
}