#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.closureTest import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

dirs = getUser()

print "********************************************************************************"
print "performing muon background closure test with WJetsToLNu..."
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdClosureTest_WJetsToLNu.root", "recreate")
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

muonBkgdClosureTest_WJetsToLNu = LeptonBkgdClosureTest ("muon")
muonBkgdClosureTest_WJetsToLNu.addTFile (fout)
muonBkgdClosureTest_WJetsToLNu.addTCanvas (canvas)
muonBkgdClosureTest_WJetsToLNu.addMetCut (100.0)
muonBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35",             "MuonTagPt35",           "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",     "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",    "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",     "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_WJetsToLNu.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       "WJetsToLNu_HT",  dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest_WJetsToLNu.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest_WJetsToLNu.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_WJetsToLNu.printNest ()

print "--------------------------------------------------------------------------------"

(nBack, nBackError) = muonBkgdClosureTest_WJetsToLNu.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background closure test with TTJets..."
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdClosureTest_TTJets.root", "recreate")

muonBkgdClosureTest_TTJets = LeptonBkgdClosureTest ("muon")
muonBkgdClosureTest_TTJets.addTFile (fout)
muonBkgdClosureTest_TTJets.addTCanvas (canvas)
muonBkgdClosureTest_TTJets.addMetCut (100.0)
muonBkgdClosureTest_TTJets.addChannel  ("TagPt35",             "MuonTagPt35",           "TTJets",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest_TTJets.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",     "TTJets",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_TTJets.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",    "TTJets",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest_TTJets.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",     "TTJets",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       "TTJets",  dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  "TTJets",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS_LHS")
muonBkgdClosureTest_TTJets.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_TTJets.printNest ()

print "--------------------------------------------------------------------------------"

(nBack, nBackError) = muonBkgdClosureTest_TTJets.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"

fout.Close ()
