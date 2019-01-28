#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate, FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]

# '' will gives you Dataset_2017.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F']
runPeriods = ['']

nEstFake = {}
nEstElectron = {}
nEstMuon = {}
nEstTau = {}

nLeptons = {}
nTotal = {}

nEstFakeVsNHits = {}
nEstFakeVsNHitsZtoMuMu = {}

stdout = sys.stdout
nullout = open("/dev/null", "w")

for runPeriod in runPeriods:

    nEstFakeVsNHits[runPeriod] = {}
    nEstFakeVsNHitsZtoMuMu[runPeriod] = {}

    if background == "FAKE" or background == "ALL":

        for minHits in range(3, 8):

            if minHits != 7:
                sys.stdout = nullout
            else:
                sys.stdout = stdout

            print "********************************************************************************"
            print "performing fake track background estimate in search region(2017", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("fakeTrackBkgdEstimate_2017" + runPeriod + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate()
            fakeTrackBkgdEstimate.addTFile(fout)
            fakeTrackBkgdEstimate.addTCanvas(canvas)
            fakeTrackBkgdEstimate.addLuminosityInInvPb(lumi["MET_2017" + runPeriod])
            fakeTrackBkgdEstimate.addMinHits(minHits)
            fakeTrackBkgdEstimate.addChannel("Basic3hits",           "DisTrkSelectionNoD0CutNHits3",       "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/fakeTrackSystematic_tmp")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0",       "DisTrkSelectionSidebandD0Cut",       "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/fakeTrackSystematic_tmp")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0NHits3", "DisTrkSelectionSidebandD0CutNHits3", "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/fakeTrackSystematic_tmp")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0NHits4", "DisTrkSelectionSidebandD0CutNHits4", "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/fakeTrackSystematic_tmp")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0NHits5", "DisTrkSelectionSidebandD0CutNHits5", "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/fakeTrackSystematic_tmp")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0NHits6", "DisTrkSelectionSidebandD0CutNHits6", "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/fakeTrackSystematic_tmp")
            fakeTrackBkgdEstimate.addChannel("Basic",                "BasicSelection",                     "MET_2017" + runPeriod, dirs['Brian']+"2017/fromRutgers/basicSelection")

            print "********************************************************************************"

            nEst = fakeTrackBkgdEstimate.printNest()
            nEstFakeVsNHits[runPeriod][minHits] = nEst

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

            print "********************************************************************************"
            print "performing fake track background estimate in ZtoMuMu(2017", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("zToMuMuEstimate_2017" + runPeriod + ".root", "recreate")

            zToMuMuEstimate = FakeTrackBkgdEstimate()
            zToMuMuEstimate.addTFile(fout)
            zToMuMuEstimate.addTCanvas(canvas)
            zToMuMuEstimate.addLuminosityInInvPb(lumi["SingleMuon_2017" + runPeriod])
            zToMuMuEstimate.addMinHits(minHits)
            zToMuMuEstimate.addChannel("Basic3hits",           "ZtoMuMuDisTrkNoD0CutNHits3",       "SingleMu_2017" + runPeriod, dirs['fixme']+"2017/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel("DisTrkInvertD0",       "ZtoMuMuDisTrkSidebandD0Cut",       "SingleMu_2017" + runPeriod, dirs['fixme']+"2017/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel("DisTrkInvertD0NHits3", "ZtoMuMuDisTrkSidebandD0CutNHits3", "SingleMu_2017" + runPeriod, dirs['fixme']+"2017/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel("DisTrkInvertD0NHits4", "ZtoMuMuDisTrkSidebandD0CutNHits4", "SingleMu_2017" + runPeriod, dirs['fixme']+"2017/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel("DisTrkInvertD0NHits5", "ZtoMuMuDisTrkSidebandD0CutNHits5", "SingleMu_2017" + runPeriod, dirs['fixme']+"2017/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel("DisTrkInvertD0NHits6", "ZtoMuMuDisTrkSidebandD0CutNHits6", "SingleMu_2017" + runPeriod, dirs['fixme']+"2017/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel("Basic",                "BasicSelection",                   "MET_2017"      + runPeriod, dirs['Brian']+"2017/fromRutgers/basicSelection")
            zToMuMuEstimate.addChannel("ZtoLL",                "ZtoMuMu",                          "SingleMu_2017" + runPeriod, dirs['Brian']+"2017/zToMuMu")

            print "********************************************************************************"

            nEst = zToMuMuEstimate.printNest()
            nEstFakeVsNHitsZtoMuMu[runPeriod][minHits] = nEst
            if minHits == 7:
                nEstFake[runPeriod] = nEst

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

    if background == "ELECTRON" or background == "LEPTON" or background == "ALL":

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing electron background estimate in search region(2017", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("electronBkgdEstimate_2017" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(lumi["MET_2017" + runPeriod] / lumi["SingleElectron_2017" + runPeriod])
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2017" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["SingleElectron_2017" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            electronBkgdEstimate.addPlotLabel("SingleElectron 2017" + runPeriod)

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWord, "SingleEle_2017"        + runPeriod, dirs['Brian']+"2017/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWord, "SingleEle_rereco_2017" + runPeriod, dirs['Brian']+"2017/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWord, "SingleEle_rereco_2017" + runPeriod, dirs['Brian']+"2017/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWord, "SingleEle_2017"        + runPeriod, dirs['Brian']+"2017/fromLPC/electronControlRegionBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWord, "SingleEle_2017"        + runPeriod, dirs['Brian']+"2017/fromLPC/electronControlRegionBinnedLayers")
        
            electronBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # use offline quantities instead of online
            electronBkgdEstimate.addRebinFactor(4)

            print "********************************************************************************"

            nEstElectron[(nLayersWord, runPeriod)] = electronBkgdEstimate.printNest()
            electronBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

    if background == "MUON" or background == "LEPTON" or background == "ALL":

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing muon background estimate in search region(2017", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("muonBkgdEstimate_2017" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(lumi["MET_2017" + runPeriod] / lumi["SingleMuon_2017" + runPeriod])
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2017" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["SingleMuon_2017" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            muonBkgdEstimate.addPlotLabel("SingleMuon 2017" + runPeriod)

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWord, "SingleMu_2017" + runPeriod, dirs['Brian'] + "2017/muonBackgroundNoFilterBinnedLayers")
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWord, "SingleMu_rereco_2017" + runPeriod, dirs['Brian'] + "2017/muonBackgroundNoFilterBinnedLayers")
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWord, "SingleMu_rereco_2017" + runPeriod, dirs['Brian'] + "2017/muonBackgroundNoFilterBinnedLayers")
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWord, "SingleMu_2017" + runPeriod, dirs['Brian'] + "2017/muonBackgroundControlRegionBinnedLayers")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWord, "SingleMu_2017" + runPeriod, dirs['Brian'] + "2017/muonBackgroundControlRegionBinnedLayers")

            muonBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # use offline quantities instead of online
            muonBkgdEstimate.addRebinFactor(4)

            print "********************************************************************************"

            nEstMuon[(nLayersWord, runPeriod)] = muonBkgdEstimate.printNest()
            muonBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

    if background == "TAU" or background == "LEPTON" or background == "ALL":

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing tau background estimate in search region(2017", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("tauBkgdEstimate_2017" + runPeriod + ".root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(lumi["MET_2017" + runPeriod] / lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2017" + runPeriod])
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2017" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2017" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2017" + runPeriod)
            
            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWord, "SingleMu_2017"         + runPeriod, dirs['Brian']+"2017/fromLPC/zToTauToMuBkgd"  + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWord, "SingleMu_rereco_2017"  + runPeriod, dirs['Brian']+"2017/fromLPC/zToTauToMuBkgd"  + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWord, "SingleMu_rereco_2017"  + runPeriod, dirs['Brian']+"2017/fromLPC/zToTauToMuBkgd"  + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWord, "SingleEle_2017"        + runPeriod, dirs['Brian']+"2017/fromLPC/zToTauToEleBkgd" + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWord, "SingleEle_rereco_2017" + runPeriod, dirs['Brian']+"2017/fromLPC/zToTauToEleBkgd" + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWord, "SingleEle_rereco_2017" + runPeriod, dirs['Brian']+"2017/fromLPC/zToTauToEleBkgd" + nLayersWord)
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWord, "Tau_2017"              + runPeriod, dirs['Brian']+"2017/fromLPC/tauControlRegionBinnedHits_v2")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWord, "Tau_2017"              + runPeriod, dirs['Brian']+"2017/fromLPC/tauControlRegionBinnedHits_v2")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWord, "SingleEle_2017"        + runPeriod, dirs['Brian']+"2017/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWord, "SingleEle_2017"        + runPeriod, dirs['Brian']+"2017/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWord, "Tau_2017"              + runPeriod, dirs['Brian']+"2017/fromLPC/tauControlRegionBinnedHits")

            tauBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # temporary measure
            tauBkgdEstimate.addRebinFactor(8)

            print "********************************************************************************"

            nEstTau[(nLayersWord, runPeriod)] = tauBkgdEstimate.printNest()
            tauBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

