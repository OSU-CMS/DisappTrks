#!/usr/bin/env python

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile
import os

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "evaluating fake track systematic (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2016BC.root", "recreate")

fakeTrackSystematicBC = FakeTrackSystematic ()
fakeTrackSystematicBC.addTFile (fout)
fakeTrackSystematicBC.addTCanvas (canvas)
fakeTrackSystematicBC.addLuminosityLabel (str (round (lumi["MET_2016BC"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
fakeTrackSystematicBC.addChannel  ("Basic",                "BasicSelection",                                 "MET_2016BC",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",                          "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",                          "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",                          "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",                          "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("ZtoLL",                "ZtoMuMu",                                        "SingleMu_2016BC",  dirs['Brian']+"2016/zToMuMu_noSkim")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3NoElectronMuonFiducialCuts",  "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4NoElectronMuonFiducialCuts",  "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5NoElectronMuonFiducialCuts",  "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6NoElectronMuonFiducialCuts",  "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")

print "********************************************************************************"

fakeTrackSystematicBC.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating fake track systematic (2016DEFG)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2016DEFG.root", "recreate")

fakeTrackSystematicDEFG = FakeTrackSystematic ()
fakeTrackSystematicDEFG.addTFile (fout)
fakeTrackSystematicDEFG.addTCanvas (canvas)
fakeTrackSystematicDEFG.addLuminosityLabel (str (round (lumi["MET_2016DEFG"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
fakeTrackSystematicDEFG.addChannel  ("Basic",                "BasicSelection",                                 "MET_2016DEFG",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicDEFG.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",                          "MET_2016DEFG",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFG.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",                          "MET_2016DEFG",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFG.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",                          "MET_2016DEFG",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFG.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",                          "MET_2016DEFG",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFG.addChannel  ("ZtoLL",                "ZtoMuMu",                                        "SingleMu_2016DEFG",  dirs['Brian']+"2016/zToMuMu_noSkim")
fakeTrackSystematicDEFG.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3NoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicDEFG.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4NoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicDEFG.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5NoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicDEFG.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6NoElectronMuonFiducialCuts",  "SingleMu_2016DEFG",  dirs['Brian']+"2016/fakeTrackBackground_v2")

print "********************************************************************************"

fakeTrackSystematicDEFG.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating electron energy systematic (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronEnergySystematic_2016BC.root", "recreate")

electronEnergySystematicBC = LeptonEnergySystematic ("electron")
electronEnergySystematicBC.addTFile (fout)
electronEnergySystematicBC.addTCanvas (canvas)
electronEnergySystematicBC.addLuminosityLabel (str (round (lumi["SingleElectron_2016BC"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
electronEnergySystematicBC.addPlotLabel ("SingleElectron 2016B+C")
electronEnergySystematicBC.addMetCut (100.0)
electronEnergySystematicBC.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
electronEnergySystematicBC.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

print "********************************************************************************"

electronEnergySystematicBC.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating electron energy systematic (2016DEFG)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronEnergySystematic_2016DEFG.root", "recreate")

electronEnergySystematicDEFG = LeptonEnergySystematic ("electron")
electronEnergySystematicDEFG.addTFile (fout)
electronEnergySystematicDEFG.addTCanvas (canvas)
electronEnergySystematicDEFG.addLuminosityLabel (str (round (lumi["SingleElectron_2016DEFG"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
electronEnergySystematicDEFG.addPlotLabel ("SingleElectron 2016D-G")
electronEnergySystematicDEFG.addMetCut (100.0)
electronEnergySystematicDEFG.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016DEFG",         dirs['Brian']+"2016/electronBackground_v2")
electronEnergySystematicDEFG.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016DEFG",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

print "********************************************************************************"

electronEnergySystematicDEFG.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating tau energy systematic (2016B & 2016C)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauEnergySystematic_2016BC.root", "recreate")

tauEnergySystematicBC = LeptonEnergySystematic ("tau")
tauEnergySystematicBC.addTFile (fout)
tauEnergySystematicBC.addTCanvas (canvas)
tauEnergySystematicBC.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
tauEnergySystematicBC.addPlotLabel ("Tau 2016B+C")
tauEnergySystematicBC.addMetCut (100.0)
tauEnergySystematicBC.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016BC",               dirs['Brian']+"2016/tauBackground_v2")
#tauEnergySystematicBC.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016BC",               dirs['Brian']+"2016/tauBackground_v2NoTrig")
tauEnergySystematicBC.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2")
tauEnergySystematicBC.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016BC",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

print "********************************************************************************"

tauEnergySystematicBC.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating tau energy systematic (2016D)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauEnergySystematic_2016DEFG.root", "recreate")

tauEnergySystematicDEFG = LeptonEnergySystematic ("tau")
tauEnergySystematicDEFG.addTFile (fout)
tauEnergySystematicDEFG.addTCanvas (canvas)
tauEnergySystematicBC.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFG"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
tauEnergySystematicDEFG.addPlotLabel ("Tau 2016D")
tauEnergySystematicDEFG.addMetCut (100.0)
tauEnergySystematicDEFG.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016DEFG",              dirs['Brian']+"2016/tauBackground_v2")
#tauEnergySystematicDEFG.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016DEFG",              dirs['Brian']+"2016/tauBackground_v2NoTrig")
tauEnergySystematicDEFG.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016DEFG",        dirs['Brian']+"2016/electronBackground_v2")
tauEnergySystematicDEFG.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016DEFG",        dirs['Brian']+"2016/electronBackground_v2NoTrig")

print "********************************************************************************"

tauEnergySystematicDEFG.printSystematic ()

print "********************************************************************************"

fout.Close ()
