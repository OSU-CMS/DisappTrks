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
print "evaluating fake track systematic (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2016_v3.root", "recreate")

fakeTrackSystematic_v3 = FakeTrackSystematic ()
fakeTrackSystematic_v3.addTFile (fout)
fakeTrackSystematic_v3.addTCanvas (canvas)
fakeTrackSystematic_v3.addLuminosityLabel ("8.53 fb^{-1} (13 TeV)")
fakeTrackSystematic_v3.addChannel  ("Basic",                "BasicSelection",         "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/basicSelection")
fakeTrackSystematic_v3.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v3.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v3.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v3.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v3.addChannel  ("ZtoMuMu",              "ZtoMuMu",                "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackSystematic_v3.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackSystematic_v3.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackSystematic_v3.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackSystematic_v3.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")

print "********************************************************************************"

fakeTrackSystematic_v3.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating fake track systematic (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2016_v4.root", "recreate")

fakeTrackSystematic_v4 = FakeTrackSystematic ()
fakeTrackSystematic_v4.addTFile (fout)
fakeTrackSystematic_v4.addTCanvas (canvas)
fakeTrackSystematic_v4.addLuminosityLabel ("4.35 fb^{-1} (13 TeV)")
fakeTrackSystematic_v4.addChannel  ("Basic",                "BasicSelection",         "MET_2016D",       dirs['Andrew']+"2016_ICHEP/basicSelection")
fakeTrackSystematic_v4.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016D",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v4.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016D",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v4.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016D",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v4.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016D",       dirs['Andrew']+"2016_ICHEP/fakeTrackSystematics")
fakeTrackSystematic_v4.addChannel  ("ZtoMuMu",              "ZtoMuMu",                "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackSystematic_v4.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackSystematic_v4.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackSystematic_v4.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackSystematic_v4.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")

print "********************************************************************************"

fakeTrackSystematic_v4.printSystematic ()

print "********************************************************************************"

fout.Close ()
