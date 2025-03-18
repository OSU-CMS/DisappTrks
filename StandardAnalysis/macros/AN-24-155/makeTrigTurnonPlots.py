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

print("\n********************************************************************************************************")
print("* Be sure that you are running this script after running the TRIGGER_TURN_ON signal systematic source!")
print("* Otherwise, the input files below will not have been created.")
print("********************************************************************************************************\n")

inputFile4 = TFile("../../../SignalSystematics/test/triggerEfficiency_AMSB_chargino_NLayers4.root")
inputFile5 = TFile("../../../SignalSystematics/test/triggerEfficiency_AMSB_chargino_NLayers5.root")
inputFile6 = TFile("../../../SignalSystematics/test/triggerEfficiency_AMSB_chargino_NLayers6plus.root")

trigTurnOn4 = inputFile4.Get("GrandOr_METPath_AMSB_700GeV")
trigTurnOn5 = inputFile5.Get("GrandOr_METPath_AMSB_700GeV")
trigTurnOn6 = inputFile6.Get("GrandOr_METPath_AMSB_700GeV")

trigTurnOn4.SetMarkerStyle(20)
trigTurnOn4.SetMarkerSize(1.0)
trigTurnOn4.SetLineColor(1)
trigTurnOn4.SetMarkerColor(1)

trigTurnOn5.SetMarkerStyle(20)
trigTurnOn5.SetMarkerSize(1.0)
trigTurnOn5.SetLineColor(2)
trigTurnOn5.SetMarkerColor(2)

trigTurnOn6.SetMarkerStyle(20)
trigTurnOn6.SetMarkerSize(1.0)
trigTurnOn6.SetLineColor(4)
trigTurnOn6.SetMarkerColor(4)

Legend2022 = TLegend(0.65,0.75,0.93,0.88)
Legend2022.SetBorderSize(0)
Legend2022.SetFillColor(0)
Legend2022.SetFillStyle(0)
Legend2022.SetTextSize(0.03)
Legend2022.SetHeader("OR of Signal Paths")
Legend2022.AddEntry(trigTurnOn4,"NLayers4","P")
Legend2022.AddEntry(trigTurnOn5,"NLayers5","P")
Legend2022.AddEntry(trigTurnOn6,"NLayers6plus","P")

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
Canvas2022.SetLogx()
trigTurnOn4.SetTitle("")
trigTurnOn4.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
trigTurnOn4.GetYaxis().SetTitle("Trigger Efficiency")
trigTurnOn4.GetYaxis().SetTitleOffset(1.4)
trigTurnOn4.GetXaxis().SetLimits(9,1000)
trigTurnOn4.GetYaxis().SetRangeUser(0.0,1.4)
trigTurnOn4.Draw()
trigTurnOn5.Draw("SAME,P,L")
trigTurnOn6.Draw("SAME,P,L")
Legend2022.Draw()

CMS_lumi.CMS_lumi(Canvas2022, iPeriod, iPos)
Canvas2022.Update()
Canvas2022.Print("compareNLayers_GrandOr_700GeV_2022EE.pdf")

# Legend2023 = TLegend(0.7,0.75,0.9,0.85)
# Legend2023.SetBorderSize(0)
# Legend2023.SetFillColor(0)
# Legend2023.SetFillStyle(0)
# Legend2023.SetTextSize(0.03)
# Legend2023.AddEntry(data2023,"2023 data","P")
# Legend2023.AddEntry(mc2023,"W #rightarrow l#nu MC","P")

# Canvas2023 = TCanvas("Canvas2023","Canvas2023",50,50,CMS_lumi.W,CMS_lumi.H)
# Canvas2023.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
# Canvas2023.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
# Canvas2023.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
# Canvas2023.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

# Canvas2023.cd()
# Canvas2023.SetLogx()
# data2023.SetTitle("")
# data2023.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
# data2023.GetYaxis().SetTitle("Trigger Efficiency")
# data2023.GetYaxis().SetTitleOffset(1.4)
# data2023.GetXaxis().SetLimits(9,1000)
# data2023.GetYaxis().SetRangeUser(0.0,1.4)
# data2023.Draw()
# mc2023.Draw("SAME,P,L")
# Legend2023.Draw()

# CMS_lumi.CMS_lumi(Canvas2023, iPeriod, iPos)
# Canvas2023.Update()
# Canvas2023.Print("TrigEff2023.pdf")

