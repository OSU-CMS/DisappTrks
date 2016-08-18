#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.bkgdEstimate import *
from DisappTrks.StandardAnalysis.getUser import *
from ROOT import TCanvas, TFile
import os

metLumi_v3       =  8530.9
metLumi_v4       =  4353.4
metLumi          =  metLumi_v3 + metLumi_v4
electronLumi_v3  =  8529.8
electronLumi_v4  =  4353.449
electronLumi     =  electronLumi_v3 + electronLumi_v4
muonLumi_v3      =  8523.9
muonLumi_v4      =  4353.449
muonLumi         =  muonLumi_v3 + muonLumi_v4
tauLumi_v3       =  813.73
tauLumi_v4       =  138.94
tauLumi          =  tauLumi_v3 + tauLumi_v4

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing fake track background estimate in search region (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate_v3.root", "recreate")

fakeTrackBkgdEstimate_v3 = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate_v3.addTFile (fout)
fakeTrackBkgdEstimate_v3.addTCanvas (canvas)
fakeTrackBkgdEstimate_v3.addPrescaleFactor (metLumi_v3 / muonLumi_v3)
fakeTrackBkgdEstimate_v3.addLuminosityInInvFb (metLumi_v3)
fakeTrackBkgdEstimate_v3.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackBkgdEstimate_v3.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/fakeTrackBkgdForDisappearingTrackSelection")
fakeTrackBkgdEstimate_v3.addChannel  ("Basic",        "BasicSelection",  "MET_2016_v3",       dirs['Andrew']+"2016_ICHEP/basicSelection")

print "********************************************************************************"

(nEstFake_v3, nEstFakeError_v3) = fakeTrackBkgdEstimate_v3.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing fake track background estimate in search region (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate_v4.root", "recreate")

fakeTrackBkgdEstimate_v4 = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate_v4.addTFile (fout)
fakeTrackBkgdEstimate_v4.addTCanvas (canvas)
fakeTrackBkgdEstimate_v4.addPrescaleFactor (metLumi_v4 / muonLumi_v4)
fakeTrackBkgdEstimate_v4.addLuminosityInInvFb (metLumi_v4)
fakeTrackBkgdEstimate_v4.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/zToMuMu")
fakeTrackBkgdEstimate_v4.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/fakeTrackBkgdForDisappearingTrackSelection")
fakeTrackBkgdEstimate_v4.addChannel  ("Basic",        "BasicSelection",  "MET_2016D",       dirs['Andrew']+"2016_ICHEP/basicSelection")

print "********************************************************************************"

(nEstFake_v4, nEstFakeError_v4) = fakeTrackBkgdEstimate_v4.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron background estimate in search region (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdEstimate_v3.root", "recreate")

electronBkgdEstimate_v3 = LeptonBkgdEstimate ("electron")
electronBkgdEstimate_v3.addTFile (fout)
electronBkgdEstimate_v3.addTCanvas (canvas)
electronBkgdEstimate_v3.addPrescaleFactor (metLumi_v3 / electronLumi_v3)
electronBkgdEstimate_v3.addLuminosityInInvFb (metLumi_v3)
electronBkgdEstimate_v3.addMetCut (100.0)
electronBkgdEstimate_v3.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2016_v3",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v3.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2016_v3",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v3.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2016_v3",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
#electronBkgdEstimate_v3.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2016_v3",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v3.addChannel  ("TrigEffDenom",    "MuonTagPt55",              "SingleMu_2016_v3",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v3.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",       "SingleMu_2016_v3",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstElectron_v3, nEstElectronError_v3) = electronBkgdEstimate_v3.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron background estimate in search region (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdEstimate_v4.root", "recreate")

electronBkgdEstimate_v4 = LeptonBkgdEstimate ("electron")
electronBkgdEstimate_v4.addTFile (fout)
electronBkgdEstimate_v4.addTCanvas (canvas)
electronBkgdEstimate_v4.addPrescaleFactor (metLumi_v4 / electronLumi_v4)
electronBkgdEstimate_v4.addLuminosityInInvFb (metLumi_v4)
electronBkgdEstimate_v4.addMetCut (100.0)
electronBkgdEstimate_v4.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2016D",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v4.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2016D",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v4.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2016D",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
#electronBkgdEstimate_v4.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2016D",  dirs['Andrew']+"2016_ICHEP/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v4.addChannel  ("TrigEffDenom",    "MuonTagPt55",              "SingleMu_2016D",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
electronBkgdEstimate_v4.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",       "SingleMu_2016D",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstElectron_v4, nEstElectronError_v4) = electronBkgdEstimate_v4.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in search region (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate_v3.root", "recreate")

muonBkgdEstimate_v3 = LeptonBkgdEstimate ("muon")
muonBkgdEstimate_v3.addTFile (fout)
muonBkgdEstimate_v3.addTCanvas (canvas)
muonBkgdEstimate_v3.addPrescaleFactor (metLumi_v3 / muonLumi_v3)
muonBkgdEstimate_v3.addLuminosityInInvFb (metLumi_v3)
muonBkgdEstimate_v3.addMetCut (100.0)
muonBkgdEstimate_v3.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/muonTagAndProbe_withMissingOuterHitsCut")
muonBkgdEstimate_v3.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/muonTagAndProbe_withMissingOuterHitsCut")
muonBkgdEstimate_v3.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
#muonBkgdEstimate_v3.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
muonBkgdEstimate_v3.addChannel  ("TrigEffDenom",    "MuonTagPt55",              "SingleMu_2016_v3",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
muonBkgdEstimate_v3.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",       "SingleMu_2016_v3",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstMuon_v3, nEstMuonError_v3) = muonBkgdEstimate_v3.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in search region (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate_v4.root", "recreate")

muonBkgdEstimate_v4 = LeptonBkgdEstimate ("muon")
muonBkgdEstimate_v4.addTFile (fout)
muonBkgdEstimate_v4.addTCanvas (canvas)
muonBkgdEstimate_v4.addPrescaleFactor (metLumi_v4 / muonLumi_v4)
muonBkgdEstimate_v4.addLuminosityInInvFb (metLumi_v4)
muonBkgdEstimate_v4.addMetCut (100.0)
muonBkgdEstimate_v4.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/muonTagAndProbe_withMissingOuterHitsCut")
muonBkgdEstimate_v4.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/muonTagAndProbe_withMissingOuterHitsCut")
muonBkgdEstimate_v4.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
#muonBkgdEstimate_v4.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
muonBkgdEstimate_v4.addChannel  ("TrigEffDenom",    "MuonTagPt55",              "SingleMu_2016D",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
muonBkgdEstimate_v4.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",       "SingleMu_2016D",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstMuon_v4, nEstMuonError_v4) = muonBkgdEstimate_v4.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in search region (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdEstimate_v3.root", "recreate")

tauBkgdEstimate_v3 = LeptonBkgdEstimate ("tau")
tauBkgdEstimate_v3.addTFile (fout)
tauBkgdEstimate_v3.addTCanvas (canvas)
tauBkgdEstimate_v3.addPrescaleFactor (metLumi_v3 / tauLumi_v3)
tauBkgdEstimate_v3.addLuminosityInInvFb (metLumi_v3)
tauBkgdEstimate_v3.addMetCut (100.0)
tauBkgdEstimate_v3.addChannel  ("TagProbe",        "ZtoTauProbeTrkWithZCuts",  "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v3.addChannel  ("TagProbePass",    "ZtoTauDisTrk",             "SingleMu_2016_v3",  dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v3.addChannel  ("TagPt35",         "TauTagPt55",               "Tau_2016_v3",       dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
#tauBkgdEstimate_v3.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",        "Tau_2016_v3",       dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v3.addChannel  ("TrigEffDenom",    "MuonTagPt55",              "SingleMu_2016_v3",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v3.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",       "SingleMu_2016_v3",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstTau_v3, nEstTauError_v3) = tauBkgdEstimate_v3.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in search region (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdEstimate_v4.root", "recreate")

tauBkgdEstimate_v4 = LeptonBkgdEstimate ("tau")
tauBkgdEstimate_v4.addTFile (fout)
tauBkgdEstimate_v4.addTCanvas (canvas)
tauBkgdEstimate_v4.addPrescaleFactor (metLumi_v4 / tauLumi_v4)
tauBkgdEstimate_v4.addLuminosityInInvFb (metLumi_v4)
tauBkgdEstimate_v4.addMetCut (100.0)
tauBkgdEstimate_v4.addChannel  ("TagProbe",        "ZtoTauProbeTrkWithZCuts",  "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v4.addChannel  ("TagProbePass",    "ZtoTauDisTrk",             "SingleMu_2016D",  dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v4.addChannel  ("TagPt35",         "TauTagPt55",               "Tau_2016D",       dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
#tauBkgdEstimate_v4.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",        "Tau_2016D",       dirs['Andrew']+"2016_ICHEP/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v4.addChannel  ("TrigEffDenom",    "MuonTagPt55",              "SingleMu_2016D",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")
tauBkgdEstimate_v4.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",       "SingleMu_2016D",   dirs['Andrew']+"2016_ICHEP/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstTau_v4, nEstTauError_v4) = tauBkgdEstimate_v4.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
nEstElectron = nEstElectron_v3 + nEstElectron_v4
nEstElectronError = math.hypot (nEstElectronError_v3, nEstElectronError_v4)
nEstMuon = nEstMuon_v3 + nEstMuon_v4
nEstMuonError = math.hypot (nEstMuonError_v3, nEstMuonError_v4)
nEstTau = nEstTau_v3 + nEstTau_v4
nEstTauError = math.hypot (nEstTauError_v3, nEstTauError_v4)
nEst = nEstElectron + nEstMuon + nEstTau
nEstError = math.hypot (math.hypot (nEstElectronError, nEstMuonError), nEstTauError)
print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"

print "\n\n"

print "********************************************************************************"
nEstFake = nEstFake_v3 + nEstFake_v4
nEstFakeError = math.hypot (nEstFakeError_v3, nEstFakeError_v4)
nEst += nEstFake
nEstError = math.hypot (nEstError, nEstFakeError)
print "total background: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"
