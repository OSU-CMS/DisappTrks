#!/usr/bin/env python
import os
import sys
import math

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText, TObject, TLine

from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.tdrstyle import *
setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

def setStyle(h, color = 1):
    h.SetLineColor(color)
    h.SetLineStyle(1)
    h.SetLineWidth(2)
    h.SetMarkerColor(color)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.5)
    h.SetTitle("")

def setCanvasStyle(canvas):
    canvas.SetHighLightColor(2)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetBorderSize(2)
    canvas.SetTickx(1)
    canvas.SetTicky(1)
    canvas.SetLeftMargin(0.128141)
    canvas.SetRightMargin(0.0414573)
    canvas.SetBottomMargin(0.0971503)
    canvas.SetTopMargin(0.0712435)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)


def setAxisStyle(h, xTitle = "", yTitle = "", xRange = (0, 0), yRange = (0, 0)):
    h.GetXaxis().SetNdivisions(505)
    h.GetXaxis().SetLabelOffset(0.005)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetXaxis().SetTitleOffset(1.0)
    h.GetXaxis().SetTitleSize(0.04)
    if xTitle is not "":
        h.GetXaxis().SetTitle(xTitle)
    if xRange[0] != 0 or xRange[1] != 0:
        h.GetXaxis().SetRangeUser(xRange[0], xRange[1])
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetLabelOffset(0.005)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleSize(0.04)
    if yTitle is not "":
        h.GetYaxis().SetTitle(yTitle)
    if yRange[0] != 0 or yRange[1] != 0:
        h.GetYaxis().SetRangeUser(yRange[0], yRange[1])

