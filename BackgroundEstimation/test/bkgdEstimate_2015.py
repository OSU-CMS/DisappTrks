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

runPeriods = ['D']

nEstFake = []
nEstElectron = []
nEstMuon = []
nEstTau = []

nEstFakeVsNHits = {}
nEstFakeVsNHitsZtoMuMu = {}

stdout = sys.stdout
nullout = open ("/dev/null", "w")

if background == "FAKE" or background == "ALL":

    for minHits in range (3, 8):

        if minHits != 7:
            sys.stdout = nullout
        else:
            sys.stdout = stdout

        print "********************************************************************************"
        print "performing fake track background estimate in disappearing track search region (2015)"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackBkgdEstimate_2015.root", "recreate")

        fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
        fakeTrackBkgdEstimate.addTFile (fout)
        fakeTrackBkgdEstimate.addTCanvas (canvas)
        fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
        fakeTrackBkgdEstimate.addMinHits (minHits)
        fakeTrackBkgdEstimate.addChannel  ("Basic3hits",            "DisTrkSelectionNoD0CutNHits3",        "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",        "DisTrkSelectionSidebandD0Cut",        "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits3",  "DisTrkSelectionSidebandD0CutNHits3",  "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits4",  "DisTrkSelectionSidebandD0CutNHits4",  "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits5",  "DisTrkSelectionSidebandD0CutNHits5",  "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits6",  "DisTrkSelectionSidebandD0CutNHits6",  "MET_2015D",  dirs['Brian']+"2015/fakeTrackBackground_d0sideband")
        fakeTrackBkgdEstimate.addChannel  ("Basic",                 "BasicSelection",                      "MET_2015D",  dirs['Brian']+"2015/basicSelection")

        print "********************************************************************************"

        nEst = fakeTrackBkgdEstimate.printNest ()
        nEstFakeVsNHits[minHits] = nEst

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
        zToMuMuEstimate.addMinHits (minHits)
        zToMuMuEstimate.addChannel  ("Basic3hits",            "ZtoMuMuDisTrkNoD0CutNHits3",        "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_noD0Cut")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0",        "ZtoMuMuDisTrkSidebandD0Cut",        "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits3",  "ZtoMuMuDisTrkSidebandD0CutNHits3",  "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits4",  "ZtoMuMuDisTrkSidebandD0CutNHits4",  "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits5",  "ZtoMuMuDisTrkSidebandD0CutNHits5",  "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits6",  "ZtoMuMuDisTrkSidebandD0CutNHits6",  "SingleMu_2015D",  dirs['Brian']+"2015/fakeTrackSystematic_d0sideband")
        zToMuMuEstimate.addChannel  ("Basic",                 "BasicSelection",                    "MET_2015D",       dirs['Brian']+"2015/basicSelection")
        zToMuMuEstimate.addChannel  ("ZtoLL",                 "ZtoMuMu",                           "SingleMu_2015D",  dirs['Brian']+"2015/zToMuMu")

        print "********************************************************************************"

        nEst = zToMuMuEstimate.printNest ()
        nEstFakeVsNHitsZtoMuMu[minHits] = nEst
        if minHits == 7:
            nEstFake.append( nEst )

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
    electronBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
    electronBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleElectron_2015"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronBkgdEstimate.addPlotLabel ("SingleElectron 2015D")
    electronBkgdEstimate.addMetCut (100.0)
    electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrk",              "SingleEle_2015D",         dirs['Andrew']+"2015/stenson/electronBackground")
    electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleProbeTrk",              "SingleEle_rereco_2015D",  dirs['Andrew']+"2015/stenson/electronBackground")
    electronBkgdEstimate.addChannel  ("TagProbePassSS",  "ZtoEleProbeTrkWithSSFilter",  "SingleEle_2015D",         dirs['Andrew']+"2015/stenson/sameSign/skims/electronBackground")
    electronBkgdEstimate.addChannel  ("TagPt35",         "ElectronTagPt55",             "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")

    #electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")

    electronBkgdEstimate.addUseHistogramsForPpassMetTriggers (True)
    electronBkgdEstimate.addRebinFactor (4)
    electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55",  "SingleEle_2015D",  dirs['Andrew']+"2015/electronBackground_passesMETTriggers_new")

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
    muonBkgdEstimate.addLuminosityInInvPb (lumi["MET_2015"])
    muonBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleMuon_2015"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    muonBkgdEstimate.addPlotLabel ("SingleMuon 2015D")
    muonBkgdEstimate.addMetCut (100.0)
    muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrk",              "SingleMu_2015D",         dirs['Andrew']+"2015/stenson/muonBackground")
    muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuProbeTrk",              "SingleMu_rereco_2015D",  dirs['Andrew']+"2015/stenson/muonBackground")
    muonBkgdEstimate.addChannel  ("TagProbePassSS",  "ZtoMuProbeTrkWithSSFilter",  "SingleMu_2015D",         dirs['Andrew']+"2015/stenson/sameSign/skims/muonBackground")
    muonBkgdEstimate.addChannel  ("TagPt35",         "MuonTagPt55",                "SingleMu_2015D",         dirs['Andrew']+"2015/muonBackground_nCtrl_new")

    #muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2015D",         dirs['Andrew']+"2015/muonBackground_nCtrl_new")

    muonBkgdEstimate.addUseHistogramsForPpassMetTriggers (True)
    muonBkgdEstimate.addRebinFactor (4)
    muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55",  "SingleMu_2015D",  dirs['Andrew']+"2015/muonBackground_passesMETTriggers_new")

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
    tauBkgdEstimate.addChannel  ("TagProbe",         "ZtoTauToMuProbeTrk",               "SingleMu_2015D",          dirs['Andrew']+"2015/stenson/tauToMuonBackground")
    tauBkgdEstimate.addChannel  ("TagProbePass",     "ZtoTauToMuProbeTrk",               "SingleMu_rereco_2015D",   dirs['Andrew']+"2015/stenson/tauToMuonBackground")
    tauBkgdEstimate.addChannel  ("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter",   "SingleMu_2015D",          dirs['Andrew']+"2015/stenson/sameSign/skims/tauToMuonBackground")
    tauBkgdEstimate.addChannel  ("TagProbe1",        "ZtoTauToEleProbeTrk",              "SingleEle_2015D",         dirs['Andrew']+"2015/stenson/tauToElectronBackground")
    tauBkgdEstimate.addChannel  ("TagProbePass1",    "ZtoTauToEleProbeTrk",              "SingleEle_rereco_2015D",  dirs['Andrew']+"2015/stenson/tauToElectronBackground")
    tauBkgdEstimate.addChannel  ("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter",  "SingleEle_2015D",         dirs['Andrew']+"2015/stenson/sameSign/skims/tauToElectronBackground")
    tauBkgdEstimate.addChannel  ("TagPt35",          "TauTagPt55",                       "Tau_2015D",               dirs['Andrew']+"2015/tauBackground_nCtrl_new")

    #tauBkgdEstimate.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",             "Tau_2015D",               dirs['Andrew']+"2015/tauBackground_nCtrl_new")
    #tauBkgdEstimate.addChannel  ("TrigEffDenom",    "ElectronTagPt55",               "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")
    #tauBkgdEstimate.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",        "SingleEle_2015D",         dirs['Andrew']+"2015/electronBackground_nCtrl_new")

    tauBkgdEstimate.addUseHistogramsForPpassMetTriggers (True)
    tauBkgdEstimate.addRebinFactor (8)
    tauBkgdEstimate.addChannel  ("TagPt35MetTrig",  "TauTagPt55",  "Tau_2015D",  dirs['Andrew']+"2015/tauBackground_passesMETTriggers_new")

    print "********************************************************************************"

    nEstTau.append( tauBkgdEstimate.printNest () )

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

