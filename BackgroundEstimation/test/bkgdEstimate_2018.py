#!/usr/bin/env python3

import math, os, sys
from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate, FakeTrackBkgdEstimate, prettyPrintTotals
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "ELECTRON"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
combineLayers = True
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]
    combineLayers = False

# '' will gives you Dataset_2018.root for the whole year
#runPeriods = ['A', 'B', 'C', 'D']
#runPeriods = ['']
runPeriods = ['AB', 'CD']

nEstFake = {}
nEstElectron = {}
nEstMuon = {}
nEstTau = {}

nLeptons = {}
nTotal = {}

# ARC EXO-19-010: use one large sideband for fake estimate
#fakeSidebands = [(x * 0.05, (x + 1) * 0.05) for x in range(1, 10)]
fakeSidebands = [(0.05, 0.50)]

applyHEMveto = True

stdout = sys.stdout
nullout = open("/dev/null", "w")

for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing fake track background estimate in search region(2018", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("fakeTrackBkgdEstimate_zToMuMu_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2018" + runPeriod])
            fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoMuMuDisTrkNoD0CutNLayers4",       "SingleMu_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/fakeBackground")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoMuMuDisTrkNoD0Cut" + nLayersWord, "SingleMu_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/fakeBackground")
            fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                     "MET_2018"      + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/basicSelection_v2")
            fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoMuMu",                            "SingleMu_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/zToMuMu")

            print("********************************************************************************")
            print("Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1]))
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
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
            print("performing fake track background estimate with Z->ee selection in search region(2018", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("fakeTrackBkgdEstimate_zToEE_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2018" + runPeriod])
            # durp
            # only 99.4% of events were run over (failed job in A), so there is an extra prescale factor
            fakeTrackBkgdEstimate.addPrescaleFactor ((16299633 + 19271182 + 20289301 + 21758154 + 6815966 + 27504879 + 49328605 + 10905430 + 68323666) / 238987094.0)
            fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoEEDisTrkNoD0CutNLayers4",       "EGamma_2018" + runPeriod, dirs['Mike']   + "kweiStore/2018/fromLPC/fakeTrackSystematic_zToEE")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoEEDisTrkNoD0Cut" + nLayersWord, "EGamma_2018" + runPeriod, dirs['Mike']   + "kweiStore/2018/fromLPC/fakeTrackSystematic_zToEE")
            fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                   "MET_2018"    + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/basicSelection_v2")
            fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoEE",                            "EGamma_2018" + runPeriod, dirs['Mike']   + "kweiStore/2018/fromLPC/zToEE")

            print("********************************************************************************")
            print("Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1]))
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
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
                    sbResults = fakeTrackBkgdEstimate.printNest (verbose = False)
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
            print("performing electron background estimate in search region(2018", runPeriod, "-- combined layers bins)")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("electronBkgdEstimate_2018" + runPeriod + "_combinedBins.root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["EGamma_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["EGamma_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            electronBkgdEstimate.addPlotLabel("EGamma 2018" + runPeriod)

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[0], "EGamma_2018"        + runPeriod, dirs['Mike'] + "kweiStore/2018/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[0], "EGamma_rereco_2018" + runPeriod, dirs['Mike'] + "kweiStore/2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[0], "EGamma_rereco_2018" + runPeriod, dirs['Mike'] + "kweiStore/2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[0], "EGamma_2018"        + runPeriod, dirs['Mike'] + "kweiStore/2018/fromLPC/electronControlRegionBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[0], "EGamma_2018"        + runPeriod, dirs['Mike'] + "kweiStore/2018/fromLPC/electronControlRegionBinnedLayers")
        
            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                # HEM 15/16 issue; veto MET in phi range
                electronBkgdEstimate.addChannel("TagPt35MetTrigHEMveto", "ElectronTagPt55MetTrigHEMveto" + nLayersWords[0], "EGamma_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/electronControlRegion_HEMveto")

            for iBin in range(1, len(nLayersWords)):
                electronBkgdEstimate.appendChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[iBin], "EGamma_2018"        + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/eleBkgdNoFilterBinnedLayers")
                electronBkgdEstimate.appendChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[iBin], "EGamma_rereco_2018" + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/eleBkgdWithFilterBinnedLayers")
                electronBkgdEstimate.appendChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[iBin], "EGamma_rereco_2018" + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/eleBkgdWithFilterBinnedLayers")
                electronBkgdEstimate.appendChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[iBin], "EGamma_2018"        + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/electronControlRegionBinnedLayers")
                electronBkgdEstimate.appendChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[iBin], "EGamma_2018"        + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/electronControlRegionBinnedLayers")
                if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                    # HEM 15/16 issue; veto MET in phi range
                    electronBkgdEstimate.appendChannel("TagPt35MetTrigHEMveto", "ElectronTagPt55MetTrigHEMveto" + nLayersWords[iBin], "EGamma_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/electronControlRegion_HEMveto")

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
            print("performing electron background estimate in search region(2018", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("electronBkgdEstimate_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["EGamma_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["EGamma_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            electronBkgdEstimate.addPlotLabel("EGamma 2018" + runPeriod)

            electronBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.840, 0.005))

            if False:
                if runPeriod is 'AB':
                    electronBkgdEstimate.useExternalTriggerEfficiency (47952, 118, 50044, 141)
                    #if nLayersWord is 'NLayers4': electronBkgdEstimate.useExternalTriggerEfficiency (647, 12, 812, 29)
                    #elif nLayersWord is 'NLayers5': electronBkgdEstimate.useExternalTriggerEfficiency (1572, 10, 1702, 12)
                    #elif nLayersWord is 'NLayers6plus': electronBkgdEstimate.useExternalTriggerEfficiency (45733, 96, 47532, 100)
                elif runPeriod is 'CD':
                    electronBkgdEstimate.useExternalTriggerEfficiency (67485, 137, 70422, 167)
                    #if nLayersWord is 'NLayers4': electronBkgdEstimate.useExternalTriggerEfficiency (920, 24, 1131, 46)
                    #elif nLayersWord is 'NLayers5': electronBkgdEstimate.useExternalTriggerEfficiency (2137, 10, 2323, 14)
                    #elif nLayersWord is 'NLayers6plus': electronBkgdEstimate.useExternalTriggerEfficiency (64428, 103, 66968, 107)

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWord, "EGamma_2018"        + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWord, "EGamma_rereco_2018" + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWord, "EGamma_rereco_2018" + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWord, "EGamma_2018"        + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/electronControlRegionBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWord, "EGamma_2018"        + runPeriod, dirs['Mike']+"kweiStore/2018/fromLPC/electronControlRegionBinnedLayers")

            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                # HEM 15/16 issue; veto MET in phi range
                electronBkgdEstimate.addChannel("TagPt35MetTrigHEMveto", "ElectronTagPt55MetTrigHEMveto" + nLayersWord, "EGamma_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/electronControlRegion_HEMveto")
        
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
            print("performing muon background estimate in search region(2018", runPeriod, "-- combined layer bins)")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("muonBkgdEstimate_2018" + runPeriod + "_combinedBins.root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["SingleMuon_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["SingleMuon_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            muonBkgdEstimate.addPlotLabel("SingleMuon 2018" + runPeriod)

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[0])
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[0], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[0])
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[0], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[0])
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")


            for iBin in range(1, len(nLayersWords)):
                muonBkgdEstimate.appendChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[iBin])
                muonBkgdEstimate.appendChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[iBin], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[iBin])
                muonBkgdEstimate.appendChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[iBin], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[iBin])
                muonBkgdEstimate.appendChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")
                muonBkgdEstimate.appendChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")

            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                # only NLayers6plus has any events passing in CD, so these aren't in the above block -- they're the only channels, so no "appendChannel"
                # HEM 15/16 issue; veto MET in phi range
                #muonBkgdEstimate.addChannel("TagPt35HEMveto",        "MuonTagPt55HEMvetoNLayers6plus",        "SingleMu_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion_HEMveto_NLayers6plus")
                muonBkgdEstimate.addChannel("TagPt35MetTrigHEMveto", "MuonTagPt55MetTrigHEMvetoNLayers6plus", "SingleMu_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion_HEMveto_NLayers6plus")

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
            print("performing muon background estimate in search region(2018", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("muonBkgdEstimate_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["SingleMuon_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["SingleMuon_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            muonBkgdEstimate.addPlotLabel("SingleMuon 2018" + runPeriod)

            muonBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.940, 0.004))

            if False:
                if runPeriod is 'AB':
                    muonBkgdEstimate.useExternalTriggerEfficiency (390778, 58, 412351, 139)
                    #if nLayersWord is 'NLayers4': muonBkgdEstimate.useExternalTriggerEfficiency (22, 2, 132, 49) # >55 GeV (0-0)/(17 - 24) --> NaN
                    #elif nLayersWord is 'NLayers5': muonBkgdEstimate.useExternalTriggerEfficiency (30, 0, 92, 5) # >55 GeV (0-0)/(2 - 3) --> NaN
                    #elif nLayersWord is 'NLayers6plus': muonBkgdEstimate.useExternalTriggerEfficiency (390778, 58, 412332, 63)
                elif runPeriod is 'CD':
                    muonBkgdEstimate.useExternalTriggerEfficiency (430356, 44, 452247, 75)
                    #if nLayersWord is 'NLayers4': muonBkgdEstimate.useExternalTriggerEfficiency (5, 2, 101, 65) # >55 GeV (0-0)/(20-24) --> NaN
                    #elif nLayersWord is 'NLayers5': muonBkgdEstimate.useExternalTriggerEfficiency (6, 0, 94, 8) # >55 GeV (0-0)/(5-3) --> NaN
                    #elif nLayersWord is 'NLayers6plus': muonBkgdEstimate.useExternalTriggerEfficiency (430356, 44, 452222, 48)

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWord)
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWord, "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWord)
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWord, "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWord)
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")

            if runPeriod in ['C', 'D', 'CD'] and nLayersWord == "NLayers6plus" and applyHEMveto:
                # only NLayers6plus has any events passing in CD
                # HEM 15/16 issue; veto MET in phi range
                #muonBkgdEstimate.addChannel("TagPt35HEMveto",        "MuonTagPt55HEMvetoNLayers6plus",        "SingleMu_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion_HEMveto_NLayers6plus")
                muonBkgdEstimate.addChannel("TagPt35MetTrigHEMveto", "MuonTagPt55MetTrigHEMvetoNLayers6plus", "SingleMu_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion_HEMveto_NLayers6plus")

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
            print("performing tau background estimate in search region(2018", runPeriod, "-- combined layer bins)")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("tauBkgdEstimate_2018" + runPeriod + "_combinedBins.root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2018" + runPeriod)
            
            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWords[0], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWords[0], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWords[0], "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWords[0], "EGamma_rereco_2018"   + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWords[0], "EGamma_rereco_2018"   + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWords[0], "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWords[0], "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWords[0], "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWords[0], "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWords[0], "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")

            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                # HEM 15/16 issue; veto MET in phi range
                tauBkgdEstimate.addChannel("TrigEffNumerHEMveto", "ElectronTagPt55MetTrigHEMveto" + nLayersWords[0], "EGamma_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/electronControlRegion_HEMveto")

            for iBin in range(1, len(nLayersWords)):
                tauBkgdEstimate.appendChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
                tauBkgdEstimate.appendChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWords[iBin], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
                tauBkgdEstimate.appendChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWords[iBin], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
                tauBkgdEstimate.appendChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWords[iBin], "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
                tauBkgdEstimate.appendChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWords[iBin], "EGamma_rereco_2018"   + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
                tauBkgdEstimate.appendChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWords[iBin], "EGamma_rereco_2018"   + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
                tauBkgdEstimate.appendChannel("TagPt35",          "TauTagPt55"                      + nLayersWords[iBin], "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
                tauBkgdEstimate.appendChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWords[iBin], "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
                tauBkgdEstimate.appendChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWords[iBin], "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/electronControlRegionBinnedLayers")
                tauBkgdEstimate.appendChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWords[iBin], "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/electronControlRegionBinnedLayers")
                tauBkgdEstimate.appendChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWords[iBin], "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
 
                if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                    # HEM 15/16 issue; veto MET in phi range
                    tauBkgdEstimate.appendChannel("TrigEffNumerHEMveto", "ElectronTagPt55MetTrigHEMveto" + nLayersWords[iBin], "EGamma_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/electronControlRegion_HEMveto")

            tauBkgdEstimate.useOnlineQuantitiesForPpassMetTriggers(False) # doesn't work without a custom HLT menu and full re-reco...
            tauBkgdEstimate.addRebinFactor(8)

            print("********************************************************************************")

            nEstTau[("combinedBins", runPeriod)] = tauBkgdEstimate.printNest()
            tauBkgdEstimate.printPpassVetoTagProbe()

            combinedPpassMetCut = tauBkgdEstimate.getPpassMetCut()
            combinedPpassMetTriggers, combinedTriggerEfficiency = tauBkgdEstimate.getPpassMetTriggers()

            combinedPpassHEMveto = None
            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                combinedPpassHEMveto = tauBkgdEstimate.getPpassHEMveto()

            print("********************************************************************************")
            
            fout.Close()

            print("\n\n")

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing tau background estimate in search region(2018", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("tauBkgdEstimate_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2018" + runPeriod)
            
            tauBkgdEstimate.useExternalFlatTriggerEfficiency (Measurement (0.900, 0.006))

            if runPeriod == '2018':
                # Can only find 3/38 events in SingleMuon 2018A
                if nLayersWord == 'NLayers4':
                    tauBkgdEstimate.addTagProbePass1ScaleFactor(121./94.)
                if nLayersWord == 'NLayers5':
                    tauBkgdEstimate.addTagProbePass1ScaleFactor(28./21.)
                if nLayersWord == 'NLayers6plus':
                    tauBkgdEstimate.addTagProbePass1ScaleFactor(21./20.)

            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWord, "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWord, "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/ZtoTauToMuProbeTrk")
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWord, "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWord, "EGamma_rereco_2018"   + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWord, "EGamma_rereco_2018"   + runPeriod, dirs['Kai']   + "2018/fromLPC/ZtoTauToEleProbeTrk")
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWord, "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWord, "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWord, "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWord, "EGamma_2018"          + runPeriod, dirs['Kai']   + "2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWord, "Tau_2018"             + runPeriod, dirs['Brian'] + "2018/fromLPC/TauControlRegion")

            if runPeriod in ['C', 'D', 'CD'] and applyHEMveto:
                # HEM 15/16 issue; veto MET in phi range
                tauBkgdEstimate.addChannel("TrigEffNumerHEMveto", "ElectronTagPt55MetTrigHEMveto" + nLayersWord, "EGamma_2018" + runPeriod, dirs['Brian'] + "2018/fromLPC/electronControlRegion_HEMveto")

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
