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



  // Open output root file.  
  TFile* fOut = 0;
  TString dir = "";  
  if (outFile=="") fOut = new TFile("newBNTreePlot.root", "RECREATE");  
  else {
    fOut = new TFile(outFile,              "UPDATE");  
    dir = fChain->GetName();
    dir = dir(0, dir.Last('/'));  
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
    tDir->Delete("BNTree_Met;*");  
  }

  // Declare desired histograms.  
  TH1F* hMet = new TH1F("BNTree_Met", ";MET (GeV)", 100, 0, 500);  


  Long64_t nentries = fChain->GetEntries();

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
      events_puScaleFactor      ->at(0) * 
      events_muonScaleFactor    ->at(0) * 
      events_electronScaleFactor->at(0);  

    hMet->Fill(mets_pt->at(0), BNTreeWt);  
    // cout << "Debug:  met = " << mets_pt->at(0) << std::endl;  
    // cout << "Debug:  met size = " << mets_pt->size() << std::endl;  
    //      std::cout << "Debug:  events_weight = " << events_weight << std::endl;  
    //      cout << "Debug:  events_weight size = " << events_weight->size() << std::endl;  

    // if (Cut(ientry) < 0) continue;
  }

  cout << "Debug:  mean of hMet = " << hMet->GetMean() << endl;  

  // close output root file 
  hMet->Write();
  fOut->Close();  

  cout << "Finished BNTree::Loop() successfully." << endl;
  cout << "Total time:  " << flush;
  timer.Print();  


} // void BNTree::Loop()

