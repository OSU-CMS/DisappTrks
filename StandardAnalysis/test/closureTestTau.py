#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.closureTest import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

dirs = getUser()

#print "********************************************************************************"
#print "performing tau background closure test with WJetsToLNu..."
#print "--------------------------------------------------------------------------------"

#fout = TFile.Open ("tauBkgdClosureTest_WJetsToLNu.root", "recreate")
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

#tauBkgdClosureTest_WJetsToLNu = LeptonBkgdClosureTest ("tau")
#tauBkgdClosureTest_WJetsToLNu.addTFile (fout)
#tauBkgdClosureTest_WJetsToLNu.addTCanvas (canvas)
#tauBkgdClosureTest_WJetsToLNu.addMetCut (100.0)
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35",             "TauTagPt50",           "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50")
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35NoTrig",       "TauTagPt50NoTrig",     "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest")
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35MetTrig",      "TauTagPt50MetTrig",    "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50MetTrig")
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35MetCut",       "TauTagPt50MetCut",     "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50MetCut")
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("CandTrkIdPt35",       "CandTrkIdTauPt50",       "WJetsToLNu_HT",  dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_CandTrkIdTauPt50")
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdTauPt50NoMet",  "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_CandTrkIdTauPt50NoMet")
#tauBkgdClosureTest_WJetsToLNu.printSingleLeptonTriggerEff ()

#print "********************************************************************************"

#(nEst, nEstError) = tauBkgdClosureTest_WJetsToLNu.printNest ()

#print "--------------------------------------------------------------------------------"

#(nBack, nBackError) = tauBkgdClosureTest_WJetsToLNu.printNback ()
#print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

#print "********************************************************************************"

#fout.Close ()

#print "\n\n"

print "********************************************************************************"
print "performing tau background closure test with TTJets..."
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdClosureTest_TTJets.root", "recreate")

tauBkgdClosureTest_TTJets = LeptonBkgdClosureTest ("tau")
tauBkgdClosureTest_TTJets.addTFile (fout)
tauBkgdClosureTest_TTJets.addTCanvas (canvas)
tauBkgdClosureTest_TTJets.addMetCut (100.0)
tauBkgdClosureTest_TTJets.addChannel  ("TagPt35",             "TauTagPt50",           "TTJets",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50")
#tauBkgdClosureTest_TTJets.addChannel  ("TagPt35NoTrig",       "TauTagPt50NoTrig",     "TTJets",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest")
tauBkgdClosureTest_TTJets.addChannel  ("TagPt35MetTrig",      "TauTagPt50MetTrig",    "TTJets",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50MetTrig")
#tauBkgdClosureTest_TTJets.addChannel  ("TagPt35MetCut",       "TauTagPt50MetCut",     "TTJets",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50MetCut")
tauBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35",       "CandTrkIdTauPt50",       "TTJets",  dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_CandTrkIdTauPt50")
tauBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdTauPt50NoMet",  "TTJets",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_CandTrkIdTauPt50NoMet")
tauBkgdClosureTest_TTJets.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = tauBkgdClosureTest_TTJets.printNest ()

print "--------------------------------------------------------------------------------"

(nBack, nBackError) = tauBkgdClosureTest_TTJets.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"

fout.Close ()
