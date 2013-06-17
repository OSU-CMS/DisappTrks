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
  // hard-code the directory for the reweighting histograms
  fData ->GetObject("OSUAnalysis/WToMuSimple/mets_phi", hMetPhiData);  
  fWjets->GetObject("OSUAnalysis/WToMuSimple/mets_phi", hMetPhiWjets);  
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
  TH1F* hMetPhiDataOverMC = (TH1F*) hMetPhiData->Clone("BNHist_MetPhiDataOverMC");  
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

  // delete all previously existing instances of all BNTree histograms  
  TDirectory* tDir = fOut->GetDirectory(dir);  
  if (!tDir) {
    cout << "Could not find directory " << dir << endl;  
  } else {
    // tDir->Delete("BNHist_MetPhiDataOverMC;*");  
    // tDir->Delete("BNHist_Met;*");  
    // tDir->Delete("BNHist_MetWithPhiRewtToData;*");  
    // tDir->Delete("BNHist_MetWithPhiRewtFlat;*");  
    // tDir->Delete("BNHist_MetCutPhiLo;*");  
    // tDir->Delete("BNHist_MetCutPhiMed;*");  
    // tDir->Delete("BNHist_MetCutPhiHi;*");  
    // tDir->Delete("BNHist_MetPhi;*");  
    // tDir->Delete("BNHist_MetPhiWithPhiRewtToData;*");  
    // tDir->Delete("BNHist_MetPhiWithPhiRewtFlat;*");  
    // tDir->Delete("BNHist_MetPhiCutMetLo;*");  
    // tDir->Delete("BNHist_MetPhiCutMetMed;*");  
    // tDir->Delete("BNHist_MetPhiCutMetHi;*");  
    // tDir->Delete("BNHist_MuonPhi;*");  
    // tDir->Delete("BNHist_MuonPhiWithPhiRewtToData;*");  
    // tDir->Delete("BNHist_MuonPhiWithPhiRewtFlat;*");  

    tDir->Delete("BNHist_*;*");  

  }

  // Declare desired histograms.  
  TH1::SetDefaultSumw2();
  TH1F* hMet                     = new TH1F("BNHist_Met",                     ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetWithPhiRewtToData    = new TH1F("BNHist_MetWithPhiRewtToData",    ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetWithPhiRewtFlat      = new TH1F("BNHist_MetWithPhiRewtFlat",      ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhiLo             = new TH1F("BNHist_MetCutPhiLo",             ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhiMed            = new TH1F("BNHist_MetCutPhiMed",            ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhiHi             = new TH1F("BNHist_MetCutPhiHi",             ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi1              = new TH1F("BNHist_MetCutPhi1",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi2              = new TH1F("BNHist_MetCutPhi2",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi3              = new TH1F("BNHist_MetCutPhi3",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi4              = new TH1F("BNHist_MetCutPhi4",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi5              = new TH1F("BNHist_MetCutPhi5",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi6              = new TH1F("BNHist_MetCutPhi6",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi7              = new TH1F("BNHist_MetCutPhi7",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi8              = new TH1F("BNHist_MetCutPhi8",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi9              = new TH1F("BNHist_MetCutPhi9",              ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi10             = new TH1F("BNHist_MetCutPhi10",             ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi11             = new TH1F("BNHist_MetCutPhi11",             ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhi12             = new TH1F("BNHist_MetCutPhi12",             ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhiLoRewtToData   = new TH1F("BNHist_MetCutPhiLoRewtToData",   ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhiMedRewtToData  = new TH1F("BNHist_MetCutPhiMedRewtToData",  ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutPhiHiRewtToData   = new TH1F("BNHist_MetCutPhiHiRewtToData",   ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets0            = new TH1F("BNHist_MetCutNJets0",            ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets1            = new TH1F("BNHist_MetCutNJets1",            ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets2            = new TH1F("BNHist_MetCutNJets2",            ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets3            = new TH1F("BNHist_MetCutNJets3",            ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets4            = new TH1F("BNHist_MetCutNJets4",            ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets0RewtToData  = new TH1F("BNHist_MetCutNJets0RewtToData",  ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets1RewtToData  = new TH1F("BNHist_MetCutNJets1RewtToData",  ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets2RewtToData  = new TH1F("BNHist_MetCutNJets2RewtToData",  ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets3RewtToData  = new TH1F("BNHist_MetCutNJets3RewtToData",  ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetCutNJets4RewtToData  = new TH1F("BNHist_MetCutNJets4RewtToData",  ";MET (GeV)", 100, 0, 500);  
  TH1F* hMetPhi                  = new TH1F("BNHist_MetPhi",                  ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiWithPhiRewtToData = new TH1F("BNHist_MetPhiWithPhiRewtToData", ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiWithPhiRewtFlat   = new TH1F("BNHist_MetPhiWithPhiRewtFlat",   ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutMetLo          = new TH1F("BNHist_MetPhiCutMetLo",          ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutMetMed         = new TH1F("BNHist_MetPhiCutMetMed",         ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutMetHi          = new TH1F("BNHist_MetPhiCutMetHi",          ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutPhiLo          = new TH1F("BNHist_MetPhiCutPhiLo",          ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutPhiMed         = new TH1F("BNHist_MetPhiCutPhiMed",         ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMetPhiCutPhiHi          = new TH1F("BNHist_MetPhiCutPhiHi",          ";MET #phi",  100, -3.15, 3.15);  
  TH1F* hMuonPhi                 = new TH1F("BNHist_MuonPhi",                 ";#mu #phi",  100, -3.15, 3.15);  
  TH1F* hMuonPhiPhiRewtToData    = new TH1F("BNHist_MuonPhiWithPhiRewtToData",";#mu #phi",  100, -3.15, 3.15);  
  TH1F* hMuonPhiPhiRewtFlat      = new TH1F("BNHist_MuonPhiWithPhiRewtFlat",  ";#mu #phi",  100, -3.15, 3.15);  
  TH1F* hJetPt                   = new TH1F("BNHist_JetPt",                   ";jet p_{T} (GeV)", 100, 0, 500);  
  TH1F* hJetEta                  = new TH1F("BNHist_JetEta",                  ";jet #eta",  100, -5.0,  5.0);  
  TH1F* hJetIDLoose              = new TH1F("BNHist_JetIDLoose",              ";jet ID Loose", 11, -0.5, 10.5);  
  TH1F* hNJets                   = new TH1F("BNHist_NJets",                   ";N(jets)",      21, -0.5, 20.5);  
  TH1F* hMetCutNJets0PU1         = new TH1F("BNHist_MetCutNJets0PU1",         ";MET (GeV) (0 jets,    #PV<5)",  100, 0, 500);  
  TH1F* hMetCutNJets0PU2         = new TH1F("BNHist_MetCutNJets0PU2",         ";MET (GeV) (0 jets, 5 <#PV<10)", 100, 0, 500);  
  TH1F* hMetCutNJets0PU3         = new TH1F("BNHist_MetCutNJets0PU3",         ";MET (GeV) (0 jets, 10<#PV<15)", 100, 0, 500);  
  TH1F* hMetCutNJets0PU4         = new TH1F("BNHist_MetCutNJets0PU4",         ";MET (GeV) (0 jets, 15<#PV<20)", 100, 0, 500);  
  TH1F* hMetCutNJets0PU5         = new TH1F("BNHist_MetCutNJets0PU5",         ";MET (GeV) (0 jets, 20<#PV<25)", 100, 0, 500);  
  TH1F* hMetCutNJets0PU6         = new TH1F("BNHist_MetCutNJets0PU6",         ";MET (GeV) (0 jets, 25<#PV<30)", 100, 0, 500);  
  TH1F* hMetCutNJets0PU7         = new TH1F("BNHist_MetCutNJets0PU7",         ";MET (GeV) (0 jets, 30<#PV)",    100, 0, 500);  
  TH1F* hNPVPU1         = new TH1F("BNHist_NPVPU1",         ";NumPV (0 jets, #PV<5)",     50, 0, 50);  
  TH1F* hNPVPU2         = new TH1F("BNHist_NPVPU2",         ";NumPV (0 jets, 5 <#PV<10)", 50, 0, 50);  
  TH1F* hNPVPU3         = new TH1F("BNHist_NPVPU3",         ";NumPV (0 jets, 10<#PV<15)", 50, 0, 50);  
  TH1F* hNPVPU4         = new TH1F("BNHist_NPVPU4",         ";NumPV (0 jets, 15<#PV<20)", 50, 0, 50);  
  TH1F* hNPVPU5         = new TH1F("BNHist_NPVPU5",         ";NumPV (0 jets, 20<#PV<25)", 50, 0, 50);  
  TH1F* hNPVPU6         = new TH1F("BNHist_NPVPU6",         ";NumPV (0 jets, 25<#PV<30)", 50, 0, 50);  
  TH1F* hNPVPU7         = new TH1F("BNHist_NPVPU7",         ";NumPV (0 jets, 30<#PV)",    50, 0, 50);  
    
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

    // Calculate reweighting.
    double wtToData = hMetPhiDataOverMC->GetBinContent(hMetPhiDataOverMC->FindBin(mets_phi->at(0)));  
    if (isData) wtToData = 1.0;  
    double      wtToFlat = 1.0 / hMetPhiWjets->GetBinContent(hMetPhiWjets->FindBin(mets_phi->at(0)));  
    if (isData) wtToFlat = 1.0 / hMetPhiData ->GetBinContent(hMetPhiData ->FindBin(mets_phi->at(0)));  

    // Count number of jets
    int njets = 0;
    for (uint ijet = 0; ijet<jets_pt->size(); ijet++) {
      if (jets_pt->at(ijet) < 30)               continue;  
      if (fabs(jets_eta->at(ijet)) > 2.4)       continue;  
      if (jets_jetIDLoose->at(ijet) == 0)       continue;  
      hJetPt ->Fill(jets_pt ->at(ijet),            BNTreeWt);  
      hJetEta->Fill(jets_eta->at(ijet),            BNTreeWt);  
      hJetIDLoose->Fill(jets_jetIDLoose->at(ijet), BNTreeWt);  
      njets++;  
    }  
    hNJets->Fill(njets, BNTreeWt);  

    // Fill histograms
    hMet                     ->Fill(mets_pt->at(0), BNTreeWt);  
    hMetWithPhiRewtToData    ->Fill(mets_pt->at(0), BNTreeWt * wtToData);  
    hMetWithPhiRewtFlat      ->Fill(mets_pt->at(0), BNTreeWt * wtToFlat);  
    
    hMetCutPhiLo             ->Fill(mets_pt->at(0), BNTreeWt * (fabs(mets_phi->at(0))<1.0));  
    hMetCutPhiMed            ->Fill(mets_pt->at(0), BNTreeWt * (fabs(mets_phi->at(0))>1.0 && fabs(mets_phi->at(0))<2.0));  
    hMetCutPhiHi             ->Fill(mets_pt->at(0), BNTreeWt * (fabs(mets_phi->at(0))>2.0));  
    
    hMetCutPhi1              ->Fill(mets_pt->at(0), BNTreeWt * (                          mets_phi->at(0) < -2.5));  
    hMetCutPhi2              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) > -2.5 && mets_phi->at(0) < -2.0));  
    hMetCutPhi3              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) > -2.0 && mets_phi->at(0) < -1.5));  
    hMetCutPhi4              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) > -1.5 && mets_phi->at(0) < -1.0));  
    hMetCutPhi5              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) > -1.0 && mets_phi->at(0) < -0.5));  
    hMetCutPhi6              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) > -0.5 && mets_phi->at(0) <  0.0));  
    hMetCutPhi7              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) >  0.0 && mets_phi->at(0) <  0.5));  
    hMetCutPhi8              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) >  0.5 && mets_phi->at(0) <  1.0));  
    hMetCutPhi9              ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) >  1.0 && mets_phi->at(0) <  1.5));  
    hMetCutPhi10             ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) >  1.5 && mets_phi->at(0) <  2.0));  
    hMetCutPhi11             ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) >  2.0 && mets_phi->at(0) <  2.5));  
    hMetCutPhi12             ->Fill(mets_pt->at(0), BNTreeWt * (mets_phi->at(0) >  2.5 ));  
    
    hMetCutPhiLoRewtToData   ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (fabs(mets_phi->at(0))<1.0));  
    hMetCutPhiMedRewtToData  ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (fabs(mets_phi->at(0))>1.0 && fabs(mets_phi->at(0))<2.0));  
    hMetCutPhiHiRewtToData   ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (fabs(mets_phi->at(0))>2.0));  

    hMetCutNJets0            ->Fill(mets_pt->at(0), BNTreeWt * (njets==0));  
    hMetCutNJets1            ->Fill(mets_pt->at(0), BNTreeWt * (njets==1));  
    hMetCutNJets2            ->Fill(mets_pt->at(0), BNTreeWt * (njets==2));  
    hMetCutNJets3            ->Fill(mets_pt->at(0), BNTreeWt * (njets==3));  
    hMetCutNJets4            ->Fill(mets_pt->at(0), BNTreeWt * (njets>=4));  

    hMetCutNJets0PU1         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 &&                             events_numPV->at(0) < 5));  
    hMetCutNJets0PU2         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 &&  5 < events_numPV->at(0) && events_numPV->at(0) < 10));  
    hMetCutNJets0PU3         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 && 10 < events_numPV->at(0) && events_numPV->at(0) < 15));  
    hMetCutNJets0PU4         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 && 15 < events_numPV->at(0) && events_numPV->at(0) < 20));  
    hMetCutNJets0PU5         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 && 20 < events_numPV->at(0) && events_numPV->at(0) < 25));  
    hMetCutNJets0PU6         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 && 25 < events_numPV->at(0) && events_numPV->at(0) < 30));  
    hMetCutNJets0PU7         ->Fill(mets_pt->at(0), BNTreeWt * (njets==0 && 30 < events_numPV->at(0)) );  

    hNPVPU1                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 &&                             events_numPV->at(0) < 5));  
    hNPVPU2                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 &&  5 < events_numPV->at(0) && events_numPV->at(0) < 10));  
    hNPVPU3                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 && 10 < events_numPV->at(0) && events_numPV->at(0) < 15));  
    hNPVPU4                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 && 15 < events_numPV->at(0) && events_numPV->at(0) < 20));  
    hNPVPU5                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 && 20 < events_numPV->at(0) && events_numPV->at(0) < 25));  
    hNPVPU6                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 && 25 < events_numPV->at(0) && events_numPV->at(0) < 30));  
    hNPVPU7                  ->Fill(events_numPV->at(0), BNTreeWt * (njets==0 && 30 < events_numPV->at(0)));  


    hMetCutNJets0RewtToData  ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (njets==0));  
    hMetCutNJets1RewtToData  ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (njets==1));  
    hMetCutNJets2RewtToData  ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (njets==2));  
    hMetCutNJets3RewtToData  ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (njets==3));  
    hMetCutNJets4RewtToData  ->Fill(mets_pt->at(0), BNTreeWt * wtToData * (njets>=4));  

    hMetPhi                  ->Fill(mets_phi->at(0), BNTreeWt);  
    hMetPhiWithPhiRewtToData ->Fill(mets_phi->at(0), BNTreeWt * wtToData);  
    hMetPhiWithPhiRewtFlat   ->Fill(mets_phi->at(0), BNTreeWt * wtToFlat);  
    hMetPhiCutMetLo          ->Fill(mets_phi->at(0), BNTreeWt * (mets_pt->at(0) < 100));  
    hMetPhiCutMetMed         ->Fill(mets_phi->at(0), BNTreeWt * (mets_pt->at(0) > 100 && mets_pt->at(0) < 200));  
    hMetPhiCutMetHi          ->Fill(mets_phi->at(0), BNTreeWt * (mets_pt->at(0) > 200));  

    // hMetPhiCutMetLoRewtToData ->Fill(mets_phi->at(0), BNTreeWt * wtToData * (mets_pt->at(0) < 100));  
    // hMetPhiCutMetMedRewtToData->Fill(mets_phi->at(0), BNTreeWt * wtToData * (mets_pt->at(0) > 100 && mets_pt->at(0) < 200));  
    // hMetPhiCutMetHiRewtToData ->Fill(mets_phi->at(0), BNTreeWt * wtToData * (mets_pt->at(0) > 200));  

    hMetPhiCutPhiLo          ->Fill(mets_phi->at(0), BNTreeWt * (fabs(mets_phi->at(0))<1.0));  
    hMetPhiCutPhiMed         ->Fill(mets_phi->at(0), BNTreeWt * (fabs(mets_phi->at(0))>1.0 && fabs(mets_phi->at(0))<2.0));  
    hMetPhiCutPhiHi          ->Fill(mets_phi->at(0), BNTreeWt * (fabs(mets_phi->at(0))>2.0));  


    hMuonPhi                 ->Fill(muons_phi->at(0), BNTreeWt);  
    hMuonPhiPhiRewtToData    ->Fill(muons_phi->at(0), BNTreeWt * wtToData);  
    hMuonPhiPhiRewtFlat      ->Fill(muons_phi->at(0), BNTreeWt * wtToFlat);  


  }  // end   for (Long64_t jentry=0; jentry<nentries;jentry++) {
  
  cout << "Debug:  mean of hMet = " << hMet->GetMean() << endl;  
  
  hMet                     ->Write();  
  hMetWithPhiRewtToData    ->Write();  
  hMetWithPhiRewtFlat      ->Write();  
  hMetCutPhiLo             ->Write();  
  hMetCutPhiMed            ->Write();  
  hMetCutPhiHi             ->Write();  
  hMetCutPhi1              ->Write();  
  hMetCutPhi2              ->Write();  
  hMetCutPhi3              ->Write();  
  hMetCutPhi4              ->Write();  
  hMetCutPhi5              ->Write();  
  hMetCutPhi6              ->Write();  
  hMetCutPhi7              ->Write();  
  hMetCutPhi8              ->Write();  
  hMetCutPhi9              ->Write();  
  hMetCutPhi10             ->Write();  
  hMetCutPhi11             ->Write();  
  hMetCutPhi12             ->Write();  
  hMetCutPhiLoRewtToData   ->Write();  
  hMetCutPhiMedRewtToData  ->Write();  
  hMetCutPhiHiRewtToData   ->Write();  
  hMetCutNJets0            ->Write();  
  hMetCutNJets1            ->Write();  
  hMetCutNJets2            ->Write();  
  hMetCutNJets3            ->Write();  
  hMetCutNJets4            ->Write();  
  hMetCutNJets0PU1         ->Write();
  hMetCutNJets0PU2         ->Write();
  hMetCutNJets0PU3         ->Write();
  hMetCutNJets0PU4         ->Write();
  hMetCutNJets0PU5         ->Write();
  hMetCutNJets0PU6         ->Write();
  hMetCutNJets0PU7         ->Write();
  hNPVPU1                  ->Write();
  hNPVPU2                  ->Write();
  hNPVPU3                  ->Write();
  hNPVPU4                  ->Write();
  hNPVPU5                  ->Write();
  hNPVPU6                  ->Write();
  hNPVPU7                  ->Write();
  hMetCutNJets0RewtToData  ->Write();  
  hMetCutNJets1RewtToData  ->Write();  
  hMetCutNJets2RewtToData  ->Write();  
  hMetCutNJets3RewtToData  ->Write();  
  hMetCutNJets4RewtToData  ->Write();  
  hMetPhi                  ->Write();  
  hMetPhiWithPhiRewtToData ->Write();  
  hMetPhiWithPhiRewtFlat   ->Write();  
  hMetPhiCutMetLo          ->Write();  
  hMetPhiCutMetMed         ->Write();  
  hMetPhiCutMetHi          ->Write();  
  hMetPhiCutPhiLo          ->Write();  
  hMetPhiCutPhiMed         ->Write();  
  hMetPhiCutPhiHi          ->Write();  
  hMetPhiDataOverMC        ->Write();  
  hMuonPhi                 ->Write();  
  hMuonPhiPhiRewtToData    ->Write();  
  hMuonPhiPhiRewtFlat      ->Write();  
  hNJets                   ->Write();  
  hJetPt                   ->Write();  
  hJetEta                  ->Write();  
  hJetIDLoose              ->Write();  


  fOut->Close();  

  cout << "Finished BNTree::Loop() successfully." << endl;
  cout << "Total time to run BNTree::Loop():  " << flush;
  timer.Print();  


} // void BNTree::Loop()

