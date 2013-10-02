// New histograms must be added in three places:
// * declare
// * fill
// * write

// Execution history:
// makeBNTreePlot.py -D AMSB_mGrav50K_0p5ns_Reco -l BNTreePlotMonojet.py -c condor_2013_06_19_Monojet
// makeBNTreePlot.py -C -l BNTreePlotMonojet.py -c condor_2013_06_19_Monojet 

#define BNTree_cxx
#include "BNTree.h"
#include <TH1F.h>
#include <TH2.h>
#include <TVector2.h>
#include <TStopwatch.h>
#include <TProfile.h>
#include <TString.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream> 
#include <cmath>
#include <math.h>
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"

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

  bool isData = outFile.Contains("MET");  

  // delete all previously existing instances of all BNHist histograms  
  TDirectory* tDir = fOut->GetDirectory(dir);  
  if (!tDir) {
    cout << "Could not find directory " << dir << endl;  
  } else {
    tDir->Delete("BNHist_*;*");  
  }

  // Declare desired histograms.  
  TH1::SetDefaultSumw2();

  TH1F* hNJets                   = new TH1F("BNHist_NJets",                 ";Jet mulitiplicity",      11, -0.5, 10.5);     
  TH1F* hEvtIsGoodVtx            = new TH1F("BNHist_EvtIsGoodVtx",          ";is good primary vertex", 11, -0.5, 10.5);     

  TH1F* numPV                    = new TH1F("BNHist_numPV",                 ";# primary vertices", 70, 0, 70);  
  TH1F* METPre                   = new TH1F("BNHist_METPre",                ";MET [GeV]", 100, 0, 500);  
  TH1F* MET                      = new TH1F("BNHist_MET",                   ";MET [GeV]", 32, 200, 1000);  
  TH1F* METPhiCorr               = new TH1F("BNHist_METPhiCorr",                 ";MET Phi Corr", 100, -4, 4);
  TH1F* METPhi                   = new TH1F("BNHist_METPhi",                 ";MET Phi", 100, -4, 4);
  TH1F* MetDPhi_Check            = new TH1F("BNHist_METDPhi_Check",                 ";MET Phi Check", 100, -0.5, 0.5);
  TH1F* MetDPhi                  = new TH1F("BNHist_METDPhi",                 ";Phi Corr - Phi Reg", 100, -0.5, 0.5);
  TH1F* METCorr                  = new TH1F("BNHist_METCorr",                 ";MET Corr", 100, 0, 500);
  TH1F* METFull                  = new TH1F("BNHist_METFull",               ";MET [GeV]", 40, 0, 1000);  
  TH1F* jetChargedHadFrac        = new TH1F("BNHist_jetChargedHadFrac",     ";ChargedHadFrac", 60,  0.0, 1.2);  
  TH1F* jetNeutralHadFrac        = new TH1F("BNHist_jetNeutralHadFrac",     ";NeutralHadFrac", 60, -0.1, 1.1);  
  TH1F* jetChargedEMFrac         = new TH1F("BNHist_jetChargedEMFrac",      ";ChargedEMFrac",  60, -0.1, 1.1);  
  TH1F* jetNeutralEMFrac         = new TH1F("BNHist_jetNeutralEMFrac",      ";NeutralEMFrac",  60, -0.1, 1.1);  
  TH1F* jetOneEta                = new TH1F("BNHist_jetOneEta",             ";Jet1 #eta", 36, -3.6, 3.6);  
  TH1F* jetOnePt                 = new TH1F("BNHist_jetOnePt",              ";Jet1 pT [GeV]", 40, 0, 1000);  

  //jet hists that also contain a candidate trk requirement
  TH1F* METFullPTrk              = new TH1F("BNHist_METFullPTrk",               ";MET [GeV]", 40, 0, 1000);
  TH1F* jetChargedHadFracPTrk    = new TH1F("BNHist_jetChargedHadFracPTrk",     ";ChargedHadFrac", 60,  0.0, 1.2);
  TH1F* jetNeutralHadFracPTrk    = new TH1F("BNHist_jetNeutralHadFracPTrk",     ";NeutralHadFrac", 60, -0.1, 1.1);
  TH1F* jetChargedEMFracPTrk     = new TH1F("BNHist_jetChargedEMFracPTrk",      ";ChargedEMFrac",  60, -0.1, 1.1);
  TH1F* jetNeutralEMFracPTrk     = new TH1F("BNHist_jetNeutralEMFracPTrk",      ";NeutralEMFrac",  60, -0.1, 1.1);
  TH1F* jetOneEtaPTrk            = new TH1F("BNHist_jetOneEtaPTrk",             ";Jet1 #eta", 36, -3.6, 3.6);
  TH1F* jetOnePtPTrk             = new TH1F("BNHist_jetOnePtPTrk",              ";Jet1 pT [GeV]", 40, 0, 1000);



  TH1F* jetTwoChHadFrac          = new TH1F("BNHist_jetTwoChHadFrac",       ";Jet2 Charged Had Frac", 60,  0.0, 1.2);  
  TH1F* jetTwoNeutralHadFrac     = new TH1F("BNHist_jetTwoNeutralHadFrac",  ";Jet2 Neutral Had Frac", 60, -0.1, 1.1);  
  TH1F* jetTwoChEMFrac           = new TH1F("BNHist_jetTwoChEMFrac",        ";Jet2 Charged EM Frac",  60, -0.1, 1.1);  
  TH1F* jetTwoNeutralEMFrac      = new TH1F("BNHist_jetTwoNeutralEMFrac",   ";Jet2 Neutral EM Frac",  60, -0.1, 1.1);  
  TH1F* jetTwoEta                = new TH1F("BNHist_jetTwoEta",             ";Jet2 #eta", 60, -5, 5);  
  TH1F* jetTwoPt                 = new TH1F("BNHist_jetTwoPt",              ";Jet2 pT", 25, 0, 600);  
  TH1F* jetOneMetDPhi            = new TH1F("BNHist_jetOneMetDPhi",         ";#Delta #phi (Jet1, MET)",  35, 0, 3.5);  
  TH1F* jetTwoMetDPhi            = new TH1F("BNHist_jetTwoMetDPhi",         ";#Delta #phi (Jet2, MET)",  35, 0, 3.5);  
  TH1F* jetDPhi                  = new TH1F("BNHist_jetDPhi",               ";#Delta #phi (Jet1, Jet2)", 35, 0, 3.5);  
  TH1F* jetJetDeltaPhi                  = new TH1F("BNHist_jetJetDeltaPhi",               ";#Delta #phi (Jet1, Jet2)", 100, -3.5, 3.5);  


  TH1F* hNElecs                  = new TH1F("BNHist_NElecs",                ";Elec mulitiplicity",               11, -0.5, 10.5);   
  TH1F* hNMuons                  = new TH1F("BNHist_NMuons",                ";Muon mulitiplicity", 		 11, -0.5, 10.5);   
  TH1F* hNTaus                   = new TH1F("BNHist_NTaus",                 ";Tau  mulitiplicity", 		 11, -0.5, 10.5);   
  TH1F* hNElecsNoCut             = new TH1F("BNHist_NElecsNoCut",           ";Elec mulitiplicity (no elec cut)", 11, -0.5, 10.5);   
  TH1F* hNMuonsNoCut             = new TH1F("BNHist_NMuonsNoCut",           ";Muon mulitiplicity (no muon cut)", 11, -0.5, 10.5);   
  TH1F* hNTausNoCut              = new TH1F("BNHist_NTausNoCut",            ";Tau  mulitiplicity (no tau cut)",  11, -0.5, 10.5);   
  TH1F* hNMets                   = new TH1F("BNHist_NMets",                 ";Met mulitiplicity",                11, -0.5, 10.5);  
  TH1F* hNMetsCut0               = new TH1F("BNHist_NMetsCut0",             ";Met mulitiplicity (cut 0)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut1               = new TH1F("BNHist_NMetsCut1",             ";Met mulitiplicity (cut 1)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut1A               = new TH1F("BNHist_NMetsCut1A",             ";Met mulitiplicity (cut 1a)",     11, -0.5, 10.5);
  TH1F* hNMetsCut1B               = new TH1F("BNHist_NMetsCut1B",             ";Met mulitiplicity (cut 1b)",     11, -0.5, 10.5);
  TH1F* hNMetsCut1C               = new TH1F("BNHist_NMetsCut1C",             ";Met mulitiplicity (cut 1c)",     11, -0.5, 10.5);
  TH1F* hNMetsCut1D               = new TH1F("BNHist_NMetsCut1D",             ";Met mulitiplicity (cut 1d)",     11, -0.5, 10.5);
  TH1F* hNMetsCut1E               = new TH1F("BNHist_NMetsCut1E",             ";Met mulitiplicity (cut 1e)",     11, -0.5, 10.5);
  TH1F* hNMetsCut1F               = new TH1F("BNHist_NMetsCut1F",             ";Met mulitiplicity (cut 1f)",     11, -0.5, 10.5);
  TH1F* hNMetsCut2               = new TH1F("BNHist_NMetsCut2",             ";Met mulitiplicity (cut 2)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut3               = new TH1F("BNHist_NMetsCut3",             ";Met mulitiplicity (cut 3)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut4               = new TH1F("BNHist_NMetsCut4",             ";Met mulitiplicity (cut 4)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut5               = new TH1F("BNHist_NMetsCut5",             ";Met mulitiplicity (cut 5)",  	 11, -0.5, 10.5);  
  TH1F* hNMetsCut6               = new TH1F("BNHist_NMetsCut6",             ";Met mulitiplicity (cut 6)",  	 11, -0.5, 10.5);  
  TH1F* hElecMVA                 = new TH1F("BNHist_ElecMVA",               ";Elec MVA",           100, -2, 2);

  //for disappTrks
  TH1F* hNPV_Sig                 = new TH1F("BNHist_NumPV_Sig",             ";# reco PV (signal)",                   50,  0,     50);   
  TH1F* hNPV_NotSig              = new TH1F("BNHist_NumPV_NotSig",          ";# reco PV (not signal)",               50,  0,     50);   
  TH1F* hNTrks                   = new TH1F("BNHist_NTrks",                 ";Trk mulitiplicity",                    11, -0.5, 10.5);   
  TH1F* hNTrksAllButDeltaR       = new TH1F("BNHist_NTrksAllButDeltaR",     ";Trk mulitiplicity (no #DeltaR(trk-jet) cut)", 11, -0.5, 10.5);   
  TH1F* hNTrksBest_Sig           = new TH1F("BNHist_NTrksBest_Sig",         ";Trk mulitiplicity (signal)",           11, -0.5, 10.5);   
  TH1F* hNTrksBest_NotSig        = new TH1F("BNHist_NTrksBest_NotSig",      ";Trk mulitiplicity (not signal)",       11, -0.5, 10.5);   
  //  TH1F* jetPt                    = new TH1F("BNHist_jetPt",                 ";Jet pT [GeV]",                         100, 0, 1000);
  TH1F* trackPt                  = new TH1F("BNHist_trackPt",               ";track pT [GeV]",                       100, 0, 1000);
  TH1F* trackIsIso               = new TH1F("BNHist_trackIsIso",            ";track isIso ",                         11, -0.5, 10.5);     
  TH1F* trackIsIso_Sig           = new TH1F("BNHist_trackIsIso_Sig",        ";track isIso (signal)",                 11, -0.5, 10.5);     
  TH1F* trackIsIso_NotSig        = new TH1F("BNHist_trackIsIso_NotSig",     ";track isIso (not signal)",             11, -0.5, 10.5);     
  TH1F* trackNumHits             = new TH1F("BNHist_trackNumHits",          ";track number of valid hits ",          31, -0.5, 30.5);
  TH1F* trackNHitsMissingOut        = new TH1F("BNHist_trackNHitsMissingOut",        ";track number of missing outer hits ",           31, -0.5, 30.5);
  TH1F* trackNHitsMissingOutPreCut  = new TH1F("BNHist_trackNHitsMissingOutPreCut",  ";track number of missing outer hits (pre cut)",  31, -0.5, 30.5);
  TH1F* trackNHitsMissingOutPostCut = new TH1F("BNHist_trackNHitsMissingOutPostCut", ";track number of missing outer hits (post cut)", 31, -0.5, 30.5);

  TH1F* trackdepTrkRp5           = new TH1F("BNHist_trackdepTrkRp5",        ";track  depTrkRp5 ",                    100, 0, 500);

  TH1F* trackdepTrkRp5MinusPt            = new TH1F("BNHist_trackdepTrkRp5MinusPt", ";#sum(p_{T})^{#DeltaR<0.5} - p_{T}^{track} ",                    100, 0, 150);
  TH1F* trackdepTrkRp3MinusPt            = new TH1F("BNHist_trackdepTrkRp3MinusPt", ";#sum(p_{T})^{#DeltaR<0.3} - p_{T}^{track} ",                    100, 0, 150);


  TH1F* trackdepTrkRp5MinusPt_Sig        = new TH1F("BNHist_trackdepTrkRp5MinusPt_Sig", ";track  depTrkRp5MinusPt ",                100, 0, 150);
  TH1F* trackdepTrkRp5MinusPtRhoCorr_Sig        = new TH1F("BNHist_trackdepTrkRp5MinusPtRhoCorr_Sig", ";track  depTrkRp5MinusPt ",                100, 0, 150);
  TH1F* trackdepTrkRp5MinusPtRhoCorr_Sig_PV10         = new TH1F("BNHist_trackdepTrkRp5MinusPtRhoCorr_Sig_10", ";track  depTrkRp5MinusPtRhoCorr ",                100, 0, 30);
  TH1F* trackdepTrkRp5MinusPt_Sig_PV10         = new TH1F("BNHist_trackdepTrkRp5MinusPtr_Sig_10", ";track  depTrkRp5MinusPt ",                100, 0, 30);

  TH1F* trackdepTrkRp5MinusPtRhoCorr_Sig_PV20         = new TH1F("BNHist_trackdepTrkRp5MinusPtRhoCorr_Sig_20", ";track  depTrkRp5MinusPtRhoCorr ",                100, 0, 30);
  TH1F* trackdepTrkRp5MinusPt_Sig_PV20         = new TH1F("BNHist_trackdepTrkRp5MinusPt_Sig_20", ";track  depTrkRp5MinusPt ",                100, 0, 30);


  TH1F* trackdepTrkRp5MinusPtRhoCorr_Sig_PV30         = new TH1F("BNHist_trackdepTrkRp5MinusPtRhoCorr_Sig_30", ";track  depTrkRp5MinusPtRhoCorr ",                100, 0, 30);
  TH1F* trackdepTrkRp5MinusPt_Sig_PV30         = new TH1F("BNHist_trackdepTrkRp5MinusPt_Sig_30", ";track  depTrkRp5MinusPt ",                100, 0, 30);

  TH1F* trackdepTrkRp5MinusPtRhoCorr_Sig_PV40         = new TH1F("BNHist_trackdepTrkRp5MinusPtRhoCorr_Sig_40", ";track  depTrkRp5MinusPtRhoCorr ",                100, 0, 30);
  TH1F* trackdepTrkRp5MinusPt_Sig_PV40         = new TH1F("BNHist_trackdepTrkRp5MinusPt_Sig_40", ";track  depTrkRp5MinusPt ",                100, 0, 30);

  TH1F* trackdepTrkRp3MinusPt_Sig        = new TH1F("BNHist_trackdepTrkRp3MinusPt_Sig", ";track  depTrkRp3MinusPt ",                100, 0, 150);

  TH1F* trackdepTrkRp5MinusPt_NotSig     = new TH1F("BNHist_trackdepTrkRp5MinusPt_NotSig", ";#sum(p_{T})^{#DeltaR<0.5} - p_{T}^{track} (not signal)",         100, 0, 150);
  TH1F* trackdepTrkRp3MinusPt_NotSig     = new TH1F("BNHist_trackdepTrkRp3MinusPt_NotSig", ";#sum(p_{T})^{#DeltaR<0.3} - p_{T}^{track} (not signal)",         100, 0, 150);


  TH1F* trackerVetoPtRp3_Sig        = new TH1F("BNHist_trackerVetoPtRp3_Sig", ";trackerVetoPtRp3 ",                100, 0, 300);
  TH1F* trackerVetoPtRp5_Sig        = new TH1F("BNHist_trackerVetoPtRp5_Sig", ";trackerVetoPtRp5 ",                100, 0, 300);

  TH1F* trackerVetoPtRp3_NotSig        = new TH1F("BNHist_trackerVetoPtRp3_NotSig", ";trackerVetoPtRp3 ",                100, 0, 300);
  TH1F* trackerVetoPtRp5_NotSig        = new TH1F("BNHist_trackerVetoPtRp5_NotSig", ";trackerVetoPtRp5 ",                100, 0, 300);

  TH1F* trackerVetoPtRp3MinusPt        = new TH1F("BNHist_trackerVetoPtRp3MinusPt",  ";candEnergy - track p_{T} (GeV)",  100, -10, 10);
  TH1F* trackerVetoPtRp3_PreCut        = new TH1F("BNHist_trackerVetoPtRp5_PreCut",  ";candEnergy (GeV)",                100, 0, 300);
  TH1F* trackerVetoPtRp3_PostCut       = new TH1F("BNHist_trackerVetoPtRp5_PostCut", ";candEnergy (GeV)",                100, 0, 300);



  TH1F* trackdepTrkRp5MinusPtBest_Sig    = new TH1F("BNHist_trackdepTrkRp5MinusPtBest_Sig",    ";track (best) depTrkRp5MinusPt ",   100, 0, 150);
  TH1F* trackdepTrkRp5MinusPtBest_NotSig = new TH1F("BNHist_trackdepTrkRp5MinusPtBest_NotSig", ";track (best) depTrkRp5MinusPt ",   100, 0, 150);
  TH1F* trackdepTrkRp5MinusPtPreCut      = new TH1F("BNHist_trackdepTrkRp5MinusPtPreCut",      ";track depTrkRp5MinusPt ",          100, 0, 150); 
  TH1F* trackdepTrkRp5MinusPtPostCut     = new TH1F("BNHist_trackdepTrkRp5MinusPtPostCut",     ";track depTrkRp5MinusPt ",          100, 0, 150); 

  TH1F* trackPtByDepTrkRp5_Sig        = new TH1F("BNHist_trackPtByDepTrkRp5_Sig",    ";p_{T}^{track} / #sum(p_{T})^{#DeltaR<0.5} (signal)",     100, 0, 2);
  TH1F* trackPtByDepTrkRp5_NotSig     = new TH1F("BNHist_trackPtByDepTrkRp5_NotSig", ";p_{T}^{track} / #sum(p_{T})^{#DeltaR<0.5} (not signal)", 100, 0, 2);

  TH1F* trackRelIsoRp5_SigZoom       = new TH1F("BNHist_trackRelIsoRp5_SigZoom",   ";(#sum(p_{T})^{#DeltaR<0.5}-p_{T}^{track}) / p_{T}^{track} (signal)",     100, 0, 0.1);
  TH1F* trackRelIsoRp5_Sig           = new TH1F("BNHist_trackRelIsoRp5_Sig",       ";(#sum(p_{T})^{#DeltaR<0.5}-p_{T}^{track}) / p_{T}^{track} (signal)",     100, 0, 3);
  TH1F* trackRelIsoRp5_NotSig        = new TH1F("BNHist_trackRelIsoRp5_NotSig",    ";(#sum(p_{T})^{#DeltaR<0.5}-p_{T}^{track}) / p_{T}^{track} (not signal)", 100, 0, 3);

  TH2F* trackRelIsoRp3VsPV_Sig       = new TH2F("BNHist_trackRelIsoRp3VsPV_Sig",    ";# reco PV;(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (signal)",    50, 0, 50, 100, 0, 0.1);
  TH2F* trackRelIsoRp3VsPV_NotSig    = new TH2F("BNHist_trackRelIsoRp3VsPV_NotSig", ";# reco PV;(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (not sig.)",  50, 0, 50, 100, 0, 10);
  TH1F* trackRelIsoRp3_SigZoom       = new TH1F("BNHist_trackRelIsoRp3_SigZoom",   ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (signal)",     100, 0, 0.1);
  TH1F* trackRelIsoRp3_Sig           = new TH1F("BNHist_trackRelIsoRp3_Sig",       ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (signal)",     100, 0, 3);
  TH1F* trackRelIsoRp3_SigTestCut    = new TH1F("BNHist_trackRelIsoRp3_SigTestCut", ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (signal)",     100, 0, 3);
  TH1F* trackRelIsoRp3_NotSig        = new TH1F("BNHist_trackRelIsoRp3_NotSig",    ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (not signal)", 100, 0, 3);
  TH1F* trackRelIsoRp3_NotSigTestCut = new TH1F("BNHist_trackRelIsoRp3_NotSigTestCut", ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (not signal)", 100, 0, 3);

  TH2F* trackRelIsoRp3CorrVsPV_Sig       = new TH2F("BNHist_trackRelIsoRp3CorrVsPV_Sig",    ";# reco PV;(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)",    50, 0, 50, 100, 0, 0.1);
  TH2F* trackRelIsoRp3CorrVsPV_NotSig    = new TH2F("BNHist_trackRelIsoRp3CorrVsPV_NotSig", ";# reco PV;(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (not sig.)",  50, 0, 50, 100, 0, 10);
  TH1F* trackRelIsoRp3Corr_SigZoom       = new TH1F("BNHist_trackRelIsoRp3Corr_SigZoom",   ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)",     100, 0, 0.1);
  TH1F* trackRelIsoRp3Corr_Sig           = new TH1F("BNHist_trackRelIsoRp3Corr_Sig",       ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)",     100, 0, 3);
  TH1F* trackRelIsoRp3Corr_NotSig        = new TH1F("BNHist_trackRelIsoRp3Corr_NotSig",    ";(#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (not signal)", 100, 0, 3);



  TH1F* trackPtByDepTrkRp5_PreCut     = new TH1F("BNHist_trackPtByDepTrkRp5_PreCut", ";p_{T}^{track} / #sum(p_{T})^{#DeltaR<0.5}", 100, 0, 2);
  //TH1F* trackdepTrkRp5MinusPt_isIso    = new TH1F("BNHist_trackdepTrkRp5MinusPt_isIso", ";track  depTrkRp5MinusPt ",             100, 0, 150);
  //TH1F* trackdepTrkRp5MinusPt_isNotIso    = new TH1F("BNHist_trackdepTrkRp5MinusPt_isNotIso", ";track  depTrkRp5MinusPt ",             100, 0, 150);

  TH1F* trackCaloTot             = new TH1F("BNHist_trackCaloTot",          ";track  CaloTot ",                      100, 0, 150);
  TH1F* trackCaloTotBest         = new TH1F("BNHist_trackCaloTotBest",      ";track  CaloTot (best trk)",            100, 0, 150);
  TH1F* trackCaloTotSigReg       = new TH1F("BNHist_trackCaloTotSigReg",    ";track  CaloTot (sig reg)",             100, 0, 150);
  TH1F* trackCaloTotByP          = new TH1F("BNHist_trackCaloTotByP",       ";track  CaloTotByP ",                   100, 0, 2);
  TH1F* trackCaloTotByPBest      = new TH1F("BNHist_trackCaloTotByPBest",   ";track  CaloTotByP (best trk) ",        100, 0, 2);
  TH1F* trackCaloTotByPSigReg    = new TH1F("BNHist_trackCaloTotByPSigReg", ";track  CaloTotByP (sig reg)",          100, 0, 2);


  TH1F* trackMetDeltaPhi_Sig         = new TH1F("BNHist_trackMetDeltaPhi_Sig",        ";track-Met  deltaPhi ",       100, -3, 3);
  TH1F* trackMetDeltaPhi_NotSig      = new TH1F("BNHist_trackMetDeltaPhi_NotSig",     ";track-Met  deltaPhi ",       100, -3, 3);
  TH1F* jetMetDeltaPhi               = new TH1F("BNHist_jetMetDeltaPhi",              ";jet-Met    deltaPhi ",       100, -3.5, 3.5);
  TH1F* jetMetDeltaPhi_Sig               = new TH1F("BNHist_jetMetDeltaPhi_Sig",              ";jet-Met    deltaPhi (signal) ",       100, -3, 3);
   TH1F* jetMetDeltaPhi_NotSig               = new TH1F("BNHist_jetMetDeltaPhi_NotSig",              ";jet-Met    deltaPhi ( not signal) ",       100, -3, 3);


  TH1F* trackDeltaR_Sig              = new TH1F("BNHist_trackDeltaR_Sig",             ";#DeltaR_{min}(trk-trk)",     100, 0, 5);
  TH1F* trackDeltaR_NotSig           = new TH1F("BNHist_trackDeltaRNotSig",           ";#DeltaR_{min}(trk-trk)",     100, 0, 5);
  TH1F* trackJetDeltaR_Sig           = new TH1F("BNHist_trackJetDeltaR_Sig",          ";#DeltaR_{min}(trk-jet)",     100, 0, 5);
  TH1F* trackJetDeltaR_NotSig        = new TH1F("BNHist_trackJetDeltaR_NotSig",       ";#DeltaR_{min}(trk-jet)",         100, 0, 5);
  TH1F* trackJetDeltaR_PreCut        = new TH1F("BNHist_trackJetDeltaR_PreCut",       ";#DeltaR_{min}(trk-jet)",           100, 0, 5);
  //  TH1F* trackJet1DeltaR              = new TH1F("BNHist_trackJet1DeltaR",           ";track-jet1  deltaR ",             100, 0, 5);
  //  TH1F* trackJet1DeltaR_isIso              = new TH1F("BNHist_trackJet1DeltaRisIso",           ";track-jet1  deltaR ",             100, 0, 5);
  //TH1F* trackJet1DeltaR_isNotIso              = new TH1F("BNHist_trackJet1DeltaRisNotIso",           ";track-jet1  deltaR ",             100, 0, 5);
  //TH1F* trackJet2DeltaR_isIso              = new TH1F("BNHist_trackJet2DeltaR_isIso",           ";track-jet2  deltaR ",             100, 0, 5);
  //TH1F* trackJet2DeltaR              = new TH1F("BNHist_trackJet2DeltaR",           ";track-jet2  deltaR ",             100, 0, 5);
  //TH1F* trackJet2DeltaR_isNotIso              = new TH1F("BNHist_trackJet2DeltaR_isNotIso",           ";track-jet2  deltaR ",             100, 0, 5);
  //TH1F* trackGenMatchedId_isIso              = new TH1F("BNHist_trackGenMatchedId_isIso",           ";track genMatchedId ",                   25, -0.5, 24.5);
  TH1F* trackGenMatchedId_isNotIso   = new TH1F("BNHist_trackGenMatchedId_isNotIso",   ";track genMatchedId ",                         25, -0.5, 24.5);
  TH1F* trackGenMatchedIdFitReg      = new TH1F("BNHist_trackGenMatchedIdFitReg",      ";track genMatchedId (w/ miss outer hits cut)", 25, -0.5, 24.5);
  TH1F* trackGenMatchedIdSigReg      = new TH1F("BNHist_trackGenMatchedIdSigReg",      ";track genMatchedId (sig reg)",                25, -0.5, 24.5);
  TH1F* trackPdgIdTestCut            = new TH1F("BNHist_trackPdgIdTestCut",            ";track genMatchedId (after rel trk iso cut)",  25, -0.5, 24.5);

    
  Long64_t nentries = fChain->GetEntries();

  double lumiWt = fChain->GetWeight();  // The BNTree weight must be set by mergeOutput.py.  
  if (outFile.Contains("hist_")) lumiWt = 1.0;  // Do not apply the lumi weight if writing histograms to hist_*.root files, since the lumi wt will be applied by mergeOutput.py.  

  int nEvtPassPre    = 0;  
  double nEvtPassPreWtd = 0;  

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

    // Fill for all events:  
    hEvtIsGoodVtx            ->Fill(events_GoodVertex->at(0), BNTreeWt);  


    // Count other physics objects, according to AN-2012-421-v6.  
    int numJets  = 0;
    int numMuons = 0;
    int numElecs = 0;
    int numTaus  = 0; 
    int numTrks  = 0;
    int numTrksAllButDeltaR = 0;
    vector<uint> jetPassedIdx;  
    bool isPassedLeadingJet = false;  
    for (uint ijet = 0; ijet<jets_pt->size(); ijet++) {
      // count number of jets that have pT>30 and |eta|<4.5
      if (!(jets_pt                         ->at(ijet)  > 30))  continue;
      if (!(fabs(jets_eta                   ->at(ijet)) < 4.5)) continue;
      if (!(jets_neutralHadronEnergyFraction->at(ijet)  < 0.7)) continue;  
      if (!(jets_chargedEmEnergyFraction    ->at(ijet)  < 0.5)) continue;   
      // Must reapply jet selection criteria, since they were not applied to the jet collection (only the secondary jet collection).  
      jetPassedIdx.push_back(ijet);  
      numJets++;  

      isPassedLeadingJet |= 
	(jets_pt                         ->at(ijet)  > 110  &&
	 fabs(jets_eta                   ->at(ijet)) < 2.4  &&
	 jets_chargedHadronEnergyFraction->at(ijet)  > 0.2  &&
	 jets_chargedEmEnergyFraction    ->at(ijet)  < 0.5  &&
	 jets_neutralHadronEnergyFraction->at(ijet)  < 0.7  &&
	 jets_neutralEmEnergyFraction    ->at(ijet)  < 0.7);  
      
    }
    
    /*if (numJets==2) {
      uint idx0 = jetPassedIdx.at(0);
      uint idx1 = jetPassedIdx.at(1);


      // check that idx0 corresponds to the leading jet; switch if not
      if (jets_pt->at(idx0) < jets_pt->at(idx1)) {
      jetPassedIdx.at(0) = idx1;
      jetPassedIdx.at(1) = idx0;
      }
      }*/

    double DiJetDeltaPhiMax = 0;  // event passes if only one jet found  
    for (uint i=0; i<jetPassedIdx.size(); i++) {
      int idxCur   = jetPassedIdx.at(i);
      int idxFirst = jetPassedIdx.at(0);
      if (jets_pt->at(idxCur) > jets_pt->at(idxFirst)) {
	int idxTmp = idxFirst; 
	jetPassedIdx.at(0) = idxCur;
	jetPassedIdx.at(i) = idxTmp;
      }
      
      for (uint j=0; j<jetPassedIdx.size(); j++) {
	int idxJ   = jetPassedIdx.at(j);
	double DiJetDeltaPhi = fabs(deltaPhi(jets_phi->at(idxCur), 
					     jets_phi->at(idxJ)));  
	if (DiJetDeltaPhi > DiJetDeltaPhiMax) DiJetDeltaPhiMax = DiJetDeltaPhi;  
      }
      
    } 


    // test tighter muon cut: 
    //    if (muons_pt->size()>0) continue;  
    for (uint imuon = 0; imuon<muons_pt->size(); imuon++) {
      if (!(muons_pt                      ->at(imuon)  > 10))   continue;  
      //      if (!(muons_isGlobalMuon->at(imuon) ==1 || // correct
      if (!(muons_isGlobalMuon ->at(imuon)==1 ||  
	    muons_isTrackerMuon->at(imuon)==1)) continue;  

      
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


    double jetMetDPhi_v2 = -99.;
    for (uint ijetPass = 0; ijetPass<jetPassedIdx.size(); ijetPass++) {
      jetMetDPhi_v2 = deltaPhi(mets_phi->at(0),  jets_phi->at(jetPassedIdx.at(ijetPass)));
    
    }


    // Apply other selection requirements, corresponding to https://twiki.cern.ch/twiki/bin/viewauth/CMS/MonojetDataFinalStandard2012v2#Cutflow
    METPre    ->Fill(mets_pt->at(0),     BNTreeWt);  	
    hNMetsCut0->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(mets_pt->at(0) > 220))   continue;     hNMetsCut1->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(isPassedLeadingJet))     continue;     hNMetsCut1A->Fill(mets_pt->size(),    BNTreeWt);
    //     if (!(numJets  <= 2))         continue;     hNMetsCut2->Fill(mets_pt->size(),    BNTreeWt);  	
    //    if (!(fabs(jetJetDPhi) < 2.5))   continue;     hNMetsCut3->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(DiJetDeltaPhiMax < 2.5)) continue;     hNMetsCut3->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numElecs == 0))         continue;     hNMetsCut4->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numMuons == 0))         continue;     hNMetsCut5->Fill(mets_pt->size(),    BNTreeWt);  	
    if (!(numTaus  == 0))         continue; 
    //    if (!(fabs(jetMetDPhi_v2)                                            > 0.5   ))  continue;


    //Add in cuts for disappTrks

    int idxTrkBest = -1;  
    double trkPtBest = -99;  
    //    double trkJetDeltaRBest = -99;  

    for (uint itrk = 0; itrk<tracks_pt->size(); itrk++) {

      //      double trkJet1DeltaR = deltaR(tracks_eta->at(itrk), tracks_phi->at(itrk), jets_eta->at(jetPassedIdx.at(0)), jets_phi->at(jetPassedIdx.at(0)));
      //      if (jetPassedIdx.size()>1) double trkJet2DeltaR = deltaR(tracks_eta->at(itrk), tracks_phi->at(itrk), jets_eta->at(jetPassedIdx.at(1)), jets_phi->at(jetPassedIdx.at(1)));
      double trkJetDeltaR = 99.;
      for (uint ijetPass = 0; ijetPass<jetPassedIdx.size(); ijetPass++) {
	double trkJetDeltaRTemp = deltaR(tracks_eta->at(itrk), tracks_phi->at(itrk), jets_eta->at(jetPassedIdx.at(ijetPass)), jets_phi->at(jetPassedIdx.at(ijetPass)));
	if (trkJetDeltaRTemp < trkJetDeltaR) trkJetDeltaR = trkJetDeltaRTemp;
      }
      double trackMetDeltaPhi = deltaPhi(tracks_phi->at(itrk), mets_phi->at(0));

      if (!(tracks_pt                                           ->at(itrk)  > 20))      continue;
      if (!(fabs(tracks_eta                                     ->at(itrk))  < 2.1))    continue;
      if (!(fabs(tracks_d0wrtPV                                 ->at(itrk))  < 0.02))   continue;
      if (!(fabs(tracks_dZwrtPV                                 ->at(itrk))  < 0.5))   continue;
      if (!(tracks_numValidHits                                 ->at(itrk)  > 4))       continue;
      if (!(tracks_nHitsMissingInner                            ->at(itrk)  == 0))      continue;
      if (!(tracks_nHitsMissingMiddle                           ->at(itrk)  == 0))      continue;
      //      if (!(tracks_isIso                                        ->at(itrk)  == 1))      continue;
      //      if (!(trkJetDeltaR                                                    > 0.5 ))  continue;
      if (!(tracks_isMatchedDeadEcal                            ->at(itrk)  == 0))      continue;
      if (!((fabs(tracks_eta                                    ->at(itrk))  < 1.42) || 
 	    (fabs(tracks_eta                                    ->at(itrk))  > 1.65)))  continue;
      //if (!(fabs(trackMetDeltaPhi)  < 2))    continue;


      // Testing only:       if (!((tracks_depTrkRp5MinusPt ->at(itrk))/tracks_pt->at(itrk)  < 0.05))      continue;
      if (!((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk)  < 0.05))      continue;

      

      numTrksAllButDeltaR++;
      
      trackJetDeltaR_PreCut       ->Fill(trkJetDeltaR,                     BNTreeWt);  
      
      if (!(trkJetDeltaR                                                     > 0.5 ))  continue;

      if (tracks_pt->at(itrk) > trkPtBest) { 
	trkPtBest = tracks_pt->at(itrk);  
	idxTrkBest = itrk;  
	//	trkJetDeltaRBest = trkJetDeltaR;  
      }

      numTrks++;
      double trkDeltaR = 99.;
      for (uint jtrk = 0; jtrk<tracks_pt->size(); jtrk++) {
        if(tracks_eta->at(itrk) == tracks_eta->at(jtrk) && tracks_phi->at(itrk) == tracks_phi->at(jtrk)) continue;
        if(itrk == jtrk) continue;
	double trkDeltaRTemp = deltaR(tracks_eta->at(itrk), tracks_phi->at(itrk), tracks_eta->at(jtrk), tracks_phi  ->at(jtrk));
	if (trkDeltaRTemp < trkDeltaR) trkDeltaR = trkDeltaRTemp;

	//	trackDeltaR ->Fill(trkDeltaR, BNTreeWt);
      }
      
      
      //      trackJet1DeltaR  ->Fill(trkJet1DeltaR, BNTreeWt);

      //      if (jetPassedIdx.size()>1) {
      //	trackJet2DeltaR  ->Fill(trkJet2DeltaR, BNTreeWt);

      //	  if (tracks_isIso -> at(itrk) == 0){     trackJet2DeltaR_isNotIso ->Fill( trkJet2DeltaR, BNTreeWt);}
      //	  if (tracks_isIso -> at(itrk) == 1){     trackJet2DeltaR_isIso    ->Fill( trkJet2DeltaR, BNTreeWt);}
      // }


      //      if (tracks_isIso  ->at(itrk)  == 1){

      if (tracks_genMatchedId  ->at(itrk)  == 24){
	//	trackGenMatchedId_isIso       ->Fill(tracks_genMatchedId     ->at(itrk), BNTreeWt);
	/*	trackdepTrkRp5MinusPt_Sig        ->Fill(tracks_depTrkRp5MinusPt ->at(itrk), BNTreeWt);
	trackdepTrkRp5MinusPtRhoCorr_Sig ->Fill(tracks_depTrkRp5MinusPtRhoCorr ->at(itrk), BNTreeWt);		
	if (0 < events_numPV->at(0) && events_numPV->at(0) < 10 ){

	trackdepTrkRp5MinusPtRhoCorr_Sig_PV10  ->Fill(tracks_depTrkRp5MinusPtRhoCorr ->at(itrk), BNTreeWt);
	trackdepTrkRp5MinusPt_Sig_PV10  ->Fill(tracks_depTrkRp5MinusPt ->at(itrk), BNTreeWt);
	}
	if (10 < events_numPV->at(0) && events_numPV->at(0) < 20 ){
	  trackdepTrkRp5MinusPtRhoCorr_Sig_PV20  ->Fill(tracks_depTrkRp5MinusPtRhoCorr ->at(itrk), BNTreeWt);
	  trackdepTrkRp5MinusPt_Sig_PV20  ->Fill(tracks_depTrkRp5MinusPt ->at(itrk), BNTreeWt);
	}
	if (20 < events_numPV->at(0) && events_numPV->at(0) < 30 ){
          trackdepTrkRp5MinusPtRhoCorr_Sig_PV30  ->Fill(tracks_depTrkRp5MinusPtRhoCorr ->at(itrk), BNTreeWt);
          trackdepTrkRp5MinusPt_Sig_PV30  ->Fill(tracks_depTrkRp5MinusPt ->at(itrk), BNTreeWt);
        }
	if (30 <  events_numPV->at(0)  && events_numPV->at(0) < 40 ){
          trackdepTrkRp5MinusPtRhoCorr_Sig_PV40  ->Fill(tracks_depTrkRp5MinusPtRhoCorr ->at(itrk), BNTreeWt);
          trackdepTrkRp5MinusPt_Sig_PV40  ->Fill(tracks_depTrkRp5MinusPt ->at(itrk), BNTreeWt);
	  }*/

	trackdepTrkRp3MinusPt_Sig  ->Fill(tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk), BNTreeWt);
	trackerVetoPtRp5_Sig       ->Fill(tracks_trackerVetoPtRp5->at(itrk), BNTreeWt);
	trackerVetoPtRp3_Sig       ->Fill(tracks_trackerVetoPtRp3->at(itrk), BNTreeWt);
	trackRelIsoRp3_SigZoom->Fill((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackRelIsoRp3_Sig    ->Fill((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackRelIsoRp3VsPV_Sig->Fill(events_numPV->at(0),  (tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	// 	trackRelIsoRp3Corr_SigZoom->Fill((tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	// 	trackRelIsoRp3Corr_Sig    ->Fill((tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	// 	trackRelIsoRp3CorrVsPV_Sig->Fill(events_numPV->at(0),  (tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	//	trackRelIsoRp3Corr_SigZoom->Fill((tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	//	trackRelIsoRp3Corr_Sig    ->Fill((tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	//trackRelIsoRp3CorrVsPV_Sig->Fill(events_numPV->at(0),  (tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackRelIsoRp5_SigZoom->Fill((tracks_depTrkRp5->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackRelIsoRp5_Sig    ->Fill((tracks_depTrkRp5->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackPtByDepTrkRp5_Sig     ->Fill((tracks_pt->at(itrk) / tracks_depTrkRp5 ->at(itrk)), BNTreeWt);
	trackJetDeltaR_Sig         ->Fill( trkJetDeltaR                    , BNTreeWt);
	trackDeltaR_Sig            ->Fill( trkDeltaR                       , BNTreeWt);
	trackMetDeltaPhi_Sig       ->Fill( trackMetDeltaPhi                , BNTreeWt);
	trackIsIso_Sig             ->Fill(tracks_isIso->at(itrk),            BNTreeWt);
	hNPV_Sig                   ->Fill(events_numPV->at(0),               BNTreeWt);

	if ((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk) < 0.05) {
	  trackRelIsoRp3_SigTestCut ->Fill((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	}

      } else {
	//	std::cout << "Debug 2 " << std::endl;
	//	trackGenMatchedId_isNotIso      ->Fill(tracks_genMatchedId      ->at(itrk), BNTreeWt);
	trackdepTrkRp5MinusPt_NotSig  ->Fill(tracks_depTrkRp5MinusPt  ->at(itrk), BNTreeWt);
	trackdepTrkRp3MinusPt_NotSig  ->Fill(tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk), BNTreeWt);
        trackerVetoPtRp5_NotSig  ->Fill(tracks_trackerVetoPtRp5->at(itrk), BNTreeWt);
        trackerVetoPtRp3_NotSig  ->Fill(tracks_trackerVetoPtRp3->at(itrk), BNTreeWt);
	trackRelIsoRp5_NotSig  ->Fill((tracks_depTrkRp5->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackRelIsoRp3_NotSig  ->Fill((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackRelIsoRp3VsPV_NotSig->Fill(events_numPV->at(0),  (tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	//	trackRelIsoRp3Corr_NotSig  ->Fill((tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	//	trackRelIsoRp3CorrVsPV_NotSig->Fill(events_numPV->at(0),  (tracks_depTrkRp3MinusPtRhoCorr->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	trackPtByDepTrkRp5_NotSig     ->Fill((tracks_pt->at(itrk) / tracks_depTrkRp5 ->at(itrk)), BNTreeWt); 
	trackJetDeltaR_NotSig         ->Fill( trkJetDeltaR                     , BNTreeWt);
	trackDeltaR_NotSig            ->Fill( trkDeltaR                     , BNTreeWt);
	trackMetDeltaPhi_NotSig       ->Fill( trackMetDeltaPhi                , BNTreeWt);
	trackIsIso_NotSig             ->Fill(tracks_isIso->at(itrk),            BNTreeWt);
	hNPV_NotSig                   ->Fill(events_numPV->at(0),               BNTreeWt);

	if ((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk) < 0.05) {
	  trackRelIsoRp3_NotSigTestCut ->Fill((tracks_depTrkRp3->at(itrk)-tracks_pt->at(itrk))/tracks_pt->at(itrk), BNTreeWt);
	  trackPdgIdTestCut         ->Fill(tracks_genMatchedId  ->at(itrk), BNTreeWt);   
	} else {
	  trackGenMatchedId_isNotIso->Fill(tracks_genMatchedId  ->at(itrk), BNTreeWt);  
	}

      }


      trackPt                 ->Fill(tracks_pt                          ->at(itrk),          BNTreeWt);
      trackIsIso              ->Fill(tracks_isIso                       ->at(itrk),          BNTreeWt);
      trackNumHits            ->Fill(tracks_numValidHits                ->at(itrk),          BNTreeWt);
      trackNHitsMissingOut    ->Fill(tracks_nHitsMissingOuter           ->at(itrk),          BNTreeWt);
      trackdepTrkRp5          ->Fill(tracks_depTrkRp5                   ->at(itrk),          BNTreeWt);
      trackdepTrkRp5MinusPt   ->Fill(fabs(tracks_depTrkRp5              ->at(itrk)-tracks_pt->at(itrk)),          BNTreeWt);
      trackdepTrkRp3MinusPt   ->Fill(fabs(tracks_depTrkRp3              ->at(itrk)-tracks_pt->at(itrk)),          BNTreeWt);
      trackCaloTot            ->Fill(tracks_caloTotDeltaRp5RhoCorr      ->at(itrk),          BNTreeWt);
      trackCaloTotByP         ->Fill(tracks_caloTotDeltaRp5ByPRhoCorr   ->at(itrk),          BNTreeWt);

    } // ends for (uint itrk = 0; itrk<tracks_pt->size(); itrk++)
    //    std::cout << "Debug 0" << std::endl;
    // Next two lines for debugging only.  
    hNTrksAllButDeltaR        ->Fill(numTrksAllButDeltaR,                   BNTreeWt);  	
    if (numTrksAllButDeltaR > 0) {
      hNMetsCut6                  ->Fill(mets_pt->size(),                   BNTreeWt);  	
    }  

    hNTrks                  ->Fill(numTrks,                   BNTreeWt);  	

    if (numTrks == 0) continue;  // Only fill histograms below for events that have at least one track passing the selection.  
    jetMetDeltaPhi->Fill(jetMetDPhi_v2, BNTreeWt);
    //    jetJetDeltaPhi->Fill(jetJetDPhi, BNTreeWt);
    if (tracks_genMatchedId  ->at(idxTrkBest)  == 24){
      trackdepTrkRp5MinusPtBest_Sig   ->Fill(fabs(tracks_depTrkRp5->at(idxTrkBest)-tracks_pt ->at(idxTrkBest)), BNTreeWt);
	hNTrksBest_Sig                  ->Fill(1.0,                                      BNTreeWt);
    } else {
	  trackdepTrkRp5MinusPtBest_NotSig->Fill(fabs(tracks_depTrkRp5->at(idxTrkBest)-tracks_pt ->at(idxTrkBest)), BNTreeWt);
	hNTrksBest_NotSig               ->Fill(1.0,                                      BNTreeWt);
    }


    hNJets                  ->Fill(numJets,                   BNTreeWt);  	
    hNMuons                 ->Fill(numMuons,                  BNTreeWt);  	
    hNElecs                 ->Fill(numElecs,                  BNTreeWt);  	
    hNTaus                  ->Fill(numTaus,                   BNTreeWt);  	
    hNMuonsNoCut            ->Fill(muons_pt->size(),          BNTreeWt);  	
    hNElecsNoCut            ->Fill(electrons_pt->size(),      BNTreeWt);  	
    hNTausNoCut             ->Fill(taus_pt->size(),           BNTreeWt);  	
    hNMets                  ->Fill(mets_pt->size(),           BNTreeWt);  	
    cout << "Found event that passed presel, incl. trk iso: run = " << int(events_run->at(0))  
	 << "; lumi = " << int(events_lumi->at(0))
	 << "; evt = " << long(events_evt->at(0))    
	 << "; best trk pt = " << tracks_pt ->at(idxTrkBest)
	 << "; eta = "         << tracks_eta->at(idxTrkBest)
	 << "; phi = "         << tracks_phi->at(idxTrkBest)
	 << "; relIso0.3 = " << (tracks_depTrkRp3->at(idxTrkBest)-tracks_pt->at(idxTrkBest))/tracks_pt->at(idxTrkBest)
	 << "; genMatchPdgId = " << int(tracks_genMatchedPdgId  ->at(idxTrkBest) )  
	 << endl;  
    nEvtPassPre++;  
    nEvtPassPreWtd += BNTreeWt;  


    double jetMetDPhi = fabs(fabs(fabs(jets_phi->at(jetPassedIdx.at(0)) - mets_phi->at(0)) - 3.14159) - 3.14159);  
    jetChargedHadFrac->Fill(jets_chargedHadronEnergyFraction->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetNeutralHadFrac->Fill(jets_neutralHadronEnergyFraction->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetChargedEMFrac ->Fill(jets_chargedEmEnergyFraction    ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetNeutralEMFrac ->Fill(jets_neutralEmEnergyFraction    ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetOneEta        ->Fill(jets_eta                        ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetOnePt         ->Fill(jets_pt                         ->at(jetPassedIdx.at(0)),    BNTreeWt);
    jetOneMetDPhi    ->Fill(jetMetDPhi                                           ,    BNTreeWt);
    jetDPhi          ->Fill(DiJetDeltaPhiMax                                     ,    BNTreeWt);

    if (numTrks > 0) {
      jetChargedHadFracPTrk->Fill(jets_chargedHadronEnergyFraction->at(jetPassedIdx.at(0)),    BNTreeWt);
      jetNeutralHadFracPTrk ->Fill(jets_neutralHadronEnergyFraction->at(jetPassedIdx.at(0)),    BNTreeWt);
      jetChargedEMFracPTrk ->Fill(jets_chargedEmEnergyFraction    ->at(jetPassedIdx.at(0)),    BNTreeWt);
      jetNeutralEMFracPTrk ->Fill(jets_neutralEmEnergyFraction    ->at(jetPassedIdx.at(0)),    BNTreeWt);
      jetOneEtaPTrk        ->Fill(jets_eta                        ->at(jetPassedIdx.at(0)),    BNTreeWt);
      jetOnePtPTrk         ->Fill(jets_pt                         ->at(jetPassedIdx.at(0)),    BNTreeWt);
      METFullPTrk          ->Fill(mets_pt->at(0)                                          ,    BNTreeWt);
    }

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

    /*    double jetMetDPhi_v2 = -99.;
    for (uint ijetPass = 0; ijetPass<jetPassedIdx.size(); ijetPass++) {
      jetMetDPhi_v2 = deltaPhi(mets_phi->at(0),  jets_phi->at(jetPassedIdx.at(ijetPass)));
      jetMetDeltaPhi->Fill(jetMetDPhi_v2, BNTreeWt);
      }*/
    
    MET       ->Fill(mets_pt->at(0),             BNTreeWt);
    METPhi    ->Fill(mets_phi->at(0),            BNTreeWt);

    //    TVector2 phiCorrection(TVector2 met, int Nvtx, isData) {
      
      float corX,corY;
      double Nvtx = events_sumNVtx->at(0);
      if(isData) {
   
	//CHristian corrections 2012ABC

	corX = 0.2661 + 0.3217*Nvtx; 
	corY = -0.2251 -0.1747*Nvtx;
	//	std::cout << "Correcting Met for data" << std::endl;
      }
      else {
	corX = 0.1166 + 0.0200*Nvtx; 
	corY = 0.2764 - 0.1280*Nvtx;
	//std::cout << "Correcting Met for everything else" << endl;
      }

      TVector2 corMET(0,0);
      corMET.Set( mets_px->at(0) - corX, mets_py->at(0) -corY );
      double corMetMag = sqrt ( pow( (corMET.X()) , 2) + pow( (corMET.Y()) , 2) );
      //      return corMET;
      // }
      double phiReg = atan2(mets_py->at(0), mets_px->at(0));
      MetDPhi_Check -> Fill ( mets_phi->at(0) - phiReg );
      double phiCorr = atan2( corMET.Y(), corMET.X() );
      MetDPhi       -> Fill ( phiCorr - phiReg );

      METPhiCorr    ->Fill(phiCorr,            BNTreeWt);
      METCorr       ->Fill(corMetMag,          BNTreeWt);


    METFull   ->Fill(mets_pt->at(0),             BNTreeWt);
    numPV     ->Fill(events_numPV->at(0),        BNTreeWt);  	


    // Additional disappearing track selection.  
    double trackIsoVal = tracks_depTrkRp5MinusPt->at(idxTrkBest);  
    if (trackIsoVal<0) trackIsoVal = 0;  // prevent from being negative  
    trackdepTrkRp5MinusPtPreCut ->Fill(trackIsoVal,          BNTreeWt);  
    trackPtByDepTrkRp5_PreCut->Fill((tracks_pt       ->at(idxTrkBest) / 
				     tracks_depTrkRp5->at(idxTrkBest)), BNTreeWt); 
//     if (!(tracks_depTrkRp5MinusPt           ->at(idxTrkBest) < 7)) continue;   
//     trackdepTrkRp5MinusPtPostCut->Fill(trackIsoVal,          BNTreeWt);  
    trackNHitsMissingOutPreCut ->Fill(tracks_nHitsMissingOuter           ->at(idxTrkBest),          BNTreeWt);  

    trackerVetoPtRp3MinusPt  ->Fill(tracks_trackerVetoPtRp3->at(idxTrkBest) - 
				    tracks_pt              ->at(idxTrkBest), BNTreeWt); 
    trackerVetoPtRp3_PreCut  ->Fill(tracks_trackerVetoPtRp3->at(idxTrkBest), BNTreeWt);
    //    if (!(tracks_trackerVetoPtRp3->at(idxTrkBest)>70)) continue;  
    trackerVetoPtRp3_PostCut ->Fill(tracks_trackerVetoPtRp3->at(idxTrkBest), BNTreeWt);


    if (!(tracks_nHitsMissingOuter          ->at(idxTrkBest) >= 3)) continue;  
    trackNHitsMissingOutPostCut->Fill(tracks_nHitsMissingOuter           ->at(idxTrkBest),          BNTreeWt);  
    trackGenMatchedIdFitReg    ->Fill(tracks_genMatchedId                ->at(idxTrkBest),          BNTreeWt); 

    double caloTot    = tracks_caloTotDeltaRp5RhoCorr      ->at(idxTrkBest); 
    double caloTotByP = tracks_caloTotDeltaRp5ByPRhoCorr   ->at(idxTrkBest); 
//     double caloTot    = tracks_caloTotDeltaRp5             ->at(idxTrkBest); // test without rho correction
//     double caloTotByP = tracks_caloTotDeltaRp5ByP          ->at(idxTrkBest); // test without rho correction

    // blind the data in the signal region  
    bool isSigReg = (caloTot    < 20 ||  
		     caloTotByP < 0.4);  
    
    if (isData && isSigReg) continue;  
    trackCaloTotBest           ->Fill(caloTot,          BNTreeWt);  
    trackCaloTotByPBest        ->Fill(caloTotByP,       BNTreeWt);  

    if (!isSigReg) continue;  
    trackCaloTotSigReg         ->Fill(caloTot,          BNTreeWt);
    trackCaloTotByPSigReg      ->Fill(caloTotByP,       BNTreeWt);  
    trackGenMatchedIdSigReg    ->Fill(tracks_genMatchedId                ->at(idxTrkBest),          BNTreeWt); 

    

  }  // end   for (Long64_t jentry=0; jentry<nentries;jentry++) {
  
  hEvtIsGoodVtx            ->Write();  
  hElecMVA                 ->Write();  

  METPre                   ->Write();  
  hNMetsCut0               ->Write();  
  hNMetsCut1               ->Write();  
  hNMetsCut1A              ->Write();  
  hNMetsCut1B              ->Write();  
  hNMetsCut1C              ->Write();  
  hNMetsCut1D              ->Write();  
  hNMetsCut1E              ->Write();  
  hNMetsCut1F              ->Write();  
  hNMetsCut2               ->Write();  
  hNMetsCut3               ->Write();  
  hNMetsCut4               ->Write();  
  hNMetsCut5               ->Write();  
  hNMetsCut6               ->Write();  
  hNMets                   ->Write();  

  hNJets                   ->Write();  
  numPV                    ->Write();
  MET                      ->Write();  
  METPhi                   ->Write();  
  MetDPhi_Check            ->Write();  
  MetDPhi                  ->Write();  
  METPhiCorr               ->Write();  
  METCorr                  ->Write();  
  METFull                  ->Write();
  
  jetChargedHadFrac        ->Write();
  jetNeutralHadFrac        ->Write();
  jetChargedEMFrac         ->Write();
  jetNeutralEMFrac         ->Write();
  jetOneEta                ->Write();
  jetOnePt                 ->Write();
  jetOneMetDPhi            ->Write();

  jetDPhi                  ->Write();
  jetJetDeltaPhi                  ->Write();

  jetTwoChHadFrac          ->Write();  
  jetTwoNeutralHadFrac     ->Write();
  jetTwoChEMFrac           ->Write();
  jetTwoNeutralEMFrac      ->Write();
  jetTwoEta                ->Write();
  jetTwoPt                 ->Write();
  jetTwoMetDPhi            ->Write();


  jetChargedHadFracPTrk ->Write();
  jetNeutralHadFracPTrk ->Write();
  jetChargedEMFracPTrk  ->Write();
  jetNeutralEMFracPTrk  ->Write();
  jetOneEtaPTrk         ->Write();
  jetOnePtPTrk          ->Write();
  jetMetDeltaPhi       ->Write();
  METFullPTrk           ->Write();

  hNElecs                  ->Write();  
  hNMuons                  ->Write();  
  hNTaus                   ->Write();  
  hNElecsNoCut             ->Write();  
  hNMuonsNoCut             ->Write();  
  hNTausNoCut              ->Write();  


  hNPV_Sig                 ->Write();  
  hNPV_NotSig              ->Write();  
  hNTrks                   ->Write();
  hNTrksAllButDeltaR       ->Write();  
  trackPt                  ->Write();
  trackIsIso               ->Write();
  trackIsIso_Sig           ->Write();
  trackIsIso_NotSig        ->Write();
  trackNumHits             ->Write();
  trackNHitsMissingOut     ->Write();
  trackdepTrkRp5           ->Write();
  trackdepTrkRp5MinusPt    ->Write();
  trackdepTrkRp5MinusPt_Sig    ->Write();

  trackdepTrkRp5MinusPtRhoCorr_Sig           ->Write();
  trackdepTrkRp5MinusPtRhoCorr_Sig_PV10      ->Write();
  trackdepTrkRp5MinusPt_Sig_PV10             ->Write();
  trackdepTrkRp5MinusPtRhoCorr_Sig_PV20      ->Write();
  trackdepTrkRp5MinusPt_Sig_PV20             ->Write();
  trackdepTrkRp5MinusPtRhoCorr_Sig_PV30      ->Write();
  trackdepTrkRp5MinusPt_Sig_PV30             ->Write();
  trackdepTrkRp5MinusPtRhoCorr_Sig_PV40      ->Write();
  trackdepTrkRp5MinusPt_Sig_PV40             ->Write();

  trackdepTrkRp5MinusPt_NotSig ->Write();
  trackdepTrkRp3MinusPt        ->Write();
  trackdepTrkRp3MinusPt_Sig    ->Write();
  trackdepTrkRp3MinusPt_NotSig ->Write();
  trackPtByDepTrkRp5_Sig       ->Write();
  trackPtByDepTrkRp5_NotSig    ->Write();

  trackerVetoPtRp5_Sig    ->Write();
  trackerVetoPtRp5_NotSig ->Write();

  trackerVetoPtRp3_Sig    ->Write();
  trackerVetoPtRp3_NotSig ->Write();

  trackerVetoPtRp3_PreCut ->Write();  
  trackerVetoPtRp3_PostCut->Write();  
  trackerVetoPtRp3MinusPt ->Write();  

  trackPdgIdTestCut->Write();  
  trackRelIsoRp3_Sig    ->Write();
  trackRelIsoRp3_SigZoom->Write();
  trackRelIsoRp5_Sig    ->Write();
  trackRelIsoRp5_SigZoom->Write();
  trackRelIsoRp3Corr_Sig    ->Write();
  trackRelIsoRp3Corr_SigZoom->Write();
  trackRelIsoRp3_SigTestCut->Write();
  trackRelIsoRp3_NotSigTestCut->Write();  

  trackRelIsoRp3_NotSig ->Write();
  trackRelIsoRp3Corr_NotSig ->Write();
  trackRelIsoRp5_NotSig ->Write();

  trackRelIsoRp3VsPV_Sig->Write();
  trackRelIsoRp3CorrVsPV_Sig->Write();
  trackRelIsoRp3VsPV_NotSig->Write();
  trackRelIsoRp3CorrVsPV_NotSig->Write();

  TProfile* trackRelIsoRp3VsPV_Sig_pfx    = trackRelIsoRp3VsPV_Sig   ->ProfileX(); 
  TProfile* trackRelIsoRp3VsPV_NotSig_pfx = trackRelIsoRp3VsPV_NotSig->ProfileX(); 

  TProfile* trackRelIsoRp3VsPV_Sig_pfx2    = trackRelIsoRp3VsPV_Sig   ->ProfileX("BNHist_trackRelIsoRp3VsPV_Sig_pfx2"); 
  TProfile* trackRelIsoRp3VsPV_NotSig_pfx2 = trackRelIsoRp3VsPV_NotSig->ProfileX("BNHist_trackRelIsoRp3VsPV_NotSig_pfx2"); 
  trackRelIsoRp3VsPV_Sig_pfx   ->Rebin(2);
  trackRelIsoRp3VsPV_NotSig_pfx->Rebin(2);  
  trackRelIsoRp3VsPV_Sig_pfx2   ->Rebin(5);
  trackRelIsoRp3VsPV_NotSig_pfx2->Rebin(5);  

  trackRelIsoRp3VsPV_Sig_pfx    ->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)");  	 
  trackRelIsoRp3VsPV_NotSig_pfx ->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (not sig.)");  
  trackRelIsoRp3VsPV_Sig_pfx2   ->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)");  	 
  trackRelIsoRp3VsPV_NotSig_pfx2->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (not sig.)");  


  trackRelIsoRp3VsPV_Sig_pfx    ->Write();
  trackRelIsoRp3VsPV_NotSig_pfx ->Write();
  trackRelIsoRp3VsPV_Sig_pfx2   ->Write();
  trackRelIsoRp3VsPV_NotSig_pfx2->Write();

  TProfile* trackRelIsoRp3CorrVsPV_Sig_pfx    = trackRelIsoRp3CorrVsPV_Sig   ->ProfileX(); 
  TProfile* trackRelIsoRp3CorrVsPV_NotSig_pfx = trackRelIsoRp3CorrVsPV_NotSig->ProfileX(); 

  TProfile* trackRelIsoRp3CorrVsPV_Sig_pfx2    = trackRelIsoRp3CorrVsPV_Sig   ->ProfileX("BNHist_trackRelIsoRp3CorrVsPV_Sig_pfx2"); 
  TProfile* trackRelIsoRp3CorrVsPV_NotSig_pfx2 = trackRelIsoRp3CorrVsPV_NotSig->ProfileX("BNHist_trackRelIsoRp3CorrVsPV_NotSig_pfx2"); 
  trackRelIsoRp3CorrVsPV_Sig_pfx   ->Rebin(2);
  trackRelIsoRp3CorrVsPV_NotSig_pfx->Rebin(2);  
  trackRelIsoRp3CorrVsPV_Sig_pfx2   ->Rebin(5);
  trackRelIsoRp3CorrVsPV_NotSig_pfx2->Rebin(5);  

  trackRelIsoRp3CorrVsPV_Sig_pfx    ->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)");  	 
  trackRelIsoRp3CorrVsPV_NotSig_pfx ->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (not sig.)");  
  trackRelIsoRp3CorrVsPV_Sig_pfx2   ->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (signal)");  	 
  trackRelIsoRp3CorrVsPV_NotSig_pfx2->SetYTitle("#sum(p_{T})^{#DeltaR<0.3}-p_{T}^{track}) / p_{T}^{track} (#rho corr) (not sig.)");  

  trackRelIsoRp3CorrVsPV_Sig_pfx    ->Write();
  trackRelIsoRp3CorrVsPV_NotSig_pfx ->Write();
  trackRelIsoRp3CorrVsPV_Sig_pfx2   ->Write();
  trackRelIsoRp3CorrVsPV_NotSig_pfx2->Write();


  //trackdepTrkRp5MinusPt_isIso    ->Write();
  //trackdepTrkRp5MinusPt_isNotIso    ->Write();
  //trackGenMatchedId_isIso ->Write();
  trackGenMatchedId_isNotIso ->Write();


  trackDeltaR_Sig        ->Write();
  trackDeltaR_NotSig     ->Write();
  trackMetDeltaPhi_Sig   ->Write();
  trackMetDeltaPhi_NotSig->Write();
  trackJetDeltaR_Sig     ->Write();
  trackJetDeltaR_NotSig  ->Write();
  trackJetDeltaR_PreCut  ->Write();  
  hNTrksBest_Sig         ->Write();
  hNTrksBest_NotSig      ->Write();

  trackdepTrkRp5MinusPtBest_Sig ->Write();
  trackdepTrkRp5MinusPtBest_NotSig ->Write();

  //  trackJet1DeltaR ->Write();
  //trackJet1DeltaR_isIso ->Write();
  //trackJet1DeltaR_isNotIso ->Write();
  //trackJet2DeltaR ->Write();
  //trackJet2DeltaR_isIso ->Write();
  //trackJet2DeltaR_isNotIso ->Write();
  trackCaloTot             ->Write();
  trackCaloTotByP          ->Write();


  trackPtByDepTrkRp5_PreCut    ->Write();
  trackdepTrkRp5MinusPtPreCut ->Write();  
  trackdepTrkRp5MinusPtPostCut->Write();  
  trackNHitsMissingOutPreCut  ->Write();  
  trackNHitsMissingOutPostCut ->Write();  
  trackCaloTotBest            ->Write();  
  trackCaloTotByPBest         ->Write();  
  trackCaloTotSigReg          ->Write();
  trackCaloTotByPSigReg       ->Write();

  trackGenMatchedIdFitReg     ->Write();    
  trackGenMatchedIdSigReg     ->Write();    


  fOut->Close();  

  cout << "Total events found that pass presel (wtd):  " << nEvtPassPre 
       << "  ( " << nEvtPassPreWtd << " )" << endl;  

  cout << "Finished BNTree::Loop() successfully." << endl;
  cout << "Total time to run BNTree::Loop():  " << flush;
  timer.Print();  


} // void BNTree::Loop()

