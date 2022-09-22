#!/usr/bin/env python3
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
    mu = par[0]
    sigma = par[1]
    return 0.5 * (1.0 + TMath.Erf((x[0] - mu) / (math.sqrt(2.0) * sigma)))

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
    if '2017' in data:
        dataLabel = '2017 data'
    if '2018' in data:
        dataLabel = '2018 data'

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

def compareDatasets(trigger, leg, datasets, lineColors, legendLabels, axisTitle, canvas, dataLumi, metHLTFilters, outputSuffix = None):

    inputFiles = [TFile.Open("triggerEfficiency_" + x + ".root") for x in datasets]
    efficiencies = [x.Get(trigger + "_" + leg) for x in inputFiles]

    for iEff in range(len(efficiencies)):
        SetStyle(efficiencies[iEff])
        efficiencies[iEff].SetLineColor(lineColors[iEff])
        efficiencies[iEff].SetMarkerColor(lineColors[iEff])

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
    for eff in efficiencies:
        eff.Draw("CP same")
    #oneLine.Draw("same")

    pt_cmsPrelim = TPaveText(0.132832, 0.859453, 0.486216, 0.906716, "brNDC")
    pt_cmsPrelim.SetBorderSize(0)
    pt_cmsPrelim.SetFillStyle(0)
    pt_cmsPrelim.SetTextFont(62)
    pt_cmsPrelim.SetTextSize(0.0374065)
    if dataLumi > 0:
        pt_cmsPrelim.AddText("CMS Preliminary")
    else:
        pt_cmsPrelim.AddText("CMS Simulation")
    pt_cmsPrelim.Draw("same")

    if dataLumi > 0:
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
    for iEff in range(len(efficiencies)):
        legend.AddEntry(efficiencies[iEff], legendLabels[iEff], 'P')
    legend.Draw("same")

    if outputSuffix is not None:
        canvas.SaveAs('compareDatasets_' + trigger + '_' + leg + '_' + outputSuffix + '.pdf')
    else:
        canvas.SaveAs('compareDatasets_' + trigger + '_' + leg + '_.pdf')

    for inputFile in inputFiles:
        inputFile.Close()

    return

