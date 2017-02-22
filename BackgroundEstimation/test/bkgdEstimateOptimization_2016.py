#!/usr/bin/env python

import math
from DisappTrks.BackgroundEstimation.bkgdEstimate import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile, TGraph
import os

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

all_nBackground = []
all_nBackgroundError = []

all_nSignal = []
all_nSignalError = []

all_fiducialCuts = []

for iCut in range(1, 50):

    fiducialCut = iCut / 10.0

    print "********************************************************************************"
    print "performing fake track background estimate in search region"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackBkgdEstimate_2016.root", "recreate")

    fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
    fakeTrackBkgdEstimate.setFiducialMapCuts (fiducialCut, fiducialCut)
    fakeTrackBkgdEstimate.addTFile (fout)
    fakeTrackBkgdEstimate.addTCanvas (canvas)
    fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016"])
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
    fakeTrackBkgdEstimateBC.setFiducialMapCuts (fiducialCut, fiducialCut)
    fakeTrackBkgdEstimateBC.addTFile (fout)
    fakeTrackBkgdEstimateBC.addTCanvas (canvas)
    fakeTrackBkgdEstimateBC.addLuminosityInInvPb (lumi["MET_2016BC"])
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
    fakeTrackBkgdEstimateDEFGH.setFiducialMapCuts (fiducialCut, fiducialCut)
    fakeTrackBkgdEstimateDEFGH.addTFile (fout)
    fakeTrackBkgdEstimateDEFGH.addTCanvas (canvas)
    fakeTrackBkgdEstimateDEFGH.addLuminosityInInvPb (lumi["MET_2016DEFGH"])
    fakeTrackBkgdEstimateDEFGH.addChannel  ("ZtoLL",        "ZtoMuMu",                                  "SingleMu_2016DEFGH",  dirs['Brian']+"2016/zToMuMu_noSkim")
    fakeTrackBkgdEstimateDEFGH.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrkNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",  dirs['Brian']+"2016/fakeTrackBackground_v2")
    fakeTrackBkgdEstimateDEFGH.addChannel  ("Basic",        "BasicSelection",                           "MET_2016DEFGH",       dirs['Andrew']+"2016/basicSelection")

    print "********************************************************************************"

    (nEstFakeDEFGH, nEstFakeErrorDEFGH) = fakeTrackBkgdEstimateDEFGH.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "performing electron background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("electronBkgdEstimate_2016BC.root", "recreate")

    electronBkgdEstimateBC = LeptonBkgdEstimate ("electron")
    electronBkgdEstimateBC.setFiducialMapCuts (fiducialCut, fiducialCut)
    electronBkgdEstimateBC.addTFile (fout)
    electronBkgdEstimateBC.addTCanvas (canvas)
    electronBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleElectron_2016BC"])
    electronBkgdEstimateBC.addLuminosityInInvPb (lumi["MET_2016BC"])
    electronBkgdEstimateBC.addLuminosityLabel ("8.53 fb^{-1} (13 TeV)")
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
    electronBkgdEstimateDEFGH.setFiducialMapCuts (fiducialCut, fiducialCut)
    electronBkgdEstimateDEFGH.addTFile (fout)
    electronBkgdEstimateDEFGH.addTCanvas (canvas)
    electronBkgdEstimateDEFGH.addPrescaleFactor (lumi["MET_2016DEFGH"] / lumi["SingleElectron_2016DEFGH"])
    electronBkgdEstimateDEFGH.addTagProbePassScaleFactor (lumi["SingleElectron_2016DEFGH"] / (lumi["SingleElectron_2016DEFGH"] - lumi["SingleElectron_2016F"]))
    electronBkgdEstimateDEFGH.addLuminosityInInvPb (lumi["MET_2016DEFGH"])
    electronBkgdEstimateDEFGH.addLuminosityLabel ("4.35 fb^{-1} (13 TeV)")
    electronBkgdEstimateDEFGH.addPlotLabel ("SingleElectron 2016D")
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

    print "********************************************************************************"
    print "performing muon background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("muonBkgdEstimate_2016BC.root", "recreate")

    muonBkgdEstimateBC = LeptonBkgdEstimate ("muon")
    muonBkgdEstimateBC.setFiducialMapCuts (fiducialCut, fiducialCut)
    muonBkgdEstimateBC.addTFile (fout)
    muonBkgdEstimateBC.addTCanvas (canvas)
    muonBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleMuon_2016BC"])
    muonBkgdEstimateBC.addLuminosityInInvPb (lumi["MET_2016BC"])
    muonBkgdEstimateBC.addLuminosityLabel ("8.52 fb^{-1} (13 TeV)")
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
    muonBkgdEstimateDEFGH.setFiducialMapCuts (fiducialCut, fiducialCut)
    muonBkgdEstimateDEFGH.addTFile (fout)
    muonBkgdEstimateDEFGH.addTCanvas (canvas)
    muonBkgdEstimateDEFGH.addPrescaleFactor (lumi["MET_2016DEFGH"] / lumi["SingleMuon_2016DEFGH"])
    muonBkgdEstimateDEFGH.addTagProbePassScaleFactor (lumi["SingleMuon_2016DEFGH"] / (lumi["SingleMuon_2016DEFGH"] - lumi["SingleMuon_2016D"]))
    muonBkgdEstimateDEFGH.addLuminosityInInvPb (lumi["MET_2016DEFGH"])
    muonBkgdEstimateDEFGH.addLuminosityLabel ("4.35 fb^{-1} (13 TeV)")
    muonBkgdEstimateDEFGH.addPlotLabel ("SingleMuon 2016D")
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

    print "********************************************************************************"
    print "performing tau background estimate in search region (2016BC)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("tauBkgdEstimate_2016BC.root", "recreate")

    tauBkgdEstimateBC = LeptonBkgdEstimate ("tau")
    tauBkgdEstimateBC.setFiducialMapCuts (fiducialCut, fiducialCut)
    tauBkgdEstimateBC.addTFile (fout)
    tauBkgdEstimateBC.addTCanvas (canvas)
    tauBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"])
    tauBkgdEstimateBC.addLuminosityInInvPb (lumi["MET_2016BC"])
    tauBkgdEstimateBC.addLuminosityLabel ("0.814 fb^{-1} (13 TeV)")
    tauBkgdEstimateBC.addPlotLabel ("Tau 2016B+C")
    tauBkgdEstimateBC.addMetCut (100.0)
    tauBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",   "SingleMu_2016BC",          dirs['Brian']+"2016/muonBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoElectronMuonFiducialCuts",              "SingleMu_2016BC_rereco",   dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016BC_rereco",  dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016BC",               dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016BC",               dirs['Brian']+"2016/tauBackground_v2NoTrig")
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
    tauBkgdEstimateDEFGH.setFiducialMapCuts (fiducialCut, fiducialCut)
    tauBkgdEstimateDEFGH.addTFile (fout)
    tauBkgdEstimateDEFGH.addTCanvas (canvas)
    tauBkgdEstimateDEFGH.addPrescaleFactor (lumi["MET_2016DEFGH"] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"])
    tauBkgdEstimateDEFGH.addTagProbePassScaleFactor (lumi["SingleMuon_2016DEFGH"] / (lumi["SingleMuon_2016DEFGH"] - lumi["SingleMuon_2016D"]))
    tauBkgdEstimateDEFGH.addTagProbePass1ScaleFactor (lumi["SingleElectron_2016DEFGH"] / (lumi["SingleElectron_2016DEFGH"] - lumi["SingleElectron_2016F"]))
    tauBkgdEstimateDEFGH.addLuminosityInInvPb (lumi["MET_2016DEFGH"])
    tauBkgdEstimateDEFGH.addLuminosityLabel ("0.139 fb^{-1} (13 TeV)")
    tauBkgdEstimateDEFGH.addPlotLabel ("Tau 2016D")
    tauBkgdEstimateDEFGH.addMetCut (100.0)
    tauBkgdEstimateDEFGH.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",   "SingleMu_2016DEFGH",         dirs['Brian']+"2016/muonBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrkNoElectronMuonFiducialCuts",              "SingleMu_2016EFG_rereco",   dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016DEG_rereco",  dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016DEFGH",              dirs['Brian']+"2016/tauBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016DEFGH",              dirs['Brian']+"2016/tauBackground_v2NoTrig")
    tauBkgdEstimateDEFGH.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2")
    tauBkgdEstimateDEFGH.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2NoTrig")

    print "********************************************************************************"

    (nEstTauDEFGH, nEstTauErrorDEFGH) = tauBkgdEstimateDEFGH.printNest ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "calculating signal acceptance"
    print "--------------------------------------------------------------------------------"

    (nSignalBC, nSignalErrorBC) = getHistIntegralFromProjectionZ ("AMSB_chargino_200GeV_100cm_80X", dirs['Brian'] + "2016/signalCentralValues_BC", "disTrkSelectionSmearedJetsNoElectronMuonFiducialCutsPlotter", fiducialCut, fiducialCut)
    (nSignalDEFGH, nSignalErrorDEFGH) = getHistIntegralFromProjectionZ ("AMSB_chargino_200GeV_100cm_80X", dirs['Brian'] + "2016/signalCentralValues_DEFGH", "disTrkSelectionSmearedJetsNoElectronMuonFiducialCutsPlotter", fiducialCut, fiducialCut)
    all_nSignal.append (nSignalBC + nSignalDEFGH)
    all_nSignalError.append (math.hypot (nSignalErrorBC, nSignalErrorDEFGH))

    print "********************************************************************************"

    print "\n\n"

    print "********************************************************************************"
    nEstElectron = nEstElectronBC + nEstElectronDEFGH
    nEstElectronError = math.hypot (nEstElectronErrorBC, nEstElectronErrorDEFGH)
    nEstMuon = nEstMuonBC + nEstMuonDEFGH
    nEstMuonError = math.hypot (nEstMuonErrorBC, nEstMuonErrorDEFGH)
    nEstTau = nEstTauBC + nEstTauDEFGH
    nEstTauError = math.hypot (nEstTauErrorBC, nEstTauErrorDEFGH)

    nEstBC = nEstElectronBC + nEstMuonBC + nEstTauBC
    nEstDEFGH = nEstElectronDEFGH + nEstMuonDEFGH + nEstTauDEFGH
    nEst = nEstElectron + nEstMuon + nEstTau
    nEstErrorBC = math.hypot (math.hypot (nEstElectronErrorBC, nEstMuonErrorBC), nEstTauErrorBC)
    nEstErrorDEFGH = math.hypot (math.hypot (nEstElectronErrorDEFGH, nEstMuonErrorDEFGH), nEstTauErrorDEFGH)
    nEstError = math.hypot (math.hypot (nEstElectronError, nEstMuonError), nEstTauError)
    print "total background from leptons (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
    print "total background from leptons (2016DEFGH): " + str (nEstDEFGH) + " +- " + str (nEstErrorDEFGH)
    print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
    print "********************************************************************************"

    print "\n\n"

    print "********************************************************************************"
    nEstBC += nEstFakeBC
    nEstDEFGH += nEstFakeDEFGH
    nEst += nEstFake
    nEstErrorBC = math.hypot (nEstErrorBC, nEstFakeErrorBC)
    nEstErrorDEFGH = math.hypot (nEstErrorDEFGH, nEstFakeErrorDEFGH)
    nEstError = math.hypot (nEstError, nEstFakeError)
    print "total background (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
    print "total background (2016DEFGH): " + str (nEstDEFGH) + " +- " + str (nEstErrorDEFGH)
    print "total background: " + str (nEst) + " +- " + str (nEstError)
    print "********************************************************************************"

    all_nBackground.append (nEstBC + nEstDEFGH)
    all_nBackgroundError.append (math.hypot (nEstErrorBC, nEstErrorDEFGH))

    all_fiducialCuts.append(fiducialCut)

signalCutPass = TH1D('signalCutEff', 'signalCutEff', len(all_nSignal), 1./10., 50./10.)
signalCutTotal = TH1D('signalCutTotal', 'signalCutTotal', len(all_nSignal), 1./10., 50./10.)

backgroundPrediction = TH1D('backgroundPrediction', 'backgroundPrediction', len(all_nSignal), 1./10., 50./10.)
backgroundPrediction.Sumw2()

for i in range(0, len(all_nSignal)):
    signalCutPass.SetBinContent(i+1, all_nSignal[i])
    signalCutTotal.SetBinContent(i+1, all_nSignal[-1])

    backgroundPrediction.SetBinContent(i+1, all_nBackground[i])
    backgroundPrediction.SetBinError(i+1, all_nBackgroundError[i])

all_sOverRootB = []

for i in range(0, len(all_nSignal)):
    all_sOverRootB.append (all_nSignal[i] / math.sqrt (all_nBackground[i]))

fout = TFile.Open ("fiducialCutOptimization.root", "recreate")

signalEff  = TGraphAsymmErrors(signalCutPass, signalCutTotal)
sOverRootB = TGraph(len(all_sOverRootB),  array("d", all_fiducialCuts), array("d", all_sOverRootB))

backgroundPrediction.Write("backgroundPrediction")
signalEff.Write("signalEff")
sOverRootB.Write("sOverRootB")

fout.Write()
fout.Close()
