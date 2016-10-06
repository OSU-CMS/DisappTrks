TString inputFiles[6] = {"puData_2015_central", "puData_2015_up", "puData_2015_down",
                         "puData_2016_central", "puData_2016_up", "puData_2016_down"};

TString histNames[6] = {"pileup15", "pileup15_up", "pileup15_down",
                        "pileup16", "pileup16_up", "pileup16_down"};

void combineDataFiles() {

  TFile * output = new TFile("puData.root", "RECREATE");

  for(int i = 0; i < 6; i++) {
    TFile * input = new TFile(inputFiles[i] + ".root");
    TH1D * hist = (TH1D*)input->Get("pileup");
    output->cd();
    hist->Write(histNames[i]);
    input->Close();
  }

  output->Write();
  output->Close();

}
