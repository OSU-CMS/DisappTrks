#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.bkgdEstimate import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import TCanvas, TFile
import os

# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/706
pPassVeto = (0.104, 0.013)

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

#print "********************************************************************************"
#print "performing tau background closure test with WJetsToLNu..."
#print "--------------------------------------------------------------------------------"

#fout = TFile.Open ("tauBkgdClosureTest_WJetsToLNu.root", "recreate")

#tauBkgdClosureTest_WJetsToLNu = LeptonBkgdEstimate ("tau")
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

tauBkgdClosureTest_TTJets = LeptonBkgdEstimate ("tau")
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

tauBkgdClosureTest_CandTrk = LeptonBkgdEstimate ("tau")
tauBkgdClosureTest_CandTrk.addTFile (fout)
tauBkgdClosureTest_CandTrk.addTCanvas (canvas)
tauBkgdClosureTest_CandTrk.addMetCut (100.0)
tauBkgdClosureTest_CandTrk.addPpassVeto (pPassVeto)
tauBkgdClosureTest_CandTrk.addPrescaleFactor (11.559)
tauBkgdClosureTest_CandTrk.addChannel  ("TagPt35",         "TauTagPt50",         "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_CandTrk.addChannel  ("TagPt35MetTrig",  "TauTagPt50MetTrig",  "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_CandTrk.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = tauBkgdClosureTest_CandTrk.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background closure test in missing outer hits sideband region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdClosureTest_NmissOutSideband.root", "recreate")

tauBkgdClosureTest_NmissOutSideband = LeptonBkgdEstimate ("tau")
tauBkgdClosureTest_NmissOutSideband.addTFile (fout)
tauBkgdClosureTest_NmissOutSideband.addTCanvas (canvas)
tauBkgdClosureTest_NmissOutSideband.addMetCut (100.0)
tauBkgdClosureTest_NmissOutSideband.addPpassVeto (pPassVeto)
tauBkgdClosureTest_NmissOutSideband.addPrescaleFactor (11.559)
tauBkgdClosureTest_NmissOutSideband.addChannel  ("TagPt35ForNctrl",  "TauTagPt50",         "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForMissingOuterHitsSideband")
tauBkgdClosureTest_NmissOutSideband.addChannel  ("TagPt35",          "TauTagPt50",         "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_NmissOutSideband.addChannel  ("TagPt35MetTrig",   "TauTagPt50MetTrig",  "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_NmissOutSideband.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = tauBkgdClosureTest_NmissOutSideband.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdEstimate.root", "recreate")

tauBkgdClosureTest_DisTrk = LeptonBkgdEstimate ("tau")
tauBkgdClosureTest_DisTrk.addTFile (fout)
tauBkgdClosureTest_DisTrk.addTCanvas (canvas)
tauBkgdClosureTest_DisTrk.addMetCut (100.0)
tauBkgdClosureTest_DisTrk.addPpassVeto (pPassVeto)
tauBkgdClosureTest_DisTrk.addPrescaleFactor (11.559)
tauBkgdClosureTest_DisTrk.addChannel  ("TagPt35ForNctrl",  "TauTagPt50",         "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForDisappearingTrackSelection")
tauBkgdClosureTest_DisTrk.addChannel  ("TagPt35",          "TauTagPt50",         "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_DisTrk.addChannel  ("TagPt35MetTrig",   "TauTagPt50MetTrig",  "Tau_2015D",  dirs['Andrew']+"withFiducialCuts/tauBkgdForCandidateTrackSelection_noJetMETCut")
tauBkgdClosureTest_DisTrk.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = tauBkgdClosureTest_DisTrk.printNest ()

print "********************************************************************************"

fout.Close ()
