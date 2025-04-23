import os
import CMS_lumi
from OSUT3Analysis.Configuration.histogramUtilities import *
from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

def modHist(hist, color, style, norm, histLineWidth):

  hist.LabelsDeflate()
  hist.LabelsOption("v")

  hist.Rebin(5)

  hist.GetXaxis().SetLabelSize(0.023)
  hist.GetYaxis().SetLabelSize(0.023)
  hist.GetYaxis().SetTitleSize(0.023)

  hist.SetLineColor(color)
  hist.SetLineStyle(style)

  hist.SetMarkerColor(color)
  hist.SetMarkerStyle(20)
  hist.SetMarkerSize(1.5)

  hist.SetLineWidth(histLineWidth)
  hist.SetTitle("")

  return hist

gStyle.SetPadLeftMargin(0.065)
gStyle.SetPadRightMargin(0.005)
gStyle.SetPadTopMargin(0.1)
gStyle.SetPadBottomMargin(0.560)

mc_condor_dir = '/data/users/borzari/condor/SignalMC/Run3/2022/triggerSFPlots'

hist100without = getHist('hist_merged_AMSB_100GeV_10000cm_withoutSFTriggerOnlyPlots',mc_condor_dir,'VertexCutOnlyPlotter','Met Plots/metNoMu',False)
hist100with = getHist('hist_merged_AMSB_100GeV_10000cm_withSFTriggerOnlyPlots',mc_condor_dir,'VertexCutOnlyPlotter','Met Plots/metNoMu',False)

hist100without = modHist(hist100without, 4, 2, True, 2)
hist100with = modHist(hist100with, 4, 1, True, 2)

Canvas100 = TCanvas("Canvas100","Canvas100",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas100.SetLeftMargin(CMS_lumi.L/CMS_lumi.W )
Canvas100.SetRightMargin(CMS_lumi.R/CMS_lumi.W )
Canvas100.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas100.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

legend100 = TLegend(0.52, 0.74, 0.73, 0.89)
legend100.SetLineWidth(0)
legend100.SetTextSize(0.03)
legend100.SetHeader('AMSB 100 GeV (c#tau = 10000cm)')
legend100.AddEntry(hist100without,'Without trigger scale factors','l')
legend100.AddEntry(hist100with,'With trigger scale factors','l')

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas100.cd()
hist100without.GetYaxis().SetTitle("Entries / 25 GeV (arb. norm.)")
hist100without.GetXaxis().SetLabelSize(0.033)
hist100without.GetYaxis().SetLabelSize(0.033)
hist100without.GetYaxis().SetTitleSize(0.033)
hist100without.GetXaxis().SetRangeUser(100,500)
hist100without.GetYaxis().SetRangeUser(10,2500)
hist100without.Draw('hist')
hist100with.Draw('hist,same')
legend100.Draw()
CMS_lumi.CMS_lumi(Canvas100, iPeriod, iPos)
Canvas100.Update()
Canvas100.Print("triggerScaleFactorComparison_100_2022.pdf")

hist700without = getHist('hist_merged_AMSB_700GeV_10000cm_withoutSFTriggerOnlyPlots',mc_condor_dir,'VertexCutOnlyPlotter','Met Plots/metNoMu',False)
hist700with = getHist('hist_merged_AMSB_700GeV_10000cm_withSFTriggerOnlyPlots',mc_condor_dir,'VertexCutOnlyPlotter','Met Plots/metNoMu',False)

hist700without = modHist(hist700without, 2, 2, True, 2)
hist700with = modHist(hist700with, 2, 1, True, 2)

Canvas700 = TCanvas("Canvas700","Canvas700",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas700.SetLeftMargin(CMS_lumi.L/CMS_lumi.W )
Canvas700.SetRightMargin(CMS_lumi.R/CMS_lumi.W )
Canvas700.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas700.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

legend700 = TLegend(0.52, 0.74, 0.73, 0.89)
legend700.SetLineWidth(0)
legend700.SetTextSize(0.03)
legend700.SetHeader('AMSB 700 GeV (c#tau = 10000cm)')
legend700.AddEntry(hist700without,'Without trigger scale factors','l')
legend700.AddEntry(hist700with,'With trigger scale factors','l')

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas700.cd()
hist700without.GetYaxis().SetTitle("Entries / 25 GeV (arb. norm.)")
hist700without.GetXaxis().SetLabelSize(0.033)
hist700without.GetYaxis().SetLabelSize(0.033)
hist700without.GetYaxis().SetTitleSize(0.033)
hist700without.GetXaxis().SetRangeUser(100,500)
hist700without.GetYaxis().SetRangeUser(10,6000)
hist700without.Draw('hist')
hist700with.Draw('hist,same')
legend700.Draw()
CMS_lumi.CMS_lumi(Canvas700, iPeriod, iPos)
Canvas700.Update()
Canvas700.Print("triggerScaleFactorComparison_700_2022.pdf")