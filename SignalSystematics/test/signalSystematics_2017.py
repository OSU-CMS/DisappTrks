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
suffix = "80X"
extraSamples = getExtraSamples (suffix)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

if systematic == "ECALO" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ECalo systematic"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic = ECaloSystematic ()
    ecaloSystematic.addChannel  ("Data",  "ZtoMuMuDisTrkNLayers4NoECaloCut",  "SingleMu_2017",  dirs['Andrew']+"2017/ecaloSystematic_atMost4Layers")
    ecaloSystematic.addChannel  ("MC",    "ZtoMuMuDisTrkNLayers4NoECaloCut",  "DYJetsToLL_50",       dirs['Andrew']+"2017/ecaloSystematic_atMost4Layers")

    print "********************************************************************************"

    ecaloSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"
