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
  //      Root > .L BNTree.C
  //      Root > BNTree t
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

  // Get histograms for reweighting 
  TFile* fData  = new TFile("condor/condor_2013_06_04_AODCtrlMuonNewTrig/SingleMu_Rewt.root", "READ");  // use different names so that output file does not collide
  TFile* fWjets = new TFile("condor/condor_2013_06_04_AODCtrlMuonNewTrig/Wjets_Rewt.root",    "READ");  // use different names so that output file does not collide
  if (!fData || !fWjets) {
    cout << "Could not open file: fData or fWjets" << endl; 
  }

  TH1* hMetPhiData  = 0;
  TH1* hMetPhiWjets = 0;
  fData ->GetObject(dir+"/mets_phi", hMetPhiData);  
  fWjets->GetObject(dir+"/mets_phi", hMetPhiWjets);  
  if (!hMetPhiWjets) {
    cout << "Could not open histograms: hMetPhiWjets "
	 << " from directory:  " << dir << endl;  
  }
  if (!hMetPhiData) {
    cout << "Could not open histograms: hMetPhiData  "
	 << " from directory:  " << dir << endl;  
  }

  hMetPhiData  ->Scale(1.0 * hMetPhiData ->GetNbinsX() / hMetPhiData ->Integral());  // normalize to area 1.0 * nbins 
  hMetPhiWjets ->Scale(1.0 * hMetPhiWjets->GetNbinsX() / hMetPhiWjets->Integral());  // normalize to area 1.0 * nbins
  TH1F* hMetPhiDataOverMC = (TH1F*) hMetPhiData->Clone("BNTree_MetPhiDataOverMC");  
  hMetPhiDataOverMC->Sumw2();  
  hMetPhiDataOverMC->Divide(hMetPhiWjets);  

  bool isData = outFile.Contains("SingleMu") || outFile.Contains("SingleElec");  // FIXME:  need a better way to do this  

  // Open output root file.  
  TFile* fOut = 0;
  if (outFile=="") fOut = new TFile("newBNTreePlot.root", "RECREATE");  
  else {
    fOut = new TFile(outFile,              "UPDATE");  
    cout << "Debug:  name of dir is: " << dir << endl;  
    fOut->cd(dir);  
  }
  cout << "Will write histograms to file " << fOut->GetName()
       << " in directory:  " << dir << endl;  

  // delete all previously existing instances of the histograms  
  TDirectory* tDir = fOut->GetDirectory(dir);  
  if (!tDir) {
    cout << "Could not find directory " << dir << endl;  
  } else {
    tDir->Delete("BNTree_MetPhiDataOverMC;*");  
    tDir->Delete("BNTree_Met;*");  
    tDir->Delete("BNTree_MetWithPhiRewtToData;*");  
    tDir->Delete("BNTree_MetWithPhiRewtFlat;*");  
    tDir->Delete("BNTree_MetPhi;*");  
    tDir->Delete("BNTree_MetPhiWithPhiRewtToData;*");  
    tDir->Delete("BNTree_MetPhiWithPhiRewtFlat;*");  
    tDir->Delete("BNTree_MetPhiCutPhiLo;*");  
    tDir->Delete("BNTree_MetPhiCutPhiMed;*");  
    tDir->Delete("BNTree_MetPhiCutPhiHi;*");  

  }

  // Declare desired histograms.  
  TH1F* hMet                     = new TH1F("BNTree_Met",                     ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetWithPhiRewtToData    = new TH1F("BNTree_MetWithPhiRewtToData",    ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetWithPhiRewtFlat      = new TH1F("BNTree_MetWithPhiRewtFlat",      ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetPhi                  = new TH1F("BNTree_MetPhi",                  ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiWithPhiRewtToData = new TH1F("BNTree_MetPhiWithPhiRewtToData", ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiWithPhiRewtFlat   = new TH1F("BNTree_MetPhiWithPhiRewtFlat",   ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutPhiLo          = new TH1F("BNTree_MetPhiCutPhiLo",          ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutPhiMed         = new TH1F("BNTree_MetPhiCutPhiMed",         ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutPhiHi          = new TH1F("BNTree_MetPhiCutPhiHi",          ";MET #phi",  100, -3.15, 3.15);  
  
  // Set Sumw2() to get the errors correct 
  hMet                     ->Sumw2();
  hMetWithPhiRewtToData    ->Sumw2();
  hMetWithPhiRewtFlat      ->Sumw2();
  hMetPhi                  ->Sumw2();
  hMetPhiWithPhiRewtToData ->Sumw2();
  hMetPhiWithPhiRewtFlat   ->Sumw2();
  hMetPhiCutPhiLo          ->Sumw2();
  hMetPhiCutPhiMed         ->Sumw2();
  hMetPhiCutPhiHi          ->Sumw2();
  
  Long64_t nentries = fChain->GetEntries();

  double lumiWt = fChain->GetWeight();  // The BNTree weight must be set by mergeOutput.py.  

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
    if (mets_pt->size() < 1) { 
      cout << "Warning:  found event " << jentry << " with no MET." << endl;
      continue;
    }  
    double BNTreeWt = 
      lumiWt * 
      events_puScaleFactor      ->at(0) * 
      events_muonScaleFactor    ->at(0) * 
      events_electronScaleFactor->at(0);  

    // Calculate reweighting.
    double wtToData = hMetPhiDataOverMC->GetBinContent(hMetPhiDataOverMC->FindBin(mets_phi->at(0)));  
    if (isData) wtToData = 1.0;  
    double      wtToFlat = 1.0 / hMetPhiWjets->GetBinContent(hMetPhiWjets->FindBin(mets_phi->at(0)));  
    if (isData) wtToFlat = 1.0 / hMetPhiData ->GetBinContent(hMetPhiData ->FindBin(mets_phi->at(0)));  

    hMet                     ->Fill(mets_pt->at(0), BNTreeWt);  
    hMetWithPhiRewtToData    ->Fill(mets_pt->at(0), BNTreeWt * wtToData);  
    hMetWithPhiRewtFlat      ->Fill(mets_pt->at(0), BNTreeWt * wtToFlat);  

    hMetPhi                  ->Fill(mets_phi->at(0), BNTreeWt);  
    hMetPhiWithPhiRewtToData ->Fill(mets_phi->at(0), BNTreeWt * wtToData);  
    hMetPhiWithPhiRewtFlat   ->Fill(mets_phi->at(0), BNTreeWt * wtToFlat);  
    hMetPhiCutPhiLo          ->Fill(mets_phi->at(0), BNTreeWt * (mets_pt->at(0) < 100));  
    hMetPhiCutPhiMed         ->Fill(mets_phi->at(0), BNTreeWt * (mets_pt->at(0) > 100 && mets_pt->at(0) < 200));  
    hMetPhiCutPhiHi          ->Fill(mets_phi->at(0), BNTreeWt * (mets_pt->at(0) > 200));  


  }  // end   for (Long64_t jentry=0; jentry<nentries;jentry++) {

  cout << "Debug:  mean of hMet = " << hMet->GetMean() << endl;  

  hMet                     ->Write();  
  hMetWithPhiRewtToData    ->Write();  
  hMetWithPhiRewtFlat      ->Write();  
  hMetPhi                  ->Write();  
  hMetPhiWithPhiRewtToData ->Write();  
  hMetPhiWithPhiRewtFlat   ->Write();  
  hMetPhiCutPhiLo          ->Write();  
  hMetPhiCutPhiMed         ->Write();  
  hMetPhiCutPhiHi          ->Write();  
  hMetPhiDataOverMC        ->Write();  

  fOut->Close();  

  cout << "Finished BNTree::Loop() successfully." << endl;
  cout << "Total time to run BNTree::Loop():  " << flush;
  timer.Print();  


} // void BNTree::Loop()

