#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.bkgdEstimate import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import TCanvas, TFile
import os

# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/672
pPassVeto = (1.73e-5, 0.77e-5)

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing muon background closure test with WJetsToLNu..."
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdClosureTest_WJetsToLNu.root", "recreate")

muonBkgdClosureTest_WJetsToLNu = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_WJetsToLNu.addTFile (fout)
muonBkgdClosureTest_WJetsToLNu.addTCanvas (canvas)
muonBkgdClosureTest_WJetsToLNu.addMetCut (100.0)
muonBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35",             "MuonTagPt35",           "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_WJetsToLNu.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",    "WJetsToLNu",     dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
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

muonBkgdClosureTest_TTJets = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_TTJets.addTFile (fout)
muonBkgdClosureTest_TTJets.addTCanvas (canvas)
muonBkgdClosureTest_TTJets.addMetCut (100.0)
muonBkgdClosureTest_TTJets.addChannel  ("TagPt35",             "MuonTagPt35",           "TTJets",  dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_TTJets.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",    "TTJets",  dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       "TTJets",  dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  "TTJets",  dirs['Andrew']+"withFiducialCuts/muonBkgdClosureTest_LHS_LHS")
muonBkgdClosureTest_TTJets.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_TTJets.printNest ()

print "--------------------------------------------------------------------------------"

(nBack, nBackError) = muonBkgdClosureTest_TTJets.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background closure test in candidate track control region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdClosureTest_CandTrk.root", "recreate")

muonBkgdClosureTest_CandTrk = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_CandTrk.addTFile (fout)
muonBkgdClosureTest_CandTrk.addTCanvas (canvas)
muonBkgdClosureTest_CandTrk.addMetCut (100.0)
muonBkgdClosureTest_CandTrk.addPpassVeto (pPassVeto)
muonBkgdClosureTest_CandTrk.addChannel  ("TagPt35",         "MuonTagPt50",         "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForCandidateTrackSelection")
muonBkgdClosureTest_CandTrk.addChannel  ("TagPt35MetTrig",  "MuonTagPt50MetTrig",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForCandidateTrackSelection")
muonBkgdClosureTest_CandTrk.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_CandTrk.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background closure test in missing outer hits sideband region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdClosureTest_NmissOutSideband.root", "recreate")

muonBkgdClosureTest_NmissOutSideband = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_NmissOutSideband.addTFile (fout)
muonBkgdClosureTest_NmissOutSideband.addTCanvas (canvas)
muonBkgdClosureTest_NmissOutSideband.addMetCut (100.0)
muonBkgdClosureTest_NmissOutSideband.addPpassVeto (pPassVeto)
muonBkgdClosureTest_NmissOutSideband.addChannel  ("TagPt35",         "MuonTagPt50",         "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForMissingOuterHitsSideband")
muonBkgdClosureTest_NmissOutSideband.addChannel  ("TagPt35MetTrig",  "MuonTagPt50MetTrig",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForMissingOuterHitsSideband")
muonBkgdClosureTest_NmissOutSideband.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_NmissOutSideband.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate.root", "recreate")

muonBkgdClosureTest_DisTrk = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_DisTrk.addTFile (fout)
muonBkgdClosureTest_DisTrk.addTCanvas (canvas)
muonBkgdClosureTest_DisTrk.addMetCut (100.0)
muonBkgdClosureTest_DisTrk.addPpassVeto (pPassVeto)
muonBkgdClosureTest_DisTrk.addChannel  ("TagPt35",         "MuonTagPt50",         "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForDisappearingTrackSelection")
muonBkgdClosureTest_DisTrk.addChannel  ("TagPt35MetTrig",  "MuonTagPt50MetTrig",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForDisappearingTrackSelection")
muonBkgdClosureTest_DisTrk.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_DisTrk.printNest ()

print "\n\n"
print "********************************************************************************"
print "performing muon background estimate in disappearing track search region without missing outer hits cut for MC"
print "--------------------------------------------------------------------------------"

sample = "allBkgd"
fout = TFile.Open ("muonBkgdEstimate_MC.root", "recreate")
muonBkgdClosureTest_DisTrkMC = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_DisTrkMC.addTFile (fout)
muonBkgdClosureTest_DisTrkMC.addTCanvas (canvas)
muonBkgdClosureTest_DisTrkMC.addMetCut (100.0)
muonBkgdClosureTest_DisTrkMC.addChannel  ("TagProbe",       "ZtoMuProbeTrkWithZCuts",       sample, dirs['Wells']+"ZtoMuProbeTrkWithZCuts")
muonBkgdClosureTest_DisTrkMC.addChannel  ("TagProbePass",   "ZtoMuDisTrk",                  sample, dirs['Wells']+"ZtoMuDisTrk")
muonBkgdClosureTest_DisTrkMC.addChannel  ("TagPt35",        "MuonTagPt55NoNMissOut",        sample, dirs['Wells']+"MuonTagPt55NoNMissOut")
muonBkgdClosureTest_DisTrkMC.addChannel  ("TagPt35MetTrig", "MuonTagPt55NoNMissOutMetTrig", sample, dirs['Wells']+"MuonTagPt55NoNMissOut")
muonBkgdClosureTest_DisTrkMC.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_DisTrkMC.printNest ()

print "\n\n"
print "********************************************************************************"
print "performing muon background estimate in loose candidate track region for MC"
print "--------------------------------------------------------------------------------"

#sample = "allBkgd"
sample = "TTJets"
fout = TFile.Open ("muonBkgdEstimate_CandTrkLooseMC.root", "recreate")
muonBkgdClosureTest_CandTrkLooseMC = LeptonBkgdEstimate ("muon")
muonBkgdClosureTest_CandTrkLooseMC.addTFile (fout)
muonBkgdClosureTest_CandTrkLooseMC.addTCanvas (canvas)
muonBkgdClosureTest_CandTrkLooseMC.addMetCut (100.0)
muonBkgdClosureTest_CandTrkLooseMC.useMetMinusOneForIntegrals (False)
muonBkgdClosureTest_CandTrkLooseMC.useIdMatch (True)
muonBkgdClosureTest_CandTrkLooseMC.addChannel  ("TagProbe",       "ZtoMuProbeTrkWithZCuts", sample, dirs['Wells']+"ZtoMuProbeTrkWithZCuts")
muonBkgdClosureTest_CandTrkLooseMC.addChannel  ("TagProbePass",   "ZtoMuProbeTrkTightVeto",            sample, dirs['Wells']+"ZtoMuDisTrk")
muonBkgdClosureTest_CandTrkLooseMC.addChannel  ("TagPt35",        "MuonTagPt55NoNMissOut",        sample, dirs['Wells']+"MuonTagPt55NoNMissOut")
muonBkgdClosureTest_CandTrkLooseMC.addChannel  ("TagPt35MetTrig", "MuonTagPt55NoNMissOutMetTrig", sample, dirs['Wells']+"MuonTagPt55NoNMissOut")
muonBkgdClosureTest_CandTrkLooseMC.addChannel  ("CandTrkIdPt35",  "CandTrkLoose",                 sample, dirs['Wells']+"candTrkLooseV2", True)
muonBkgdClosureTest_CandTrkLooseMC.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest_CandTrkLooseMC.printNest ()

print "--------------------------------------------------------------------------------"
(nBack, nBackError) = muonBkgdClosureTest_CandTrkLooseMC.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"


print "********************************************************************************"

fout.Close ()
