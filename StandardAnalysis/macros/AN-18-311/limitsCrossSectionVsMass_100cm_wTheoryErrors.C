void limitsCrossSectionVsMass_100cm_wTheoryErrors()
{
//=========Macro generated from canvas: limits_vs_100cm/
//=========  (Wed Feb 12 12:57:23 2020) by ROOT version 6.14/06
   TCanvas *limits_vs_100cm = new TCanvas("limits_vs_100cm", "",154,209,800,719);
   limits_vs_100cm->SetHighLightColor(2);
   limits_vs_100cm->Range(-74.51404,-3.851908,1142.848,3.476336);
   limits_vs_100cm->SetFillColor(0);
   limits_vs_100cm->SetBorderMode(0);
   limits_vs_100cm->SetBorderSize(2);
   limits_vs_100cm->SetLogy();
   limits_vs_100cm->SetTickx(1);
   limits_vs_100cm->SetTicky(1);
   limits_vs_100cm->SetLeftMargin(0.1425);
   limits_vs_100cm->SetRightMargin(0.035);
   limits_vs_100cm->SetTopMargin(0.065);
   limits_vs_100cm->SetBottomMargin(0.11625);
   limits_vs_100cm->SetFrameFillStyle(0);
   limits_vs_100cm->SetFrameBorderMode(0);
   limits_vs_100cm->SetFrameFillStyle(0);
   limits_vs_100cm->SetFrameBorderMode(0);
   
   TH1F *hBackground__5__1__1 = new TH1F("hBackground__5__1__1","hBackground",1000,90,1210);
   hBackground__5__1__1->SetMinimum(0.001);
   hBackground__5__1__1->SetMaximum(1000);
   hBackground__5__1__1->SetDirectory(0);
   hBackground__5__1__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hBackground__5__1__1->SetLineColor(ci);
   hBackground__5__1__1->SetLineStyle(0);
   hBackground__5__1__1->SetMarkerStyle(20);
   hBackground__5__1__1->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground__5__1__1->GetXaxis()->SetRange(9,902);
   hBackground__5__1__1->GetXaxis()->SetNdivisions(505);
   hBackground__5__1__1->GetXaxis()->SetLabelFont(42);
   hBackground__5__1__1->GetXaxis()->SetLabelSize(0.055);
   hBackground__5__1__1->GetXaxis()->SetTitleSize(0.045);
   hBackground__5__1__1->GetXaxis()->SetTitleOffset(1.15);
   hBackground__5__1__1->GetXaxis()->SetTitleFont(42);
   hBackground__5__1__1->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground__5__1__1->GetYaxis()->SetNdivisions(505);
   hBackground__5__1__1->GetYaxis()->SetLabelFont(42);
   hBackground__5__1__1->GetYaxis()->SetLabelSize(0.055);
   hBackground__5__1__1->GetYaxis()->SetTitleSize(0.045);
   hBackground__5__1__1->GetYaxis()->SetTitleOffset(1.5);
   hBackground__5__1__1->GetYaxis()->SetTitleFont(42);
   hBackground__5__1__1->GetZaxis()->SetNdivisions(509);
   hBackground__5__1__1->GetZaxis()->SetLabelFont(42);
   hBackground__5__1__1->GetZaxis()->SetLabelOffset(0.007);
   hBackground__5__1__1->GetZaxis()->SetLabelSize(0.045);
   hBackground__5__1__1->GetZaxis()->SetTitleSize(0.06);
   hBackground__5__1__1->GetZaxis()->SetTitleFont(42);
   hBackground__5__1__1->Draw("axis");
   
   Double_t limits_vs_100cm_graph_twoSigma_fx3001[11] = {
   100,
   200,
   300,
   400,
   500,
   600,
   700,
   800,
   900,
   1000,
   1100};
   Double_t limits_vs_100cm_graph_twoSigma_fy3001[11] = {
   0.03676517,
   0.0122631,
   0.007729327,
   0.005747431,
   0.005487279,
   0.00453562,
   0.00419141,
   0.003902661,
   0.003751977,
   0.003833578,
   0.003715331};
   Double_t limits_vs_100cm_graph_twoSigma_felx3001[11] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t limits_vs_100cm_graph_twoSigma_fely3001[11] = {
   0.01737729,
   0.005796232,
   0.003623122,
   0.002716559,
   0.002593597,
   0.002143789,
   0.001997469,
   0.001859862,
   0.001788052,
   0.001871864,
   0.001814126};
   Double_t limits_vs_100cm_graph_twoSigma_fehx3001[11] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t limits_vs_100cm_graph_twoSigma_fehy3001[11] = {
   0.0376152,
   0.01236199,
   0.007791656,
   0.005865728,
   0.005614148,
   0.004668806,
   0.004361672,
   0.00408544,
   0.003960298,
   0.004337362,
   0.004212195};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(11,limits_vs_100cm_graph_twoSigma_fx3001,limits_vs_100cm_graph_twoSigma_fy3001,limits_vs_100cm_graph_twoSigma_felx3001,limits_vs_100cm_graph_twoSigma_fehx3001,limits_vs_100cm_graph_twoSigma_fely3001,limits_vs_100cm_graph_twoSigma_fehy3001);
   grae->SetName("limits_vs_100cm_graph_twoSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#ffcc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#ffcc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#ffcc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001 = new TH1F("Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetMinimum(0.001711084);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetMaximum(0.08162829);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_100cm_graph_twoSigma300330013001);
   
   grae->Draw("3");
   
   Double_t limits_vs_100cm_graph_oneSigma_fx3002[11] = {
   100,
   200,
   300,
   400,
   500,
   600,
   700,
   800,
   900,
   1000,
   1100};
   Double_t limits_vs_100cm_graph_oneSigma_fy3002[11] = {
   0.03676517,
   0.0122631,
   0.007729327,
   0.005747431,
   0.005487279,
   0.00453562,
   0.00419141,
   0.003902661,
   0.003751977,
   0.003833578,
   0.003715331};
   Double_t limits_vs_100cm_graph_oneSigma_felx3002[11] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t limits_vs_100cm_graph_oneSigma_fely3002[11] = {
   0.01072504,
   0.003577362,
   0.002236146,
   0.001676626,
   0.001600735,
   0.00132312,
   0.001232813,
   0.001147883,
   0.001117532,
   0.001169915,
   0.001133829};
   Double_t limits_vs_100cm_graph_oneSigma_fehx3002[11] = {
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t limits_vs_100cm_graph_oneSigma_fehy3002[11] = {
   0.01626678,
   0.005376937,
   0.003389036,
   0.002520046,
   0.00242785,
   0.002006788,
   0.001887906,
   0.001757848,
   0.001704932,
   0.001833697,
   0.001791946};
   grae = new TGraphAsymmErrors(11,limits_vs_100cm_graph_oneSigma_fx3002,limits_vs_100cm_graph_oneSigma_fy3002,limits_vs_100cm_graph_oneSigma_felx3002,limits_vs_100cm_graph_oneSigma_fehx3002,limits_vs_100cm_graph_oneSigma_fely3002,limits_vs_100cm_graph_oneSigma_fehy3002);
   grae->SetName("limits_vs_100cm_graph_oneSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#00cc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#00cc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002 = new TH1F("Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetMinimum(0.002323352);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetMaximum(0.05807699);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_100cm_graph_oneSigma300430023002);
   
   grae->Draw("3");
   
   Double_t limits_vs_100cm_graph_expected_fx1[11] = {
   100,
   200,
   300,
   400,
   500,
   600,
   700,
   800,
   900,
   1000,
   1100};
   Double_t limits_vs_100cm_graph_expected_fy1[11] = {
   0.03676517,
   0.0122631,
   0.007729327,
   0.005747431,
   0.005487279,
   0.00453562,
   0.00419141,
   0.003902661,
   0.003751977,
   0.003833578,
   0.003715331};
   TGraph *graph = new TGraph(11,limits_vs_100cm_graph_expected_fx1,limits_vs_100cm_graph_expected_fy1);
   graph->SetName("limits_vs_100cm_graph_expected");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_100cm_graph_expected811 = new TH1F("Graph_Graph_Graph_limits_vs_100cm_graph_expected811","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetMinimum(0.0004103469);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetMaximum(0.04007015);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_expected811->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_100cm_graph_expected811);
   
   graph->Draw("l");
   
   Double_t limits_vs_100cm_graph_observed_fx2[11] = {
   100,
   200,
   300,
   400,
   500,
   600,
   700,
   800,
   900,
   1000,
   1100};
   Double_t limits_vs_100cm_graph_observed_fy2[11] = {
   0.03873803,
   0.01310709,
   0.008159459,
   0.005927583,
   0.005866023,
   0.004873607,
   0.004472242,
   0.004327771,
   0.003995967,
   0.003687899,
   0.003586721};
   graph = new TGraph(11,limits_vs_100cm_graph_observed_fx2,limits_vs_100cm_graph_observed_fy2);
   graph->SetName("limits_vs_100cm_graph_observed");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_100cm_graph_observed922 = new TH1F("Graph_Graph_Graph_limits_vs_100cm_graph_observed922","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetMinimum(7.159007e-05);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetMaximum(0.04225317);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_100cm_graph_observed922->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_100cm_graph_observed922);
   
   graph->Draw("l");
   
   Double_t limits_vs_100cm_graph_theory_fx3[11] = {
   100,
   200,
   300,
   400,
   500,
   600,
   700,
   800,
   900,
   1000,
   1100};
   Double_t limits_vs_100cm_graph_theory_fy3[11] = {
   34.282,
   2.709959,
   0.577095,
   0.1796441,
   0.0684798,
   0.02963633,
   0.01394902,
   0.0069704,
   0.00364968,
   0.001965386,
   0.001082998};

   Double_t theoryUnc[11] = {
      0.03218703897,
      0.0423204534,
      0.05127486773,
      0.05965032887,
      0.06714568106,
      0.0755393968,
      0.08150186132,
      0.08823733246,
      0.09374351066,
      0.09758102944,
      0.10655204766};

   TGraphErrors * graphTheory = new TGraphErrors();
   for(int i = 0; i < 11; i++) {
        graphTheory->SetPoint(i, limits_vs_100cm_graph_theory_fx3[i], limits_vs_100cm_graph_theory_fy3[i]);
        graphTheory->SetPointError(i, 0.0, limits_vs_100cm_graph_theory_fy3[i] * theoryUnc[i]);
   }

   graphTheory->SetName("limits_vs_100cm_graph_theory");
   graphTheory->SetTitle("Graph");
   graphTheory->SetFillStyle(1001);
   graphTheory->SetFillColorAlpha(kRed-7, 0.45);
   graphTheory->SetLineColor(kRed);
   graphTheory->SetLineStyle(1);
   graphTheory->SetLineWidth(2);
   graphTheory->SetMarkerColor(2);
   graphTheory->SetMarkerStyle(21);
   
   graphTheory->Draw("3");
   graphTheory->Draw("lX");
   
   //TLegend *leg = new TLegend(0.5877193,0.7363112,0.9461153,0.8731988,NULL,"brNDC");
   //TLegend *leg = new TLegend(0.55, 0.65, 0.95, 0.85, NULL, "brNDC");
   TLegend *leg = new TLegend(0.537594, 0.667147, 0.938596, 0.865994, NULL, "brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.0361757);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("limits_vs_100cm_graph_twoSigma","95% expected","F");

   ci = TColor::GetColor("#ffcc00");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1000);

   ci = TColor::GetColor("#ffcc00");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_100cm_graph_oneSigma","68% expected","F");

   ci = TColor::GetColor("#00cc00");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1000);

   ci = TColor::GetColor("#00cc00");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_100cm_graph_expected","Median expected","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_100cm_graph_observed","Observed","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_100cm_graph_theory","NLO+NLL theory (#pm1#sigma)","FL");
   entry->SetLineColor(2);
   entry->SetLineStyle(9);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   TPaveLabel *pl = new TPaveLabel(0.695489,0.939276,0.974937,0.989664,"140 fb^{-1} (13 TeV)","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(32);
   pl->SetTextFont(42);
   pl->SetTextSize(0.756287);
   pl->Draw();
   
   pl = new TPaveLabel(0.2894737,0.8083573,0.4373434,0.9106628,"CMS","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(12);
   pl->SetTextSize(0.448718);
   pl->Draw();
   
   pl = new TPaveLabel(0.14787,0.726098,0.531328,0.776486,"c#tau_{#tilde{#chi}^{#pm}_{1}} = 100 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = 3.34 ns)","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextFont(42);
   //pl->SetTextSize(0.517241);
   pl->SetTextSize(0.7);
   pl->Draw();
   
   pl = new TPaveLabel(0.007518797,0.7680115,0.4210526,0.8371758,"Wino-like #tilde{#chi}_{0}","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(32);
   pl->SetTextFont(42);
   pl->SetTextSize(0.517241);
   pl->Draw();
   
   TH1F *hBackground_copy__6__2__2 = new TH1F("hBackground_copy__6__2__2","hBackground",1000,90,1210);
   hBackground_copy__6__2__2->SetMinimum(0.001);
   hBackground_copy__6__2__2->SetMaximum(1000);
   hBackground_copy__6__2__2->SetDirectory(0);
   hBackground_copy__6__2__2->SetStats(0);

   ci = TColor::GetColor("#000099");
   hBackground_copy__6__2__2->SetLineColor(ci);
   hBackground_copy__6__2__2->SetLineStyle(0);
   hBackground_copy__6__2__2->SetMarkerStyle(20);
   hBackground_copy__6__2__2->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground_copy__6__2__2->GetXaxis()->SetRange(9,902);
   hBackground_copy__6__2__2->GetXaxis()->SetNdivisions(505);
   hBackground_copy__6__2__2->GetXaxis()->SetLabelFont(42);
   hBackground_copy__6__2__2->GetXaxis()->SetLabelSize(0.035);
   hBackground_copy__6__2__2->GetXaxis()->SetTitleSize(0.035);
   hBackground_copy__6__2__2->GetXaxis()->SetTitleOffset(1.25);
   hBackground_copy__6__2__2->GetXaxis()->SetTitleFont(42);
   hBackground_copy__6__2__2->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground_copy__6__2__2->GetYaxis()->SetNdivisions(505);
   hBackground_copy__6__2__2->GetYaxis()->SetLabelFont(42);
   hBackground_copy__6__2__2->GetYaxis()->SetLabelSize(0.035);
   hBackground_copy__6__2__2->GetYaxis()->SetTitleSize(0.035);
   hBackground_copy__6__2__2->GetYaxis()->SetTitleOffset(1.25);
   hBackground_copy__6__2__2->GetYaxis()->SetTitleFont(42);
   hBackground_copy__6__2__2->GetZaxis()->SetNdivisions(509);
   hBackground_copy__6__2__2->GetZaxis()->SetLabelFont(42);
   hBackground_copy__6__2__2->GetZaxis()->SetLabelOffset(0.007);
   hBackground_copy__6__2__2->GetZaxis()->SetLabelSize(0.045);
   hBackground_copy__6__2__2->GetZaxis()->SetTitleSize(0.06);
   hBackground_copy__6__2__2->GetZaxis()->SetTitleFont(42);
   hBackground_copy__6__2__2->Draw("sameaxig");
   limits_vs_100cm->Modified();
   limits_vs_100cm->cd();
   limits_vs_100cm->SetSelected(limits_vs_100cm);

   limits_vs_100cm->SaveAs("limitsCrossSectionVsMass_100cm_wTheoryErrors.pdf");

}
