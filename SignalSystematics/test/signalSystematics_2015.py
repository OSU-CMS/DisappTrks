#!/usr/bin/env python

import math
from DisappTrks.SignalSystematics.signalSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import TFile
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700, 800, 900]
lifetimes = [10, 100, 1000, 10000]
allTheLifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                   '20', '30', '40', '50', '60', '70', '80', '90', '100',
                   '200', '300', '400', '500', '600', '700', '800', '900', '1000',
                   '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
suffix = "76X"
extraSamples = getExtraSamples (suffix)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2015.txt", "w")

    pileupSystematic = PileupSystematic (masses, lifetimes)
    pileupSystematic.addFout (fout)
    pileupSystematic.addExtraSamples (extraSamples)
    pileupSystematic.addChannel  ("PileupCentral",  "DisTrkSelection",  suffix,  dirs['Andrew']+"2015/disappearingTracks_signal")
    pileupSystematic.addChannel  ("PileupDown",     "DisTrkSelection",  suffix,  dirs['Andrew']+"2015/disappearingTracks_signal_puDown")
    pileupSystematic.addChannel  ("PileupUp",       "DisTrkSelection",  suffix,  dirs['Andrew']+"2015/disappearingTracks_signal_puUp")
    pileupSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "MET" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating met systematics"
    print "--------------------------------------------------------------------------------"

    metVaryTypes = [
        'JetRes',
        'JetEn',
        'ElectronEn',
        'TauEn',
        'UnclusteredEn',
        'PhotonEn',
    ]

    metSystematic = MetSystematic (masses, lifetimes)
    metSystematic.addExtraSamples (extraSamples)
    metSystematic.addChannel ("central", "DisTrkNoMet", suffix, dirs['Andrew']+"2015/jetSystematics")
    metSystematic.addChannel ("down",    "DisTrkNoMet", suffix, dirs['Andrew']+"2015/jetSystematics")
    metSystematic.addChannel ("up",      "DisTrkNoMet", suffix, dirs['Andrew']+"2015/jetSystematics")
    metSystematic.addMetTypes (metVaryTypes)
    metSystematic.setMetCut (100.0)
    metSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__metVary", "2015.txt")
    metSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jec_2015.txt", "w")

    jecSystematic = YieldSystematic (masses, lifetimes)
    jecSystematic.addFout (fout)
    jecSystematic.addExtraSamples (extraSamples)
    jecSystematic.addChannel  ("central",  "disTrkSelectionSmearedJets",         suffix,  dirs['Andrew']+"2015/jetSystematics")
    jecSystematic.addChannel  ("down",     "disTrkSelectionSmearedJetsJECUp",    suffix,  dirs['Andrew']+"2015/jetSystematics")
    jecSystematic.addChannel  ("up",       "disTrkSelectionSmearedJetsJECDown",  suffix,  dirs['Andrew']+"2015/jetSystematics")
    jecSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "JER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JER systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jer_2015.txt", "w")

    jerSystematic = YieldSystematic (masses, lifetimes)
    jerSystematic.addFout (fout)
    jerSystematic.addExtraSamples (extraSamples)
    jerSystematic.addChannel  ("central", "disTrkSelectionSmearedJets",      suffix,  dirs['Andrew']+"2015/jetSystematics")
    jerSystematic.addChannel  ("up",      "disTrkSelectionSmearedJetsUp",    suffix,  dirs['Andrew']+"2015/jetSystematics")
    jerSystematic.addChannel  ("down",    "disTrkSelectionSmearedJetsDown",  suffix,  dirs['Andrew']+"2015/jetSystematics")
    jerSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic"
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__isr_2015.txt", "w")

    isrSystematic = YieldSystematic (masses, lifetimes)
    isrSystematic.setIsWeightFluctuation (True)
    isrSystematic.addFout (fout)
    isrSystematic.addExtraSamples (extraSamples)
    isrSystematic.addChannel ("central", "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2015/signalISRSystematics_final")
    isrSystematic.addChannel ("up",      "disTrkSelectionSmearedJetsPlotter_isrWeightUp", suffix, dirs['Brian']+"2015/signalISRSystematics_final")
    isrSystematic.addChannel ("down",    "disTrkSelectionSmearedJetsPlotter_isrWeightDown", suffix, dirs['Brian']+"2015/signalISRSystematics_final")
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ECALO" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ECalo systematic"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic = ECaloSystematic ()
    ecaloSystematic.addChannel  ("Data",  "ZtoMuMuDisTrkNHits4NoECaloCut",  "SingleMu_2015D",  dirs['Andrew']+"2015/ecaloSystematic")
    ecaloSystematic.addChannel  ("MC",    "ZtoMuMuDisTrkNHits4NoECaloCut",  "Background",      dirs['Andrew']+"2015/ecaloSystematic")

    print "********************************************************************************"

    ecaloSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating hits systematic"
    print "--------------------------------------------------------------------------------"

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2015D",   dirs['Andrew']+"2015/hitsSystematics_hist_new")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "Background",  dirs['Andrew']+"2015/hitsSystematics_hist_new")
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleVsInner")
    print "--------------------------------------------------------------------------------"
    print "before correction to missing middle hits"
    hitsSystematic.printSystematic ()
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleCorrectedVsInner")
    print "--------------------------------------------------------------------------------"
    print "after correction to missing middle hits"
    hitsSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "MISSING_OUTER_HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating missing outer hits systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__nMissOut_2015.txt", "w")
    foutForPlot = TFile.Open ("nMissOutSystematic_2015.root", "recreate")

    missingOuterHitsSystematic_2015 = MissingOuterHitsSystematic (masses, allTheLifetimes)
    #missingOuterHitsSystematic_2015 = MissingOuterHitsSystematic (masses, lifetimes)
    missingOuterHitsSystematic_2015.addFout (fout)
    missingOuterHitsSystematic_2015.addFoutForPlot (foutForPlot)
    missingOuterHitsSystematic_2015.addSignalSuffix ("_" + suffix)
    missingOuterHitsSystematic_2015.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    missingOuterHitsSystematic_2015.addChannel  ("Data",    "MuonCtrlSelection",  "MET_2015D",         dirs['Andrew']+"2015/hipAndTOBDrop")
    missingOuterHitsSystematic_2015.addChannel  ("MC",      "MuonCtrlSelection",  "Background_noQCD",  dirs['Andrew']+"2015/hipAndTOBDrop")
    missingOuterHitsSystematic_2015.addChannel  ("Signal",  "DisTrkNoNMissOut",   "",                  dirs['Andrew']+"2016_final_prompt/disTrkSelection_noNMissOutCut_2015")
    missingOuterHitsSystematic_2015.printSystematic ()

    print "********************************************************************************"

    fout.close ()
    foutForPlot.Close ()

if systematic == "TRIGGER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics"
    print "--------------------------------------------------------------------------------"

    triggerFluctuations = [
        'grandOrWeightData',
        'grandOrWeightMC',
    ]

    triggerSystematic = TriggerSystematic (masses, lifetimes)
    triggerSystematic.addExtraSamples (extraSamples)
    triggerSystematic.addChannel ("central", "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2015/triggerSystematics_final")
    triggerSystematic.addChannel ("down",    "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2015/triggerSystematics_final")
    triggerSystematic.addChannel ("up",      "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2015/triggerSystematics_final")
    triggerSystematic.addTriggerFluctuations (triggerFluctuations)
    triggerSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_", "2015.txt")
    triggerSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"
