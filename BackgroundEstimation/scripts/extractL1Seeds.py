#!/usr/bin/env python

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
        if not re.match (r"^L1_ETM[0-9]+$", name):
            return (None, None, None, None, None, None)
        threshold             =  re.sub  (r"^L1_ETM([0-9]+)$", r"\1", name)
        countsBeforePrescale  =  re.sub  (r"[^ ]* [^ ]* ([^ ]*) [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* .*",  r"\1",  line)
        countsAfterPrescale   =  re.sub  (r"[^ ]* [^ ]* [^ ]* [^ ]* ([^ ]*) [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* .*",  r"\1",  line)
        initialPrescale       =  re.sub  (r"[^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* ([^ ]*) [^ ]* .*",  r"\1",  line)
        finalPrescale         =  re.sub  (r"[^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* [^ ]* ([^ ]*) .*",  r"\1",  line)

        return (name, int (threshold), int (countsBeforePrescale), int (countsAfterPrescale), int (initialPrescale), int (finalPrescale))

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

    def __gt__ (self, other):
        return (not self < other)

    def __ge__ (self, other):
        return (self > other or self == other)

    def __ne__ (self, other):
        return (not self == other)

import sys, re, os, glob

def extractL1Seeds (fileName):
    l1Seeds = []

    fin = open (fileName, "r")
    run = None
    for line in fin:
        if not re.match (r".*L1_ETM.*", line) and not re.match (r".*<title>.*", line):
            continue;

        line = line.rstrip ("\n")

        if re.match (r".*<title>.*", line):
            run = re.sub (r".*<title>(.*)<\/title>.*", r"\1", line)
            run = int (re.sub (r"WBM L1Summary Run ([0-9]+).*", r"\1", run))
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
    print "Usage: " + os.path.basename (sys.argv[0]) + " HTML_FILE|HTML_DIR"
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
