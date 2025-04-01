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

def ratioErrorCalc(val1,val2,err1,err2):
    err = math.sqrt(((1.0/val2)*(1.0/val2)*(err1*err1))+((val1/(val2*val2))*(val1/(val2*val2))*(err2*err2)))
    return err

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

Legend2022 = TLegend(0.65,0.7,0.9,0.85)
Legend2022.SetBorderSize(0)
Legend2022.SetFillColor(0)
Legend2022.SetFillStyle(0)
Legend2022.SetTextSize(0.04)
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
pz12022 = TPad("pz12022", "", 0.0, 0.25, 1.0, 1.0, 21)
pz22022 = TPad("pz22022", "", 0.0, 0.0, 1.0, 0.24, 21)
pz12022.SetFillColor(0)
pz22022.SetFillColor(0)
pz12022.SetTopMargin(0.11)
pz12022.SetBottomMargin(0.017)
pz12022.SetLeftMargin(0.15)
pz12022.SetRightMargin(0.05)
pz22022.SetTopMargin(0.005)
pz22022.SetBottomMargin(0.4)
pz22022.SetLeftMargin(0.15)
pz22022.SetRightMargin(0.05)
pz12022.Draw()
pz22022.Draw()

line2022 = TLine(9,1.0,1000,1.0)
line2022.SetLineWidth(2)
line2022.SetLineStyle(2)

pz12022.cd()
pz12022.SetLogx()
trigTurnOn4.SetTitle("")
trigTurnOn4.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
trigTurnOn4.GetYaxis().SetTitle("Trigger Efficiency")
trigTurnOn4.GetYaxis().SetTitleOffset(1.4)
trigTurnOn4.GetYaxis().SetTitleSize(0.045)
trigTurnOn4.GetXaxis().SetLimits(9,1000)
trigTurnOn4.GetXaxis().SetLabelSize(0.0)
trigTurnOn4.GetYaxis().SetLabelSize(0.045)
trigTurnOn4.GetYaxis().SetRangeUser(0.0,1.4)
trigTurnOn4.Draw()
trigTurnOn5.Draw("SAME,P,L")
trigTurnOn6.Draw("SAME,P,L")
Legend2022.Draw()
line2022.Draw()

ratio4Layers2022 = trigTurnOn4.Clone("ratio4Layers2022")

for i in range(trigTurnOn4.GetN()):
    if trigTurnOn6.GetPointY(i+20) > 0.0:
        ratio4Layers2022.SetPoint(i,trigTurnOn4.GetPointX(i),trigTurnOn4.GetPointY(i)/trigTurnOn6.GetPointY(i+20))
        ratio4Layers2022.SetPointError(i,trigTurnOn4.GetErrorXlow(i),trigTurnOn4.GetErrorXhigh(i),ratioErrorCalc(trigTurnOn4.GetPointY(i),trigTurnOn6.GetPointY(i+20),trigTurnOn4.GetErrorYlow(i),trigTurnOn6.GetErrorYlow(i+20)),ratioErrorCalc(trigTurnOn4.GetPointY(i),trigTurnOn6.GetPointY(i+20),trigTurnOn4.GetErrorYhigh(i),trigTurnOn6.GetErrorYhigh(i+20)))
    else:
        ratio4Layers2022.SetPoint(i,trigTurnOn4.GetPointX(i),0.0)

ratio5Layers2022 = trigTurnOn5.Clone("ratio5Layers2022")

for i in range(trigTurnOn5.GetN()):
    if trigTurnOn6.GetPointY(i+17) > 0.0:
        ratio5Layers2022.SetPoint(i,trigTurnOn5.GetPointX(i),trigTurnOn5.GetPointY(i)/trigTurnOn6.GetPointY(i+17))
        ratio5Layers2022.SetPointError(i,trigTurnOn5.GetErrorXlow(i),trigTurnOn5.GetErrorXhigh(i),ratioErrorCalc(trigTurnOn5.GetPointY(i),trigTurnOn6.GetPointY(i+17),trigTurnOn5.GetErrorYlow(i),trigTurnOn6.GetErrorYlow(i+17)),ratioErrorCalc(trigTurnOn5.GetPointY(i),trigTurnOn6.GetPointY(i+17),trigTurnOn5.GetErrorYhigh(i),trigTurnOn6.GetErrorYhigh(i+17)))
    else:
        ratio5Layers2022.SetPoint(i,trigTurnOn5.GetPointX(i),0.0)

pz22022.cd()
pz22022.SetLogx()
ratio4Layers2022.GetXaxis().SetLimits(9,1000)
ratio4Layers2022.GetYaxis().SetRangeUser(0.0,1.99)
ratio4Layers2022.GetYaxis().SetTitle("#frac{NLayers4/5}{NLayers6plus}")
ratio4Layers2022.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")
ratio4Layers2022.GetXaxis().SetTitleSize(0.15)
ratio4Layers2022.GetXaxis().SetLabelSize(0.15)
ratio4Layers2022.GetYaxis().SetTitleSize(0.15)
ratio4Layers2022.GetYaxis().SetLabelSize(0.15)
ratio4Layers2022.GetYaxis().SetNdivisions(4, 1, 0)
ratio4Layers2022.GetXaxis().SetTitleOffset(1.2)
ratio4Layers2022.GetYaxis().SetTitleOffset(0.45)
ratio4Layers2022.Draw()
ratio5Layers2022.Draw("SAME,P,L")
line2022.Draw()

CMS_lumi.CMS_lumi(Canvas2022, iPeriod, iPos)
Canvas2022.Update()
Canvas2022.Print("compareNLayersRatio_GrandOr_700GeV_2022EE.pdf")

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

