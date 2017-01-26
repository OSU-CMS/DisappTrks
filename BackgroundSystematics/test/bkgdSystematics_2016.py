#!/usr/bin/env python

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
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
fakeTrackSystematicBC.addChannel  ("Basic",                "BasicSelection",                                   "MET_2016BC",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3NoElectronMuonFiducialCuts",  "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4NoElectronMuonFiducialCuts",  "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5NoElectronMuonFiducialCuts",  "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6NoElectronMuonFiducialCuts",  "MET_2016BC",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicBC.addChannel  ("ZtoLL",                "ZtoMuMu",                                          "SingleMu_2016BC",  dirs['Brian']+"2016/zToMuMu_noSkim")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3NoElectronMuonFiducialCuts",    "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4NoElectronMuonFiducialCuts",    "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5NoElectronMuonFiducialCuts",    "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicBC.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6NoElectronMuonFiducialCuts",    "SingleMu_2016BC",  dirs['Brian']+"2016/fakeTrackBackground_v2")

print "********************************************************************************"

fakeTrackSystematicBC.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating fake track systematic (2016DEFGH)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2016DEFGH.root", "recreate")

fakeTrackSystematicDEFGH = FakeTrackSystematic ()
fakeTrackSystematicDEFGH.addTFile (fout)
fakeTrackSystematicDEFGH.addTCanvas (canvas)
fakeTrackSystematicDEFGH.addLuminosityLabel (str (round (lumi["MET_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
fakeTrackSystematicDEFGH.addChannel  ("Basic",                "BasicSelection",                                   "MET_2016DEFGH",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicDEFGH.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3NoElectronMuonFiducialCuts",  "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFGH.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4NoElectronMuonFiducialCuts",  "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFGH.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5NoElectronMuonFiducialCuts",  "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFGH.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6NoElectronMuonFiducialCuts",  "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicDEFGH.addChannel  ("ZtoLL",                "ZtoMuMu",                                          "SingleMu_2016DEFGH",  dirs['Brian']+"2016/zToMuMu_noSkim")
fakeTrackSystematicDEFGH.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3NoElectronMuonFiducialCuts",    "SingleMu_2016DEFGH",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicDEFGH.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4NoElectronMuonFiducialCuts",    "SingleMu_2016DEFGH",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicDEFGH.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5NoElectronMuonFiducialCuts",    "SingleMu_2016DEFGH",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicDEFGH.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6NoElectronMuonFiducialCuts",    "SingleMu_2016DEFGH",  dirs['Brian']+"2016/fakeTrackBackground_v2")

print "********************************************************************************"

fakeTrackSystematicDEFGH.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating fake track systematic (2016G)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematic_2016G.root", "recreate")

fakeTrackSystematicG = FakeTrackSystematic ()
fakeTrackSystematicG.addTFile (fout)
fakeTrackSystematicG.addTCanvas (canvas)
fakeTrackSystematicG.addLuminosityLabel (str (round (lumi["MET_2016G"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
fakeTrackSystematicG.addChannel  ("Basic",                "BasicSelection",                                   "MET_2016G",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicG.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3NoElectronMuonFiducialCuts",  "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicG.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4NoElectronMuonFiducialCuts",  "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicG.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5NoElectronMuonFiducialCuts",  "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicG.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6NoElectronMuonFiducialCuts",  "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicG.addChannel  ("ZtoLL",                "ZtoMuMu",                                          "SingleMu_2016G",  dirs['Brian']+"2016/zToMuMu_noSkim")
fakeTrackSystematicG.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3NoElectronMuonFiducialCuts",    "SingleMu_2016G",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicG.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4NoElectronMuonFiducialCuts",    "SingleMu_2016G",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicG.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5NoElectronMuonFiducialCuts",    "SingleMu_2016G",  dirs['Brian']+"2016/fakeTrackBackground_v2")
fakeTrackSystematicG.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6NoElectronMuonFiducialCuts",    "SingleMu_2016G",  dirs['Brian']+"2016/fakeTrackBackground_v2")

print "********************************************************************************"

fakeTrackSystematicG.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating fake track systematic with jet requirement (2016DEFGH)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematicWithJet_2016DEFGH.root", "recreate")

fakeTrackSystematicWithJetDEFGH = FakeTrackSystematic ()
fakeTrackSystematicWithJetDEFGH.addTFile (fout)
fakeTrackSystematicWithJetDEFGH.addTCanvas (canvas)
fakeTrackSystematicWithJetDEFGH.addLuminosityLabel (str (round (lumi["MET_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
fakeTrackSystematicWithJetDEFGH.addChannel  ("Basic",                "BasicSelection",                                    "MET_2016DEFGH",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicWithJetDEFGH.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3NoElectronMuonFiducialCuts",   "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetDEFGH.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4NoElectronMuonFiducialCuts",   "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetDEFGH.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5NoElectronMuonFiducialCuts",   "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetDEFGH.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6NoElectronMuonFiducialCuts",   "MET_2016DEFGH",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetDEFGH.addChannel  ("ZtoLL",                "ZtoMuMuJet",                                        "SingleMu_2016DEFGH",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetDEFGH.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3JetNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetDEFGH.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4JetNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetDEFGH.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5JetNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetDEFGH.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6JetNoElectronMuonFiducialCuts",  "SingleMu_2016DEFGH",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")

print "********************************************************************************"

fakeTrackSystematicWithJetDEFGH.printSystematic ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "evaluating fake track systematic with jet requirement (2016G)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackSystematicWithJet_2016G.root", "recreate")

fakeTrackSystematicWithJetG = FakeTrackSystematic ()
fakeTrackSystematicWithJetG.addTFile (fout)
fakeTrackSystematicWithJetG.addTCanvas (canvas)
fakeTrackSystematicWithJetG.addLuminosityLabel (str (round (lumi["MET_2016G"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
fakeTrackSystematicWithJetG.addChannel  ("Basic",                "BasicSelection",                                    "MET_2016G",       dirs['Andrew']+"2016/basicSelection")
fakeTrackSystematicWithJetG.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3NoElectronMuonFiducialCuts",   "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetG.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4NoElectronMuonFiducialCuts",   "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetG.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5NoElectronMuonFiducialCuts",   "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetG.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6NoElectronMuonFiducialCuts",   "MET_2016G",       dirs['Andrew']+"2016/fakeTrackSystematics")
fakeTrackSystematicWithJetG.addChannel  ("ZtoLL",                "ZtoMuMuJet",                                        "SingleMu_2016G",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetG.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3JetNoElectronMuonFiducialCuts",  "SingleMu_2016G",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetG.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4JetNoElectronMuonFiducialCuts",  "SingleMu_2016G",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetG.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5JetNoElectronMuonFiducialCuts",  "SingleMu_2016G",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
fakeTrackSystematicWithJetG.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6JetNoElectronMuonFiducialCuts",  "SingleMu_2016G",  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")

print "********************************************************************************"

fakeTrackSystematicWithJetG.printSystematic ()

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
print "evaluating electron energy systematic (2016DEFGH)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronEnergySystematic_2016DEFGH.root", "recreate")

electronEnergySystematicDEFGH = LeptonEnergySystematic ("electron")
electronEnergySystematicDEFGH.addTFile (fout)
electronEnergySystematicDEFGH.addTCanvas (canvas)
electronEnergySystematicDEFGH.addLuminosityLabel (str (round (lumi["SingleElectron_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
electronEnergySystematicDEFGH.addPlotLabel ("SingleElectron 2016D-G")
electronEnergySystematicDEFGH.addMetCut (100.0)
electronEnergySystematicDEFGH.addChannel  ("TagPt35",         "ElectronTagPt55NoElectronMuonFiducialCuts",          "SingleEle_2016DEFGH",         dirs['Brian']+"2016/electronBackground_v2")
electronEnergySystematicDEFGH.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",   "SingleEle_2016DEFGH",         dirs['Brian']+"2016/electronBackground_v2NoTrig")

print "********************************************************************************"

electronEnergySystematicDEFGH.printSystematic ()

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
print "evaluating tau energy systematic (2016DEFGH)"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauEnergySystematic_2016DEFGH.root", "recreate")

tauEnergySystematicDEFGH = LeptonEnergySystematic ("tau")
tauEnergySystematicDEFGH.addTFile (fout)
tauEnergySystematicDEFGH.addTCanvas (canvas)
tauEnergySystematicDEFGH.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
tauEnergySystematicDEFGH.addPlotLabel ("Tau 2016D")
tauEnergySystematicDEFGH.addMetCut (100.0)
tauEnergySystematicDEFGH.addChannel  ("TagPt35",         "TauTagPt55NoElectronMuonFiducialCuts",                    "Tau_2016DEFGH",              dirs['Brian']+"2016/tauBackground_v2")
#tauEnergySystematicDEFGH.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrigNoElectronMuonFiducialCuts",             "Tau_2016DEFGH",              dirs['Brian']+"2016/tauBackground_v2NoTrig")
tauEnergySystematicDEFGH.addChannel  ("TrigEffDenom",    "ElectronTagPt55NoElectronMuonFiducialCuts",               "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2")
tauEnergySystematicDEFGH.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrigNoElectronMuonFiducialCuts",        "SingleEle_2016DEFGH",        dirs['Brian']+"2016/electronBackground_v2NoTrig")

print "********************************************************************************"

tauEnergySystematicDEFGH.printSystematic ()

print "********************************************************************************"

fout.Close ()
