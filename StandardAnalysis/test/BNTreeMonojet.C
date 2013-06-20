// New histograms must be added in three places:
// * declare
// * fill
// * write


#define BNTree_cxx
#include "BNTree.h"
#include <TH1F.h>
#include <TH2.h>
#include <TStopwatch.h>
#include <TString.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream> 
using std::cout;
using std::endl;

void BNTree::Loop(TString outFile)
{
  //   In a ROOT session, you can do:
  //      Root > .L BNTreeMonojet.C
  //      Root > BNTreeMonojet t
  //      Root > t.GetEntry(12); // Fill t data members with entry number 12
  //      Root > t.Show();       // Show values of entry 12
  //      Root > t.Show(16);     // Read and show values of entry 16
  //      Root > t.Loop();       // Loop on all entries
  //

  //     This is the loop skeleton where:
  //    jentry is the global entry number in the chain
  //    ientry is the entry number in the current Tree
  //  Note that the argument to GetEntry must be:
  //    jentry for TChain::GetEntry
  //    ientry for TTree::GetEntry and TBranch::GetEntry
  //
  //       To read only selected branches, Insert statements like:
  // METHOD1:
  //    fChain->SetBranchStatus("*",0);  // disable all branches
  //    fChain->SetBranchStatus("branchname",1);  // activate branchname
  // METHOD2: replace line
  //    fChain->GetEntry(jentry);       //read all branches
  //by  b_branchname->GetEntry(ientry); //read only this branch

  TStopwatch timer;  
  timer.Start();

  if (fChain == 0) return;

  TString dir = "";  
  dir = fChain->GetName();
  dir = dir(0, dir.Last('/'));  

  // Open output root file.  
  TFile* fOut = 0;
  if (outFile=="") fOut = new TFile("newBNTreeMonojetPlot.root", "RECREATE");  
  else {
    fOut = new TFile(outFile,              "UPDATE");  
    cout << "Debug:  name of dir is: " << dir << endl;  
    fOut->cd(dir);  
  }
  cout << "Will write histograms to file " << fOut->GetName()
       << " in directory:  " << dir << endl;  

  // delete all previously existing instances of all BNHist histograms  
  TDirectory* tDir = fOut->GetDirectory(dir);  
  if (!tDir) {
    cout << "Could not find directory " << dir << endl;  
  } else {
    tDir->Delete("BNHist_*;*");  
  }

  // Declare desired histograms.  
  TH1::SetDefaultSumw2();

  TH1F* hNJets                   = new TH1F("BNHist_NJets",                 ";Jet mulitiplicity", 10, 0, 10);  
  TH1F* numPV                    = new TH1F("BNHist_numPV",                 ";# primary vertices", 70, 0, 70);  
  TH1F* METPre                   = new TH1F("BNHist_METPre",                ";MET [GeV]", 100, 0, 500);  
  TH1F* MET                      = new TH1F("BNHist_MET",                   ";MET [GeV]", 32, 200, 1000);  
  TH1F* METFull                  = new TH1F("BNHist_METFull",               ";MET [GeV]", 40, 0, 1000);  
  TH1F* jetChargedHadFrac        = new TH1F("BNHist_jetChargedHadFrac",     ";ChargedHadFrac", 60,  0.0, 1.2);  
  TH1F* jetNeutralHadFrac        = new TH1F("BNHist_jetNeutralHadFrac",     ";NeutralHadFrac", 60, -0.1, 1.1);  
  TH1F* jetChargedEMFrac         = new TH1F("BNHist_jetChargedEMFrac",      ";ChargedEMFrac",  60, -0.1, 1.1);  
  TH1F* jetNeutralEMFrac         = new TH1F("BNHist_jetNeutralEMFrac",      ";NeutralEMFrac",  60, -0.1, 1.1);  
  TH1F* jetOneEta                = new TH1F("BNHist_jetOneEta",             ";Jet1 #eta", 36, -3.6, 3.6);  
  TH1F* jetOnePt                 = new TH1F("BNHist_jetOnePt",              ";Jet1 pT [GeV]", 40, 0, 1000);  
  TH1F* jetTwoChHadFrac          = new TH1F("BNHist_jetTwoChHadFrac",       ";Jet2 Charged Had Frac", 60,  0.0, 1.2);  
  TH1F* jetTwoNeutralHadFrac     = new TH1F("BNHist_jetTwoNeutralHadFrac",  ";Jet2 Neutral Had Frac", 60, -0.1, 1.1);  
  TH1F* jetTwoChEMFrac           = new TH1F("BNHist_jetTwoChEMFrac",        ";Jet2 Charged EM Frac",  60, -0.1, 1.1);  
  TH1F* jetTwoNeutralEMFrac      = new TH1F("BNHist_jetTwoNeutralEMFrac",   ";Jet2 Neutral EM Frac",  60, -0.1, 1.1);  
  TH1F* jetTwoEta                = new TH1F("BNHist_jetTwoEta",             ";Jet2 #eta", 60, -5, 5);  
  TH1F* jetTwoPt                 = new TH1F("BNHist_jetTwoPt",              ";Jet2 pT", 25, 0, 600);  
  TH1F* jetOneMetDPhi            = new TH1F("BNHist_jetOneMetDPhi",         ";#Delta #phi (Jet1, MET)",  35, 0, 3.5);  
  TH1F* jetTwoMetDPhi            = new TH1F("BNHist_jetTwoMetDPhi",         ";#Delta #phi (Jet2, MET)",  35, 0, 3.5);  
  TH1F* jetDPhi                  = new TH1F("BNHist_jetDPhi",               ";#Delta #phi (Jet1, Jet2)", 35, 0, 3.5);  


  TH1F* hNElecs                  = new TH1F("BNHist_NElecs",                ";Elec mulitiplicity",               11, -0.5, 10.5);   
  TH1F* hNMuons                  = new TH1F("BNHist_NMuons",                ";Muon mulitiplicity", 		 11, -0.5, 10.5);   
  TH1F* hNTaus                   = new TH1F("BNHist_NTaus",                 ";Tau  mulitiplicity", 		 11, -0.5, 10.5);   
  TH1F* hNElecsNoCut             = new TH1F("BNHist_NElecsNoCut",           ";Elec mulitiplicity (no elec cut)", 11, -0.5, 10.5);   
  TH1F* hNMuonsNoCut             = new TH1F("BNHist_NMuonsNoCut",           ";Muon mulitiplicity (no muon cut)", 11, -0.5, 10.5);   
  TH1F* hNTausNoCut              = new TH1F("BNHist_NTausNoCut",            ";Tau  mulitiplicity (no tau cut)",  11, -0.5, 10.5);   
  TH1F* hNMets                   = new TH1F("BNHist_NMets",                 ";Met mulitiplicity",                11, -0.5, 10.5);  
  TH1F* hNMetsCut0               = new TH1F("BNHist_NMetsCut0",             ";Met mulitiplicity (cut 0)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut1               = new TH1F("BNHist_NMetsCut1",             ";Met mulitiplicity (cut 1)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut2               = new TH1F("BNHist_NMetsCut2",             ";Met mulitiplicity (cut 2)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut3               = new TH1F("BNHist_NMetsCut3",             ";Met mulitiplicity (cut 3)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut4               = new TH1F("BNHist_NMetsCut4",             ";Met mulitiplicity (cut 4)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut5               = new TH1F("BNHist_NMetsCut5",             ";Met mulitiplicity (cut 5)",  	 11, -0.5, 10.5);  
  TH1F* hElecMVA                 = new TH1F("BNHist_ElecMVA",               ";Elec MVA",           100, -2, 2);


    
  Long64_t nentries = fChain->GetEntries();

  double lumiWt = fChain->GetWeight();  // The BNTree weight must be set by mergeOutput.py.  
  if (outFile.Contains("hist_")) lumiWt = 1.0;  // Do not apply the lumi weight if writing histograms to hist_*.root files, since the lumi wt will be applied by mergeOutput.py.  

  cout << "Looping over " << nentries << " entries in chain: " << fChain->GetTitle() << endl;  
  Long64_t nbytes = 0, nb = 0;
  for (Long64_t jentry=0; jentry<nentries;jentry++) {
    //   for (Long64_t jentry=0; jentry<10;jentry++) {
    if (jentry%1000000==0 && jentry>0) {
      cout << "Time elapsed for this job after "
	   << jentry << " entries is: ";  
      timer.Print();
      timer.Continue();
    }  
     
    Long64_t ientry = LoadTree(jentry);
    if (ientry < 0) break;
    nb = fChain->GetEntry(jentry);   nbytes += nb;
    double BNTreeWt = 
      lumiWt * 
      events_puScaleFactor      ->at(0) * 
      events_muonScaleFactor    ->at(0) * 
      events_electronScaleFactor->at(0);  



    // Count other physics objects, according to AN-2012-421-v6.  
    int numJets  = 0;
    int numMuons = 0;
    int numElecs = 0;
    int numTaus  = 0; 

    double DiJetDeltaPhi = 0;  // default is 0, so event passes if only one jet found  
    vector<uint> jetPassedIdx;  
    for (uint ijet = 0; ijet<jets_pt->size(); ijet++) {
      // count number of jets that have pT>30 and |eta|<4.5
      if (!(jets_pt      ->at(ijet)  > 30))  continue;
      if (!(fabs(jets_eta->at(ijet)) < 4.5)) continue;
      jetPassedIdx.push_back(ijet);  
      numJets++;  
    } 
    if (numJets>1) {
      uint idx0 = jetPassedIdx.at(0);
      uint idx1 = jetPassedIdx.at(1);
      DiJetDeltaPhi = fabs(fabs(fabs(jets_phi->at(idx0) - jets_phi->at(idx1)) - 3.14159) - 3.14159);  

      // check that idx0 corresponds to the leading jet; switch if not
      if (jets_pt->at(idx0) < jets_pt->at(idx1)) {
	jetPassedIdx.at(0) = idx1;
	jetPassedIdx.at(1) = idx0;
      }

    }

    for (uint imuon = 0; imuon<muons_pt->size(); imuon++) {
      if (!(muons_pt                      ->at(imuon)  > 10))   continue;  
      if (!(muons_isGlobalMuon->at(imuon) ==1 || 
	    muons_isTrackerMuon->at(imuon)==1                         ))   continue;  

      // Selection below is for positive muon ID, not muon veto!
      // if (!(muons_pt                      ->at(imuon)  > 20))   continue;
      // if (!(fabs(muons_eta                ->at(imuon)) < 2.1))  continue;
      // if (!(muons_isGlobalMuon            ->at(imuon) == 1))    continue;
      // if (!(fabs(muons_correctedD0Vertex  ->at(imuon)) < 0.02)) continue;
      // // FIXME:  no R<0.2 cut applied 
      // if (!(muons_numberOfValidPixelHits  ->at(imuon) >= 1))    continue;
      // if (!(muons_numberOfValidTrackerHits->at(imuon) >= 10)) 	continue;
      // if (!(muons_numberOfMatchedStations ->at(imuon) >= 2))  	continue;
      // if (!(muons_numberOfValidMuonHits   ->at(imuon) >= 1))  	continue;
      numMuons++;  
    }

    for (uint ielec = 0; ielec<electrons_pt->size(); ielec++) {
      hElecMVA->Fill(electrons_mvaNonTrigV0->at(ielec), BNTreeWt);  
      if (!(electrons_pt                     ->at(ielec)  > 10))   continue;  
      if (!(electrons_mvaNonTrigV0           ->at(ielec)  >  0))   continue;  // FIXME:  May need to tune this cut value!  
      numElecs++;  
    }

    for (uint itau = 0; itau<taus_pt->size(); itau++) {
      if (!(taus_pt                                           ->at(itau)  > 10))  continue;  
      if (!(fabs(taus_eta                		      ->at(itau)) < 2.3)) continue;  
      if (!(fabs(taus_HPSbyLooseCombinedIsolationDeltaBetaCorr->at(itau)) == 1))  continue;  
      if (!(fabs(taus_HPSdecayModeFinding                     ->at(itau)) == 1))  continue;  					 
      if (!(fabs(taus_HPSagainstElectronLoose		      ->at(itau)) == 1))  continue;  					 
      if (!(fabs(taus_HPSagainstMuonTight    		      ->at(itau)) == 1))  continue;    // monojet uses AgainstMuonTight2  
      numTaus++;  
    }

    // Apply other selection requirements, corresponding to https://twiki.cern.ch/twiki/bin/viewauth/CMS/MonojetDataFinalStandard2012v2#Cutflow
    METPre    ->Fill(mets_pt->at(0),     BNTreeWt);  	
    hNMetsCut0->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(mets_pt->at(0) > 250))  continue;     hNMetsCut1->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numJets  <= 2))         continue;     hNMetsCut2->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(DiJetDeltaPhi < 2.5))   continue;     hNMetsCut3->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numMuons == 0))         continue;     hNMetsCut4->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numElecs == 0))         continue;     hNMetsCut5->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numTaus  == 0))         continue; 

    hNJets            ->Fill(numJets,                   BNTreeWt);  	
    hNMuons           ->Fill(numMuons,                  BNTreeWt);  	
    hNElecs           ->Fill(numElecs,                  BNTreeWt);  	
    hNTaus            ->Fill(numTaus,                   BNTreeWt);  	
    hNMuonsNoCut      ->Fill(muons_pt->size(),          BNTreeWt);  	
    hNElecsNoCut      ->Fill(electrons_pt->size(),      BNTreeWt);  	
    hNTausNoCut       ->Fill(taus_pt->size(),           BNTreeWt);  	
    hNMets            ->Fill(mets_pt->size(),           BNTreeWt);  	


    double jetMetDPhi = fabs(fabs(fabs(jets_phi->at(jetPassedIdx.at(0)) - mets_phi->at(0)) - 3.14159) - 3.14159);  
    jetChargedHadFrac->Fill(jets_chargedHadronEnergyFraction->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetNeutralHadFrac->Fill(jets_neutralHadronEnergyFraction->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetChargedEMFrac ->Fill(jets_chargedEmEnergyFraction    ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetNeutralEMFrac ->Fill(jets_neutralEmEnergyFraction    ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetOneEta        ->Fill(jets_eta                        ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetOnePt         ->Fill(jets_pt                         ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetOneMetDPhi    ->Fill(jetMetDPhi                                           ,    BNTreeWt);
    jetDPhi          ->Fill(DiJetDeltaPhi                                        ,    BNTreeWt);

    if (jetPassedIdx.size()>1) {
      double subJetMetDPhi = fabs(fabs(fabs(jets_phi->at(jetPassedIdx.at(1)) - mets_phi->at(0)) - 3.14159) - 3.14159);
      jetTwoChHadFrac         ->Fill(jets_chargedHadronEnergyFraction->at(jetPassedIdx.at(1)),    BNTreeWt);
      jetTwoNeutralHadFrac    ->Fill(jets_neutralHadronEnergyFraction->at(jetPassedIdx.at(1)),    BNTreeWt);
      jetTwoChEMFrac          ->Fill(jets_chargedEmEnergyFraction    ->at(jetPassedIdx.at(1)),    BNTreeWt);
      jetTwoNeutralEMFrac     ->Fill(jets_neutralEmEnergyFraction    ->at(jetPassedIdx.at(1)),    BNTreeWt);
      jetTwoEta               ->Fill(jets_eta                        ->at(jetPassedIdx.at(1)),    BNTreeWt);
      jetTwoPt                ->Fill(jets_pt                         ->at(jetPassedIdx.at(1)),    BNTreeWt);
      jetTwoMetDPhi           ->Fill(subJetMetDPhi                                           ,    BNTreeWt);
    }
    
    MET->Fill(mets_pt->at(0),    BNTreeWt);
    METFull->Fill(mets_pt->at(0),    BNTreeWt);

    hNJets->Fill(jets_pt->size(),    BNTreeWt);  	
    numPV->Fill(events_numTruePV->at(0),    BNTreeWt);  	
    

  }  // end   for (Long64_t jentry=0; jentry<nentries;jentry++) {
  
  hNJets                   ->Write();  

  numPV ->Write();
  METPre ->Write();  
  MET ->Write();  
  METFull ->Write();

  jetChargedHadFrac        ->Write();
  jetNeutralHadFrac        ->Write();
  jetChargedEMFrac         ->Write();
  jetNeutralEMFrac         ->Write();
  jetOneEta                ->Write();
  jetOnePt                 ->Write();
  jetOneMetDPhi            ->Write();

  jetDPhi                  ->Write();

  jetTwoChHadFrac          ->Write();  
  jetTwoNeutralHadFrac     ->Write();
  jetTwoChEMFrac           ->Write();
  jetTwoNeutralEMFrac      ->Write();
  jetTwoEta                ->Write();
  jetTwoPt                 ->Write();
  jetTwoMetDPhi            ->Write();


  hElecMVA                 ->Write();  
  hNElecs                  ->Write();  
  hNMuons                  ->Write();  
  hNTaus                   ->Write();  
  hNElecsNoCut             ->Write();  
  hNMuonsNoCut             ->Write();  
  hNTausNoCut              ->Write();  
  hNMets                   ->Write();  
  hNMetsCut0               ->Write();  
  hNMetsCut1               ->Write();  
  hNMetsCut2               ->Write();  
  hNMetsCut3               ->Write();  
  hNMetsCut4               ->Write();  


  fOut->Close();  

  cout << "Finished BNTree::Loop() successfully." << endl;
  cout << "Total time to run BNTree::Loop():  " << flush;
  timer.Print();  


} // void BNTree::Loop()