# print sums
if background == "ALL":
    print "********************************************************************************"
    nLeptons = nEstElectron[0] + nEstMuon[0] + nEstTau[0]
    nTotal = nLeptons + nEstFake[0]
    print "Total background from leptons (2015):", nLeptons
    print "Total background from fake tracks (2015):", nEstFake[0]
    print "********************************************************************************"
    print "Total background (2015):", nTotal
    print "********************************************************************************"
    print "\n\n"

    nElectrons = nEstElectron[0]
    nMuons = nEstMuon[0]
    nTaus = nEstTau[0]
    nFakes = nEstFake[0]

    x = array ("d"); ex = array ("d")
    electron   =  array  ("d");  muon   =  array  ("d");  tau   =  array  ("d");  fake   =  array  ("d")
    eElectron   =  array  ("d");  eMuon   =  array  ("d");  eTau   =  array  ("d");  eFake   =  array  ("d")

    runPeriodsToPlot = ["D"]
    i = 0.0

    for runPeriod in runPeriodsToPlot:
        x.append (i); ex.append (0.0); i += 1.0

        electron.append  ((nEstElectron[runPeriods.index  (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).centralValue ())
        muon.append      ((nEstMuon[runPeriods.index      (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).centralValue ())
        tau.append       ((nEstTau[runPeriods.index       (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).centralValue ())
        fake.append      ((nEstFake[runPeriods.index      (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).centralValue ())

        eElectron.append  ((nEstElectron[runPeriods.index  (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).maxUncertainty ())
        eMuon.append      ((nEstMuon[runPeriods.index      (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).maxUncertainty ())
        eTau.append       ((nEstTau[runPeriods.index       (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).maxUncertainty ())
        eFake.append      ((nEstFake[runPeriods.index      (runPeriod)]  /  lumi["MET_2015"  +  runPeriod]).maxUncertainty ())

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
