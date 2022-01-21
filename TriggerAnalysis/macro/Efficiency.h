//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Sep  2 20:28:57 2021 by ROOT version 6.22/09
// from TTree tree/tree
// found on file: histo.root
//////////////////////////////////////////////////////////

#ifndef Efficiency_h
#define Efficiency_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1D.h>
#include <TString.h>
#include <TLegend.h>
// Header file for the classes stored in the TTree if any.
#include "vector"
#include "vector"

class Efficiency {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain
   TString         fTriggerName;
// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Bool_t          hasGoodPV;
   Bool_t          hasGoodJet;
   Double_t        maxJetsDPhi;
   Double_t        dPhi_Jet_METNoMu;
   Double_t        MetPt;
   Double_t        MetNoMuPt;
   vector<double>  *JetPt;
   vector<double>  *JetEta;
   vector<bool>    *JetTightLepVeto;
   Bool_t          fireTrigger;
   Double_t        offlineIsoTrkPt;
   Bool_t          offlineSelection;
   Bool_t          offlineSelection_NoMETNoMu;

   // List of branches
   TBranch        *b_hasGoodPV;   //!
   TBranch        *b_hasGoodJet;   //!
   TBranch        *b_maxJetsDPhi;   //!
   TBranch        *b_dPhi_Jet_METNoMu;   //!
   TBranch        *b_MetPt;   //!
   TBranch        *b_MetNoMuPt;   //!
   TBranch        *b_JetPt;   //!
   TBranch        *b_JetEta;   //!
   TBranch        *b_JetTightLepVeto;   //!
   TBranch        *b_fireTrigger;   //!
   TBranch        *b_offlineIsoTrkPt;   //!
   TBranch        *b_offlineSelection;   //!
   TBranch        *b_offlineSelection_NoMETNoMu;   //!

   TH1D *METNoMuDenominator = new TH1D("METNoMuDenominator", "offline w/o METNoMu",50, -0.5, 499.5);
   TH1D *METNoMuNumerator   = new TH1D("METNoMuNumerator", "trigger fired with offline w/o METNoMu",50, -0.5, 499.5);
   TH1D *METNoMuEfficiency  = new TH1D("METNoMuEfficiency", "efficiency over METNoMu", 50, -0.5, 499.5);

   Efficiency(TString triggerName = "trigger",TTree *tree=0);
   virtual ~Efficiency();
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

#ifdef Efficiency_cxx
Efficiency::Efficiency(TString triggerName, TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   fTriggerName = triggerName;
   TString fileName = "histo_"+triggerName+".root";
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject(fileName);
      if (!f || !f->IsOpen()) {
         f = new TFile(fileName);
      }
      TDirectory * dir = (TDirectory*)f->Get(fileName+":/efficiency");
      dir->GetObject("tree",tree);
   }
   
   Init(tree);
}

Efficiency::~Efficiency()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t Efficiency::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Efficiency::LoadTree(Long64_t entry)
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

void Efficiency::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   JetPt = 0;
   JetEta = 0;
   JetTightLepVeto = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("hasGoodPV", &hasGoodPV, &b_hasGoodPV);
   fChain->SetBranchAddress("hasGoodJet", &hasGoodJet, &b_hasGoodJet);
   fChain->SetBranchAddress("maxJetsDPhi", &maxJetsDPhi, &b_maxJetsDPhi);
   fChain->SetBranchAddress("dPhi_Jet_METNoMu", &dPhi_Jet_METNoMu, &b_dPhi_Jet_METNoMu);
   fChain->SetBranchAddress("MetPt", &MetPt, &b_MetPt);
   fChain->SetBranchAddress("MetNoMuPt", &MetNoMuPt, &b_MetNoMuPt);
   fChain->SetBranchAddress("JetPt", &JetPt, &b_JetPt);
   fChain->SetBranchAddress("JetEta", &JetEta, &b_JetEta);
   fChain->SetBranchAddress("JetTightLepVeto", &JetTightLepVeto, &b_JetTightLepVeto);
   fChain->SetBranchAddress("fireTrigger", &fireTrigger, &b_fireTrigger);
   fChain->SetBranchAddress("offlineIsoTrkPt", &offlineIsoTrkPt, &b_offlineIsoTrkPt);
   fChain->SetBranchAddress("offlineSelection", &offlineSelection, &b_offlineSelection);
   fChain->SetBranchAddress("offlineSelection_NoMETNoMu", &offlineSelection_NoMETNoMu, &b_offlineSelection_NoMETNoMu);
   Notify();
}

Bool_t Efficiency::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Efficiency::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Efficiency::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef Efficiency_cxx
