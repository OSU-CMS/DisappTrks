#!/usr/bin/env python3

class L1Seed:
    _run = None
    _name = None
    _threshold = None
    _averagePrescale = None
    _initialPrescale = None
    _finalPrescale = None

    def __init__ (self, run, name, threshold = None, countsBeforePrescale = None, countsAfterPrescale = None, initialPrescale = None, finalPrescale = None):
        if not threshold and not countsBeforePrescale and not countsAfterPrescale and not initialPrescale and not finalPrescale:
            name, threshold, countsBeforePrescale, countsAfterPrescale, initialPrescale, finalPrescale = self.parseLineFromFile (name)
        self._run = run
        self._name = name
        self._threshold = threshold
        if countsBeforePrescale is not None and countsAfterPrescale is not None:
            if countsAfterPrescale != 0:
                self._averagePrescale = float (countsBeforePrescale) / float (countsAfterPrescale)
            else:
                self._averagePrescale = 0.0
        else:
            self._averagePrescale = None
        self._initialPrescale = initialPrescale
        self._finalPrescale = finalPrescale

    def parseLineFromFile (self, line):
        name                  =  re.sub  (r"[^ ]* ([^ ]*) [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* .*",  r"\1",  line)
        if not re.match (r"^L1.*_ETM(HF)?([0-9]+)_?.*", name):
            return (None, None, None, None, None, None)
        threshold             =  re.sub  (r"^L1.*_ETM(HF)?([0-9]+)_?.*", r"\2", name)
        countsBeforePrescale  =  re.sub  (r"[^ ]* [^ ]* ([^ ]*) [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* .*",  r"\1",  line)
        countsAfterPrescale   =  re.sub  (r"[^ ]* [^ ]* [^ ]* [^ ]* ([^ ]*) [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* .*",  r"\1",  line)
        initialPrescale       =  re.sub  (r"[^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* ([^ ]*) [^ ]* .*",  r"\1",  line)
        finalPrescale         =  re.sub  (r"[^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* ([^ ]*) .*",  r"\1",  line)

        threshold            = int(threshold) if not threshold == "n/a" else None
        countsBeforePrescale = int(countsBeforePrescale) if not countsBeforePrescale == "n/a" else None
        countsAfterPrescale  = int(countsAfterPrescale) if not countsAfterPrescale == "n/a" else None
        initialPrescale      = int(initialPrescale) if not initialPrescale == "n/a" else None
        finalPrescale        = int(finalPrescale) if not finalPrescale == "n/a" else None

        return (name, threshold, countsBeforePrescale, countsAfterPrescale, initialPrescale, finalPrescale)

    def setRun (self, run):
        self._run = run

    def run (self):
        return self._run

    def name (self):
        return self._name

    def threshold (self):
        return self._threshold

    def averagePrescale (self):
        return self._averagePrescale

    def initialPrescale (self):
        return self._initialPrescale

    def finalPrescale (self):
        return self._finalPrescale

    def __str__ (self):
        return ("run: " + str (self._run) + " name: " + str (self._name) + " threshold: " + str (self._threshold) + " average_prescale: " + str (self._averagePrescale) + " initial_prescale: " + str (self._initialPrescale) + " final_prescale: " + str (self._finalPrescale))

    def __nonzero__ (self):
        return (self._name is not None)

    def __eq__ (self, other):
        if hasattr (other, "_averagePrescale"):
            return (self.threshold () == other.threshold ())
        else:
            return (self.threshold () == other)

    def __lt__ (self, other):
        if hasattr (other, "_averagePrescale"):
            return (self.threshold () < other.threshold ())
        else:
            return (self.threshold () < other)

    def __le__ (self, other):
        return (self < other or self == other)

    def __ge__ (self, other):
        return (not self < other)

    def __gt__ (self, other):
        return (not self <= other)

    def __ne__ (self, other):
        return (not self == other)

import sys, re, os, glob

