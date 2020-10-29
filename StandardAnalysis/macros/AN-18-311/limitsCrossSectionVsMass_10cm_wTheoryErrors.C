void limitsCrossSectionVsMass_10cm_wTheoryErrors()
{
//=========Macro generated from canvas: limits_vs_10cm/
//=========  (Wed Feb 12 12:53:25 2020) by ROOT version 6.14/06
   TCanvas *limits_vs_10cm = new TCanvas("limits_vs_10cm", "",797,175,800,719);
   limits_vs_10cm->SetHighLightColor(2);
   limits_vs_10cm->Range(-74.51404,-3.851908,1142.848,3.476336);
   limits_vs_10cm->SetFillColor(0);
   limits_vs_10cm->SetBorderMode(0);
   limits_vs_10cm->SetBorderSize(2);
   limits_vs_10cm->SetLogy();
   limits_vs_10cm->SetTickx(1);
   limits_vs_10cm->SetTicky(1);
   limits_vs_10cm->SetLeftMargin(0.1425);
   limits_vs_10cm->SetRightMargin(0.035);
   limits_vs_10cm->SetTopMargin(0.065);
   limits_vs_10cm->SetBottomMargin(0.11625);
   limits_vs_10cm->SetFrameFillStyle(0);
   limits_vs_10cm->SetFrameBorderMode(0);
   limits_vs_10cm->SetFrameFillStyle(0);
   limits_vs_10cm->SetFrameBorderMode(0);
   
   TH1F *hBackground__3__1__1 = new TH1F("hBackground__3__1__1","hBackground",1000,90,1210);
   hBackground__3__1__1->SetMinimum(0.001);
   hBackground__3__1__1->SetMaximum(1000);
   hBackground__3__1__1->SetDirectory(0);
   hBackground__3__1__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hBackground__3__1__1->SetLineColor(ci);
   hBackground__3__1__1->SetLineStyle(0);
   hBackground__3__1__1->SetMarkerStyle(20);
   hBackground__3__1__1->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground__3__1__1->GetXaxis()->SetRange(9,902);
   hBackground__3__1__1->GetXaxis()->SetNdivisions(505);
   hBackground__3__1__1->GetXaxis()->SetLabelFont(42);
   hBackground__3__1__1->GetXaxis()->SetLabelSize(0.055);
   hBackground__3__1__1->GetXaxis()->SetTitleSize(0.045);
   hBackground__3__1__1->GetXaxis()->SetTitleOffset(1.15);
   hBackground__3__1__1->GetXaxis()->SetTitleFont(42);
   hBackground__3__1__1->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground__3__1__1->GetYaxis()->SetNdivisions(505);
   hBackground__3__1__1->GetYaxis()->SetLabelFont(42);
   hBackground__3__1__1->GetYaxis()->SetLabelSize(0.055);
   hBackground__3__1__1->GetYaxis()->SetTitleSize(0.045);
   hBackground__3__1__1->GetYaxis()->SetTitleOffset(1.5);
   hBackground__3__1__1->GetYaxis()->SetTitleFont(42);
   hBackground__3__1__1->GetZaxis()->SetNdivisions(509);
   hBackground__3__1__1->GetZaxis()->SetLabelFont(42);
   hBackground__3__1__1->GetZaxis()->SetLabelOffset(0.007);
   hBackground__3__1__1->GetZaxis()->SetLabelSize(0.045);
   hBackground__3__1__1->GetZaxis()->SetTitleSize(0.06);
   hBackground__3__1__1->GetZaxis()->SetTitleFont(42);
   hBackground__3__1__1->Draw("axis");
   
   Double_t limits_vs_10cm_graph_twoSigma_fx3001[11] = {
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
   Double_t limits_vs_10cm_graph_twoSigma_fy3001[11] = {
   0.03901611,
   0.02993133,
   0.02589355,
   0.02103579,
   0.02638711,
   0.0262075,
   0.02815764,
   0.02921697,
   0.02908516,
   0.03171902,
   0.03080127};
   Double_t limits_vs_10cm_graph_twoSigma_felx3001[11] = {
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
   Double_t limits_vs_10cm_graph_twoSigma_fely3001[11] = {
   0.01889843,
   0.01426415,
   0.01223875,
   0.01027138,
   0.01247203,
   0.01248951,
   0.01330888,
   0.01403784,
   0.0138609,
   0.01524,
   0.01479905};
   Double_t limits_vs_10cm_graph_twoSigma_fehx3001[11] = {
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
   Double_t limits_vs_10cm_graph_twoSigma_fehy3001[11] = {
   0.04127898,
   0.02979799,
   0.02538592,
   0.02230791,
   0.02539813,
   0.02687995,
   0.02753153,
   0.03040382,
   0.02975763,
   0.03422393,
   0.03277809};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(11,limits_vs_10cm_graph_twoSigma_fx3001,limits_vs_10cm_graph_twoSigma_fy3001,limits_vs_10cm_graph_twoSigma_felx3001,limits_vs_10cm_graph_twoSigma_fehx3001,limits_vs_10cm_graph_twoSigma_fely3001,limits_vs_10cm_graph_twoSigma_fehy3001);
   grae->SetName("limits_vs_10cm_graph_twoSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#ffcc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#ffcc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#ffcc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001 = new TH1F("Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetMinimum(0.003811339);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetMaximum(0.08724816);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_10cm_graph_twoSigma300130013001);
   
   grae->Draw("3");
   
   Double_t limits_vs_10cm_graph_oneSigma_fx3002[11] = {
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
   Double_t limits_vs_10cm_graph_oneSigma_fy3002[11] = {
   0.03901611,
   0.02993133,
   0.02589355,
   0.02103579,
   0.02638711,
   0.0262075,
   0.02815764,
   0.02921697,
   0.02908516,
   0.03171902,
   0.03080127};
   Double_t limits_vs_10cm_graph_oneSigma_felx3002[11] = {
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
   Double_t limits_vs_10cm_graph_oneSigma_fely3002[11] = {
   0.01166387,
   0.008803654,
   0.007553603,
   0.006419613,
   0.007697582,
   0.007708371,
   0.008214077,
   0.008773651,
   0.008554772,
   0.009405936,
   0.009249404};
   Double_t limits_vs_10cm_graph_oneSigma_fehx3002[11] = {
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
   Double_t limits_vs_10cm_graph_oneSigma_fehy3002[11] = {
   0.01788479,
   0.01312383,
   0.0112502,
   0.009726548,
   0.01125428,
   0.01169999,
   0.01212166,
   0.01315999,
   0.01286875,
   0.01466627,
   0.01411914};
   grae = new TGraphAsymmErrors(11,limits_vs_10cm_graph_oneSigma_fx3002,limits_vs_10cm_graph_oneSigma_fy3002,limits_vs_10cm_graph_oneSigma_felx3002,limits_vs_10cm_graph_oneSigma_fehx3002,limits_vs_10cm_graph_oneSigma_fely3002,limits_vs_10cm_graph_oneSigma_fehy3002);
   grae->SetName("limits_vs_10cm_graph_oneSigma");
   grae->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   grae->SetFillColor(ci);
   grae->SetFillStyle(1000);

   ci = TColor::GetColor("#00cc00");
   grae->SetLineColor(ci);

   ci = TColor::GetColor("#00cc00");
   grae->SetMarkerColor(ci);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002 = new TH1F("Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetMinimum(0.0103877);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetMaximum(0.06112936);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_Graph_limits_vs_10cm_graph_oneSigma300230023002);
   
   grae->Draw("3");
   
   Double_t limits_vs_10cm_graph_expected_fx1[11] = {
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
   Double_t limits_vs_10cm_graph_expected_fy1[11] = {
   0.03901611,
   0.02993133,
   0.02589355,
   0.02103579,
   0.02638711,
   0.0262075,
   0.02815764,
   0.02921697,
   0.02908516,
   0.03171902,
   0.03080127};
   TGraph *graph = new TGraph(11,limits_vs_10cm_graph_expected_fx1,limits_vs_10cm_graph_expected_fy1);
   graph->SetName("limits_vs_10cm_graph_expected");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_10cm_graph_expected511 = new TH1F("Graph_Graph_Graph_limits_vs_10cm_graph_expected511","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetMinimum(0.01923776);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetMaximum(0.04081414);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_expected511->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_10cm_graph_expected511);
   
   graph->Draw("l");
   
   Double_t limits_vs_10cm_graph_observed_fx2[11] = {
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
   Double_t limits_vs_10cm_graph_observed_fy2[11] = {
   0.04247753,
   0.03735961,
   0.0326169,
   0.02677417,
   0.03401935,
   0.03470671,
   0.03461064,
   0.03813037,
   0.03893537,
   0.04258732,
   0.04070602};
   graph = new TGraph(11,limits_vs_10cm_graph_observed_fx2,limits_vs_10cm_graph_observed_fy2);
   graph->SetName("limits_vs_10cm_graph_observed");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(5);
   graph->SetMarkerStyle(21);
   
   TH1F *Graph_Graph_Graph_limits_vs_10cm_graph_observed622 = new TH1F("Graph_Graph_Graph_limits_vs_10cm_graph_observed622","Graph",100,0,1200);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetMinimum(0.02519285);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetMaximum(0.04416864);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetDirectory(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetLineColor(ci);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetLineStyle(0);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->SetMarkerStyle(20);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetTitleOffset(1.1);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetTitleOffset(1.23);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetZaxis()->SetNdivisions(509);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetZaxis()->SetLabelSize(0.045);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph_limits_vs_10cm_graph_observed622->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_limits_vs_10cm_graph_observed622);
   
   graph->Draw("l");
   
   Double_t limits_vs_10cm_graph_theory_fx3[11] = {
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
   Double_t limits_vs_10cm_graph_theory_fy3[11] = {
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
   	graphTheory->SetPoint(i, limits_vs_10cm_graph_theory_fx3[i], limits_vs_10cm_graph_theory_fy3[i]);
   	graphTheory->SetPointError(i, 0.0, limits_vs_10cm_graph_theory_fy3[i] * theoryUnc[i]);
   }

   graphTheory->SetName("limits_vs_10cm_graph_theory");
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

   //TLegend *leg = new TLegend(0.5877193,0.7291066,0.9461153,0.8731988,NULL,"brNDC");
   //TLegend *leg = new TLegend(0.55, 0.65, 0.95, 0.85, NULL, "brNDC");
   TLegend *leg = new TLegend(0.537594, 0.667147, 0.938596, 0.865994, NULL, "brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.0361757);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("limits_vs_10cm_graph_twoSigma","95% expected","F");

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
   entry=leg->AddEntry("limits_vs_10cm_graph_oneSigma","68% expected","F");

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
   entry=leg->AddEntry("limits_vs_10cm_graph_expected","Median expected","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_10cm_graph_observed","Observed","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(5);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("limits_vs_10cm_graph_theory","NLO+NLL theory (#pm1#sigma)","FL");
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
   
   pl = new TPaveLabel(0.2894737,0.8126801,0.4373434,0.9149856,"CMS","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(12);
   pl->SetTextSize(0.448718);
   pl->Draw();
   
   pl = new TPaveLabel(0.14787,0.726098,0.531328,0.776486,"c#tau_{#tilde{#chi}^{#pm}_{1}} = 10 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = 0.33 ns)","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextFont(42);
   //pl->SetTextSize(0.517241);
   pl->SetTextSize(0.7);
   pl->Draw();
   
   pl = new TPaveLabel(0.01378446,0.7694524,0.4273183,0.8386167,"Wino-like #tilde{#chi}_{0}","brNDC");
   pl->SetBorderSize(0);
   pl->SetFillColor(0);
   pl->SetFillStyle(0);
   pl->SetTextAlign(32);
   pl->SetTextFont(42);
   pl->SetTextSize(0.517241);
   pl->Draw();
   
   TH1F *hBackground_copy__4__2__2 = new TH1F("hBackground_copy__4__2__2","hBackground",1000,90,1210);
   hBackground_copy__4__2__2->SetMinimum(0.001);
   hBackground_copy__4__2__2->SetMaximum(1000);
   hBackground_copy__4__2__2->SetDirectory(0);
   hBackground_copy__4__2__2->SetStats(0);

   ci = TColor::GetColor("#000099");
   hBackground_copy__4__2__2->SetLineColor(ci);
   hBackground_copy__4__2__2->SetLineStyle(0);
   hBackground_copy__4__2__2->SetMarkerStyle(20);
   hBackground_copy__4__2__2->GetXaxis()->SetTitle("m_{#tilde{#chi}^{#pm}_{1}} [GeV]");
   hBackground_copy__4__2__2->GetXaxis()->SetRange(9,902);
   hBackground_copy__4__2__2->GetXaxis()->SetNdivisions(505);
   hBackground_copy__4__2__2->GetXaxis()->SetLabelFont(42);
   hBackground_copy__4__2__2->GetXaxis()->SetLabelSize(0.035);
   hBackground_copy__4__2__2->GetXaxis()->SetTitleSize(0.035);
   hBackground_copy__4__2__2->GetXaxis()->SetTitleOffset(1.25);
   hBackground_copy__4__2__2->GetXaxis()->SetTitleFont(42);
   hBackground_copy__4__2__2->GetYaxis()->SetTitle("#sigma (#tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1}) #it{B} [pb]");
   hBackground_copy__4__2__2->GetYaxis()->SetNdivisions(505);
   hBackground_copy__4__2__2->GetYaxis()->SetLabelFont(42);
   hBackground_copy__4__2__2->GetYaxis()->SetLabelSize(0.035);
   hBackground_copy__4__2__2->GetYaxis()->SetTitleSize(0.035);
   hBackground_copy__4__2__2->GetYaxis()->SetTitleOffset(1.25);
   hBackground_copy__4__2__2->GetYaxis()->SetTitleFont(42);
   hBackground_copy__4__2__2->GetZaxis()->SetNdivisions(509);
   hBackground_copy__4__2__2->GetZaxis()->SetLabelFont(42);
   hBackground_copy__4__2__2->GetZaxis()->SetLabelOffset(0.007);
   hBackground_copy__4__2__2->GetZaxis()->SetLabelSize(0.045);
   hBackground_copy__4__2__2->GetZaxis()->SetTitleSize(0.06);
   hBackground_copy__4__2__2->GetZaxis()->SetTitleFont(42);
   hBackground_copy__4__2__2->Draw("sameaxig");
   limits_vs_10cm->Modified();
   limits_vs_10cm->cd();
   limits_vs_10cm->SetSelected(limits_vs_10cm);

   limits_vs_10cm->SaveAs("limitsCrossSectionVsMass_10cm_wTheoryErrors.pdf");

}
