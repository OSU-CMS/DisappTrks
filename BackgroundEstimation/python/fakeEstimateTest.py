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

class FakeTrackBkgdEstimate:
    _fout = None
    _canvas = None
    _prescale = 1.0
    _luminosityInInvFb = float ("nan")
    _minHits = 7
    _minD0 = 0.02
    _maxD0 = 0.1

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

    def addMinHits (self, minHits):
        self._minHits = minHits

    def addMinD0 (self, minD0):
        self._minD0 = minD0

    def addMaxD0 (self, maxD0):
        self._maxD0 = maxD0

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        n, nError = getHistIntegral (sample, condorDir, name + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, self._maxD0 - 0.001)
        channel["yield"] = Measurement (n, nError)
        channel["yield"].isPositive ()
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"])

    def printTransferFactor (self):
        if hasattr (self, "Basic3hits"):
            passes, passesError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["condorDir"], self.Basic3hits["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, 0.02 - 0.001)
            fails, failsError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["condorDir"], self.Basic3hits["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)

            passes = Measurement (passes, passesError)
            fails = Measurement (fails, failsError)

            passes.isPositive ()
            fails.isPositive ()

            if fails > 0.0:
                transferFactor = passes / fails
                print "Transfer factor: " + str (transferFactor)
                return (transferFactor, passes, fails)
            else:
                print "N(fail d0 cut, 3 hits) = 0, not printing scale factor..."
                return (float ("nan"), float ("nan"), float ("nan"))

        else:
            print "Basic3hits is not defined. Not printing transfer factor..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printNctrl (self):
        if hasattr (self, "DisTrkInvertD0"):
            n, nError = getHistIntegral (self.DisTrkInvertD0["sample"], self.DisTrkInvertD0["condorDir"], self.DisTrkInvertD0["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
            n = Measurement (n, (nError if n != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))))
            n.isPositive ()

            if self._minHits < 7:
                n6, n6Error = getHistIntegral (self.DisTrkInvertD0NHits6["sample"], self.DisTrkInvertD0NHits6["condorDir"], self.DisTrkInvertD0NHits6["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n6 = Measurement (n6, (n6Error if n6 != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n6 + 1))))
                n6.isPositive ()
                n += n6
            if self._minHits < 6:
                n5, n5Error = getHistIntegral (self.DisTrkInvertD0NHits5["sample"], self.DisTrkInvertD0NHits5["condorDir"], self.DisTrkInvertD0NHits5["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n5 = Measurement (n5, (n5Error if n5 != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n5 + 1))))
                n5.isPositive ()
                n += n5
            if self._minHits < 5:
                n4, n4Error = getHistIntegral (self.DisTrkInvertD0NHits4["sample"], self.DisTrkInvertD0NHits4["condorDir"], self.DisTrkInvertD0NHits4["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n4 = Measurement (n4, (n4Error if n4 != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n4 + 1))))
                n4.isPositive ()
                n += n4
            if self._minHits < 4:
                n3, n3Error = getHistIntegral (self.DisTrkInvertD0NHits3["sample"], self.DisTrkInvertD0NHits3["condorDir"], self.DisTrkInvertD0NHits3["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n3 = Measurement (n3, (n3Error if n3 != 0.0 else 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n3 + 1))))
                n3.isPositive ()
                n += n3

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

            print "N_ctrl: " + str (n) + " (" + str (n / self._luminosityInInvFb) + " fb)"
            print "P_fake^raw: " + str (pFake)
            return (n, nRaw, norm, pFake)
        else:
            print "DisTrkInvertD0 is not defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"))

    def printNest (self):
        xi, xiPass, xiFail = self.printTransferFactor ()
        nCtrl, nRaw, norm, pFake = self.printNctrl ()

        pFake *= xi

        N = nRaw
        alpha = norm * (xiPass / xiFail)

        nEst = xi * nCtrl

        alpha.printLongFormat ()
        print "P_fake: " + str (pFake)
        print "N: " + str (N)
        print "alpha: " + str (alpha)
        print "error on alpha: " + str ((1.0 + (alpha.maxUncertainty () / alpha.centralValue ())) if alpha != 0.0 else float ("nan"))
        print "N_est: " + str (nEst) + " (" + str (nEst / self._luminosityInInvFb) + " fb)"

        return (nEst.centralValue (), nEst.uncertainty ())
