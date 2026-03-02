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
muon_key = f"Muon_{year}{__ERA__}"

for runPeriod in runPeriods:

    print("********************************************************************************")
    print(f"performing muon background estimate in search region({year}{runPeriod} -- combined layer bins)")
    print("--------------------------------------------------------------------------------")

    fout = TFile.Open(f"muonBkgdEstimate_{year}{runPeriod}_combinedBins.root", "recreate")

    muonBkgdEstimate = LeptonBkgdEstimate("muon")
    muonBkgdEstimate.addMetCut(120.0)
    muonBkgdEstimate.addPhiCut(0.5)
    muonBkgdEstimate.addTFile(fout)
    muonBkgdEstimate.addTCanvas(canvas)
    muonBkgdEstimate.addPrescaleFactor(round(lumi[met_key] / lumi[muon_key], 5))
    muonBkgdEstimate.addLuminosityInInvPb(lumi[met_key])
    muonBkgdEstimate.addLuminosityLabel(str(round(lumi[muon_key] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
    muonBkgdEstimate.addPlotLabel(muon_key)
    muonBkgdEstimate.useFilesForTriggerEfficiency()

    muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[0], f"Muon_{year}{runPeriod}", "data")
    muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[0], f"Muon_{year}{runPeriod}", "data")
    muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[0], f"Muon_{year}{runPeriod}", "data")
    muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[0], f"Muon_{year}{runPeriod}", "data")
    muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[0], f"Muon_{year}{runPeriod}", "data")


    for iBin in range(1, len(nLayersWords)):
        muonBkgdEstimate.appendChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[iBin], f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.appendChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[iBin], f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.appendChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[iBin], f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.appendChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[iBin], f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.appendChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[iBin], f"Muon_{year}{runPeriod}", "data")

    muonBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
    muonBkgdEstimate.addRebinFactor(4)

    print("********************************************************************************")

    muonBkgdEstimate.printNest()
    muonBkgdEstimate.printPpassVetoTagProbe()

    combinedPpassMetCut = muonBkgdEstimate.getPpassMetCut()
    combinedPpassMetTriggers, combinedTriggerEfficiency = muonBkgdEstimate.getPpassMetTriggers()

    print("combined met probability", combinedPpassMetCut)
    print("combined trigger probability", combinedPpassMetTriggers)


    print("********************************************************************************")

    fout.Close()

    print("\n\n")

    for nLayersWord in nLayersWords:

        print("********************************************************************************")
        print(f"performing muon background estimate in search region({year}{runPeriod} -- {nLayersWord}", ")")
        print("--------------------------------------------------------------------------------")

        fout = TFile.Open(f"muonBkgdEstimate_{year}{runPeriod}_{nLayersWord}.root", "recreate")

        muonBkgdEstimate = LeptonBkgdEstimate("muon")
        muonBkgdEstimate.addMetCut(120.0)
        muonBkgdEstimate.addPhiCut(0.5)
        muonBkgdEstimate.addTFile(fout)
        muonBkgdEstimate.addTCanvas(canvas)
        muonBkgdEstimate.addPrescaleFactor(round(lumi[met_key] / lumi[muon_key], 5))
        muonBkgdEstimate.addLuminosityInInvPb(lumi[met_key])
        muonBkgdEstimate.addLuminosityLabel(str(round(lumi[muon_key] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
        muonBkgdEstimate.addPlotLabel(muon_key)
        muonBkgdEstimate.useFilesForTriggerEfficiency()

        muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWord, f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWord, f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWord, f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWord, f"Muon_{year}{runPeriod}", "data")
        muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWord, f"Muon_{year}{runPeriod}", "data")

        muonBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
        muonBkgdEstimate.addRebinFactor(4)

        print("********************************************************************************")

        if nLayersWord == "NLayers4" or nLayersWord == "NLayers5":
            print("using the combined 4/5/6+ layers sample for Poffline and Ptrigger:")
            muonBkgdEstimate.printNestCombinedMet(combinedPpassMetCut, combinedPpassMetTriggers)
        else:
            muonBkgdEstimate.printNest()
        muonBkgdEstimate.printPpassVetoTagProbe()

        print("********************************************************************************")

        fout.Close()

        print("\n\n")

