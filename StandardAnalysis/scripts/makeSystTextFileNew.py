#!/usr/bin/env python3

# Calculates the systematic uncertainty associated with Ecalo, by reweighting data and MC distributions by the signal distribution, then taking the difference in yields.
#
# Example usage:
# Usage:  makeSystTextFileNew.py -l systematicConfig_IsrVaryNew.py

import sys
import os
import re
from math import *
from array import *
from decimal import *
from optparse import OptionParser
import copy
from operator import itemgetter

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *

parser = OptionParser()
parser.add_option("-s", "--singleSample", action="store_true", dest="singleSample", default=False,
                  help="run over a single sample")
parser = set_commandline_arguments(parser)
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")


def getIntegral(sample, condor_dir, channel, hist, xlo, xhi, hwts):
    inputFile = TFile("condor/"+condor_dir+"/"+sample+".root")
    #print "Reading file:  " + inputFile.GetName()

    HistogramObj = inputFile.Get("OSUAnalysis/"+channel+"/"+hist)
    if not HistogramObj:
        print "WARNING: Could not find histogram " + "OSUAnalysis/"+channel+"/"+hist + " in file " + sample +".root" + ". Will skip it and continue."
        return
    histogram = HistogramObj.Clone()
    histogram.SetDirectory(0)
    inputFile.Close()

    xloBin = histogram.GetXaxis().FindBin(float(xlo))
    xhiBin = histogram.GetXaxis().FindBin(float(xhi))
    xlo = histogram.GetXaxis().GetBinLowEdge(xloBin)   # lo edge is the left edge of the first bin
    xhi = histogram.GetXaxis().GetBinLowEdge(xhiBin+1) # hi edge is the left edge of the bin to the right of the last bin

    if hwts:
        for i in range(1,histogram.GetNbinsX()+1):
            val = histogram.GetBinContent(i)
            err = histogram.GetBinError(i)
            binCtr = histogram.GetBinCenter(i)
            wt = hwts.GetBinContent(hwts.FindBin(binCtr)) + 1.0 # Add 1.0, to convert from (data-MC)/MC to data/MC
#            print "Debug:  bin ", i, ": wt=", wt
            histogram.SetBinContent(i, val * wt)
            histogram.SetBinError  (i, err * wt)
    intError = Double (0.0)
    integral = histogram.IntegralAndError(xloBin, xhiBin, intError)

    line = "Integral of " + hist + " in " + inputFile.GetName() + " from " + str(xlo) + " to " + str(xhi) + ": " + str (integral) + " +- " + str (intError)
#    print line
    return integral


outputFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic_name + ".txt"
if not makeRewtdPlot:
    fout = open (outputFile, "w")

# get rewt histogram
fileWithWtHist = TFile(str(ratioHistFile))
hwts = fileWithWtHist.Get(ratioHistName)
print "Debug:  using hwts hist=", ratioHistName, ", ratioHistFile=", ratioHistFile

for sample in datasets:

    numEvents         = getIntegral(sample, central_condor_dir,     channel,       "numEvents",                  0, 10, 0)
    central_yield     = getIntegral(sample, central_condor_dir,     channel,       histRewtName, histMin, histMax, 0)
    plus_yield        = getIntegral(sample, central_condor_dir,     channel,       histRewtName, histMin, histMax, hwts)
    central_gen_yield = getIntegral(sample, central_gen_condor_dir, channelNoCuts, histRewtName, histMin, histMax, 0)
    plus_gen_yield    = getIntegral(sample, central_gen_condor_dir, channelNoCuts, histRewtName, histMin, histMax, hwts)
    effOrig = float(central_yield) / central_gen_yield
    effRewt = plus_yield / plus_gen_yield
    plus_factor  = effRewt / effOrig  # Kevin method
#    plus_factor  = plus_yield / central_yield  # Method 2:  do not compare gen yields
    minus_factor = 1.0 / plus_factor
    #    print "Debug:  sample=", sample, ", central_yield=", central_yield, ", plus_yield=", plus_yield, ", central_gen_yield=", central_gen_yield, ", plus_gen_yield=", plus_gen_yield # ", effOrig=", effOrig, ", effRewt=", effRewt, ", plus_factor=", plus_factor, ", minus_factor=", minus_factor
    line = '{0: <40}'.format(str(sample)) + " Y^wt_full / Y_full = " + '{0: <5}'.format(plus_yield/central_yield) + ", Y^wt_gen / Y_gen = " + '{0: <8}'.format(plus_gen_yield/central_gen_yield) + ", sigma = " +  '{0: <8}'.format(plus_factor - 1.0)
    print line

    #    print "Debug:  sample=", sample, ", Y^wt_full / Y_full = ", plus_yield/central_yield, ", Y^wt_gen / Y_gen = ", plus_gen_yield/central_gen_yield, ", sigma = =", plus_factor - 1.0

    #    print "Found systematic error: " + str(plus_factor)
    if makeRewtdPlot:
        command = "rewtHist.py -p -f " + ratioHistFile + " -i " + ratioHistName + " -c " + central_condor_dir + " -n OSUAnalysis/" + channel + "/" + histRewtName + " -d " + sample
        print "Running:  " + command
        os.system(command + " -l localOptionsCtrlMuon.py")
#        plotCmd = "makePlots.py -l localOptionsAll2.py " + histRewtName_Reweighted -f -N " + str(normFactor) + " -l localOptionsCtrlMuon.py -c " + condor_dir + " -o stacked_histogramsRewt_" + sample + ".root"
#        print "Running:  " + plotCmd
#        os.system(plotCmd)

    line = '{0: <40}'.format(str(sample)) + " " + '{0: <8}'.format(minus_factor) + " " + '{0: <8}'.format(plus_factor) + "\n" # format the sample name to use a fixed number of characters
#    print line
    if not makeRewtdPlot:
        fout.write (line)
if not makeRewtdPlot:
    fout.close()
    print "Finished writing systematics file: " + outputFile






