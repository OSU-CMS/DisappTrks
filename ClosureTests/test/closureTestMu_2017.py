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
print "performing muon closure test with just TTJets_SemiLeptonic (2017)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonClosureTest_TTJets_SemiLeptonic.root", "recreate")

muonBkgdEstimate_TTJets_SemiLeptonic = LeptonBkgdEstimate ("muon")
muonBkgdEstimate_TTJets_SemiLeptonic.addTFile (fout)
muonBkgdEstimate_TTJets_SemiLeptonic.addTCanvas (canvas)
muonBkgdEstimate_TTJets_SemiLeptonic.addLuminosityInInvPb (lumi["MET_2017"])
muonBkgdEstimate_TTJets_SemiLeptonic.addLuminosityLabel (str (round (lumi["MET_2017"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
muonBkgdEstimate_TTJets_SemiLeptonic.addMetCut (120.0)
muonBkgdEstimate_TTJets_SemiLeptonic.addPhiCut (-1.0)
muonBkgdEstimate_TTJets_SemiLeptonic.addECaloCut (10.0)
muonBkgdEstimate_TTJets_SemiLeptonic.addUseHistogramsForPpassMetTriggers (False) # temporary measure
muonBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TagPt35",            "MuonTagPt35NoJetCuts",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/" + nLayers + "layers/muon")
muonBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TagPt35MetTrig",     "MuonTagPt35NoJetCutsMetTrig", "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/" + nLayers + "layers/muon_metTrig")
muonBkgdEstimate_TTJets_SemiLeptonic.addChannel ("CandTrkIdPt35",      "CandTrkIdMuPt35",             "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest/" + nLayers + "layers/muon")
muonBkgdEstimate_TTJets_SemiLeptonic.addChannel ("CandTrkIdPt35NoMet", "CandTrkIdMuPt35NoMet",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest/" + nLayers + "layers/muon_noMet")
if int (nLayers) < 6:
  muonBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TrigEffDenom",            "MuonTagPt35NoJetCuts",        "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/6layers/muon")
  muonBkgdEstimate_TTJets_SemiLeptonic.addChannel ("TrigEffNumer",     "MuonTagPt35NoJetCutsMetTrig", "TTJets_SemiLeptonic", dirs['Andrew']+"2017/closureTest_background/6layers/muon_metTrig")
if nLayers == "6":
  nLayers = "6plus"
muonBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbe",       "ZtoMuProbeTrkNLayers"+nLayers,             "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/muon")
muonBkgdEstimate_TTJets_SemiLeptonic.addChannel   ("TagProbePass",   "ZtoMuProbeTrkNLayers"+nLayers,   "DYJetsToLL_50", dirs['Andrew']+"2017/closureTest_tagAndProbe/muon")

print "********************************************************************************"

est = muonBkgdEstimate_TTJets_SemiLeptonic.printNest ()

print "--------------------------------------------------------------------------------"

obs = muonBkgdEstimate_TTJets_SemiLeptonic.printNback ()

print ""

diff = est - obs

print "N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma"

print "********************************************************************************"

fout.Close ()
