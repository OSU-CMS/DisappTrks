#!/usr/bin/env python

# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/Configuration/scripts/makeSystematicTextFile.py  

import sys
import os
import re
import math
from array import *
from decimal import *
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *

### parse the command-line options

parser = OptionParser()
parser = set_commandline_arguments(parser)

parser.remove_option("-o")
parser.remove_option("-n")
parser.remove_option("-u")
parser.remove_option("-e")
parser.remove_option("-r")
parser.remove_option("-R")
parser.remove_option("-d")
parser.remove_option("-b")
parser.remove_option("--2D")
parser.remove_option("-y")
parser.remove_option("-p")
parser.remove_option("-c")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")

from ROOT import TFile, TH1F


def getYield(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    cutFlowHistogram = inputFile.Get("OSUAnalysis/"+channel+"CutFlow")
    if not cutFlowHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0

    yield_ = cutFlowHistogram.GetBinContent(cutFlowHistogram.GetNbinsX())

    inputFile.Close()
    return yield_

def getPdfErrors(sample, condor_dir):
    inputFile = open("condor/" + condor_dir + "/upDown_" + sample + ".txt") 
    lines = inputFile.readlines()
    inputFile.close()  
    return lines[-1]  # Return the last element  


outputFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic_name + ".txt"
fout = open (outputFile, "w")

for sample in datasets:

    if usePdfWt:
        errors = getPdfErrors(sample, central_condor_dir)  
        errors = errors.split(" ")
        plus_factor  = 1.0 + float(errors[0])
        minus_factor = 1.0 - float(errors[0])  

    else: 
        minus_yield   = getYield(sample,  minus_condor_dir,channel)
        central_yield = getYield(sample,central_condor_dir,channel)
        plus_yield    = getYield(sample,   plus_condor_dir,channel)
        
        minus_factor = 1.0 + (minus_yield-central_yield)/central_yield if central_yield != 0 else 0.0
        plus_factor  = 1.0 + ( plus_yield-central_yield)/central_yield if central_yield != 0 else 0.0
        
    minus_factor = str(round_sigfigs(minus_factor,5))
    plus_factor  = str(round_sigfigs(plus_factor,5))

    line = '{0: <24}'.format(str(sample)) + " " + '{0: <8}'.format(minus_factor) + " " + '{0: <8}'.format(plus_factor) + "\n"  # format the sample name to use a fixed number of characters  
#    fout.write (sample+" "+minus_factor+" "+plus_factor+"\n")
    fout.write (line)

fout.close()
print "Finished writing systematics file: " + outputFile





