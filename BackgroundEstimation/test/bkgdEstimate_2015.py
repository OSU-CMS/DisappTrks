#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate
from DisappTrks.BackgroundEstimation.fakeEstimateTest import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I too am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

nEstFake = []
nEstElectron = []
nEstMuon = []
nEstTau = []

runPeriods = ["D"]

if background == "FAKE" or background == "ALL":

    print "********************************************************************************"
    print "performing fake track background estimate in disappearing track search region (2015)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2015.root", "recreate")

    fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimate.addTFile (fout)
    fakeTrackBkgdEstimate.addTCanvas (canvas)
    fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
    fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "DisTrkSelectionNoD0CutNHits3",  "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
    fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "DisTrkSelectionSidebandD0Cut",  "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
    fakeTrackBkgdEstimate.addChannel  ("Basic",           "BasicSelection",                "MET_2015D",  dirs['Brian']+"2015/basicSelection")

    print "********************************************************************************"

    fakeTrackBkgdEstimate.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing fake track background estimate in ZtoMuMu (2015)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("zToMuMuEstimate_2015.root", "recreate")

    zToMuMuEstimate = FakeTrackBkgdEstimate ()
    zToMuMuEstimate.addTFile (fout)
    zToMuMuEstimate.addTCanvas (canvas)
    zToMuMuEstimate.addLuminosityInInvPb (lumi["SingleMuon_2015"])
    zToMuMuEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0CutNHits3",  "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_noD0Cut")
    zToMuMuEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkSidebandD0Cut",  "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
    zToMuMuEstimate.addChannel  ("Basic",           "BasicSelection",              "MET_2015D"     ,  dirs['Brian']+"2015/basicSelection")
    zToMuMuEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                     "SingleMu_2015D",  dirs['Brian']+"2015/zToMuMu")

    print "********************************************************************************"

    nEstFake.append( zToMuMuEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "ELECTRON" or background == "ALL":

    print "********************************************************************************"
    print "performing electron background estimate in disappearing track search region"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("electronBkgdEstimate_2015.root", "recreate")

    electronBkgdEstimate = LeptonBkgdEstimate ("electron")
    electronBkgdEstimate.addTFile (fout)
    electronBkgdEstimate.addTCanvas (canvas)
    electronBkgdEstimate.addPrescaleFactor (lumi["MET_2015"] / lumi["SingleElectron_2015"])
    # One event in ../data/zToEleDisTrk_2015_raw.root produces a segfault
    electronBkgdEstimate.addTagProbePassScaleFactor (9./10.)
    electronBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
    electronBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleElectron_2015"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronBkgdEstimate.addPlotLabel ("SingleElectron 2015D")
    electronBkgdEstimate.addMetCut (100.0)
    electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2015D",         dirs['Brian']+"2015/electronBackground")
    electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2015D_rereco",  dirs['Brian']+"2015/electronBackground")
    electronBkgdEstimate.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2015D",         dirs['Brian']+"2015/electronBackground")
    electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2015D",         dirs['Brian']+"2015/electronBackground")

    print "********************************************************************************"

    nEstElectron.append( electronBkgdEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "MUON" or background == "ALL":

    print "********************************************************************************"
    print "performing muon background estimate in disappearing track search region"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("muonBkgdEstimate_2015.root", "recreate")

    muonBkgdEstimate = LeptonBkgdEstimate ("muon")
    muonBkgdEstimate.addTFile (fout)
    muonBkgdEstimate.addTCanvas (canvas)
    muonBkgdEstimate.addPrescaleFactor (lumi["MET_2015"] / lumi["SingleMuon_2015"])
    # One event in ../data/zToMuDisTrk_2015_raw.root produces a segfault
    muonBkgdEstimate.addTagProbePassScaleFactor (5./6.)
    muonBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
    muonBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleMuon_2015"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    muonBkgdEstimate.addPlotLabel ("SingleMuon 2015D")
    muonBkgdEstimate.addMetCut (100.0)
    muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2015D",         dirs['Brian']+"2015/muonBackground")
    muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2015D_rereco",  dirs['Brian']+"2015/muonBackground")
    muonBkgdEstimate.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2015D",         dirs['Brian']+"2015/muonBackground")
    muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2015D",         dirs['Brian']+"2015/muonBackground")

    print "********************************************************************************"

    nEstMuon.append( muonBkgdEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "TAU" or background == "ALL":

    print "********************************************************************************"
    print "performing tau background estimate in disappearing track search region"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("tauBkgdEstimate_2015.root", "recreate")

    tauBkgdEstimate = LeptonBkgdEstimate ("tau")
    tauBkgdEstimate.addTFile (fout)
    tauBkgdEstimate.addTCanvas (canvas)
    tauBkgdEstimate.addPrescaleFactor (lumi["MET_2015"] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015"])
    tauBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
    tauBkgdEstimate.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    tauBkgdEstimate.addPlotLabel ("Tau 2015D")
    tauBkgdEstimate.addMetCut (100.0)
    tauBkgdEstimate.addRebinFactor (4)
    tauBkgdEstimate.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCuts",   "SingleMu_2015D",          dirs['Brian']+"2015/muonBackground")
    tauBkgdEstimate.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrk",              "SingleMu_2015D_rereco",   dirs['Brian']+"2015/muonBackground")
    tauBkgdEstimate.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCuts",  "SingleEle_2015D",         dirs['Brian']+"2015/electronBackground")
    tauBkgdEstimate.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrk",             "SingleEle_2015D_rereco",  dirs['Brian']+"2015/electronBackground")
    tauBkgdEstimate.addChannel  ("TagPt35",         "TauTagPt55",                    "Tau_2015D",               dirs['Brian']+"2015/tauBackground")
    #tauBkgdEstimate.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",             "Tau_2015D",               dirs['Brian']+"2015/tauBackground_metTrig")
    tauBkgdEstimate.addChannel  ("TrigEffDenom",    "ElectronTagPt55",               "SingleEle_2015D",         dirs['Brian']+"2015/electronBackground")
    tauBkgdEstimate.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",        "SingleEle_2015D",         dirs['Brian']+"2015/electronBackground")

    print "********************************************************************************"

    nEstTau.append( tauBkgdEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

# print sums
if background == "ALL":
    print "********************************************************************************"
    nLeptons = nEstElectron[0][0] + nEstMuon[0][0] + nEstTau[0][0]
    nLeptonsError = math.hypot (math.hypot (nEstElectron[0][1], nEstMuon[0][1]), nEstTau[0][1])
    nTotal = nLeptons + nEstFake[0][0]
    nTotalError = math.hypot(nLeptonsError, nEstFake[0][1])
    print "Total background from leptons (2015):", nLeptons, "+/-", nLeptonsError
    print "Total background from fake tracks (2015):", nEstFake[0][0], "+/-", nEstFake[0][1]
    print "********************************************************************************"
    print "Total background (2015):", nTotal, "+/-", nTotalError
    print "********************************************************************************"
    print "\n\n"

    nFakes = nEstFake[0]

    x = array ("d"); ex = array ("d")
    electron   =  array  ("d");  muon   =  array  ("d");  tau   =  array  ("d");  fake   =  array  ("d")
    eElectron  =  array  ("d");  eMuon  =  array  ("d");  eTau  =  array  ("d");  eFake  =  array  ("d")

    runPeriodsToPlot = ["D"]
    i = 0.0

    for runPeriod in runPeriodsToPlot:
        x.append (i); ex.append (0.0); i += 1.0

        electron.append  (nEstElectron[runPeriods.index  (runPeriod)][0]  /  lumi["MET_2015"  +  runPeriod])
        muon.append      (nEstMuon[runPeriods.index      (runPeriod)][0]  /  lumi["MET_2015"  +  runPeriod])
        tau.append       (nEstTau[runPeriods.index       (runPeriod)][0]  /  lumi["MET_2015"  +  runPeriod])
        fake.append      (nEstFake[runPeriods.index      (runPeriod)][0]  /  lumi["MET_2015"  +  runPeriod])

        eElectron.append  (nEstElectron[runPeriods.index  (runPeriod)][1]  /  lumi["MET_2015"  +  runPeriod])
        eMuon.append      (nEstMuon[runPeriods.index      (runPeriod)][1]  /  lumi["MET_2015"  +  runPeriod])
        eTau.append       (nEstTau[runPeriods.index       (runPeriod)][1]  /  lumi["MET_2015"  +  runPeriod])
        eFake.append      (nEstFake[runPeriods.index      (runPeriod)][1]  /  lumi["MET_2015"  +  runPeriod])

    gElectron  =  TGraphErrors  (len  (x),  x,  electron,  ex,  eElectron)
    gMuon      =  TGraphErrors  (len  (x),  x,  muon,      ex,  eMuon)
    gTau       =  TGraphErrors  (len  (x),  x,  tau,       ex,  eTau)
    gFake      =  TGraphErrors  (len  (x),  x,  fake,      ex,  eFake)

    fout = TFile.Open ("backgroundCrossSections_2015.root", "recreate")
    fout.cd ()
    gElectron.Write ("electron")
    gMuon.Write ("muon")
    gTau.Write ("tau")
    gFake.Write ("fake")
    fout.Close ()
