#!/usr/bin/env python

from DisappTrks.StandardAnalysis.closureTest import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 


dirs = getUser() 

print "********************************************************************************"

fout = TFile.Open ("muonBkgdClosureTest.root", "recreate")
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

muonBkgdClosureTest = LeptonBkgdClosureTest ("muon")
muonBkgdClosureTest.addTFile (fout)
muonBkgdClosureTest.addTCanvas (canvas)
muonBkgdClosureTest.addMetCut (100.0)
muonBkgdClosureTest.addChannel  ("TagPt35",             "MuonTagPt35",           "WJetsToLNu",    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",     "WJetsToLNu",    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",    "WJetsToLNu",    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",     "WJetsToLNu",    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       "WJetsToLNu_HT", dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  "WJetsToLNu",    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")

# sample = "TTJets"
# muonBkgdClosureTest.addChannel  ("TagPt35",             "MuonTagPt35",           sample,    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
# #muonBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",     sample,    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
# muonBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",    sample,    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
# #muonBkgdClosureTest.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",     sample,    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
# muonBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       sample,    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
# muonBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  sample,    dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
# muonBkgdClosureTest.printSingleLeptonTriggerEff ()

print "********************************************************************************"

muonBkgdClosureTest.printNest ()

print "--------------------------------------------------------------------------------"

muonBkgdClosureTest.printNback ()

print "********************************************************************************"

fout.Close ()
