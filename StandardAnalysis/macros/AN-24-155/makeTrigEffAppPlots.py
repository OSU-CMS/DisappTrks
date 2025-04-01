from array import *
import CMS_lumi
import math

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

def modHists(hist2022, hist2023, histmc):

    hist2022.SetMarkerStyle(20)
    hist2022.SetLineColor(1)
    hist2022.SetMarkerColor(1)

    hist2023.SetMarkerStyle(20)
    hist2023.SetLineColor(2)
    hist2023.SetMarkerColor(2)

    histmc.SetMarkerStyle(20)
    histmc.SetLineColor(4)
    histmc.SetMarkerColor(4)

def writeCanvas(hist2022, hist2023, histmc, path, xAxis):

    modHists(hist2022, hist2023, histmc)

    # Change the CMS_lumi variables (see CMS_lumi.py)
    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "Preliminary"
    CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

    # Define position of CMS text and period of lumi to plot
    iPos = 0
    if( iPos==0 ): CMS_lumi.relPosX = 0.12
    iPeriod = 20223

    line = TLine(9,1.0,1000,1.0)
    line.SetLineWidth(2)
    line.SetLineStyle(2)

    canvas = TCanvas("canvas","canvas",50,50,CMS_lumi.W,CMS_lumi.H)
    canvas.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
    canvas.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
    canvas.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
    canvas.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

    legend = TLegend(0.18,0.725,0.43,0.875)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextSize(0.035)
    legend.SetHeader(path)
    legend.AddEntry(hist2022,"2022 data","P")
    legend.AddEntry(hist2023,"2023 data","P")
    legend.AddEntry(histmc,"W #rightarrow l#nu MC","P")

    canvas.cd()
    canvas.SetLogx()
    hist2022.SetTitle("")
    hist2022.GetXaxis().SetTitle("")
    hist2022.GetYaxis().SetTitle("Trigger Efficiency")
    if xAxis == "metNoMu": hist2022.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
    if xAxis == "met": hist2022.GetXaxis().SetTitle("PF E_{T}^{miss} [GeV]")
    if xAxis == "muon": hist2022.GetXaxis().SetTitle("muon p_{T}[GeV]")
    hist2022.GetXaxis().SetTitleOffset(1.4)
    hist2022.GetYaxis().SetTitleOffset(1.4)
    # hist2022.GetYaxis().SetTitleSize(0.045)
    hist2022.GetXaxis().SetLimits(9,1000)
    # hist2022.GetXaxis().SetLabelSize(0.0)
    # hist2022.GetYaxis().SetLabelSize(0.045)
    hist2022.GetYaxis().SetRangeUser(0.0,1.4)
    hist2022.Draw("A,P")
    # hist2023.Draw("SAME,P,L")
    # histmc.Draw("SAME,P,L")
    hist2023.Draw("SAME,P")
    histmc.Draw("SAME,P")
    legend.Draw()
    line.Draw()

    CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
    canvas.Update()
    canvas.Print("triggerEfficiencyComparison_" + path + ".pdf")

inputFile2022 = TFile("/data/users/borzari/condor/BGData/Run3/2022/triggerEffs/log_right_Muon_2022Test.root")
inputFile2023 = TFile("/data/users/borzari/condor/BGData/Run3/2022/triggerEffs/log_right_Muon_2023Test.root")
inputFilemc = TFile("/data/users/borzari/condor/BGMC/Run3/2022/triggerEffs/log_right_WToLNu_Test.root")

hist2022_hltMet105 = inputFile2022.Get("Graph;2")
hist2023_hltMet105 = inputFile2023.Get("Graph;2")
histmc_hltMet105 = inputFilemc.Get("Graph;2")

hist2022_isoTrk50 = inputFile2022.Get("Graph;6")
hist2023_isoTrk50 = inputFile2023.Get("Graph;6")
histmc_isoTrk50 = inputFilemc.Get("Graph;6")

hist2022_HLT_MET105_IsoTrk50 = inputFile2022.Get("Graph;11")
hist2023_HLT_MET105_IsoTrk50 = inputFile2023.Get("Graph;11")
histmc_HLT_MET105_IsoTrk50 = inputFilemc.Get("Graph;11")

hist2022_HLT_MET105_IsoTrk50 = inputFile2022.Get("Graph;11")
hist2023_HLT_MET105_IsoTrk50 = inputFile2023.Get("Graph;11")
histmc_HLT_MET105_IsoTrk50 = inputFilemc.Get("Graph;11")

hist2022_HLT_MET120_IsoTrk50 = inputFile2022.Get("Graph;12")
hist2023_HLT_MET120_IsoTrk50 = inputFile2023.Get("Graph;12")
histmc_HLT_MET120_IsoTrk50 = inputFilemc.Get("Graph;12")

hist2022_HLT_PFMET105_IsoTrk50 = inputFile2022.Get("Graph;13")
hist2023_HLT_PFMET105_IsoTrk50 = inputFile2023.Get("Graph;13")
histmc_HLT_PFMET105_IsoTrk50 = inputFilemc.Get("Graph;13")

hist2022_HLT_PFMET120_PFMHT120_IDTight = inputFile2022.Get("Graph;14")
hist2023_HLT_PFMET120_PFMHT120_IDTight = inputFile2023.Get("Graph;14")
histmc_HLT_PFMET120_PFMHT120_IDTight = inputFilemc.Get("Graph;14")

