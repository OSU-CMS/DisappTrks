#!/usr/bin/env python3
import os
import sys
import math
import functools
import glob
import importlib


from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TH3D, TMath, TPaveText, TObject, TF1, gDirectory, TH2D, TChain

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import dataFormat
from OSUT3Analysis.Configuration.Measurement import Measurement
from OSUT3Analysis.Configuration.ProgressIndicator import ProgressIndicator
from DisappTrks.StandardAnalysis.plotUtilities import *
import ctypes
from array import *

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

up68 = 0.5 * TMath.ChisquareQuantile (0.68, 2)

def prettyPrintTotals (electrons, muons, taus, fakes, nLayersWords, runPeriods, year):
    print('pretty print totals for paper:')
    fullTotal = Measurement(0.0, 0.0, 0.0, 0.0, 0.0)
    for runPeriod in runPeriods:
        for nLayersWord in nLayersWords:
            module = importlib.import_module('DisappTrks.LimitSetting.bkgdConfig_' + year + runPeriod + '_' + nLayersWord) 
            background_systematics = getattr(module, 'background_systematics')
            
            eleSystematic = [0.0, 0.0]
            muonSystematic = [0.0, 0.0]
            tauSystematic = [0.0, 0.0]
            fakeSystematic = [0.0, 0.0]
            
            for systematic in background_systematics:
                if '_alpha_' in systematic:
                    continue

                if '/' in background_systematics[systematic]['value']:
                    systValue = (1.0 - float(background_systematics[systematic]['value'].split('/')[0]), float(background_systematics[systematic]['value'].split('/')[1]) - 1.0)
                else:
                    systValue = (float(background_systematics[systematic]['value']) - 1.0, float(background_systematics[systematic]['value']) - 1.0)

                if background_systematics[systematic]['background'] == 'Fake': 
                    fakeSystematic[0] += (systValue[0] * fakes[(nLayersWord, runPeriod)].centralValue()) ** 2.
                    fakeSystematic[1] += (systValue[1] * fakes[(nLayersWord, runPeriod)].centralValue()) ** 2.
                elif background_systematics[systematic]['background'] == 'Elec':
                    eleSystematic[0] += (systValue[0] * electrons[(nLayersWord, runPeriod)].centralValue()) ** 2.
                    eleSystematic[1] += (systValue[1] * electrons[(nLayersWord, runPeriod)].centralValue()) ** 2.
                elif background_systematics[systematic]['background'] == 'Muon':
                    muonSystematic[0] += (systValue[0] * muons[(nLayersWord, runPeriod)].centralValue()) ** 2.
                    muonSystematic[1] += (systValue[1] * muons[(nLayersWord, runPeriod)].centralValue()) ** 2.
                elif background_systematics[systematic]['background'] == 'Tau':
                    tauSystematic[0] += (systValue[0] * taus[(nLayersWord, runPeriod)].centralValue()) ** 2.
                    tauSystematic[1] += (systValue[1] * taus[(nLayersWord, runPeriod)].centralValue()) ** 2.

            electrons[(nLayersWord, runPeriod)].setSystematicDown(math.sqrt(eleSystematic[0]))
            electrons[(nLayersWord, runPeriod)].setSystematicUp(math.sqrt(eleSystematic[1]))

            muons[(nLayersWord, runPeriod)].setSystematicDown(math.sqrt(muonSystematic[0]))
            muons[(nLayersWord, runPeriod)].setSystematicUp(math.sqrt(muonSystematic[1]))

            taus[(nLayersWord, runPeriod)].setSystematicDown(math.sqrt(tauSystematic[0]))
            taus[(nLayersWord, runPeriod)].setSystematicUp(math.sqrt(tauSystematic[1]))

            fakes[(nLayersWord, runPeriod)].setSystematicDown(math.sqrt(fakeSystematic[0]))
            fakes[(nLayersWord, runPeriod)].setSystematicUp(math.sqrt(fakeSystematic[1]))

            leptons = electrons[(nLayersWord, runPeriod)] + muons[(nLayersWord, runPeriod)] + taus[(nLayersWord, runPeriod)]
            totals = leptons + fakes[(nLayersWord, runPeriod)]

            fullTotal += totals

            print("********************************************************************************")
            print("Period: " + year + runPeriod)
            print("nLayers: " + nLayersWord)
            print("\tElectrons: " + str(electrons[(nLayersWord, runPeriod)]))
            print("\tMuons: " + str(muons[(nLayersWord, runPeriod)]))
            print("\tTaus: " + str(taus[(nLayersWord, runPeriod)]))
            print("\t-------------------------------------")
            print("\tLeptons (total): " + str(leptons))
            print("\tFake tracks: " + str(fakes[(nLayersWord, runPeriod)]))
            print("\t-------------------------------------")
            print("Total background: " + str(totals))
            print("********************************************************************************")
    print('Full total across all nLayers categories, run periods:')
    print(str(fullTotal))

