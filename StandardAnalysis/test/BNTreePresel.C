// New histograms must be added in three places:
// * declare
// * fill
// * write


#define BNTreePresel_cxx
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

void BNTreePresel::Loop(TString outFile)
{
  //   In a ROOT session, you can do:
  //      Root > .L BNTreePresel.C
  //      Root > BNTreePresel t
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
  if (outFile=="") fOut = new TFile("newBNTreePreselPlot.root", "RECREATE");  
  else {
    fOut = new TFile(outFile,              "UPDATE");  
    cout << "Debug:  name of dir is: " << dir << endl;  
    fOut->cd(dir);  
  }
  cout << "Will write histograms to file " << fOut->GetName()
       << " in directory:  " << dir << endl;  

  // delete all previously existing instances of all BNTree histograms  
  TDirectory* tDir = fOut->GetDirectory(dir);  
  if (!tDir) {
    cout << "Could not find directory " << dir << endl;  
  } else {
    tDir->Delete("BNHist_*;*");  
  }

  // Declare desired histograms.  
  TH1::SetDefaultSumw2();

  TH1F* hCaloTot                 = new TH1F("BNHist_CaloTot",                 ";Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (GeV) (PU corr.)", 100, 20, 400);  
  TH1F* hCaloTotByP              = new TH1F("BNHist_CaloTotByP",              ";Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)",     100, 0.2, 6);  
  TH1F* hDepTrk                  = new TH1F("BNHist_DepTrk",                  ";Track isolation (PU corr.); #Sigma^{#DeltaR<0.5} p_{T} - p_{T}^{cand} (GeV)", 100, 0, 100);
  TH1F* hNHitsMissOut            = new TH1F("BNHist_NHitsMissOut",            ";Number of Missing Outer Hits", 16, -0.5, 15.5),

  TH1F* hCaloTotCutIso                 = new TH1F("BNHist_CaloTotCutIso",                 ";Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (GeV) (PU corr.)", 100, 20, 400);  
  TH1F* hCaloTotByPCutIso              = new TH1F("BNHist_CaloTotByPCutIso",              ";Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)",     100, 0.2, 6);  
  TH1F* hDepTrkCutIso                  = new TH1F("BNHist_DepTrkCutIso",                  ";Track isolation (PU corr.); #Sigma^{#DeltaR<0.5} p_{T} - p_{T}^{cand} (GeV)", 100, 0, 100);
  TH1F* hNHitsMissOutCutIso            = new TH1F("BNHist_NHitsMissOutCutIso",            ";Number of Missing Outer Hits", 16, -0.5, 15.5),

  TH1F* hCaloTotCutIsoNHits                 = new TH1F("BNHist_CaloTotCutIsoNHits",                 ";Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (GeV) (PU corr.)", 100, 20, 400);  
  TH1F* hCaloTotByPCutIsoNHits              = new TH1F("BNHist_CaloTotByPCutIsoNHits",              ";Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)",     100, 0.2, 6);  
  TH1F* hDepTrkCutIsoNHits                  = new TH1F("BNHist_DepTrkCutIsoNHits",                  ";Track isolation (PU corr.); #Sigma^{#DeltaR<0.5} p_{T} - p_{T}^{cand} (GeV)", 100, 0, 100);
  TH1F* hNHitsMissOutCutIsoNHits            = new TH1F("BNHist_NHitsMissOutCutIsoNHits",            ";Number of Missing Outer Hits", 16, -0.5, 15.5),

    
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
    if (mets_pt->size() < 1) { 
      cout << "Warning:  found event " << jentry << " with no MET." << endl;
      continue;
    }  
    double BNTreeWt = 
      lumiWt * 
      events_puScaleFactor      ->at(0) * 
      events_muonScaleFactor    ->at(0) * 
      events_electronScaleFactor->at(0);  

    // Loop over tracks  
    for (uint itrk = 0; itrk<tracks_pt->size(); itrk++) {
      hCaloTot                 ->Fill(tracks_caloTotDeltaRp5RhoCorr->at(itrk),    BNTreeWt);  	
      hCaloTotByP              ->Fill(tracks_caloTotDeltaRp5ByPRhoCorr->at(itrk), BNTreeWt);  	
      hDepTrk                  ->Fill(tracks_depTrkRp5MinusPt->at(itrk),          BNTreeWt);  	
      hNHitsMissOut            ->Fill(tracks_nHitsMissingOuter->at(itrk),         BNTreeWt);         

      hCaloTotCutIso           ->Fill(tracks_caloTotDeltaRp5RhoCorr->at(itrk),    BNTreeWt * (tracks_depTrkRp5MinusPt < 7));  	
      hCaloTotByPCutIso        ->Fill(tracks_caloTotDeltaRp5ByPRhoCorr->at(itrk), BNTreeWt * (tracks_depTrkRp5MinusPt < 7));  	  	
      hDepTrkCutIso            ->Fill(tracks_depTrkRp5MinusPt->at(itrk),          BNTreeWt * (tracks_depTrkRp5MinusPt < 7));  	  	
      hNHitsMissOutCutIso      ->Fill(tracks_nHitsMissingOuter->at(itrk),         BNTreeWt * (tracks_depTrkRp5MinusPt < 7));  	         

      hCaloTotCutIsoNHits      ->Fill(tracks_caloTotDeltaRp5RhoCorr->at(itrk),    BNTreeWt * (tracks_depTrkRp5MinusPt < 7 && tracks_nHitsMissingOuter >= 3));  	
      hCaloTotByPCutIsoNHits   ->Fill(tracks_caloTotDeltaRp5ByPRhoCorr->at(itrk), BNTreeWt * (tracks_depTrkRp5MinusPt < 7 && tracks_nHitsMissingOuter >= 3));  	  	
      hDepTrkCutIsoNHits       ->Fill(tracks_depTrkRp5MinusPt->at(itrk),          BNTreeWt * (tracks_depTrkRp5MinusPt < 7 && tracks_nHitsMissingOuter >= 3));  	  	
      hNHitsMissOutCutIsoNHits ->Fill(tracks_nHitsMissingOuter->at(itrk),         BNTreeWt * (tracks_depTrkRp5MinusPt < 7 && tracks_nHitsMissingOuter >= 3));  	         

    }  

  }  // end   for (Long64_t jentry=0; jentry<nentries;jentry++) {
  
  TH1F* hCaloTot                 ->Write();  
  TH1F* hCaloTotByP              ->Write();  
  TH1F* hDepTrk                  ->Write();  
  TH1F* hNHitsMissOut            ->Write();  

  TH1F* hCaloTotCutIso           ->Write();  
  TH1F* hCaloTotByPCutIso        ->Write();  
  TH1F* hDepTrkCutIso            ->Write();  
  TH1F* hNHitsMissOutCutIso      ->Write();  

  TH1F* hCaloTotCutIsoNHits      ->Write();  
  TH1F* hCaloTotByPCutIsoNHits   ->Write();  
  TH1F* hDepTrkCutIsoNHits       ->Write();  
  TH1F* hNHitsMissOutCutIsoNHits ->Write();  


  fOut->Close();  

  cout << "Finished BNTreePresel::Loop() successfully." << endl;
  cout << "Total time to run BNTreePresel::Loop():  " << flush;
  timer.Print();  


} // void BNTreePresel::Loop()