# run < 299368
seedString2017_v1 = "L1_DoubleJet60er3p0_ETM60 OR L1_DoubleJet60er3p0_ETM80 OR L1_ETM100 OR L1_ETM100_Jet60_dPhi_Min0p4 OR L1_ETM105 OR L1_ETM110 OR L1_ETM115 OR L1_ETM120 OR L1_ETM150 OR L1_ETM60 OR L1_ETM70 OR L1_ETM75 OR L1_ETM75_Jet60_dPhi_Min0p4 OR L1_ETM80 OR L1_ETM85 OR L1_ETM90 OR L1_ETM95 OR L1_ETMHF100 OR L1_ETMHF100_Jet60_OR_DiJet30woTT28 OR L1_ETMHF100_Jet60_OR_DoubleJet30 OR L1_ETMHF100_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF105_Jet60_OR_DoubleJet30 OR L1_ETMHF110 OR L1_ETMHF110_Jet60_OR_DiJet30woTT28 OR L1_ETMHF110_Jet60_OR_DoubleJet30 OR L1_ETMHF110_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF115_Jet60_OR_DoubleJet30 OR L1_ETMHF120 OR L1_ETMHF120_Jet60_OR_DiJet30woTT28 OR L1_ETMHF120_Jet60_OR_DoubleJet30 OR L1_ETMHF150 OR L1_ETMHF70 OR L1_ETMHF70_Jet60_OR_DiJet30woTT28 OR L1_ETMHF70_Jet60_OR_DoubleJet30 OR L1_ETMHF70_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF75_Jet60_OR_DoubleJet30 OR L1_ETMHF80 OR L1_ETMHF80_Jet60_OR_DiJet30woTT28 OR L1_ETMHF80_Jet60_OR_DoubleJet30 OR L1_ETMHF80_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF85_Jet60_OR_DoubleJet30 OR L1_ETMHF90 OR L1_ETMHF90_Jet60_OR_DiJet30woTT28 OR L1_ETMHF90_Jet60_OR_DoubleJet30 OR L1_ETMHF90_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF95_Jet60_OR_DoubleJet30"

# run >= 299368 and run < 305113
# (HLT v2.0.0 - 3.2.1)
# HLT_MET105_IsoTrk50_v* is added
seedString2017_v2 = seedString2017_v1 + " OR " + "L1_ETM80 OR L1_ETM85 OR L1_ETM90 OR L1_ETM95 OR L1_ETM100 OR L1_ETM105 OR L1_ETM110 OR L1_ETM115 OR L1_ETM120 OR L1_ETM150"
    
# run >= 305113 and run < 305405
# (HLT v3.2.2)
seedString2017_v322 = "L1_DoubleJet60er2p7_ETM60 OR L1_DoubleJet60er2p7_ETM80 OR L1_ETM100 OR L1_ETM100_Jet60_dPhi_Min0p4 OR L1_ETM105 OR L1_ETM110 OR L1_ETM115 OR L1_ETM120 OR L1_ETM150 OR L1_ETM60 OR L1_ETM70 OR L1_ETM75 OR L1_ETM75_Jet60_dPhi_Min0p4 OR L1_ETM80 OR L1_ETM85 OR L1_ETM90 OR L1_ETM95 OR L1_ETMHF100 OR L1_ETMHF100_Jet60_OR_DiJet30woTT28 OR L1_ETMHF100_Jet60_OR_DoubleJet30 OR L1_ETMHF100_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF110 OR L1_ETMHF110_Jet60_OR_DiJet30woTT28 OR L1_ETMHF110_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF120 OR L1_ETMHF120_Jet60_OR_DiJet30woTT28 OR L1_ETMHF150 OR L1_ETMHF70 OR L1_ETMHF70_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF80 OR L1_ETMHF80_Jet90_OR_DoubleJet45_OR_TripleJet30 OR L1_ETMHF90 OR L1_ETMHF90_Jet90_OR_DoubleJet45_OR_TripleJet30" + " OR " + "L1_ETM80 OR L1_ETM85 OR L1_ETM90 OR L1_ETM95 OR L1_ETM100 OR L1_ETM105 OR L1_ETM110 OR L1_ETM115 OR L1_ETM120 OR L1_ETM150"