def compareTriggers(triggerA, triggerB, leg, dataset, axisTitle, canvas, dataLumi, metHLTFilters):
    inputFile = TFile.Open("triggerEfficiency_" + dataset + ".root", "read")

    effA = inputFile.Get(triggerA + "_" + leg)
    effB = inputFile.Get(triggerB + "_" + leg)

    SetStyle(effA)
    SetStyle(effB)
    effB.SetLineColor(600)
    effB.SetMarkerColor(600)

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
    effA.Draw("CP same")
    effB.Draw("CP same")
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
                firstLine = triggerA.split("_")[0] + "_" + triggerA.split("_")[1] + "_"
                pt_leg.AddText(firstLine)
                secondLine = ""
                for line in triggerA.split("_")[2:-1]:
                    secondLine += line + "_"
                secondLine += triggerA.split("_")[-1] + "*"
                pt_leg.AddText(secondLine)
            else:
                pt_leg.AddText(triggerA + "* vs")
                pt_leg.AddText(triggerB + "*")
    pt_leg.Draw("same")

    dataLabel = '2015 data'
    if '2016BC' in dataset:
        dataLabel = '2016 B+C data'
    if '2016DEFGH' in dataset:
        dataLabel = '2016 D-H data'
    if '2017' in dataset:
        dataLabel = '2017 data'
    if '2018' in dataset:
        dataLabel = '2018 data'

    legendLabel = ""

    legend = TLegend(0.65, 0.75, 0.93, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
    if leg == 'METLeg':
        legend.SetHeader('MET Leg')
    elif leg == 'TrackLeg':
        legend.SetHeader('Track Leg')
    legend.AddEntry(effA, triggerA, 'P')
    legend.AddEntry(effB, triggerB, 'P')
    legend.Draw("same")

    outputDirectory = 'plots_compare'
    if 'BC' in dataset:
        outputDirectory = 'plots_compareBC'
    if 'DEFGH' in dataset:
        outputDirectory = 'plots_compareDEFGH'

    if not os.path.exists(outputDirectory):
        os.mkdir(outputDirectory)

    canvas.SaveAs(outputDirectory + '/' + triggerA + '_vs_' + triggerB + '_' + leg + '.pdf')

    inputFile.Close()

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
    _tgraphSuffix = None

    def __init__(self, path, metHLTFilters, leg):
        self._path = path
        self._metHLTFilters = metHLTFilters
        self._leg = leg

    def addTFile(self, fout, nameSuffix = None):
        self._fout = fout
        if nameSuffix is not None:
            self._tgraphSuffix = nameSuffix

    def addTCanvas(self, canvas):
        self._canvas = canvas

    def addLuminosityInInvPb(self, luminosityInInvPb):
        self._luminosityInInvFb = luminosityInInvPb / 1000.0
        self._luminosityLabel = "{:.2f}".format(self._luminosityInInvFb) + " fb^{-1}, 13.6 TeV"

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

    def PlotFit(self, efficiencyGraph):
        fitFunc = TF1("fitFunc0", normCDF, xlo, xhi, 2)
        fitFunc.SetParName(0, "#mu")
        fitFunc.SetParameter(0, 100.0)
        fitFunc.SetParLimits(0, xlo, xhi)
        fitFunc.SetParName(1, "#sigma")
        fitFunc.SetParameter(1, 25.0)
        fitFunc.SetParLimits(1, 0.01, xhi - xlo)

        efficiencyGraph.Fit(fitFunc, "emr0")

        fitText = TPaveText(0.159148,0.689055,0.342105,0.774876,"brNDC")
        fitText.SetBorderSize(0)
        fitText.SetFillStyle(0)
        fitText.SetTextFont(42)
        fitText.SetTextSize(0.0349127)
        fitText.SetTextAlign(12)
        fitText.AddText("#mu: ({0:.3f} #pm {1:.2f}) GeV".format(fitFunc.GetParameter(0), fitFunc.GetParError(0)))
        fitText.AddText("#sigma: ({0:.3f} #pm {1:.2f}) GeV".format(fitFunc.GetParameter(1), fitFunc.GetParError(1)))

        return (fitFunc, fitText)

    def plotEfficiency(self, doFit = False):
        if hasattr(self, "Denominator") and hasattr(self, "Numerator"):
            if self._rebinFactor != 1:
                self.Denominator["hist"].Rebin(self._rebinFactor)
                self.Numerator["hist"].Rebin(self._rebinFactor)
		
            for ibin in range(-1, self.Numerator["hist"].GetNbinsX()+1):
                if self.Numerator["hist"].GetBinContent(ibin+1) > self.Denominator["hist"].GetBinContent(ibin+1):
                    print('Fixing bad bin:', (ibin+1))
                    self.Numerator["hist"].SetBinContent(ibin+1, self.Denominator["hist"].GetBinContent(ibin+1))
                    self.Numerator["hist"].SetBinError(ibin+1, self.Denominator["hist"].GetBinError(ibin+1))

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

            if doFit:
                (fitFunc, fitText) = self.PlotFit(efficiencyGraph)
                fitFunc.Draw("same")
                fitText.Draw("same")

            if not os.path.exists('plots_' + self.Denominator["sample"]):
                os.mkdir('plots_' + self.Denominator["sample"])

            if self._leg == "METPath":
                self._canvas.SaveAs('plots_' + self.Denominator["sample"] + '/' + self._path + "_Efficiency.pdf")
            else:
                self._canvas.SaveAs('plots_' + self.Denominator["sample"] + '/' + self._path + "_" + self._leg + ".pdf")
            self._fout.cd()
            if self._tgraphSuffix is not None:
                efficiencyGraph.Write(self._path + "_" + self._leg + "_" + self._tgraphSuffix)
                if doFit:
                    fitFunc.Write(self._path + "_" + self._leg + "_" + self._tgraphSuffix + "_fitResult")
            else:
                efficiencyGraph.Write(self._path + "_" + self._leg)
                if doFit:
                    fitFunc.Write(self._path + "_" + self._leg + "_fitResult")

        else:
            print("Denominator and Numerator must be defined for path ", self._path, ", leg ", self._leg)
            return 0.0
