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
print "performing electron closure test with just DYJetsToLL_50 (2016)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronClosureTest_DYJetsToLL_50.root", "recreate")

electronBkgdEstimate_DYJetsToLL_50 = LeptonBkgdEstimate ("electron")
electronBkgdEstimate_DYJetsToLL_50.addTFile (fout)
electronBkgdEstimate_DYJetsToLL_50.addTCanvas (canvas)
electronBkgdEstimate_DYJetsToLL_50.addPrescaleFactor (lumi["MET_2016"] / lumi["MET_2016DEFGH"])
electronBkgdEstimate_DYJetsToLL_50.addLuminosityInInvPb (lumi["MET_2016"])
electronBkgdEstimate_DYJetsToLL_50.addLuminosityLabel (str (round (lumi["MET_2016"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
electronBkgdEstimate_DYJetsToLL_50.addMetCut (100.0)
electronBkgdEstimate_DYJetsToLL_50.addPhiCut (-1.0)
electronBkgdEstimate_DYJetsToLL_50.addECaloCut (10.0)
electronBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",          "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_DYJetsToLL_50.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoNMissOutCut",        "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_DYJetsToLL_50.addChannel  ("TagPt35",         "ElectronTagPt35NoJetCuts",         "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_DYJetsToLL_50.addChannel  ("TagPt35MetTrig",  "ElectronTagPt35NoJetCutsMetTrig",  "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_DYJetsToLL_50.addChannel  ("CandTrkIdPt35",   "CandTrkIdElecPt35",                "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_metMinimalSkim")

print "********************************************************************************"

est = electronBkgdEstimate_DYJetsToLL_50.printNest ()

print "--------------------------------------------------------------------------------"

obs = electronBkgdEstimate_DYJetsToLL_50.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron closure test with just WZToLNuNuNu (2016)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronClosureTest_WZToLNuNuNu.root", "recreate")

electronBkgdEstimate_WZToLNuNuNu = LeptonBkgdEstimate ("electron")
electronBkgdEstimate_WZToLNuNuNu.addTFile (fout)
electronBkgdEstimate_WZToLNuNuNu.addTCanvas (canvas)
electronBkgdEstimate_WZToLNuNuNu.addPrescaleFactor (lumi["MET_2016"] / lumi["MET_2016DEFGH"])
electronBkgdEstimate_WZToLNuNuNu.addLuminosityInInvPb (lumi["MET_2016"])
electronBkgdEstimate_WZToLNuNuNu.addLuminosityLabel (str (round (lumi["MET_2016"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
electronBkgdEstimate_WZToLNuNuNu.addMetCut (100.0)
electronBkgdEstimate_WZToLNuNuNu.addPhiCut (-1.0)
electronBkgdEstimate_WZToLNuNuNu.addECaloCut (10.0)
electronBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",          "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_WZToLNuNuNu.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoNMissOutCut",        "DYJetsToLL_50_2016MC",  dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_WZToLNuNuNu.addChannel  ("TagPt35",         "ElectronTagPt35NoJetCuts",         "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_WZToLNuNuNu.addChannel  ("TagPt35MetTrig",  "ElectronTagPt35NoJetCutsMetTrig",  "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_electronTagSkim")
electronBkgdEstimate_WZToLNuNuNu.addChannel  ("CandTrkIdPt35",   "CandTrkIdElecPt35",                "WZToLNuNuNu_2016MC",    dirs['Andrew']+"2016_final_prompt/closureTest_metMinimalSkim")

print "********************************************************************************"

est = electronBkgdEstimate_WZToLNuNuNu.printNest ()

print "--------------------------------------------------------------------------------"

obs = electronBkgdEstimate_WZToLNuNuNu.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
