from array import *
import CMS_lumi

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

inputFile = TFile("/data/users/borzari/condor/BGMC/Run3/2022/fakeTrackGaussPlot/fakeClosureTest_NLayers4.root")

simulated = inputFile.Get("d0;1")
fit = inputFile.Get("d0_fit;1")

simulated.SetLineColor(1)
simulated.SetLineWidth(2)
simulated.SetMarkerColor(1)
simulated.SetMarkerStyle(20)

fit.SetLineColor(2)
fit.SetLineWidth(2)

Legend2022 = TLegend(0.18,0.8,0.38,0.9)
Legend2022.SetBorderSize(0)
Legend2022.SetFillColor(0)
Legend2022.SetFillStyle(0)
Legend2022.SetTextSize(0.03)
Legend2022.AddEntry(simulated,"Simulated background","P")
Legend2022.AddEntry(fit,"Gaussian fit","L")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas2022 = TCanvas("Canvas2022","Canvas2022",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2022.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2022.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2022.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2022.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas2022.cd()
simulated.SetTitle("")
simulated.GetXaxis().SetTitle("track d_{0} [cm]")
simulated.GetYaxis().SetTitle("Entries / 0.05 cm")
simulated.GetYaxis().SetTitleOffset(1.4)
simulated.SetMinimum(0.0)
simulated.SetMaximum(50.0)
simulated.Draw("P")
fit.Draw("SAME")
Legend2022.Draw()

CMS_lumi.CMS_lumi(Canvas2022, iPeriod, iPos)
Canvas2022.Update()
Canvas2022.Print("fakeTrackClosureTestFit2022.pdf")
