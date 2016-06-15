#!/usr/bin/env python
import os
import sys
import math

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText

from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.tdrstyle import *
setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

def setStyle(h):
    h.SetLineColor(1)
    h.SetLineStyle(1)
    h.SetLineWidth(1)
    h.SetMarkerColor(1)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.0)
    h.SetTitle("")

def setAxisStyle(h, xTitle = "", yTitle = "", xRange = (0, 0), yRange = (0, 0)):
    h.GetXaxis().SetLabelOffset(0.005)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetXaxis().SetTitleOffset(1.0)
    h.GetXaxis().SetTitleSize(0.04)
    if xTitle is not "":
        h.GetXaxis().SetTitle(xTitle)
    if xRange[0] != 0 or xRange[1] != 0:
        h.GetXaxis().SetRangeUser(xRange[0], xRange[1])
    h.GetYaxis().SetLabelOffset(0.005)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleSize(0.04)
    if yTitle is not "":
        h.GetYaxis().SetTitle(yTitle)
    if yRange[0] != 0 or yRange[1] != 0:
        h.GetYaxis().SetRangeUser(yRange[0], yRange[1])

class LeptonBkgdClosureTest:
    _Flavor = ""
    _flavor = ""
    _fout = None
    _canvas = None
    _metCut = 0.0

    def __init__ (self, flavor):
        self._flavor = flavor.lower ()
        self._Flavor = self._flavor[0].upper () + self._flavor[1:]

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addMetCut (self, metCut):
        self._metCut = metCut

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printSingleLeptonTriggerEff (self):
        if hasattr (self, "TagPt35") and hasattr (self, "TagPt35NoTrig"):
            total = getattr (self, "TagPt35NoTrig")["yield"]
            totalError = getattr (self, "TagPt35NoTrig")["yieldError"]
            passes = getattr (self, "TagPt35")["yield"]
            passesError = getattr (self, "TagPt35")["yieldError"]

            eff = passes / total
            effError = math.sqrt (total * total * passesError * passesError + passes * passes * totalError * totalError) / (total * total)
            print "efficiency of single lepton trigger after offline selection: " + str (eff) + " +- " + str (effError)
            return (eff, effError)
        else:
            print "TagPt35 and TagPt35NoTrig not both defined. Not printing single lepton trigger efficiency..."
            return (float ("nan"), float ("nan"))

    def printNctrl (self):
        metMinusOne = self.plotMetForNctrl ()
        if hasattr (self, "TagPt35"):
            n = getattr (self, "TagPt35")["yield"]
            nError = getattr (self, "TagPt35")["yieldError"]
            print "N_ctrl: " + str (n) + " +- " + str (nError)
            return (n, nError, metMinusOne)
        else:
            print "TagPt35 not defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"))

    def plotMetForNctrl (self):
        if hasattr (self, "TagPt35"):
            if self._fout and self._canvas:
                sample = getattr (self, "TagPt35")["sample"]
                condorDir = getattr (self, "TagPt35")["condorDir"]
                name = getattr (self, "TagPt35")["name"]
                hist = "Met Plots/metNoMu"
                met = getHist (sample, condorDir, name + "Plotter", hist)
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHist (sample, condorDir, name + "Plotter", hist)

                pt = TPaveText(0.702261,0.816062,0.908291,0.869171,"brNDC")
                pt.SetBorderSize(0)
                pt.SetFillStyle(0)
                pt.SetTextFont(42)
                pt.SetTextSize(0.0388601)
                pt.AddText("use for N_{ctrl}")

                setStyle (met)
                setAxisStyle (met)
                self._canvas.cd ()
                met.Draw ()
                pt.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metForNctrl")

                setStyle (metMinusOne)
                setAxisStyle (metMinusOne)
                self._canvas.cd ()
                metMinusOne.Draw ()
                pt.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metMinusOneForNctrl")

                return metMinusOne
            else:
                print "A TFile and TCanvas must be added. Not making plots..."
                return None
        else:
            print "TagPt35 not defined. Not plotting MET for N_ctrl..."
            return None

    def printPpassVeto (self):
        if hasattr (self, "TagPt35") and hasattr (self, "CandTrkIdPt35NoMet"):
            total = getattr (self, "TagPt35")["yield"]
            totalError = getattr (self, "TagPt35")["yieldError"]
            passes = getattr (self, "CandTrkIdPt35NoMet")["yield"]
            passesError = getattr (self, "CandTrkIdPt35NoMet")["yieldError"]

            eff = passes / total
            effError = math.sqrt (total * total * passesError * passesError + passes * passes * totalError * totalError) / (total * total)
            print "P (pass lepton veto): " + str (eff) + " +- " + str (effError)
            return (eff, effError)
        else:
            print "TagPt35 and CandTrkIdPt35NoMet not both defined. Not printing P (pass lepton veto)..."
            return (float ("nan"), float ("nan"))

    def printPpassMetCut (self):
        if hasattr (self, "TagPt35"):
            total = getattr (self, "TagPt35")["yield"]
            totalError = getattr (self, "TagPt35")["yieldError"]
            passes = 0.0
            passesError = 0.0

            if hasattr (self, "TagPt35MetCut"):
                passes = getattr (self, "TagPt35MetCut")["yield"]
                passesError = getattr (self, "TagPt35MetCut")["yieldError"]
            else:
                sample = getattr (self, "TagPt35")["sample"]
                condorDir = getattr (self, "TagPt35")["condorDir"]
                name = getattr (self, "TagPt35")["name"]
                hist = "Met Plots/metNoMu"
                met = getHist (sample, condorDir, name + "Plotter", hist)

                passesError = Double (0.0)
                passes = met.IntegralAndError (met.FindBin (self._metCut), met.GetNbinsX () + 1, passesError)

            eff = passes / total
            effError = math.sqrt (total * total * passesError * passesError + passes * passes * totalError * totalError) / (total * total)
            print "P (pass met cut): " + str (eff) + " +- " + str (effError)
            return (eff, effError)
        else:
            print "TagPt35 not defined. Not printing P (pass met cut)..."
            return (float ("nan"), float ("nan"))

    def printPpassMetTriggers (self):
        if hasattr (self, "TagPt35") and hasattr (self, "TagPt35MetTrig"):
            sample = getattr (self, "TagPt35")["sample"]
            condorDir = getattr (self, "TagPt35")["condorDir"]
            name = getattr (self, "TagPt35")["name"]
            hist = "Met Plots/metNoMu"
            totalHist = getHist (sample, condorDir, name + "Plotter", hist)

            sample = getattr (self, "TagPt35MetTrig")["sample"]
            condorDir = getattr (self, "TagPt35MetTrig")["condorDir"]
            name = getattr (self, "TagPt35MetTrig")["name"]
            hist = "Met Plots/metNoMu"
            passesHist = getHist (sample, condorDir, name + "Plotter", hist)

            self.plotTriggerEfficiency (passesHist, totalHist)

            sample = getattr (self, "TagPt35")["sample"]
            condorDir = getattr (self, "TagPt35")["condorDir"]
            name = getattr (self, "TagPt35")["name"]
            hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
            metHist = getHist (sample, condorDir, name + "Plotter", hist)

            passesHist.Divide (totalHist)
            metHist.Multiply (passesHist)

            total = 0.0
            totalError = 0.0
            passesError = Double (0.0)
            passes = metHist.IntegralAndError (metHist.FindBin (self._metCut), metHist.GetNbinsX (), passesError)

            if hasattr (self, "TagPt35MetCut"):
                total = getattr (self, "TagPt35MetCut")["yield"]
                totalError = getattr (self, "TagPt35MetCut")["yieldError"]
            else:
                sample = getattr (self, "TagPt35")["sample"]
                condorDir = getattr (self, "TagPt35")["condorDir"]
                name = getattr (self, "TagPt35")["name"]
                hist = "Met Plots/metNoMu"
                met = getHist (sample, condorDir, name + "Plotter", hist)

                totalError = Double (0.0)
                total = met.IntegralAndError (met.FindBin (self._metCut), met.GetNbinsX () + 1, totalError)

            eff = passes / total
            effError = math.sqrt (total * total * passesError * passesError + passes * passes * totalError * totalError) / (total * total)
            print "P (pass met triggers): " + str (eff) + " +- " + str (effError)
            return (eff, effError, passesHist)
        else:
            print "TagPt35 and TagPt35MetTrig not both defined. Not printing P (pass met triggers)..."
            return (float ("nan"), float ("nan"))

    def plotTriggerEfficiency (self, passesHist, totalHist):
        if self._fout and self._canvas:
            metGraph = TGraphAsymmErrors (passesHist, totalHist)

            pt = TPaveText(0.190955,0.806995,0.658292,0.88601,"brNDC")
            pt.SetBorderSize(0)
            pt.SetFillStyle(0)
            pt.SetTextFont(42)
            pt.SetTextSize(0.0388601)
            pt.AddText("use for P(pass E_{T}^{miss} triggers)")

            setStyle (metGraph)
            self._canvas.cd ()
            metGraph.Draw ("ap")
            setAxisStyle (metGraph, "E_{T}^{miss} excluding muons [GeV]", "trigger efficiency", (0.0, 500.0), (0.0, 1.4))
            pt.Draw ("same")
            self._fout.cd ()
            self._canvas.Write ("triggerEfficiency")
        else:
            print "A TFile and TCanvas must be added. Not making plots..."

    def printNback (self):
        self.plotMetForNback ()
        if hasattr (self, "CandTrkIdPt35"):
            n = getattr (self, "CandTrkIdPt35")["yield"]
            nError = getattr (self, "CandTrkIdPt35")["yieldError"]
            if not (n == 0.0):
                print "N_back: " + str (n) + " +- " + str (nError)
            else:
                nUpperLimit = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1)) * getattr (self, "CandTrkIdPt35")["weight"]
                print "N_back: " + str (n) + " - 0.0 + " + str (nUpperLimit)
        else:
            print "CandTrkIdPt35 not defined. Not printing N_back..."

    def plotMetForNback (self):
        if hasattr (self, "CandTrkIdPt35"):
            if self._fout and self._canvas:
                sample = getattr (self, "CandTrkIdPt35")["sample"]
                condorDir = getattr (self, "CandTrkIdPt35")["condorDir"]
                name = getattr (self, "CandTrkIdPt35")["name"]
                hist = "Met Plots/metNoMu"
                met = getHist (sample, condorDir, name + "Plotter", hist)
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHist (sample, condorDir, name + "Plotter", hist)

                pt = TPaveText(0.702261,0.816062,0.908291,0.869171,"brNDC")
                pt.SetBorderSize(0)
                pt.SetFillStyle(0)
                pt.SetTextFont(42)
                pt.SetTextSize(0.0388601)
                pt.AddText("use for N_{back}")

                setStyle (met)
                setAxisStyle (met)
                self._canvas.cd ()
                met.Draw ()
                pt.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metForNback")

                setStyle (metMinusOne)
                setAxisStyle (metMinusOne)
                self._canvas.cd ()
                metMinusOne.Draw ()
                pt.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metMinusOneForNback")
            else:
                print "A TFile and TCanvas must be added. Not making plots..."
        else:
            print "CandTrkIdPt35 not defined. Not plotting MET for N_back..."

    def printNest (self):
        nCtrl,             nCtrlError,             metMinusOne        =                      self.printNctrl             ()
        pPassVeto,         pPassVetoError                             =                      self.printPpassVeto         ()
        pPassMetCut,       pPassMetCutError                           =                      self.printPpassMetCut       ()
        pPassMetTriggers,  pPassMetTriggersError,  triggerEfficiency  =                      self.printPpassMetTriggers  ()

        self.plotMetForNest (metMinusOne, (pPassVeto, pPassVetoError), (pPassMetCut, pPassMetCutError), triggerEfficiency)

        nEst = nCtrl * pPassVeto * pPassMetCut * pPassMetTriggers
        nEstError = 0.0
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pPassVeto       *  pPassMetCut       *  pPassMetTriggersError)
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pPassVeto       *  pPassMetCutError  *  pPassMetTriggers)
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pPassVetoError  *  pPassMetCut       *  pPassMetTriggers)
        nEstError  =  math.hypot  (nEstError,  nCtrlError  *  pPassVeto       *  pPassMetCut       *  pPassMetTriggers)

        print "N_est: " + str (nEst) + " +- " + str (nEstError)
        return (nEst, nEstError)

    def plotMetForNest (self, metMinusOne, (pPassVeto, pPassVetoError), (pPassMetCut, pPassMetCutError), triggerEfficiency):
        if self._fout and self._canvas:
            metMinusOne.Multiply (triggerEfficiency)
            for i in range (0, metMinusOne.GetNbinsX () + 1):
                content = metMinusOne.GetBinContent (i)
                error = metMinusOne.GetBinError (i)
                upperEdge = metMinusOne.GetBinLowEdge (i) + metMinusOne.GetBinWidth (i)

                newContent = content * pPassVeto if self._metCut < upperEdge else 0.0
                newError = error * pPassVeto if self._metCut < upperEdge else 0.0

                metMinusOne.SetBinContent (i, newContent)
                metMinusOne.SetBinError (i, newError)

            pt = TPaveText(0.702261,0.816062,0.908291,0.869171,"brNDC")
            pt.SetBorderSize(0)
            pt.SetFillStyle(0)
            pt.SetTextFont(42)
            pt.SetTextSize(0.0388601)
            pt.AddText("use for N_{est}")

            setStyle (metMinusOne)
            setAxisStyle (metMinusOne)
            self._canvas.cd ()
            metMinusOne.Draw ()
            pt.Draw ("same")
            self._fout.cd ()
            self._canvas.Write ("metMinusOneForNest")
        else:
            print "A TFile and TCanvas must be added. Not making plots..."

