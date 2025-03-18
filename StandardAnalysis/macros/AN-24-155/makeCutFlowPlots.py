import os
import CMS_lumi
from OSUT3Analysis.Configuration.histogramUtilities import *
from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)
gStyle.SetPadGridX(1)

def modHist(hist, color, norm, histLineWidth):

  hist.LabelsDeflate()
  hist.LabelsOption("v")

  hist.GetXaxis().SetLabelSize(0.023)
  hist.GetYaxis().SetLabelSize(0.023)
  hist.GetYaxis().SetTitleSize(0.023)

  hist.SetLineColor(color)

  hist.SetMarkerColor(color)
  hist.SetMarkerStyle(20)
  hist.SetMarkerSize(1.5)

  hist.SetLineWidth(histLineWidth)
  hist.SetTitle("")

  if (norm == True):
    scale = 1 / hist.GetBinContent(1)
    hist.Scale(scale)

  return hist

gStyle.SetPadLeftMargin(0.065)
gStyle.SetPadRightMargin(0.005)
gStyle.SetPadTopMargin(0.1)
gStyle.SetPadBottomMargin(0.560)

mc_condor_dir = '/data/users/borzari/condor/SignalMC/Run3/2022/signalAcceptance_sigCentralLooseNoMissOut_v2'

cutflow70010 = getHist('AMSB_chargino_700GeV_10cm_130X',mc_condor_dir,'disTrkSelectionSmearedJetsNLayers6plusCutFlowPlotter','cutFlow',False)
cutflow700100 = getHist('AMSB_chargino_700GeV_100cm_130X',mc_condor_dir,'disTrkSelectionSmearedJetsNLayers6plusCutFlowPlotter','cutFlow',False)
cutflow7001000 = getHist('AMSB_chargino_700GeV_1000cm_130X',mc_condor_dir,'disTrkSelectionSmearedJetsNLayers6plusCutFlowPlotter','cutFlow',False)

cutflow70010 = modHist(cutflow70010, 2, True, 2)
cutflow700100 = modHist(cutflow700100, 3, True, 2)
cutflow7001000 = modHist(cutflow7001000, 4, True, 2)

c = TCanvas('', '', 2200, 1200)

legend = TLegend(0.77, 0.74, 0.98, 0.89)
legend.SetLineWidth(1)
legend.SetTextSize(0.03)
legend.SetHeader('AMSB chargino (700 GeV)')
legend.AddEntry(cutflow70010,'c#tau = 10 cm','lp')
legend.AddEntry(cutflow700100,'c#tau = 100 cm','lp')
legend.AddEntry(cutflow7001000,'c#tau = 1000 cm','lp')

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.07
iPeriod = 0

c.cd()
c.SetLogy()
cutflow70010.GetYaxis().SetTitle("Cumulative efficiency")
cutflow70010.GetYaxis().SetTitleOffset(0.9)
cutflow70010.GetYaxis().SetLabelSize(0.033)
cutflow70010.GetYaxis().SetTitleSize(0.033)
cutflow70010.SetMinimum(4e-4)
cutflow70010.SetMaximum(5.0)
cutflow70010.Draw('p')
cutflow700100.Draw('p,same')
cutflow7001000.Draw('p,same')
legend.Draw()
CMS_lumi.CMS_lumi(c, iPeriod, iPos)
c.Update()
c.Print("signalCutFlow2022.pdf")