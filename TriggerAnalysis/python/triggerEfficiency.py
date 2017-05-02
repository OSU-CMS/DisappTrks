#!/usr/bin/env python
import os
import sys
import math

from ROOT import gROOT, gStyle, TCanvas, TFile, TMath, TGraphAsymmErrors, TH1D, TPaveText, TLine

from DisappTrks.StandardAnalysis.plotUtilities import *

setTDRStyle()

gROOT.SetBatch()

NBINS = 100

xlo = 9.0
xhi = 1100.0

ylo = 0.0
yhi = 1.5

def SetStyle(histogram):
    histogram.SetMarkerStyle(20)
    histogram.SetLineStyle(1)
    histogram.SetMarkerSize(1.5)
    histogram.SetLineWidth(1)

    histogram.GetXaxis().SetLabelSize(0.04)
    histogram.GetXaxis().SetTitleSize(0.04)
    histogram.GetXaxis().SetTitleOffset(1.25)

    histogram.GetYaxis().SetLabelSize(0.04)
    histogram.GetYaxis().SetTitleSize(0.04)
    histogram.GetYaxis().SetTitleOffset(1.5)
    histogram.GetYaxis().SetRangeUser(ylo, yhi)

def normCDF(x, par):
    return (0.5 * par[2] * (1.0 + TMath.Erf((x[0] - par[0]) / (math.sqrt(2.0) * par[1]))) + par[3])


def compare():
    # durp
    return