sys.stdout = stdout

# print sums
if background == "ALL":
    nElectrons = {}
    nMuons = {}
    nTaus = {}
    nFakes = {}

    nLeptons = copy.deepcopy(nEstElectron)
    nTotal = copy.deepcopy(nEstElectron)

    for runPeriod in runPeriods:
        for nLayersWord in nLayersWords:
            nLeptons[(nLayersWord, runPeriod)] += nEstMuon[(nLayersWord, runPeriod)] + nEstTau[(nLayersWord, runPeriod)]
            nTotal[(nLayersWord, runPeriod)] = nLeptons[(nLayersWord, runPeriod)] + nEstFake[(nLayersWord, runPeriod)]
            print "********************************************************************************"
            print "Total background from leptons (2017" + runPeriod + ", " + nLayersWord + "): " + nLayersWord[(nLayersWord, runPeriod)]
            print "Total background from fake tracks (2017" + runPeriod + ", " + nLayersWord + "): " + nEstFake[(nLayersWord, runPeriod)]
            print "********************************************************************************"
            print "Total background (2017" + runPeriod + ", " + nLayersWord + "): " + nTotal[(nLayersWord, runPeriod)]
            print "********************************************************************************"
            print "\n\n"

    fout = TFile.Open("backgroundCrossSections_2017.root", "recreate")

    for nLayersWord in nLayersWords:

        x = array("d"); ex = array("d")
        electron   =  array ("d");  muon   =  array ("d");  tau   =  array ("d");  fake   =  array ("d")
        eElectron  =  array ("d");  eMuon  =  array ("d");  eTau  =  array ("d");  eFake  =  array ("d")

        #runPeriodsToPlot = ["B", "C", "D", "E", "F"]
        runPeriodsToPlot = [""]
        i = 0.0

        for runPeriod in runPeriodsToPlot:
            x.append(i)
            ex.append(0.0)
            i += 1.0

            electron.append( nEstElectron[(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).centralValue()
            muon.append    ( nEstMuon    [(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).centralValue()
            tau.append     ( nEstTau     [(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).centralValue()
            fake.append    ( nEstFake    [(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).centralValue()

            eElectron.append( nEstElectron[(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).maxUncertainty()
            eMuon.append    ( nEstMuon    [(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).maxUncertainty()
            eTau.append     ( nEstTau     [(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).maxUncertainty()
            eFake.append    ( nEstFake    [(nLayersWord, runPeriod)] / lumi["MET_2017" + runPeriod] ).maxUncertainty()

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