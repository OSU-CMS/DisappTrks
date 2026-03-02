#!/usr/bin/env python3

import math, os, sys
from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate, FakeTrackBkgdEstimate, prettyPrintTotals
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.integrated_luminosity import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

triggerEfficiencyFlat = False
closureTest = False

background = "FAKE"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
#nLayersWords = ['']
combineLayers = True
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]
    combineLayers = False

# '' will gives you Dataset_2018.root for the whole year
#runPeriods = ['A', 'B', 'C', 'D']
#runPeriods = ['']
runPeriods = ['C', 'D']

nEstFake = {}
nEstElectron = {}
nEstMuon = {}
nEstTau = {}

nLeptons = {}
nTotal = {}

# ARC EXO-19-010: use one large sideband for fake estimate
#fakeSidebands = [(x * 0.05, (x + 1) * 0.05) for x in range(1, 10)]
fakeSidebands = [(0.05, 0.5)] 

applyHEMveto = False

stdout = sys.stdout
nullout = open("/dev/null", "w")

for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing fake track background estimate in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("fakeTrackBkgdEstimate_zToMuMu_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")
            txtFile = "fakeTrackBkgdEstimate_zToMuMu_2023" + runPeriod + "_" + nLayersWord + '.txt'
            f = open(txtFile, 'w+')
            f.close()

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addTxtFile(txtFile)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2023" + runPeriod])
            fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoMuMuDisTrkNoD0CutNLayers4",       "Muon_2023" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_2023{runPeriod}_ZtoMuMuDisTrkNoD0Cut/")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoMuMuDisTrkNoD0Cut" + nLayersWord, "Muon_2023" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_2023{runPeriod}_ZtoMuMuDisTrkNoD0Cut/")
            if closureTest:
                fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelectionInvertJetMetPhiCut",                   "MET_2023"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelectionInvertJetMetPhiCut/")
            else:
                fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                   "MET_2023"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelection")
            fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoMuMu",                            "Muon_2023" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_2023{runPeriod}_ZtoMuMu")

            print("********************************************************************************")
            print("Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1]))
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
            fakeTrackBkgdEstimate.addRebinFactor(5)
            nEstFake[(nLayersWord, runPeriod)] = fakeTrackBkgdEstimate.printNest ()[0]
            fout.Close ()

            if len(fakeSidebands) > 1:
                print("********************************************************************************")
                print("Mean result over sidebands: ")
                nEstAllSidebands = Measurement(0, 0)
                pFakeAllSidebands = Measurement(0, 0)
                for sb in fakeSidebands:
                    fakeTrackBkgdEstimate.addMinD0 (sb[0])
                    fakeTrackBkgdEstimate.addMaxD0 (sb[1])
                    sbResults = fakeTrackBkgdEstimate.printNest (verbose = False)
                    nEstAllSidebands += sbResults[0]
                    pFakeAllSidebands += sbResults[1]
                    print('\t({:.2f}, {:.2f}: N_est = '.format(sb[0], sb[1]) + str(sbResults[0]) + ' ; P_fake = ' + str(sbResults[1]))
                nEstAllSidebands /= len(fakeSidebands)
                pFakeAllSidebands /= len(fakeSidebands)
                print("N_est (mean): ", nEstAllSidebands)
                print("P_fake (mean): ", pFakeAllSidebands)
                print("********************************************************************************")
                print("\n\n")

            print("********************************************************************************")
            print("performing fake track background estimate with Z->ee selection in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("fakeTrackBkgdEstimate_zToEE_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")
            txtFile = "fakeTrackBkgdEstimate_zToEE_2023" + runPeriod + "_" + nLayersWord + '.txt'
            f = open(txtFile, 'w+')
            f.close()
            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addTxtFile(txtFile)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2023" + runPeriod])

            # durp
            # only 99.4% of events were run over (failed job in A), so there is an extra prescale factor
            #fakeTrackBkgdEstimate.addPrescaleFactor ((16299633 + 19271182 + 20289301 + 21758154 + 6815966 + 27504879 + 49328605 + 10905430 + 68323666) / 238987094.0)
            fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoEEDisTrkNoD0CutNLayers4",       "EGamma_2023" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoEEDisTrkNoD0Cut" + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/")
            if closureTest:
                fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelectionInvertJetMetPhiCut",                   "MET_2023"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelectionInvertJetMetPhiCut/")
            else:
                fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                   "MET_2023"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelection")
            fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoEE",                            "EGamma_2023" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/")

            print("********************************************************************************")
            print("Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1]))
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
            fakeTrackBkgdEstimate.addRebinFactor(5)
            fakeTrackBkgdEstimate.printNest ()
            fout.Close ()

            if len(fakeSidebands) > 1:
                print("********************************************************************************")
                print("Mean result over sidebands: ")
                nEstAllSidebands = Measurement(0, 0)
                pFakeAllSidebands = Measurement(0, 0)
                for sb in fakeSidebands:
                    fakeTrackBkgdEstimate.addMinD0 (sb[0])
                    fakeTrackBkgdEstimate.addMaxD0 (sb[1])
                    sbResults = fakeTrackBkgdEstimate.printNest (verbose = True)
                    nEstAllSidebands += sbResults[0]
                    pFakeAllSidebands += sbResults[1]
                    print('\t({:.2f}, {:.2f}: N_est = '.format(sb[0], sb[1]) + str(sbResults[0]) + ' ; P_fake = ' + str(sbResults[1]))
                nEstAllSidebands /= len(fakeSidebands)
                pFakeAllSidebands /= len(fakeSidebands)
                print("N_est: ", nEstAllSidebands)
                print("P_fake: ", pFakeAllSidebands)
                print("********************************************************************************")
                print("\n\n")

    if background == "ELECTRON" or background == "LEPTON" or background == "ALL":

        if combineLayers:

            print("********************************************************************************")
            print("performing electron background estimate in search region(2023", runPeriod, "-- combined layers bins)")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("electronBkgdEstimate_2023" + runPeriod + "_combinedBins.root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addPhiCut(0.5)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(round(lumi["MET_2023" + runPeriod] / lumi["EGamma_2023" + runPeriod], 5))
            print("Prescale factor:", {round(lumi["MET_2023" + runPeriod] / lumi["EGamma_2023" + runPeriod], 4)})
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2023" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["EGamma_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            electronBkgdEstimate.addPlotLabel("EGamma 2023" + runPeriod)

            if triggerEfficiencyFlat:
                electronBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.840, 0.005))
            else:
                electronBkgdEstimate.useFilesForTriggerEfficiency()

            if closureTest:
                electronBkgdEstimate._invertJetMetPhi = True

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[0], "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[0], "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[0], "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[0], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[0], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
        
            for iBin in range(1, len(nLayersWords)):
                electronBkgdEstimate.appendChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[iBin], "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
                electronBkgdEstimate.appendChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[iBin], "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
                electronBkgdEstimate.appendChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[iBin], "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
                electronBkgdEstimate.appendChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[iBin], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
                electronBkgdEstimate.appendChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[iBin], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
                #electronBkgdEstimate.appendChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[iBin], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"EGamma_2023/EGamma_2023{runPeriod}_zToEE/")
                #electronBkgdEstimate.appendChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[iBin], "EGamma_2023" + runPeriod, dirs['Mike'] + f"EGamma_2023/EGamma_2023{runPeriod}_zToEE/")
                #electronBkgdEstimate.appendChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[iBin], "EGamma_2023" + runPeriod, dirs['Mike'] + f"EGamma_2023/EGamma_2023{runPeriod}_zToEE/")
                #electronBkgdEstimate.appendChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[iBin], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"EGamma_2023/EGamma_2023{runPeriod}_zToEE/")
                #electronBkgdEstimate.appendChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[iBin], "EGamma_2023"        + runPeriod, dirs['Mike'] + f"EGamma_2023/EGamma_2023{runPeriod}_zToEE/")
            
            electronBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            electronBkgdEstimate.addRebinFactor(4)


            print("********************************************************************************")

            nEstElectron[("combinedBins", runPeriod)] = electronBkgdEstimate.printNest()
            electronBkgdEstimate.printPpassVetoTagProbe()

            print("********************************************************************************")

            fout.Close()

            print("\n\n")

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing electron background estimate in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("electronBkgdEstimate_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addPhiCut(0.5)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(round(lumi["MET_2023" + runPeriod] / lumi["EGamma_2023" + runPeriod], 5))
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2023" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["EGamma_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            electronBkgdEstimate.addPlotLabel("EGamma 2023" + runPeriod)

            if triggerEfficiencyFlat:
                electronBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.840, 0.005))
            else:
                electronBkgdEstimate.useFilesForTriggerEfficiency()

            if closureTest:
                electronBkgdEstimate._invertJetMetPhi = True

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWord, "EGamma_2023"        + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWord, "EGamma_2023"        + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/")
            
            electronBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            electronBkgdEstimate.addRebinFactor(4)

            print("********************************************************************************")

            nEstElectron[(nLayersWord, runPeriod)] = electronBkgdEstimate.printNest()
            electronBkgdEstimate.printPpassVetoTagProbe()

            print("********************************************************************************")

            fout.Close()

            print("\n\n")

    if background == "MUON" or background == "LEPTON" or background == "ALL":

        if combineLayers:

            print("********************************************************************************")
            print("performing muon background estimate in search region(2023", runPeriod, "-- combined layer bins)")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("muonBkgdEstimate_2023" + runPeriod + "_combinedBins.root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(round(lumi["MET_2023" + runPeriod] / lumi["Muon_2023" + runPeriod], 5))
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2023" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["Muon_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            muonBkgdEstimate.addPlotLabel("Muon 2023" + runPeriod)

            if triggerEfficiencyFlat:
                muonBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.940, 0.004))
            else:
                muonBkgdEstimate.useFilesForTriggerEfficiency()

            if closureTest:
                muonBkgdEstimate._invertJetMetPhi = True

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[0], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[0], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[0], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[0], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[0], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")


            for iBin in range(1, len(nLayersWords)):
                muonBkgdEstimate.appendChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[iBin], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                muonBkgdEstimate.appendChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[iBin], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                muonBkgdEstimate.appendChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[iBin], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                muonBkgdEstimate.appendChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[iBin], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                muonBkgdEstimate.appendChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[iBin], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")

            muonBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            muonBkgdEstimate.addRebinFactor(4)

            print("********************************************************************************")

            nEstMuon[("combinedBins", runPeriod)] = muonBkgdEstimate.printNest()
            muonBkgdEstimate.printPpassVetoTagProbe()

            combinedPpassMetCut = muonBkgdEstimate.getPpassMetCut()
            combinedPpassMetTriggers, combinedTriggerEfficiency = muonBkgdEstimate.getPpassMetTriggers()

            combinedPpassHEMveto = None
            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                combinedPpassHEMveto = muonBkgdEstimate.getPpassHEMveto()

            print("********************************************************************************")

            fout.Close()

            print("\n\n")

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing muon background estimate in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("muonBkgdEstimate_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(round(lumi["MET_2023" + runPeriod] / lumi["Muon_2023" + runPeriod], 5))
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2023" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["Muon_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            muonBkgdEstimate.addPlotLabel("Muon_2023 2023" + runPeriod)

            if triggerEfficiencyFlat:
                muonBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.940, 0.004))
            else:
                muonBkgdEstimate.useFilesForTriggerEfficiency()

            if closureTest:
                muonBkgdEstimate._invertJetMetPhi = True

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWord, "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWord, "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWord, "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWord, "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWord, "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")

            muonBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            muonBkgdEstimate.addRebinFactor(4)

            print("********************************************************************************")

            nEstMuon[(nLayersWord, runPeriod)] = muonBkgdEstimate.printNest()
            muonBkgdEstimate.printPpassVetoTagProbe()

            print("********************************************************************************")

            if nLayersWord == "NLayers4" or nLayersWord == "NLayers5":
                print("using the combined 4/5/6+ layers sample for Poffline and Ptrigger:")
                nEstMuon[(nLayersWord, runPeriod)] = muonBkgdEstimate.printNestCombinedMet(combinedPpassMetCut, combinedPpassMetTriggers, combinedPpassHEMveto)

            print("********************************************************************************")

            fout.Close()

            print("\n\n")

    if background == "TAU" or background == "LEPTON" or background == "ALL":

        if combineLayers:

            print("********************************************************************************")
            print("performing tau background estimate in search region(2023", runPeriod, "-- combined layer bins)")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("tauBkgdEstimate_2023" + runPeriod + "_combinedBins.root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(round(lumi["MET_2023" + runPeriod] / lumi["Tau_2023" + runPeriod], 5))
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2023" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["Tau_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2023" + runPeriod)
            #prescale for IsoMu20 trigger used to calculate tau trigger probability
            tauBkgdEstimate.setTriggerSFPrescale(210)

            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWords[0], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWords[0], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWords[0], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWords[0], "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayers")
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWords[0], "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayersFilter")
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWords[0], "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayersFilter")
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWords[0], "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWords[0], "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWords[0], "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWords[0], "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWords[0], "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
            tauBkgdEstimate.addChannel("IsoMuTrig",        "TauTagSkimSingleMuonTriggerSelection2", "Muon_2023"          + runPeriod, dirs['Mike'] + f"santosAbyss/SingleTauTriggerEstimate_2023{runPeriod}")
            tauBkgdEstimate.addChannel("MuonTauTrig",      "TauTagSkimMuonTauTriggerSelection", "Muon_2023"          + runPeriod, dirs['Mike'] + f"santosAbyss/SingleTauTriggerEstimate_2023{runPeriod}")
            
            if triggerEfficiencyFlat:
                tauBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.900, 0.006))
            else:
                tauBkgdEstimate.useFilesForTriggerEfficiency()

            if closureTest:
                tauBkgdEstimate._invertJetMetPhi = True

            for iBin in range(1, len(nLayersWords)):
                tauBkgdEstimate.appendChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWords[iBin], "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                tauBkgdEstimate.appendChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWords[iBin], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                tauBkgdEstimate.appendChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWords[iBin], "Muon_2023" + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
                tauBkgdEstimate.appendChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWords[iBin], "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayers")
                tauBkgdEstimate.appendChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWords[iBin], "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayersFilter")
                tauBkgdEstimate.appendChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWords[iBin], "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayersFilter")
                tauBkgdEstimate.appendChannel("TagPt35",          "TauTagPt55"                      + nLayersWords[iBin], "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
                tauBkgdEstimate.appendChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWords[iBin], "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
                tauBkgdEstimate.appendChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWords[iBin], "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers")
                tauBkgdEstimate.appendChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWords[iBin], "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers")
                tauBkgdEstimate.appendChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWords[iBin], "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
 
            tauBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            tauBkgdEstimate.addRebinFactor(8)

            print("********************************************************************************")

            nEstTau[("combinedBins", runPeriod)] = tauBkgdEstimate.printNest()
            tauBkgdEstimate.printPpassVetoTagProbe()

            combinedPpassMetCut = tauBkgdEstimate.getPpassMetCut()
            combinedPpassMetTriggers, combinedTriggerEfficiency = tauBkgdEstimate.getPpassMetTriggers()
            tauTriggerSF = tauBkgdEstimate.printTriggerSF()


            print("********************************************************************************")
            
            fout.Close()

            print("\n\n")

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing tau background estimate in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("tauBkgdEstimate_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(round(lumi["MET_2023" + runPeriod] / lumi["Tau_2023" + runPeriod]))
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2023" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["Tau_2023" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13.6 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2023" + runPeriod)
            combinedPpassHEMveto = None
            tauBkgdEstimate._triggerSF = tauTriggerSF

            if triggerEfficiencyFlat:
                tauBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.900, 0.006))
            else:
                tauBkgdEstimate.useFilesForTriggerEfficiency()

            if closureTest:
                tauBkgdEstimate._invertJetMetPhi = True

            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWord, "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWord, "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWord, "Muon_2023"        + runPeriod, dirs['Matt'] + f"merged_data/Muon_2023{runPeriod}/")
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWord, "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayers")
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWord, "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayersFilter")
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWord, "EGamma_2023"   + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_ZtoTauToEleProbeTrkNLayersFilter")
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWord, "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWord, "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWord, "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWord, "EGamma_2023"          + runPeriod, dirs['Mike'] + f"abyss/EGamma_run3/EGamma_2023{runPeriod}_TagPT55NLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWord, "Tau_2023"             + runPeriod, dirs['Mike'] + f"abyss/Tau_run3/Tau_2023{runPeriod}_TauTagPt55")

            tauBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            tauBkgdEstimate.addRebinFactor(8)

            print("********************************************************************************")

            nEstTau[(nLayersWord, runPeriod)] = tauBkgdEstimate.printNest()
            tauBkgdEstimate.printPpassVetoTagProbe()

            print("********************************************************************************")

            if nLayersWord == "NLayers4" or nLayersWord == "NLayers5":
                print("using the combined 4/5/6+ layers sample for Poffline and Ptrigger:")
                nEstTau[(nLayersWord, runPeriod)] = tauBkgdEstimate.printNestCombinedMet(combinedPpassMetCut, combinedPpassMetTriggers, combinedPpassHEMveto)

            print("********************************************************************************")

            fout.Close()

            print("\n\n")

