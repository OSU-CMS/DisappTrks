#!/usr/bin/env python3

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
if not (os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_")):
    exec("from DisappTrks.SignalMC.signalCrossSecs import *")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    exec("from DisappTrks.SignalMC.signalCrossSecs13p6TeV import *")
#from lumiMet2012 import *

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


def getGenYield(sample):
    mass = re.sub(r"AMSB_chargino_([^_]*)GeV_RewtCtau[^_]*cm", r"\1", sample)
    print "Debug:  checking mass=", mass, " for sample=", sample
    crossSec = float(signal_cross_sections[mass]['value'])
    genYield = intLumi * crossSec
    print "Debug:  using crossSec=", crossSec, ", intLumi=", intLumi, ", genYield=", genYield
    return genYield


outputFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic_name + ".txt"
fout = open (outputFile, "w")

for sample in datasets:

    if usePdfWt:
        errorsCTEQ  = getPdfErrors(sample, condor_dir_CTEQ);  errorsCTEQ  = errorsCTEQ.split(" ")
        errorsMSTW  = getPdfErrors(sample, condor_dir_MSTW);  errorsMSTW  = errorsMSTW.split(" ")
        errorsNNPDF = getPdfErrors(sample, condor_dir_NNPDF); errorsNNPDF = errorsNNPDF.split(" ")
        errorMax = max(errorsCTEQ[0], errorsMSTW[0], errorsNNPDF[0])
        plus_factor  = 1.0 + float(errorMax)
        minus_factor = 1.0 - float(errorMax)
    elif useEfficiency:
        central_yield = getYield(sample,central_condor_dir,channel)
        plus_yield    = getYield(sample,   plus_condor_dir,channel)
        central_gen_yield = getYield(sample, central_gen_condor_dir,channelNoCuts)
        plus_gen_yield    = getYield(sample, plus_gen_condor_dir,   channelNoCuts)
        effOrig = central_yield / central_gen_yield
        effRewt = plus_yield / plus_gen_yield
        plus_factor  = effRewt / effOrig
#        minus_factor = 1.0 / plus_factor if plus_factor != 0 else 0.0
        minus_factor = plus_factor
#        print "Debug:  sample=", sample, ", central_yield=", central_yield, ", plus_yield=", plus_yield, ", central_gen_yield=", central_gen_yield, ", plus_gen_yield=", plus_gen_yield, ", effOrig=", effOrig, ", effRewt=", effRewt, ", plus_factor=", plus_factor, ", minus_factor=", minus_factor
        print "Debug:  sample=", sample, ", plus/central=", plus_yield/central_yield, ", plus_gen/central_gen=", plus_gen_yield/central_gen_yield, ", plus_factor=", plus_factor
    else:
#        central_gen_yield = getGenYield(sample)   # testing
        minus_yield   = getYield(sample,  minus_condor_dir,channel)
#        minus_yield   = getYield(sample,  minus_condor_dir,"FullSelectionFilterMC")
        central_yield = getYield(sample,central_condor_dir,channel)
        plus_yield    = getYield(sample,   plus_condor_dir,channel)

        minus_factor = 1.0 + (minus_yield-central_yield)/central_yield if central_yield != 0 else 0.0
        plus_factor  = 1.0 + ( plus_yield-central_yield)/central_yield if central_yield != 0 else 0.0

    minus_factor = str(round_sigfigs(minus_factor,5))
    plus_factor  = str(round_sigfigs(plus_factor,5))

    line = '{0: <40}'.format(str(sample)) + " " + '{0: <8}'.format(minus_factor) + " " + '{0: <8}'.format(plus_factor) + "\n"  # format the sample name to use a fixed number of characters
#    fout.write (sample+" "+minus_factor+" "+plus_factor+"\n")
    fout.write (line)

fout.close()
print "Finished writing systematics file: " + outputFile





