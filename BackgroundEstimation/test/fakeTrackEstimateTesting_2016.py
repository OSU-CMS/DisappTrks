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
    fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "DisTrkSelectionInvertD0Cut",     "MET_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeBkgd_d0sideband")

    print "********************************************************************************"

    nEstFake.append( fakeTrackBkgdEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"
