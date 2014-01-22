#!/usr/bin/env python

# Sample usage:
# ../scripts/bkgdFromData.py -l bkgdFromDataPreSel.py -c condor_2014_01_13_BkgdEstFromData
# -c:  output directory
# -l:  local options to specify scale factors and errors, datasets 

import sys
import os
import re
from math import *
from array import *
from decimal import *
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

from ROOT import TFile, gROOT, gDirectory, TH1, TH2, TH3, TIter, TKey
gROOT.SetBatch()

parser = OptionParser()
parser = set_commandline_arguments(parser)

parser.remove_option("-d")
parser.remove_option("-n")
parser.remove_option("-u")
parser.remove_option("-e")
parser.remove_option("-R")
parser.remove_option("-b")
parser.remove_option("-y")
parser.remove_option("-p")
parser.remove_option("-r")
parser.remove_option("-o")
parser.remove_option("--2D")

(arguments, args) = parser.parse_args()

condor_dir = set_condor_output_dir(arguments)
os.system("mkdir -p " + condor_dir)  

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
    os.system("cp " + arguments.localConfig + " " + condor_dir + "/bkgdOptions.py")   # make a copy of the local options file  
else:
    print "ERROR:  Must specify configuration options file with option -l." 



########################################################
########################################################
def applySF (Histogram, sf, sfError):
    xLimit = Histogram.GetNbinsX () + 2
    yLimit = Histogram.GetNbinsY () + 2
    zLimit = Histogram.GetNbinsZ () + 2
    if yLimit == 3:
      yLimit = 1
    if zLimit == 3:
      zLimit = 1
    for x in range (0, xLimit):
        for y in range (0, yLimit):
            for z in range (0, zLimit):
                bin = Histogram.GetBin (x, y, z)
                content = Histogram.GetBinContent (bin)
                error = Histogram.GetBinError (bin)
                newContent = content * sf
                newError = sqrt (content * content * sfError * sfError + error * error * sf * sf)
                Histogram.SetBinContent (bin, newContent)
                Histogram.SetBinError (bin, newError)

# Code for impurities is not yet implemented
def subtractImpurities (Histogram,channel=""):
    for sample in impurities:
        dataset_file = "%s/%s.root" % (bkgdSrc_dir,sample)
        inputFile = TFile(dataset_file)
        ImpurityHistogram = inputFile.Get(rootDirectory+"/"+channel+"/"+histogramName).Clone()
        ImpurityHistogram.SetDirectory(0)
        inputFile.Close()
        Histogram.Add(ImpurityHistogram,-1)
    
########################################################
########################################################





#### Loop over each background input source 
for bkgd in bkgd_sources:  

    outputFileName = bkgd + ".root"
    outputFile = TFile(condor_dir + "/" + outputFileName, "RECREATE")
    print "Creating file: " + outputFile.GetName()

    channels = []
    processed_datasets = []
    bkgdSrc_dir = re.sub (r"([^/]*)/[^/]*", r"\1/" + bkgd_sources[bkgd]['inputDir'], condor_dir)
#    print "Debug:  bkgdSrc_dir = " + bkgdSrc_dir  

#### check which input datasets have valid output files
    for sample in bkgd_sources[bkgd]['datasetsIn']:
        fileName = bkgdSrc_dir + "/" + sample + ".root"
        if not os.path.exists(fileName):
            print fileName, "does not exist"
            continue
        testFile = TFile(fileName)
        if testFile.IsZombie() or not testFile.GetNkeys():
            continue
        processed_datasets.append(sample)
        

    if len(processed_datasets) is 0:
        sys.exit("No datasets have been processed")

    #### open first input file and re-make its directory structure in the output file
    testFile = TFile(bkgdSrc_dir + "/" + processed_datasets[0] + ".root")
    testFile.cd()
    for key in testFile.GetListOfKeys():
        if (key.GetClassName() != "TDirectoryFile"):
            continue
        outputFile.cd()
        outputFile.mkdir(key.GetName())
        rootDirectory = key.GetName()

        testFile.cd(key.GetName())
        for key2 in gDirectory.GetListOfKeys():
            if (key2.GetClassName() != "TDirectoryFile"):
                continue
            if key2.GetName () in bkgd_sources[bkgd]['channel_map']:
                channels.append(key2.GetName())
                for targetChannel in bkgd_sources[bkgd]['channel_map'][key2.GetName()]:
                    outputFile.cd(key.GetName())
                    gDirectory.mkdir(targetChannel)

    #do the thing for cutflow histograms
    testFile.cd(rootDirectory)
    for key in gDirectory.GetListOfKeys(): # loop over histograms in the current directory
        if not re.match (r"TH[123]", key.GetClassName()):
            continue
        histogramName = key.GetName()

        for sample in processed_datasets: # loop over different samples as listed in configurationOptions.py
            dataset_file = "%s/%s.root" % (bkgdSrc_dir,sample)
            inputFile = TFile(dataset_file)
            Histogram = inputFile.Get(rootDirectory+"/"+histogramName).Clone()
            Histogram.SetDirectory(0)
            inputFile.Close()

            subtractImpurities (Histogram)
            applySF (Histogram, bkgd_sources[bkgd]['scale_factor'], bkgd_sources[bkgd]['scale_factor_error'])
            outputFile.cd (rootDirectory)
            #change the names of the cutflow histograms, so it will still work with makeYieldsTables.py
            for channel in channels:
                if Histogram.GetName().find(channel) is -1:
                    Histogram.Write()
                else:
                    for targetChannel in bkgd_sources[bkgd]['channel_map'][channel]:
                        Histogram.Write(Histogram.GetName().replace(channel,targetChannel))

    #do the thing for histograms in the channels directories
    for channel in channels: # loop over final states, which each have their own directory

        print "  Processing " + channel + " channel..."

        testFile.cd(rootDirectory+"/"+channel)

        for key in gDirectory.GetListOfKeys(): # loop over histograms in the current directory
            if not re.match (r"TH[123]", key.GetClassName()):
                continue
            histogramName = key.GetName()

            for sample in processed_datasets: # loop over different samples as listed in configurationOptions.py
                dataset_file = "%s/%s.root" % (bkgdSrc_dir,sample)
                inputFile = TFile(dataset_file)
                Histogram = inputFile.Get(rootDirectory+"/"+channel+"/"+histogramName).Clone()
                Histogram.SetDirectory(0)
                inputFile.Close()

                subtractImpurities (Histogram,channel)
                applySF (Histogram, bkgd_sources[bkgd]['scale_factor'], bkgd_sources[bkgd]['scale_factor_error'])
                for targetChannel in bkgd_sources[bkgd]['channel_map'][channel]:
                    outputFile.cd (rootDirectory + "/" + targetChannel)
                    Histogram.Write ()

    outputFile.Close()