class TriggerEfficiency:
    _path = ""
    _metHLTFilters = []
    _leg = ""
    _fout = None
    _canvas = None
    _luminosityInInvFb = float("nan")
    _luminosityLabel = "13 TeV"
    _plotLabel = float("nan")
    _rebinFactor = 1
    _metLegHistName = "Met Plots/metNoMuLogX"
    _trackLegHistName = "Eventvariable Plots/leadMuonPt"
    _isMC = False

    def __init__(self, path, metHLTFilters, leg):
        self._path = path
        self._metHLTFilters = metHLTFilters
        self._leg = leg

    def addTFile(self, fout):
        self._fout = fout

    def addTCanvas(self, canvas):
        self._canvas = canvas

    def addLuminosityInInvPb(self, luminosityInInvPb):
        self._luminosityInInvFb = luminosityInInvPb / 1000.0
        #self._luminosityLabel =

    def addLuminosityLabel(self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

    def addPlotLabel(self, plotLabel):
        self._plotLabel = plotLabel

    def addRebinFactor(self, rebinFactor):
        self._rebinFactor = rebinFactor

    def setMetLegHistName(self, name):
        self._metLegHistName = name

    def setTrackLegHistName(self, name):
        self._trackLegHistName = name

    def setIsMC(self, isMC):
        self._isMC = isMC
        self._trackLegHistName = "Eventvariable Plots/leadTrackPt"

    def addChannel(self, role, name, sample, condorDir):
        channel = {"name" : name, "condorDir" : condorDir}
        if self._leg == "METLeg" or self._leg == "METPath":
            channel["hist"] = getHist(sample, condorDir, name + "Plotter", self._metLegHistName)
        elif self._leg == "TrackLeg":
            channel["hist"] = getHist(sample, condorDir, name + "Plotter", self._trackLegHistName)
        setattr(self, role, channel)

    def plotEfficiency(self, doFit = False):
        if hasattr(self, "Denominator") and hasattr(self, "Numerator"):
            if self._rebinFactor != 1:
                self.Denominator["hist"].Rebin(self._rebinFactor)
                self.Numerator["hist"].Rebin(self._rebinFactor)
            efficiencyGraph = TGraphAsymmErrors(self.Numerator["hist"], self.Denominator["hist"], "cp")

            pt_cmsPrelim = TPaveText(0.132832, 0.859453, 0.486216, 0.906716, "brNDC")
            pt_cmsPrelim.SetBorderSize(0)
            pt_cmsPrelim.SetFillStyle(0)
            pt_cmsPrelim.SetTextFont(62)
            pt_cmsPrelim.SetTextSize(0.0374065)
            pt_cmsPrelim.AddText("CMS Preliminary")

            pt_lumi = TPaveText(0.744361, 0.92928, 0.860902, 0.977667, "brNDC")
            pt_lumi.SetBorderSize(0)
            pt_lumi.SetFillStyle(0)
            pt_lumi.SetTextFont(42)
            pt_lumi.SetTextSize(0.0374065)
            pt_lumi.AddText(self._luminosityLabel) #durp

            pt_leg = TPaveText(0.160401, 0.768657, 0.342105, 0.863184, "brNDC")
            pt_leg.SetBorderSize(0)
            pt_leg.SetFillStyle(0)
            pt_leg.SetTextFont(42)
            pt_leg.SetTextSize(0.0349127)
            pt_leg.SetTextAlign(12)
            if self._leg == "METPath" or self._leg == "TrackLeg":
                pt_leg.AddText(self._path)
                #pt_leg.AddText(durp datasetLabel)
                if self._leg == "TrackLeg":
                    legLabel = ""
                    for filt in self._metHLTFilters[:-1]:
                        legLabel = legLabel + filt + ", "
                    legLabel = legLabel + filt[-1] + " applied"
                    pt_leg.AddText(legLabel)
            elif self._leg == "METLeg":
                legLabel = ""
                for filt in self._metHLTFilters[:-1]:
                    legLabel = legLabel + filt + ", "
                legLabel = legLabel + filt[-1]
                pt_leg.AddText(legLabel)
                #pt_leg.AddText(durp datasetLabel)

            pt = TPaveText(0.522556, 0.838501, 0.921053, 0.885013, "brNDC")
            pt.SetBorderSize(0)
            pt.SetFillStyle(0)
            pt.SetTextFont(42)
            pt.SetTextSize(0.0387597)
            pt.AddText(str (self._plotLabel))

            cmsLabel = TPaveText(0.134085, 0.937984, 0.418546, 0.984496, "brNDC")
            cmsLabel.SetBorderSize(0)
            cmsLabel.SetFillStyle(0)
            cmsLabel.SetTextFont(62)
            cmsLabel.SetTextSize(0.0387597)
            cmsLabel.AddText("CMS Preliminary")

            lumiLabel = TPaveText(0.66416, 0.937339, 0.962406, 0.992894, "brNDC")
            lumiLabel.SetBorderSize(0)
            lumiLabel.SetFillStyle(0)
            lumiLabel.SetTextFont(42)
            lumiLabel.SetTextSize(0.0387597)
            lumiLabel.AddText(str (self._luminosityLabel))

            oneLine = TLine(xlo, 1.0, xhi, 1.0)
            oneLine.SetLineWidth(3)
            oneLine.SetLineStyle(2)

            backgroundHist = TH1D("backgroundHist", "backgroundHist", 1, xlo, xhi)
            backgroundHist.GetYaxis().SetTitle("Trigger Efficiency")
            backgroundHist.GetYaxis().SetRangeUser(ylo, yhi)
            if self._leg == "METLeg":
                backgroundHist.GetXaxis().SetTitle("PF E_{T}^{miss} (no muons) [GeV]")
                #efficiencyGraph.SetName("metTriggerEfficiency")
            elif self._leg == "TrackLeg":
                backgroundHist.GetXaxis().SetTitle("Track p_{T} [GeV]" if self._isMC else "Muon p_{T} [GeV]")
                #efficiencyGraph.SetName("trackTriggerEfficiency")

            setStyle(efficiencyGraph)

            self._canvas.cd()
            backgroundHist.Draw()
            efficiencyGraph.Draw("P")
            pt_cmsPrelim.Draw("same")
            pt_lumi.Draw("same")
            pt_leg.Draw("same")
            oneLine.Draw("same")

            fitFunc = TF1("fitFunc0", normCDF, 1.0e1, 1.0e3, 4)

            if doFit:
                fitFunc = self.PlotFit()

            if self._leg == "METPath":
                self._canvas.SaveAs(self._path + "_Efficiency.pdf")
            else:
                self._canvas.SaveAs(self._path + "_" + self._leg + ".pdf")
            self._fout.cd()
            efficiencyGraph.Write(self._path + "_" + self._leg)
            if doFit:
                fitFunc.Write(self._path + "_" + self._leg + "_fitResult")

        else:
            print "Denominator and Numerator must be defined for path ", self._path, ", leg ", self._leg
            return 0.0
