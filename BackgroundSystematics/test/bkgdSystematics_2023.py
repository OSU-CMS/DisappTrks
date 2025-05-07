#!/usr/bin/env python3

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile
import os

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "TAU"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]

# '' will gives you Dataset_2017.root for the whole year
runPeriods = ['C', 'D']

if background == "FAKE" or background == "ALL":

    for runPeriod in runPeriods:

        print("********************************************************************************")
        print("evaluating fake track systematic(2022", runPeriod, ")")
        print("--------------------------------------------------------------------------------")

        fout = TFile.Open("fakeTrackSystematic_2022" + runPeriod + ".root", "recreate")

        fakeTrackSystematic = FakeTrackSystematic()
        fakeTrackSystematic.addTFile(fout)
        fakeTrackSystematic.addTCanvas(canvas)
        fakeTrackSystematic.addLuminosityLabel(str(round(lumi["MET_2022" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
        fakeTrackSystematic.addChannel ("Basic",                       "BasicSelection",                      "MET_2022"       +  runPeriod,  dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_basicSelection")
        fakeTrackSystematic.addChannel ("DisTrkNHits3",                "DisTrkSelectionSidebandD0CutNHits3",  "MET_2022"       +  runPeriod,  dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("DisTrkNHits3NoD0Cut",         "DisTrkSelectionNoD0CutNHits3",        "MET_2022"       +  runPeriod,  dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("DisTrkNHits4",                "DisTrkSelectionSidebandD0CutNHits4",  "MET_2022"       +  runPeriod,  dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("DisTrkNHits5",                "DisTrkSelectionSidebandD0CutNHits5",  "MET_2022"       +  runPeriod,  dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("DisTrkNHits6",                "DisTrkSelectionSidebandD0CutNHits6",  "MET_2022"       +  runPeriod,  dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("ZtoLL",                       "ZtoMuMu",                             "Muon_2022"  +  runPeriod,  dirs['Mike'] + f"abyss/Muon_run3/Muon_2022{runPeriod}_ZtoMuMu")
        fakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits3",         "DisTrkSelectionSidebandD0CutNHits3",    "Muon_2022"  +  runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits3NoD0Cut",  "DisTrkSelectionNoD0CutNHits3",          "Muon_2022"  +  runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits4",         "DisTrkSelectionSidebandD0CutNHits4",    "Muon_2022"  +  runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits5",         "DisTrkSelectionSidebandD0CutNHits5",    "Muon_2022"  +  runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        fakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits6",         "DisTrkSelectionSidebandD0CutNHits6",    "Muon_2022"  +  runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        #fakeTrackSystematic.addD0TransferFactor()
        fakeTrackSystematic.reweightTo("MET_2022"+runPeriod, dirs['Mike']+f"abyss/MET_run3/MET_2022{runPeriod}_basicSelection", "BasicSelection", "Eventvariable Plots/nTracks")

        print("********************************************************************************")

        fakeTrackSystematic.printSystematic()

        print("********************************************************************************")

        fout.Close()

        print("\n\n")

        print("*************************************************************************************")
        print("evaluating fake track systematic in data with sideband D0 cut(2022", runPeriod, ")")
        print("-------------------------------------------------------------------------------------")

        fout = TFile.Open("sidebandD0CutFakeTrackSystematic" + runPeriod + ".root", "recreate")

        sidebandD0CutFakeTrackSystematic = FakeTrackSystematic()
        sidebandD0CutFakeTrackSystematic.addTFile(fout)
        sidebandD0CutFakeTrackSystematic.addTCanvas(canvas)
        sidebandD0CutFakeTrackSystematic.addLuminosityLabel(str(round(lumi["MET_2022" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
        sidebandD0CutFakeTrackSystematic.addChannel ("Basic",                "BasicSelection",                     "MET_2022" + runPeriod,       dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_basicSelection")
        sidebandD0CutFakeTrackSystematic.addChannel ("DisTrkNHits3",         "DisTrkSelectionSidebandD0CutNHits3", "MET_2022" + runPeriod,       dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("DisTrkNHits3NoD0Cut",  "DisTrkSelectionNoD0CutNHits3",       "MET_2022" + runPeriod,       dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("DisTrkNHits4",         "DisTrkSelectionSidebandD0CutNHits4", "MET_2022" + runPeriod,       dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("DisTrkNHits5",         "DisTrkSelectionSidebandD0CutNHits5", "MET_2022" + runPeriod,       dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("DisTrkNHits6",         "DisTrkSelectionSidebandD0CutNHits6", "MET_2022" + runPeriod,       dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("ZtoLL",                "ZtoMuMu",                            "Muon_2022" + runPeriod,  dirs['Mike'] + f"abyss/Muon_run3/Muon_2022{runPeriod}_ZtoMuMu")
        sidebandD0CutFakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits3",  "DisTrkSelectionSidebandD0CutNHits3",   "Muon_2022" + runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits3NoD0Cut",  "DisTrkSelectionNoD0CutNHits3",   "Muon_2022" + runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits4",  "DisTrkSelectionSidebandD0CutNHits4",   "Muon_2022" + runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits5",  "DisTrkSelectionSidebandD0CutNHits5",   "Muon_2022" + runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        sidebandD0CutFakeTrackSystematic.addChannel ("ZtoMuMuDisTrkNHits6",  "DisTrkSelectionSidebandD0CutNHits6",   "Muon_2022" + runPeriod,  dirs['Mike']+f"abyss/Muon_run3/Muon_2022{runPeriod}_DisTrkSelectionNoD0Cut")
        #sidebandD0CutFakeTrackSystematic.addD0TransferFactor()
        sidebandD0CutFakeTrackSystematic.reweightTo("MET_2022"+runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2022{runPeriod}_basicSelection", "BasicSelection", "Eventvariable Plots/nTracks")

        print("********************************************************************************")

        sidebandD0CutFakeTrackSystematic.printSystematic()

        print("********************************************************************************")

        fout.Close()

        print("\n\n")

if background == "ELECTRON" or background == "ALL":

    for runPeriod in runPeriods:

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("evaluating electron energy systematic (2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("electronEnergySystematic_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            electronEnergySystematic = LeptonEnergySystematic("electron")
            electronEnergySystematic.addTFile(fout)
            electronEnergySystematic.addTCanvas(canvas)
            electronEnergySystematic.addLuminosityLabel(str(round(lumi["EGamma_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            electronEnergySystematic.addPlotLabel("EGamma 2023" + runPeriod)
            electronEnergySystematic.addMetCut(120.0)

            electronEnergySystematic.addChannel("TagPt35",        "ElectronTagPt55"        + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers/")
            electronEnergySystematic.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig" + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers/")

            print("********************************************************************************")
            electronEnergySystematic.printSystematic()
            print("********************************************************************************")

            fout.Close()
            print("\n\n")

if background == "TAU" or background == "ALL":

    for runPeriod in runPeriods:

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("evaluating tau energy systematic(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("tauEnergySystematic_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            tauEnergySystematic = LeptonEnergySystematic("tau")
            tauEnergySystematic.addTFile(fout)
            tauEnergySystematic.addTCanvas(canvas)
            tauEnergySystematic.addLuminosityLabel(str(round(lumi["Tau_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            tauEnergySystematic.addPlotLabel("Tau 2023" + runPeriod)
            tauEnergySystematic.addMetCut(120.0)
            tauEnergySystematic.addRebinFactor(4)

            tauEnergySystematic.addChannel("TagPt35",        "TauTagPt55"             + nLayersWord, "Tau_2023"    + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55/")
            #tauEnergySystematic.addChannel("TagPt35MetTrig", "TauTagPt55MetTrig"      + nLayersWord, "Tau_2023"    + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55/")
            tauEnergySystematic.addChannel("TrigEffDenom",   "ElectronTagPt55"        + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers/")
            tauEnergySystematic.addChannel("TrigEffNumer",   "ElectronTagPt55MetTrig" + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers/")

            print("********************************************************************************")
            tauEnergySystematic.printSystematic()
            print("********************************************************************************")

            fout.Close()
            print("\n\n")
