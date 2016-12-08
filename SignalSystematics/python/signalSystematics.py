#!/usr/bin/env python
import os
import sys
import math
import copy

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

# defines a base class simply comparing the yields between central and up/down channels
class YieldSystematic:

    def __init__ (self, masses, lifetimes):
        self._masses = masses
        self._lifetimes = lifetimes

        self._integrateHistogram = "Met Plots/metNoMu"
        self._fout = ""
        self._doFout = False
        self._extraSamples = {}

        self._systematic = []
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0

    def addChannel (self, role, name, suffix, condorDir):
        channel = {"name" : name, "suffix" : suffix, "condorDir" : condorDir}
        setattr (self, role, channel)

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addFout (self, fout):
        self._fout = fout
        self._doFout = True

    def addExtraSamples (self, extraSamples):
        self._extraSamples = extraSamples

    def printSampleSystematic (self, mass, lifetime):
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.down["suffix"]
            condorDir = self.down["condorDir"]
            name = self.down["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            down = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.up["suffix"]
            condorDir = self.up["condorDir"]
            name = self.up["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            up = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)
        else:
            print "central, down, and up not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):

        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime)
                self._systematic.append ([sample, str (1.0 + relDiffDown), str (1.0 + relDiffUp)])

                if abs (relDiffDown) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffUp)

                self._averageSystematic += abs (relDiffDown)
                self._averageSystematic += abs (relDiffUp)
                self._n += 2
        self._averageSystematic /= self._n

        print "maximum systematic: " + str (self._maxSystematic * 100.0) + "%"
        print "average systematic: " + str (self._averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in self._systematic for word in row) + 2
            for row in self._systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class TriggerSystematic(YieldSystematic):

    def __init__ (self, masses, lifetimes):
        YieldSystematic.__init__ (self, masses, lifetimes)
        self._fluctuations = []
        self._foutPrefix = ""
        self._foutSuffix = ""

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nTriggerSystematics = 0

    def addTriggerFluctuations (self, triggerFluctuations):
        self._fluctuations = triggerFluctuations

    def setFoutNames (self, prefix, suffix):
        self._foutPrefix = prefix
        self._foutSuffix = suffix
        self._doFout = True

    def printSampleSystematic (self, mass, lifetime, fluctuation):
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral ()

            metHist = getHist (sample, condorDir, name + "Plotter_" + fluctuation + "Down", self._integrateHistogram)
            down = metHist.Integral ()

            metHist = getHist (sample, condorDir, name + "Plotter_" + fluctuation + "Up", self._integrateHistogram)
            up = metHist.Integral ()

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)

        else:
            print "central, down, and up not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nTriggerSystematics = 0

        for fluctuation in self._fluctuations:
            self._systematic = []
            self._maxSystematic = 0.0
            self._averageSystematic = 0.0
            self._n = 0
            for mass in self._masses:
                for lifetime in self._lifetimes:
                    sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime, fluctuation)
                    self._systematic.append ([sample, str (1.0 + relDiffDown), str (1.0 + relDiffUp)])

                    if abs(relDiffDown) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffDown)
                    if abs (relDiffUp) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffUp)

                    if abs(relDiffDown) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffDown)
                    if abs(relDiffUp) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffUp)

                    self._averageSystematic += abs (relDiffDown)
                    self._averageSystematic += abs (relDiffUp)
                    self._n += 2

                    self._overallAverageSystematic += abs (relDiffDown)
                    self._overallAverageSystematic += abs (relDiffUp)
                    self._nTriggerSystematics += 2

            self._averageSystematic /= self._n

            print "maximum %s systematic: %f%%" % (fluctuation, self._maxSystematic * 100.0)
            print "average %s systematic: %f%%" % (fluctuation, self._averageSystematic * 100.0)

            if self._doFout:
                fout = open(self._foutPrefix + fluctuation + "_" + self._foutSuffix, "w")
                width = max (len (word) for row in self._systematic for word in row) + 2
                for row in self._systematic:
                    if row[0] in self._extraSamples:
                        extraRow = copy.deepcopy (row)
                        for sample in self._extraSamples[row[0]]:
                            extraRow[0] = sample
                            fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                    fout.write ("".join (word.ljust (width) for word in row) + "\n")

                fout.close ()

        self._overallAverageSystematic /= self._nTriggerSystematics

        print "\n"
        print "maximum trigger systematic (all types): %f%%" % (self._overallMaxSystematic * 100.0)
        print "average trigger systematic (all types): %f%%" % (self._overallAverageSystematic * 100.0)

