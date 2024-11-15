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

inputFile = TFile("../../data/triggerEfficiencies_disappTrks_run3.root")

mc2022 = inputFile.Get("WJetsToLNu_2022/grandOr")
mc2023 = inputFile.Get("WJetsToLNu_2023/grandOr")

data2022 = inputFile.Get("Muon_2022/grandOr")
data2023 = inputFile.Get("Muon_2023/grandOr")

data2022.SetMarkerStyle(20)
data2022.SetLineColor(1)
data2022.SetMarkerColor(1)

mc2022.SetMarkerStyle(20)
mc2022.SetLineColor(4)
mc2022.SetMarkerColor(4)

data2023.SetMarkerStyle(20)
data2023.SetLineColor(1)
data2023.SetMarkerColor(1)

mc2023.SetMarkerStyle(20)
mc2023.SetLineColor(4)
mc2023.SetMarkerColor(4)

Legend2022 = TLegend(0.7,0.75,0.9,0.85)
Legend2022.SetBorderSize(0)
Legend2022.SetFillColor(0)
Legend2022.SetFillStyle(0)
Legend2022.SetTextSize(0.03)
Legend2022.AddEntry(data2022,"2022 data","P")
Legend2022.AddEntry(mc2022,"W #rightarrow l#nu MC","P")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 136

Canvas2022 = TCanvas("Canvas2022","Canvas2022",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2022.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2022.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2022.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2022.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas2022.cd()
Canvas2022.SetLogx()
data2022.SetTitle("")
data2022.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
data2022.GetYaxis().SetTitle("Trigger Efficiency")
data2022.GetYaxis().SetTitleOffset(1.4)
data2022.GetXaxis().SetLimits(9,1000)
data2022.GetYaxis().SetRangeUser(0.0,1.4)
data2022.Draw()
mc2022.Draw("SAME,P,L")
Legend2022.Draw()

CMS_lumi.CMS_lumi(Canvas2022, iPeriod, iPos)
Canvas2022.Update()
Canvas2022.Print("TrigEff2022.pdf")

Legend2023 = TLegend(0.7,0.75,0.9,0.85)
Legend2023.SetBorderSize(0)
Legend2023.SetFillColor(0)
Legend2023.SetFillStyle(0)
Legend2023.SetTextSize(0.03)
Legend2023.AddEntry(data2023,"2023 data","P")
Legend2023.AddEntry(mc2023,"W #rightarrow l#nu MC","P")

Canvas2023 = TCanvas("Canvas2023","Canvas2023",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2023.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2023.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2023.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2023.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas2023.cd()
Canvas2023.SetLogx()
data2023.SetTitle("")
data2023.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
data2023.GetYaxis().SetTitle("Trigger Efficiency")
data2023.GetYaxis().SetTitleOffset(1.4)
data2023.GetXaxis().SetLimits(9,1000)
data2023.GetYaxis().SetRangeUser(0.0,1.4)
data2023.Draw()
mc2023.Draw("SAME,P,L")
Legend2023.Draw()

CMS_lumi.CMS_lumi(Canvas2023, iPeriod, iPos)
Canvas2023.Update()
Canvas2023.Print("TrigEff2023.pdf")

