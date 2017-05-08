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
maxSidebandValue = 0.5

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
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printTransferFactor (self):
        if hasattr (self, "Basic3hits"):
            passes, passesError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["name"], "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, d0CutValue)
            fails, failsError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["name"], "Track-eventvariable Plots/trackd0WRTPVMag", d0CutValue, maxSidebandValue)

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

            print "N_ctrl: " + str (n) + " +- " + str (nError) + " (" + str (n / self._luminosityInInvFb) + " +- " + str (nError / self._luminosityInInvFb) + " fb)"
            return (n, nError)
        else:
            print "DisTrkInvertD0 is not defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"))

    def printNest (self):
        xi, xiError, xiPass, xiPassError, xiFail, xiFailError = self.printTransferFactor ()
        nCtrl, nCtrlError = self.printNctrl ()

        nEst = xi * nCtrl
        nEstError = nEst * math.hypot (xiError/xi, nCtrl/nCtrlError)

        if nEst > 0.0:
            print "N_est: " + str (nEst) + " +- " + str (nEstError) + " (" + str (nEst / self._luminosityInInvFb) + " +- " + str (nEstError / self._luminosityInInvFb) + " fb)"
        else:
            print "N_est: " + str (nEst) + " - 0.0 + " + str (nEstError) + " (" + str (nEst / self._luminosityInInvFb) + " +- " + str (nEstError / self._luminosityInInvFb) + " fb)"

        return (nEst, nEstError)
