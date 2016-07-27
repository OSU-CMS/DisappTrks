#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.bkgdEstimate import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

metLumi       =  6317.0
electronLumi  =  6235.971
muonLumi      =  6227.437
tauLumi       =  742.02

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing fake track background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate.root", "recreate")

fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate.addTFile (fout)
fakeTrackBkgdEstimate.addTCanvas (canvas)
fakeTrackBkgdEstimate.addPrescaleFactor (metLumi / muonLumi)
fakeTrackBkgdEstimate.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2016B",  dirs['Andrew']+"2016/zToMuMu")
fakeTrackBkgdEstimate.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2016B",  dirs['Andrew']+"2016/zToMuMuTrack")
fakeTrackBkgdEstimate.addChannel  ("Basic",        "BasicSelection",  "MET_2016B",       dirs['Andrew']+"2016/basicSelection")

print "********************************************************************************"

(nEstFake, nEstFakeError) = fakeTrackBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdEstimate.root", "recreate")

electronBkgdEstimate = LeptonBkgdEstimate ("electron")
electronBkgdEstimate.addTFile (fout)
electronBkgdEstimate.addTCanvas (canvas)
electronBkgdEstimate.addPrescaleFactor (metLumi / electronLumi)
electronBkgdEstimate.addMetCut (100.0)
electronBkgdEstimate.useMetMinusOneForIntegrals (True)
electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2016B",  dirs['Andrew']+"2016/electronTagAndProbe")
electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2016B",  dirs['Andrew']+"2016/electronTagAndProbe")
electronBkgdEstimate.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2016B",  dirs['Andrew']+"2016/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2016B",  dirs['Andrew']+"2016/electronBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstElectron, nEstElectronError) = electronBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate.root", "recreate")

muonBkgdEstimate = LeptonBkgdEstimate ("muon")
muonBkgdEstimate.addTFile (fout)
muonBkgdEstimate.addTCanvas (canvas)
muonBkgdEstimate.addPrescaleFactor (metLumi / muonLumi)
muonBkgdEstimate.addMetCut (100.0)
muonBkgdEstimate.useMetMinusOneForIntegrals (False)
muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2016B",  dirs['Andrew']+"2016/muonTagAndProbe")
muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2016B",  dirs['Andrew']+"2016/muonTagAndProbe")
muonBkgdEstimate.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2016B",  dirs['Andrew']+"2016/muonBkgdForDisappearingTrackSelection")
muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2016B",  dirs['Andrew']+"2016/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstMuon, nEstMuonError) = muonBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
#nEst = nEstElectron + nEstMuon + nEstTau
nEst = nEstElectron + nEstMuon
#nEstError = math.hypot (math.hypot (nEstElectronError, nEstMuonError), nEstTauError)
nEstError = math.hypot (nEstElectronError, nEstMuonError)
print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"

print "\n\n"

print "********************************************************************************"
nEst += nEstFake
nEstError = math.hypot (nEstError, nEstFakeError)
print "total background: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"
