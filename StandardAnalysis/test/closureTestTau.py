#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.closureTest import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

#print "********************************************************************************"
#print "performing tau background closure test with WJetsToLNu..."
#print "--------------------------------------------------------------------------------"

#fout = TFile.Open ("tauBkgdClosureTest_WJetsToLNu.root", "recreate")

#tauBkgdClosureTest_WJetsToLNu = LeptonBkgdClosureTest ("tau")
#tauBkgdClosureTest_WJetsToLNu.addTFile (fout)
#tauBkgdClosureTest_WJetsToLNu.addTCanvas (canvas)
#tauBkgdClosureTest_WJetsToLNu.addMetCut (100.0)
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35",             "TauTagPt50",             "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50")
#tauBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35MetTrig",      "TauTagPt50MetTrig",      "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50MetTrig")
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
tauBkgdClosureTest_TTJets.addChannel  ("TagPt35",             "TauTagPt50",             "TTJets",  dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50")
tauBkgdClosureTest_TTJets.addChannel  ("TagPt35MetTrig",      "TauTagPt50MetTrig",      "TTJets",  dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_TauTagPt50MetTrig")
tauBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35",       "CandTrkIdTauPt50",       "TTJets",  dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_CandTrkIdTauPt50")
tauBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdTauPt50NoMet",  "TTJets",  dirs['Andrew']+"withFiducialCuts/tauBkgdClosureTest_CandTrkIdTauPt50NoMet")
tauBkgdClosureTest_TTJets.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = tauBkgdClosureTest_TTJets.printNest ()

print "--------------------------------------------------------------------------------"

(nBack, nBackError) = tauBkgdClosureTest_TTJets.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background closure test in candidate track control region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdClosureTest_CandTrk.root", "recreate")

tauBkgdClosureTest_CandTrk = LeptonBkgdClosureTest ("tau")
tauBkgdClosureTest_CandTrk.addTFile (fout)
tauBkgdClosureTest_CandTrk.addTCanvas (canvas)
tauBkgdClosureTest_CandTrk.addMetCut (100.0)
tauBkgdClosureTest_CandTrk.addPpassVeto ((0.104, 0.013))
tauBkgdClosureTest_CandTrk.addPrescaleFactor (11.559)
tauBkgdClosureTest_CandTrk.addChannel  ("TagPt35",         "TauTagPt50",         "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_CandTrk.addChannel  ("TagPt35MetTrig",  "TauTagPt50MetTrig",  "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_CandTrk.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = tauBkgdClosureTest_CandTrk.printNest ()

print "********************************************************************************"

fout.Close ()
