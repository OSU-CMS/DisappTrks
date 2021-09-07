#define Efficiency_cxx
#include "Efficiency.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void Efficiency::Loop()
{
//   In a ROOT session, you can do:
//      root> .L Efficiency.C
//      root> Efficiency t
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
      METNoMuDenominator->Fill(MetNoMuPt, offlineSelection_NoMETNoMu);
      METNoMuNumerator->Fill(MetNoMuPt, offlineSelection_NoMETNoMu && fireTrigger);
   }
}

void Efficiency::Finish()
{
      Loop();
      TCanvas *c1 = new TCanvas("c1","c1", 600,600);

      METNoMuDenominator->SetStats(0);
      METNoMuDenominator->SetTitle("offlineSelection w/o METNoMu");
      METNoMuDenominator->GetXaxis()->SetTitle("p_{T}^{miss,no #mu} [GeV]");
      METNoMuDenominator->GetYaxis()->SetTitle("nEntries/10GeV");
      TLegend *lgMETNoMuDenom = new TLegend(0.4,0.7,0.85,0.8,"","brNDC");
      lgMETNoMuDenom->SetBorderSize(0);
      lgMETNoMuDenom->SetLineWidth(7);
      lgMETNoMuDenom->SetTextSize(0.03);
      lgMETNoMuDenom->AddEntry(METNoMuDenominator, "offline w/o METNoMu", "lp");
      METNoMuDenominator->SetMarkerStyle(8);
      METNoMuDenominator->SetMarkerSize(1.2);
      METNoMuDenominator->Draw("PE1");
      lgMETNoMuDenom->Draw("same");
      c1->SaveAs("METNoMu_looseOffline_"+fTriggerName+".pdf");
      c1->Update();

      METNoMuNumerator->SetStats(0);
      METNoMuNumerator->SetTitle("fired offlineSelection w/o METNoMu");
      METNoMuNumerator->GetXaxis()->SetTitle("p_{T}^{miss,no #mu} [GeV]");
      METNoMuNumerator->GetYaxis()->SetTitle("nEntries/10GeV");
      TLegend *lgMETNoMuNume = new TLegend(0.4,0.7,0.85,0.8,"","brNDC");
      lgMETNoMuNume->SetBorderSize(0);
      lgMETNoMuNume->SetLineWidth(7);
      lgMETNoMuNume->SetTextSize(0.03);
      lgMETNoMuNume->AddEntry(METNoMuNumerator, "Trigger fired && offline w/o METNoMu", "lp");
      METNoMuNumerator->SetMarkerStyle(8);
      METNoMuNumerator->SetMarkerSize(1.2);
      METNoMuNumerator->Draw("PE1");
      lgMETNoMuNume->Draw("same");
      c1->SaveAs("METNoMu_firedlooseOffline_"+fTriggerName+".pdf");
      c1->Update();

      METNoMuNumerator->SetLineColor(kRed);
      METNoMuNumerator->SetMarkerColor(kRed);
      METNoMuDenominator->SetLineColor(kBlack);
      METNoMuDenominator->SetMarkerColor(kBlack);
      METNoMuDenominator->Draw("PE1");
      METNoMuNumerator->Draw("PE1same");
      c1->SaveAs("compare_"+fTriggerName+".pdf");
      c1->Update();

      METNoMuEfficiency = (TH1D*) METNoMuNumerator->Clone();
      METNoMuEfficiency->Divide(METNoMuDenominator); 
      METNoMuEfficiency->GetYaxis()->SetRangeUser(0.0,1.1);
      METNoMuEfficiency->SetStats(0);
      METNoMuEfficiency->SetTitle(fTriggerName+" Efficiency");
      METNoMuEfficiency->GetXaxis()->SetTitle("p_{T}^{miss,no #mu} [GeV]");
      METNoMuEfficiency->GetYaxis()->SetTitle("nEntries/10GeV");
      TLegend *lgMETNoMuEff = new TLegend(0.4,0.7,0.85,0.8,"","brNDC");
      lgMETNoMuEff->SetBorderSize(0);
      lgMETNoMuEff->SetLineWidth(7);
      lgMETNoMuEff->SetTextSize(0.03);
      lgMETNoMuEff->AddEntry(METNoMuEfficiency, "Trigger efficiency (offline w/o METNoMu)", "lp");
      METNoMuEfficiency->SetMarkerStyle(8);
      METNoMuEfficiency->SetMarkerSize(1.2);
      METNoMuEfficiency->SetMarkerColor(kBlack);
      METNoMuEfficiency->SetLineColor(kBlack);
      METNoMuEfficiency->Draw("PE1");
      //lgMETNoMuEff->Draw("same");
      c1->SaveAs("METNoMu_triggerEfficiency_"+fTriggerName+".pdf");
      c1->Update();

}
