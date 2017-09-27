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
print "performing muon closure test with just DYJetsToLL_50 (2016)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonClosureTest_DYJetsToLL_50.root", "recreate")

muonBkgdEstimate_DYJetsToLL_50 = LeptonBkgdEstimate ("muon")
muonBkgdEstimate_DYJetsToLL_50.addTFile (fout)
muonBkgdEstimate_DYJetsToLL_50.addTCanvas (canvas)
muonBkgdEstimate_DYJetsToLL_50.addPrescaleFactor ((lumi["MET_2015"] + lumi["MET_2016"]) / lumi["MET_2016DEFGH"])
muonBkgdEstimate_DYJetsToLL_50.addLuminosityInInvPb (lumi["MET_2015"] + lumi["MET_2016"])
muonBkgdEstimate_DYJetsToLL_50.addLuminosityLabel (str (round ((lumi["MET_2015"] + lumi["MET_2016"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
muonBkgdEstimate_DYJetsToLL_50.addMetCut (100.0)
muonBkgdEstimate_DYJetsToLL_50.addPhiCut (-1.0)
muonBkgdEstimate_DYJetsToLL_50.addECaloCut (10.0)
muonBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",       "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoNMissOutCut",     "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_DYJetsToLL_50.addChannel  ("TagPt35",         "MuonTagPt35NoJetCuts",         "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_DYJetsToLL_50.addChannel  ("TagPt35MetTrig",  "MuonTagPt35NoJetCutsMetTrig",  "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_DYJetsToLL_50.addChannel  ("CandTrkIdPt35",   "CandTrkIdMuPt35",              "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_metMinimalSkim")

print "********************************************************************************"

est = muonBkgdEstimate_DYJetsToLL_50.printNest ()

print "--------------------------------------------------------------------------------"

obs = muonBkgdEstimate_DYJetsToLL_50.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon closure test with just WZToLNuNuNu (2016)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonClosureTest_WZToLNuNuNu.root", "recreate")

muonBkgdEstimate_WZToLNuNuNu = LeptonBkgdEstimate ("muon")
muonBkgdEstimate_WZToLNuNuNu.addTFile (fout)
muonBkgdEstimate_WZToLNuNuNu.addTCanvas (canvas)
muonBkgdEstimate_WZToLNuNuNu.addPrescaleFactor ((lumi["MET_2015"] + lumi["MET_2016"]) / lumi["MET_2016DEFGH"])
muonBkgdEstimate_WZToLNuNuNu.addLuminosityInInvPb (lumi["MET_2015"] + lumi["MET_2016"])
muonBkgdEstimate_WZToLNuNuNu.addLuminosityLabel (str (round ((lumi["MET_2015"] + lumi["MET_2016"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
muonBkgdEstimate_WZToLNuNuNu.addMetCut (100.0)
muonBkgdEstimate_WZToLNuNuNu.addPhiCut (-1.0)
muonBkgdEstimate_WZToLNuNuNu.addECaloCut (10.0)
muonBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",       "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoNMissOutCut",     "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_WZToLNuNuNu.addChannel  ("TagPt35",         "MuonTagPt35NoJetCuts",         "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_WZToLNuNuNu.addChannel  ("TagPt35MetTrig",  "MuonTagPt35NoJetCutsMetTrig",  "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_muonTagSkim")
muonBkgdEstimate_WZToLNuNuNu.addChannel  ("CandTrkIdPt35",   "CandTrkIdMuPt35",              "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_metMinimalSkim")

print "********************************************************************************"

est = muonBkgdEstimate_WZToLNuNuNu.printNest ()

print "--------------------------------------------------------------------------------"

obs = muonBkgdEstimate_WZToLNuNuNu.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
