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
suffix = "76X"
extraSamples = {
    "AMSB_chargino_100GeV_10000cm_76X" : [],
    "AMSB_chargino_100GeV_1000cm_76X" : [],
    "AMSB_chargino_100GeV_100cm_76X" : [],
    "AMSB_chargino_100GeV_10cm_76X" : [],
    "AMSB_chargino_200GeV_10000cm_76X" : [],
    "AMSB_chargino_200GeV_1000cm_76X" : [],
    "AMSB_chargino_200GeV_100cm_76X" : [],
    "AMSB_chargino_200GeV_10cm_76X" : [],
    "AMSB_chargino_300GeV_10000cm_76X" : [],
    "AMSB_chargino_300GeV_1000cm_76X" : [],
    "AMSB_chargino_300GeV_100cm_76X" : [],
    "AMSB_chargino_300GeV_10cm_76X" : [],
    "AMSB_chargino_400GeV_10000cm_76X" : [],
    "AMSB_chargino_400GeV_1000cm_76X" : [],
    "AMSB_chargino_400GeV_100cm_76X" : [],
    "AMSB_chargino_400GeV_10cm_76X" : [],
    "AMSB_chargino_500GeV_10000cm_76X" : [],
    "AMSB_chargino_500GeV_1000cm_76X" : [],
    "AMSB_chargino_500GeV_100cm_76X" : [],
    "AMSB_chargino_500GeV_10cm_76X" : [],
    "AMSB_chargino_600GeV_10000cm_76X" : [],
    "AMSB_chargino_600GeV_1000cm_76X" : [],
    "AMSB_chargino_600GeV_100cm_76X" : [],
    "AMSB_chargino_600GeV_10cm_76X" : [],
    "AMSB_chargino_700GeV_10000cm_76X" : [],
    "AMSB_chargino_700GeV_1000cm_76X" : [],
    "AMSB_chargino_700GeV_100cm_76X" : [],
    "AMSB_chargino_700GeV_10cm_76X" : [],
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
    print "evaluating pileup systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__pileup_2015.txt", "w")

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
    metSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__metVary", "2015.txt")
    metSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__jec_2015.txt", "w")

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

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/StandardAnalysis/data/systematic_values__jer_2015.txt", "w")

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
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2015D",   dirs['Andrew']+"2015/hitsSystematics")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "Background",  dirs['Andrew']+"2015/hitsSystematics")

    print "********************************************************************************"

    hitsSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "MISSING_OUTER_HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating missing outer hits systematic"
    print "--------------------------------------------------------------------------------"

    missingOuterHitsSystematic = MissingOuterHitsSystematic ()
    missingOuterHitsSystematic.addChannel  ("Data",  "MuonCtrlSelection",  "MET_2015D",   dirs['Andrew']+"2015/hipAndTOBDrop_new")
    missingOuterHitsSystematic.addChannel  ("MC",    "MuonCtrlSelection",  "Background",  dirs['Andrew']+"2015/hipAndTOBDrop_new")
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
