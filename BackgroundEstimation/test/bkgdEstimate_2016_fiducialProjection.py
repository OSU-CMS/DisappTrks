#!/usr/bin/env python

import math
from DisappTrks.BackgroundEstimation.bkgdEstimate import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile
import os

metLumi          =  lumi["MET_2016BC"] + lumi["MET_2016DEFG"]
electronLumi     =  lumi["SingleElectron_2016BC"] + lumi["SingleElectron_2016DEFG"]
muonLumi         =  lumi["SingleMuon_2016BC"] + lumi["SingleMuon_2016DEFG"]
tauLumi          =  lumi["Tau_2016BC"] + lumi["Tau_2016DEFG"]

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing fake track background estimate in search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate_2016.root", "recreate")

fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate.addTFile (fout)
fakeTrackBkgdEstimate.addTCanvas (canvas)
fakeTrackBkgdEstimate.addPrescaleFactor (metLumi / muonLumi)
fakeTrackBkgdEstimate.addLuminosityInInvFb (metLumi)
fakeTrackBkgdEstimate.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2016",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackBkgdEstimate.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2016",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackBkgdEstimate.addChannel  ("Basic",        "BasicSelection",  "MET_2016",       dirs['Andrew']+"2016_ICHEP/basicSelection")

print "********************************************************************************"

