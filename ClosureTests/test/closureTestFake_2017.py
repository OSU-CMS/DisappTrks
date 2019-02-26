#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I too am Groot.

if len (sys.argv) < 2:
  print "Usage: " + os.path.basename (sys.argv[0]) + " NLAYERS"
  sys.exit (1)
nLayers = "NLayers" + sys.argv[1]
if nLayers == "NLayers6":
  nLayers += "plus"

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

fout = TFile.Open ("muonClosureTest_TTJets_SemiLeptonic.root", "recreate")

print "********************************************************************************"
print "performing fake track background closure test("+nLayers+")"
print "--------------------------------------------------------------------------------"

fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2017"])
fakeTrackBkgdEstimate.addMinD0 (0.05)
fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0Cut3Layers",          "DYJetsToLL_50",  dirs['Andrew']+"2017/fakeTrackClosureTest")
fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkNoD0Cut"+nLayers,  "DYJetsToLL_50",  dirs['Andrew']+"2017/fakeTrackClosureTest")
fakeTrackBkgdEstimate.addChannel  ("Basic",           "BasicSelection",                       "TTJets_SemiLeptonic",  dirs['Andrew']+"2017/basicSelection")
fakeTrackBkgdEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                              "DYJetsToLL_50",  dirs['Andrew']+"2017/zToMuMu")
fakeTrackBkgdEstimate.addChannel  ("DisTrkIdFake",           "DisTrkIdFake"+nLayers,                              "TTJets_SemiLeptonic",  dirs['Andrew']+"2017/disTrkFake")

print "********************************************************************************"

est = fakeTrackBkgdEstimate.printNest ()

print "********************************************************************************"

print "\n\n"

print "--------------------------------------------------------------------------------"

obs = fakeTrackBkgdEstimate.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