sys.stdout = stdout

# print sums
if background == "ALL":
    prettyPrintTotals(nEstElectron, nEstMuon, nEstTau, nEstFake, nLayersWords, runPeriods, '2018')
    fout = TFile.Open("backgroundCrossSections_2018.root", "recreate")
    for nLayersWord in nLayersWords:
        x = array("d"); ex = array("d")
        electron   =  array ("d");  muon   =  array ("d");  tau   =  array ("d");  fake   =  array ("d")
        eElectron  =  array ("d");  eMuon  =  array ("d");  eTau  =  array ("d");  eFake  =  array ("d")

        runPeriodsToPlot = ['AB', 'CD']
        i = 0.0

        for runPeriod in runPeriodsToPlot:
            x.append(i)
            ex.append(0.0)
            i += 1.0

            electron.append(nEstElectron[(nLayersWord, runPeriod)].centralValue() / lumi["MET_2018" + runPeriod])
            muon.append    (nEstMuon    [(nLayersWord, runPeriod)].centralValue() / lumi["MET_2018" + runPeriod])
            tau.append     (nEstTau     [(nLayersWord, runPeriod)].centralValue() / lumi["MET_2018" + runPeriod])
            fake.append    (nEstFake    [(nLayersWord, runPeriod)].centralValue() / lumi["MET_2018" + runPeriod])

            eElectron.append(nEstElectron[(nLayersWord, runPeriod)].maxUncertainty() / lumi["MET_2018" + runPeriod])
            eMuon.append    (nEstMuon    [(nLayersWord, runPeriod)].maxUncertainty() / lumi["MET_2018" + runPeriod])
            eTau.append     (nEstTau     [(nLayersWord, runPeriod)].maxUncertainty() / lumi["MET_2018" + runPeriod])
            eFake.append    (nEstFake    [(nLayersWord, runPeriod)].maxUncertainty() / lumi["MET_2018" + runPeriod])

        gElectron = TGraphErrors(len(x), x, electron, ex, eElectron)
        gMuon     = TGraphErrors(len(x), x, muon,     ex, eMuon)
        gTau      = TGraphErrors(len(x), x, tau,      ex, eTau)
        gFake     = TGraphErrors(len(x), x, fake,     ex, eFake)

        fout.mkdir(nLayersWord)
        fout.cd(nLayersWord)

        gElectron.Write("electron")
        gMuon.Write("muon")
        gTau.Write("tau")
        gFake.Write("fake")

        fout.cd()

    fout.Close()