(nEstFake, nEstFakeError) = fakeTrackBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing fake track background estimate in search region (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate_2016_v3.root", "recreate")

fakeTrackBkgdEstimate_v3 = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate_v3.addTFile (fout)
fakeTrackBkgdEstimate_v3.addTCanvas (canvas)
fakeTrackBkgdEstimate_v3.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleMuon_2016BC"])
fakeTrackBkgdEstimate_v3.addLuminosityInInvFb (lumi["MET_2016BC"])
fakeTrackBkgdEstimate_v3.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackBkgdEstimate_v3.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackBkgdEstimate_v3.addChannel  ("Basic",        "BasicSelection",  "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/basicSelection")

print "********************************************************************************"

(nEstFake_v3, nEstFakeError_v3) = fakeTrackBkgdEstimate_v3.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing fake track background estimate in search region (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate_2016_v4.root", "recreate")

fakeTrackBkgdEstimate_v4 = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate_v4.addTFile (fout)
fakeTrackBkgdEstimate_v4.addTCanvas (canvas)
fakeTrackBkgdEstimate_v4.addPrescaleFactor (lumi["MET_2016DEFG"] / lumi["SingleMuon_2016DEFG"])
fakeTrackBkgdEstimate_v4.addLuminosityInInvFb (lumi["MET_2016DEFG"])
fakeTrackBkgdEstimate_v4.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackBkgdEstimate_v4.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/fakeTrackBackground")
fakeTrackBkgdEstimate_v4.addChannel  ("Basic",        "BasicSelection",  "MET_2016D",       dirs['Andrew']+"2016_ICHEP/basicSelection")

print "********************************************************************************"

(nEstFakeDEFG, nEstFakeErrorDEFG) = fakeTrackBkgdEstimate_v4.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron background estimate in search region (2016BC)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdEstimate_2016BC.root", "recreate")

electronBkgdEstimateBC = LeptonBkgdEstimate ("electron")
electronBkgdEstimateBC.addTFile (fout)
electronBkgdEstimateBC.addTCanvas (canvas)
electronBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleElectron_2016BC"])
electronBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"])
electronBkgdEstimateBC.addLuminosityLabel ("8.53 fb^{-1} (13 TeV)")
electronBkgdEstimateBC.addPlotLabel ("SingleElectron 2016B+C")
electronBkgdEstimateBC.addMetCut (100.0)
electronBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016BC",  "electronBackground")
electronBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016BC",  "electronBackground")
electronBkgdEstimateBC.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016BC",  "electronBackground")
electronBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016BC",  "electronBackground")

print "********************************************************************************"

(nEstElectronBC, nEstElectronErrorBC) = electronBkgdEstimateBC.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron background estimate in search region (2016D-G)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdEstimate_2016DEFG.root", "recreate")

electronBkgdEstimateDEFG = LeptonBkgdEstimate ("electron")
electronBkgdEstimateDEFG.addTFile (fout)
electronBkgdEstimateDEFG.addTCanvas (canvas)
electronBkgdEstimateDEFG.addPrescaleFactor ((18.0 / 27.0) * lumi["MET_2016DEFG"] / lumi["SingleElectron_2016DEFG"])
electronBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"])
electronBkgdEstimateDEFG.addLuminosityLabel ("4.35 fb^{-1} (13 TeV)")
electronBkgdEstimateDEFG.addPlotLabel ("SingleElectron 2016D")
electronBkgdEstimateDEFG.addMetCut (100.0)
electronBkgdEstimateDEFG.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleEle_2016DEFG",  "electronBackground")
electronBkgdEstimateDEFG.addChannel  ("TagProbePass",    "ZtoEleDisTrkNoElectronMuonFiducialCuts",             "SingleEle_2016DEFG",  "electronBackground")
electronBkgdEstimateDEFG.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016DEFG",  "electronBackground")
electronBkgdEstimateDEFG.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016DEFG",  "electronBackground")

print "********************************************************************************"

(nEstElectronDEFG, nEstElectronErrorDEFG) = electronBkgdEstimateDEFG.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in search region (2016BC)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate_2016BC.root", "recreate")

muonBkgdEstimateBC = LeptonBkgdEstimate ("muon")
muonBkgdEstimateBC.addTFile (fout)
muonBkgdEstimateBC.addTCanvas (canvas)
muonBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["SingleMuon_2016BC"])
muonBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"])
muonBkgdEstimateBC.addLuminosityLabel ("8.52 fb^{-1} (13 TeV)")
muonBkgdEstimateBC.addPlotLabel ("SingleMuon 2016B+C")
muonBkgdEstimateBC.addMetCut (100.0)
muonBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleMu_2016BC",  "muonBackground")
muonBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoElectronMuonFiducialCuts",             "SingleMu_2016BC",  "muonBackground")
muonBkgdEstimateBC.addChannel  ("TagPt35",         "MuonTagPt55NoElectronMuonFiducialCuts",             "SingleMu_2016BC",  "muonBackground")
muonBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrigNoElectronMuonFiducialCuts",      "SingleMu_2016BC",  "muonBackground")

print "********************************************************************************"

(nEstMuonBC, nEstMuonErrorBC) = muonBkgdEstimateBC.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in search region (2016D-G)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate_2016DEFG.root", "recreate")

muonBkgdEstimateDEFG = LeptonBkgdEstimate ("muon")
muonBkgdEstimateDEFG.addTFile (fout)
muonBkgdEstimateDEFG.addTCanvas (canvas)
muonBkgdEstimateDEFG.addPrescaleFactor (lumi["MET_2016DEFG"] / lumi["SingleMuon_2016DEFG"])
muonBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"])
muonBkgdEstimateDEFG.addLuminosityLabel ("4.35 fb^{-1} (13 TeV)")
muonBkgdEstimateDEFG.addPlotLabel ("SingleMuon 2016D")
muonBkgdEstimateDEFG.addMetCut (100.0)
muonBkgdEstimateDEFG.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCutsNoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",  "muonBackground")
muonBkgdEstimateDEFG.addChannel  ("TagProbePass",    "ZtoMuDisTrkNoElectronMuonFiducialCuts",             "SingleMu_2016DEFG",  "muonBackground")
muonBkgdEstimateDEFG.addChannel  ("TagPt35",         "MuonTagPt55NoElectronMuonFiducialCuts",             "SingleMu_2016DEFG",  "muonBackground")
muonBkgdEstimateDEFG.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrigNoElectronMuonFiducialCuts",      "SingleMu_2016DEFG",  "muonBackground")

print "********************************************************************************"

(nEstMuonDEFG, nEstMuonErrorDEFG) = muonBkgdEstimateDEFG.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in search region (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdEstimate_2016BC.root", "recreate")

tauBkgdEstimateBC = LeptonBkgdEstimate ("tau")
tauBkgdEstimateBC.addTFile (fout)
tauBkgdEstimateBC.addTCanvas (canvas)
tauBkgdEstimateBC.addPrescaleFactor (lumi["MET_2016BC"] / lumi["Tau_2016BC"])
tauBkgdEstimateBC.addLuminosityInInvFb (lumi["MET_2016BC"])
tauBkgdEstimateBC.addLuminosityLabel ("0.814 fb^{-1} (13 TeV)")
tauBkgdEstimateBC.addPlotLabel ("Tau 2016B+C")
tauBkgdEstimateBC.addMetCut (100.0)
tauBkgdEstimateBC.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCuts",  "SingleMu_2016BC",  "tauBackground")
tauBkgdEstimateBC.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrk",             "SingleMu_2016_rerecoBC",  "tauBackground")
tauBkgdEstimateBC.addChannel  ("TagProbe1",        "ZtoTauToEleProbeTrkWithZCuts",  "SingleEle_2016BC",  "tauBackground")
tauBkgdEstimateBC.addChannel  ("TagProbePass1",    "ZtoTauToEleDisTrk",             "SingleEle_2016_rerecoBC",  "tauBackground")
tauBkgdEstimateBC.addChannel  ("TagPt35",         "TauTagPt55",               "Tau_2016BC",       "tauBackgroundControlRegion")
#tauBkgdEstimateBC.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",        "Tau_2016BC",       "tauBackgroundControlRegion")
tauBkgdEstimateBC.addChannel  ("TrigEffDenom",         "ElectronTagPt55",          "SingleEle_2016BC",  "electronBackgroundControlRegion")
tauBkgdEstimateBC.addChannel  ("TrigEffNumer",  "ElectronTagPt55MetTrig",   "SingleEle_2016BC",  "electronBackgroundControlRegion")

print "********************************************************************************"

(nEstTauBC, nEstTauErrorBC) = tauBkgdEstimateBC.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in search region (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdEstimate_2016DEFG.root", "recreate")

tauBkgdEstimateDEFG = LeptonBkgdEstimate ("tau")
tauBkgdEstimateDEFG.addTFile (fout)
tauBkgdEstimateDEFG.addTCanvas (canvas)
tauBkgdEstimateDEFG.addPrescaleFactor (lumi["MET_2016DEFG"] / lumi["Tau_2016DEFG"])
tauBkgdEstimateDEFG.addLuminosityInInvFb (lumi["MET_2016DEFG"])
tauBkgdEstimateDEFG.addLuminosityLabel ("0.139 fb^{-1} (13 TeV)")
tauBkgdEstimateDEFG.addPlotLabel ("Tau 2016D")
tauBkgdEstimateDEFG.addMetCut (100.0)
tauBkgdEstimateDEFG.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCuts",  "SingleMu_2016D",  "tauBackground")
tauBkgdEstimateDEFG.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrk",             "SingleMu_2016D_rereco",  "tauBackground")
tauBkgdEstimateDEFG.addChannel  ("TagProbe1",        "ZtoTauToEleProbeTrkWithZCuts",  "SingleEle_2016D",  "tauBackground")
tauBkgdEstimateDEFG.addChannel  ("TagProbePass1",    "ZtoTauToEleDisTrk",             "SingleEle_2016D",  "tauBackground")
tauBkgdEstimateDEFG.addChannel  ("TagPt35",         "TauTagPt55",               "Tau_2016D",       "tauBackgroundControlRegion")
#tauBkgdEstimateDEFG.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",        "Tau_2016D",       "tauBackgroundControlRegion")
tauBkgdEstimateDEFG.addChannel  ("TrigEffDenom",         "ElectronTagPt55",          "SingleEle_2016D",  "electronBackgroundControlRegion")
tauBkgdEstimateDEFG.addChannel  ("TrigEffNumer",  "ElectronTagPt55MetTrig",   "SingleEle_2016D",  "electronBackgroundControlRegion")

print "********************************************************************************"

(nEstTauDEFG, nEstTauErrorDEFG) = tauBkgdEstimateDEFG.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
nEstElectron = nEstElectronBC + nEstElectronDEFG
nEstElectronError = math.hypot (nEstElectronErrorBC, nEstElectronErrorDEFG)
nEstMuon = nEstMuonBC + nEstMuonDEFG
nEstMuonError = math.hypot (nEstMuonErrorBC, nEstMuonErrorDEFG)
nEstTau = nEstTauBC + nEstTauDEFG
nEstTauError = math.hypot (nEstTauErrorBC, nEstTauErrorDEFG)

nEstBC = nEstElectronBC + nEstMuonBC + nEstTauBC
nEstDEFG = nEstElectronDEFG + nEstMuonDEFG + nEstTauDEFG
nEst = nEstElectron + nEstMuon + nEstTau
nEstErrorBC = math.hypot (math.hypot (nEstElectronErrorBC, nEstMuonErrorBC), nEstTauErrorBC)
nEstErrorDEFG = math.hypot (math.hypot (nEstElectronErrorDEFG, nEstMuonErrorDEFG), nEstTauErrorDEFG)
nEstError = math.hypot (math.hypot (nEstElectronError, nEstMuonError), nEstTauError)
print "total background from leptons (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
print "total background from leptons (2016D): " + str (nEstDEFG) + " +- " + str (nEstErrorDEFG)
print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"

print "\n\n"

print "********************************************************************************"
nEstBC += nEstFakeBC
nEstDEFG += nEstFakeDEFG
nEst += nEstFake
nEstErrorBC = math.hypot (nEstErrorBC, nEstFakeErrorBC)
nEstErrorDEFG = math.hypot (nEstErrorDEFG, nEstFakeErrorDEFG)
nEstError = math.hypot (nEstError, nEstFakeError)
print "total background (2016B & 2016C): " + str (nEstBC) + " +- " + str (nEstErrorBC)
print "total background (2016D): " + str (nEstDEFG) + " +- " + str (nEstErrorDEFG)
print "total background: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"
