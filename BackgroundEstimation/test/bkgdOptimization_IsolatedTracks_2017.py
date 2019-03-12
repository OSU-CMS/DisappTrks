#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import FakeTrackBkgdOptimizer
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
combineLayers = True
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]
    combineLayers = False

# '' will gives you Dataset_2017.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F']
runPeriods = ['']

nEstFake = {}

for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "Optimizing fake track background estimate in search region(2017", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("optimizeFake_zToMuMu_2017" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdOptimizer ()
            fakeTrackBkgdEstimate.addTFile(fout)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2017" + runPeriod])
            fakeTrackBkgdEstimate.addMinD0 (0.05)
            fakeTrackBkgdEstimate.addChannel ("Basic3hits",      "ZtoMuMuDisTrkNoD0Cut3LayersVeryClean", "SingleMu_2017"  +  runPeriod,  dirs['Brian']+"2017_isolatedTracks/fakeTrackBackground_noTrkIso_noECalo_normalLepVetos_v2", False)
            fakeTrackBkgdEstimate.addChannel ("DisTrkInvertD0",  "ZtoMuMuDisTrkNoD0Cut" + nLayersWord,   "SingleMu_2017"  +  runPeriod,  dirs['Brian']+"2017_isolatedTracks/fakeTrackBackground_noTrkIso_noECalo_normalLepVetos_v2", False)
            fakeTrackBkgdEstimate.addChannel ("Basic",           "BasicSelection",                       "MET_2017"       +  runPeriod,  dirs['Andrew']+"2017/basicSelection", False)
            fakeTrackBkgdEstimate.addChannel ("ZtoLL",           "ZtoMuMu",                              "SingleMu_2017"  +  runPeriod,  dirs['Andrew']+"2017/zToMuMu", False)

            fakeTrackBkgdEstimate.addTrees("Basic3hits", "ZtoMuMuDisTrkNoD0Cut3LayersVeryCleanTreeMaker/Tree", "condor/2017_isolatedTracks/fakeTrackBackground_noTrkIso_noECalo_normalLepVetos_v2")
            fakeTrackBkgdEstimate.addTrees("DisTrkInvertD0", "ZtoMuMuDisTrkNoD0Cut" + nLayersWord + "TreeMaker/Tree", "condor/2017_isolatedTracks/fakeTrackBackground_noTrkIso_noECalo_normalLepVetos_v2")

            print "********************************************************************************"

            fakeTrackBkgdEstimate.optimize()

            print "********************************************************************************"
