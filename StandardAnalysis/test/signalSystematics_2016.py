#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.signalSystematics import *
from DisappTrks.StandardAnalysis.getUser import *
from ROOT import TCanvas, TFile
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700]
lifetimes = [10, 100, 1000, 10000]
suffix = "80X"
extraSamples = {
    "AMSB_chargino_100GeV_10000cm_80X" : [],
    "AMSB_chargino_100GeV_1000cm_80X" : [],
    "AMSB_chargino_100GeV_100cm_80X" : [],
    "AMSB_chargino_100GeV_10cm_80X" : [],
    "AMSB_chargino_200GeV_10000cm_80X" : [],
    "AMSB_chargino_200GeV_1000cm_80X" : [],
    "AMSB_chargino_200GeV_100cm_80X" : [],
    "AMSB_chargino_200GeV_10cm_80X" : [],
    "AMSB_chargino_300GeV_10000cm_80X" : [],
    "AMSB_chargino_300GeV_1000cm_80X" : [],
    "AMSB_chargino_300GeV_100cm_80X" : [],
    "AMSB_chargino_300GeV_10cm_80X" : [],
    "AMSB_chargino_400GeV_10000cm_80X" : [],
    "AMSB_chargino_400GeV_1000cm_80X" : [],
    "AMSB_chargino_400GeV_100cm_80X" : [],
    "AMSB_chargino_400GeV_10cm_80X" : [],
    "AMSB_chargino_500GeV_10000cm_80X" : [],
    "AMSB_chargino_500GeV_1000cm_80X" : [],
    "AMSB_chargino_500GeV_100cm_80X" : [],
    "AMSB_chargino_500GeV_10cm_80X" : [],
    "AMSB_chargino_600GeV_10000cm_80X" : [],
    "AMSB_chargino_600GeV_1000cm_80X" : [],
    "AMSB_chargino_600GeV_100cm_80X" : [],
    "AMSB_chargino_600GeV_10cm_80X" : [],
    "AMSB_chargino_700GeV_10000cm_80X" : [],
    "AMSB_chargino_700GeV_1000cm_80X" : [],
    "AMSB_chargino_700GeV_100cm_80X" : [],
    "AMSB_chargino_700GeV_10cm_80X" : [],
}

for sample in extraSamples:
    if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_.*', sample):
        continue
    mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_.*', r'\1', sample)
    ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_.*', r'\1', sample))
    suffix = re.sub (r'AMSB_chargino_[^_]*GeV_[^_]*cm_(.*)', r'\1', sample)
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

        extraSamples[sample].append (dataset)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__pileup_2016BC.txt", "w")

    pileupSystematic_v3 = PileupSystematic (masses, lifetimes)
    pileupSystematic_v3.addFout (fout)
    pileupSystematic_v3.addExtraSamples (extraSamples)
    pileupSystematic_v3.addChannel  ("PileupCentral",  "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToBC")
    pileupSystematic_v3.addChannel  ("PileupDown",     "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToBC_puDown")
    pileupSystematic_v3.addChannel  ("PileupUp",       "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToBC_puUp")
    pileupSystematic_v3.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "********************************************************************************"
    print "evaluating pileup systematic (2016D)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__pileup_2016D.txt", "w")

    pileupSystematic_v4 = PileupSystematic (masses, lifetimes)
    pileupSystematic_v4.addFout (fout)
    pileupSystematic_v4.addExtraSamples (extraSamples)
    pileupSystematic_v4.addChannel  ("PileupCentral",  "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToD")
    pileupSystematic_v4.addChannel  ("PileupDown",     "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToD_puDown")
    pileupSystematic_v4.addChannel  ("PileupUp",       "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToD_puUp")
    pileupSystematic_v4.printSystematic ()

    print "********************************************************************************"

    fout.close ()

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
    metSystematic.addChannel ("central", "DisTrkNoMet", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    metSystematic.addChannel ("down",    "DisTrkNoMet", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    metSystematic.addChannel ("up",      "DisTrkNoMet", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    metSystematic.addMetTypes (metVaryTypes)
    metSystematic.setMetCut (100.0)
    metSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__metVary", "2016.txt")
    metSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__jec_2016.txt", "w")

    jecSystematic = YieldSystematic (masses, lifetimes)
    jecSystematic.addFout (fout)
    jecSystematic.addExtraSamples (extraSamples)
    jecSystematic.addChannel  ("central",  "disTrkSelectionSmearedJets",         suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jecSystematic.addChannel  ("down",     "disTrkSelectionSmearedJetsJECUp",    suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jecSystematic.addChannel  ("up",       "disTrkSelectionSmearedJetsJECDown",  suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jecSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "JER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JER systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__jer_2016.txt", "w")

    jerSystematic = YieldSystematic (masses, lifetimes)
    jerSystematic.addFout (fout)
    jerSystematic.addExtraSamples (extraSamples)
    jerSystematic.addChannel  ("central", "disTrkSelectionSmearedJets",      suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jerSystematic.addChannel  ("up",      "disTrkSelectionSmearedJetsUp",    suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jerSystematic.addChannel  ("down",    "disTrkSelectionSmearedJetsDown",  suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jerSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating hits systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2016BC",   dirs['Andrew']+"2016/hitsSystematics")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "Background",  dirs['Andrew']+"2016/hitsSystematics_hist")
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
    print "evaluating missing outer hits systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    missingOuterHitsSystematic = MissingOuterHitsSystematic ()
    missingOuterHitsSystematic.addChannel  ("Data",  "MuonCtrlSelection",  "MET_2016BC",   dirs['Andrew']+"2016/hipAndTOBDrop")
    missingOuterHitsSystematic.addChannel  ("MC",    "MuonCtrlSelection",  "Background",  dirs['Andrew']+"2016/hipAndTOBDrop_new")
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuter")
    print "--------------------------------------------------------------------------------"
    print "before correction to missing outer hits"
    missingOuterHitsSystematic.printSystematic ()
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    print "--------------------------------------------------------------------------------"
    print "after correction to missing outer hits"
    missingOuterHitsSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic"
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__isr_2016.txt", "w")

    isrSystematic = YieldSystematic (masses, lifetimes)
    isrSystematic.addFout (fout)
    isrSystematic.addExtraSamples (extraSamples)
    isrSystematic.addChannel ("central", "disTrkSelectionSmearedJets", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    isrSystematic.addChannel ("up",      "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"isrSystematic_80X")
    isrSystematic.addChannel ("down",    "disTrkSelectionSmearedJets", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"
