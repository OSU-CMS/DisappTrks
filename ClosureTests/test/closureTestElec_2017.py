#!/usr/bin/env python3

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I too am Groot.

if len (sys.argv) < 2:
  print "Usage: " + os.path.basename (sys.argv[0]) + " NLAYERS"
  sys.exit (1)
nLayers = sys.argv[1]

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing electron closure test with just TTbar (2017)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronClosureTest_TTbar.root", "recreate")

electronBkgdEstimate_TTJets_SemiLeptonic = LeptonBkgdEstimate ("electron")
electronBkgdEstimate_TTJets_SemiLeptonic.addTFile (fout)
electronBkgdEstimate_TTJets_SemiLeptonic.addTCanvas (canvas)
electronBkgdEstimate_TTJets_SemiLeptonic.addLuminosityInInvPb (lumi["MET_2017"])
electronBkgdEstimate_TTJets_SemiLeptonic.addLuminosityLabel (str (round (lumi["MET_2017"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
electronBkgdEstimate_TTJets_SemiLeptonic.addMetCut (120.0)
electronBkgdEstimate_TTJets_SemiLeptonic.addPhiCut (-1.0)
electronBkgdEstimate_TTJets_SemiLeptonic.addECaloCut (10.0)
electronBkgdEstimate_TTJets_SemiLeptonic.addUseHistogramsForPpassMetTriggers (False) # temporary measure
electronBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TagPt35",            "ElectronTagPt35NoJetCuts",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/" + nLayers + "layers/electron")
electronBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TagPt35MetTrig",     "ElectronTagPt35NoJetCutsMetTrig", "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/" + nLayers + "layers/electron_metTrig")
electronBkgdEstimate_TTJets_SemiLeptonic.addChannel ("CandTrkIdPt35",      "CandTrkIdElecPt35",               "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest/" + nLayers + "layers/electron")
electronBkgdEstimate_TTJets_SemiLeptonic.addChannel ("CandTrkIdPt35NoMet", "CandTrkIdElecPt35NoMet",          "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest/" + nLayers + "layers/electron_noMet")
if int (nLayers) < 6:
  electronBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TrigEffDenom",            "ElectronTagPt35NoJetCuts",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/6layers/electron")
  electronBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TrigEffNumer",     "ElectronTagPt35NoJetCutsMetTrig", "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/6layers/electron_metTrig")
if nLayers == "6":
  nLayers = "6plus"
electronBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbe",       "ZtoEleProbeTrkNLayers"+nLayers,             "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/electron")
electronBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbePass",   "ZtoEleProbeTrkNLayers"+nLayers,   "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/electron")

print "********************************************************************************"

est = electronBkgdEstimate_TTJets_SemiLeptonic.printNest ()

print "--------------------------------------------------------------------------------"

obs = electronBkgdEstimate_TTJets_SemiLeptonic.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
