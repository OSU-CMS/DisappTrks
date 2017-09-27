#!/usr/bin/env python

import math, os
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate
from DisappTrks.BackgroundEstimation.fakeEstimateTest import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I too am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing tau closure test with just DYJetsToLL_50 (2016)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauClosureTest_DYJetsToLL_50.root", "recreate")

tauBkgdEstimate_DYJetsToLL_50 = LeptonBkgdEstimate ("tau")
tauBkgdEstimate_DYJetsToLL_50.addTFile (fout)
tauBkgdEstimate_DYJetsToLL_50.addTCanvas (canvas)
tauBkgdEstimate_DYJetsToLL_50.addPrescaleFactor ((lumi["MET_2015"] + lumi["MET_2016"]) / lumi["MET_2016DEFGH"])
tauBkgdEstimate_DYJetsToLL_50.addLuminosityInInvPb (lumi["MET_2015"] + lumi["MET_2016"])
tauBkgdEstimate_DYJetsToLL_50.addLuminosityLabel (str (round ((lumi["MET_2015"] + lumi["MET_2016"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
tauBkgdEstimate_DYJetsToLL_50.addMetCut (100.0)
tauBkgdEstimate_DYJetsToLL_50.addPhiCut (-1.0)
tauBkgdEstimate_DYJetsToLL_50.addECaloCut (10.0)
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCuts",     "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoNMissOutCut",   "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCuts",    "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoNMissOutCut",  "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("TagPt35",         "TauTagPt55NoJetCuts",             "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_tauTagSkim")
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("TagPt35MetTrig",  "TauTagPt55NoJetCutsMetTrig",      "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_tauTagSkim")
tauBkgdEstimate_DYJetsToLL_50.addChannel  ("CandTrkIdPt35",   "CandTrkIdTauPt55",                "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_metMinimalSkim")

print "********************************************************************************"

est = tauBkgdEstimate_DYJetsToLL_50.printNest ()

print "--------------------------------------------------------------------------------"

obs = tauBkgdEstimate_DYJetsToLL_50.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau closure test with just WZToLNuNuNu (2016)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauClosureTest_WZToLNuNuNu.root", "recreate")

tauBkgdEstimate_WZToLNuNuNu = LeptonBkgdEstimate ("tau")
tauBkgdEstimate_WZToLNuNuNu.addTFile (fout)
tauBkgdEstimate_WZToLNuNuNu.addTCanvas (canvas)
tauBkgdEstimate_WZToLNuNuNu.addPrescaleFactor ((lumi["MET_2015"] + lumi["MET_2016"]) / lumi["MET_2016DEFGH"])
tauBkgdEstimate_WZToLNuNuNu.addLuminosityInInvPb (lumi["MET_2015"] + lumi["MET_2016"])
tauBkgdEstimate_WZToLNuNuNu.addLuminosityLabel (str (round ((lumi["MET_2015"] + lumi["MET_2016"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
tauBkgdEstimate_WZToLNuNuNu.addMetCut (100.0)
tauBkgdEstimate_WZToLNuNuNu.addPhiCut (-1.0)
tauBkgdEstimate_WZToLNuNuNu.addECaloCut (10.0)
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCuts",     "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoNMissOutCut",   "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCuts",    "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoNMissOutCut",  "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("TagPt35",         "TauTagPt55NoJetCuts",             "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_tauTagSkim")
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("TagPt35MetTrig",  "TauTagPt55NoJetCutsMetTrig",      "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_tauTagSkim")
tauBkgdEstimate_WZToLNuNuNu.addChannel  ("CandTrkIdPt35",   "CandTrkIdTauPt55",                "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_metMinimalSkim")

print "********************************************************************************"

est = tauBkgdEstimate_WZToLNuNuNu.printNest ()

print "--------------------------------------------------------------------------------"

obs = tauBkgdEstimate_WZToLNuNuNu.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