# run >= 305405 
# (HLT v4.0.0)
seedString2017_v4 = "L1_ETMHF80 OR L1_ETMHF80_HTT60er OR L1_ETMHF90 OR L1_ETMHF90_HTT60er OR L1_ETMHF100 OR L1_ETMHF100_HTT60er OR L1_ETMHF110 OR L1_ETMHF110_HTT60er OR L1_ETMHF120 OR L1_ETMHF120_HTT60er OR L1_ETMHF150" + " OR " + "L1_ETMHF70 OR L1_ETMHF80 OR L1_ETMHF90 OR L1_ETMHF100 OR L1_ETMHF110 OR L1_ETMHF120 OR L1_ETMHF150"

seeds2017_v1 = {}
seeds2017_v2 = {}
seeds2017_v322 = {}
seeds2017_v4 = {}

for seedName in seedString2017_v1.split(' OR '):
    threshold = re.sub(r"^L1.*_ETM(HF)?([0-9]+)_?.*", r"\2", seedName)
    if not seedName in seeds2017_v1:
        seeds2017_v1[seedName] = threshold

for seedName in seedString2017_v2.split(' OR '):
    threshold = re.sub(r"^L1.*_ETM(HF)?([0-9]+)_?.*", r"\2", seedName)
    if not seedName in seeds2017_v2:
        seeds2017_v2[seedName] = threshold

for seedName in seedString2017_v322.split(' OR '):
    threshold = re.sub(r"^L1.*_ETM(HF)?([0-9]+)_?.*", r"\2", seedName)
    if not seedName in seeds2017_v322:
        seeds2017_v322[seedName] = threshold

for seedName in seedString2017_v4.split(' OR '):
    threshold = re.sub(r"^L1.*_ETM(HF)?([0-9]+)_?.*", r"\2", seedName)
    if not seedName in seeds2017_v4:
        seeds2017_v4[seedName] = threshold

def extractL1Seeds (fileName):
    l1Seeds = []

    fin = open (fileName, "r")
    run = None

    seedsToUse = {}

    for line in fin:
        line = line.rstrip ("\n")

        if re.match (r".*<title>.*", line):
            if run is None:
                run = re.sub (r".*<title>(.*)<\/title>.*", r"\1", line)
                run = int (re.sub (r"WBM L1Summary Run ([0-9]+).*", r"\1", run))
                if run < 299368:
                    seedsToUse = seeds2017_v1
                elif run >= 299368 and run < 305113:
                    seedsToUse = seeds2017_v2
                elif run >= 305113 and run < 305405:
                    seedsToUse = seeds2017_v322
                else:
                    seedsToUse = seeds2017_v4
                continue
            else:
                continue

        isInteresting = False
        for interestingSeed in seedsToUse:
            if ">" + interestingSeed + "<" in line and "<title>" not in line:
                isInteresting = True
                break

        if not isInteresting:
            continue

        while re.match (r"[^<]*<[^>]*>.*", line):
            line = re.sub (r"([^<]*)<[^>]*>(.*)", r"\1 \2", line)
        line = re.sub (r"  *", r" ", line)
        line = re.sub (r"^ *", r"", line)

        l1Seed = L1Seed (run, line)
        if l1Seed:
            l1Seeds.append (l1Seed)

    l1Seeds = sorted (l1Seeds)
    return l1Seeds

if len (sys.argv) < 2:
    print( "Usage: " + os.path.basename (sys.argv[0]) + " HTML_FILE|HTML_DIR" )
    sys.exit (1)

fileName = None
dirName = None
if os.path.isfile (sys.argv[1]):
    fileName = sys.argv[1]
if os.path.isdir (sys.argv[1]):
    dirName = sys.argv[1]

if fileName:
    for l1Seed in extractL1Seeds (fileName):
        print l1Seed
if dirName:
    for fileName in glob.glob (dirName + "/*"):
        for l1Seed in extractL1Seeds (fileName):
            print l1Seed
