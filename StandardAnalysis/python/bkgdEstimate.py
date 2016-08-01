#!/usr/bin/env python
import os
import sys
import math

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText, TObject 

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

class LeptonBkgdEstimate:
    _Flavor = ""
    _flavor = ""
    _fout = None
    _canvas = None
    _metCut = 0.0
    _pPassVeto = (float ("nan"), float ("nan"))
    _prescale = 1.0
    _metMinusOneHist = ""
    _useIdMatch = False  # match the track to get the true bkgd yield 

    def __init__ (self, flavor):
        self._flavor = flavor.lower ()
        self._Flavor = self._flavor[0].upper () + self._flavor[1:]
        self._metMinusOneHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addMetCut (self, metCut):
        self._metCut = metCut

    def useIdMatch (self, match):
        self._useIdMatch = match

    def addPpassVeto (self, (pPassVeto, pPassVetoError)):
        self._pPassVeto = (pPassVeto, pPassVetoError)

    def addPrescaleFactor (self, prescale):
        self._prescale = prescale

    def useMetMinusOneForIntegrals (self, flag = True):
        if flag:
            self._metMinusOneHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
        else:
            self._metMinusOneHist = "Met Plots/metNoMu"

    def getPdgRange(self):
        if   self._flavor == "electron":
            return 11, 11
        elif self._flavor == "muon":
            return 13, 13
        elif self._flavor == "tau":
            return 14, 40  # define tau to include everything besides electrons and muons.  Last bin value is for 38.  

    def addChannel (self, role, name, sample, condorDir, useIdMatch = False):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        if useIdMatch:
            pdgLo, pdgHi = self.getPdgRange()  
            channel["yield"], channel["yieldError"] = getHistIntegral (sample, condorDir, name + "Plotter", "Track Plots/bestMatchPdgId", pdgLo, pdgHi)  
        else: 
            channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printSingleLeptonTriggerEff (self):
        if hasattr (self, "TagPt35") and hasattr (self, "TagPt35NoTrig"):
            total = self.TagPt35NoTrig["yield"]
            totalError = self.TagPt35NoTrig["yieldError"]
            passes = self.TagPt35["yield"]
            passesError = self.TagPt35["yieldError"]

            eff = passes / total
            effError = math.hypot (total * passesError, totalError * passes) / (total * total)
            print "efficiency of single lepton trigger after offline selection: " + str (eff) + " +- " + str (effError)
            return (eff, effError)
        else:
            print "TagPt35 and TagPt35NoTrig not both defined. Not printing single lepton trigger efficiency..."
            return (float ("nan"), float ("nan"))

    def printNctrl (self):
        metMinusOne = self.plotMetForNctrl ()
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            n = self.TagPt35ForNctrl["yield"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["yield"]
            nError = self.TagPt35ForNctrl["yieldError"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["yieldError"]
            weight = self.TagPt35ForNctrl["weight"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["weight"]

            n *= self._prescale
            nError *= self._prescale
            weight *= self._prescale

            if not (n == 0.0):
                print "N_ctrl: " + str (n) + " +- " + str (nError)
                return (n, nError, metMinusOne)
            else:
                nUpperLimit = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1)) * weight
                print "N_ctrl: " + str (n) + " - 0.0 + " + str (nUpperLimit)
                return (n, nUpperLimit, metMinusOne)
        else:
            print "Neither TagPt35 nor TagPt35ForNctrl defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"))

    def plotMetForNctrl (self):
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            if self._fout and self._canvas:
                sample = self.TagPt35ForNctrl["sample"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["sample"]
                condorDir = self.TagPt35ForNctrl["condorDir"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["condorDir"]
                name = self.TagPt35ForNctrl["name"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["name"]
                hist = "Met Plots/metNoMu"
                met = getHist (sample, condorDir, name + "Plotter", hist)

                # explicitly get metNoMuMinusOne instead of using
                # _metMinusOneHist since we plot both metNoMu and
                # metNoMuMinusOne here
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHist (sample, condorDir, name + "Plotter", hist)

                metMinusOne.Scale (self._prescale)

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
            print "Neither TagPt35 nor TagPt35ForNctrl defined. Not plotting MET for N_ctrl..."
            return None

    def printPpassVeto (self):
        if math.isnan (self._pPassVeto[0]) or math.isnan (self._pPassVeto[1]):
            if hasattr (self, "TagPt35") and hasattr (self, "CandTrkIdPt35NoMet"):
                total = self.TagPt35["yield"]
                totalError = self.TagPt35["yieldError"]
                passes = self.CandTrkIdPt35NoMet["yield"]
                passesError = self.CandTrkIdPt35NoMet["yieldError"]

                eff = passes / total
                effError = math.hypot (total * passesError, totalError * passes) / (total * total)
                print "P (pass lepton veto) in baseline sample: " + str (eff) + " +- " + str (effError)
                return (eff, effError)
            else:
                print "TagPt35 and CandTrkIdPt35NoMet not both defined. Not printing P (pass lepton veto)..."
                return (float ("nan"), float ("nan"))
        else:
            print "P (pass lepton veto) from user input: " + str (self._pPassVeto[0]) + " +- " + str (self._pPassVeto[1])
            return (self._pPassVeto[0], self._pPassVeto[1])

    def printPpassVetoSystErr (self):
        if hasattr (self, "TagPt35") and hasattr (self, "CandTrkIdPt35NoMet"):
            hTotal  = getHist (self.TagPt35["sample"], self.TagPt35["condorDir"], self.TagPt35["name"] + "Plotter", "Track Plots/trackPt")
            hPasses = getHist (self.CandTrkIdPt35NoMet["sample"], self.CandTrkIdPt35NoMet["condorDir"], self.CandTrkIdPt35NoMet["name"] + "Plotter", "Track Plots/trackPt")

            ptCut = 50.0

            totalError  = Double(0.0)
            passesError = Double(0.0)
            total  =  hTotal.IntegralAndError (0,  hTotal.FindBin(ptCut),  totalError)
            passes = hPasses.IntegralAndError (0, hPasses.FindBin(ptCut), passesError)
            effLo = passes / total
            effLoError = effLo * math.hypot(passesError/passes, totalError/total) if passes else 0 # sum relative errors in quadrature
            print "P_lo (pass lepton veto) for pT < 50 GeV:    " + str (effLo) + " +- " + str (effLoError)

            total  =  hTotal.IntegralAndError ( hTotal.FindBin(ptCut),  hTotal.GetNbinsX() + 1,  totalError)
            passes = hPasses.IntegralAndError (hPasses.FindBin(ptCut), hPasses.GetNbinsX() + 1, passesError)
            effHi = passes / total
            effHiError = effHi * math.hypot(passesError/passes, totalError/total) if passes else 0 # sum relative errors in quadrature
            print "P_hi (pass lepton veto) for pT > 50 GeV:    " + str (effHi) + " +- " + str (effHiError)

            total  =  hTotal.IntegralAndError (0,  hTotal.GetNbinsX() + 1,  totalError)
            passes = hPasses.IntegralAndError (0, hPasses.GetNbinsX() + 1, passesError)
            effAll = passes / total
            effAllError = effAll * math.hypot(passesError/passes, totalError/total) if passes else 0 # sum relative errors in quadrature
            print "P_all (pass lepton veto) for all pT:        " + str (effAll) + " +- " + str (effAllError)

            systErr = (effHi - effAll) / effAll
            print "The systematic difference in lepton veto efficiency with and without the pT > 50 GeV cut is (P_hi - P_all) / P_all = ", systErr
        else:
            print "TagPt35 and CandTrkIdPt35NoMet not both defined. Not printing P (pass lepton veto)..."

    def printPpassMetCut (self):
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
                met = getHist (sample, condorDir, name + "Plotter", self._metMinusOneHist)

                passesError = Double (0.0)
                passes = met.IntegralAndError (met.FindBin (self._metCut), met.GetNbinsX () + 1, passesError)

            eff = passes / total
            effError = math.hypot (total * passesError, totalError * passes) / (total * total)
            print "P (pass met cut): " + str (eff) + " +- " + str (effError)
            return (eff, effError)
        else:
            print "TagPt35 not defined. Not printing P (pass met cut)..."
            return (float ("nan"), float ("nan"))

    def printPpassMetTriggers (self):
        if hasattr (self, "TagPt35") and hasattr (self, "TagPt35MetTrig"):
            sample = self.TagPt35["sample"]
            condorDir = self.TagPt35["condorDir"]
            name = self.TagPt35["name"]
            hist = "Met Plots/metNoMu"
            totalHist = getHist (sample, condorDir, name + "Plotter", hist)

            sample = self.TagPt35MetTrig["sample"]
            condorDir = self.TagPt35MetTrig["condorDir"]
            name = self.TagPt35MetTrig["name"]
            hist = "Met Plots/metNoMu"
            passesHist = getHist (sample, condorDir, name + "Plotter", hist)

            self.plotTriggerEfficiency (passesHist, totalHist)

            sample = self.TagPt35["sample"]
            condorDir = self.TagPt35["condorDir"]
            name = self.TagPt35["name"]
            metHist = getHist (sample, condorDir, name + "Plotter", self._metMinusOneHist)

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
                met = getHist (sample, condorDir, name + "Plotter", self._metMinusOneHist)

                totalError = Double (0.0)
                total = met.IntegralAndError (met.FindBin (self._metCut), met.GetNbinsX () + 1, totalError)

            eff = passes / total
            effError = math.hypot (total * passesError, totalError * passes) / (total * total)
            print "P (pass met triggers): " + str (eff) + " +- " + str (effError)
            return (eff, effError, passesHist)
        else:
            print "TagPt35 and TagPt35MetTrig not both defined. Not printing P (pass met triggers)..."
            return (float ("nan"), float ("nan"))

    def plotTriggerEfficiency (self, passesHist, totalHist):
        if self._fout and self._canvas:
            self.makePassesConsistentWithTotal (passesHist, totalHist)
            metGraph = TGraphAsymmErrors (passesHist, totalHist)
            metGraph.SetEditable (0)

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
            n      = self.CandTrkIdPt35["yield"]
            nError = self.CandTrkIdPt35["yieldError"]
            weight = self.CandTrkIdPt35["weight"]
            if not (n == 0.0):
                print "N_back: " + str (n) + " +- " + str (nError)
                return (n, nError)
            else:
                nUpperLimit = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1)) * weight
                print "N_back: " + str (n) + " - 0.0 + " + str (nUpperLimit)
                return (n, nUpperLimit)
        else:
            print "CandTrkIdPt35 not defined. Not printing N_back..."
            return (float ("nan"), float ("nan"))

    def plotMetForNback (self):
        if hasattr (self, "CandTrkIdPt35"):
            if self._fout and self._canvas:
                sample = self.CandTrkIdPt35["sample"]
                condorDir = self.CandTrkIdPt35["condorDir"]
                name = self.CandTrkIdPt35["name"]
                hist = "Met Plots/metNoMu"
                met         = getHist (sample, condorDir, name + "Plotter", hist)

                # explicitly get metNoMuMinusOne instead of using
                # _metMinusOneHist since we plot both metNoMu and
                # metNoMuMinusOne here
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHist (sample, condorDir, name + "Plotter", hist)
                if not isinstance(met, TObject) or not isinstance(metMinusOne, TObject):
                    print "Warning [plotMetForNback]: Could not get required hists from sample=", sample, "condorDir=", condorDir, "name=", name
                    return

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

    def makePassesConsistentWithTotal (self, passes, total):
        for i in range (0, passes.GetNbinsX () + 2):
            if passes.GetBinContent (i) > total.GetBinContent (i):
                passes.SetBinContent (i, total.GetBinContent (i))
                passes.SetBinError (i, total.GetBinError (i))

    def printNest (self):
        nCtrl,             nCtrlError,             metMinusOne        =  self.printNctrl             ()
        pPassVeto,         pPassVetoError                             =  self.printPpassVetoTagProbe ()
        pPassMetCut,       pPassMetCutError                           =  self.printPpassMetCut       ()
        pPassMetTriggers,  pPassMetTriggersError,  triggerEfficiency  =  self.printPpassMetTriggers  ()

        if math.isnan (pPassVeto) or math.isnan (pPassVetoError):
            pPassVeto, pPassVetoError = self.printPpassVeto ()

        self.plotMetForNest (metMinusOne, (pPassVeto, pPassVetoError), (pPassMetCut, pPassMetCutError), triggerEfficiency)

        N = nCtrl
        alpha = pPassVeto * pPassMetCut * pPassMetTriggers
        alphaError = 0.0
        alphaError  =  math.hypot  (alphaError,  pPassVeto       *  pPassMetCut       *  pPassMetTriggersError)
        alphaError  =  math.hypot  (alphaError,  pPassVeto       *  pPassMetCutError  *  pPassMetTriggers)
        alphaError  =  math.hypot  (alphaError,  pPassVetoError  *  pPassMetCut       *  pPassMetTriggers)

        nEst = nCtrl * pPassVeto * pPassMetCut * pPassMetTriggers
        nEstError = 0.0
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pPassVeto       *  pPassMetCut       *  pPassMetTriggersError)
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pPassVeto       *  pPassMetCutError  *  pPassMetTriggers)
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pPassVetoError  *  pPassMetCut       *  pPassMetTriggers)
        nEstError  =  math.hypot  (nEstError,  nCtrlError  *  pPassVeto       *  pPassMetCut       *  pPassMetTriggers)

        print "N: " + str (N)
        if not (alpha == 0):
            print "alpha: " + str (alpha) + " +- " + str (alphaError)
        else:
            print "alpha: " + str (alpha) + " - 0 + " + str (alphaError)

        if not (nEst == 0):
            print "N_est: " + str (nEst) + " +- " + str (nEstError)
        else:
            print "N_est: " + str (nEst) + " - 0 + " + str (nEstError)
        return (nEst, nEstError)

    def plotMetForNest (self, metMinusOne, (pPassVeto, pPassVetoError), (pPassMetCut, pPassMetCutError), triggerEfficiency):
        if self._fout and self._canvas:
            metMinusOne.Multiply (triggerEfficiency)
            for i in range (0, metMinusOne.GetNbinsX () + 2):
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

    def printPpassVetoTagProbe (self):
        if math.isnan (self._pPassVeto[0]) or math.isnan (self._pPassVeto[1]):
            if hasattr (self, "TagProbe") and hasattr (self, "TagProbePass"):
                total       = self.TagProbe["yield"]
                totalError  = self.TagProbe["yieldError"]
                passes      = self.TagProbePass["yield"]
                passesError = self.TagProbePass["yieldError"]

                eff = passes / (2.0 * total - passes)
                effError = 2.0 * math.hypot (passesError * total, passes * totalError) / ((2.0 * total - passes) * (2.0 * total - passes))
                print "P (pass lepton veto) in tag-probe sample: " + str (eff) + " +- " + str (effError)
                return (eff, effError)
            else:
                print "TagProbe and TagProbePass not both defined.  Not printing lepton veto efficiency..."
                return (float ("nan"), float ("nan"))
        else:
            print "P (pass lepton veto) from user input: " + str (self._pPassVeto[0]) + " +- " + str (self._pPassVeto[1])
            return (self._pPassVeto[0], self._pPassVeto[1])

    def printStdResults (self):

        print "********************************************************************************"
        print "Compare lepton veto efficiency in tag and probe sample and in baseline sample (latter requires MC truth)."

        (nTP, nTPError)     = self.printPpassVetoTagProbe ()
        (nBase, nBaseError) = self.printPpassVeto ()
        print "|P_tp - P_base| = " + str (abs (nTP - nBase) / math.hypot (nTPError, nBaseError)) + " sigma"
        self.printPpassVetoSystErr()

        print "********************************************************************************"

        (nEst, nEstError) = self.printNest ()

        print "--------------------------------------------------------------------------------"

        (nBack, nBackError) = self.printNback ()
        print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

        print "********************************************************************************"