class FakeTrackSystematic:
    _fout = None
    _canvas = None
    _luminosityLabel = "13 TeV"

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addLuminosityLabel (self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printFakeRateRatio (self, nHits):
        if hasattr (self, "Basic") and hasattr (self, "ZtoMuMu") and hasattr (self, "DisTrkNHits" + str (nHits)) and hasattr (self, "ZtoMuMuDisTrkNHits" + str (nHits)):
            disTrkNHits = getattr (self, "DisTrkNHits" + str (nHits))
            zToMuMuDisTrkNHits = getattr (self, "ZtoMuMuDisTrkNHits" + str (nHits))

            total = (self.Basic["yield"], self.ZtoMuMu["yield"])
            totalError = (self.Basic["yieldError"], self.ZtoMuMu["yieldError"])
            passes = (disTrkNHits["yield"], zToMuMuDisTrkNHits["yield"])
            passesError = (disTrkNHits["yieldError"], zToMuMuDisTrkNHits["yieldError"])

            fakeRate = (passes[0] / total[0], passes[1] / total[1])
            fakeRateError = (math.hypot ((passes[0] * totalError[0]) / (total[0] * total[0]), (passesError[0] * total[0]) / (total[0] * total[0])), math.hypot ((passes[1] * totalError[1]) / (total[1] * total[1]), (passesError[1] * total[1]) / (total[1] * total[1])))
            ratio = fakeRate[1] / fakeRate[0]
            ratioError = math.hypot ((fakeRate[0] * fakeRateError[1]) / (fakeRate[0] * fakeRate[0]), (fakeRateError[0] * fakeRate[1]) / (fakeRate[0] * fakeRate[0]))

            print "nHits: " + str (nHits) + ", basic: " + str (fakeRate[0]) + " +- " + str (fakeRateError[0]) + ", zToMuMu: " + str (fakeRate[1]) + " +- " + str (fakeRateError[1]) + ", difference: " + str ((fakeRate[1] - fakeRate[0]) / math.hypot (fakeRateError[1], fakeRateError[0])) + " sigma, ratio: " + str (ratio) + " +- " + str (ratioError)
            return (fakeRate, fakeRateError, ratio, ratioError)
        else:
            print "Basic, ZtoMuMu, DisTrkNHits" + str (nHits) + ", and ZtoMuMuDisTrkNHits" + str (nHits) + " not all defined. Not printing fake rate ratio..."
            return (float ("nan"), float ("nan"), float ("nan"), float ("nan"))


    def printSystematic (self):
        fakeRate3, fakeRate3Error, ratio3, ratio3Error = self.printFakeRateRatio (3)
        fakeRate4, fakeRate4Error, ratio4, ratio4Error = self.printFakeRateRatio (4)
        fakeRate5, fakeRate5Error, ratio5, ratio5Error = self.printFakeRateRatio (5)
        fakeRate6, fakeRate6Error, ratio6, ratio6Error = self.printFakeRateRatio (6)

        print "systematic uncertainty: " + str ((abs (ratio5 - 1.0) + ratio5Error) * 100.0) + "%"

        basicFakeRate = TH1D ("basicFakeRate", ";number of hits", 400, 2.5, 6.5)
        zToMuMuFakeRate = TH1D ("zToMuMuFakeRate", ";number of hits", 400, 2.5, 6.5)
        ratio = TH1D ("ratio", ";number of hits", 400, 2.5, 6.5)

        basicFakeRate.SetBinContent  (basicFakeRate.FindBin  (3.0),  fakeRate3[0])
        basicFakeRate.SetBinError    (basicFakeRate.FindBin  (3.0),  fakeRate3Error[0])
        basicFakeRate.SetBinContent  (basicFakeRate.FindBin  (4.0),  fakeRate4[0])
        basicFakeRate.SetBinError    (basicFakeRate.FindBin  (4.0),  fakeRate4Error[0])
        basicFakeRate.SetBinContent  (basicFakeRate.FindBin  (5.0),  fakeRate5[0])
        basicFakeRate.SetBinError    (basicFakeRate.FindBin  (5.0),  fakeRate5Error[0])
        basicFakeRate.SetBinContent  (basicFakeRate.FindBin  (6.0),  fakeRate6[0])
        basicFakeRate.SetBinError    (basicFakeRate.FindBin  (6.0),  fakeRate6Error[0])

        zToMuMuFakeRate.SetBinContent  (zToMuMuFakeRate.FindBin  (3.0),  fakeRate3[1])
        zToMuMuFakeRate.SetBinError    (zToMuMuFakeRate.FindBin  (3.0),  fakeRate3Error[1])
        zToMuMuFakeRate.SetBinContent  (zToMuMuFakeRate.FindBin  (4.0),  fakeRate4[1])
        zToMuMuFakeRate.SetBinError    (zToMuMuFakeRate.FindBin  (4.0),  fakeRate4Error[1])
        zToMuMuFakeRate.SetBinContent  (zToMuMuFakeRate.FindBin  (5.0),  fakeRate5[1])
        zToMuMuFakeRate.SetBinError    (zToMuMuFakeRate.FindBin  (5.0),  fakeRate5Error[1])
        zToMuMuFakeRate.SetBinContent  (zToMuMuFakeRate.FindBin  (6.0),  fakeRate6[1])
        zToMuMuFakeRate.SetBinError    (zToMuMuFakeRate.FindBin  (6.0),  fakeRate6Error[1])

        ratio.SetBinContent  (ratio.FindBin  (3.0),  ratio3)
        ratio.SetBinError    (ratio.FindBin  (3.0),  ratio3Error)
        ratio.SetBinContent  (ratio.FindBin  (4.0),  ratio4)
        ratio.SetBinError    (ratio.FindBin  (4.0),  ratio4Error)
        ratio.SetBinContent  (ratio.FindBin  (5.0),  ratio5)
        ratio.SetBinError    (ratio.FindBin  (5.0),  ratio5Error)
        ratio.SetBinContent  (ratio.FindBin  (6.0),  ratio6)
        ratio.SetBinError    (ratio.FindBin  (6.0),  ratio6Error)

        cmsLabel = TPaveText(0.134085,0.937984,0.418546,0.984496,"brNDC")
        cmsLabel.SetBorderSize(0)
        cmsLabel.SetFillStyle(0)
        cmsLabel.SetTextFont(62)
        cmsLabel.SetTextSize(0.0387597)
        cmsLabel.AddText("CMS Preliminary")

        lumiLabel = TPaveText(0.66416,0.937339,0.962406,0.992894,"brNDC")
        lumiLabel.SetBorderSize(0)
        lumiLabel.SetFillStyle(0)
        lumiLabel.SetTextFont(42)
        lumiLabel.SetTextSize(0.0387597)
        lumiLabel.AddText(str (self._luminosityLabel))

        leg = TLegend(0.7550251,0.7759067,0.9459799,0.8795337)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.0388601)
        leg.SetTextFont(42)
        leg.SetLineColor(1)
        leg.SetLineStyle(1)
        leg.SetLineWidth(1)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.AddEntry (zToMuMuFakeRate, "Z#rightarrow#mu#mu", "p")
        leg.AddEntry (basicFakeRate, "basic", "p")

        setStyle (basicFakeRate, 632)
        setStyle (zToMuMuFakeRate, 600)
        setAxisStyle (basicFakeRate, yTitle = "P_{fake}")
        setAxisStyle (zToMuMuFakeRate, yTitle = "P_{fake}")
        self._canvas.cd ()
        self._canvas.SetLogy ()
        zToMuMuFakeRate.Draw ()
        basicFakeRate.Draw ("same")
        leg.Draw ("same")
        cmsLabel.Draw ("same")
        lumiLabel.Draw ("same")
        self._fout.cd ()
        self._canvas.Write ("fakeRate")

        line = TLine (2.5, 1.0, 6.5, 1.0)
        line.SetLineStyle (2)
        line.SetLineWidth (2)
        line.SetLineColor (1)

        setStyle (ratio)
        setAxisStyle (ratio, yTitle = "P_{fake}^{Z#rightarrow#mu#mu} / P_{fake}^{basic}")
        self._canvas.cd ()
        self._canvas.SetLogy (False)
        ratio.Draw ()
        line.Draw ("same")
        cmsLabel.Draw ("same")
        lumiLabel.Draw ("same")
        self._fout.cd ()
        self._canvas.Write ("fakeRateRatio")

