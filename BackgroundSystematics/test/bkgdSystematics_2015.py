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

if background == "FAKE" or background == "ALL":

    print "********************************************************************************"
    print "evaluating fake track systematic (2015)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackSystematic_2015D.root", "recreate")

    fakeTrackSystematic = FakeTrackSystematic ()
    fakeTrackSystematic.addTFile (fout)
    fakeTrackSystematic.addTCanvas (canvas)
    fakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2015D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    fakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",         "MET_2015D",       dirs['Brian']+"2015/basicSelection")
    fakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2015D",  dirs['Brian']+"2015/zToMuMu")
    fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")
    fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")
    fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")
    fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")

    print "********************************************************************************"

    fakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with reweighting (2015)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackSystematicWithReweighting_2015D" + ".root", "recreate")

    fakeTrackSystematicWithReweighting = FakeTrackSystematic ()
    fakeTrackSystematicWithReweighting.addTFile (fout)
    fakeTrackSystematicWithReweighting.addTCanvas (canvas)
    fakeTrackSystematicWithReweighting.addLuminosityLabel (str (round (lumi["MET_2015D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    fakeTrackSystematicWithReweighting.addChannel  ("Basic",                "BasicSelection",         "MET_2015D",       dirs['Brian']+"2015/basicSelection")
    fakeTrackSystematicWithReweighting.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematicWithReweighting.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematicWithReweighting.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematicWithReweighting.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2015D",       dirs['Brian']+"2015/fakeTrackSystematic")
    fakeTrackSystematicWithReweighting.reweightTo  ("MET_2015D",                                                         dirs['Brian']+"2015/basicSelection",  "BasicSelection",  "Eventvariable Plots/nTracks")
    fakeTrackSystematicWithReweighting.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2015D",  dirs['Brian']+"2015/zToMuMu")
    fakeTrackSystematicWithReweighting.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")
    fakeTrackSystematicWithReweighting.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")
    fakeTrackSystematicWithReweighting.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")
    fakeTrackSystematicWithReweighting.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackBackground")

    print "********************************************************************************"

    fakeTrackSystematicWithReweighting.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "ELECTRON" or background == "ALL":

    print "********************************************************************************"
    print "evaluating electron energy systematic (2015)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("electronEnergySystematic_2015D" + ".root", "recreate")

    electronEnergySystematic = LeptonEnergySystematic ("electron")
    electronEnergySystematic.addTFile (fout)
    electronEnergySystematic.addTCanvas (canvas)
    electronEnergySystematic.addLuminosityLabel (str (round (lumi["SingleElectron_2015D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronEnergySystematic.addPlotLabel ("SingleElectron 2015D")
    electronEnergySystematic.addMetCut (100.0)
    electronEnergySystematic.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")
    electronEnergySystematic.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")

    print "********************************************************************************"

    electronEnergySystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "TAU" or background == "ALL":

    print "********************************************************************************"
    print "evaluating tau energy systematic (2015)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("tauEnergySystematic_2015D" + ".root", "recreate")

    tauEnergySystematic = LeptonEnergySystematic ("tau")
    tauEnergySystematic.addTFile (fout)
    tauEnergySystematic.addTCanvas (canvas)
    tauEnergySystematic.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    tauEnergySystematic.addPlotLabel ("Tau 2015D")
    tauEnergySystematic.addMetCut (100.0)
    tauEnergySystematic.addRebinFactor (4)
    tauEnergySystematic.addChannel  ("TagPt35",         "TauTagPt55",                    "Tau_2015D",               dirs['Andrew']+"2015/tauBackground_nCtrl_new")
    #tauEnergySystematic.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",             "Tau_2015D",               dirs['Andrew']+"2015/tauBackground_nCtrl_new")
    tauEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",               "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")
    tauEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",        "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")

    print "********************************************************************************"

    tauEnergySystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"
