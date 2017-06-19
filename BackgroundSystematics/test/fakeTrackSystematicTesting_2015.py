#!/usr/bin/env python

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile
import os

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

print "*************************************************************************************"
print "evaluating fake track systematic in data with sideband D0 cut (2015)"
print "-------------------------------------------------------------------------------------"

fout = TFile.Open ("sidebandD0CutFakeTrackSystematic_2015.root", "recreate")

sidebandD0CutFakeTrackSystematic = FakeTrackSystematic ()
sidebandD0CutFakeTrackSystematic.addTFile (fout)
sidebandD0CutFakeTrackSystematic.addTCanvas (canvas)
sidebandD0CutFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2015D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
sidebandD0CutFakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",                     "MET_2015D",       dirs['Brian']+"2015/basicSelection")
sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionSidebandD0CutNHits3", "MET_2015D",       dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits3NoD0Cut",  "DisTrkSelectionNoD0CutNHits3",       "MET_2015D",       dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionSidebandD0CutNHits4", "MET_2015D",       dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionSidebandD0CutNHits5", "MET_2015D",       dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionSidebandD0CutNHits6", "MET_2015D",       dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                            "SingleMu_2015D",  dirs['Brian']+"2015/zToMuMu")

sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkSidebandD0CutNHits3",   "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3NoD0Cut",  "ZtoMuMuDisTrkNoD0CutNHits3",   "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_noD0Cut")
sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkSidebandD0CutNHits4",   "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkSidebandD0CutNHits5",   "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkSidebandD0CutNHits6",   "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
sidebandD0CutFakeTrackSystematic.addD0TransferFactor ()
sidebandD0CutFakeTrackSystematic.reweightTo ("MET_2015D", dirs['Brian']+"2015/basicSelection", "BasicSelection", "Eventvariable Plots/nTracks")

print "********************************************************************************"

sidebandD0CutFakeTrackSystematic.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"
