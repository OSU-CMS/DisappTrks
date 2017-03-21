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

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

useJetRequirementForFakes = False

# '' will gives you Dataset_2016.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['BC', 'DEFG', 'DEFGH', 'H', '']

if background == "FAKE" or background == "ALL":

    print "********************************************************************************"
    print "evaluating fake track systematic with nTracks reweighting"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("nTracksReweightedFakeTrackSystematic_2016H" + ".root", "recreate")

    nTracksReweightedFakeTrackSystematic = FakeTrackSystematic ()
    nTracksReweightedFakeTrackSystematic.addTFile (fout)
    nTracksReweightedFakeTrackSystematic.addTCanvas (canvas)
    nTracksReweightedFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    nTracksReweightedFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest",  "BasicSelection",  "Eventvariable Plots/nTracks")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")

    print "********************************************************************************"

    nTracksReweightedFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with trackRho reweighting"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("rhoReweightedFakeTrackSystematic_2016H" + ".root", "recreate")

    rhoReweightedFakeTrackSystematic = FakeTrackSystematic ()
    rhoReweightedFakeTrackSystematic.addTFile (fout)
    rhoReweightedFakeTrackSystematic.addTCanvas (canvas)
    rhoReweightedFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    rhoReweightedFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest",  "BasicSelection",  "Eventvariable Plots/trackRho")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")

    print "********************************************************************************"

    rhoReweightedFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with nTracks reweighting with lost tracks"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("nTracksReweightedWithLostTracksFakeTrackSystematic_2016H" + ".root", "recreate")

    nTracksReweightedWithLostTracksFakeTrackSystematic = FakeTrackSystematic ()
    nTracksReweightedWithLostTracksFakeTrackSystematic.addTFile (fout)
    nTracksReweightedWithLostTracksFakeTrackSystematic.addTCanvas (canvas)
    nTracksReweightedWithLostTracksFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks",  "BasicSelection",  "Eventvariable Plots/nTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")

    print "********************************************************************************"

    nTracksReweightedWithLostTracksFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with trackRho reweighting with lost tracks"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("rhoReweightedWithLostTracksFakeTrackSystematic_2016H" + ".root", "recreate")

    rhoReweightedWithLostTracksFakeTrackSystematic = FakeTrackSystematic ()
    rhoReweightedWithLostTracksFakeTrackSystematic.addTFile (fout)
    rhoReweightedWithLostTracksFakeTrackSystematic.addTCanvas (canvas)
    rhoReweightedWithLostTracksFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks",  "BasicSelection",  "Eventvariable Plots/trackRho")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")

    print "********************************************************************************"

    rhoReweightedWithLostTracksFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic in MC"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("mcFakeTrackSystematic_2016D" + ".root", "recreate")

    mcFakeTrackSystematic = FakeTrackSystematic ()
    mcFakeTrackSystematic.addTFile (fout)
    mcFakeTrackSystematic.addTCanvas (canvas)
    mcFakeTrackSystematic.addLuminosityLabel ("13 TeV")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "JustADisTrkNHits3",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "JustADisTrkNHits4",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "JustADisTrkNHits5",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "JustADisTrkNHits6",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "JustADisTrkNHits3",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "JustADisTrkNHits4",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "JustADisTrkNHits5",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "JustADisTrkNHits6",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")

    print "********************************************************************************"

    mcFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic in MC truth"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("mcTruthFakeTrackSystematic_2016D" + ".root", "recreate")

    mcTruthFakeTrackSystematic = FakeTrackSystematic ()
    mcTruthFakeTrackSystematic.addTFile (fout)
    mcTruthFakeTrackSystematic.addTCanvas (canvas)
    mcTruthFakeTrackSystematic.addLuminosityLabel ("13 TeV")
    mcTruthFakeTrackSystematic.getTruthFakeRate (True)
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "JustADisTrkNHits3",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "JustADisTrkNHits4",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "JustADisTrkNHits5",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "JustADisTrkNHits6",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "JustADisTrkNHits3",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "JustADisTrkNHits4",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "JustADisTrkNHits5",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "JustADisTrkNHits6",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonNHits")

    print "********************************************************************************"

    mcTruthFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with ZeroBias data (2016D)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("zeroBiasFakeTrackSystematic_2016D" + ".root", "recreate")

    zeroBiasFakeTrackSystematic = FakeTrackSystematic ()
    zeroBiasFakeTrackSystematic.addTFile (fout)
    zeroBiasFakeTrackSystematic.addTCanvas (canvas)
    zeroBiasFakeTrackSystematic.addLuminosityLabel (str (round (lumi["ZeroBias_2016D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    zeroBiasFakeTrackSystematic.addChannel  ("Basic",                "ZeroBiasSelection",        "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBias")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "ZeroBiasSelectionNHits3",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "ZeroBiasSelectionNHits4",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "ZeroBiasSelectionNHits5",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "ZeroBiasSelectionNHits6",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                  "SingleMu_2016D",  dirs['Andrew']+"2016/zToMuMu_noSkim")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")

    print "********************************************************************************"

    zeroBiasFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with ZeroBias data with jet cut (2016D)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("zeroBiasJetFakeTrackSystematic_2016D" + ".root", "recreate")

    zeroBiasJetFakeTrackSystematic = FakeTrackSystematic ()
    zeroBiasJetFakeTrackSystematic.addTFile (fout)
    zeroBiasJetFakeTrackSystematic.addTCanvas (canvas)
    zeroBiasJetFakeTrackSystematic.addLuminosityLabel (str (round (lumi["ZeroBias_2016D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    zeroBiasJetFakeTrackSystematic.addChannel  ("Basic",                "ZeroBiasJetSelection",        "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "ZeroBiasJetSelectionNHits3",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "ZeroBiasJetSelectionNHits4",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "ZeroBiasJetSelectionNHits5",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "ZeroBiasJetSelectionNHits6",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                     "SingleMu_2016D",  dirs['Andrew']+"2016/zToMuMu_noSkim")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")

    print "********************************************************************************"

    zeroBiasJetFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating fake track systematic (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackSystematic_2016" + runPeriod + ".root", "recreate")

        fakeTrackSystematic = FakeTrackSystematic ()
        fakeTrackSystematic.addTFile (fout)
        fakeTrackSystematic.addTCanvas (canvas)
        fakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        fakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",         "MET_2016" + runPeriod,       dirs['Andrew']+"2016/basicSelection")
        fakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/zToMuMu_noSkim")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")

        print "********************************************************************************"

        fakeTrackSystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating fake track systematic with 1 jet, 16 PV (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackSystematicOneJet14to18PV_2016" + runPeriod + ".root", "recreate")

        fakeTrackSystematicOneJet14to18PV = FakeTrackSystematic ()
        fakeTrackSystematicOneJet14to18PV.addTFile (fout)
        fakeTrackSystematicOneJet14to18PV.addTCanvas (canvas)
        fakeTrackSystematicOneJet14to18PV.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("Basic",                "BasicSelection",                   "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits3",         "DisTrkSelectionOneJet14to18PVNHits3",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits4",         "DisTrkSelectionOneJet14to18PVNHits4",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits5",         "DisTrkSelectionOneJet14to18PVNHits5",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits6",         "DisTrkSelectionOneJet14to18PVNHits6",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoLL",                "ZtoMuMuOneJet14to18PV",                "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuOneJet14to18PVDisTrkNHits3",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuOneJet14to18PVDisTrkNHits4",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuOneJet14to18PVDisTrkNHits5",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuOneJet14to18PVDisTrkNHits6",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")

        print "********************************************************************************"

        fakeTrackSystematicOneJet14to18PV.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if useJetRequirementForFakes:

        for runPeriod in runPeriods:

            print "********************************************************************************"
            print "evaluating fake track systematic with jet requirement (2016", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open ("fakeTrackSystematicWithJet_2016" + runPeriod + ".root", "recreate")

            fakeTrackSystematicWithJet = FakeTrackSystematic ()
            fakeTrackSystematicWithJet.addTFile (fout)
            fakeTrackSystematicWithJet.addTCanvas (canvas)
            fakeTrackSystematicWithJet.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
            fakeTrackSystematicWithJet.addChannel  ("Basic",                "BasicSelection",          "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final/basicSelection")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("ZtoLL",                "ZtoMuMuJet",              "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")

            print "********************************************************************************"

            fakeTrackSystematicWithJet.printSystematic ()

            print "********************************************************************************"

            fout.Close ()

            print "\n\n"

if background == "ELECTRON" or background == "ALL":

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating electron energy systematic (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("electronEnergySystematic_2016" + runPeriod + ".root", "recreate")

        electronEnergySystematic = LeptonEnergySystematic ("electron")
        electronEnergySystematic.addTFile (fout)
        electronEnergySystematic.addTCanvas (canvas)
        electronEnergySystematic.addLuminosityLabel (str (round (lumi["SingleElectron_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        electronEnergySystematic.addPlotLabel ("SingleElectron 2016" + runPeriod)
        electronEnergySystematic.addMetCut (100.0)
        electronEnergySystematic.addChannel  ("TagPt35",         "ElectronTagPt55",         "SingleEle_2016"  +  runPeriod,  dirs['Andrew']+"2016/electronBackground")
        #electronEnergySystematic.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",  "SingleEle_2016"  +  runPeriod,  dirs['Andrew']+"2016/electronBackground")
        electronEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",         "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")
        electronEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",  "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")

        print "********************************************************************************"

        electronEnergySystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

if background == "TAU" or background == "ALL":

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating tau energy systematic (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("tauEnergySystematic_2016" + runPeriod + ".root", "recreate")

        tauEnergySystematic = LeptonEnergySystematic ("tau")
        tauEnergySystematic.addTFile (fout)
        tauEnergySystematic.addTCanvas (canvas)
        tauEnergySystematic.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        tauEnergySystematic.addPlotLabel ("Tau 2016" + runPeriod)
        tauEnergySystematic.addMetCut (100.0)
        tauEnergySystematic.addRebinFactor (4)
        tauEnergySystematic.addChannel  ("TagPt35",         "TauTagPt55",              "Tau_2016"        +  runPeriod,  dirs['Andrew']+"2016/tauBackground")
        #tauEnergySystematic.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",       "Tau_2016H",                     dirs['Andrew']+"2016/tauBackground")
        tauEnergySystematic.addChannel  ("TrigEffDenom",    "ElectronTagPt55",         "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")
        tauEnergySystematic.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",  "SingleEle_2016H",               dirs['Andrew']+"2016/electronBackground")

        print "********************************************************************************"

        tauEnergySystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"
