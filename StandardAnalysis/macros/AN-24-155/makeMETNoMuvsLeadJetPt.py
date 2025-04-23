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

data_condor_dir = "/data/users/borzari/condor/Data/Run3/2022/MET_2022F_BasicSelPlots"
mc_condor_dir = "/data/users/borzari/condor/SignalMC/Run3/2022/metNoMuvsLeadJetPt"

dataHist = getHist('hist_merged_MET_2022F_BasicSelPlots',data_condor_dir,'metMinimalSkimPlotter','Jet-met Plots/leadJetPtVsMetNoMu',False)
mcHist = getHist('AMSB_Wino_700GeV_10000cm_metNoMuvsLeadJetPt',mc_condor_dir,'metMinimalSkimPlotter','Jet-met Plots/leadJetPtVsMetNoMu',False)

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.14
iPeriod = 136

CanvasData = TCanvas("CanvasData","CanvasData",50,50,CMS_lumi.W,CMS_lumi.H)
CanvasData.SetLeftMargin( 0.02 + CMS_lumi.L/CMS_lumi.W )
CanvasData.SetRightMargin( 0.11 + CMS_lumi.R/CMS_lumi.W )
CanvasData.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
CanvasData.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

CanvasData.cd()
dataHist.GetXaxis().SetRangeUser(120,1200)
dataHist.GetYaxis().SetRangeUser(50,1000)
dataHist.SetTitle("")
dataHist.Draw("COLZ")

Line = TLine(120, 110, 1200, 110)
Line.SetLineStyle(7)
Line.SetLineWidth(2)
Line.SetLineColor(2)
Line.Draw()

CMS_lumi.CMS_lumi(CanvasData, iPeriod, iPos)
CanvasData.Update()
CanvasData.Print("jetPtVsMET_data.pdf")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

CanvasSignal = TCanvas("CanvasSignal","CanvasSignal",50,50,CMS_lumi.W,CMS_lumi.H)
CanvasSignal.SetLeftMargin( 0.02 + CMS_lumi.L/CMS_lumi.W )
CanvasSignal.SetRightMargin( 0.05 + CMS_lumi.R/CMS_lumi.W )
CanvasSignal.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
CanvasSignal.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

CanvasSignal.cd()
mcHist.GetXaxis().SetRangeUser(120,1200)
mcHist.GetYaxis().SetRangeUser(50,1000)
mcHist.SetTitle("")
mcHist.Draw("COLZ")
Line.Draw()

CMS_lumi.CMS_lumi(CanvasSignal, iPeriod, iPos)
CanvasSignal.Update()
CanvasSignal.Print("jetPtVsMET_signal.pdf")