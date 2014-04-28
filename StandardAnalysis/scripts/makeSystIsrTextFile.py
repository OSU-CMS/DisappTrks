#!/usr/bin/env python

# getHistIntegrals.py
# Prints the integral of specified histograms over the specified range.  
#
# Example usage:
# Usage:  makeSystIsrTextFile.py -l systematicConfig_IsrVary.py  

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
parser = set_commandline_arguments(parser)
(arguments, args) = parser.parse_args()  

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")


#for hist in input_hists:     # loop over different input hists in config file


def getIntegral(sample, hist, xlo, xhi):     
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
    intError = Double (0.0)
    integral = histogram.IntegralAndError(xloBin, xhiBin, intError)

    line = "Integral of " + hist + " in " + inputFile.GetName() + " from " + str(xlo) + " to " + str(xhi) + ": " + str (integral) + " +- " + str (intError)
    print line 
    return integral  


outputFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic_name + ".txt"
fout = open (outputFile, "w")  

for sample in datasets:
    # FIXME:  Do not need to re-run mergeOutput.py, if you instead just do rewtHist.py for the data and the sum of all background.
    # Those datasets should be specified as an argument rather than passing in localOptionsCtrlDblMuon.py.  
    os.system("rewtHist.py -b 5 -l localOptionsCtrlDblMuon.py -f condor/condor_2014_03_07_NoCutsFilterMC/" + sample + ".root -i OSUAnalysis/FullSelectionFilterMC/totalMcparticlePt -c " + condor_dir + " -n OSUAnalysis/" + channel + "/totalMuonPt")      
    os.system("mergeOutput.py -q -C -s Background -l localOptionsCtrlDblMuon.py -c " + condor_dir)  
    yieldDataTot = getIntegral('DoubleMu_22Jan2013', 'numEvents', 0, 10) 
    yieldBkgdTot = getIntegral('Background',         'numEvents', 0, 10) 
    yieldDataPt  = getIntegral('DoubleMu_22Jan2013', 'totalMuonPt_Reweighted', 0, 500) 
    yieldBkgdPt  = getIntegral('Background',         'totalMuonPt_Reweighted', 0, 500) 
    normFactor   = yieldDataTot / yieldBkgdTot
    plus_factor  = yieldDataPt / (yieldBkgdPt * normFactor)
    minus_factor = plus_factor 
    print "Found systematic error: " + str(plus_factor)
    
    line = '{0: <24}'.format(str(sample)) + " " + '{0: <8}'.format(minus_factor) + " " + '{0: <8}'.format(plus_factor) + "\n" # format the sample name to use a fixed number of characters
    print line    
    fout.write (line)

fout.close()
print "Finished writing systematics file: " + outputFile  