hist2022_HLT_PFMET130_PFMHT130_IDTight = inputFile2022.Get("Graph;15")
hist2023_HLT_PFMET130_PFMHT130_IDTight = inputFile2023.Get("Graph;15")
histmc_HLT_PFMET130_PFMHT130_IDTight = inputFilemc.Get("Graph;15")

hist2022_HLT_PFMET140_PFMHT140_IDTight = inputFile2022.Get("Graph;16")
hist2023_HLT_PFMET140_PFMHT140_IDTight = inputFile2023.Get("Graph;16")
histmc_HLT_PFMET140_PFMHT140_IDTight = inputFilemc.Get("Graph;16")

hist2022_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 = inputFile2022.Get("Graph;17")
hist2023_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 = inputFile2023.Get("Graph;17")
histmc_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 = inputFilemc.Get("Graph;17")

hist2022_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF = inputFile2022.Get("Graph;18")
hist2023_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF = inputFile2023.Get("Graph;18")
histmc_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF = inputFilemc.Get("Graph;18")

hist2022_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF = inputFile2022.Get("Graph;19")
hist2023_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF = inputFile2023.Get("Graph;19")
histmc_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF = inputFilemc.Get("Graph;19")

hist2022_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF = inputFile2022.Get("Graph;20")
hist2023_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF = inputFile2023.Get("Graph;20")
histmc_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF = inputFilemc.Get("Graph;20")

hist2022_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF = inputFile2022.Get("Graph;21")
hist2023_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF = inputFile2023.Get("Graph;21")
histmc_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF = inputFilemc.Get("Graph;21")

hist2022_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight = inputFile2022.Get("Graph;22")
hist2023_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight = inputFile2023.Get("Graph;22")
histmc_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight = inputFilemc.Get("Graph;22")

hist2022_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight = inputFile2022.Get("Graph;23")
hist2023_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight = inputFile2023.Get("Graph;23")
histmc_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight = inputFilemc.Get("Graph;23")

hist2022_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight = inputFile2022.Get("Graph;24")
hist2023_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight = inputFile2023.Get("Graph;24")
histmc_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight = inputFilemc.Get("Graph;24")

hist2022_HLT_PFMET120_PFMHT120_IDTight_PFHT60 = inputFile2022.Get("Graph;25")
hist2023_HLT_PFMET120_PFMHT120_IDTight_PFHT60 = inputFile2023.Get("Graph;25")
histmc_HLT_PFMET120_PFMHT120_IDTight_PFHT60 = inputFilemc.Get("Graph;25")

writeCanvas(hist2022_hltMet105, hist2023_hltMet105, histmc_hltMet105, "hltMet105 filter", "metNoMu")

writeCanvas(hist2022_isoTrk50, hist2023_isoTrk50, histmc_isoTrk50, "HLT_MET105_IsoTrk50, hltMet105 filter applied", "muon")

writeCanvas(hist2022_HLT_MET105_IsoTrk50, hist2023_HLT_MET105_IsoTrk50, histmc_HLT_MET105_IsoTrk50, "HLT_MET105_IsoTrk50", "metNoMu")

writeCanvas(hist2022_HLT_MET120_IsoTrk50, hist2023_HLT_MET120_IsoTrk50, histmc_HLT_MET120_IsoTrk50, "HLT_MET120_IsoTrk50", "metNoMu")

writeCanvas(hist2022_HLT_PFMET105_IsoTrk50, hist2023_HLT_PFMET105_IsoTrk50, histmc_HLT_PFMET105_IsoTrk50, "HLT_PFMET105_IsoTrk50", "met")

writeCanvas(hist2022_HLT_PFMET120_PFMHT120_IDTight, hist2023_HLT_PFMET120_PFMHT120_IDTight, histmc_HLT_PFMET120_PFMHT120_IDTight, "HLT_PFMET120_PFMHT120_IDTight", "met")

writeCanvas(hist2022_HLT_PFMET130_PFMHT130_IDTight, hist2023_HLT_PFMET130_PFMHT130_IDTight, histmc_HLT_PFMET130_PFMHT130_IDTight, "HLT_PFMET130_PFMHT130_IDTight", "met")

writeCanvas(hist2022_HLT_PFMET140_PFMHT140_IDTight, hist2023_HLT_PFMET140_PFMHT140_IDTight, histmc_HLT_PFMET140_PFMHT140_IDTight, "HLT_PFMET140_PFMHT140_IDTight", "met")

writeCanvas(hist2022_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60, hist2023_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60, histmc_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF, hist2023_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF, histmc_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF, "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF, hist2023_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF, histmc_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF, hist2023_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF, histmc_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF, "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF, hist2023_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF, histmc_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF, "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight, hist2023_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight, histmc_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight, hist2023_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight, histmc_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight, "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight", "metNoMu")

writeCanvas(hist2022_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight, hist2023_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight, histmc_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight, "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight", "metNoMu")

writeCanvas(hist2022_HLT_PFMET120_PFMHT120_IDTight_PFHT60, hist2023_HLT_PFMET120_PFMHT120_IDTight_PFHT60, histmc_HLT_PFMET120_PFMHT120_IDTight_PFHT60, "HLT_PFMET120_PFMHT120_IDTight_PFHT60", "met")