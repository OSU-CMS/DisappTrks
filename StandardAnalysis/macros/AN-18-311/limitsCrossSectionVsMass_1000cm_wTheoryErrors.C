void limitsCrossSectionVsMass_1000cm_wTheoryErrors()
{
//=========Macro generated from canvas: limits_vs_1000cm/
//=========  (Wed Feb 12 12:59:13 2020) by ROOT version 6.14/06
   TCanvas *limits_vs_1000cm = new TCanvas("limits_vs_1000cm", "",0,89,800,719);
   limits_vs_1000cm->SetHighLightColor(2);
   limits_vs_1000cm->Range(-74.51404,-3.851908,1142.848,3.476336);
   limits_vs_1000cm->SetFillColor(0);
   limits_vs_1000cm->SetBorderMode(0);
   limits_vs_1000cm->SetBorderSize(2);
   limits_vs_1000cm->SetLogy();
   limits_vs_1000cm->SetTickx(1);
   limits_vs_1000cm->SetTicky(1);
   limits_vs_1000cm->SetLeftMargin(0.1425);
   limits_vs_1000cm->SetRightMargin(0.035);
   limits_vs_1000cm->SetTopMargin(0.065);
   limits_vs_1000cm->SetBottomMargin(0.11625);
   limits_vs_1000cm->SetFrameFillStyle(0);
   limits_vs_1000cm->SetFrameBorderMode(0);
   limits_vs_1000cm->SetFrameFillStyle(0);
   limits_vs_1000cm->SetFrameBorderMode(0);
   
   TH1F *hBackground__7__1__1 = new TH1F("hBackground__7__1__1","hBackground",1000,90,1210);
   hBackground__7__1__1->SetMinimum(0.001);
   hBackground__7__1__1->SetMaximum(1000);
   hBackground__7__1__1->SetDirectory(0);
   hBackground__7__1__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hBackground__7__1__1->SetLineColor(ci);
   hBackground__7__1__1->SetLineStyle(0);
   hBackground__7__1__1->SetMarkerStyle(20);
   hBackground__7__1__1->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground__7__1__1->GetXaxis()->SetRange(9,902);
   hBackground__7__1__1->GetXaxis()->SetNdivisions(505);
   hBackground__7__1__1->GetXaxis()->SetLabelFont(42);
   hBackground__7__1__1->GetXaxis()->SetLabelSize(0.055);
   hBackground__7__1__1->GetXaxis()->SetTitleSize(0.045);
   hBackground__7__1__1->GetXaxis()->SetTitleOffset(1.15);
   hBackground__7__1__1->GetXaxis()->SetTitleFont(42);
   hBackground__7__1__1->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground__7__1__1->GetYaxis()->SetNdivisions(505);
   hBackground__7__1__1->GetYaxis()->SetLabelFont(42);
   hBackground__7__1__1->GetYaxis()->SetLabelSize(0.055);
   hBackground__7__1__1->GetYaxis()->SetTitleSize(0.045);
   hBackground__7__1__1->GetYaxis()->SetTitleOffset(1.5);
   hBackground__7__1__1->GetYaxis()->SetTitleFont(42);
   hBackground__7__1__1->GetZaxis()->SetNdivisions(509);
   hBackground__7__1__1->GetZaxis()->SetLabelFont(42);
   hBackground__7__1__1->GetZaxis()->SetLabelOffset(0.007);
   hBackground__7__1__1->GetZaxis()->SetLabelSize(0.045);
   hBackground__7__1__1->GetZaxis()->SetTitleSize(0.06);
   hBackground__7__1__1->GetZaxis()->SetTitleFont(42);
   hBackground__7__1__1->Draw("axis");
   
   Double_t limits_vs_1000cm_graph_twoSigma_fx3001[11] = {
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
   Double_t limits_vs_1000cm_graph_twoSigma_fy3001[11] = {
   0.1670407,
   0.07263631,
   0.0384414,
   0.02711006,
   0.02280941,
   0.01875278,
   0.01483843,
   0.01406893,
   0.01349447,
   0.01297587,
   0.01168171};
   Double_t limits_vs_1000cm_graph_twoSigma_felx3001[11] = {
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
   Double_t limits_vs_1000cm_graph_twoSigma_fely3001[11] = {
   0.08286785,
   0.03518321,
   0.01816957,
   0.01281374,
   0.01069191,
   0.008863617,
   0.007071439,
   0.006704723,
   0.006483671,
   0.00638656,
   0.005795225};
   Double_t limits_vs_1000cm_graph_twoSigma_fehx3001[11] = {
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
   Double_t limits_vs_1000cm_graph_twoSigma_fehy3001[11] = {
   0.1962252,
   0.07961662,
   0.03981024,
   0.02821132,
   0.02362161,
   0.01951455,
   0.01588248,
   0.01493726,
   0.01444396,
   0.01508576,
   0.01374869};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(11,limits_vs_1000cm_graph_twoSigma_fx3001,limits_vs_1000cm_graph_twoSigma_fy3001,limits_vs_1000cm_graph_twoSigma_felx3001,limits_vs_1000cm_graph_twoSigma_fehx3001,limits_vs_1000cm_graph_twoSigma_fely3001,limits_vs_1000cm_graph_twoSigma_fehy3001);
   grae->SetName("limits_vs_1000cm_graph_twoSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#ffcc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#ffcc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#ffcc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001 = new TH1F("Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetMinimum(0.00529784);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetMaximum(0.3990038);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_1000cm_graph_twoSigma300530013001);
   
   grae->Draw("3");
   
   Double_t limits_vs_1000cm_graph_oneSigma_fx3002[11] = {
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
   Double_t limits_vs_1000cm_graph_oneSigma_fy3002[11] = {
   0.1670407,
   0.07263631,
   0.0384414,
   0.02711006,
   0.02280941,
   0.01875278,
   0.01483843,
   0.01406893,
   0.01349447,
   0.01297587,
   0.01168171};
   Double_t limits_vs_1000cm_graph_oneSigma_felx3002[11] = {
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
   Double_t limits_vs_1000cm_graph_oneSigma_fely3002[11] = {
   0.05243981,
   0.02171464,
   0.01121403,
   0.007908479,
   0.006598915,
   0.005470514,
   0.004419649,
   0.004190452,
   0.004001641,
   0.0039916,
   0.003622016};
   Double_t limits_vs_1000cm_graph_oneSigma_fehx3002[11] = {
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
   Double_t limits_vs_1000cm_graph_oneSigma_fehy3002[11] = {
   0.08189726,
   0.03416471,
   0.01700843,
   0.01221099,
   0.01009204,
   0.008446679,
   0.006801861,
   0.006393046,
   0.006185797,
   0.00636185,
   0.005773912};
   grae = new TGraphAsymmErrors(11,limits_vs_1000cm_graph_oneSigma_fx3002,limits_vs_1000cm_graph_oneSigma_fy3002,limits_vs_1000cm_graph_oneSigma_felx3002,limits_vs_1000cm_graph_oneSigma_fehx3002,limits_vs_1000cm_graph_oneSigma_fely3002,limits_vs_1000cm_graph_oneSigma_fehy3002);
   grae->SetName("limits_vs_1000cm_graph_oneSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#00cc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#00cc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002 = new TH1F("Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetMinimum(0.007253728);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetMaximum(0.2730258);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_1000cm_graph_oneSigma300630023002);
   
   grae->Draw("3");
   
   Double_t limits_vs_1000cm_graph_expected_fx1[11] = {
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
   Double_t limits_vs_1000cm_graph_expected_fy1[11] = {
   0.1670407,
   0.07263631,
   0.0384414,
   0.02711006,
   0.02280941,
   0.01875278,
   0.01483843,
   0.01406893,
   0.01349447,
   0.01297587,
   0.01168171};
   TGraph *graph = new TGraph(11,limits_vs_1000cm_graph_expected_fx1,limits_vs_1000cm_graph_expected_fy1);
   graph->SetName("limits_vs_1000cm_graph_expected");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111 = new TH1F("Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetMinimum(0.01051354);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetMaximum(0.1825766);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_1000cm_graph_expected1111);
   
   graph->Draw("l");
   
   Double_t limits_vs_1000cm_graph_observed_fx2[11] = {
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
   Double_t limits_vs_1000cm_graph_observed_fy2[11] = {
   0.1897554,
   0.08125258,
   0.03927531,
   0.02842087,
   0.02595895,
   0.02128613,
   0.01460903,
   0.01477471,
   0.0135944,
   0.01128927,
   0.00991352};
   graph = new TGraph(11,limits_vs_1000cm_graph_observed_fx2,limits_vs_1000cm_graph_observed_fy2);
   graph->SetName("limits_vs_1000cm_graph_observed");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222 = new TH1F("Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetMinimum(0.008922168);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetMaximum(0.2077396);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_1000cm_graph_observed1222);
   
   graph->Draw("l");
   
   Double_t limits_vs_1000cm_graph_theory_fx3[11] = {
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
   Double_t limits_vs_1000cm_graph_theory_fy3[11] = {
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
        graphTheory->SetPoint(i, limits_vs_1000cm_graph_theory_fx3[i], limits_vs_1000cm_graph_theory_fy3[i]);
        graphTheory->SetPointError(i, 0.0, limits_vs_1000cm_graph_theory_fy3[i] * theoryUnc[i]);
   }

   graphTheory->SetName("limits_vs_1000cm_graph_theory");
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
   
   //TLegend *leg = new TLegend(0.5877193,0.7348703,0.9461153,0.8731988,NULL,"brNDC");
   //TLegend *leg = new TLegend(0.55, 0.65, 0.95, 0.85, NULL, "brNDC");
   TLegend *leg = new TLegend(0.537594, 0.667147, 0.938596, 0.865994, NULL, "brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.0361757);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("limits_vs_1000cm_graph_twoSigma","95% expected","F");

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
   entry=leg->AddEntry("limits_vs_1000cm_graph_oneSigma","68% expected","F");

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
   entry=leg->AddEntry("limits_vs_1000cm_graph_expected","Median expected","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_1000cm_graph_observed","Observed","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_1000cm_graph_theory","NLO+NLL theory (#pm1#sigma)","FL");
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
   
   pl = new TPaveLabel(0.2869674,0.8126801,0.4348371,0.9149856,"CMS","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(12);
   pl->SetTextSize(0.448718);
   pl->Draw();
   
   pl = new TPaveLabel(0.14787,0.726098,0.531328,0.776486,"c#tau_{#tilde{#chi}^{#pm}_{1}} = 1000 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = 33.4 ns)","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextFont(42);
   //pl->SetTextSize(0.517241);
   pl->SetTextSize(0.7);
   pl->Draw();
   
   pl = new TPaveLabel(0.01253133,0.7737752,0.4260652,0.8429395,"Wino-like #tilde{#chi}_{0}","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(32);
   pl->SetTextFont(42);
   pl->SetTextSize(0.517241);
   pl->Draw();
   
   TH1F *hBackground_copy__8__2__2 = new TH1F("hBackground_copy__8__2__2","hBackground",1000,90,1210);
   hBackground_copy__8__2__2->SetMinimum(0.001);
   hBackground_copy__8__2__2->SetMaximum(1000);
   hBackground_copy__8__2__2->SetDirectory(0);
   hBackground_copy__8__2__2->SetStats(0);

   ci = TColor::GetColor("#000099");
   hBackground_copy__8__2__2->SetLineColor(ci);
   hBackground_copy__8__2__2->SetLineStyle(0);
   hBackground_copy__8__2__2->SetMarkerStyle(20);
   hBackground_copy__8__2__2->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground_copy__8__2__2->GetXaxis()->SetRange(9,902);
   hBackground_copy__8__2__2->GetXaxis()->SetNdivisions(505);
   hBackground_copy__8__2__2->GetXaxis()->SetLabelFont(42);
   hBackground_copy__8__2__2->GetXaxis()->SetLabelSize(0.035);
   hBackground_copy__8__2__2->GetXaxis()->SetTitleSize(0.035);
   hBackground_copy__8__2__2->GetXaxis()->SetTitleOffset(1.25);
   hBackground_copy__8__2__2->GetXaxis()->SetTitleFont(42);
   hBackground_copy__8__2__2->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground_copy__8__2__2->GetYaxis()->SetNdivisions(505);
   hBackground_copy__8__2__2->GetYaxis()->SetLabelFont(42);
   hBackground_copy__8__2__2->GetYaxis()->SetLabelSize(0.035);
   hBackground_copy__8__2__2->GetYaxis()->SetTitleSize(0.035);
   hBackground_copy__8__2__2->GetYaxis()->SetTitleOffset(1.25);
   hBackground_copy__8__2__2->GetYaxis()->SetTitleFont(42);
   hBackground_copy__8__2__2->GetZaxis()->SetNdivisions(509);
   hBackground_copy__8__2__2->GetZaxis()->SetLabelFont(42);
   hBackground_copy__8__2__2->GetZaxis()->SetLabelOffset(0.007);
   hBackground_copy__8__2__2->GetZaxis()->SetLabelSize(0.045);
   hBackground_copy__8__2__2->GetZaxis()->SetTitleSize(0.06);
   hBackground_copy__8__2__2->GetZaxis()->SetTitleFont(42);
   hBackground_copy__8__2__2->Draw("sameaxig");
   limits_vs_1000cm->Modified();
   limits_vs_1000cm->cd();
   limits_vs_1000cm->SetSelected(limits_vs_1000cm);

   limits_vs_1000cm->SaveAs("limitsCrossSectionVsMass_1000cm_wTheoryErrors.pdf");

}
