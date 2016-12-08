TString inputFiles[12] = {"puData_2015_central", "puData_2015_up", "puData_2015_down",
                          "puData_2016_central", "puData_2016_up", "puData_2016_down",
                          "puData_2016BC_central", "puData_2016BC_up", "puData_2016BC_down",
                          "puData_2016DEFG_central", "puData_2016DEFG_up", "puData_2016DEFG_down"};

TString histNames[12] = {"data2015", "data2015Up", "data2015Down",
                         "data2016", "data2016Up", "data2016Down",
                         "data2016_BC", "data2016_BCUp", "data2016_BCDown",
                         "data2016_DEFG", "data2016_DEFGUp", "data2016_DEFGDown"};

void combineDataFiles() {

  TFile * output = new TFile("puData.root", "RECREATE");

  for(int i = 0; i < 12; i++) {
    TFile * input = new TFile(inputFiles[i] + ".root");

cout << "working on " << inputFiles[i] << ".root" << endl;

    TH1D * hist = (TH1D*)input->Get("pileup");
    if(!hist) continue;
    output->cd();
    hist->Write(histNames[i]);

    input->Close();
  }

  output->Write();
  output->Close();

}

