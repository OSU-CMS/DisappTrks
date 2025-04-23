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
data2022Up = inputFile.Get("data2022Up")
data2022Up.Scale(1.0/data2022Up.Integral())
data2022Down = inputFile.Get("data2022Down")
data2022Down.Scale(1.0/data2022Down.Integral())
data2023 = inputFile.Get("data2023")
data2023.Scale(1.0/data2023.Integral())
data2023Up = inputFile.Get("data2023Up")
data2023Up.Scale(1.0/data2023Up.Integral())
data2023Down = inputFile.Get("data2023Down")
data2023Down.Scale(1.0/data2023Down.Integral())

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
Canvas2022.Print("pileup2022.pdf")

data2022.SetMarkerStyle(20)
data2022.SetLineColor(1)
data2022.SetMarkerColor(1)

data2022Up.SetLineColor(2)
data2022Up.SetLineStyle(3)
data2022Up.SetLineWidth(2)

data2022Down.SetLineColor(4)
data2022Down.SetLineStyle(3)
data2022Down.SetLineWidth(2)

Legend2022UpDown = TLegend(0.7,0.75,0.9,0.85)
Legend2022UpDown.SetBorderSize(0)
Legend2022UpDown.SetFillColor(0)
Legend2022UpDown.SetFillStyle(0)
Legend2022UpDown.SetTextSize(0.03)
Legend2022UpDown.AddEntry(data2022,"nominal","P")
Legend2022UpDown.AddEntry(data2022Down,"scaled down","L")
Legend2022UpDown.AddEntry(data2022Up,"scaled up","L")

Canvas2022UpDown = TCanvas("Canvas2022UpDown","Canvas2022UpDown",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2022UpDown.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2022UpDown.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2022UpDown.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2022UpDown.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas2022UpDown.cd()
data2022Down.SetTitle("")
data2022Down.GetXaxis().SetTitle("Number of interactions")
data2022Down.GetYaxis().SetTitle("Number of events [arb. norm.]")
data2022Down.GetYaxis().SetTitleOffset(1.8)
data2022Down.Draw("HIST")
data2022.Draw("P,SAME")
data2022Up.Draw("HIST,SAME")
Legend2022UpDown.Draw()

CMS_lumi.CMS_lumi(Canvas2022UpDown, iPeriod, iPos)
Canvas2022UpDown.Update()
Canvas2022UpDown.Print("pileup2022_upDown.pdf")

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
Canvas2023.Print("pileup2023.pdf")

data2023.SetMarkerStyle(20)
data2023.SetLineColor(1)
data2023.SetMarkerColor(1)

data2023Up.SetLineColor(2)
data2023Up.SetLineStyle(3)
data2023Up.SetLineWidth(2)

data2023Down.SetLineColor(4)
data2023Down.SetLineStyle(3)
data2023Down.SetLineWidth(2)

Legend2023UpDown = TLegend(0.7,0.75,0.9,0.85)
Legend2023UpDown.SetBorderSize(0)
Legend2023UpDown.SetFillColor(0)
Legend2023UpDown.SetFillStyle(0)
Legend2023UpDown.SetTextSize(0.03)
Legend2023UpDown.AddEntry(data2023,"nominal","P")
Legend2023UpDown.AddEntry(data2023Down,"scaled down","L")
Legend2023UpDown.AddEntry(data2023Up,"scaled up","L")

Canvas2023UpDown = TCanvas("Canvas2023UpDown","Canvas2023UpDown",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas2023UpDown.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas2023UpDown.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas2023UpDown.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas2023UpDown.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas2023UpDown.cd()
data2023Down.SetTitle("")
data2023Down.GetXaxis().SetTitle("Number of interactions")
data2023Down.GetYaxis().SetTitle("Number of events [arb. norm.]")
data2023Down.GetYaxis().SetTitleOffset(1.8)
data2023Down.Draw("HIST")
data2023.Draw("P,SAME")
data2023Up.Draw("HIST,SAME")
Legend2023UpDown.Draw()

CMS_lumi.CMS_lumi(Canvas2023UpDown, iPeriod, iPos)
Canvas2023UpDown.Update()
Canvas2023UpDown.Print("pileup2023_upDown.pdf")