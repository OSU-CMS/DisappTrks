#!/usr/bin/env python

import math
from DisappTrks.BackgroundEstimation.bkgdEstimate import *
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

nEstFake = []
nEstElectron = []
nEstMuon = []
nEstTau = []

for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        print "********************************************************************************"
        print "performing fake track background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
        fakeTrackBkgdEstimate.addTFile (fout)
        fakeTrackBkgdEstimate.addTCanvas (canvas)
        fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        fakeTrackBkgdEstimate.addChannel  ("ZtoLL",        "ZtoMuMu",        "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final/zToMuMu")
        fakeTrackBkgdEstimate.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",  "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_rereco/fakeTrackBackground_v2")
        fakeTrackBkgdEstimate.addChannel  ("Basic",        "BasicSelection", "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final/basicSelection")

        print "********************************************************************************"

        nEstFake.append( fakeTrackBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "ELECTRON" or background == "ALL":

        print "********************************************************************************"
        print "performing electron background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("electronBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        electronBkgdEstimate = LeptonBkgdEstimate ("electron")
        electronBkgdEstimate.addTFile (fout)
        electronBkgdEstimate.addTCanvas (canvas)
        electronBkgdEstimate.addPrescaleFactor (lumi["MET_2016" + runPeriod] / lumi["SingleElectron_2016" + runPeriod])
        electronBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        electronBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleElectron_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        electronBkgdEstimate.addPlotLabel ("SingleElectron 2016" + runPeriod)
        electronBkgdEstimate.addMetCut (100.0)
        electronBkgdEstimate.addChannel  ("TagProbe",       "ZtoEleProbeTrkWithZCuts", "SingleEle_2016" + runPeriod,              dirs['Brian']+"2016_rereco/electronBackgrounds")
        electronBkgdEstimate.addChannel  ("TagProbePass",   "ZtoEleDisTrk",            "SingleEle_2016" + runPeriod + "_rereco",  dirs['Brian']+"2016_rereco/electronBackgrounds")
        electronBkgdEstimate.addChannel  ("TagPt35",        "ElectronTagPt55",         "SingleEle_2016" + runPeriod,              dirs['Brian']+"2016_rereco/eleTagPt55")
        electronBkgdEstimate.addChannel  ("TagPt35MetTrig", "ElectronTagPt55MetTrig",  "SingleEle_2016" + runPeriod,              dirs['Brian']+"2016_rereco/eleTagPt55")

        print "********************************************************************************"

        nEstElectron.append( electronBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "MUON" or background == "ALL":

        print "********************************************************************************"
        print "performing muon background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("muonBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        muonBkgdEstimate = LeptonBkgdEstimate ("muon")
        muonBkgdEstimate.addTFile (fout)
        muonBkgdEstimate.addTCanvas (canvas)
        muonBkgdEstimate.addPrescaleFactor (lumi["MET_2016" + runPeriod] / lumi["SingleMuon_2016" + runPeriod])
        muonBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        muonBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleMuon_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        muonBkgdEstimate.addPlotLabel ("SingleMuon 2016" + runPeriod)
        muonBkgdEstimate.addMetCut (100.0)
        muonBkgdEstimate.addChannel  ("TagProbe",       "ZtoMuProbeTrkWithZCuts", "SingleMu_2016" + runPeriod,             dirs['Andrew']+"2016_final/muonBackground")
        muonBkgdEstimate.addChannel  ("TagProbePass",   "ZtoMuDisTrk",            "SingleMu_2016" + runPeriod + "_rereco", dirs['Andrew']+"2016_final/muonBackground")
        muonBkgdEstimate.addChannel  ("TagPt35",        "MuonTagPt55",            "SingleMu_2016" + runPeriod,             dirs['Andrew']+"2016_final/muonBackground")
        muonBkgdEstimate.addChannel  ("TagPt35MetTrig", "MuonTagPt55MetTrig",     "SingleMu_2016" + runPeriod,             dirs['Andrew']+"2016_final/muonBackground")

        print "********************************************************************************"

        nEstMuon.append( muonBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "TAU" or background == "ALL":

        print "********************************************************************************"
        print "performing tau background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("tauBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        tauBkgdEstimate = LeptonBkgdEstimate ("tau")
        tauBkgdEstimate.addTFile (fout)
        tauBkgdEstimate.addTCanvas (canvas)
        tauBkgdEstimate.addPrescaleFactor (lumi["MET_2016" + runPeriod] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016" + runPeriod])
        tauBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        tauBkgdEstimate.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        tauBkgdEstimate.addPlotLabel ("Tau 2016" + runPeriod)
        tauBkgdEstimate.addMetCut (100.0)
        tauBkgdEstimate.addRebinFactor (4)
        tauBkgdEstimate.addChannel  ("TagProbe",       "ZtoTauToMuProbeTrkWithZCuts",  "SingleMu_2016" + runPeriod,         dirs['Andrew']+"2016_final/muonBackground")
        tauBkgdEstimate.addChannel  ("TagProbePass",   "ZtoTauToMuDisTrk",             "SingleMu_2016" + runPeriod + "_rereco",  dirs['Andrew']+"2016_final/muonBackground")
        tauBkgdEstimate.addChannel  ("TagProbe1",      "ZtoTauToEleProbeTrkWithZCuts", "SingleEle_2016" + runPeriod,        dirs['Brian']+"2016_rereco/electronBackgrounds")
        tauBkgdEstimate.addChannel  ("TagProbePass1",  "ZtoTauToEleDisTrk",            "SingleEle_2016" + runPeriod + "_rereco", dirs['Brian']+"2016_rereco/electronBackgrounds")
        tauBkgdEstimate.addChannel  ("TagPt35",        "TauTagPt55",                   "Tau_2016" + runPeriod,              dirs['Andrew']+"2016_final/tauBackground")
        #tauBkgdEstimate.addChannel  ("TagPt35MetTrig", "TauTagPt55MetTrig",            "Tau_2016" + runPeriod,              dirs['Andrew']+"2016_final/tauBackground")
        tauBkgdEstimate.addChannel  ("TrigEffDenom",   "ElectronTagPt55",              "SingleEle_2016" + runPeriod,        dirs['Brian']+"2016_rereco/eleTagPt55")
        tauBkgdEstimate.addChannel  ("TrigEffNumer",   "ElectronTagPt55MetTrig",       "SingleEle_2016" + runPeriod,        dirs['Brian']+"2016_rereco/eleTagPt55")

        print "********************************************************************************"

        nEstTau.append ( tauBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

# print sums
if background == "ALL":
    for iRunPeriod in len(runPeriods):
        print "********************************************************************************"
        nLeptons = nEstElectron[iRunPeriod][0] + nEstMuon[iRunPeriod][0] + nEstTau[iRunPeriod][0]
        nLeptonsError = math.sqrt(
            nEstElectron[iRunPeriod][1]**2 +
            nEstMuon[iRunPeriod][1]**2 +
            nEstTau[iRunPeriod][1]**2
            )
        nTotal = nLeptons + nEstFake[iRunPeriod][0]
        nTotalError = math.hypot(nLeptonsError, nEstFake[iRunPeriod][1])
        print "Total background from leptons (2016", runPeriods[iRunPeriod], "): ", nLeptons, " +/- ", nLeptonsError
        print "Total background from fake tracks (2016",runPeriods[iRunPeriod], "): ", nEstFake[iRunPeriod][0], " +/- ", nEstFake[iRunPeriod][1]
        print "********************************************************************************"
        print "Total background (2016", runPeriods[iRunPeriod], "): ", nTotal, " +/- ", nTotalError
        print "********************************************************************************"
        print "\n\n"