class MetSystematic(YieldSystematic):

    def __init__ (self, masses, lifetimes):
        YieldSystematic.__init__ (self, masses, lifetimes)
        self._metCut = 100.0
        self._metTypes = []
        self._foutPrefix = ""
        self._foutSuffix = ""

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nMetSystematics = 0

    def addMetTypes (self, metTypes):
        self._metTypes = metTypes

    def setMetCut (self, metCut):
        self._metCut = metCut

    def setFoutNames (self, prefix, suffix):
        self._foutPrefix = prefix
        self._foutSuffix = suffix
        self._doFout = True

    def printSampleSystematic (self, mass, lifetime, metType):
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            central = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram + "_" + metType + "Down")
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            down = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram + "_" + metType + "Up")
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            up = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)

        else:
            print "central, down, and up not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nMetSystematics = 0

        for metType in self._metTypes:
            self._systematic = []
            self._maxSystematic = 0.0
            self._averageSystematic = 0.0
            self._n = 0
            for mass in self._masses:
                for lifetime in self._lifetimes:
                    sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime, metType)
                    self._systematic.append ([sample, str (1.0 + relDiffDown), str (1.0 + relDiffUp)])

                    if abs(relDiffDown) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffDown)
                    if abs (relDiffUp) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffUp)

                    if abs(relDiffDown) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffDown)
                    if abs(relDiffUp) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffUp)

                    self._averageSystematic += abs (relDiffDown)
                    self._averageSystematic += abs (relDiffUp)
                    self._n += 2

                    self._overallAverageSystematic += abs (relDiffDown)
                    self._overallAverageSystematic += abs (relDiffUp)
                    self._nMetSystematics += 2

            self._averageSystematic /= self._n

            print "maximum %s systematic: %f%%" % (metType, self._maxSystematic * 100.0)
            print "average %s systematic: %f%%" % (metType, self._averageSystematic * 100.0)

            if self._doFout:
                fout = open(self._foutPrefix + metType + "_" + self._foutSuffix, "w")
                width = max (len (word) for row in self._systematic for word in row) + 2
                for row in self._systematic:
                    if row[0] in self._extraSamples:
                        extraRow = copy.deepcopy (row)
                        for sample in self._extraSamples[row[0]]:
                            extraRow[0] = sample
                            fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                    fout.write ("".join (word.ljust (width) for word in row) + "\n")

                fout.close ()

        self._overallAverageSystematic /= self._nMetSystematics

        print "\n"
        print "maximum met systematic (all types): %f%%" % (self._overallMaxSystematic * 100.0)
        print "average met systematic (all types): %f%%" % (self._overallAverageSystematic * 100.0)

