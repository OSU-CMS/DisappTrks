TString inputFiles[24] = {"puData_2015_central", "puData_2015_up", "puData_2015_down",
                          "puData_2016_central", "puData_2016_up", "puData_2016_down",
                          "puData_2016BC_central", "puData_2016BC_up", "puData_2016BC_down",
                          "puData_2016DEFGH_central", "puData_2016DEFGH_up", "puData_2016DEFGH_down",
                          "puData_2017_central", "puData_2017_up", "puData_2017_down",
                          "puData_2018_central", "puData_2018_up", "puData_2018_down",
                          "puData_2022_central", "puData_2022_up", "puData_2022_down",
                          "puData_2023_central", "puData_2023_up", "puData_2023_down"};

TString histNames[24] = {"data2015", "data2015Up", "data2015Down",
                         "data2016", "data2016Up", "data2016Down",
                         "data2016_BC", "data2016_BCUp", "data2016_BCDown",
                         "data2016_DEFGH", "data2016_DEFGHUp", "data2016_DEFGHDown",
                         "data2017", "data2017Up", "data2017Down",
                         "data2018", "data2018Up", "data2018Down",
                         "data2022", "data2022Up", "data2022Down",
                         "data2023", "data2023Up", "data2023Down"};

void combineDataFiles() {

  TFile * output = new TFile("puData.root", "RECREATE");

  for(int i = 0; i < 24; i++) {
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
