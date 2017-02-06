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
    print "performing fake track background estimate in search region (2016DEFGH)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2016DEFGH.root", "recreate")

    fakeTrackBkgdEstimateDEFGH = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimateDEFGH.addTFile (fout)
    fakeTrackBkgdEstimateDEFGH.addTCanvas (canvas)
    fakeTrackBkgdEstimateDEFGH.addLuminosityInInvFb (lumi["MET_2016DEFGH"] / 1000.)
    fakeTrackBkgdEstimateDEFGH.addChannel  ("ZtoLL",        "ZtoMuMu",                                  "SingleMu_2016DEFGH",  dirs['Brian']+"2016/zToMuMu_noSkim")
    fakeTrackBkgdEstimateDEFGH.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrkNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",  dirs['Brian']+"2016/fakeTrackBackground_v2")
    fakeTrackBkgdEstimateDEFGH.addChannel  ("Basic",        "BasicSelection",                           "MET_2016DEFGH",       dirs['Andrew']+"2016/basicSelection")

    print "********************************************************************************"

    (nEstFakeDEFGH, nEstFakeErrorDEFGH) = fakeTrackBkgdEstimateDEFGH.printNest ()

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
    print "performing electron background estimate in search region (2016DEFGH)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("electronBkgdEstimate_2016DEFGH.root", "recreate")

    electronBkgdEstimateDEFGH = LeptonBkgdEstimate ("electron")
    electronBkgdEstimateDEFGH.addTFile (fout)
    electronBkgdEstimateDEFGH.addTCanvas (canvas)
    electronBkgdEstimateDEFGH.addPrescaleFactor (lumi["MET_2016DEFGH"] / lumi["SingleElectron_2016DEFGH"])
    electronBkgdEstimateDEFGH.addTagProbePassScaleFactor (lumi["SingleElectron_2016DEFGH"] / (lumi["SingleElectron_2016DEFGH"] - lumi["SingleElectron_2016F"]))
    electronBkgdEstimateDEFGH.addLuminosityInInvFb (lumi["MET_2016DEFGH"] / 1000.)
    electronBkgdEstimateDEFGH.addLuminosityLabel (str (round (lumi["SingleElectron_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronBkgdEstimateDEFGH.addPlotLabel ("SingleElectron 2016D-G")
    electronBkgdEstimateDEFGH.addMetCut (100.0)
    electronBkgdEstimateDEFGH.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016DEFGH",         dirs['Brian']+"2016/electronBackground_v2")
    electronBkgdEstimateDEFGH.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016DEFGH_rereco",  dirs['Andrew']+"2016/electronBackground")
    electronBkgdEstimateDEFGH.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016DEFGH",         dirs['Brian']+"2016/electronBackground_v2")
    electronBkgdEstimateDEFGH.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016DEFGH",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstElectronDEFGH, nEstElectronErrorDEFGH) = electronBkgdEstimateDEFGH.printNest ()

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
    print "performing muon background estimate in search region (2016DEFGH)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("muonBkgdEstimate_2016DEFGH.root", "recreate")

    muonBkgdEstimateDEFGH = LeptonBkgdEstimate ("muon")
    muonBkgdEstimateDEFGH.addTFile (fout)
    muonBkgdEstimateDEFGH.addTCanvas (canvas)
    muonBkgdEstimateDEFGH.addPrescaleFactor (lumi["MET_2016DEFGH"] / lumi["SingleMuon_2016DEFGH"])
    muonBkgdEstimateDEFGH.addTagProbePassScaleFactor (lumi["SingleMuon_2016DEFGH"] / (lumi["SingleMuon_2016DEFGH"] - lumi["SingleMuon_2016D"]))
    muonBkgdEstimateDEFGH.addLuminosityInInvFb (lumi["MET_2016DEFGH"] / 1000.)
    muonBkgdEstimateDEFGH.addLuminosityLabel (str (round (lumi["SingleMuon_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    muonBkgdEstimateDEFGH.addPlotLabel ("SingleMuon 2016D-G")
    muonBkgdEstimateDEFGH.addMetCut (100.0)
    muonBkgdEstimateDEFGH.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",         dirs['Brian']+"2016/muonBackground_v2")
    muonBkgdEstimateDEFGH.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoElectronMuonFiducialCuts",             "SingleMu_2016DEFGH_rereco",  dirs['Andrew']+"2016/muonBackground")
    muonBkgdEstimateDEFGH.addChannel  ("TagPt35",         "MuonTagPt55NoElectronMuonFiducialCuts",             "SingleMu_2016DEFGH",         dirs['Brian']+"2016/muonBackground_v2")
    muonBkgdEstimateDEFGH.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrigNoElectronMuonFiducialCuts",      "SingleMu_2016DEFGH",         dirs['Brian']+"2016/muonBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstMuonDEFGH, nEstMuonErrorDEFGH) = muonBkgdEstimateDEFGH.printNest ()

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
    tauBkgdEstimateBC.addRebinFactor (4)
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
    print "performing tau background estimate in search region (2016DEFGH)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("tauBkgdEstimate_2016DEFGH.root", "recreate")

    tauBkgdEstimateDEFGH = LeptonBkgdEstimate ("tau")
    tauBkgdEstimateDEFGH.addTFile (fout)
    tauBkgdEstimateDEFGH.addTCanvas (canvas)
    tauBkgdEstimateDEFGH.addPrescaleFactor (lumi["MET_2016DEFGH"] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"])
    tauBkgdEstimateDEFGH.addTagProbePassScaleFactor (lumi["SingleMuon_2016DEFGH"] / (lumi["SingleMuon_2016DEFGH"] - lumi["SingleMuon_2016D"]))
    tauBkgdEstimateDEFGH.addTagProbePass1ScaleFactor (lumi["SingleElectron_2016DEFGH"] / (lumi["SingleElectron_2016DEFGH"] - lumi["SingleElectron_2016F"]))
    tauBkgdEstimateDEFGH.addLuminosityInInvFb (lumi["MET_2016DEFGH"] / 1000.)
    tauBkgdEstimateDEFGH.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    tauBkgdEstimateDEFGH.addPlotLabel ("Tau 2016D-G")
    tauBkgdEstimateDEFGH.addMetCut (100.0)
    tauBkgdEstimateDEFGH.addRebinFactor (4)
    tauBkgdEstimateDEFGH.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",   "SingleMu_2016DEFGH",         dirs['Brian']+"2016/muonBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoElectronMuonFiducialCuts",              "SingleMu_2016EFG_rereco",   dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016DEG_rereco",  dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016DEFGH",              dirs['Brian']+"2016/tauBackground_v2")
    #tauBkgdEstimateDEFGH.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016DEFGH",              dirs['Brian']+"2016/tauBackground_v2NoTrig")
    tauBkgdEstimateDEFGH.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstTauDEFGH, nEstTauErrorDEFGH) = tauBkgdEstimateDEFGH.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"


if background == "ALL":

    print "********************************************************************************"
    nEstElectron  =  nEstElectronBC  +  nEstElectronDEFGH
    nEstMuon      =  nEstMuonBC      +  nEstMuonDEFGH
    nEstTau       =  nEstTauBC       +  nEstTauDEFGH
    nEstElectronError  =  math.hypot  (nEstElectronErrorBC,  nEstElectronErrorDEFGH)
    nEstMuonError      =  math.hypot  (nEstMuonErrorBC,      nEstMuonErrorDEFGH)
    nEstTauError       =  math.hypot  (nEstTauErrorBC,       nEstTauErrorDEFGH)

    nEstBC    =  nEstElectronBC    +  nEstMuonBC    +  nEstTauBC
    nEstDEFGH  =  nEstElectronDEFGH  +  nEstMuonDEFGH  +  nEstTauDEFGH
    nEst      =  nEstElectron      +  nEstMuon      +  nEstTau
    nEstErrorBC    =  math.hypot  (math.hypot  (nEstElectronErrorBC,    nEstMuonErrorBC),    nEstTauErrorBC)
    nEstErrorDEFGH  =  math.hypot  (math.hypot  (nEstElectronErrorDEFGH,  nEstMuonErrorDEFGH),  nEstTauErrorDEFGH)
    nEstError      =  math.hypot  (math.hypot  (nEstElectronError,      nEstMuonError),      nEstTauError)
    print "total background from leptons (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
    print "total background from leptons (2016DEFGH): " + str (nEstDEFGH) + " +- " + str (nEstErrorDEFGH)
    print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
    print "********************************************************************************"

    print "\n\n"

    print "********************************************************************************"
    nEstBC    +=  nEstFakeBC
    nEstDEFGH  +=  nEstFakeDEFGH
    nEst      +=  nEstFake
    nEstErrorBC    =  math.hypot  (nEstErrorBC,    nEstFakeErrorBC)
    nEstErrorDEFGH  =  math.hypot  (nEstErrorDEFGH,  nEstFakeErrorDEFGH)
    nEstError      =  math.hypot  (nEstError,      nEstFakeError)
    print "total background (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
    print "total background (2016DEFGH): " + str (nEstDEFGH) + " +- " + str (nEstErrorDEFGH)
    print "total background: " + str (nEst) + " +- " + str (nEstError)
    print "********************************************************************************"