class FakeTrackBkgdEstimate:
    _fout = None
    _canvas = None
    _prescale = 1.0

    def __init__ (self):
        pass

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addPrescaleFactor (self, prescale):
        self._prescale = prescale

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printPfakeTrack (self):
        if hasattr (self, "ZtoLL") and hasattr (self, "ZtoLLdisTrk"):
            total = self.ZtoLL["yield"]
            totalError = self.ZtoLL["yieldError"]
            passes = self.ZtoLLdisTrk["yield"]
            passesError = self.ZtoLLdisTrk["yieldError"] if passes > 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (0.0 + 1)) * self.ZtoLLdisTrk["weight"]

            eff = passes / total
            effError = math.hypot (total * passesError, totalError * passes) / (total * total)
            if eff > 0.0:
                print "P (fake track): " + str (eff) + " +- " + str (effError)
            else:
                print "P (fake track): " + str (eff) + " - 0.0 + " + str (effError)
            return (eff, effError, passes, passesError, total, totalError)
        else:
            print "ZtoLL and ZtoLLdisTrk not both defined. Not printing P (fake track)..."
            return (float ("nan"), float ("nan"))

    def printNctrl (self):
        if hasattr (self, "Basic"):
            n = self.Basic["yield"]
            nError = self.Basic["yieldError"]

            n *= self._prescale
            nError *= self._prescale

            print "N_ctrl: " + str (n) + " +- " + str (nError)
            return (n, nError)
        else:
            print "Basic not defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"))

    def printNest (self):
        pFakeTrack,  pFakeTrackError,  passes,  passesError,  total,  totalError  =  self.printPfakeTrack  ()
        nCtrl,       nCtrlError       =  self.printNctrl       ()

        N = passes
        alpha = nCtrl / total
        alphaError = math.hypot (nCtrl * totalError, nCtrlError * total) / (total * total)

        nEst = nCtrl * pFakeTrack
        nEstError = 0.0
        nEstError  =  math.hypot  (nEstError,  nCtrl       *  pFakeTrackError)
        nEstError  =  math.hypot  (nEstError,  nCtrlError  *  pFakeTrack)

        print "N: " + str (N)
        if not (alpha == 0):
            print "alpha: " + str (alpha) + " +- " + str (alphaError)
        else:
            print "alpha: " + str (alpha) + " - 0 + " + str (alphaError)

        if not (nEst == 0.0):
            print "N_est: " + str (nEst) + " +- " + str (nEstError)
        else:
            print "N_est: " + str (nEst) + " - 0.0 + " + str (nEstError)

        return (nEst, nEstError)
