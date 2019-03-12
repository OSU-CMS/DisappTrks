#!/usr/bin/env python

import math
from DisappTrks.SignalSystematics.signalSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TFile
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700, 800, 900]
lifetimes = ['1', '10', '100', '1000', '10000']
allLiftimes = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1',
               '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '20', '30', '40', '50', '60', '70', '80', '90', '100',
               '200', '300', '400', '500', '600', '700', '800', '900', '1000',
               '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
suffix = "94X"

extraSamples = getExtraSamples(suffix)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

nLayersWord = "NLayers4"
if len(sys.argv) > 2:
    nLayersWord = sys.argv[2]

lumi = lumi["MET_2017"]

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2017_" + nLayersWord + ".txt", "w")

    pileupSystematic = WeightSystematicFromTrees(masses, allLiftimes, lumi)
    pileupSystematic.addFout(fout)
    pileupSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_full_v7")
    pileupSystematic.defineWeightToFluctuate('eventvariable_puScalingFactor')
    pileupSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

if systematic == "MET" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating met systematics (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    metVaryTypes = [
        'JetRes',
        'JetEn',
        'ElectronEn',
        'TauEn',
        'UnclusteredEn',
        'PhotonEn',
    ]

    metSystematic = MetSystematic(masses, lifetimes)
    metSystematic.addExtraSamples(extraSamples)
    metSystematic.addChannel("central", "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7_metSyst")
    metSystematic.addChannel("up",      "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7_metSyst")
    metSystematic.addChannel("down",    "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7_metSyst")
    metSystematic.addMetTypes(metVaryTypes)
    metSystematic.setMetCut(120.0)
    metSystematic.setFoutNames(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__metVary", "2017_" + nLayersWord + ".txt")
    metSystematic.printSystematic()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jec_2017_" + nLayersWord + ".txt", "w")

    jecSystematic = SystematicCalculator(masses, lifetimes)
    jecSystematic.addFout(fout)
    jecSystematic.addExtraSamples(extraSamples)
    jecSystematic.addChannel("central", "disTrkSelectionSmearedJets"        + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_full_v7")
    jecSystematic.addChannel("down",    "disTrkSelectionSmearedJetsJECUp"   + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_full_v7_jecSyst")
    jecSystematic.addChannel("up",      "disTrkSelectionSmearedJetsJECDown" + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_full_v7_jecSyst")
    jecSystematic.printSystematic()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "JER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JER systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jer_2017_" + nLayersWord + ".txt", "w")

    jerSystematic = SystematicCalculator(masses, lifetimes)
    jerSystematic.addFout(fout)
    jerSystematic.addExtraSamples(extraSamples)
    jerSystematic.addChannel("central",  "disTrkSelectionSmearedJets"     + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_full_v7")
    jerSystematic.addChannel("down",     "disTrkSelectionSmearedJetsUp"   + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_full_v7_jerSyst")
    jerSystematic.addChannel("up",       "disTrkSelectionSmearedJetsDown" + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_full_v7_jerSyst")
    jerSystematic.printSystematic()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__isr_2017_" + nLayersWord + ".txt", "w")

    isrSystematic = WeightSystematicFromTrees(masses, allLiftimes, lumi)
    isrSystematic.addFout(fout)
    isrSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_full_v7")
    isrSystematic.defineWeightToFluctuate('eventvariable_isrWeight')
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "TRIGGER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    for flux in ['Data', 'MC']:
        fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_grandOrWeight" + flux + '_2017_' + nLayersWord + ".txt", "w")

        triggerSystematic = WeightSystematicFromTrees(masses, allLiftimes, lumi)
        triggerSystematic.addFout(fout)
        triggerSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_full_v7")
        triggerSystematic.defineFluctuationUp  ('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Up')
        triggerSystematic.defineFluctuationDown('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Down')
        triggerSystematic.printSystematic()

    print "********************************************************************************\n\n"

    print "\n\n"

if systematic == "ECALO" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ECalo systematic (2017)"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic = ECaloSystematic ()
    ecaloSystematic.addChannel  ("Data",  "ZtoMuMuDisTrkNLayers4NoECaloCut",  "SingleMu_2017",  dirs['Andrew'] + "2017/ecaloSystematic_atMost4Layers")
    ecaloSystematic.addChannel  ("MC",    "ZtoMuMuDisTrkNLayers4NoECaloCut",  "DYJetsToLL_50",  dirs['Andrew'] + "2017/ecaloSystematic_atMost4Layers")

    print "********************************************************************************"

    ecaloSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating hits systematic (2017)"
    print "--------------------------------------------------------------------------------"

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2017",     dirs['Brian'] + "2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "AllMC_scaled", dirs['Brian'] + "2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
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
    print "evaluating missing outer hits systematic (2017)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__nMissOut_2017.txt", "w")
    foutForPlot = TFile.Open ("nMissOutSystematic_2017.root", "recreate")

    missingOuterHitsSystematic = MissingOuterHitsSystematic (masses, lifetimes)
    missingOuterHitsSystematic.addFout (fout)
    missingOuterHitsSystematic.addFoutForPlot (foutForPlot)
    missingOuterHitsSystematic.addSignalSuffix ("_" + suffix)
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    missingOuterHitsSystematic.addChannel  ("Data",    "MuonCtrlSelection",                "MET_2017",     dirs['Brian'] + "2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
    missingOuterHitsSystematic.addChannel  ("MC",      "MuonCtrlSelection",                "AllMC_scaled", dirs['Brian'] + "2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
    missingOuterHitsSystematic.addChannel  ("Signal",  "DisTrkNoNMissOut" + nLayersWord,   "",             dirs['Brian'] + "2017/signalAcceptance_full_v7_noNMissOutCut")
    missingOuterHitsSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()
    foutForPlot.Close ()

    print "\n\n"
