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
electronBkgdClosureTest.useMetMinusOneForIntegrals (True)
electronBkgdClosureTest.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2016B",  dirs['Andrew']+"2016/electronTagAndProbe")
electronBkgdClosureTest.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2016B",  dirs['Andrew']+"2016/electronTagAndProbe")
electronBkgdClosureTest.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2016B",  dirs['Andrew']+"2016/electronBkgdForDisappearingTrackSelection")
electronBkgdClosureTest.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2016B",  dirs['Andrew']+"2016/electronBkgdForDisappearingTrackSelection")

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
muonBkgdClosureTest.useMetMinusOneForIntegrals (False)
muonBkgdClosureTest.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2016B",  dirs['Andrew']+"2016/muonTagAndProbe")
muonBkgdClosureTest.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2016B",  dirs['Andrew']+"2016/muonTagAndProbe")
muonBkgdClosureTest.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2016B",  dirs['Andrew']+"2016/muonBkgdForDisappearingTrackSelection")
muonBkgdClosureTest.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2016B",  dirs['Andrew']+"2016/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstMuon, nEstMuonError) = muonBkgdClosureTest.printNest ()

print "********************************************************************************"

fout.Close ()
