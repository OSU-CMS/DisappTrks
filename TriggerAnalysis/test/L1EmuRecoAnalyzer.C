#define L1EmuRecoAnalyzer_cxx
#include "L1EmuRecoAnalyzer.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLegend.h>

void L1EmuRecoAnalyzer::Loop()
{
//   In a ROOT session, you can do:
//      root> .L L1EmuRecoAnalyzer.C
//      root> L1EmuRecoAnalyzer t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
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
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      EMTHF->Fill(L1ETMHFPt);
      EMTHF_offline->Fill(passOfflineSelection ? L1ETMHFPt : -99 );

      HTT->Fill(L1HTT);
      HTT_offline->Fill(passOfflineSelection ? L1HTT : -99 );

      double leadingJetPt = -1.0;
      double maxdPhiMetJet = -1.0;
      std::vector<double> vL1JetPt = *L1JetPt;
      std::vector<double> vL1dPhiJetMet = *L1dPhiJetMet; 
      for (size_t index = 0; index < vL1JetPt.size(); ++index) {
         leadingJetPt = max(vL1JetPt.at(index),leadingJetPt);
         if (vL1JetPt.at(index) > 60 && L1HTT > 60 && L1ETMHFPt > 90) {
            maxdPhiMetJet = max(vL1dPhiJetMet.at(index),maxdPhiMetJet);
         }
      }
      dPhi->Fill(maxdPhiMetJet);
      dPhi_offline->Fill(passOfflineSelection ? maxdPhiMetJet : -1.0);
      JetPt->Fill(leadingJetPt);
      JetPt_offline->Fill(passOfflineSelection ? leadingJetPt : -1.0);
      if (passOfflineSelection) {
         nPassOffline++;
      }
   }
}


void L1EmuRecoAnalyzer::Finish()
{
   Loop();
   TCanvas *c1 = new TCanvas("c1","c1", 600,600);

   TH1D* EMTHF_cumulative = (TH1D*) EMTHF->GetCumulative(0);
   TH1D* HTT_cumulative   = (TH1D*) HTT->GetCumulative(0);
   TH1D* JetPt_cumulative = (TH1D*) JetPt->GetCumulative(0);
   TH1D* dPhi_cumulative  = (TH1D*) dPhi->GetCumulative(0);

   TH1D* EMTHF_offline_cumulative = (TH1D*) EMTHF_offline->GetCumulative(0);
   TH1D* HTT_offline_cumulative   = (TH1D*) HTT_offline->GetCumulative(0);
   TH1D* JetPt_offline_cumulative = (TH1D*) JetPt_offline->GetCumulative(0);
   TH1D* dPhi_offline_cumulative  = (TH1D*) dPhi_offline->GetCumulative(0);

   TH1D* efficiencyEMTHF = (TH1D*) EMTHF_offline_cumulative->Clone();
   efficiencyEMTHF->Scale(1.0/nPassOffline);
   efficiencyEMTHF->SetStats(0);
   efficiencyEMTHF->SetTitle("Efficiency over EMTHF threshold");
   efficiencyEMTHF->GetXaxis()->SetTitle("EMTHF threshold [GeV]");
   efficiencyEMTHF->GetYaxis()->SetTitle("passOffline/nPassOffline");
   TLegend *lgEMTHF = new TLegend(0.4,0.7,0.85,0.8,"","brNDC");
   lgEMTHF->SetBorderSize(0);
   lgEMTHF->SetLineWidth(7);
   lgEMTHF->SetTextSize(0.03);
   lgEMTHF->AddEntry(efficiencyEMTHF, "L1_EMTHF* SingleLeg", "l");
   efficiencyEMTHF->Draw("PE");
   lgEMTHF->Draw("same");
   c1->SaveAs("EfficiencyOverEMTHF.pdf");
   c1->Update();

   TH1D* efficiencyHTT = (TH1D*) HTT_offline_cumulative->Clone();
   efficiencyHTT->Scale(1.0/nPassOffline);
   efficiencyHTT->SetStats(0);
   efficiencyHTT->SetTitle("Efficiency over HTT");
   efficiencyHTT->GetXaxis()->SetTitle("HTT threshold [GeV]");
   efficiencyHTT->GetYaxis()->SetTitle("passOffline/nPassOffline");
   TLegend *lgHTT = new TLegend(0.4,0.7,0.85,0.8,"","brNDC");
   lgHTT->SetBorderSize(0);
   lgHTT->SetLineWidth(7);
   lgHTT->SetTextSize(0.03);
   lgHTT->AddEntry(efficiencyHTT, "L1_HTT* SingleLeg", "l");
   efficiencyHTT->Draw("PE");
   lgHTT->Draw("same");
   c1->SaveAs("EfficiencyOverHTT.pdf");
   c1->Update();

   TH1D* efficiencyJetPt = (TH1D*) JetPt_offline_cumulative->Clone();
   efficiencyJetPt->Scale(1.0/nPassOffline);
   efficiencyJetPt->SetStats(0);
   efficiencyJetPt->SetTitle("Efficiency over JetPt");
   efficiencyJetPt->GetXaxis()->SetTitle("JetPt threshold [GeV]");
   efficiencyJetPt->GetYaxis()->SetTitle("passOffline/nPassOffline");
   TLegend *lgJetPt = new TLegend(0.4,0.7,0.85,0.8,"","brNDC");
   lgJetPt->SetBorderSize(0);
   lgJetPt->SetLineWidth(7);
   lgJetPt->SetTextSize(0.03);
   lgJetPt->AddEntry(efficiencyJetPt, "L1_Jet* SingleLeg", "l");
   efficiencyJetPt->Draw("PE");
   lgJetPt->Draw("same");
   c1->SaveAs("EfficiencyOverJetPt.pdf");
   c1->Update();

   TH1D* efficiencydPhi = (TH1D*) dPhi_offline_cumulative->Clone();
   efficiencydPhi->Scale(1.0/nPassOffline);
   efficiencydPhi->SetStats(0);
   efficiencydPhi->SetTitle("Efficiency over dPhi");
   efficiencydPhi->GetXaxis()->SetTitle("dPhi [rad]");
   efficiencydPhi->GetYaxis()->SetTitle("(passOffline && passL1)/nPassOffline");
   TLegend *lgdPhi = new TLegend(0.15,0.15,0.45,0.5,"","brNDC");
   lgdPhi->SetBorderSize(0);
   lgdPhi->SetLineWidth(7);
   lgdPhi->SetTextSize(0.02);
   lgdPhi->AddEntry(efficiencydPhi, "L1_EMTHF90_HTT60er_SingleJet60_dPhi(EMTHF,Jet60)*", "l");
   efficiencydPhi->Draw("PE");
   lgdPhi->Draw("same");
   c1->SaveAs("EfficiencyOverdPhiCut.pdf");
   c1->Update();
}