class LeptonEnergySystematic:
    _Flavor = ""
    _flavor = ""
    _fout = None
    _canvas = None
    _metCut = 0.0
    _luminosityLabel = "13 TeV"

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addMetCut (self, metCut):
        self._metCut = metCut

    def addLuminosityLabel (self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

    def __init__ (self, flavor):
        self._flavor = flavor.lower ()
        self._Flavor = self._flavor[0].upper () + self._flavor[1:]

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printPpassMetTriggers (self, metMinusOneHist):
        if hasattr (self, "TagPt35") and (hasattr (self, "TagPt35MetTrig") or (hasattr (self, "TrigEffDenom") and hasattr (self, "TrigEffNumer"))):
            sample = self.TrigEffDenom["sample"] if hasattr (self, "TrigEffDenom") else self.TagPt35["sample"]
            condorDir = self.TrigEffDenom["condorDir"] if hasattr (self, "TrigEffDenom") else self.TagPt35["condorDir"]
            name = self.TrigEffDenom["name"] if hasattr (self, "TrigEffDenom") else self.TagPt35["name"]
            hist = "Met Plots/metNoMu"
            totalHist = getHist (sample, condorDir, name + "Plotter", hist)

            sample = self.TrigEffNumer["sample"] if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig["sample"]
            condorDir = self.TrigEffNumer["condorDir"] if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig["condorDir"]
            name = self.TrigEffNumer["name"] if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig["name"]
            hist = "Met Plots/metNoMu"
            passesHist = getHist (sample, condorDir, name + "Plotter", hist)

            sample = self.TagPt35["sample"]
            condorDir = self.TagPt35["condorDir"]
            name = self.TagPt35["name"]
            metHist = getHist (sample, condorDir, name + "Plotter", self._Flavor + " Plots/" + self._flavor + metMinusOneHist)

            passesHist.Divide (totalHist)
            metHist.Multiply (passesHist)

            total = 0.0
            totalError = Double (0.0)
            passesError = Double (0.0)
            passes = metHist.IntegralAndError (metHist.FindBin (self._metCut), metHist.GetNbinsX () + 1, passesError)

            if hasattr (self, "TagPt35MetCut"):
                total = self.TagPt35MetCut["yield"]
                totalError = self.TagPt35MetCut["yieldError"]
            else:
                sample = self.TagPt35["sample"]
                condorDir = self.TagPt35["condorDir"]
                name = self.TagPt35["name"]
                met = getHist (sample, condorDir, name + "Plotter", self._Flavor + " Plots/" + self._flavor + metMinusOneHist)

                totalError = Double (0.0)
                total = met.IntegralAndError (met.FindBin (self._metCut), met.GetNbinsX () + 1, totalError)

            eff = passes / total
            effError = math.hypot (total * passesError, totalError * passes) / (total * total)
            print "P (pass met triggers) with \"" + metMinusOneHist + "\": " + str (eff) + " +- " + str (effError)
            return (eff, effError, passesHist)
        else:
            print "TagPt35 and TagPt35MetTrig not both defined. Not printing P (pass met triggers)..."
            return (float ("nan"), float ("nan"))

    def printPpassMetCut (self, metMinusOneHist):
        if hasattr (self, "TagPt35"):
            total = self.TagPt35["yield"]
            totalError = self.TagPt35["yieldError"]
            passes = 0.0
            passesError = 0.0

            if hasattr (self, "TagPt35MetCut"):
                passes = self.TagPt35MetCut["yield"]
                passesError = self.TagPt35MetCut["yieldError"]
            else:
                sample = self.TagPt35["sample"]
                condorDir = self.TagPt35["condorDir"]
                name = self.TagPt35["name"]
                met = getHist (sample, condorDir, name + "Plotter", self._Flavor + " Plots/" + self._flavor + metMinusOneHist)

                passesError = Double (0.0)
                passes = met.IntegralAndError (met.FindBin (self._metCut), met.GetNbinsX () + 1, passesError)

            eff = passes / total
            effError = math.hypot (total * passesError, totalError * passes) / (total * total)
            print "P (pass met cut) with \"" + metMinusOneHist + "\": " + str (eff) + " +- " + str (effError)
            return (eff, effError)
        else:
            print "TagPt35 not defined. Not printing P (pass met cut)..."
            return (float ("nan"), float ("nan"))

    def printSystematic (self):
        pPassMetCut0       =  self.printPpassMetCut       ("MetNoMuMinusOnePt")
        pPassMetCut1       =  self.printPpassMetCut       ("MetNoMuMinusOneUpPt")
        pPassMetTriggers0  =  self.printPpassMetTriggers  ("MetNoMuMinusOnePt")
        pPassMetTriggers1  =  self.printPpassMetTriggers  ("MetNoMuMinusOneUpPt")

        ratio = (pPassMetCut1[0] * pPassMetTriggers1[0]) / (pPassMetCut0[0] * pPassMetTriggers0[0])
        ratioError = 0.0
        ratioError = math.hypot (ratioError, pPassMetCut0[0] * pPassMetTriggers0[0] * pPassMetCut1[0] * pPassMetTriggers1[1])
        ratioError = math.hypot (ratioError, pPassMetCut0[0] * pPassMetTriggers0[0] * pPassMetCut1[1] * pPassMetTriggers1[0])
        ratioError = math.hypot (ratioError, pPassMetCut0[0] * pPassMetTriggers0[1] * pPassMetCut1[0] * pPassMetTriggers1[0])
        ratioError = math.hypot (ratioError, pPassMetCut0[1] * pPassMetTriggers0[0] * pPassMetCut1[0] * pPassMetTriggers1[0])
        ratioError /= ((pPassMetCut0[0] * pPassMetTriggers0[0]) * (pPassMetCut0[0] * pPassMetTriggers0[0]))

        print "ratio: " + str (ratio) + " +- " + str (ratioError)

        print "systematic uncertainty: " + str ((abs (ratio - 1.0) + ratioError) * 100.0) + "%"
