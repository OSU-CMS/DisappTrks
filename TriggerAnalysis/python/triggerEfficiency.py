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

def compare(trigger, leg, data, mc, axisTitle, canvas, dataLumi, metHLTFilters):
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

    pt_lumi = TPaveText(0.744361, 0.92928, 0.860902, 0.977667, "brNDC")
    pt_lumi.SetBorderSize(0)
    pt_lumi.SetFillStyle(0)
    pt_lumi.SetTextFont(42)
    pt_lumi.SetTextSize(0.0374065)
    pt_lumi.AddText("{:.2f}".format(dataLumi / 1000.0) + " fb^{-1}, 13 TeV")
    pt_lumi.Draw("same")

    pt_leg = TPaveText(0.160401, 0.768657, 0.342105, 0.863184, "brNDC")
    pt_leg.SetBorderSize(0)
    pt_leg.SetFillStyle(0)
    pt_leg.SetTextFont(42)
    pt_leg.SetTextSize(0.025)
    pt_leg.SetTextAlign(12)
    if leg == "METLeg":
        legLabel = ""
        for filt in metHLTFilters[:-1]:
            legLabel = legLabel + filt + ", "
        legLabel = legLabel + metHLTFilters[-1]
        pt_leg.AddText(legLabel)
    if leg == "TrackLeg":
        pt_leg.AddText(trigger + "*")
        legLabel = ""
        for filt in metHLTFilters[:-1]:
            legLabel = legLabel + filt + ", "
        legLabel = legLabel + metHLTFilters[-1] + " applied"
        pt_leg.AddText(legLabel)
    if leg == "METPath":
        if trigger == "GrandOr":
            pt_leg.AddText("OR of Signal Paths")
        else:
            if len(trigger) > 25 and len(trigger.split("_")) > 2:
                firstLine = trigger.split("_")[0] + "_" + trigger.split("_")[1] + "_"
                pt_leg.AddText(firstLine)
                secondLine = ""
                for line in trigger.split("_")[2:-1]:
                    secondLine += line + "_"
                secondLine += trigger.split("_")[-1] + "*"
                pt_leg.AddText(secondLine)
            else:
                pt_leg.AddText(trigger + "*")
    pt_leg.Draw("same")

    dataLabel = '2015 data'
    if '2016BC' in data:
        dataLabel = '2016 B+C data'
    if '2016DEFGH' in data:
        dataLabel = '2016 D-H data'

    legendLabel = trigger

    legend = TLegend(0.65, 0.75, 0.93, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
    if leg == 'METLeg':
        legend.SetHeader('MET Leg')
    elif leg == 'TrackLeg':
        legend.SetHeader('Track Leg')
    legend.AddEntry(dataEff, dataLabel, 'P')
    legend.AddEntry(mcEff, 'W #rightarrow l#nu MC', 'P')
    legend.Draw("same")

    outputDirectory = 'plots_compare'
    if 'BC' in data:
        outputDirectory = 'plots_compareBC'
    if 'DEFGH' in data:
        outputDirectory = 'plots_compareDEFGH'

    if not os.path.exists(outputDirectory):
        os.mkdir(outputDirectory)

    canvas.SaveAs(outputDirectory + '/' + trigger + '_' + leg + '.pdf')

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
    _rebinFactor = 10
    _metLegHistName = "Met Plots/metNoMuLogX"
    _metLegAxisTitle = "PF E_{T}^{miss, no #mu} [GeV]"
    _trackLegHistName = "Eventvariable Plots/leadMuonPt"
    _trackLegAxisTitle =  "Muon p_{T} [GeV]"
    _datasetLabel = ""
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
        self._luminosityLabel = "{:.2f}".format(self._luminosityInInvFb) + " fb^{-1}, 13 TeV"

    def addLuminosityLabel(self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

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

    def setDatasetLabel(self, label):
        self._datasetLabel = label

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
            pt_lumi.AddText(self._luminosityLabel)

            pt_leg = TPaveText(0.160401, 0.768657, 0.342105, 0.863184, "brNDC")
            pt_leg.SetBorderSize(0)
            pt_leg.SetFillStyle(0)
            pt_leg.SetTextFont(42)
            pt_leg.SetTextSize(0.0349127)
            pt_leg.SetTextAlign(12)
            if self._leg == "METLeg":
                legLabel = ""
                for filt in self._metHLTFilters[:-1]:
                    legLabel = legLabel + filt + ", "
                legLabel = legLabel + self._metHLTFilters[-1]
                pt_leg.AddText(legLabel)
                pt_leg.AddText(self._datasetLabel)
            if self._leg == "TrackLeg":
                pt_leg.AddText(self._path + "*")
                pt_leg.AddText(self._datasetLabel)
                legLabel = ""
                for filt in self._metHLTFilters[:-1]:
                    legLabel = legLabel + filt + ", "
                legLabel = legLabel + self._metHLTFilters[-1] + " applied"
                pt_leg.AddText(legLabel)
            if self._leg == "METPath":
                if self._path == "GrandOr":
                    pt_leg.AddText("OR of Signal Paths")
                else:
                    pt_leg.AddText(self._path + "*")
                pt_leg.AddText(self._datasetLabel)

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
