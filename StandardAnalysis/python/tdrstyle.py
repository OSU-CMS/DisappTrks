#!/usr/bin/env python3

#from ROOT import TStyle
from ROOT import TF1, TFile, TH2F, TGraph, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TPaveLabel, TH2D, TPave, Double
def setTDRStyle():
    tdrStyle = TStyle("tdrStyle","Style for P-TDR")
    tdrStyle.SetCanvasBorderMode(0)
    #    tdrStyle.SetCanvasColor(kWhite)
    tdrStyle.SetCanvasColor(0)
    tdrStyle.SetCanvasDefH(600)
    tdrStyle.SetCanvasDefW(600)
    tdrStyle.SetCanvasDefX(0)
    tdrStyle.SetCanvasDefY(0)

    tdrStyle.SetPadBorderMode(0)
    #    tdrStyle.SetPadColor(kWhite)
    tdrStyle.SetPadColor(0)
    #    tdrStyle.SetPadGridX(kFALSE)
    tdrStyle.SetPadGridX(0)
    #    tdrStyle.SetPadGridY(false)
    tdrStyle.SetPadGridY(0)
    tdrStyle.SetGridColor(0)
    tdrStyle.SetGridStyle(3)
    tdrStyle.SetGridWidth(1)

    tdrStyle.SetFrameBorderMode(0)
    tdrStyle.SetFrameBorderSize(1)
    tdrStyle.SetFrameFillColor(0)
    tdrStyle.SetFrameFillStyle(0)
    tdrStyle.SetFrameLineColor(1)
    tdrStyle.SetFrameLineStyle(1)
    tdrStyle.SetFrameLineWidth(1)

    tdrStyle.SetHistLineColor(1)
    tdrStyle.SetHistLineStyle(0)
    tdrStyle.SetHistLineWidth(1)

    tdrStyle.SetEndErrorSize(2)
    tdrStyle.SetErrorX(0.)

    tdrStyle.SetMarkerStyle(20)

    tdrStyle.SetOptFit(0)
    tdrStyle.SetFitFormat("5.4g")
    tdrStyle.SetFuncColor(2)
    tdrStyle.SetFuncStyle(1)
    tdrStyle.SetFuncWidth(1)

    tdrStyle.SetOptDate(0)

    tdrStyle.SetOptFile(0)
    tdrStyle.SetOptStat(0000000)
    tdrStyle.SetStatColor(0)
    tdrStyle.SetStatFont(42)
    tdrStyle.SetStatFontSize(0.025)
    tdrStyle.SetStatTextColor(1)
    tdrStyle.SetStatFormat("6.4g")
    tdrStyle.SetStatBorderSize(1)
    tdrStyle.SetStatH(0.1)
    tdrStyle.SetStatW(0.15)

    tdrStyle.SetPadTopMargin(0.07)
    #    tdrStyle.SetPadBottomMargin(0.13)
    tdrStyle.SetPadBottomMargin(0.16)
    tdrStyle.SetPadLeftMargin(0.16)
    #    tdrStyle.SetPadRightMargin(0.02)
    tdrStyle.SetPadRightMargin(0.06)

    tdrStyle.SetOptTitle(0)
    tdrStyle.SetTitleFont(42)
    tdrStyle.SetTitleColor(1)
    tdrStyle.SetTitleTextColor(1)
    tdrStyle.SetTitleFillColor(10)
    tdrStyle.SetTitleFontSize(0.05)

    tdrStyle.SetTitleColor(1, "XYZ")
    tdrStyle.SetTitleFont(42, "XYZ")
    tdrStyle.SetTitleSize(0.06, "XYZ")

    #    tdrStyle.SetTitleXOffset(0.9)
    tdrStyle.SetTitleXOffset(1.1)
    #    tdrStyle.SetTitleYOffset(1.25)
    #    tdrStyle.SetTitleYOffset(1.2)
    tdrStyle.SetTitleYOffset(1.1)


    tdrStyle.SetTitleColor(1, "XYZ")
    tdrStyle.SetTitleFont(42, "XYZ")
    tdrStyle.SetTitleSize(0.06, "XYZ")
    tdrStyle.SetTitleXOffset(1.1)
    #    tdrStyle.SetTitleYOffset(1.25)
    tdrStyle.SetTitleYOffset(1.23)

    tdrStyle.SetLabelColor(1, "XYZ")
    tdrStyle.SetLabelFont(42, "XYZ")
    tdrStyle.SetLabelOffset(0.007, "XYZ")
    #    tdrStyle.SetLabelSize(0.05, "XYZ")
    tdrStyle.SetLabelSize(0.045, "XYZ")

    tdrStyle.SetAxisColor(1, "XYZ")
    #    tdrStyle.SetStripDecimals(kTRUE)
    tdrStyle.SetStripDecimals(1)
    tdrStyle.SetTickLength(0.03, "XYZ")
#    tdrStyle.SetNdivisions(510, "XYZ")
    tdrStyle.SetNdivisions(509, "XYZ")
    tdrStyle.SetPadTickX(1)
    tdrStyle.SetPadTickY(1)

    tdrStyle.SetOptLogx(0)
    tdrStyle.SetOptLogy(0)
    tdrStyle.SetOptLogz(0)

    tdrStyle.SetPaperSize(20.,20.)

    tdrStyle.cd()

