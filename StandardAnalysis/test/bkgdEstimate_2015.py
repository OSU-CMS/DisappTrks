#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.closureTest import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing electron background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdClosureTest.root", "recreate")

electronBkgdClosureTest = LeptonBkgdClosureTest ("electron")
electronBkgdClosureTest.addTFile (fout)
electronBkgdClosureTest.addTCanvas (canvas)
electronBkgdClosureTest.addMetCut (100.0)
electronBkgdClosureTest.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronTagAndProbe")
electronBkgdClosureTest.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronTagAndProbe")
electronBkgdClosureTest.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronBkgdForDisappearingTrackSelection")
electronBkgdClosureTest.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstElectron, nEstElectronError) = electronBkgdClosureTest.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdClosureTest.root", "recreate")

muonBkgdClosureTest = LeptonBkgdClosureTest ("muon")
muonBkgdClosureTest.addTFile (fout)
muonBkgdClosureTest.addTCanvas (canvas)
muonBkgdClosureTest.addMetCut (100.0)
muonBkgdClosureTest.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonTagAndProbe")
muonBkgdClosureTest.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonTagAndProbe")
muonBkgdClosureTest.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForDisappearingTrackSelection")
muonBkgdClosureTest.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstMuon, nEstMuonError) = muonBkgdClosureTest.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdClosureTest.root", "recreate")

tauBkgdClosureTest = LeptonBkgdClosureTest ("tau")
tauBkgdClosureTest.addTFile (fout)
tauBkgdClosureTest.addTCanvas (canvas)
tauBkgdClosureTest.addMetCut (100.0)
tauBkgdClosureTest.addChannel  ("TagProbe",        "ZtoTauProbeTrkWithZCuts",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/tauTagAndProbe")
tauBkgdClosureTest.addChannel  ("TagProbePass",    "ZtoTauDisTrk",             "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/tauTagAndProbe")
tauBkgdClosureTest.addChannel  ("TagPt35",         "TauTagPt55",             "Tau_2015D",       dirs['Andrew']+"withFiducialCuts/tauBkgdForDisappearingTrackSelection")
tauBkgdClosureTest.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",      "Tau_2015D",       dirs['Andrew']+"withFiducialCuts/tauBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstTau, nEstTauError) = tauBkgdClosureTest.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
nEst = nEstElectron + nEstMuon + nEstTau
nEstError = math.hypot (math.hypot (nEstElectronError, nEstMuonError), nEstTauError)
print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"
