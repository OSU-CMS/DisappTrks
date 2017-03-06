#!/usr/bin/env python

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
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
fakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",         "MET_2015D",       dirs['Andrew']+"2015/basicSelection")
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

print "\n\n"

print "********************************************************************************"
print "evaluating electron energy systematic"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronEnergySystematic_2015.root", "recreate")

electronEnergySystematic = LeptonEnergySystematic ("electron")
electronEnergySystematic.addTFile (fout)
electronEnergySystematic.addTCanvas (canvas)
electronEnergySystematic.addLuminosityLabel ("2.67 fb^{-1} (13 TeV)")
electronEnergySystematic.addPlotLabel ("SingleElectron 2015D")
electronEnergySystematic.addMetCut (100.0)
electronEnergySystematic.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2015D",  dirs['Andrew']+"2015/electronBackgroundControlRegion")
electronEnergySystematic.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2015D",  dirs['Andrew']+"2015/electronBackgroundControlRegion")

print "********************************************************************************"

electronEnergySystematic.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating tau energy systematic"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauEnergySystematic_2015.root", "recreate")

tauEnergySystematic = LeptonEnergySystematic ("tau")
tauEnergySystematic.addTFile (fout)
tauEnergySystematic.addTCanvas (canvas)
tauEnergySystematic.addLuminosityLabel ("0.225 fb^{-1} (13 TeV)")
tauEnergySystematic.addPlotLabel ("Tau 2015D")
tauEnergySystematic.addMetCut (100.0)
tauEnergySystematic.addRebinFactor (4)
tauEnergySystematic.addChannel  ("TagPt35",         "TauTagPt55",          "Tau_2015D",  dirs['Andrew']+"2015/tauBackgroundControlRegion")
#tauEnergySystematic.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",   "Tau_2015D",  dirs['Andrew']+"2015/tauBackgroundControlRegion")
tauEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",               "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackgroundControlRegion")
tauEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",        "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackgroundControlRegion")

print "********************************************************************************"

tauEnergySystematic.printSystematic ()

print "********************************************************************************"

fout.Close ()
