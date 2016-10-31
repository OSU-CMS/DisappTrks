#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.signalSystematics import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os
import re

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

print "********************************************************************************"
print "evaluating hits systematic"
print "--------------------------------------------------------------------------------"

hitsSystematic = HitsSystematic ()
hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2015D",   dirs['Andrew']+"2015/hitsSystematics")
hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "Background",  dirs['Andrew']+"2015/hitsSystematics")

print "********************************************************************************"

hitsSystematic.printSystematic ()

print "********************************************************************************"