class LeptonBkgdEstimate:
    _Flavor = ""
    _flavor = ""
    _fout = None
    _canvas = None
    _metCut = 120.0 if (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")) else 100.0
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
    _useHistogramsForPpassVeto = True
    _useOnlineQuantitiesForPpassMetTriggers = False
    _useExternalTriggerEfficiency = False

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

    def addUseHistogramsForPpassVeto (self, useHistogramsForPpassVeto):
        self._useHistogramsForPpassVeto = useHistogramsForPpassVeto

    def useOnlineQuantitiesForPpassMetTriggers (self, useOnlineQuantitiesForPpassMetTriggers):
        self._useOnlineQuantitiesForPpassMetTriggers = useOnlineQuantitiesForPpassMetTriggers

    def useExternalFlatTriggerEfficiency (self, eff):
        self._useExternalTriggerEfficiency = True
        print("External trigger efficiency: " + str(eff))
        setattr (self, 'externalTriggerEfficiency', eff)

    def useExternalTriggerEfficiency (self, nMatchedOS, nMatchedSS, nOS, nSS):
        self._useExternalTriggerEfficiency = True

        matchedOS = Measurement (nMatchedOS, math.sqrt (nMatchedOS)) if nMatchedOS > 0 else Measurement (0.0, 0.0, up68)
        matchedSS = Measurement (nMatchedSS, math.sqrt (nMatchedSS)) if nMatchedSS > 0 else Measurement (0.0, 0.0, up68)
        allOS     = Measurement (nOS, math.sqrt (nOS)) if nOS > 0 else Measurement (0.0, 0.0, up68)
        allSS     = Measurement (nSS, math.sqrt (nSS)) if nSS > 0 else Measurement (0.0, 0.0, up68)

        eff = (matchedOS - matchedSS) / (allOS - allSS)
        eff.isPositive ()

        print("External trigger efficiency: " + str(eff))
        setattr (self, 'externalTriggerEfficiency', eff)

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
        channel["total"] = Measurement (n * w, (nError if n != 0.0 else up68) * w)
        channel["total"].isPositive ()

        if useIdMatch:
            pdgLo, pdgHi = self.getPdgRange()
            # NOTE: below is wrong since the fiducial map cuts haven't been applied.
            #       need to add 3d plot of bestMatchPdgId vs these maxSigmas
            # N.B. "bestMatch" changed to "promptOrTauDecay" but hist name remains
            n, nError = getHistIntegral (sample, condorDir, name + "Plotter", "Track Plots/bestMatchPdgId", pdgLo, pdgHi)
        else:
            n, nError = self.getHistIntegralFromProjectionZ (sample, condorDir, name + "Plotter")
        n /= w
        nError /= w
        channel["yield"] = Measurement (n * w, (nError if n != 0.0 else up68) * w)
        channel["yield"].isPositive ()

        setattr (self, role, channel)
        print("yield for " + name + ": " + str (channel["yield"]))

    def appendChannel (self, role, name, sample, condorDir, useIdMatch = False):
        if not hasattr (self, role):
            print("Cannot append to role", role, "before it has been defined!")
            return

        channel = getattr (self, role)

        if "weight" not in channel or "total" not in channel or "yield" not in channel:
            print("Role", role, "is missing weight/total/yield and is improperly defined!")
            return

        n = None
        nError = None

        n, nError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        w = (nError * nError) / n
        n /= w
        nError /= w
        thisTotal = Measurement (n * w, (nError if n != 0.0 else up68) * w)
        thisTotal.isPositive ()

        # calculate effective weight:
        # if total(a) = Ta*wa, want X such that total(a+b) = (Ta + Tb) * X = Ta*wa + Tb*wb
        # X = (Ta*wa + Tb*wb) / (Ta + Tb)
        effectiveWeight = (channel["total"].centralValue() + thisTotal.centralValue()) / (channel["total"].centralValue()/channel["weight"] + thisTotal.centralValue()/w)

        channel["weight"] = effectiveWeight
        channel["total"] += thisTotal
        channel["total"].isPositive ()

        if useIdMatch:
            pdgLo, pdgHi = self.getPdgRange()
            # NOTE: below is wrong since the fiducial map cuts haven't been applied.
            #       need to add 3d plot of bestMatchPdgId vs these maxSigmas
            # N.B. "bestMatch" changed to "promptOrTauDecay" but hist name remains
            n, nError = getHistIntegral (sample, condorDir, name + "Plotter", "Track Plots/bestMatchPdgId", pdgLo, pdgHi)
        else:
            n, nError = self.getHistIntegralFromProjectionZ (sample, condorDir, name + "Plotter")
        n /= w
        nError /= w
        thisYield = Measurement (n * w, (nError if n != 0.0 else up68) * w)
        thisYield.isPositive ()

        channel["yield"] += thisYield
        channel["yield"].isPositive ()

        channelExtension = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        if "extensions" in channel:
            channel["extensions"].append(channelExtension)
        else:
            channel["extensions"] = [channelExtension]

        print('yield for role', role, 'appended with channel', name, 'increased yield to', channel['yield'])

    def printNctrl (self):
        self.plotMetForNctrl ()
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            n = self.TagPt35ForNctrl["yield"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["yield"]
            n *= self._prescale

            print("N_ctrl: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)")
            return n
        else:
            print("Neither TagPt35 nor TagPt35ForNctrl defined. Not printing N_ctrl...")
            return float ("nan")

    def plotMetForNctrl (self):
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            if self._fout and self._canvas:
                channel = self.TagPt35ForNctrl if hasattr (self, "TagPt35ForNctrl") else self.TagPt35

                #hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                #met = self.getHistFromProjectionZ (channel["sample"], channel["condorDir"], channel["name"] + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu")

                hist = "Met-eventvariable Plots/deltaPhiMetJetLeadingVsMetNoMu"
                met = getHistFromChannelDict(channel, hist)
                addChannelExtensions(met, channel, hist)

                # explicitly get metNoMuMinusOne instead of using
                # _metMinusOneHist since we plot both metNoMu and
                # metNoMuMinusOne here
                #hist = "Track-" + self._flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                #metMinusOne = self.getHistFromProjectionZ (channel["sample"], channel["condorDir"], channel["name"] + "Plotter", hist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
                hist = self._Flavor + "-eventvariable Plots/deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHistFromChannelDict (channel, hist)
                addChannelExtensions(metMinusOne, channel, hist)

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
                print("A TFile and TCanvas must be added. Not making plots...")
        else:
            print("Neither TagPt35 nor TagPt35ForNctrl defined. Not plotting MET for N_ctrl...")

    def printPpassVeto (self):
        if not hasattr (self._pPassVeto, "centralValue"):
            if hasattr (self, "TagPt35") and hasattr (self, "CandTrkIdPt35NoMet"):
                total = self.TagPt35["yield"]
                passes = self.CandTrkIdPt35NoMet["yield"]

                eff = passes / total
                print("P (pass lepton veto) in baseline sample: " + str (eff))
                return eff
            else:
                print("TagPt35 and CandTrkIdPt35NoMet not both defined. Not printing P (pass lepton veto)...")
                return float ("nan")
        else:
            print("P (pass lepton veto) from user input: " + str (self._pPassVeto))
            return self._pPassVeto

    def printPpassMetCut (self):
        if hasattr (self, "TagPt35"):
            channel = self.TagPt35
        else:
            print("TagPt35 not defined. Not printing P (pass met cut)...")
            return float ("nan")

        total = channel["yield"]
        passes = 0.0

        #met = self.getHistFromProjectionZ (channel["sample"], channel["condorDir"], channel["name"] + "Plotter", self._metMinusOneHist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
            
        hist = self._Flavor + "-eventvariable Plots/deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt"
        met = getHistFromChannelDict (channel, hist)
        addChannelExtensions(met, channel, hist)

        passesError = ctypes.c_double (0.0)
        passes = met.IntegralAndError (met.GetXaxis ().FindBin (self._metCut), met.GetNbinsX () + 1, met.GetYaxis ().FindBin (self._phiCut), met.GetNbinsY () + 1, passesError)
        passes = Measurement (passes, passesError)
        passes.isPositive ()

        eff = passes / total if total > 0.0 else 0.0
        print("P (pass met cut): " + str (eff))
        return eff

    def printPpassHEMveto (self):
        if (hasattr (self, "TagPt35MetTrigHEMveto") and hasattr (self, "TagPt35MetTrig")) or (hasattr (self, "TrigEffNumerHEMveto") and hasattr (self, "TrigEffNumer")):
            hist = "Met Plots/metNoMu"
            channel = self.TrigEffNumer if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig
            denominator = getHistFromChannelDict (channel, hist)
            nEventsDenominator = ctypes.c_double (getHist (channel["sample"], channel["condorDir"], channel["name"] + "CutFlowPlotter", "eventCounter").GetBinContent(1))
            if "extensions" in channel:
                for x in channel["extensions"]:
                    denominator.Add (getHist (x["sample"], x["condorDir"], x["name"] + "Plotter", hist))

            channel = self.TrigEffNumerHEMveto if hasattr (self, "TrigEffNumerHEMveto") else self.TagPt35MetTrigHEMveto
            numerator = getHistFromChannelDict (channel, hist)
            nEventsNumerator = ctypes.c_double (getHist (channel["sample"], channel["condorDir"], channel["name"] + "CutFlowPlotter", "eventCounter").GetBinContent(1))
            if "extensions" in channel:
                for x in channel["extensions"]:
                    numerator.Add (getHist (x["sample"], x["condorDir"], x["name"] + "Plotter", hist))

            if self._Flavor != "Muon":
                # temporary scale factor to correct cases where a different number of events were run over (incomplete jobs)
                # derived from the CutFlowPlotter/eventCounter histogram
                # muons used a skim in D but had 100% completion, so just turn this off for muons...
                sf = nEventsDenominator.value / nEventsNumerator.value if nEventsNumerator.value > 0.0 else 0.0
                if sf > 1.0:
                    print("\tApplying correction for incomplete jobs:", sf)
                numerator.Scale(sf)

            totalError = ctypes.c_double (0.0)
            total = denominator.IntegralAndError (denominator.FindBin (self._metCut), denominator.GetNbinsX () + 1, totalError)
            total = Measurement (total, totalError)

            passesError = ctypes.c_double (0.0)
            passes = numerator.IntegralAndError (numerator.FindBin (self._metCut), numerator.GetNbinsX () + 1, passesError)
            passes = Measurement (passes, passesError)

            eff = passes / total if total > 0.0 else 0.0
            print("P (pass HEM 15/16 veto): " + str (eff))
            return eff

        else:
            print("TagPt35MetTrig(HEMveto) or TrigEffNumer(HEMveto) are not defined. Not printing P (pass HEM veto)...")
            return (float ("nan"), float ("nan"))

    def getPpassHEMveto (self):
        return self.printPpassHEMveto ()

    def printPpassMetTriggers (self):
        if hasattr (self, "TagPt35") and (hasattr (self, "TagPt35MetTrig") or (hasattr (self, "TrigEffDenom") and hasattr (self, "TrigEffNumer"))):
            triggerEffTotalHist = triggerEffPassesHist = l1TotalHist = l1PassesHist = None
            total = 0.0
            passes = 0.0

            # Get the metNoMu (modified)
            # Get the denominator/numerator of the trigger efficiency
            if not self._useOnlineQuantitiesForPpassMetTriggers:
                channel = self.TrigEffDenom if hasattr (self, "TrigEffDenom") else self.TagPt35
                hist = "Met Plots/metNoMu"
                triggerEffTotalHist = getHistFromChannelDict (channel, hist)
                if "extensions" in channel:
                    for x in channel["extensions"]:
                        triggerEffTotalHist.Add (getHist (x["sample"], x["condorDir"], x["name"] + "Plotter", hist))

                channel = self.TrigEffNumer if hasattr (self, "TrigEffNumer") else self.TagPt35MetTrig
                triggerEffPassesHist = getHistFromChannelDict (channel, hist)
                if "extensions" in channel:
                    for x in channel["extensions"]:
                        triggerEffPassesHist.Add (getHist (x["sample"], x["condorDir"], x["name"] + "Plotter", hist))
            else:
                hist = self._Flavor + "-eventvariable Plots/passesMETTriggersWithout" + self._Flavor + "Vs" + self._Flavor + "MetNoMuMinusOnePt"
                trigEffHist = getHistFromChannelDict (self.TagPt35MetTrig, hist)
                addChannelExtensions(trigEffHist, self.TagPt35MetTrig, hist)

                triggerEffTotalHist = trigEffHist.ProjectionX ()
                triggerEffTotalHist.SetDirectory (0)
                triggerEffTotalHist.SetName ("total")

                trigEffHist.GetYaxis ().SetRangeUser (1.0, 2.0)
                triggerEffPassesHist = trigEffHist.ProjectionX ()
                triggerEffPassesHist.SetDirectory (0)
                triggerEffPassesHist.SetName ("passes")

                if hasattr (self, "TagPt35MetL1Trig"):
                    hist = self._Flavor + "-eventvariable Plots/passesL1ETMWithout" + self._Flavor + "Vs" + self._Flavor + "MetNoMuMinusOnePt"
                    l1TrigEffHist = getHistFromChannelDict (self.TagPt35MetL1Trig, hist)
                    addChannelExtensions(l1TrigEffHist, self.TagPt35MetL1Trig, hist)

                    l1TotalHist = l1TrigEffHist.ProjectionX ()
                    l1TotalHist.SetDirectory (0)
                    l1TotalHist.SetName ("l1Total")
                    l1PassesHist = l1TotalHist.Clone ("l1PassesHist")
                    l1PassesHist.SetDirectory (0)
                    l1PassesHist.SetName ("l1PassesHist")

                    progressIndicator = ProgressIndicator ("calculating L1 trigger efficiency")
                    progressIndicator.printProgress ()

                    for x in range (1, l1TrigEffHist.GetXaxis ().GetNbins () + 1):
                        progressIndicator.setPercentDone ((x / float (l1TrigEffHist.GetXaxis ().GetNbins ())) * 100.0)
                        progressIndicator.printProgress ()

                        nFail = Measurement (l1TrigEffHist.GetBinContent (x, 1), l1TrigEffHist.GetBinError (x, 1))
                        nPass = Measurement (0.0, 0.0)
                        for y in range (2, l1TrigEffHist.GetYaxis ().GetNbins () + 1):
                            prescale = l1TrigEffHist.GetYaxis ().GetBinLowEdge (y)
                            n = Measurement (l1TrigEffHist.GetBinContent (x, y), l1TrigEffHist.GetBinError (x, y))
                            nPass += n
                            nFail += n * (prescale - 1.0)
                        nTotal = nFail + nPass

                        l1TotalHist.SetBinContent (x, nTotal.centralValue ())
                        l1TotalHist.SetBinError (x, nTotal.maxUncertainty ())
                        l1PassesHist.SetBinContent (x, nPass.centralValue ())
                        l1PassesHist.SetBinError (x, nPass.maxUncertainty ())

                    progressIndicator.printProgress (True)

            hist = self._Flavor + "-eventvariable Plots/deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt"
            metHist2D = getHistFromChannelDict (self.TagPt35, hist)
            addChannelExtensions(metHist2D, self.TagPt35, hist)

            metHist2D.GetYaxis ().SetRangeUser (self._phiCut, 4.0)
            metHist = metHist2D.ProjectionX ("metHist")

            self.plotTriggerEfficiency (triggerEffPassesHist, triggerEffTotalHist, "HLT")
            if l1PassesHist and l1TotalHist:
                self.plotTriggerEfficiency (l1PassesHist, l1TotalHist, "L1")
                triggerEffPassesHist.Multiply (l1PassesHist)
                triggerEffTotalHist.Multiply (l1TotalHist)
                self.plotTriggerEfficiency (triggerEffPassesHist, triggerEffTotalHist, "Full")
            triggerEffPassesHist.Divide (triggerEffTotalHist)
            metHist.Multiply (triggerEffPassesHist)

            total = 0.0
            totalError = ctypes.c_double (0.0)
            passesError = ctypes.c_double (0.0)

            passes = metHist.IntegralAndError (metHist.FindBin (self._metCut), metHist.GetNbinsX () + 1, passesError)
            passes = Measurement (passes, passesError)
            passes.isPositive ()

            #met = self.getHistFromProjectionZ (self.TagPt35["sample"], self.TagPt35["condorDir"], self.TagPt35["name"] + "Plotter", self._metMinusOneHist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
            hist = self._Flavor + "-eventvariable Plots/deltaPhiMetJetLeadingVs" + self._Flavor + "MetNoMuMinusOnePt"
            met = getHistFromChannelDict (self.TagPt35, hist)
            addChannelExtensions(met, self.TagPt35, hist)

            totalError = ctypes.c_double (0.0)
            total = met.IntegralAndError (met.GetXaxis ().FindBin (self._metCut), met.GetNbinsX () + 1, met.GetYaxis ().FindBin (self._phiCut), met.GetNbinsY () + 1, totalError)
            total = Measurement (total, totalError)
            total.isPositive ()

            eff = passes / total if total > 0.0 else 0.0
            print("P (pass met triggers): " + str (eff))
            return (eff, triggerEffPassesHist)
        else:
            print("TagPt35 and TagPt35MetTrig not both defined. Not printing P (pass met triggers)...")
            return (float ("nan"), float ("nan"))

    def plotTriggerEfficiency (self, passesHist, totalHist, label = ""):
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
            setAxisStyle (metGraph, "E_{T}^{miss, no #mu} [GeV]", label + " trigger efficiency", (0.0, 500.0), (0.0, 1.4))
            pt.Draw ("same")
            cmsLabel.Draw ("same")
            lumiLabel.Draw ("same")
            self._fout.cd ()
            self._canvas.Write ("triggerEfficiency_" + label)
        else:
            print("A TFile and TCanvas must be added. Not making plots...")

    def printNback (self):
        self.plotMetForNback ()
        if hasattr (self, "CandTrkIdPt35"):
            if dataFormat == 'MINI_AOD_ONLY_2022_CUSTOM':
                hist = "Track Plots/trackCaloJetEnergy" # This is for the MiniAOD only approach
            else:
                hist = "Track Plots/trackCaloTot_RhoCorr" # This is for the AOD+MiniAOD approach
            eCalo = getHistFromChannelDict (self.CandTrkIdPt35, hist)
            addChannelExtensions(eCalo, self.CandTrkIdPt35, hist)

            nError = ctypes.c_double (0.0)
            n = eCalo.IntegralAndError (0, eCalo.FindBin (self._eCaloCut), nError)
            w = self.CandTrkIdPt35["weight"]
            nError = nError.value

            n /= w
            nError /= w
            n = Measurement (n * w, (nError if n != 0.0 else up68) * w)
            n *= self._prescale

            print("N_back: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)")
            return n
        else:
            print("CandTrkIdPt35 not defined. Not printing N_back...")
            return float ("nan")

    def plotMetForNback (self):
        if hasattr (self, "CandTrkIdPt35"):
            if self._fout and self._canvas:
                hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                met = self.getHistFromProjectionZ (self.CandTrkIdPt35["sample"], self.CandTrkIdPt35["condorDir"], self.CandTrkIdPt35["name"] + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu")
                if not isinstance(met, TObject):
                    print("Warning [plotMetForNback]: Could not get required hists from sample=", self.CandTrkIdPt35["sample"], "condorDir=", self.CandTrkIdPt35["condorDir"], "name=", self.CandTrkIdPt35["name"])
                    return
                if "extensions" in self.CandTrkIdPt35:
                    for x in self.CandTrkIdPt35["extensions"]:
                        met.Add (self.getHistFromProjectionZ (x["sample"], x["condorDir"], x["name"] + "Plotter", hist, alternate1DHist = "Met Plots/metNoMu"))

                # explicitly get metNoMuMinusOne instead of using
                # _metMinusOneHist since we plot both metNoMu and
                # metNoMuMinusOne here
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                hist = "Track-" + self._flavor + " Plots/" + self._flavor + "NoMuMinusOnePtVsMaxSigmaForFiducialTracks"
                metMinusOne = self.getHistFromProjectionZ (self.CandTrkIdPt35["sample"], self.CandTrkIdPt35["condorDir"], self.CandTrkIdPt35["name"] + "Plotter", hist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt")
                if not isinstance(metMinusOne, TObject):
                    print("Warning [plotMetForNback]: Could not get required hists from sample=", self.CandTrkIdPt35["sample"], "condorDir=", self.CandTrkIdPt35["condorDir"], "name=", self.CandTrkIdPt35["name"])
                    return
                if "extensions" in self.CandTrkIdPt35:
                    for x in self.CandTrkIdPt35["extensions"]:
                        metMinusOne.Add (self.getHistFromProjectionZ (x["sample"], x["condorDir"], x["name"] + "Plotter", hist, alternate1DHist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"))

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
                print("A TFile and TCanvas must be added. Not making plots...")
        else:
            print("CandTrkIdPt35 not defined. Not plotting MET for N_back...")

    def makePassesConsistentWithTotal (self, passes, total):
        for i in range (0, passes.GetNbinsX () + 2):
            if passes.GetBinContent (i) > total.GetBinContent (i):
                passes.SetBinContent (i, total.GetBinContent (i))
                passes.SetBinError (i, total.GetBinError (i))

    def printNest (self):
        nCtrl = self.printNctrl ()
        pPassVeto, passes, scaleFactor, total = self.printPpassVetoTagProbe ()
        pPassMetCut = self.printPpassMetCut ()
        pPassMetTriggers, triggerEfficiency = self.printPpassMetTriggers ()

        if not hasattr (pPassVeto, "centralValue"):
            pPassVeto = self.printPpassVeto ()

        nEst = nCtrl * scaleFactor * pPassVeto * pPassMetCut * pPassMetTriggers

        if self._useExternalTriggerEfficiency and hasattr (self, 'externalTriggerEfficiency'):
            nEst /= self.externalTriggerEfficiency

        if (hasattr (self, "TagPt35MetTrigHEMveto") and hasattr (self, "TagPt35MetTrig")) or (hasattr (self, "TrigEffNumerHEMveto") and hasattr (self, "TrigEffNumer")):
            print("Applying HEM 15/16 veto")
            pPassHEMveto = self.printPpassHEMveto ()
            nEst *= pPassHEMveto

        nEst.isPositive ()

        #print("Types in alpha", type(scaleFactor), type(pPassVeto), type(pPassMetCut), type(pPassMetTriggers))
        #print("Debugging: \n\t pPassVeto {} \n\t passes {} \n\t scaleFactor {} \n\t total {} \n\t pPassMetCut {} \n\t pPassMetTriggers {}".format(str(pPassVeto), str(passes), str(scaleFactor), str(total), str(pPassMetCut), str(pPassMetTriggers)))

        alpha = scaleFactor * pPassVeto * pPassMetCut * pPassMetTriggers
        #print("Debugging, alpha after construction {}".format(str(alpha)))
        if self._useExternalTriggerEfficiency and hasattr (self, 'externalTriggerEfficiency'):
            alpha /= self.externalTriggerEfficiency        
        if (hasattr (self, "TagPt35MetTrigHEMveto") and hasattr (self, "TagPt35MetTrig")) or (hasattr (self, "TrigEffNumerHEMveto") and hasattr (self, "TrigEffNumer")):
            alpha *= pPassHEMveto
        alpha.isPositive ()
        alpha.printLongFormat ()

        if alpha.centralValue () > 0:
            print("N: " + str (nCtrl))
        else:
            print('INFO: one of the estimate probabilities is zero, so alpha would be zero.')
            print('      Instead giving N as the P(veto) numerator, and alpha to match.')
            if (self._flavor == "electron" or self._flavor == "muon") and not self._useHistogramsForPpassVeto:
                alpha = (scaleFactor / (2.0 * total)) * nCtrl * pPassMetCut * pPassMetTriggers
            else:
                alpha = (scaleFactor / total) * nCtrl * pPassMetCut * pPassMetTriggers
            print("N: " + str (passes))

        #print("Alpha is of type", type(alpha))
        print("alpha: " + str (alpha))
        if alpha.centralValue () > 0:
            if alpha.uncertaintyDown () == alpha.uncertaintyUp ():
                print("error on alpha: " + str (1.0 + (alpha.uncertainty () / alpha.centralValue ())))
            else:
                print("error on alpha: " + str (1.0 - (alpha.uncertaintyDown () / alpha.centralValue ())) + " / " + str (1.0 + (alpha.uncertaintyUp () / alpha.centralValue ())))
        else:
            print('WARNING: alpha STILL ended up as zero, so no relative error can be printed.')

        print("N_est: " + str (nEst) + " (" + str (nEst / self._luminosityInInvFb) + " fb)")
        return nEst

    def getPpassMetCut (self):
        return self.printPpassMetCut ()

    def getPpassMetTriggers (self):
        return self.printPpassMetTriggers ()

    def printNestCombinedMet (self, pPassMetCut, pPassMetTriggers, pPassHEMveto = None):
        nCtrl = self.printNctrl ()
        pPassVeto, passes, scaleFactor, total = self.printPpassVetoTagProbe ()

        if not hasattr (pPassVeto, "centralValue"):
            pPassVeto = self.printPpassVeto ()

        nEst = nCtrl * scaleFactor * pPassVeto * pPassMetCut * pPassMetTriggers
        if self._useExternalTriggerEfficiency and hasattr (self, 'externalTriggerEfficiency'):
            nEst /= self.externalTriggerEfficiency
        if pPassHEMveto != None:
            nEst *= pPassHEMveto
        nEst.isPositive ()

        alpha = scaleFactor * pPassVeto * pPassMetCut * pPassMetTriggers
        if self._useExternalTriggerEfficiency and hasattr (self, 'externalTriggerEfficiency'):
            alpha /= self.externalTriggerEfficiency
        if pPassHEMveto != None:
            alpha *= pPassHEMveto
        alpha.isPositive ()
        alpha.printLongFormat ()

        if alpha.centralValue () > 0:
            print("N: " + str (nCtrl))
        else:
            print('INFO: one of the estimate probabilities is zero, so alpha would be zero.')
            print('      Instead giving N as the P(veto) numerator, and alpha to match.')
            if (self._flavor == "electron" or self._flavor == "muon") and not self._useHistogramsForPpassVeto:
                alpha = (scaleFactor / (2.0 * total)) * nCtrl * pPassMetCut * pPassMetTriggers
            else:
                alpha = (scaleFactor / total) * nCtrl * pPassMetCut * pPassMetTriggers
            print("N: " + str (passes))

        print("alpha: " + str (alpha))
        if alpha.centralValue () > 0:
            if alpha.uncertaintyDown () == alpha.uncertaintyUp ():
                print("error on alpha: " + str (1.0 + (alpha.uncertainty () / alpha.centralValue ())))
            else:
                print("error on alpha: " + str (1.0 - (alpha.uncertaintyDown () / alpha.centralValue ())) + " / " + str (1.0 + (alpha.uncertaintyUp () / alpha.centralValue ())))
        else:
            print('WARNING: alpha ended up as zero, so no relative error can be printed.')

        print("N_est: " + str (nEst) + " (" + str (nEst / self._luminosityInInvFb) + " fb)")
        return nEst

    def printPpassVetoTagProbe (self):
        self.plotPpassVeto ()
        if not hasattr (self._pPassVeto, "centralValue"):
            if hasattr (self, "TagProbe") and hasattr (self, "TagProbePass"):
                total = None
                passes = None
                if not self._useHistogramsForPpassVeto:
                    total       = self.TagProbe["yield"]
                    passes      = self.TagProbePass["yield"]
                else:
                    hist = "Eventvariable Plots/nGoodTPPairs"
                    totalHist = getHistFromChannelDict (self.TagProbe, hist)
                    addChannelExtensions(totalHist, self.TagProbe, hist)

                    totalBackgroundExists = True

                    hist = "Eventvariable Plots/nGoodSSTPPairs"
                    totalBackgroundHist = getHistFromChannelDict (self.TagProbe, hist)
                    if not isinstance(totalBackgroundHist, TObject):
                        print("Warning [printPpassVetoTagProbe]: Could not get nGoodSSTPPairs histogram from sample=", self.TagProbe["sample"], "condorDir=", self.TagProbe["condorDir"], "name=", self.TagProbe["name"], "-- ignoring this subtraction!")
                        totalBackgroundExists = False
                    if totalBackgroundExists:
                        addChannelExtensions(totalBackgroundHist, self.TagProbe, hist)

                    hist = "Eventvariable Plots/nProbesPassingVeto"
                    passesHist = getHistFromChannelDict (self.TagProbePass, hist)
                    addChannelExtensions(passesHist, self.TagProbePass, hist)

                    total = 0.0
                    totalBackground = 0.0
                    passes = 0.0

                    totalError = 0.0
                    totalBackgroundError = 0.0
                    passesError = 0.0

                    # there could be more than one pair so add N(1) + 2*N(2) + 3*N(3) + ...
                    for ibin in range (2, totalHist.GetNbinsX () + 1):
                        total += (ibin-1) * totalHist.GetBinContent (ibin)
                        totalError = math.hypot (totalError, (ibin-1) * totalHist.GetBinError (ibin))

                        if totalBackgroundExists:
                            totalBackground += (ibin-1) * totalBackgroundHist.GetBinContent (ibin)
                            totalBackgroundError = math.hypot (totalBackgroundError, (ibin-1) * totalBackgroundHist.GetBinError (ibin))

                        passes += (ibin-1) * passesHist.GetBinContent (ibin)
                        passesError = math.hypot (passesError, (ibin-1) * passesHist.GetBinError (ibin))

                    total = Measurement (total, totalError)
                    totalBackground = Measurement (totalBackground, totalBackgroundError)
                    passes = Measurement (passes, passesError if passes != 0.0 else up68)

                passes1 = Measurement (0.0, 0.0)

                if hasattr (self, "TagProbe1") and hasattr (self, "TagProbePass1"):
                    if not self._useHistogramsForPpassVeto:
                        total        += self.TagProbe1["yield"]
                        if "extensions" in self.TagProbe1:
                            for x in self.TagProbe1["extensions"]:
                                total += x["yield"]
                        passes1       = self.TagProbePass1["yield"]
                        if "extensions" in self.TagProbePass1:
                            for x in self.TagProbePass1["extensions"]:
                                passes1 += x["yield"]
                    else:
                        hist = "Eventvariable Plots/nGoodTPPairs"
                        totalHist = getHistFromChannelDict (self.TagProbe1, hist)
                        addChannelExtensions(totalHist, self.TagProbe1, hist)

                        totalBackgroundExists = True
                        hist = "Eventvariable Plots/nGoodSSTPPairs"
                        totalBackgroundHist = getHistFromChannelDict(self.TagProbe1, hist)
                        if not isinstance(totalBackgroundHist, TObject):
                            print("Warning [printPpassVetoTagProbe]: Could not get nGoodSSTPPairs histogram from sample=", self.TagProbe["sample"], "condorDir=", self.TagProbe["condorDir"], "name=", self.TagProbe["name"], "-- ignoring this subtraction!")
                            totalBackgroundExists = False
                        addChannelExtensions(totalBackgroundHist, self.TagProbe1, hist)

                        hist = "Eventvariable Plots/nProbesPassingVeto"
                        passesHist = getHistFromChannelDict (self.TagProbePass1, hist)
                        addChannelExtensions(passesHist, self.TagProbePass1, hist)

                        total1 = 0.0
                        totalBackground1 = 0.0
                        passes1 = 0.0

                        total1Error = 0.0
                        totalBackground1Error = 0.0
                        passes1Error = 0.0

                        # there could be more than one pair so add N(1) + 2*N(2) + 3*N(3) + ...
                        for ibin in range (2, totalHist.GetNbinsX () + 1):
                            total1 += (ibin-1) * totalHist.GetBinContent (ibin)
                            total1Error = math.hypot (total1Error, (ibin-1) * totalHist.GetBinError (ibin))

                            if totalBackgroundExists:
                                totalBackground1 += (ibin-1) * totalBackgroundHist.GetBinContent (ibin)
                                totalBackground1Error = math.hypot (totalBackground1Error, (ibin-1) * totalBackgroundHist.GetBinError (ibin))

                            passes1 += (ibin-1) * passesHist.GetBinContent (ibin)
                            passes1Error = math.hypot (passes1Error, (ibin-1) * passesHist.GetBinError (ibin))

                        total += Measurement (total1, total1Error)
                        totalBackground += Measurement (totalBackground1, totalBackground1Error)
                        passes1 = Measurement (passes1, passes1Error if passes1 != 0.0 else up68)

                background = Measurement (0.0, 0.0)
                if hasattr (self, "TagProbePassSS"):
                    hist = "Met Plots/metNoMu"
                    backgroundHist = getHistFromChannelDict (self.TagProbePassSS, hist)
                    addChannelExtensions(backgroundHist, self.TagProbePassSS, hist)

                    backgroundError = ctypes.c_double (0.0)
                    background = backgroundHist.IntegralAndError (0, backgroundHist.GetNbinsX () + 1, backgroundError)
                    background = Measurement (background, backgroundError.value)
                background1 = Measurement (0.0, 0.0)
                if hasattr (self, "TagProbePassSS1"):
                    hist = "Met Plots/metNoMu"
                    backgroundHist = getHistFromChannelDict (self.TagProbePassSS1, hist)
                    addChannelExtensions(backgroundHist, self.TagProbePassSS1, hist)

                    backgroundError = ctypes.c_double (0.0)
                    background1 = backgroundHist.IntegralAndError (0, backgroundHist.GetNbinsX () + 1, backgroundError)
                    background1 = Measurement (background1, backgroundError)

                if hasattr (self, "TagProbePass1"):
                    print('P_veto := (', passes.centralValue(), '+', passes1.centralValue(), '-', background.centralValue(), '-', background1.centralValue(), ') / (', total.centralValue(), '-', totalBackground.centralValue(), ')')
                else:
                    print('P_veto := (', passes.centralValue(), '-', background.centralValue(), ') / (', total.centralValue(), '-', totalBackground.centralValue(), ')')

                # apply same-sign subtraction
                passes -= background
                passes1 -= background1

                if passes < 0:
                    print('INFO: same-sign subtraction in TagProbePass is negative. Using 0 + 1.1 - 0 for the P(veto) numerator instead!')
                    passes = Measurement (0.0, 0.0, up68)
                if passes1 < 0:
                    print('INFO: same-sign subtraction in TagProbePass1 is negative. Using 0 + 1.1 - 0 for the P(veto) numerator instead!')
                    passes1 = Measurement (0.0, 0.0, up68)

                total -= totalBackground
                if total <= 0:
                    print('Warning: same-sign subtraction is non-positive in the denominator?! Thats impressive but you messed up.')
                    sys.exit()

                passes.isPositive ()
                passes1.isPositive ()
                total.isPositive ()

                scaledPasses = passes * self._tagProbePassScaleFactor + passes1 * self._tagProbePass1ScaleFactor
                p = passes
                sf = Measurement (self._tagProbePassScaleFactor, 0.0)
                if scaledPasses > 0.0:
                    p = (scaledPasses * scaledPasses) / (passes * self._tagProbePassScaleFactor * self._tagProbePassScaleFactor + passes1 * self._tagProbePass1ScaleFactor * self._tagProbePass1ScaleFactor)
                    sf = (passes * self._tagProbePassScaleFactor * self._tagProbePassScaleFactor + passes1 * self._tagProbePass1ScaleFactor * self._tagProbePass1ScaleFactor) / scaledPasses
                    p.setUncertainty (math.sqrt (p.centralValue ()))
                    sf.setUncertainty (0.0)

                if (self._flavor == "electron" or self._flavor == "muon") and not self._useHistogramsForPpassVeto:
                    eff = scaledPasses / (2.0 * total - scaledPasses)
                else:
                    eff = scaledPasses / total

                print("P (pass lepton veto) in tag-probe sample: " + str (eff))
                #print("Debugging P {}, Eff {}".format(str(p), str(eff)))
                return (eff, p, sf, total)
            else:
                print("TagProbe and TagProbePass not both defined.  Not printing lepton veto efficiency...")
                return (float ("nan"), float ("nan"), float ("nan"), float ("nan"))
        else:
            print("P (pass lepton veto) from user input: " + str (self._pPassVeto))
            return (self._pPassVeto, float ("nan"), float ("nan"), float ("nan"))

    def plotPpassVeto (self):
        if hasattr (self, "TagProbe") and hasattr (self, "TagProbePass"):
            if self._fout and self._canvas:
                hist = "Track Plots/trackPt"
                trackPt = getHistFromChannelDict (self.TagProbe, hist)
                addChannelExtensions(trackPt, self.TagProbe, hist)

                trackPtPass = getHistFromChannelDict (self.TagProbePass, hist)
                addChannelExtensions(trackPtPass, self.TagProbePass, hist)

                if hasattr (self, "TagProbe1") and hasattr (self, "TagProbePass1"):
                    hist = "Track Plots/trackPt"
                    trackPt1 = getHistFromChannelDict (self.TagProbe1, hist)
                    addChannelExtensions(trackPt1, self.TagProbe1, hist)

                    trackPtPass1 = getHistFromChannelDict (self.TagProbePass1, hist)
                    addChannelExtensions(trackPtPass1, self.TagProbePass1, hist)

                    trackPt.Add (trackPt1)
                    trackPtPass.Add (trackPtPass1)

                invMass = None
                invMassPass = None
                if self._flavor != "tau":
                    hist = "Track-" + self._flavor + " Plots/invMassNearZ"
                    invMass = getHistFromChannelDict (self.TagProbe, hist)
                    addChannelExtensions(invMass, self.TagProbe, hist)

                    invMassPass = getHistFromChannelDict (self.TagProbePass, hist)
                    addChannelExtensions(invMassPass, self.TagProbePass, hist)

                    if hasattr (self, "TagProbe1") and hasattr (self, "TagProbePass1"):
                        hist = "Track-" + self._flavor + " Plots/invMassNearZ"
                        invMass1 = getHistFromChannelDict (self.TagProbe1, hist)
                        addChannelExtensions(invMass1, self.TagProbe1, hist)

                        invMassPass1 = getHistFromChannelDict (self.TagProbePass1, hist)
                        addChannelExtensions(invMassPass1, self.TagProbePass1, hist)

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
                print("A TFile and TCanvas must be added. Not making plots...")
        else:
            print("Neither TagProbe nor TagProbePass defined. Not plotting P_veto pt dependence...")

# Gaussian function for fitting d0 distribution
def gaussian (x, par):
    return TMath.Gaus (x[0], 0.0, par[0]) * par[1] + par[2]

def flatFunction (x, par):
    return par[0]

def getIntegralError (f, a, b):
    integralError = ctypes.c_double (0.0)
    nominal = f.IntegralOneDim (a, b, 1.0e-12, 1.0e-2, integralError)

    pars = []
    for i in range(f.GetNumberFreeParameters()):
        pars.append(f.GetParameter(i))

    # Increasing each of the parameters should increase the integral
    for i, par in enumerate(pars):
        f.SetParameter(i, par + f.GetParError(i))
    up = f.IntegralOneDim (a, b, 1.0e-12, 1.0e-2, integralError)

    # Decreasing each of the parameters should increase the integral
    for i, par in enumerate(pars):
        f.SetParameter(i, par - f.GetParError(i))
    down = f.IntegralOneDim (a, b, 1.0e-12, 1.0e-2, integralError)

    for i, par in enumerate(pars):
        f.SetParameter(i, par)

    return max (abs (up - nominal), abs (down - nominal))

class FakeTrackBkgdEstimate:
    _fout = None
    _canvas = None
    _prescale = 1.0
    _luminosityInInvFb = float ("nan")
    _nHits = None
    _minD0 = 0.02
    _maxD0 = 0.1
    _reweightPileupToBasic = False
    _useFlatD0Fit = False

    def __init__ (self):
        pass

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addPrescaleFactor (self, prescale):
        self._prescale = prescale

    def addLuminosityInInvPb (self, luminosityInInvPb):
        self._luminosityInInvFb = luminosityInInvPb / 1000.0

    def addNHits (self, nHits):
        self._nHits = nHits

    def addMinD0 (self, minD0):
        self._minD0 = minD0

    def addMaxD0 (self, maxD0):
        self._maxD0 = maxD0

    def doReweightPileupToBasic (self, doReweight):
        self._reweightPileupToBasic = doReweight

    def setUseFlatD0Fit (self, doUseFlat):
        self._useFlatD0Fit = doUseFlat

    def addChannel (self, role, name, sample, condorDir, verbose = True):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        n, nError = getHistIntegral (sample, condorDir, name + "Plotter", "Met Plots/metNoMu", 0.0, 99999.0)
        channel["yield"] = Measurement (n, nError)
        channel["yield"].isPositive ()
        setattr (self, role, channel)
        if verbose: print("yield for " + name + ": " + str (channel["yield"]))

    def printTransferFactor (self, verbose = True):

        if self._useFlatD0Fit:
            transferFactor = self._minD0 / (self._maxD0 - self._minD0)
            passes = 2.0 * (self._maxD0 - self._minD0)
            fails = 2.0 * self._minD0
            if verbose:
                print('Transfer factor (flat): (' + str (passes) + ') / ' + str (fails) + ') = ' + str (transferFactor))
            return (transferFactor, passes, fails, 0.0, 0.0)

        if hasattr (self, "Basic3hits"):
            d0 = getHistFromChannelDict (self.Basic3hits, "Track-eventvariable Plots/trackd0WRTPV")
            d0Mag = getHistFromChannelDict (self.Basic3hits, "Track-eventvariable Plots/trackd0WRTPVMag")
            d0Mag.Scale (0.5)

            f = TF1 ("gaussian", gaussian, -1.0, 1.0, 3)
            f.SetParameter (0, 0.2)
            f.SetParLimits (0, 1.0e-3, 1.0e3)
            f.SetParName (0, "Gaussian sigma")
            f.SetParameter (1, 40.0)
            f.SetParLimits (1, 1.0e-3, 1.0e3)
            f.SetParName (1, "Gaussian norm")
            if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
              f.SetParameter (2, 1.0)
              f.SetParLimits (2, 1.0e-3, 1.0e3)
              f.SetParName (2, "constant")
            else:
              f.SetParameter (2, 20.0)
              f.SetParLimits (2, -1.0e3, 1.0e3)
              f.SetParName (2, "constant")
            for i in range (0, 10):
                d0Mag.Fit (f, "LQEMN", "", 0.1, 1.0)
            d0Mag.Fit (f, "LEMN", "", 0.1, 1.0)

            if self._fout.IsOpen():
                self._fout.cd ()
                d0.Write ("d0")
                f.Write ("d0_fit")

            d0Mag.Scale (2.0)
            for i in range (0, 10):
                d0Mag.Fit (f, "LQEMN", "", 0.1, 1.0)

            passesError = ctypes.c_double (0.0)
            passes = f.IntegralOneDim (0.0, 0.02, 1.0e-12, 1.0e-2, passesError)
            passesError = getIntegralError (f, 0.0, 0.02)
            failsError = ctypes.c_double (0.0)
            fails = f.IntegralOneDim (self._minD0, self._maxD0, 1.0e-12, 1.0e-2, failsError)
            failsError = getIntegralError (f, self._minD0, self._maxD0)

            passes = Measurement (passes, 0.0)
            fails = Measurement (fails, 0.0)

            passes.isPositive ()
            fails.isPositive ()

            if fails > 0.0:
                transferFactor = passes / fails
                if verbose: print("Transfer factor: (" + str (passes) + ") / (" + str (fails) + ") = " + str (transferFactor))
                return (transferFactor, passes, fails, passesError, failsError)
            else:
                if verbose: print("N(fail d0 cut, 3 hits) = 0, not printing scale factor...")
                return (float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"))

        else:
            if verbose: print("Basic3hits is not defined. Not printing transfer factor...")
            return (float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"))

    def printNctrl (self, verbose = True):
        if hasattr (self, "DisTrkInvertD0"):
            hits = getHistFromChannelDict (self.DisTrkInvertD0, "Track Plots/trackLayersWithMeasurementVsPixelHits")
            if self._nHits !=  None:
                if self._nHits >= 6:
                    nError = ctypes.c_double (0.0)
                    n = hits.IntegralAndError (hits.GetXaxis ().FindBin (4.0), hits.GetXaxis ().FindBin (99.0), hits.GetYaxis ().FindBin (6.0), hits.GetYaxis ().FindBin (99.0), nError)
                    n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                    n.isPositive ()
                if self._nHits == 5:
                    nError = ctypes.c_double (0.0)
                    n = hits.IntegralAndError (hits.GetXaxis ().FindBin (4.0), hits.GetXaxis ().FindBin (99.0), hits.GetYaxis ().FindBin (5.0), hits.GetYaxis ().FindBin (5.0), nError)
                    n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                    n.isPositive ()
                if self._nHits == 4:
                    nError = ctypes.c_double (0.0)
                    n = hits.IntegralAndError (hits.GetXaxis ().FindBin (4.0), hits.GetXaxis ().FindBin (99.0), hits.GetYaxis ().FindBin (4.0), hits.GetYaxis ().FindBin (4.0), nError)
                    n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                    n.isPositive ()
            else:
                n, nError = getHistIntegral (self.DisTrkInvertD0["sample"], self.DisTrkInvertD0["condorDir"], self.DisTrkInvertD0["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                n.isPositive ()

            pFake = float ("nan")
            norm = 1.0

            # For ZtoMuMu control regions, need to normalize to BasicSelection
            if hasattr (self, "ZtoLL") and hasattr (self, "Basic"):
                norm = self.Basic["yield"] / self.ZtoLL["yield"]
                pFake = n / self.ZtoLL["yield"]

                if self._reweightPileupToBasic:
                    histName = 'Eventvariable Plots/numPVReco'
                    puWeights = getHistFromChannelDict(self.Basic, histName)
                    puZtoLL = getHistFromChannelDict(self.ZtoLL, histName)
                    puWeights.Scale(1.0 / puWeights.Integral(0, -1))
                    puZtoLL.Scale(1.0 / puZtoLL.Integral(0, -1))
                    puWeights.Divide(puZtoLL)

                    puBkgd = getHistFromChannelDict(self.DisTrkInvertD0, histName)
                    nReweighted = 0.0
                    nReweightedErr = 0.0
                    for ibin in range(puBkgd.GetNbinsX() + 1):
                        nReweighted += puWeights.GetBinContent(ibin+1) * puBkgd.GetBinContent(ibin+1)
                        if puWeights.GetBinContent(ibin+1) > 0.0 and puBkgd.GetBinContent(ibin+1) > 0.0:
                            nReweightedErr += (puWeights.GetBinContent(ibin+1) * puBkgd.GetBinContent(ibin+1) * 
                                               math.hypot(puWeights.GetBinError(ibin+1) / puWeights.GetBinContent(ibin+1), 
                                                          puBkgd.GetBinError(ibin+1) / puBkgd.GetBinContent(ibin+1))
                                               ) ** 2
                    nReweighted = Measurement(nReweighted, math.sqrt(nReweightedErr))
                    print('Reweighting pileup to BasicSelection, overall weight =', nReweighted, '/', self.DisTrkInvertD0["yield"], '=', nReweighted / self.DisTrkInvertD0["yield"])
                    pFake = nReweighted / self.ZtoLL["yield"]
            elif hasattr (self, "Basic"):
                pFake = n / self.Basic["yield"]

            nRaw = n
            n *= norm
            n *= self._prescale

            if verbose:
                print("N_ctrl: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)")
                print("P_fake^raw: " + str (pFake))
            return (n, nRaw, norm, pFake)
        else:
            if verbose: print("DisTrkInvertD0 is not defined. Not printing N_ctrl...")
            return (float ("nan"), float ("nan"))

    def printNest (self, verbose = True):
        xi, xiPass, xiFail, xiPassError, xiFailError = self.printTransferFactor (verbose)
        nCtrl, nRaw, norm, pFake = self.printNctrl (verbose)

        pFake *= xi

        N = nRaw
        alpha = norm * self._prescale * (xiPass / xiFail)

        nEst = xi * nCtrl
        nEst.isPositive ()

        errorFromFit = nCtrl.centralValue () * math.sqrt (xiFailError * xiFailError * xiPass.centralValue () * xiPass.centralValue () + xiPassError * xiPassError * xiFail.centralValue () * xiFail.centralValue ()) / (xiFail.centralValue () * xiFail.centralValue ())

        if verbose:
            alpha.printLongFormat ()
            print("P_fake: " + str (pFake))
            print("N: " + str (N))
            print("alpha: " + str (alpha))
            print("error on alpha: " + str ((1.0 + (alpha.maxUncertainty () / alpha.centralValue ())) if alpha != 0.0 else float ("nan")))
            print("N_est: " + str (nEst) + " (" + str (nEst / self._luminosityInInvFb) + " fb)")
            print("error from fit: " + str ((1.0 + (errorFromFit / nEst.centralValue ())) if nEst.centralValue () > 0.0 else float ("nan")))

        return nEst, pFake

    def printNback (self, verbose = True):
        if hasattr (self, "DisTrkIdFake"):
            n = self.DisTrkIdFake["yield"]

            if verbose: print("N_back: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)")
            return n
        else:
            if verbose: print("DisTrkIdFake not defined. Not printing N_back...")
            return float ("nan")

class FakeTrackBkgdOptimizer(FakeTrackBkgdEstimate):
    def __init__ (self):
        FakeTrackBkgdEstimate.__init__(self)

    def addChannel (self, role, name, sample, condorDir, verbose = True):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        n, nError = getHistIntegral (sample, condorDir, name + "Plotter", "Met Plots/metNoMu", 0.0, 99999.0)
        channel["yield"] = Measurement (n, nError)
        channel["yield"].isPositive ()
        setattr (self, role, channel)
        if verbose: print("yield for " + name + ": " + str (channel["yield"]))

    def addTrees(self, role, treeName, filePaths):
        _chain = TChain(treeName)
        for x in glob.glob(filePaths + '/*/hist_*.root'):
            _chain.Add(x)
        print('Added ' + str(_chain.GetEntries()) + ' events for role ' + role)
        setattr(self, role + 'Chain', _chain)

    def getTransferFactor (self, cutString):
        if hasattr (self, "Basic3hitsChain"):
            self.Basic3hitsChain.Draw('track_dxy >> h(100, -0.5, 0.5)', cutString, 'goff')
            self.Basic3hitsChain.Draw('abs(track_dxy) >> hMag(50, 0.0, 0.5)', cutString, 'goff')
            d0 = gDirectory.Get('h')
            d0Mag = gDirectory.Get('hMag')
            d0Mag.Scale(0.5)

            f = TF1 ("gaussian", gaussian, -1.0, 1.0, 3)
            f.SetParameter (0, 0.2)
            f.SetParLimits (0, 1.0e-3, 1.0e3)
            f.SetParName (0, "Gaussian sigma")
            f.SetParameter (1, 40.0)
            f.SetParLimits (1, 1.0e-3, 1.0e3)
            f.SetParName (1, "Gaussian norm")
            f.SetParameter (2, 20.0)
            f.SetParLimits (2, -1.0e3, 1.0e3)
            f.SetParName (2, "constant")
            for i in range (0, 10):
              d0Mag.Fit (f, "LQEMN", "", 0.1, 1.0)
            d0Mag.Fit (f, "LEMN", "", 0.1, 1.0)

            d0Mag.Scale (2.0)
            for i in range (0, 10):
              d0Mag.Fit (f, "LQEMN", "", 0.1, 1.0)

            passesError = ctypes.c_double (0.0)
            passes = f.IntegralOneDim (0.0, 0.02, 1.0e-12, 1.0e-2, passesError)
            passesError = getIntegralError (f, 0.0, 0.02)
            failsError = ctypes.c_double (0.0)
            fails = f.IntegralOneDim (self._minD0, self._maxD0, 1.0e-12, 1.0e-2, failsError)
            failsError = getIntegralError (f, self._minD0, self._maxD0)

            passes = Measurement (passes, 0.0)
            fails = Measurement (fails, 0.0)

            passes.isPositive ()
            fails.isPositive ()

            if fails > 0.0:
                transferFactor = passes / fails
                return (transferFactor, passes, fails, passesError, failsError)
            else:
                return (Measurement(-1, -1),) * 3 + (float("nan"),) * 2 

        else:
            print("Basic3hits is not defined. Not printing transfer factor...")
            return (Measurement(-1, -1),) * 3 + (float("nan"),) * 2 

    def printNctrl (self, cutString):
        if hasattr (self, "DisTrkInvertD0Chain"):
            if self._nHits !=  None:
                self.DisTrkInvertD0Chain.Draw('track_hitPattern_.trackerLayersWithMeasurement:track_hitPattern_.numberOfValidPixelHits >> h2d(10, -0.5, 9.5, 20, -0.5, 19.5)', cutString, 'goff')
                hits = gDirectory.Get('h2d')
                if self._nHits >= 6:
                    nError = ctypes.c_double (0.0)
                    n = hits.IntegralAndError (hits.GetXaxis ().FindBin (4.0), hits.GetXaxis ().FindBin (99.0), hits.GetYaxis ().FindBin (6.0), hits.GetYaxis ().FindBin (99.0), nError)
                    n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                    n.isPositive ()
                if self._nHits == 5:
                    nError = ctypes.c_double (0.0)
                    n = hits.IntegralAndError (hits.GetXaxis ().FindBin (4.0), hits.GetXaxis ().FindBin (99.0), hits.GetYaxis ().FindBin (5.0), hits.GetYaxis ().FindBin (5.0), nError)
                    n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                    n.isPositive ()
                if self._nHits == 4:
                    nError = ctypes.c_double (0.0)
                    n = hits.IntegralAndError (hits.GetXaxis ().FindBin (4.0), hits.GetXaxis ().FindBin (99.0), hits.GetYaxis ().FindBin (4.0), hits.GetYaxis ().FindBin (4.0), nError)
                    n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                    n.isPositive ()
            else:
                self.DisTrkInvertD0Chain.Draw('abs(track_dxy) >> hMag(50, 0.0, 0.5)', cutString, 'goff')
                d0Mag = gDirectory.Get('hMag')
                nError = ctypes.c_double (0.0)
                n = d0Mag.IntegralAndError(d0Mag.GetXaxis().FindBin(self._minD0), d0Mag.GetXaxis().FindBin(self.maxD0 - 0.001), nError)
                n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
                n.isPositive ()

            pFake = float ("nan")
            norm = 1.0

            # For ZtoMuMu control regions, need to normalize to BasicSelection
            if hasattr (self, "ZtoLL") and hasattr (self, "Basic"):
                norm = self.Basic["yield"] / self.ZtoLL["yield"]
                pFake = n / self.ZtoLL["yield"]
            elif hasattr (self, "Basic"):
                pFake = n / self.Basic["yield"]

            nRaw = n
            n *= norm
            n *= self._prescale

            return (n, nRaw, norm, pFake)
        else:
            return (Measurement(-1, -1),) + (float("nan"),) * 3

    def printNest (self, cutString):
        xi, xiPass, xiFail, xiPassError, xiFailError = self.getTransferFactor (cutString)
        nCtrl, nRaw, norm, pFake = self.printNctrl (cutString)

        pFake *= xi

        N = nRaw
        alpha = norm * self._prescale * (xiPass / xiFail)

        nEst = xi * nCtrl
        nEst.isPositive ()

        errorFromFit = nCtrl.centralValue () * math.sqrt (xiFailError * xiFailError * xiPass.centralValue () * xiPass.centralValue () + xiPassError * xiPassError * xiFail.centralValue () * xiFail.centralValue ()) / (xiFail.centralValue () * xiFail.centralValue ())

        errorOnAlphaRel = 1.0 + (alpha.maxUncertainty() / alpha.centralValue()) if alpha != 0.0 else float ("nan")
        errorFromFitRel = 1.0 + (errorFromFit / nEst.centralValue()) if nEst.centralValue () > 0.0 else float ("nan")

        if True:
            alpha.printLongFormat ()
            print("P_fake: " + str (pFake))
            print("N: " + str (N))
            print("alpha: " + str (alpha))
            print("error on alpha: " + str(errorOnAlphaRel))
            print("N_est: " + str (nEst) + " (" + str (nEst / self._luminosityInInvFb) + " fb)")
            print("error from fit: " + str(errorFromFitRel))

        return (nEst, pFake, N, alpha, errorOnAlphaRel, errorFromFitRel)

    def getNest(self, cuts):
        varX = '(track_pfElectronIsoDR03 + track_pfMuonIsoDR03 + track_pfHFIsoDR03 + track_pfLostTrackIsoDR03 + track_isoTrackIsoDR03 + track_pfChHadIsoDR03 + track_pfNeutralHadIsoDR03 + track_pfPhotonIsoDR03) / track_pt'
        varY  = 'track_matchedCaloJetEmEnergy + track_matchedCaloJetEmEnergy'
        cutString = varX + ' < ' + str(cuts[0]) + ' && ' + varY + ' < ' + str(cuts[1])
        return cuts + self.printNest(cutString)

    def optimize (self):
        varX = '(track_pfElectronIsoDR03 + track_pfMuonIsoDR03 + track_pfHFIsoDR03 + track_pfLostTrackIsoDR03 + track_isoTrackIsoDR03 + track_pfChHadIsoDR03 + track_pfNeutralHadIsoDR03 + track_pfPhotonIsoDR03) / track_pt'
        varY  = 'track_matchedCaloJetEmEnergy + track_matchedCaloJetEmEnergy'

        cutsX = [x * 0.05 for x in range(1, 10)]
        cutsY = [x * 1.0  for x in range(1, 10)]

        cutStrings = [(cutX, cutY) for cutX in cutsX for cutY in cutsY]

        arrX = array('d', cutsX)
        arrY = array('d', cutsY)

        h_nEst         = TH2D('nEst',         'nEst;superIso/pt;caloJetEnergy [GeV]',         len(cutsX) - 1, arrX, len(cutsY) - 1, arrY)
        h_pFake        = TH2D('pFake',        'pFake;superIso/pt;caloJetEnergy [GeV]',        len(cutsX) - 1, arrX, len(cutsY) - 1, arrY)
        h_N            = TH2D('N',            'N;superIso/pt;caloJetEnergy [GeV]',            len(cutsX) - 1, arrX, len(cutsY) - 1, arrY)
        h_alpha        = TH2D('alpha',        'alpha;superIso/pt;caloJetEnergy [GeV]',        len(cutsX) - 1, arrX, len(cutsY) - 1, arrY)
        h_errorOnAlpha = TH2D('errorOnAlpha', 'errorOnAlpha;superIso/pt;caloJetEnergy [GeV]', len(cutsX) - 1, arrX, len(cutsY) - 1, arrY)
        h_errorFromFit = TH2D('errorFromFit', 'errorFromFit;superIso/pt;caloJetEnergy [GeV]', len(cutsX) - 1, arrX, len(cutsY) - 1, arrY)

        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(1)
        cutResults = pool.map(self.getNest, cutStrings)

        for r in cutResults:
            (cutX, cutY, nEst, pFake, N, alpha, errorOnAlphaRel, errorFromFitRel) = r
            binNum = h_nEst.FindBin(cutX, cutY)
                
            h_nEst.Fill(cutX, cutY, nEst.centralValue())
            h_nEst.SetBinError(binNum, nEst.maxUncertainty())
                
            h_pFake.Fill(cutX, cutY, pFake.centralValue())
            h_pFake.SetBinError(binNum, pFake.maxUncertainty())

            h_N.Fill(cutX, cutY, N.centralValue())
            h_N.SetBinError(binNum, N.maxUncertainty())
                
            h_alpha.Fill(cutX, cutY, alpha.centralValue())
            h_alpha.SetBinError(binNum, alpha.maxUncertainty())
                
            h_errorOnAlpha.Fill(cutX, cutY, errorOnAlphaRel)
                
            h_errorFromFit.Fill(cutX, cutY, errorFromFitRel)

        self._fout.cd()
        h_nEst.Write()
        h_pFake.Write()
        h_N.Write()
        h_alpha.Write()
        h_errorOnAlpha.Write()
        h_errorFromFit.Write()
        self._fout.Close()

