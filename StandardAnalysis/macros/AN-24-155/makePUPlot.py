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

inputFile = TFile("../../data/pu_disappTrks_run3.root")

mc2022 = inputFile.Get("mc2022_22Sep2023")
mc2022.Scale(1.0/mc2022.Integral())
mc2023 = inputFile.Get("mc2023_22Sep2023")
mc2023.Scale(1.0/mc2023.Integral())

data2022 = inputFile.Get("data2022")
data2022.Scale(1.0/data2022.Integral())
data2023 = inputFile.Get("data2023")
data2023.Scale(1.0/data2023.Integral())

data2022.SetMarkerStyle(20)
data2022.SetLineColor(1)
data2022.SetMarkerColor(1)

mc2022.SetLineColor(1)
mc2022.SetLineWidth(2)

data2023.SetMarkerStyle(20)
data2023.SetLineColor(1)
data2023.SetMarkerColor(1)

mc2023.SetLineColor(1)
mc2023.SetLineWidth(2)

Legend2022 = TLegend(0.7,0.75,0.9,0.85)
Legend2022.SetBorderSize(0)
Legend2022.SetFillColor(0)
Legend2022.SetFillStyle(0)
Legend2022.SetTextSize(0.03)
Legend2022.AddEntry(data2022,"2022 data","P")
Legend2022.AddEntry(mc2022,"2022 MC","L")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
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
data2022.SetTitle("")
data2022.GetXaxis().SetTitle("Number of interactions")
data2022.GetYaxis().SetTitle("Number of events [arb. norm.]")
data2022.GetYaxis().SetTitleOffset(1.8)
data2022.Draw("P")
mc2022.Draw("SAME,HIST")
Legend2022.Draw()

CMS_lumi.CMS_lumi(Canvas2022, iPeriod, iPos)
Canvas2022.Update()
Canvas2022.Print("PU2022.pdf")

Legend2023 = TLegend(0.7,0.75,0.9,0.85)
Legend2023.SetBorderSize(0)
Legend2023.SetFillColor(0)
Legend2023.SetFillStyle(0)
Legend2023.SetTextSize(0.03)
Legend2023.AddEntry(data2023,"2023 data","P")
Legend2023.AddEntry(mc2023,"2023 MC","L")

Canvas2023 = TCanvas("Canvas2023","Canvas2023",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2023.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2023.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2023.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2023.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas2023.cd()
data2023.SetTitle("")
data2023.GetXaxis().SetTitle("Number of interactions")
data2023.GetYaxis().SetTitle("Number of events [arb. norm.]")
data2023.GetYaxis().SetTitleOffset(1.8)
data2023.Draw("P")
mc2023.Draw("SAME,HIST")
Legend2023.Draw()

CMS_lumi.CMS_lumi(Canvas2023, iPeriod, iPos)
Canvas2023.Update()
Canvas2023.Print("PU2023.pdf")

