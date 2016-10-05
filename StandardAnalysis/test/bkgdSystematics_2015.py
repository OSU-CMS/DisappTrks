#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.bkgdSystematics import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "evaluating fake track systematic"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2015.root", "recreate")

fakeTrackSystematic = FakeTrackSystematic ()
fakeTrackSystematic.addTFile (fout)
fakeTrackSystematic.addTCanvas (canvas)
fakeTrackSystematic.addLuminosityLabel ("2.59 fb^{-1} (13 TeV)")
fakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",         "MET_2015D",       dirs['Andrew']+"withFiducialCuts/basicSelection")
fakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2015D",       dirs['Andrew']+"2015/fakeTrackSystematics")
fakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2015D",       dirs['Andrew']+"2015/fakeTrackSystematics")
fakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2015D",       dirs['Andrew']+"2015/fakeTrackSystematics")
fakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2015D",       dirs['Andrew']+"2015/fakeTrackSystematics")
fakeTrackSystematic.addChannel  ("ZtoMuMu",              "ZtoMuMu",                "SingleMu_2015D",  dirs['Andrew']+"2015/zToMuMu")
fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2015D",  dirs['Andrew']+"2015/fakeTrackBackground")
fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2015D",  dirs['Andrew']+"2015/fakeTrackBackground")
fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2015D",  dirs['Andrew']+"2015/fakeTrackBackground")
fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2015D",  dirs['Andrew']+"2015/fakeTrackBackground")

print "********************************************************************************"

fakeTrackSystematic.printSystematic ()

print "********************************************************************************"

fout.Close ()
