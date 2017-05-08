#!/usr/bin/env python
import os
import sys
import math

from ROOT import gROOT, gStyle, TCanvas, TFile, TMath, TGraphAsymmErrors, TH1D, TPaveText, TLine, TLegend

from DisappTrks.StandardAnalysis.plotUtilities import *

gROOT.SetBatch()
gStyle.SetOptStat(0);
gStyle.SetOptFit(0);
gStyle.SetOptTitle(0);

NBINS = 100

xlo = 9.0
xhi = 1100.0

ylo = 0.0
yhi = 1.5

def SetStyle(graph):
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(1.5)
    graph.SetMarkerColor(1)

    graph.SetLineStyle(1)
    graph.SetLineColor(1)
    graph.SetLineWidth(1)

    graph.GetXaxis().SetLabelSize(0.04)
    graph.GetXaxis().SetTitleSize(0.04)
    graph.GetXaxis().SetTitleOffset(1.25)

    graph.GetYaxis().SetLabelSize(0.04)
    graph.GetYaxis().SetTitleSize(0.04)
    graph.GetYaxis().SetTitleOffset(1.5)
    graph.GetYaxis().SetRangeUser(ylo, yhi)

def normCDF(x, par):
    return (0.5 * par[2] * (1.0 + TMath.Erf((x[0] - par[0]) / (math.sqrt(2.0) * par[1]))) + par[3])


def compare(trigger, leg, data, mc, axisTitle, canvas):
    dataFile = TFile.Open("triggerEfficiency_" + data + ".root", "read")
    mcFile = TFile.Open("triggerEfficiency_" + mc + ".root", "read")

    dataEff = dataFile.Get(trigger + "_" + leg)
    mcEff = mcFile.Get(trigger + "_" + leg)

    SetStyle(dataEff)
    SetStyle(mcEff)
    mcEff.SetLineColor(600)
    mcEff.SetMarkerColor(600)

    oneLine = TLine(xlo, 1.0, xhi, 1.0)
    oneLine.SetLineWidth(3)
    oneLine.SetLineStyle(2)

    backgroundHist = TH1D("backgroundHist", "backgroundHist", 1, xlo, xhi)
    backgroundHist.GetYaxis().SetTitle("Trigger Efficiency")
    backgroundHist.GetYaxis().SetRangeUser(ylo, yhi)
    backgroundHist.GetXaxis().SetTitle(axisTitle)
    SetStyle(backgroundHist)

    canvas.cd()
    backgroundHist.Draw()
    dataEff.Draw("CP same")
    mcEff.Draw("CP same")
    #oneLine.Draw("same")

    pt_cmsPrelim = TPaveText(0.132832, 0.859453, 0.486216, 0.906716, "brNDC")
    pt_cmsPrelim.SetBorderSize(0)
    pt_cmsPrelim.SetFillStyle(0)
    pt_cmsPrelim.SetTextFont(62)
    pt_cmsPrelim.SetTextSize(0.0374065)
    pt_cmsPrelim.AddText("CMS Preliminary")
    pt_cmsPrelim.Draw("same")

    dataLabel = '2015 data'
    if '2016' in data:
        dataLabel = '2016D-H data'

    legendLabel = trigger

    legend = TLegend(0.6, 0.75, 0.88, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
    if leg == 'METLeg':
        legend.AddEntry(NULL, 'MET Leg', '')
    elif leg == 'TrackLeg':
        legend.AddEntry(NULL, 'Track Leg', '')
    legend.AddEntry(dataEff, dataLabel, 'P')
    legend.AddEntry(mcEff, 'W #rightarrow l#nu MC', 'P')
    legend.Draw("same")

    if not os.path.exists('plots_compare'):
        os.mkdir('plots_compare')

    canvas.SaveAs('plots_compare/' + trigger + '_' + leg + '.pdf')

    mcFile.Close()
    dataFile.Close()

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
    _rebinFactor = 10
    _metLegHistName = "Met Plots/metNoMuLogX"
    _metLegAxisTitle = "PF E_{T}^{miss, no #mu} [GeV]"
    _trackLegHistName = "Eventvariable Plots/leadMuonPt"
    _trackLegAxisTitle =  "Muon p_{T} [GeV]"
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

    def setMetLegAxisTitle(self, title):
        self._metLegAxisTitle = title

    def setTrackLegHistName(self, name):
        self._trackLegHistName = name

    def setTrackLegAxisTitle(self, title):
        self._trackLegAxisTitle = title

    def setIsMC(self, isMC):
        self._isMC = isMC
        self._trackLegHistName = "Eventvariable Plots/leadTrackPt"
        self._trackLegAxisTitle = "Track p_{T} [GeV]"

    def addChannel(self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
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
                    legLabel = legLabel + self._metHLTFilters[-1] + " applied"
                    pt_leg.AddText(legLabel)
            elif self._leg == "METLeg":
                legLabel = ""
                for filt in self._metHLTFilters[:-1]:
                    legLabel = legLabel + filt + ", "
                legLabel = legLabel + self._metHLTFilters[-1]
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
            if self._leg == "METLeg" or self._leg == "METPath":
                backgroundHist.GetXaxis().SetTitle(self._metLegAxisTitle)
            elif self._leg == "TrackLeg":
                backgroundHist.GetXaxis().SetTitle(self._trackLegAxisTitle)

            SetStyle(backgroundHist)
            SetStyle(efficiencyGraph)

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

            if not os.path.exists('plots_' + self.Denominator["sample"]):
                os.mkdir('plots_' + self.Denominator["sample"])

            if self._leg == "METPath":
                self._canvas.SaveAs('plots_' + self.Denominator["sample"] + '/' + self._path + "_Efficiency.pdf")
            else:
                self._canvas.SaveAs('plots_' + self.Denominator["sample"] + '/' + self._path + "_" + self._leg + ".pdf")
            self._fout.cd()
            efficiencyGraph.Write(self._path + "_" + self._leg)
            if doFit:
                fitFunc.Write(self._path + "_" + self._leg + "_fitResult")

        else:
            print "Denominator and Numerator must be defined for path ", self._path, ", leg ", self._leg
            return 0.0
