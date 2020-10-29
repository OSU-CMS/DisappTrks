void limitsCrossSectionVsMass_10000cm_wTheoryErrors()
{
//=========Macro generated from canvas: limits_vs_10000cm/
//=========  (Wed Feb 12 13:00:48 2020) by ROOT version 6.14/06
   TCanvas *limits_vs_10000cm = new TCanvas("limits_vs_10000cm", "",0,89,800,719);
   limits_vs_10000cm->SetHighLightColor(2);
   limits_vs_10000cm->Range(-74.51404,-3.851908,1142.848,3.476336);
   limits_vs_10000cm->SetFillColor(0);
   limits_vs_10000cm->SetBorderMode(0);
   limits_vs_10000cm->SetBorderSize(2);
   limits_vs_10000cm->SetLogy();
   limits_vs_10000cm->SetTickx(1);
   limits_vs_10000cm->SetTicky(1);
   limits_vs_10000cm->SetLeftMargin(0.1425);
   limits_vs_10000cm->SetRightMargin(0.035);
   limits_vs_10000cm->SetTopMargin(0.065);
   limits_vs_10000cm->SetBottomMargin(0.11625);
   limits_vs_10000cm->SetFrameFillStyle(0);
   limits_vs_10000cm->SetFrameBorderMode(0);
   limits_vs_10000cm->SetFrameFillStyle(0);
   limits_vs_10000cm->SetFrameBorderMode(0);
   
   TH1F *hBackground__9__1__1 = new TH1F("hBackground__9__1__1","hBackground",1000,90,1210);
   hBackground__9__1__1->SetMinimum(0.001);
   hBackground__9__1__1->SetMaximum(1000);
   hBackground__9__1__1->SetDirectory(0);
   hBackground__9__1__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hBackground__9__1__1->SetLineColor(ci);
   hBackground__9__1__1->SetLineStyle(0);
   hBackground__9__1__1->SetMarkerStyle(20);
   hBackground__9__1__1->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground__9__1__1->GetXaxis()->SetRange(9,902);
   hBackground__9__1__1->GetXaxis()->SetNdivisions(505);
   hBackground__9__1__1->GetXaxis()->SetLabelFont(42);
   hBackground__9__1__1->GetXaxis()->SetLabelSize(0.055);
   hBackground__9__1__1->GetXaxis()->SetTitleSize(0.045);
   hBackground__9__1__1->GetXaxis()->SetTitleOffset(1.15);
   hBackground__9__1__1->GetXaxis()->SetTitleFont(42);
   hBackground__9__1__1->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground__9__1__1->GetYaxis()->SetNdivisions(505);
   hBackground__9__1__1->GetYaxis()->SetLabelFont(42);
   hBackground__9__1__1->GetYaxis()->SetLabelSize(0.055);
   hBackground__9__1__1->GetYaxis()->SetTitleSize(0.045);
   hBackground__9__1__1->GetYaxis()->SetTitleOffset(1.5);
   hBackground__9__1__1->GetYaxis()->SetTitleFont(42);
   hBackground__9__1__1->GetZaxis()->SetNdivisions(509);
   hBackground__9__1__1->GetZaxis()->SetLabelFont(42);
   hBackground__9__1__1->GetZaxis()->SetLabelOffset(0.007);
   hBackground__9__1__1->GetZaxis()->SetLabelSize(0.045);
   hBackground__9__1__1->GetZaxis()->SetTitleSize(0.06);
   hBackground__9__1__1->GetZaxis()->SetTitleFont(42);
   hBackground__9__1__1->Draw("axis");
   
   Double_t limits_vs_10000cm_graph_twoSigma_fx3001[11] = {
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
   Double_t limits_vs_10000cm_graph_twoSigma_fy3001[11] = {
   2.253033,
   0.7797097,
   0.3534175,
   0.2074554,
   0.1693428,
   0.1369016,
   0.125842,
   0.1099693,
   0.09167067,
   0.09574245,
   0.08355525};
   Double_t limits_vs_10000cm_graph_twoSigma_felx3001[11] = {
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
   Double_t limits_vs_10000cm_graph_twoSigma_fely3001[11] = {
   1.152919,
   0.3776719,
   0.1684255,
   0.09724471,
   0.08070241,
   0.06631169,
   0.05948001,
   0.05240726,
   0.0436868,
   0.04749723,
   0.04145124};
   Double_t limits_vs_10000cm_graph_twoSigma_fehx3001[11] = {
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
   Double_t limits_vs_10000cm_graph_twoSigma_fehy3001[11] = {
   3.158745,
   0.9029706,
   0.3908805,
   0.2148425,
   0.1783259,
   0.1465342,
   0.1325176,
   0.1174381,
   0.09812076,
   0.1140503,
   0.1005396};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(11,limits_vs_10000cm_graph_twoSigma_fx3001,limits_vs_10000cm_graph_twoSigma_fy3001,limits_vs_10000cm_graph_twoSigma_felx3001,limits_vs_10000cm_graph_twoSigma_fehx3001,limits_vs_10000cm_graph_twoSigma_fely3001,limits_vs_10000cm_graph_twoSigma_fehy3001);
   grae->SetName("limits_vs_10000cm_graph_twoSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#ffcc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#ffcc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#ffcc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001 = new TH1F("Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetMinimum(0.03789361);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetMaximum(5.948746);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_10000cm_graph_twoSigma300730013001);
   
   grae->Draw("3");
   
   Double_t limits_vs_10000cm_graph_oneSigma_fx3002[11] = {
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
   Double_t limits_vs_10000cm_graph_oneSigma_fy3002[11] = {
   2.253033,
   0.7797097,
   0.3534175,
   0.2074554,
   0.1693428,
   0.1369016,
   0.125842,
   0.1099693,
   0.09167067,
   0.09574245,
   0.08355525};
   Double_t limits_vs_10000cm_graph_oneSigma_felx3002[11] = {
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
   Double_t limits_vs_10000cm_graph_oneSigma_fely3002[11] = {
   0.7295816,
   0.2360449,
   0.1052659,
   0.06001822,
   0.04980852,
   0.04092675,
   0.03671032,
   0.03234511,
   0.02730425,
   0.02968577,
   0.02590702};
   Double_t limits_vs_10000cm_graph_oneSigma_fehx3002[11] = {
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
   Double_t limits_vs_10000cm_graph_oneSigma_fehy3002[11] = {
   1.248315,
   0.3760627,
   0.1648223,
   0.09178879,
   0.07627585,
   0.06275498,
   0.05668211,
   0.04997103,
   0.04202137,
   0.04770419,
   0.04163185};
   grae = new TGraphAsymmErrors(11,limits_vs_10000cm_graph_oneSigma_fx3002,limits_vs_10000cm_graph_oneSigma_fy3002,limits_vs_10000cm_graph_oneSigma_felx3002,limits_vs_10000cm_graph_oneSigma_fehx3002,limits_vs_10000cm_graph_oneSigma_fely3002,limits_vs_10000cm_graph_oneSigma_fehy3002);
   grae->SetName("limits_vs_10000cm_graph_oneSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#00cc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#00cc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002 = new TH1F("Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetMinimum(0.0518834);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetMaximum(3.845718);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_10000cm_graph_oneSigma300830023002);
   
   grae->Draw("3");
   
   Double_t limits_vs_10000cm_graph_expected_fx1[11] = {
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
   Double_t limits_vs_10000cm_graph_expected_fy1[11] = {
   2.253033,
   0.7797097,
   0.3534175,
   0.2074554,
   0.1693428,
   0.1369016,
   0.125842,
   0.1099693,
   0.09167067,
   0.09574245,
   0.08355525};
   TGraph *graph = new TGraph(11,limits_vs_10000cm_graph_expected_fx1,limits_vs_10000cm_graph_expected_fy1);
   graph->SetName("limits_vs_10000cm_graph_expected");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411 = new TH1F("Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetMinimum(0.07519973);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetMaximum(2.469981);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_10000cm_graph_expected1411);
   
   graph->Draw("l");
   
   Double_t limits_vs_10000cm_graph_observed_fx2[11] = {
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
   Double_t limits_vs_10000cm_graph_observed_fy2[11] = {
   2.382116,
   0.8582021,
   0.3888921,
   0.2188843,
   0.1772934,
   0.1349663,
   0.1275388,
   0.1170256,
   0.08841014,
   0.08268944,
   0.07041769};
   graph = new TGraph(11,limits_vs_10000cm_graph_observed_fx2,limits_vs_10000cm_graph_observed_fy2);
   graph->SetName("limits_vs_10000cm_graph_observed");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522 = new TH1F("Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetMinimum(0.06337592);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetMaximum(2.613286);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_10000cm_graph_observed1522);
   
   graph->Draw("l");
   
   Double_t limits_vs_10000cm_graph_theory_fx3[11] = {
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
   Double_t limits_vs_10000cm_graph_theory_fy3[11] = {
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
        graphTheory->SetPoint(i, limits_vs_10000cm_graph_theory_fx3[i], limits_vs_10000cm_graph_theory_fy3[i]);
        graphTheory->SetPointError(i, 0.0, limits_vs_10000cm_graph_theory_fy3[i] * theoryUnc[i]);
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
   
   //TLegend *leg = new TLegend(0.5877193,0.7334294,0.9461153,0.8731988,NULL,"brNDC");
   //TLegend *leg = new TLegend(0.55, 0.65, 0.95, 0.85, NULL, "brNDC");
   TLegend *leg = new TLegend(0.537594, 0.667147, 0.938596, 0.865994, NULL, "brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.0361757);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("limits_vs_10000cm_graph_twoSigma","95% expected","F");

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
   entry=leg->AddEntry("limits_vs_10000cm_graph_oneSigma","68% expected","F");

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
   entry=leg->AddEntry("limits_vs_10000cm_graph_expected","Median expected","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_10000cm_graph_observed","Observed","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_10000cm_graph_theory","NLO+NLL theory (#pm1#sigma)","FL");
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
   
   pl = new TPaveLabel(0.2807018,0.8097983,0.4285714,0.9121037,"CMS","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(12);
   pl->SetTextSize(0.448718);
   pl->Draw();
   
   pl = new TPaveLabel(0.14787,0.726098,0.531328,0.776486,"c#tau_{#tilde{#chi}^{#pm}_{1}} = 10000 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = 333 ns)","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextFont(42);
   //pl->SetTextSize(0.517241);
   pl->SetTextSize(0.7);
   pl->Draw();
   
   pl = new TPaveLabel(0.002506266,0.7737752,0.4160401,0.8429395,"Wino-like #tilde{#chi}_{0}","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(32);
   pl->SetTextFont(42);
   pl->SetTextSize(0.517241);
   pl->Draw();
   
   TH1F *hBackground_copy__10__2__2 = new TH1F("hBackground_copy__10__2__2","hBackground",1000,90,1210);
   hBackground_copy__10__2__2->SetMinimum(0.001);
   hBackground_copy__10__2__2->SetMaximum(1000);
   hBackground_copy__10__2__2->SetDirectory(0);
   hBackground_copy__10__2__2->SetStats(0);

   ci = TColor::GetColor("#000099");
   hBackground_copy__10__2__2->SetLineColor(ci);
   hBackground_copy__10__2__2->SetLineStyle(0);
   hBackground_copy__10__2__2->SetMarkerStyle(20);
   hBackground_copy__10__2__2->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground_copy__10__2__2->GetXaxis()->SetRange(9,902);
   hBackground_copy__10__2__2->GetXaxis()->SetNdivisions(505);
   hBackground_copy__10__2__2->GetXaxis()->SetLabelFont(42);
   hBackground_copy__10__2__2->GetXaxis()->SetLabelSize(0.035);
   hBackground_copy__10__2__2->GetXaxis()->SetTitleSize(0.035);
   hBackground_copy__10__2__2->GetXaxis()->SetTitleOffset(1.25);
   hBackground_copy__10__2__2->GetXaxis()->SetTitleFont(42);
   hBackground_copy__10__2__2->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground_copy__10__2__2->GetYaxis()->SetNdivisions(505);
   hBackground_copy__10__2__2->GetYaxis()->SetLabelFont(42);
   hBackground_copy__10__2__2->GetYaxis()->SetLabelSize(0.035);
   hBackground_copy__10__2__2->GetYaxis()->SetTitleSize(0.035);
   hBackground_copy__10__2__2->GetYaxis()->SetTitleOffset(1.25);
   hBackground_copy__10__2__2->GetYaxis()->SetTitleFont(42);
   hBackground_copy__10__2__2->GetZaxis()->SetNdivisions(509);
   hBackground_copy__10__2__2->GetZaxis()->SetLabelFont(42);
   hBackground_copy__10__2__2->GetZaxis()->SetLabelOffset(0.007);
   hBackground_copy__10__2__2->GetZaxis()->SetLabelSize(0.045);
   hBackground_copy__10__2__2->GetZaxis()->SetTitleSize(0.06);
   hBackground_copy__10__2__2->GetZaxis()->SetTitleFont(42);
   hBackground_copy__10__2__2->Draw("sameaxig");
   limits_vs_10000cm->Modified();
   limits_vs_10000cm->cd();
   limits_vs_10000cm->SetSelected(limits_vs_10000cm);

   limits_vs_10000cm->SaveAs("limitsCrossSectionVsMass_10000cm_wTheoryErrors.pdf");

}
