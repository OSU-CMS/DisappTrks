#!/usr/bin/env python
import os
import sys
import math
import functools

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TH3D, TMath, TPaveText, TObject

from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.StandardAnalysis.plotUtilities import *

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

class LeptonBkgdEstimate:
    _Flavor = ""
    _flavor = ""
    _fout = None
    _canvas = None
    _metCut = 100.0
    _phiCut = 0.5
    _eCaloCut = 10.0
    _pPassVeto = float ("nan")
    _prescale = 1.0
    _tagProbePassScaleFactor = 1.0
    _tagProbePass1ScaleFactor = 1.0
    _luminosityInInvFb = float ("nan")
    _luminosityLabel = "13 TeV"
    _plotLabel = ""
    _metMinusOneHist = ""
    _useIdMatch = False  # match the track to get the true bkgd yield
    _fiducialElectronSigmaCut = 2.0
    _fiducialMuonSigmaCut = 2.0
    _rebinFactor = 1

    getHistFromProjectionZ = functools.partial (getHistFromProjectionZ, fiducialElectronSigmaCut = _fiducialElectronSigmaCut, fiducialMuonSigmaCut = _fiducialMuonSigmaCut)
    getHistIntegralFromProjectionZ = functools.partial (getHistIntegralFromProjectionZ, fiducialElectronSigmaCut = _fiducialElectronSigmaCut, fiducialMuonSigmaCut = _fiducialMuonSigmaCut)

    def __init__ (self, flavor):
        self._flavor = flavor.lower ()
        self._Flavor = self._flavor[0].upper () + self._flavor[1:]
        self._metMinusOneHist = "Track-" + self._flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addMetCut (self, metCut):
        self._metCut = metCut

    def addPhiCut (self, phiCut):
        self._phiCut = phiCut

    def addECaloCut (self, eCaloCut):
        self._eCaloCut = eCaloCut

    def useIdMatch (self, match):
        self._useIdMatch = match

    def addPpassVeto (self, pPassVeto):
        self._pPassVeto = pPassVeto

    def addPrescaleFactor (self, prescale):
        self._prescale = prescale

    def addTagProbePassScaleFactor (self, tagProbePassScaleFactor):
        self._tagProbePassScaleFactor = tagProbePassScaleFactor

    def addTagProbePass1ScaleFactor (self, tagProbePass1ScaleFactor):
        self._tagProbePass1ScaleFactor = tagProbePass1ScaleFactor

    def addLuminosityInInvPb (self, luminosityInInvPb):
        self._luminosityInInvFb = luminosityInInvPb / 1000.0

    def addLuminosityLabel (self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

    def addPlotLabel (self, plotLabel):
        self._plotLabel = plotLabel

    def addRebinFactor (self, rebinFactor):
        self._rebinFactor = rebinFactor

    def useMetMinusOneForIntegrals (self, flag = True):
        if flag:
            self._metMinusOneHist = "Track-" + self._flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
        else:
            self._metMinusOneHist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"

    def setFiducialMapCuts (self, cutValueEle, cutValueMuon):
        self._fiducialElectronSigmaCut = cutValueEle
        self._fiducialMuonSigmaCut = cutValueMuon
        self.getHistFromProjectionZ = functools.partial (getHistFromProjectionZ, fiducialElectronSigmaCut = self._fiducialElectronSigmaCut, fiducialMuonSigmaCut = self._fiducialMuonSigmaCut)
        self.getHistIntegralFromProjectionZ = functools.partial (getHistIntegralFromProjectionZ, fiducialElectronSigmaCut = self._fiducialElectronSigmaCut, fiducialMuonSigmaCut = self._fiducialMuonSigmaCut)

    def getPdgRange(self):
        if   self._flavor == "electron":
            return 11, 11
        elif self._flavor == "muon":
            return 13, 13
        elif self._flavor == "tau":
            return 14, 40  # define tau to include everything besides electrons and muons.  Last bin value is for 38.

    def addChannel (self, role, name, sample, condorDir, useIdMatch = False):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        n = None
        nError = None

        n, nError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        w = (nError * nError) / n
        n /= w
        nError /= w
        channel["weight"] = w
        channel["total"] = Measurement (n * w, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))) * w)
        channel["total"].isPositive ()

        if useIdMatch:
            pdgLo, pdgHi = self.getPdgRange()
            # NOTE: below is wrong since the fiducial map cuts haven't been applied.
            #       need to add 3d plot of bestMatchPdgId vs these maxSigmas
            n, nError = getHistIntegral (sample, condorDir, name + "Plotter", "Track Plots/bestMatchPdgId", pdgLo, pdgHi)
        else:
            n, nError = self.getHistIntegralFromProjectionZ (sample, condorDir, name + "Plotter")
        n /= w
        nError /= w
        channel["yield"] = Measurement (n * w, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))) * w)
        channel["yield"].isPositive ()

        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"])

    def printNctrl (self):
        self.plotMetForNctrl ()
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            n = self.TagPt35ForNctrl["yield"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["yield"]
            n *= self._prescale

            print "N_ctrl: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)"
            return n
        else:
            print "Neither TagPt35 nor TagPt35ForNctrl defined. Not printing N_ctrl..."
            return float ("nan")

    def plotMetForNctrl (self):
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            if self._fout and self._canvas:
                sample = self.TagPt35ForNctrl["sample"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["sample"]
                condorDir = self.TagPt35ForNctrl["condorDir"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["condorDir"]
                name = self.TagPt35ForNctrl["name"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["name"]
                #hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                #met = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu")
                hist = "Met-eventvariable Plots/deltaPhiMetJetLeadingVsMetNoMu"
                met = getHist (sample, condorDir, name + "Plotter", hist)

                # explicitly get metNoMuMinusOne instead of using
                # _metMinusOneHist since we plot both metNoMu and
                # metNoMuMinusOne here
                #hist = "Track-" + self._flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                #metMinusOne = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", hist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
                hist = self._Flavor + "-eventvariable Plots/deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHist (sample, condorDir, name + "Plotter", hist)

                pt = TPaveText(0.404762,0.137597,0.805764,0.185401,"brNDC")
                pt.SetBorderSize(0)
                pt.SetFillStyle(0)
                pt.SetTextFont(42)
                pt.SetTextSize(0.0387597)
                pt.AddText(str (self._plotLabel))

                cmsLabel = TPaveText(0.134085,0.937984,0.418546,0.984496,"brNDC")
                cmsLabel.SetBorderSize(0)
                cmsLabel.SetFillStyle(0)
                cmsLabel.SetTextFont(62)
                cmsLabel.SetTextSize(0.0387597)
                cmsLabel.AddText("CMS Preliminary")

                lumiLabel = TPaveText(0.575188,0.937339,0.874687,0.992894,"brNDC")
                lumiLabel.SetBorderSize(0)
                lumiLabel.SetFillStyle(0)
                lumiLabel.SetTextFont(42)
                lumiLabel.SetTextSize(0.0387597)
                lumiLabel.AddText(str (self._luminosityLabel))

                setStyle (met)
                setAxisStyle (met, "E_{T}^{miss, no #mu} [GeV]", "|#Delta#Phi(E_{T}^{miss, no #mu}, leading jet)|")
                self._canvas.cd ()
                met.Draw ("colz")
                pt.Draw ("same")
                cmsLabel.Draw ("same")
                lumiLabel.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metForNctrl")

                setStyle (metMinusOne)
                setAxisStyle (metMinusOne, "E_{T}^{miss, no #mu} " + ("excluding selected " + self._flavor if self._flavor != "muon" else "") + " [GeV]", "|#Delta#Phi(E_{T}^{miss, no #mu} " + ("excluding selected " + self._flavor if self._flavor != "muon" else "") + ", leading jet)|")
                self._canvas.cd ()
                metMinusOne.Draw ("colz")
                pt.Draw ("same")
                cmsLabel.Draw ("same")
                lumiLabel.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metMinusOneForNctrl")
            else:
                print "A TFile and TCanvas must be added. Not making plots..."
        else:
            print "Neither TagPt35 nor TagPt35ForNctrl defined. Not plotting MET for N_ctrl..."

    def printPpassVeto (self):
        if not hasattr (self._pPassVeto, "centralValue"):
            if hasattr (self, "TagPt35") and hasattr (self, "CandTrkIdPt35NoMet"):
                total = self.TagPt35["yield"]
                passes = self.CandTrkIdPt35NoMet["yield"]

                eff = passes / total
                print "P (pass lepton veto) in baseline sample: " + str (eff)
                return eff
            else:
                print "TagPt35 and CandTrkIdPt35NoMet not both defined. Not printing P (pass lepton veto)..."
                return float ("nan")
        else:
            print "P (pass lepton veto) from user input: " + str (self._pPassVeto)
            return self._pPassVeto

    def printPpassMetCut (self):
        if hasattr (self, "TagPt35"):
            total = self.TagPt35["yield"]
            passes = 0.0

            if hasattr (self, "TagPt35MetCut"):
                passes = self.TagPt35MetCut["yield"]
            else:
                sample = self.TagPt35["sample"]
                condorDir = self.TagPt35["condorDir"]
                name = self.TagPt35["name"]
                #met = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", self._metMinusOneHist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
                met = getHist (sample, condorDir, name + "Plotter" + "/" + self._Flavor + "-eventvariable Plots", "deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt")

                passesError = Double (0.0)
                passes = met.IntegralAndError (met.GetXaxis ().FindBin (self._metCut), met.GetNbinsX () + 1, met.GetYaxis ().FindBin (self._phiCut), met.GetNbinsY () + 1, passesError)
                passes = Measurement (passes, passesError)
                passes.isPositive ()

            eff = passes / total
            print "P (pass met cut): " + str (eff)
            return eff
        else:
            print "TagPt35 not defined. Not printing P (pass met cut)..."
            return float ("nan")

    def printPpassMetTriggers (self):
        if hasattr (self, "TagPt35") and (hasattr (self, "TagPt35MetTrig") or (hasattr (self, "TrigEffDenom") and hasattr (self, "TrigEffNumer"))):
            sample = self.TrigEffDenom["sample"] if hasattr (self, "TrigEffDenom") else self.TagPt35["sample"]
            condorDir = self.TrigEffDenom["condorDir"] if hasattr (self, "TrigEffDenom") else self.TagPt35["condorDir"]
            name = self.TrigEffDenom["name"] if hasattr (self, "TrigEffDenom") else self.TagPt35["name"]
            hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracksX"
            totalHist = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu")

            sample = self.TrigEffNumer["sample"] if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig["sample"]
            condorDir = self.TrigEffNumer["condorDir"] if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig["condorDir"]
            name = self.TrigEffNumer["name"] if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig["name"]
            hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracksX"
            passesHist = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu")

            self.plotTriggerEfficiency (passesHist, totalHist)

            sample = self.TagPt35["sample"]
            condorDir = self.TagPt35["condorDir"]
            name = self.TagPt35["name"]
            #metHist = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", self._metMinusOneHist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
            metHist2D = getHist (sample, condorDir, name + "Plotter" + "/" + self._Flavor + "-eventvariable Plots", "deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt")
            metHist2D.GetYaxis ().SetRangeUser (self._phiCut, 4.0)
            metHist = metHist2D.ProjectionX ("metHist")

            passesHist.Divide (totalHist)
            metHist.Multiply (passesHist)

            total = 0.0
            totalError = Double (0.0)
            passesError = Double (0.0)

            passes = metHist.IntegralAndError (metHist.FindBin (self._metCut), metHist.GetNbinsX () + 1, passesError)
            passes = Measurement (passes, passesError)
            passes.isPositive ()

            if hasattr (self, "TagPt35MetCut"):
                total = self.TagPt35MetCut["yield"]
            else:
                sample = self.TagPt35["sample"]
                condorDir = self.TagPt35["condorDir"]
                name = self.TagPt35["name"]
                #met = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", self._metMinusOneHist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
                met = getHist (sample, condorDir, name + "Plotter" + "/" + self._Flavor + "-eventvariable Plots", "deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt")

                totalError = Double (0.0)
                total = met.IntegralAndError (met.GetXaxis ().FindBin (self._metCut), met.GetNbinsX () + 1, met.GetYaxis ().FindBin (self._phiCut), met.GetNbinsY () + 1, totalError)
                total = Measurement (total, totalError)
                total.isPositive ()

            eff = passes / total
            print "P (pass met triggers): " + str (eff)
            return (eff, passesHist)
        else:
            print "TagPt35 and TagPt35MetTrig not both defined. Not printing P (pass met triggers)..."
            return (float ("nan"), float ("nan"))

    def plotTriggerEfficiency (self, passesHist, totalHist):
        if self._fout and self._canvas:
            passesHist = passesHist.Rebin (self._rebinFactor, "passesHist")
            totalHist = totalHist.Rebin (self._rebinFactor, "totalHist")

            self.makePassesConsistentWithTotal (passesHist, totalHist)
            metGraph = TGraphAsymmErrors (passesHist, totalHist)
            metGraph.SetEditable (0)

            pt = TPaveText(0.409774,0.843023,0.809524,0.890827,"brNDC")
            pt.SetBorderSize(0)
            pt.SetFillStyle(0)
            pt.SetTextFont(42)
            pt.SetTextSize(0.0387597)
            pt.AddText(str (self._plotLabel))

            cmsLabel = TPaveText(0.134085,0.937984,0.418546,0.984496,"brNDC")
            cmsLabel.SetBorderSize(0)
            cmsLabel.SetFillStyle(0)
            cmsLabel.SetTextFont(62)
            cmsLabel.SetTextSize(0.0387597)
            cmsLabel.AddText("CMS Preliminary")

            lumiLabel = TPaveText(0.575188,0.937339,0.874687,0.992894,"brNDC")
            lumiLabel.SetBorderSize(0)
            lumiLabel.SetFillStyle(0)
            lumiLabel.SetTextFont(42)
            lumiLabel.SetTextSize(0.0387597)
            lumiLabel.AddText(str (self._luminosityLabel))

            setStyle (metGraph)
            self._canvas.cd ()
            metGraph.Draw ("ap")
            setAxisStyle (metGraph, "E_{T}^{miss, no #mu} [GeV]", "trigger efficiency", (0.0, 500.0), (0.0, 1.4))
            pt.Draw ("same")
            cmsLabel.Draw ("same")
            lumiLabel.Draw ("same")
            self._fout.cd ()
            self._canvas.Write ("triggerEfficiency")
        else:
            print "A TFile and TCanvas must be added. Not making plots..."

    def printNback (self):
        self.plotMetForNback ()
        if hasattr (self, "CandTrkIdPt35"):
            sample = self.CandTrkIdPt35["sample"]
            condorDir = self.CandTrkIdPt35["condorDir"]
            name = self.CandTrkIdPt35["name"]
            hist = "Track Plots/trackCaloTot_RhoCorr"
            eCalo = getHist (sample, condorDir, name + "Plotter", hist)

            nError = Double (0.0)
            n = eCalo.IntegralAndError (0, eCalo.FindBin (self._eCaloCut), nError)
            w = self.CandTrkIdPt35["weight"]

            n /= w
            nError /= w
            n = Measurement (n * w, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))) * w)

            print "N_back: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)"
            return n
        else:
            print "CandTrkIdPt35 not defined. Not printing N_back..."
            return float ("nan")

    def plotMetForNback (self):
        if hasattr (self, "CandTrkIdPt35"):
            if self._fout and self._canvas:
                sample = self.CandTrkIdPt35["sample"]
                condorDir = self.CandTrkIdPt35["condorDir"]
                name = self.CandTrkIdPt35["name"]
                hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                met = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu")

                # explicitly get metNoMuMinusOne instead of using
                # _metMinusOneHist since we plot both metNoMu and
                # metNoMuMinusOne here
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                hist = "Track-" + self._flavor + " Plots/" + self._flavor + "NoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                metMinusOne = self.getHistFromProjectionZ (sample, condorDir, name + "Plotter", hist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
                if not isinstance(met, TObject) or not isinstance(metMinusOne, TObject):
                    print "Warning [plotMetForNback]: Could not get required hists from sample=", sample, "condorDir=", condorDir, "name=", name
                    return

                met.Rebin (self._rebinFactor)
                metMinusOne.Rebin (self._rebinFactor)

                pt = TPaveText(0.409774,0.843023,0.809524,0.890827,"brNDC")
                pt.SetBorderSize(0)
                pt.SetFillStyle(0)
                pt.SetTextFont(42)
                pt.SetTextSize(0.0387597)
                pt.AddText(str (self._plotLabel))

                cmsLabel = TPaveText(0.134085,0.937984,0.418546,0.984496,"brNDC")
                cmsLabel.SetBorderSize(0)
                cmsLabel.SetFillStyle(0)
                cmsLabel.SetTextFont(62)
                cmsLabel.SetTextSize(0.0387597)
                cmsLabel.AddText("CMS Preliminary")

                lumiLabel = TPaveText(0.575188,0.937339,0.874687,0.992894,"brNDC")
                lumiLabel.SetBorderSize(0)
                lumiLabel.SetFillStyle(0)
                lumiLabel.SetTextFont(42)
                lumiLabel.SetTextSize(0.0387597)
                lumiLabel.AddText(str (self._luminosityLabel))

                setStyle (met)
                setAxisStyle (met, "E_{T}^{miss, no #mu} [GeV]", "Entries / " + str (met.GetBinWidth (1)) + " GeV")
                self._canvas.cd ()
                met.Draw ()
                pt.Draw ("same")
                cmsLabel.Draw ("same")
                lumiLabel.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metForNback")

                setStyle (metMinusOne)
                setAxisStyle (metMinusOne, "E_{T}^{miss, no #mu} " + ("excluding selected " + self._flavor if self._flavor != "muon" else "") + " [GeV]", "Entries / " + str (metMinusOne.GetBinWidth (1)) + " GeV")
                self._canvas.cd ()
                metMinusOne.Draw ()
                pt.Draw ("same")
                cmsLabel.Draw ("same")
                lumiLabel.Draw ("same")
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
        nCtrl = self.printNctrl ()
        pPassVeto, passes, passes1, total = self.printPpassVetoTagProbe ()
        pPassMetCut = self.printPpassMetCut ()
        pPassMetTriggers, triggerEfficiency = self.printPpassMetTriggers ()

        if not hasattr (pPassVeto, "centralValue"):
            pPassVeto = self.printPpassVeto ()

        nEst = nCtrl * pPassVeto * pPassMetCut * pPassMetTriggers
        nEst.isPositive ()

        N = alpha = alphaError = float ("nan")
        if hasattr (passes, "centralValue") and hasattr (total, "centralValue"):
            if pPassVeto > 0.0:
                N = nCtrl / self._prescale
                alpha = self._prescale * pPassVeto * pPassMetCut * pPassMetTriggers
            else:
                N = passes
                alpha = (self._tagProbePassScaleFactor / (2.0 * total)) * nCtrl * pPassMetCut * pPassMetTriggers

        alpha.printLongFormat ()

        print "N: " + str (N)
        print "alpha: " + str (alpha)
        if not (alpha == 0):
            print "error on alpha: " + str (1.0 + (alpha.maxUncertainty () / alpha.centralValue ()))
        print "N_est: " + str (nEst) + " (" + str (nEst / self._luminosityInInvFb) + " fb)"
        return nEst

    def printPpassVetoTagProbe (self):
        self.plotPpassVeto ()
        if not hasattr (self._pPassVeto, "centralValue"):
            if hasattr (self, "TagProbe") and hasattr (self, "TagProbePass"):
                total       = self.TagProbe["yield"]
                passes      = self.TagProbePass["yield"]

                passes1 = 0.0

                if hasattr (self, "TagProbe1") and hasattr (self, "TagProbePass1"):
                    total        += self.TagProbe1["yield"]
                    passes1       = self.TagProbePass1["yield"]

                scaledPasses = passes * self._tagProbePassScaleFactor + passes1 * self._tagProbePass1ScaleFactor

                if self._flavor == "electron" or self._flavor == "muon":
                    eff = scaledPasses / (2.0 * total - scaledPasses)
                else:
                    eff = scaledPasses / total

                print "P (pass lepton veto) in tag-probe sample: " + str (eff)
                return (eff, passes, passes1, total)
            else:
                print "TagProbe and TagProbePass not both defined.  Not printing lepton veto efficiency..."
                return (float ("nan"), float ("nan"), float ("nan"), float ("nan"))
        else:
            print "P (pass lepton veto) from user input: " + str (self._pPassVeto)
            return (self._pPassVeto, float ("nan"), float ("nan"), float ("nan"))

    def plotPpassVeto (self):
        if hasattr (self, "TagProbe") and hasattr (self, "TagProbePass"):
            if self._fout and self._canvas:
                hist = "Track Plots/trackPt"
                sample = self.TagProbe["sample"]
                condorDir = self.TagProbe["condorDir"]
                name = self.TagProbe["name"]
                trackPt = getHist (sample, condorDir, name + "Plotter", hist)

                sample = self.TagProbePass["sample"]
                condorDir = self.TagProbePass["condorDir"]
                name = self.TagProbePass["name"]
                trackPtPass = getHist (sample, condorDir, name + "Plotter", hist)

                if hasattr (self, "TagProbe1") and hasattr (self, "TagProbePass1"):
                    hist = "Track Plots/trackPt"
                    sample = self.TagProbe1["sample"]
                    condorDir = self.TagProbe1["condorDir"]
                    name = self.TagProbe1["name"]
                    trackPt1 = getHist (sample, condorDir, name + "Plotter", hist)

                    sample = self.TagProbePass1["sample"]
                    condorDir = self.TagProbePass1["condorDir"]
                    name = self.TagProbePass1["name"]
                    trackPtPass1 = getHist (sample, condorDir, name + "Plotter", hist)

                    trackPt.Add (trackPt1)
                    trackPtPass.Add (trackPtPass1)

                invMass = None
                invMassPass = None
                if self._flavor != "tau":
                    hist = "Track-" + self._flavor + " Plots/invMassNearZ"
                    sample = self.TagProbe["sample"]
                    condorDir = self.TagProbe["condorDir"]
                    name = self.TagProbe["name"]
                    invMass = getHist (sample, condorDir, name + "Plotter", hist)

                    sample = self.TagProbePass["sample"]
                    condorDir = self.TagProbePass["condorDir"]
                    name = self.TagProbePass["name"]
                    invMassPass = getHist (sample, condorDir, name + "Plotter", hist)

                    if hasattr (self, "TagProbe1") and hasattr (self, "TagProbePass1"):
                        hist = "Track-" + self._flavor + " Plots/invMassNearZ"
                        sample = self.TagProbe1["sample"]
                        condorDir = self.TagProbe1["condorDir"]
                        name = self.TagProbe1["name"]
                        invMass1 = getHist (sample, condorDir, name + "Plotter", hist)

                        sample = self.TagProbePass1["sample"]
                        condorDir = self.TagProbePass1["condorDir"]
                        name = self.TagProbePass1["name"]
                        invMassPass1 = getHist (sample, condorDir, name + "Plotter", hist)

                        invMass.Add (invMass1)
                        invMassPass.Add (invMassPass1)

                pt = TPaveText(0.404762,0.137597,0.805764,0.185401,"brNDC")
                pt.SetBorderSize(0)
                pt.SetFillStyle(0)
                pt.SetTextFont(42)
                pt.SetTextSize(0.0387597)
                pt.AddText(str (self._plotLabel))

                cmsLabel = TPaveText(0.134085,0.937984,0.418546,0.984496,"brNDC")
                cmsLabel.SetBorderSize(0)
                cmsLabel.SetFillStyle(0)
                cmsLabel.SetTextFont(62)
                cmsLabel.SetTextSize(0.0387597)
                cmsLabel.AddText("CMS Preliminary")

                lumiLabel = TPaveText(0.575188,0.937339,0.874687,0.992894,"brNDC")
                lumiLabel.SetBorderSize(0)
                lumiLabel.SetFillStyle(0)
                lumiLabel.SetTextFont(42)
                lumiLabel.SetTextSize(0.0387597)
                lumiLabel.AddText(str (self._luminosityLabel))

                ksPt = TPaveText(0.421053,0.824289,0.820802,0.872093,"brNDC")
                ksPt.SetBorderSize(0)
                ksPt.SetFillStyle(0)
                ksPt.SetTextFont(42)
                ksPt.SetTextSize(0.0387597)
                ksPt.AddText("KS test p-value: " + str (round (trackPt.KolmogorovTest (trackPtPass), 3)))

                leg = TLegend (0.413534,0.729328,0.794486,0.815891)
                leg.SetBorderSize(0)
                leg.SetFillStyle(0)
                leg.SetTextFont(42)
                leg.SetTextSize(0.0387597)
                leg.AddEntry (trackPt, "before veto", "p")
                leg.AddEntry (trackPtPass, "after veto", "p")

                setStyle (trackPt, 600)
                setAxisStyle (trackPt, self._flavor + " probe track p_{T} [GeV]")
                setStyle (trackPtPass, 632)
                setAxisStyle (trackPtPass, self._flavor + " probe track p_{T} [GeV]")
                self._canvas.cd ()
                trackPt.Draw ("colz")
                trackPtPass.Draw ("colz same")
                pt.Draw ("same")
                cmsLabel.Draw ("same")
                lumiLabel.Draw ("same")
                ksPt.Draw ("same")
                leg.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("pPassVetoPtDependence")

                if self._flavor != "tau":
                    ksInvMass = TPaveText(0.421053,0.824289,0.820802,0.872093,"brNDC")
                    ksInvMass.SetBorderSize(0)
                    ksInvMass.SetFillStyle(0)
                    ksInvMass.SetTextFont(42)
                    ksInvMass.SetTextSize(0.0387597)
                    ksInvMass.AddText("KS test p-value: " + str (round (invMass.KolmogorovTest (invMassPass), 3)))

                    setStyle (invMass, 600)
                    setAxisStyle (invMass, "tag-probe invariant mass [GeV]")
                    setStyle (invMassPass, 632)
                    setAxisStyle (invMassPass, "tag-probe invariant mass [GeV]")
                    self._canvas.cd ()
                    invMass.Draw ("colz")
                    invMassPass.Draw ("colz same")
                    pt.Draw ("same")
                    cmsLabel.Draw ("same")
                    lumiLabel.Draw ("same")
                    ksInvMass.Draw ("same")
                    leg.Draw ("same")
                    self._fout.cd ()
                    self._canvas.Write ("pPassVetoInvMassDependence")
            else:
                print "A TFile and TCanvas must be added. Not making plots..."
        else:
            print "Neither TagProbe nor TagProbePass defined. Not plotting P_veto pt dependence..."