class PileupSystematic:

    _integrateHistogram = "Met Plots/metNoMu"
    _masses = []
    _lifetimes = []
    _fout = ""
    _extraSamples = {}

    def addChannel (self, role, name, suffix, condorDir):
        channel = {"name" : name, "suffix" : suffix, "condorDir" : condorDir}
        setattr (self, role, channel)

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addMasses (self, masses):
        self._masses = masses

    def addLifetimes (self, lifetimes):
        self._lifetimes = lifetimes

    def addFout (self, fout):
        self._fout = fout

    def addExtraSamples (self, extraSamples):
        self._extraSamples = extraSamples

    def __init__ (self, masses, lifetimes):
        self.addMasses (masses)
        self.addLifetimes (lifetimes)

    def printPileupSystematic (self, mass, lifetime):
        if hasattr (self, "PileupCentral") and hasattr (self, "PileupDown") and hasattr (self, "PileupUp"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupCentral["suffix"]
            condorDir = self.PileupCentral["condorDir"]
            name = self.PileupCentral["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupDown["suffix"]
            condorDir = self.PileupDown["condorDir"]
            name = self.PileupDown["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            down = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupUp["suffix"]
            condorDir = self.PileupUp["condorDir"]
            name = self.PileupUp["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            up = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(" + sample + ") down: " + str (down) + ", central: " + str (central) + ", up: " + str (up) + ", systematic uncertainty: " + str (relDiffDown * 100.0) + "%/" + str (relDiffUp * 100.0) + "%"
            return (sample, relDiffDown, relDiffUp)
        else:
            print "PileupCentral, PileupDown, and PileupUp not all defined. Not printing pileup systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        systematic = []
        maxSystematic = 0.0
        averageSystematic = 0.0
        n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printPileupSystematic (mass, lifetime)
                systematic.append ([sample, str (1.0 + relDiffDown), str (1.0 + relDiffUp)])

                if abs (relDiffDown) > maxSystematic:
                  maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > maxSystematic:
                  maxSystematic = abs (relDiffUp)

                averageSystematic += abs (relDiffDown)
                averageSystematic += abs (relDiffUp)
                n += 2
        averageSystematic /= n

        print "maximum systematic: " + str (maxSystematic * 100.0) + "%"
        print "average systematic: " + str (averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in systematic for word in row) + 2
            for row in systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class ECaloSystematic:

    _integrateHistogram = "Track Plots/trackCaloTot_RhoCorr"

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def printECaloSystematic (self, dataOrMC = "Data"):
        if hasattr (self, dataOrMC):
            channel = getattr (self, dataOrMC)
            sample = channel["sample"]
            condorDir = channel["condorDir"]
            name = channel["name"]
            ecalo = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = ecalo.IntegralAndError (0, ecalo.FindBin (10.0) - 1, passesError)
            total = ecalo.IntegralAndError (0, ecalo.GetNbinsX () + 1, totalError)

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)

            print "efficiency of ECalo cut in " + dataOrMC + ": " + str (eff) + " - " + str (effErrorLow) + " + " + str (effErrorHigh)
            return (eff, effErrorLow, effErrorHigh)
        else:
            print dataOrMC + " not defined. Not printing ECalo systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        data, dataErrorLow, dataErrorHigh = self.printECaloSystematic ("Data")
        mc, mcErrorLow, mcErrorHigh = self.printECaloSystematic ("MC")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%"

class HitsSystematic:

    _integrateHistogram = "Track Plots/trackNHitsMissingMiddleVsInner"

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def printHitsSystematic (self, dataOrMC = "Data", xOrY = "XY"):
        if hasattr (self, dataOrMC):
            channel = getattr (self, dataOrMC)
            sample = channel["sample"]
            condorDir = channel["condorDir"]
            name = channel["name"]
            hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = 0.0
            total = hits.IntegralAndError (0, hits.GetNbinsX () + 1, 0, hits.GetNbinsY () + 1, totalError)
            label = ""
            if xOrY == "XY":
                passes = hits.IntegralAndError (0, hits.GetXaxis ().FindBin (0.0), 0, hits.GetYaxis ().FindBin (0.0), passesError)
                label = "combined"
            elif xOrY == "X":
                passes = hits.IntegralAndError (0, hits.GetXaxis ().FindBin (0.0), 0, hits.GetNbinsY () + 1, passesError)
                label = hits.GetXaxis ().GetTitle ()
            elif xOrY == "Y":
                passes = hits.IntegralAndError (0, hits.GetNbinsX () + 1, 0, hits.GetYaxis ().FindBin (0.0), passesError)
                label = hits.GetYaxis ().GetTitle ()

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)

            print "efficiency of " + label + " cut in " + dataOrMC + ": " + str (eff) + " - " + str (effErrorLow) + " + " + str (effErrorHigh)
            return (eff, effErrorLow, effErrorHigh)
        else:
            print dataOrMC + " not defined. Not printing hits systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        data, dataErrorLow, dataErrorHigh = self.printHitsSystematic ("Data", "X")
        mc, mcErrorLow, mcErrorHigh = self.printHitsSystematic ("MC", "X")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%\n"

        data, dataErrorLow, dataErrorHigh = self.printHitsSystematic ("Data", "Y")
        mc, mcErrorLow, mcErrorHigh = self.printHitsSystematic ("MC", "Y")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%\n"

        data, dataErrorLow, dataErrorHigh = self.printHitsSystematic ("Data")
        mc, mcErrorLow, mcErrorHigh = self.printHitsSystematic ("MC")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%"

class MissingOuterHitsSystematic:

    _integrateHistogram = "Track Plots/trackNHitsMissingOuterCorrected"
    _fout = ""

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def printMissingOuterHitsSystematic (self, dataOrMC = "Data"):
        if hasattr (self, dataOrMC):
            channel = getattr (self, dataOrMC)
            sample = channel["sample"]
            condorDir = channel["condorDir"]
            name = channel["name"]
            hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = hits.IntegralAndError (hits.FindBin (1), hits.GetNbinsX () + 1, totalError)
            total = hits.IntegralAndError (0, hits.GetNbinsX () + 1, totalError)

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)

            print "rate of accidental missing outer hits in " + dataOrMC + ": " + str (eff) + " - " + str (effErrorLow) + " + " + str (effErrorHigh)
            return (eff, effErrorLow, effErrorHigh)
        else:
            print dataOrMC + " not defined. Not printing missing outer hits systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        data, dataErrorLow, dataErrorHigh = self.printMissingOuterHitsSystematic ("Data")
        mc, mcErrorLow, mcErrorHigh = self.printMissingOuterHitsSystematic ("MC")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%"