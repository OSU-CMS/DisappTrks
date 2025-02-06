#!/usr/bin/env python3

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I too am Groot.
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")

if len (sys.argv) < 2:
  print ("Usage: " + os.path.basename (sys.argv[0]) + " NLAYERS")
  sys.exit (1)
nLayers = "NLayers" + sys.argv[1]
if nLayers == "NLayers6":
  nLayers += "plus"

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print ("********************************************************************************")
print ("performing fake track background closure test("+nLayers+")")
print ("--------------------------------------------------------------------------------")

fout = TFile.Open("fakeClosureTest_" + nLayers + ".root", "recreate")

fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate.addTFile (fout)
fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2022CD"])
fakeTrackBkgdEstimate.addMinD0 (0.05)

fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0CutNLayers4",          "merged_preEE",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/preEE")
fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkNoD0Cut"+nLayers,          "merged_preEE",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/preEE")
fakeTrackBkgdEstimate.addChannel  ("Basic",           "BasicSelection",                        "merged_preEE",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/preEE")
fakeTrackBkgdEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                               "merged_preEE",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/preEE")
fakeTrackBkgdEstimate.addChannel  ("DisTrkIdFake",    "DisTrkIdFake"+nLayers,                  "merged_preEE",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/preEE")

fakeTrackBkgdEstimateEE = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimateEE.addTFile (fout)
fakeTrackBkgdEstimateEE.addLuminosityInInvPb (lumi["MET_2022EFG"])
fakeTrackBkgdEstimateEE.addMinD0 (0.05)

fakeTrackBkgdEstimateEE.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0CutNLayers4",          "merged_postEEFake4",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/postEEFake4")
fakeTrackBkgdEstimateEE.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkNoD0Cut"+nLayers,          "merged_postEEFake4",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/postEEFake4")
fakeTrackBkgdEstimateEE.addChannel  ("Basic",           "BasicSelection",                        "merged_postEEFake4",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/postEEFake4")
fakeTrackBkgdEstimateEE.addChannel  ("ZtoLL",           "ZtoMuMu",                               "merged_postEEFake4",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/postEEFake4")
fakeTrackBkgdEstimateEE.addChannel  ("DisTrkIdFake",    "DisTrkIdFake"+nLayers,                  "merged_postEEFake4",  dirs['Breno']+"BGMC/Run3/2022/closure_test/fakeTracks/postEEFake4")

print( "********************************************************************************")

est2022EE = fakeTrackBkgdEstimateEE.printNest()
est2022 = fakeTrackBkgdEstimate.printNest()
fout.Close ()

print( "--------------------------------------------------------------------------------")

obs2022EE = fakeTrackBkgdEstimateEE.printNback()
obs2022 = fakeTrackBkgdEstimate.printNback()

print( "")

# Uncomment one of the following pairs to calculate est and obs for 2022, 2022EE or 2022+2022EE

# est = est2022[0]
# obs = obs2022

# est = est2022EE[0]
# obs = obs2022EE

est = est2022[0] + est2022EE[0]
obs = obs2022 + obs2022EE

print("N_est: ",est)
print("N_back: ",obs)

diff = est - obs

print( "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma")

print( "********************************************************************************")