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
runPeriods = ['BC', 'DEFG', 'DEFGH', 'H', '']

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
        fakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",         "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/basicSelection")
        fakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic")
        fakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic")
        fakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic")
        fakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic")
        fakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground")

        print "********************************************************************************"

        fakeTrackSystematic.printSystematic ()

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
        electronEnergySystematic.addChannel  ("TagPt35",         "ElectronTagPt55",         "SingleEle_2016"  +  runPeriod,  dirs['Andrew']+"2016/electronBackground")
        #electronEnergySystematic.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",  "SingleEle_2016"  +  runPeriod,  dirs['Andrew']+"2016/electronBackground")
        electronEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",         "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")
        electronEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",  "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")

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
        tauEnergySystematic.addChannel  ("TagPt35",         "TauTagPt55",              "Tau_2016"        +  runPeriod,  dirs['Andrew']+"2016/tauBackground")
        #tauEnergySystematic.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",       "Tau_2016H",                     dirs['Andrew']+"2016/tauBackground")
        tauEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",         "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")
        tauEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",  "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")

        print "********************************************************************************"

        tauEnergySystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"
