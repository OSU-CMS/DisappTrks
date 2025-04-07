from array import *
import CMS_lumi
import math

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

def ratioErrorCalc(val1,val2,err1,err2):
    err = math.sqrt(((1.0/val2)*(1.0/val2)*(err1*err1))+((val1/(val2*val2))*(val1/(val2*val2))*(err2*err2)))
    return err

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

Legend2022 = TLegend(0.65,0.75,0.9,0.85)
Legend2022.SetBorderSize(0)
Legend2022.SetFillColor(0)
Legend2022.SetFillStyle(0)
Legend2022.SetTextSize(0.035)
Legend2022.SetHeader("OR of Signal Paths")
Legend2022.AddEntry(data2022,"2022 data","P")
Legend2022.AddEntry(mc2022,"W #rightarrow l#nu MC","P")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 2022

Canvas2022 = TCanvas("Canvas2022","Canvas2022",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2022.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2022.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2022.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2022.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

line2022 = TLine(9,1.0,1000,1.0)
line2022.SetLineWidth(2)
line2022.SetLineStyle(2)

Canvas2022.cd()
Canvas2022.SetLogx()
data2022.SetTitle("")
data2022.GetXaxis().SetTitle("")
data2022.GetYaxis().SetTitle("Trigger Efficiency")
data2022.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
data2022.GetXaxis().SetTitleOffset(1.4)
data2022.GetYaxis().SetTitleOffset(1.4)
# data2022.GetYaxis().SetTitleSize(0.045)
data2022.GetXaxis().SetLimits(9,1000)
# data2022.GetXaxis().SetLabelSize(0.0)
# data2022.GetYaxis().SetLabelSize(0.045)
data2022.GetYaxis().SetRangeUser(0.0,1.4)
data2022.Draw()
mc2022.Draw("SAME,P,L")
Legend2022.Draw()
line2022.Draw()

CMS_lumi.CMS_lumi(Canvas2022, iPeriod, iPos)
Canvas2022.Update()
Canvas2022.Print("triggerEfficiencyComparison_2022.pdf")

Legend2023 = TLegend(0.65,0.75,0.9,0.85)
Legend2023.SetBorderSize(0)
Legend2023.SetFillColor(0)
Legend2023.SetFillStyle(0)
Legend2023.SetTextSize(0.035)
Legend2023.SetHeader("OR of Signal Paths")
Legend2023.AddEntry(data2023,"2023 data","P")
Legend2023.AddEntry(mc2023,"W #rightarrow l#nu MC","P")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 2023

Canvas2023 = TCanvas("Canvas2023","Canvas2023",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2023.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2023.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2023.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2023.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

line2023 = TLine(9,1.0,1000,1.0)
line2023.SetLineWidth(2)
line2023.SetLineStyle(2)

Canvas2023.cd()
Canvas2023.SetLogx()
data2023.SetTitle("")
data2023.GetXaxis().SetTitle("")
data2023.GetYaxis().SetTitle("Trigger Efficiency")
data2023.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
data2023.GetXaxis().SetTitleOffset(1.4)
data2023.GetYaxis().SetTitleOffset(1.4)
# data2023.GetYaxis().SetTitleSize(0.045)
data2023.GetXaxis().SetLimits(9,1000)
# data2023.GetXaxis().SetLabelSize(0.0)
# data2023.GetYaxis().SetLabelSize(0.045)
data2023.GetYaxis().SetRangeUser(0.0,1.4)
data2023.Draw()
mc2023.Draw("SAME,P,L")
Legend2023.Draw()
line2023.Draw()

CMS_lumi.CMS_lumi(Canvas2023, iPeriod, iPos)
Canvas2023.Update()
Canvas2023.Print("triggerEfficiencyComparison_2023.pdf")