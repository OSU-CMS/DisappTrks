#!/usr/bin/env python
import os
import sys
import math
import functools

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TH3D, TMath, TPaveText, TObject

from DisappTrks.StandardAnalysis.plotUtilities import *

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

d0CutValue = 0.02
maxSidebandValue = 0.1

class FakeTrackBkgdEstimate:
    _fout = None
    _canvas = None
    _prescale = 1.0
    _luminosityInInvFb = float ("nan")

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

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getHistIntegral (sample, condorDir, name + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, maxSidebandValue - 0.001)
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printTransferFactor (self):
        if hasattr (self, "Basic3hits"):
            passes, passesError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["condorDir"], self.Basic3hits["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, d0CutValue - 0.001)
            fails, failsError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["condorDir"], self.Basic3hits["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", d0CutValue, maxSidebandValue - 0.001)

            if fails > 0.0:
                transferFactor = passes / fails
                transferFactorError = transferFactor * math.hypot (passesError/passes, failsError/fails)
                print "Transfer factor: " + str (transferFactor) + " +/- " + str (transferFactorError)
                return (transferFactor, transferFactorError, passes, passesError, fails, failsError)
            else:
                print "N(fail d0 cut, 3 hits) = 0, not printing scale factor..."
                return (float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"))

        else:
            print "Basic3hits is not defined. Not printing transfer factor..."
            return (float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"))

    def printNctrl (self):
        if hasattr (self, "DisTrkInvertD0"):
            n = self.DisTrkInvertD0["yield"]
            nError = self.DisTrkInvertD0["yieldError"]

            n *= self._prescale
            nError *= self._prescale

            if n > 0.0:
                print "N_ctrl: " + str (n) + " +- " + str (nError) + " (" + str (n / self._luminosityInInvFb) + " +- " + str (nError / self._luminosityInInvFb) + " fb)"
                return (n, nError)
            else:
                nUpperLimit = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))
                print "N_ctrl: " + str (n) + " - 0.0 + " + str (nUpperLimit) + " (" + str (n / self._luminosityInInvFb) + " - 0 + " + str (nUpperLimit / self._luminosityInInvFb) + " fb)"
                return (n, nUpperLimit)
        else:
            print "DisTrkInvertD0 is not defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"))

    def printNest (self):
        xi, xiError, xiPass, xiPassError, xiFail, xiFailError = self.printTransferFactor ()
        nCtrl, nCtrlError = self.printNctrl ()

        nEst = xi * nCtrl
        nEstError = math.hypot (xiError * nCtrl, nCtrlError * xi)

        if nEst > 0.0:
            print "N_est: " + str (nEst) + " +- " + str (nEstError) + " (" + str (nEst / self._luminosityInInvFb) + " +- " + str (nEstError / self._luminosityInInvFb) + " fb)"
        else:
            print "N_est: " + str (nEst) + " + " + str (nEstError) + " - 0.0 (" + str (nEst / self._luminosityInInvFb) + " + " + str (nEstError / self._luminosityInInvFb) + " - 0.0 fb)"

        return (nEst, nEstError)
