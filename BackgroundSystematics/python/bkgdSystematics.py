#!/usr/bin/env python3
import os
import sys
import math
import functools

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText, TObject, TLine

from DisappTrks.StandardAnalysis.plotUtilities import *

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

fiducialElectronSigmaCut = 2.0
fiducialMuonSigmaCut = 2.0

getHistFromProjectionZ = functools.partial (getHistFromProjectionZ, fiducialElectronSigmaCut = fiducialElectronSigmaCut, fiducialMuonSigmaCut = fiducialMuonSigmaCut)
getHistIntegralFromProjectionZ = functools.partial (getHistIntegralFromProjectionZ, fiducialElectronSigmaCut = fiducialElectronSigmaCut, fiducialMuonSigmaCut = fiducialMuonSigmaCut)

d0CutValue = 0.02
minD0SidebandValue = 0.02
maxD0SidebandValue = 0.1

def getTotallyNormalYield(sample, condor_dir, channel):
    hist = "Track-eventvariable Plots/trackd0WRTPVMag"
    h = getHist (sample, condor_dir, channel, hist)
    statError_ = Double(0.0)
    yield_ = h.IntegralAndError(0, h.FindBin(d0CutValue - 0.001), statError_)
    return (yield_, statError_)

class FakeTrackSystematic:
    _fout = None
    _canvas = None
    _luminosityLabel = "13 TeV"
    _getTruthFakeRate = False
    _reweightToSample = None
    _reweightToCondorDir = None
    _reweightToChannel = None
    _reweightToHist = None
    _plotDiff = False

    _useBasicTransferFactor = False
    _basicTransferFactor = 1.0
    _basicTransferFactorError = 0.0
    _useZtoMuMuTransferFactor = False
    _zToMuMuTransferFactor = 1.0
    _zToMuMuTransferFactorError = 0.0

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addLuminosityLabel (self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        if role == "Basic" or role == "ZtoLL":
            channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
        else:
            channel["yield"], channel["yieldError"] = getHistIntegralFromProjectionZ (sample, condorDir, name + "Plotter")
            #channel["yield"], channel["yieldError"] = getTotallyNormalYield(sample, condorDir, name + "Plotter")

        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print(("yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])))

    def reweightTo (self, sampleName, condorDir, channelName, histName):
        self._reweightToSample = sampleName
        self._reweightToCondorDir = condorDir
        self._reweightToChannel = channelName
        self._reweightToHist = histName

    def addD0TransferFactor (self):
        if hasattr (self, "DisTrkNHits3NoD0Cut"):
            basicPass, basicPassError = getHistIntegral (self.DisTrkNHits3NoD0Cut["sample"],
                                                         self.DisTrkNHits3NoD0Cut["condorDir"],
                                                         self.DisTrkNHits3NoD0Cut["name"] + "Plotter",
                                                         "Track-eventvariable Plots/trackd0WRTPVMag",
                                                         0.0, d0CutValue - 0.001)
            basicFail, basicFailError = getHistIntegral (self.DisTrkNHits3NoD0Cut["sample"],
                                                         self.DisTrkNHits3NoD0Cut["condorDir"],
                                                         self.DisTrkNHits3NoD0Cut["name"] + "Plotter",
                                                         "Track-eventvariable Plots/trackd0WRTPVMag",
                                                         minD0SidebandValue, maxD0SidebandValue - 0.001)
            if basicFail > 0.0:
                self._useBasicTransferFactor = True
                self._basicTransferFactor = basicPass / basicFail
                self._basicTransferFactorError = (basicPass / basicFail) * math.hypot (basicPassError/basicPass, basicFailError/basicFail)
                print(("Basic transfer factor (3 hits) = " + str(self._basicTransferFactor) + " +/- " + str(self._basicTransferFactorError)))
            else:
                print("Zero sideband D0 events for Basic (3 hits), not using transfer factor!")
        else:
            print("DisTrkNHits3NoD0Cut not defined, not using transfer factor!")

        if hasattr (self, "ZtoMuMuDisTrkNHits3NoD0Cut"):
            zToMuMuPass, zToMuMuPassError = getHistIntegral (self.ZtoMuMuDisTrkNHits3NoD0Cut["sample"],
                                                             self.ZtoMuMuDisTrkNHits3NoD0Cut["condorDir"],
                                                             self.ZtoMuMuDisTrkNHits3NoD0Cut["name"] + "Plotter",
                                                             "Track-eventvariable Plots/trackd0WRTPVMag",
                                                             0.0, d0CutValue - 0.001)
            zToMuMuFail, zToMuMuFailError = getHistIntegral (self.ZtoMuMuDisTrkNHits3NoD0Cut["sample"],
                                                             self.ZtoMuMuDisTrkNHits3NoD0Cut["condorDir"],
                                                             self.ZtoMuMuDisTrkNHits3NoD0Cut["name"] + "Plotter",
                                                             "Track-eventvariable Plots/trackd0WRTPVMag",
                                                             minD0SidebandValue, maxD0SidebandValue - 0.001)
            if zToMuMuFail > 0.0:
                self._useZtoMuMuTransferFactor = True
                self._zToMuMuTransferFactor = zToMuMuPass / zToMuMuFail
                self._zToMuMuTransferFactorError = (zToMuMuPass / zToMuMuFail) * math.hypot (zToMuMuPassError/zToMuMuPass, zToMuMuFailError/zToMuMuFail)
                print(("ZtoMuMu transfer factor (3 hits) = " + str(self._zToMuMuTransferFactor) + " +/- " + str(self._zToMuMuTransferFactorError)))
            else:
                print("Zero sideband D0 events for ZtoMuMu (3 hits), not using transfer factor!")
        else:
            print("ZtoMuMuDisTrkNHits3NoD0Cut not defined, not using transfer factor!")

    def getTruthFakeRate (self, getTruthFakeRate):
        self._getTruthFakeRate = getTruthFakeRate

    def plotDiff (self, plotDiff = True):
        self._plotDiff = plotDiff

    def printFakeRateRatio (self, nHits):
        if hasattr (self, "DisTrkNHits" + str (nHits)) and hasattr (self, "ZtoMuMuDisTrkNHits" + str (nHits)):
            disTrkNHits = getattr (self, "DisTrkNHits" + str (nHits))
            zToMuMuDisTrkNHits = getattr (self, "ZtoMuMuDisTrkNHits" + str (nHits))

            total = (disTrkNHits["total"], zToMuMuDisTrkNHits["total"])
            totalError = (disTrkNHits["totalError"], zToMuMuDisTrkNHits["totalError"])
            if hasattr (self, "Basic") and hasattr (self, "ZtoLL"):
                total = (self.Basic["yield"], self.ZtoLL["yield"])
                totalError = (self.Basic["yieldError"], self.ZtoLL["yieldError"])

            disTrkCorrection = zToMuMuDisTrkCorrection = 1.0
            disTrkCorrectionError = zToMuMuDisTrkCorrectionError = 0.0
            if self._getTruthFakeRate:
                (disTrkCorrection, disTrkCorrectionError) = self.getTruthFakeRateCorrection (disTrkNHits)
                (zToMuMuDisTrkCorrection, zToMuMuDisTrkCorrectionError) = self.getTruthFakeRateCorrection (zToMuMuDisTrkNHits)

            if self._useBasicTransferFactor:
                disTrkCorrection = disTrkCorrection * self._basicTransferFactor
                disTrkCorrectionError = math.hypot (disTrkCorrectionError, self._basicTransferFactorError)
                print(('Using', disTrkCorrection, '+/-', disTrkCorrectionError, 'for Basic as a transfer factor'))
            if self._useZtoMuMuTransferFactor:
                zToMuMuDisTrkCorrection = zToMuMuDisTrkCorrection * self._zToMuMuTransferFactor
                zToMuMuDisTrkCorrectionError = math.hypot (zToMuMuDisTrkCorrectionError, self._zToMuMuTransferFactorError)
                print(("Using", zToMuMuDisTrkCorrection, "+/-", zToMuMuDisTrkCorrectionError, "for ZtoMuMu as a transfer factor"))

            passes = (disTrkCorrection * disTrkNHits["yield"], zToMuMuDisTrkCorrection * zToMuMuDisTrkNHits["yield"])
            passesError = (math.hypot (disTrkCorrection * disTrkNHits["yieldError"], disTrkCorrectionError * disTrkNHits["yield"]), math.hypot (zToMuMuDisTrkCorrection * zToMuMuDisTrkNHits["yieldError"], zToMuMuDisTrkCorrectionError * zToMuMuDisTrkNHits["yield"]))

            fakeRate = (passes[0] / total[0], passes[1] / total[1])
            fakeRateError = (math.hypot ((passes[0] * totalError[0]) / (total[0] * total[0]), (passesError[0] * total[0]) / (total[0] * total[0])), math.hypot ((passes[1] * totalError[1]) / (total[1] * total[1]), (passesError[1] * total[1]) / (total[1] * total[1])))

            if self._reweightToSample and self._reweightToCondorDir and self._reweightToChannel and self._reweightToHist:
                print("REWEIGHTING REWEIGHTING REWEIGHTING REWEIGHTING REWEIGHTING")
                fakeRate, fakeRateError = self.getReweightedYields (disTrkNHits,
                                                                    zToMuMuDisTrkNHits,
                                                                    disTrkCorrection,
                                                                    disTrkCorrectionError,
                                                                    zToMuMuDisTrkCorrection,
                                                                    zToMuMuDisTrkCorrectionError,
                                                                    str (nHits))

            ratio = fakeRate[1] / fakeRate[0] if fakeRate[0] > 0.0 else 0.0
            ratioError = math.hypot ((fakeRate[0] * fakeRateError[1]) / (fakeRate[0] * fakeRate[0]), (fakeRateError[0] * fakeRate[1]) / (fakeRate[0] * fakeRate[0])) if fakeRate[0] > 0.0 else 0.0

            if fakeRateError[0] > 0.0 and fakeRateError[1] > 0.0:
                print("nHits: " + str (nHits) + ", basic: " + str (fakeRate[0]) + " +- " + str (fakeRateError[0]) + ", zToMuMu: " + str (fakeRate[1]) + " +- " + str (fakeRateError[1]) + ", difference: " + str ((fakeRate[1] - fakeRate[0]) / math.hypot (fakeRateError[1], fakeRateError[0])) + " sigma, ratio: " + str (ratio) + " +- " + str (ratioError))
            else:
                print("nHits: " + str (nHits) + ", basic: " + str (fakeRate[0]) + " +- " + str (fakeRateError[0]) + ", zToMuMu: " + str (fakeRate[1]) + " +- " + str (fakeRateError[1]) + ", difference: nan" + ", ratio: " + str (ratio) + " +- " + str (ratioError))
            if self._plotDiff:
                ratio = fakeRate[1] - fakeRate[0]
                ratioError = math.hypot (fakeRateError[1], fakeRateError[0])
            return (fakeRate, fakeRateError, ratio, ratioError)
        else:
            print("DisTrkNHits" + str (nHits) + ", and ZtoMuMuDisTrkNHits" + str (nHits) + " not all defined. Not printing fake rate ratio...")
            return (float ("nan"), float ("nan"), float ("nan"), float ("nan"))

    def getReweightedYields (self, disTrkNHits, zToMuMuDisTrkNHits, disTrkCorrection, disTrkCorrectionError, zToMuMuDisTrkCorrection, zToMuMuDisTrkCorrectionError, outputLabel = ""):
        if hasattr (self, "Basic") and hasattr (self, "ZtoLL"):
            sample = self.Basic["sample"]
            condorDir = self.Basic["condorDir"]
            name = self.Basic["name"]
            disTrkTotalHist = getHist (sample, condorDir, name + "Plotter", self._reweightToHist)

            sample = self.ZtoLL["sample"]
            condorDir = self.ZtoLL["condorDir"]
            name = self.ZtoLL["name"]
            zToMuMuDisTrkTotalHist = getHist (sample, condorDir, name + "Plotter", self._reweightToHist)

            sample = disTrkNHits["sample"]
            condorDir = disTrkNHits["condorDir"]
            name = disTrkNHits["name"]
            disTrkPassesHist = getHist (sample, condorDir, name + "Plotter", self._reweightToHist)

            sample = zToMuMuDisTrkNHits["sample"]
            condorDir = zToMuMuDisTrkNHits["condorDir"]
            name = zToMuMuDisTrkNHits["name"]
            zToMuMuDisTrkPassesHist = getHist (sample, condorDir, name + "Plotter", self._reweightToHist)

            weightHist = getHist (self._reweightToSample, self._reweightToCondorDir, self._reweightToChannel + "Plotter", self._reweightToHist)
            #weightHist = getHist (self._reweightToSample, self._reweightToCondorDir, disTrkNHits["name"] + "Plotter", self._reweightToHist)        # uncomment to reweight to DisTrkNHits* channels
            #weightHist = getHist (self._reweightToSample, self._reweightToCondorDir, zToMuMuDisTrkNHits["name"] + "Plotter", self._reweightToHist) # uncomment to reweight to ZtoMuMuDisTrkNHits* channels
            weightHist.Scale (1.0 / weightHist.Integral ())

            rebinFactor = 6
            disTrkTotalHist.Rebin (rebinFactor)
            zToMuMuDisTrkTotalHist.Rebin (rebinFactor)
            disTrkPassesHist.Rebin (rebinFactor)
            zToMuMuDisTrkPassesHist.Rebin (rebinFactor)
            weightHist.Rebin (rebinFactor)

            self._canvas.cd ()
            weightHist.Draw ()
            self._fout.cd ()
            self._canvas.Write ("weightHist_" + outputLabel)

            disTrkPassesHist.Divide (disTrkTotalHist.Clone ())
            zToMuMuDisTrkPassesHist.Divide (zToMuMuDisTrkTotalHist.Clone ())

            self._canvas.cd ()
            disTrkPassesHist.Draw ()
            self._fout.cd ()
            self._canvas.Write ("basicFakeRateBeforeReweighting_" + outputLabel)

            self._canvas.cd ()
            zToMuMuDisTrkPassesHist.Draw ()
            self._fout.cd ()
            self._canvas.Write ("zToMuMuFakeRateBeforeReweighting_" + outputLabel)

            disTrkPassesHist.Multiply (weightHist.Clone ())
            zToMuMuDisTrkPassesHist.Multiply (weightHist.Clone ())

            self._canvas.cd ()
            disTrkPassesHist.Draw ()
            self._fout.cd ()
            self._canvas.Write ("basicFakeRateAfterReweighting_" + outputLabel)

            self._canvas.cd ()
            zToMuMuDisTrkPassesHist.Draw ()
            self._fout.cd ()
            self._canvas.Write ("zToMuMuFakeRateAfterReweighting_" + outputLabel)

            N = (disTrkPassesHist.GetNbinsX (), zToMuMuDisTrkPassesHist.GetNbinsX ())
            disTrkPassesError = Double (0.0)
            zToMuMuDisTrkPassesError = Double (0.0)
            disTrkPasses = disTrkPassesHist.IntegralAndError (0, N[0] + 1, disTrkPassesError)
            zToMuMuDisTrkPasses = zToMuMuDisTrkPassesHist.IntegralAndError (0, N[1] + 1, zToMuMuDisTrkPassesError)

            fakeRate = (Double(disTrkCorrection) * disTrkPasses,
                        zToMuMuDisTrkCorrection * zToMuMuDisTrkPasses)

            fakeRateError = (0.0, 0.0)
            if disTrkPasses > 0.0:
                fakeRateError = (fakeRate[0] * math.hypot (disTrkCorrectionError/disTrkCorrection, disTrkPassesError/disTrkPasses), fakeRateError[1])
            if zToMuMuDisTrkPasses > 0.0:
                fakeRateError = (fakeRateError[0], fakeRate[1] * math.hypot (zToMuMuDisTrkCorrectionError/zToMuMuDisTrkCorrection, zToMuMuDisTrkPassesError/zToMuMuDisTrkPasses))

            return (fakeRate, fakeRateError)
        else:
            print("Basic and ZtoLL are not defined. Not reweighting fake track rates...")
            return ((float ("nan"), float ("nan")), (float ("nan"), float ("nan")))

    def getTruthFakeRateCorrection (self, channel):
        sample = channel["sample"]
        condorDir = channel["condorDir"]
        name = channel["name"]
        hist = "Track Plots/bestMatchPdgId" # N.B. "bestMatch" changed to "promptOrTauDecay" but hist name remains
        genMatch = getHist (sample, condorDir, name + "Plotter", hist)

        totalError = Double (0.0)
        total = genMatch.IntegralAndError (0, genMatch.GetNbinsX () + 1, totalError)
        passes = genMatch.GetBinContent (1)
        passesError = genMatch.GetBinError (1)

        (correction, correctionErrorLow, correctionErrorHigh) = getEfficiency (passes, passesError, total, totalError)
        return (correction, max (correctionErrorLow, correctionErrorHigh))

    def printSystematic (self):
        fakeRate3, fakeRate3Error, ratio3, ratio3Error = self.printFakeRateRatio (3)
        fakeRate4, fakeRate4Error, ratio4, ratio4Error = self.printFakeRateRatio (4)
        fakeRate5, fakeRate5Error, ratio5, ratio5Error = self.printFakeRateRatio (5)
        fakeRate6, fakeRate6Error, ratio6, ratio6Error = self.printFakeRateRatio (6)

        print("systematic uncertainty: " + str ((abs (ratio5 - 1.0) + ratio5Error) * 100.0) + "%")

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
        setAxisStyle (ratio, yTitle = ("P_{fake}^{Z#rightarrow#mu#mu} / P_{fake}^{basic}" if not self._plotDiff else "P_{fake}^{Z#rightarrow#mu#mu} - P_{fake}^{basic}"))
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
    _plotLabel = float ("nan")
    _rebinFactor = 1

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addMetCut (self, metCut):
        self._metCut = metCut

    def addLuminosityLabel (self, luminosityLabel):
        self._luminosityLabel = luminosityLabel

    def addPlotLabel (self, plotLabel):
        self._plotLabel = plotLabel

    def addRebinFactor (self, rebinFactor):
        self._rebinFactor = rebinFactor

    def __init__ (self, flavor):
        self._flavor = flavor.lower ()
        self._Flavor = self._flavor[0].upper () + self._flavor[1:]

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print("yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"]))

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

            eff = passes / total if total > 0.0 else 0.0
            effError = math.hypot (total * passesError, totalError * passes) / (total * total) if total > 0.0 else 0.0
            print("P (pass met triggers) with \"" + metMinusOneHist + "\": " + str (eff) + " +- " + str (effError))
            return (eff, effError)
        else:
            print("TagPt35 and TagPt35MetTrig not both defined. Not printing P (pass met triggers)...")
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

            eff = passes / total if total > 0.0 else 0.0
            effError = math.hypot (total * passesError, totalError * passes) / (total * total) if total > 0.0 else 0.0
            print("P (pass met cut) with \"" + metMinusOneHist + "\": " + str (eff) + " +- " + str (effError))
            return (eff, effError)
        else:
            print("TagPt35 not defined. Not printing P (pass met cut)...")
            return (float ("nan"), float ("nan"))

    def printSystematic (self):
        self.plotMet ()

        pPassMetCut0       =  self.printPpassMetCut       ("MetNoMuMinusOnePt")
        pPassMetCut1       =  self.printPpassMetCut       ("MetNoMuMinusOneUpPt")
        pPassMetTriggers0  =  self.printPpassMetTriggers  ("MetNoMuMinusOnePt")
        pPassMetTriggers1  =  self.printPpassMetTriggers  ("MetNoMuMinusOneUpPt")

        ratio = (pPassMetCut1[0] * pPassMetTriggers1[0]) / (pPassMetCut0[0] * pPassMetTriggers0[0]) if (pPassMetCut0[0] * pPassMetTriggers0[0] > 0.0) else 0.0
        ratioError = 0.0
        ratioError = math.hypot (ratioError, pPassMetCut0[0] * pPassMetTriggers0[0] * pPassMetCut1[0] * pPassMetTriggers1[1])
        ratioError = math.hypot (ratioError, pPassMetCut0[0] * pPassMetTriggers0[0] * pPassMetCut1[1] * pPassMetTriggers1[0])
        ratioError = math.hypot (ratioError, pPassMetCut0[0] * pPassMetTriggers0[1] * pPassMetCut1[0] * pPassMetTriggers1[0])
        ratioError = math.hypot (ratioError, pPassMetCut0[1] * pPassMetTriggers0[0] * pPassMetCut1[0] * pPassMetTriggers1[0])
        if (pPassMetCut0[0] * pPassMetTriggers0[0] > 0.0):
            ratioError /= ((pPassMetCut0[0] * pPassMetTriggers0[0]) * (pPassMetCut0[0] * pPassMetTriggers0[0]))

        print("ratio: " + str (ratio) + " +- " + str (ratioError))

        print("systematic uncertainty: " + str (abs (ratio - 1.0) * 100.0) + "%")

    def plotMet (self):
        if hasattr (self, "TagPt35") or hasattr (self, "TagPt35ForNctrl"):
            if self._fout and self._canvas:
                sample = self.TagPt35ForNctrl["sample"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["sample"]
                condorDir = self.TagPt35ForNctrl["condorDir"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["condorDir"]
                name = self.TagPt35ForNctrl["name"] if hasattr (self, "TagPt35ForNctrl") else self.TagPt35["name"]

                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOnePt"
                metMinusOne = getHist (sample, condorDir, name + "Plotter", hist)
                hist = self._Flavor + " Plots/" + self._flavor + "MetNoMuMinusOneUpPt"
                metMinusOneUp = getHist (sample, condorDir, name + "Plotter", hist)

                metMinusOne.Rebin (self._rebinFactor)
                metMinusOneUp.Rebin (self._rebinFactor)

                pt = TPaveText(0.398496,0.839147,0.798246,0.886951,"brNDC")
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

                lumiLabel = TPaveText(0.66416,0.937339,0.962406,0.992894,"brNDC")
                lumiLabel.SetBorderSize(0)
                lumiLabel.SetFillStyle(0)
                lumiLabel.SetTextFont(42)
                lumiLabel.SetTextSize(0.0387597)
                lumiLabel.AddText(str (self._luminosityLabel))

                leg = TLegend(0.414787,0.726098,0.606516,0.829457)
                leg.SetBorderSize(0)
                leg.SetTextSize(0.0388601)
                leg.SetTextFont(42)
                leg.SetLineColor(1)
                leg.SetLineStyle(1)
                leg.SetLineWidth(1)
                leg.SetFillColor(0)
                leg.SetFillStyle(0)
                leg.AddEntry (metMinusOne, "nominal (#mu = " + str (round (metMinusOne.GetMean (), 1)) + " #pm " + str (round (metMinusOne.GetMeanError (), 1)) + ")", "p")
                leg.AddEntry (metMinusOneUp, "scaled down (#mu = " + str (round (metMinusOneUp.GetMean (), 1)) + " #pm " + str (round (metMinusOneUp.GetMeanError (), 1)) + ")", "p")

                setStyle (metMinusOne, 600)
                setAxisStyle (metMinusOne, "E_{T}^{miss, no #mu} " + ("excluding selected " + self._flavor if self._flavor != "muon" else "") + " [GeV]")
                setStyle (metMinusOneUp, 632)
                setAxisStyle (metMinusOneUp, "E_{T}^{miss, no #mu} " + ("excluding selected " + self._flavor if self._flavor != "muon" else "") + " [GeV]")
                self._canvas.cd ()
                metMinusOneUp.Draw ()
                metMinusOne.Draw ("same")
                pt.Draw ("same")
                cmsLabel.Draw ("same")
                lumiLabel.Draw ("same")
                leg.Draw ("same")
                self._fout.cd ()
                self._canvas.Write ("metMinusOneComparison")
            else:
                print("A TFile and TCanvas must be added. Not making plots...")
        else:
            print("Neither TagPt35 nor TagPt35ForNctrl defined. Not plotting MET...")
