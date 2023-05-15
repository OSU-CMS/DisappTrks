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
print "performing tau closure test with just TTbar (2017)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauClosureTest_TTbar.root", "recreate")

tauBkgdEstimate_TTJets_SemiLeptonic = LeptonBkgdEstimate ("tau")
tauBkgdEstimate_TTJets_SemiLeptonic.addTFile (fout)
tauBkgdEstimate_TTJets_SemiLeptonic.addTCanvas (canvas)
tauBkgdEstimate_TTJets_SemiLeptonic.addLuminosityInInvPb (lumi["MET_2017"])
tauBkgdEstimate_TTJets_SemiLeptonic.addLuminosityLabel (str (round (lumi["MET_2017"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
tauBkgdEstimate_TTJets_SemiLeptonic.addMetCut (120.0)
tauBkgdEstimate_TTJets_SemiLeptonic.addPhiCut (-1.0)
tauBkgdEstimate_TTJets_SemiLeptonic.addECaloCut (10.0)
tauBkgdEstimate_TTJets_SemiLeptonic.addUseHistogramsForPpassMetTriggers (False) # temporary measure
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TagPt35",            "TauTagPt55NoJetCuts",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/" + nLayers + "layers/tau")
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TagPt35MetTrig",     "TauTagPt55NoJetCutsMetTrig", "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/" + nLayers + "layers/tau_metTrig")
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel ("CandTrkIdPt35",      "CandTrkIdTauPt55",               "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest/" + nLayers + "layers/tau")
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel ("CandTrkIdPt35NoMet", "CandTrkIdTauPt55NoMet",          "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest/" + nLayers + "layers/tau_noMet")
if int (nLayers) < 6:
  tauBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TrigEffDenom",            "TauTagPt55NoJetCuts",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/6layers/tau")
  tauBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TrigEffNumer",     "TauTagPt55NoJetCutsMetTrig", "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/6layers/tau_metTrig")
if nLayers == "6":
  nLayers = "6plus"
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbe",       "ZtoTauToEleProbeTrkNLayers"+nLayers,             "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/tauToElectron")
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbePass",   "ZtoTauToEleProbeTrkNLayers"+nLayers,   "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/tauToElectron")
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbe1",       "ZtoTauToMuProbeTrkNLayers"+nLayers,             "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/tauToMuon")
tauBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbePass1",   "ZtoTauToMuProbeTrkNLayers"+nLayers,   "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/tauToMuon")

print "********************************************************************************"

est = tauBkgdEstimate_TTJets_SemiLeptonic.printNest ()

print "--------------------------------------------------------------------------------"

obs = tauBkgdEstimate_TTJets_SemiLeptonic.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
