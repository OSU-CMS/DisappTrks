#!/usr/bin/env python3

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I too am Groot.

if len (sys.argv) < 2:
  print("Usage: " + os.path.basename (sys.argv[0]) + " NLAYERS")
  sys.exit (1)
nLayers = sys.argv[1]

fout = TFile.Open ("electronClosureTest_TTbar.root", "recreate")
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

electronBkgdEstimate_TTJets_SemiLeptonic2023 = LeptonBkgdEstimate ("electron")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addTFile (fout)
electronBkgdEstimate_TTJets_SemiLeptonic2023.addTCanvas (canvas)
# electronBkgdEstimate_TTJets_SemiLeptonic2023.addLuminosityInInvPb (lumi["MET_2023C"])
# electronBkgdEstimate_TTJets_SemiLeptonic2023.addLuminosityLabel (str (round (lumi["MET_2023C"] / 1000.0, 2)) + " fb^{-1} (13.6 TeV)")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addMetCut (120.0)
electronBkgdEstimate_TTJets_SemiLeptonic2023.addPhiCut (-1.0)
electronBkgdEstimate_TTJets_SemiLeptonic2023.addECaloCut (10.0)

electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel ("TagPt35", "ElectronTagPt35NoJetCutsNLayers"+nLayers, "ElectronTagPt35NoJetCuts_2024SIM_vTTBar_TTSemileptonic", "ElectronBackgrounds2024/SIM")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel ("TagPt35MetTrig", "ElectronTagPt35NoJetCutsMetTrigNLayers"+nLayers, "ElectronTagPt35NoJetCutsMetTrig_2024SIM_vTTBar_TTSemileptonic", "ElectronBackgrounds2024/SIM")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel ("CandTrkIdPt35", "CandTrkIdElecPt35NLayers"+nLayers, "CandTrkIdElecPt35_2024SIM_vTTBar_TTSemileptonic", "ElectronBackgrounds2024/SIM")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel ("TrigEffDenom", "ElectronTagPt35NoJetCutsNLayers6plus", "ElectronTagPt35NoJetCuts_2024SIM_vTTBar_TTSemileptonic", "ElectronBackgrounds2024/SIM")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel ("TrigEffNumer", "ElectronTagPt35NoJetCutsMetTrigNLayers6plus", "ElectronTagPt35NoJetCutsMetTrig_2024SIM_vTTBar_TTSemileptonic", "ElectronBackgrounds2024/SIM")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel   ("TagProbe", "ZtoEleProbeTrkNLayers"+nLayers, "ZtoEleProbeTrk_2024SIM_vEGamma_DYgt50", "ElectronBackgrounds2024/SIM")
electronBkgdEstimate_TTJets_SemiLeptonic2023.addChannel   ("TagProbePass", "ZtoEleProbeTrkNLayers"+nLayers, "ZtoEleProbeTrk_2024SIM_vEGamma_DYgt50", "ElectronBackgrounds2024/SIM")

est = electronBkgdEstimate_TTJets_SemiLeptonic2023.printNest ()
obs = electronBkgdEstimate_TTJets_SemiLeptonic2023.printNback ()
diff = est - obs
fout.Close ()

print("N_est - N_obs: " + str (diff.centralValue () / diff.maxUncertainty ()) + " sigma")

