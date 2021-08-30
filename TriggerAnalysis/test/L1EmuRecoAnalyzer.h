//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Jul  7 08:39:22 2021 by ROOT version 6.22/06
// from TTree L1EmuTree/L1EmuTree
// found on file: histo.root
//////////////////////////////////////////////////////////

#ifndef L1EmuRecoAnalyzer_h
#define L1EmuRecoAnalyzer_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TMath.h>
#include <TH1.h>
// Header file for the classes stored in the TTree if any.
#include "vector"

class L1EmuRecoAnalyzer {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Bool_t          isGoodPV;
   Double_t        L1ETMHFPt;
   Double_t        L1ETMHFPhi;
   vector<double>  *L1JetPt;
   vector<double>  *L1JetPhi;
   vector<double>  *L1dPhiJetMet;
   Double_t        L1HTT;
   Double_t        PFMetPt;
   Double_t        PFMetNoMuPt;
   Double_t        PFMetNoMuPhi;
   vector<double>  *PFJetPt;
   vector<double>  *PFJetEta;
   vector<double>  *PFJetPhi;
   vector<double>  *PFJetTightLepVeto;
   Bool_t          passL1EmuSelection;
   Bool_t          passOfflineSelection;

   // List of branches
   TBranch        *b_isGoodPV;   //!
   TBranch        *b_L1ETMHFPt;   //!
   TBranch        *b_L1ETMHFPhi;   //!
   TBranch        *b_L1JetPt;   //!
   TBranch        *b_L1JetPhi;   //!
   TBranch        *b_L1dPhiJetMet;   //!
   TBranch        *b_L1HTT;   //!
   TBranch        *b_PFMetPt;   //!
   TBranch        *b_PFMetNoMuPt;   //!
   TBranch        *b_PFMetNoMuPhi;   //!
   TBranch        *b_PFJetPt;   //!
   TBranch        *b_PFJetEta;   //!
   TBranch        *b_PFJetPhi;   //!
   TBranch        *b_PFJetTightLepVeto;   //!
   TBranch        *b_passL1EmuSelection;   //!
   TBranch        *b_passOfflineSelection;   //!


   TH1D *EMTHF = new TH1D("EMTHF", "EMTHF",200, -0.5, 999.5);
   TH1D *HTT   = new TH1D("HTT", "HTT",100, -0.5, 999.5);
   TH1D *JetPt = new TH1D("JetPt", "JetPt",100, -0.5, 999.5);
   TH1D *dPhi  = new TH1D("dPhi","dPhi", 30, 0, 3.15);

   TH1D *EMTHF_offline = new TH1D("EMTHF_offline", "EMTHF_offline",200, -0.5, 999.5);
   TH1D *HTT_offline   = new TH1D("HTT_offline", "HTT_offline",100, -0.5, 999.5);
   TH1D *JetPt_offline = new TH1D("JetPt_offline", "JetPt_offline",100, -0.5, 999.5);
   TH1D *dPhi_offline  = new TH1D("dPhi_offline","dPhi_offline", 30, 0, 3.15);

   TH1D *efficiencyOverEMTHF = new TH1D("efficiencyOverEMTHFThreshold", "efficiency over EMTHF Threshold",200, -0.5, 999.5);
   TH1D *efficiencyOverHTTThreshold = new TH1D("efficiencyOverHTTThreshold", "efficiency over HTT Threshold",100, -0.5, 999.5);
   TH1D *efficiencyOverJetPtThreshold = new TH1D("efficiencyOverHTTThreshold", "efficiency over HTT Threshold",100, -0.5, 999.5);
   TH1D *efficiencyOverdPhi = new TH1D("efficiencyOverdPhi","efficiency over dPhi", 30, 0, 3.15);

   Int_t nPassOffline = 0;

   L1EmuRecoAnalyzer(TTree *tree=0);
   virtual ~L1EmuRecoAnalyzer();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual void     Finish();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef L1EmuRecoAnalyzer_cxx
L1EmuRecoAnalyzer::L1EmuRecoAnalyzer(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("histo_N1300.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("histo_N1300.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("histo_N1300.root:/printer");
      dir->GetObject("L1EmuTree",tree);

   }
   Init(tree);
}

L1EmuRecoAnalyzer::~L1EmuRecoAnalyzer()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t L1EmuRecoAnalyzer::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t L1EmuRecoAnalyzer::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void L1EmuRecoAnalyzer::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   L1JetPt = 0;
   L1JetPhi = 0;
   L1dPhiJetMet = 0;
   PFJetPt = 0;
   PFJetEta = 0;
   PFJetPhi = 0;
   PFJetTightLepVeto = 0;

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("isGoodPV", &isGoodPV, &b_isGoodPV);
   fChain->SetBranchAddress("L1ETMHFPt", &L1ETMHFPt, &b_L1ETMHFPt);
   fChain->SetBranchAddress("L1ETMHFPhi", &L1ETMHFPhi, &b_L1ETMHFPhi);
   fChain->SetBranchAddress("L1JetPt", &L1JetPt, &b_L1JetPt);
   fChain->SetBranchAddress("L1JetPhi", &L1JetPhi, &b_L1JetPhi);
   fChain->SetBranchAddress("L1dPhiJetMet", &L1dPhiJetMet, &b_L1dPhiJetMet);
   fChain->SetBranchAddress("L1HTT", &L1HTT, &b_L1HTT);
   fChain->SetBranchAddress("PFMetPt", &PFMetPt, &b_PFMetPt);
   fChain->SetBranchAddress("PFMetNoMuPt", &PFMetNoMuPt, &b_PFMetNoMuPt);
   fChain->SetBranchAddress("PFMetNoMuPhi", &PFMetNoMuPhi, &b_PFMetNoMuPhi);
   fChain->SetBranchAddress("PFJetPt", &PFJetPt, &b_PFJetPt);
   fChain->SetBranchAddress("PFJetEta", &PFJetEta, &b_PFJetEta);
   fChain->SetBranchAddress("PFJetPhi", &PFJetPhi, &b_PFJetPhi);
   fChain->SetBranchAddress("PFJetTightLepVeto", &PFJetTightLepVeto, &b_PFJetTightLepVeto);
   fChain->SetBranchAddress("passL1EmuSelection", &passL1EmuSelection, &b_passL1EmuSelection);
   fChain->SetBranchAddress("passOfflineSelection", &passOfflineSelection, &b_passOfflineSelection);

   double dPhi_Threshold = 2.0;

   Notify();
}

Bool_t L1EmuRecoAnalyzer::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void L1EmuRecoAnalyzer::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t L1EmuRecoAnalyzer::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef L1EmuRecoAnalyzer_cxx
