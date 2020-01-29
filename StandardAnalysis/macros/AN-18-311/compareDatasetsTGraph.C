int compareDatasetsTGraph(){

	vector<TString> masses  = {"100","200","300","400","500","600","700","800","900","1000","1100"};
	vector<TString> nlayers = {"NLayers4","NLayers5","NLayers6plus"};
	vector<TString> eras    = {"plots_verA","plots_verB","plots_verC"};
	vector<double>  lumis   = {4822.568,868.626,35864.601};

	double total_lumi = 4822.568 + 35864.601 + 868.626;

	vector<double> binsLogX;
        int nBinsLogX = 1000;
        double binsLogXPowerHi = 3.0;
        double binsLogXPowerLo = 0.0;

        double binsLogXPowerWidth = (binsLogXPowerHi - binsLogXPowerLo) / nBinsLogX;

	for(int ibin = 0; ibin <= nBinsLogX ; ibin++){
	    binsLogX.push_back(pow(10, binsLogXPowerLo + ibin * binsLogXPowerWidth));
	}

	Double_t* BinsLogX = &binsLogX[0];

//	TFile* outputFile = new TFile("triggerEfficiency_AMSB_AllLifetime.root","recreate");

	for(auto i = masses.begin(); i < masses.end(); i++){
	    for(auto j = nlayers.begin(); j < nlayers.end(); j++){
		std::cout << *i << std::endl;
	        TFile* outputFile = new TFile("triggerEfficiency_AMSB_chargino_"+ TString(*i) + "GeV_allLifetimes_" + TString(*j) + ".root","recreate");
	        TH1D* eff_hist = new TH1D("triggerEfficiency_AMSB_chargino_"+ TString(*i) + "GeV_allLifetimes_" + TString(*j),"eff_hist", nBinsLogX, BinsLogX);
	        TH1D* err_high = new TH1D("triggerEfficiency_AMSB_chargino_"+ TString(*i) + "GeV_allLifetimes_" + TString(*j)+ "_err_high","err_high", nBinsLogX, BinsLogX);
	        TH1D* err_low = new TH1D("triggerEfficiency_AMSB_chargino_"+ TString(*i) + "GeV_allLifetimes_" + TString(*j)+ "_err_low","err_low", nBinsLogX, BinsLogX);
//	        TGraphAsymmErrors* eff_tgraph = new TGraphAsymmErrors();
		for(int k =0; k < eras.size(); k++){
		    TFile* inputFile = new TFile( TString(eras.at(k)) + "/triggerEfficiency_AMSB_chargino_"+ TString(*i) + "GeV_allLifetimes_" + TString(*j) + ".root","READ");
		    TGraphAsymmErrors* efficiency = (TGraphAsymmErrors*)inputFile->Get("GrandOr_METPath");
		    for( int n_x = 0; n_x < efficiency->GetN(); n_x++){
		        Double_t x=0.0;
			Double_t y=0.0;
		        Double_t y_err_high=0.0;
			Double_t y_err_low =0.0;
			efficiency->GetPoint(n_x,x,y);
			y_err_high = efficiency->GetErrorYhigh(n_x);
			y_err_low = efficiency->GetErrorYlow(n_x);
			cout << y_err_high << "," << y_err_low << endl;
			eff_hist->Fill(x, y* (double)(lumis.at(k)) / total_lumi);
			Int_t nBin = err_high->FindBin(x);
			err_high->SetBinContent(nBin, err_high->GetBinContent(nBin)+pow(y_err_high,2)*pow((double)(lumis.at(k)) / total_lumi,2));
			err_low->SetBinContent(nBin, err_low->GetBinContent(nBin)+pow(y_err_low,2)*pow((double)(lumis.at(k)) / total_lumi,2));
		    }
		}
		for(int nbin = 0; nbin < eff_hist->GetNbinsX(); nbin++){
		    eff_hist->SetBinError(nbin, (sqrt(err_high->GetBinContent(nbin))+sqrt(err_low->GetBinContent(nbin)))/2);
		}
		eff_hist->Rebin(10);
		TGraphAsymmErrors* eff_tgraph = new TGraphAsymmErrors(eff_hist);
		outputFile->cd();
		eff_hist->Write();
		eff_tgraph->Write("GrandOr_METPath");
	        outputFile->Close();	
	    }
	}
        return 1;
}
