#!/usr/bin/env python

import math
from DisappTrks.BackgroundEstimation.fakeEstimateTest import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors
import os

gROOT.SetBatch ()

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "fake"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

# '' will gives you Dataset_2016.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['BC', 'DEFGH', '']

nEstFake = []

for runPeriod in runPeriods:

    print "********************************************************************************"
    print "performing fake track background estimate in search region (2016", runPeriod, ")"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2016" + runPeriod + ".root", "recreate")

    fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimate.addTFile (fout)
    fakeTrackBkgdEstimate.addTCanvas (canvas)
    fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
    fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "DisTrkSelectionNoD0CutNHits3",   "MET_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeBkgd_d0sideband")
    fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "DisTrkSelectionSidebandD0Cut",     "MET_2016" + runPeriod,  dirs['Brian']+"2016_final/finalFakeTrackSideband_syst")

    print "********************************************************************************"

    nEstFake.append( fakeTrackBkgdEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing fake track background estimate in ZtoMuMu (2016", runPeriod, ")"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("zToMuMuEstimate_2016" + runPeriod + ".root", "recreate")

    zToMuMuEstimate = FakeTrackBkgdEstimate ()
    zToMuMuEstimate.addTFile (fout)
    zToMuMuEstimate.addTCanvas (canvas)
    zToMuMuEstimate.addLuminosityInInvPb (lumi["SingleMuon_2016" + runPeriod])

    zToMuMuEstimate.addChannel  ("Basic3hits",	    "ZtoMuMuDisTrkNoD0CutNHits3",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeSyst_d0sideband")
    zToMuMuEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkSidebandD0Cut",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/finalFakeTrackSideband")
    zToMuMuEstimate.addChannel  ("Basic",           "BasicSelection",               "MET_2016"      + runPeriod,  dirs['Andrew']+"2016_final_prompt/basicSelection_new")
    zToMuMuEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                      "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu_new")

    print "********************************************************************************"

    nEstFake.append( zToMuMuEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"
