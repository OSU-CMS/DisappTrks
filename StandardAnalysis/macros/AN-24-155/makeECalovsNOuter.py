from array import *
import CMS_lumi

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)
gStyle.SetPalette(112)

# data_condor_dir = "/abyss/users/mcarrigan/MET_2022/MET_2022EFG_basicSelection"
# mc_condor_dir = "/data/users/borzari/condor/SignalMC/Run3/2022/metNoMuvsLeadJetPt"

data_condor_dir = "/data/users/borzari/condor/BGData/Run3/2022/eCalovsNOuter"
mc_condor_dir = "/data/users/borzari/condor/SignalMC/Run3/2022/eCalovsNOuter"

dataHist = getHist('hist_merged_ECaloVSNOuter_Electron_2022F',data_condor_dir,'ElectronTagPt55NLayers6plusPlotter','Track Plots/trackFitPlaneWithCaloJet',False)
dataHist.Scale(1/dataHist.Integral())
mcHist = getHist('hist_IsoTrkSelectionNLayers6plus_2025_02_07_14h38m26s',mc_condor_dir,'IsoTrkSelectionNLayers6plusPlotter','Track Plots/trackFitPlaneWithCaloJet',False)
mcHist.Scale(1/mcHist.Integral())

dataHist.RebinY(2)
mcHist.RebinY(2)

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.14
iPeriod = 136

CanvasData = TCanvas("CanvasData","CanvasData",50,50,CMS_lumi.W,CMS_lumi.H)
CanvasData.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
CanvasData.SetRightMargin( 0.13 + CMS_lumi.R/CMS_lumi.W )
CanvasData.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
CanvasData.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Legend = TLegend(0.48,0.76,0.78,0.86)
Legend.SetBorderSize(0)
Legend.SetFillColor(0)
Legend.SetFillStyle(0)
Legend.SetTextSize(0.03)
Legend.SetTextFont(42)
Legend.AddEntry(dataHist,"2022F EGamma data","")
Legend.AddEntry(mcHist,"AMSB #tilde{#chi}^{#pm} (100 cm)","L")

mcHist.SetLineColor(2)
mcHist.SetLineWidth(2)

CanvasData.cd()
# CanvasData.SetLogz()
dataHist.GetYaxis().SetTitle("E_{calo} [GeV]")
dataHist.GetZaxis().SetTitle("Number of tracks (arb. norm.)")
dataHist.GetZaxis().SetTitleOffset(1.8)
dataHist.SetTitle("")
dataHist.Draw("COLZ")
mcHist.Draw("SAME,BOX")
Legend.Draw()

CMS_lumi.CMS_lumi(CanvasData, iPeriod, iPos)
CanvasData.Update()
CanvasData.Print("caloEnergyVsMissingOuterHits_electronControlRegion_NLayers6plus_100cm_2022.pdf")