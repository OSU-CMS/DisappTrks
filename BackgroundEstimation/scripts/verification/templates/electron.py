#!/usr/bin/env python3

import math, os, sys
from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate, FakeTrackBkgdEstimate, prettyPrintTotals
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch() # I am Groot.

canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]

year = __YEAR__
runPeriods = [__ERA__]
path = __PATH__

met_key = f"MET_{year}{__ERA__}"
egamma_key = f"EGamma_{year}{__ERA__}"

for runPeriod in runPeriods:

    print("********************************************************************************")
    print(f"performing electron background estimate in search region({year}{runPeriod} -- combined layers bins)")
    print("--------------------------------------------------------------------------------")

    fout = TFile.Open(f"electronBkgdEstimate_{year}{runPeriod}_combinedBins.root", "recreate")

    electronBkgdEstimate = LeptonBkgdEstimate("electron")
    electronBkgdEstimate.addMetCut(120.0)
    electronBkgdEstimate.addPhiCut(0.5)
    electronBkgdEstimate.addTFile(fout)
    electronBkgdEstimate.addTCanvas(canvas)

    electronBkgdEstimate.addPrescaleFactor(round(lumi[met_key] / lumi[egamma_key], 5))
    electronBkgdEstimate.addLuminosityInInvPb(lumi[met_key])
    electronBkgdEstimate.addLuminosityLabel(str(round(lumi[egamma_key] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
    electronBkgdEstimate.addPlotLabel(egamma_key)
    electronBkgdEstimate.useFilesForTriggerEfficiency()

    electronBkgdEstimate.addChannel("TagProbe", "ZtoEleProbeTrk"                   + nLayersWords[0], f"EGamma_{year}{runPeriod}", "data")
    electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[0], f"EGamma_{year}{runPeriod}", "data")
    electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[0], f"EGamma_{year}{runPeriod}", "data")
    electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[0], f"EGamma_{year}{runPeriod}", "data")
    electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[0], f"EGamma_{year}{runPeriod}", "data")

    for iBin in range(1, len(nLayersWords)):
        electronBkgdEstimate.appendChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[iBin], f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.appendChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[iBin], f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.appendChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[iBin], f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.appendChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[iBin], f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.appendChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[iBin], f"EGamma_{year}{runPeriod}", "data")

    electronBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
    electronBkgdEstimate.addRebinFactor(4)

    print("********************************************************************************")

    electronBkgdEstimate.printNest()
    electronBkgdEstimate.printPpassVetoTagProbe()

    print("********************************************************************************")

    fout.Close()

    print("\n\n")

    for nLayersWord in nLayersWords:

        print("********************************************************************************")
        print(f"performing electron background estimate in search region({year}{runPeriod}--{nLayersWord})")
        print("--------------------------------------------------------------------------------")

        fout = TFile.Open(f"electronBkgdEstimate_{year}{runPeriod}_{nLayersWord}.root", "recreate")

        electronBkgdEstimate = LeptonBkgdEstimate("electron")
        electronBkgdEstimate.addMetCut(120.0)
        electronBkgdEstimate.addPhiCut(0.5)
        electronBkgdEstimate.addTFile(fout)
        electronBkgdEstimate.addTCanvas(canvas)
        electronBkgdEstimate.addPrescaleFactor(round(lumi[met_key] / lumi[egamma_key], 5))
        electronBkgdEstimate.addLuminosityInInvPb(lumi[met_key])
        electronBkgdEstimate.addLuminosityLabel(str(round(lumi[egamma_key] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
        electronBkgdEstimate.addPlotLabel(egamma_key)
        electronBkgdEstimate.useFilesForTriggerEfficiency()

        electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWord, f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWord, f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWord, f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWord, f"EGamma_{year}{runPeriod}", "data")
        electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWord, f"EGamma_{year}{runPeriod}", "data")

        electronBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
        electronBkgdEstimate.addRebinFactor(4)

        print("********************************************************************************")

        electronBkgdEstimate.printNest()
        electronBkgdEstimate.printPpassVetoTagProbe()

        print("********************************************************************************")

        fout.Close()

        print("\n\n")
