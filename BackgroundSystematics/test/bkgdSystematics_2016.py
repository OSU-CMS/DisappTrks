#!/usr/bin/env python

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile
import os

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

# '' will gives you Dataset_2016.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['BC', 'DEFGH', '']

if background == "FAKE" or background == "ALL":

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating fake track systematic (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackSystematic_2016" + runPeriod + ".root", "recreate")

        fakeTrackSystematic = FakeTrackSystematic ()
        fakeTrackSystematic.addTFile (fout)
        fakeTrackSystematic.addTCanvas (canvas)
        fakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        fakeTrackSystematic.addChannel  ("Basic",                       "BasicSelection",                      "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/basicSelection_new")
        fakeTrackSystematic.addChannel  ("DisTrkNHits3",                "DisTrkSelectionSidebandD0CutNHits3",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackSystematic.addChannel  ("DisTrkNHits3NoD0Cut",         "DisTrkSelectionNoD0CutNHits3",        "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackSystematic.addChannel  ("DisTrkNHits4",                "DisTrkSelectionSidebandD0CutNHits4",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackSystematic.addChannel  ("DisTrkNHits5",                "DisTrkSelectionSidebandD0CutNHits5",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackSystematic.addChannel  ("DisTrkNHits6",                "DisTrkSelectionSidebandD0CutNHits6",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackSystematic.addChannel  ("ZtoLL",                       "ZtoMuMu",                             "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu_new")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",         "ZtoMuMuDisTrkSidebandD0CutNHits3",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3NoD0Cut",  "ZtoMuMuDisTrkNoD0CutNHits3",          "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",         "ZtoMuMuDisTrkSidebandD0CutNHits4",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",         "ZtoMuMuDisTrkSidebandD0CutNHits5",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",         "ZtoMuMuDisTrkSidebandD0CutNHits6",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        #fakeTrackSystematic.addD0TransferFactor ()
        fakeTrackSystematic.reweightTo ("MET_2016", dirs['Andrew']+"2016_final_prompt/basicSelection_new", "BasicSelection", "Eventvariable Plots/nTracks")

        print "********************************************************************************"

        fakeTrackSystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

        print "*************************************************************************************"
        print "evaluating fake track systematic in data with sideband D0 cut (2016", runPeriod, ")"
        print "-------------------------------------------------------------------------------------"

        fout = TFile.Open ("sidebandD0CutFakeTrackSystematic" + runPeriod + ".root", "recreate")

        sidebandD0CutFakeTrackSystematic = FakeTrackSystematic ()
        sidebandD0CutFakeTrackSystematic.addTFile (fout)
        sidebandD0CutFakeTrackSystematic.addTCanvas (canvas)
        sidebandD0CutFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        sidebandD0CutFakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",                     "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/totallyNormalBasic_andDisTrkNHits")
        sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionSidebandD0CutNHits3", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/finalFakeTrackSideband_syst")
        sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits3NoD0Cut",  "DisTrkSelectionNoD0CutNHits3",       "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/fakeBkgd_d0sideband")
        sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionSidebandD0CutNHits4", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/finalFakeTrackSideband_syst")
        sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionSidebandD0CutNHits5", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/finalFakeTrackSideband_syst")
        sidebandD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionSidebandD0CutNHits6", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/finalFakeTrackSideband_syst")
        #sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                            "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_nTracksHist")
        sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                            "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu")

        sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkSidebandD0CutNHits3",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/finalFakeTrackSideband")
        sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3NoD0Cut",  "ZtoMuMuDisTrkNoD0CutNHits3",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeSyst_d0sideband")
        sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkSidebandD0CutNHits4",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/finalFakeTrackSideband")
        sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkSidebandD0CutNHits5",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/finalFakeTrackSideband")
        sidebandD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkSidebandD0CutNHits6",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/finalFakeTrackSideband")
        #sidebandD0CutFakeTrackSystematic.addD0TransferFactor ()
        sidebandD0CutFakeTrackSystematic.reweightTo ("MET_2016", dirs['Brian']+"2016_final/totallyNormalBasic_andDisTrkNHits", "BasicSelection", "Eventvariable Plots/nTracks")

        print "********************************************************************************"

        sidebandD0CutFakeTrackSystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

if background == "ELECTRON" or background == "ALL":

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating electron energy systematic (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("electronEnergySystematic_2016" + runPeriod + ".root", "recreate")

        electronEnergySystematic = LeptonEnergySystematic ("electron")
        electronEnergySystematic.addTFile (fout)
        electronEnergySystematic.addTCanvas (canvas)
        electronEnergySystematic.addLuminosityLabel (str (round (lumi["SingleElectron_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        electronEnergySystematic.addPlotLabel ("SingleElectron 2016" + runPeriod)
        electronEnergySystematic.addMetCut (100.0)
        electronEnergySystematic.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_nCtrl_new")
        electronEnergySystematic.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_nCtrl_new")

        print "********************************************************************************"

        electronEnergySystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

if background == "TAU" or background == "ALL":

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating tau energy systematic (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("tauEnergySystematic_2016" + runPeriod + ".root", "recreate")

        tauEnergySystematic = LeptonEnergySystematic ("tau")
        tauEnergySystematic.addTFile (fout)
        tauEnergySystematic.addTCanvas (canvas)
        tauEnergySystematic.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        tauEnergySystematic.addPlotLabel ("Tau 2016" + runPeriod)
        tauEnergySystematic.addMetCut (100.0)
        tauEnergySystematic.addRebinFactor (4)
        tauEnergySystematic.addChannel  ("TagPt35",         "TauTagPt55",                    "Tau_2016"               +  runPeriod,  dirs['Andrew']+"2016_final_prompt/tauBackground_nCtrl_new")
        #tauEnergySystematic.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",             "Tau_2016"               +  runPeriod,  dirs['Andrew']+"2016_final_prompt/tauBackground_nCtrl_new")
        tauEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",               "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_nCtrl_new")
        tauEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",        "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_nCtrl_new")

        print "********************************************************************************"

        tauEnergySystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"
