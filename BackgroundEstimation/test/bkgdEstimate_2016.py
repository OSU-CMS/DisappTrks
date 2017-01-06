#!/usr/bin/env python

import math
from DisappTrks.BackgroundEstimation.bkgdEstimate import *
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
    print "performing fake track background estimate in search region"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2016.root", "recreate")

    fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimate.addTFile (fout)
    fakeTrackBkgdEstimate.addTCanvas (canvas)
    fakeTrackBkgdEstimate.addLuminosityInInvFb (lumi["MET_2016"] / 1000.)
    fakeTrackBkgdEstimate.addChannel  ("ZtoLL",        "ZtoMuMu",                                  "SingleMu_2016",  dirs['Brian']+"2016/zToMuMu_noSkim")
    fakeTrackBkgdEstimate.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrkNoElectronMuonFiducialCuts",  "SingleMu_2016",  dirs['Brian']+"2016/fakeTrackBackground_v2")
    fakeTrackBkgdEstimate.addChannel  ("Basic",        "BasicSelection",                           "MET_2016",       dirs['Andrew']+"2016/basicSelection")

    print "********************************************************************************"

    (nEstFake, nEstFakeError) = fakeTrackBkgdEstimate.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing fake track background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2016BC.root", "recreate")

    fakeTrackBkgdEstimateBC = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimateBC.addTFile (fout)
    fakeTrackBkgdEstimateBC.addTCanvas (canvas)
    fakeTrackBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"] / 1000.)
    fakeTrackBkgdEstimateBC.addChannel  ("ZtoLL",        "ZtoMuMu",                                  "SingleMu_2016BC",  dirs['Brian']+"2016/zToMuMu_noSkim")
    fakeTrackBkgdEstimateBC.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrkNoElectronMuonFiducialCuts",  "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
    fakeTrackBkgdEstimateBC.addChannel  ("Basic",        "BasicSelection",                           "MET_2016BC",       dirs['Andrew']+"2016/basicSelection")

    print "********************************************************************************"

    (nEstFakeBC, nEstFakeErrorBC) = fakeTrackBkgdEstimateBC.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing fake track background estimate in search region (2016DEFG)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2016DEFG.root", "recreate")

    fakeTrackBkgdEstimateDEFG = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimateDEFG.addTFile (fout)
    fakeTrackBkgdEstimateDEFG.addTCanvas (canvas)
    fakeTrackBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"] / 1000.)
    fakeTrackBkgdEstimateDEFG.addChannel  ("ZtoLL",        "ZtoMuMu",                                  "SingleMu_2016DEFG",  dirs['Brian']+"2016/zToMuMu_noSkim")
    fakeTrackBkgdEstimateDEFG.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrkNoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",  dirs['Brian']+"2016/fakeTrackBackground_v2")
    fakeTrackBkgdEstimateDEFG.addChannel  ("Basic",        "BasicSelection",                           "MET_2016DEFG",       dirs['Andrew']+"2016/basicSelection")

    print "********************************************************************************"

    (nEstFakeDEFG, nEstFakeErrorDEFG) = fakeTrackBkgdEstimateDEFG.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "ELECTRON" or background == "ALL":

    print "********************************************************************************"
    print "performing electron background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("electronBkgdEstimate_2016BC.root", "recreate")

    electronBkgdEstimateBC = LeptonBkgdEstimate ("electron")
    electronBkgdEstimateBC.addTFile (fout)
    electronBkgdEstimateBC.addTCanvas (canvas)
    electronBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleElectron_2016BC"])
    electronBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"] / 1000.)
    electronBkgdEstimateBC.addLuminosityLabel (str (round (lumi["SingleElectron_2016BC"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronBkgdEstimateBC.addPlotLabel ("SingleElectron 2016B+C")
    electronBkgdEstimateBC.addMetCut (100.0)
    electronBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
    electronBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016BC_rereco",  dirs['Andrew']+"2016/electronBackground")
    electronBkgdEstimateBC.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
    electronBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstElectronBC, nEstElectronErrorBC) = electronBkgdEstimateBC.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing electron background estimate in search region (2016DEFG)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("electronBkgdEstimate_2016DEFG.root", "recreate")

    electronBkgdEstimateDEFG = LeptonBkgdEstimate ("electron")
    electronBkgdEstimateDEFG.addTFile (fout)
    electronBkgdEstimateDEFG.addTCanvas (canvas)
    electronBkgdEstimateDEFG.addPrescaleFactor (lumi["MET_2016DEFG"] / lumi["SingleElectron_2016DEFG"])
    electronBkgdEstimateDEFG.addTagProbePassScaleFactor (lumi["SingleElectron_2016DEFG"] / (lumi["SingleElectron_2016DEFG"] - lumi["SingleElectron_2016F"]))
    electronBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"] / 1000.)
    electronBkgdEstimateDEFG.addLuminosityLabel (str (round (lumi["SingleElectron_2016DEFG"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronBkgdEstimateDEFG.addPlotLabel ("SingleElectron 2016D-G")
    electronBkgdEstimateDEFG.addMetCut (100.0)
    electronBkgdEstimateDEFG.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016DEFG",         dirs['Brian']+"2016/electronBackground_v2")
    electronBkgdEstimateDEFG.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016DEFG_rereco",  dirs['Andrew']+"2016/electronBackground")
    electronBkgdEstimateDEFG.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016DEFG",         dirs['Brian']+"2016/electronBackground_v2")
    electronBkgdEstimateDEFG.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016DEFG",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstElectronDEFG, nEstElectronErrorDEFG) = electronBkgdEstimateDEFG.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "MUON" or background == "ALL":

    print "********************************************************************************"
    print "performing muon background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("muonBkgdEstimate_2016BC.root", "recreate")

    muonBkgdEstimateBC = LeptonBkgdEstimate ("muon")
    muonBkgdEstimateBC.addTFile (fout)
    muonBkgdEstimateBC.addTCanvas (canvas)
    muonBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleMuon_2016BC"])
    muonBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"] / 1000.)
    muonBkgdEstimateBC.addLuminosityLabel (str (round (lumi["SingleMuon_2016BC"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    muonBkgdEstimateBC.addPlotLabel ("SingleMuon 2016B+C")
    muonBkgdEstimateBC.addMetCut (100.0)
    muonBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleMu_2016BC",         dirs['Brian']+"2016/muonBackground_v2")
    muonBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoElectronMuonFiducialCuts",             "SingleMu_2016BC_rereco",  dirs['Andrew']+"2016/muonBackground")
    muonBkgdEstimateBC.addChannel  ("TagPt35",         "MuonTagPt55NoElectronMuonFiducialCuts",             "SingleMu_2016BC",         dirs['Brian']+"2016/muonBackground_v2")
    muonBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrigNoElectronMuonFiducialCuts",      "SingleMu_2016BC",         dirs['Brian']+"2016/muonBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstMuonBC, nEstMuonErrorBC) = muonBkgdEstimateBC.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing muon background estimate in search region (2016DEFG)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("muonBkgdEstimate_2016DEFG.root", "recreate")

    muonBkgdEstimateDEFG = LeptonBkgdEstimate ("muon")
    muonBkgdEstimateDEFG.addTFile (fout)
    muonBkgdEstimateDEFG.addTCanvas (canvas)
    muonBkgdEstimateDEFG.addPrescaleFactor (lumi["MET_2016DEFG"] / lumi["SingleMuon_2016DEFG"])
    muonBkgdEstimateDEFG.addTagProbePassScaleFactor (lumi["SingleMuon_2016DEFG"] / (lumi["SingleMuon_2016DEFG"] - lumi["SingleMuon_2016D"]))
    muonBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"] / 1000.)
    muonBkgdEstimateDEFG.addLuminosityLabel (str (round (lumi["SingleMuon_2016DEFG"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    muonBkgdEstimateDEFG.addPlotLabel ("SingleMuon 2016D-G")
    muonBkgdEstimateDEFG.addMetCut (100.0)
    muonBkgdEstimateDEFG.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",         dirs['Brian']+"2016/muonBackground_v2")
    muonBkgdEstimateDEFG.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoElectronMuonFiducialCuts",             "SingleMu_2016DEFG_rereco",  dirs['Andrew']+"2016/muonBackground")
    muonBkgdEstimateDEFG.addChannel  ("TagPt35",         "MuonTagPt55NoElectronMuonFiducialCuts",             "SingleMu_2016DEFG",         dirs['Brian']+"2016/muonBackground_v2")
    muonBkgdEstimateDEFG.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrigNoElectronMuonFiducialCuts",      "SingleMu_2016DEFG",         dirs['Brian']+"2016/muonBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstMuonDEFG, nEstMuonErrorDEFG) = muonBkgdEstimateDEFG.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

if background == "TAU" or background == "ALL":

    print "********************************************************************************"
    print "performing tau background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("tauBkgdEstimate_2016BC.root", "recreate")

    tauBkgdEstimateBC = LeptonBkgdEstimate ("tau")
    tauBkgdEstimateBC.addTFile (fout)
    tauBkgdEstimateBC.addTCanvas (canvas)
    tauBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"])
    tauBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"] / 1000.)
    tauBkgdEstimateBC.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    tauBkgdEstimateBC.addPlotLabel ("Tau 2016B+C")
    tauBkgdEstimateBC.addMetCut (100.0)
    tauBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",   "SingleMu_2016BC",          dirs['Brian']+"2016/muonBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoElectronMuonFiducialCuts",              "SingleMu_2016BC_rereco",   dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016BC_rereco",  dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016BC",               dirs['Brian']+"2016/tauBackground_v2")
    #tauBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016BC",               dirs['Brian']+"2016/tauBackground_v2NoTrig")
    tauBkgdEstimateBC.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstTauBC, nEstTauErrorBC) = tauBkgdEstimateBC.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing tau background estimate in search region (2016DEFG)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("tauBkgdEstimate_2016DEFG.root", "recreate")

    tauBkgdEstimateDEFG = LeptonBkgdEstimate ("tau")
    tauBkgdEstimateDEFG.addTFile (fout)
    tauBkgdEstimateDEFG.addTCanvas (canvas)
    tauBkgdEstimateDEFG.addPrescaleFactor (lumi["MET_2016DEFG"] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFG"])
    tauBkgdEstimateDEFG.addTagProbePassScaleFactor (lumi["SingleMuon_2016DEFG"] / (lumi["SingleMuon_2016DEFG"] - lumi["SingleMuon_2016D"]))
    tauBkgdEstimateDEFG.addTagProbePass1ScaleFactor (lumi["SingleElectron_2016DEFG"] / (lumi["SingleElectron_2016DEFG"] - lumi["SingleElectron_2016F"]))
    tauBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"] / 1000.)
    tauBkgdEstimateDEFG.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFG"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    tauBkgdEstimateDEFG.addPlotLabel ("Tau 2016D-G")
    tauBkgdEstimateDEFG.addMetCut (100.0)
    tauBkgdEstimateDEFG.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",   "SingleMu_2016DEFG",         dirs['Brian']+"2016/muonBackground_v2")
    tauBkgdEstimateDEFG.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoElectronMuonFiducialCuts",              "SingleMu_2016EFG_rereco",   dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFG.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016DEFG",        dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateDEFG.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016DEG_rereco",  dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFG.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016DEFG",              dirs['Brian']+"2016/tauBackground_v2")
    #tauBkgdEstimateDEFG.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016DEFG",              dirs['Brian']+"2016/tauBackground_v2NoTrig")
    tauBkgdEstimateDEFG.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016DEFG",        dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateDEFG.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016DEFG",        dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstTauDEFG, nEstTauErrorDEFG) = tauBkgdEstimateDEFG.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"


if background == "ALL":

    print "********************************************************************************"
    nEstElectron  =  nEstElectronBC  +  nEstElectronDEFG
    nEstMuon      =  nEstMuonBC      +  nEstMuonDEFG
    nEstTau       =  nEstTauBC       +  nEstTauDEFG
    nEstElectronError  =  math.hypot  (nEstElectronErrorBC,  nEstElectronErrorDEFG)
    nEstMuonError      =  math.hypot  (nEstMuonErrorBC,      nEstMuonErrorDEFG)
    nEstTauError       =  math.hypot  (nEstTauErrorBC,       nEstTauErrorDEFG)

    nEstBC    =  nEstElectronBC    +  nEstMuonBC    +  nEstTauBC
    nEstDEFG  =  nEstElectronDEFG  +  nEstMuonDEFG  +  nEstTauDEFG
    nEst      =  nEstElectron      +  nEstMuon      +  nEstTau
    nEstErrorBC    =  math.hypot  (math.hypot  (nEstElectronErrorBC,    nEstMuonErrorBC),    nEstTauErrorBC)
    nEstErrorDEFG  =  math.hypot  (math.hypot  (nEstElectronErrorDEFG,  nEstMuonErrorDEFG),  nEstTauErrorDEFG)
    nEstError      =  math.hypot  (math.hypot  (nEstElectronError,      nEstMuonError),      nEstTauError)
    print "total background from leptons (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
    print "total background from leptons (2016DEFG): " + str (nEstDEFG) + " +- " + str (nEstErrorDEFG)
    print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
    print "********************************************************************************"

    print "\n\n"

    print "********************************************************************************"
    nEstBC    +=  nEstFakeBC
    nEstDEFG  +=  nEstFakeDEFG
    nEst      +=  nEstFake
    nEstErrorBC    =  math.hypot  (nEstErrorBC,    nEstFakeErrorBC)
    nEstErrorDEFG  =  math.hypot  (nEstErrorDEFG,  nEstFakeErrorDEFG)
    nEstError      =  math.hypot  (nEstError,      nEstFakeError)
    print "total background (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
    print "total background (2016DEFG): " + str (nEstDEFG) + " +- " + str (nEstErrorDEFG)
    print "total background: " + str (nEst) + " +- " + str (nEstError)
    print "********************************************************************************"
