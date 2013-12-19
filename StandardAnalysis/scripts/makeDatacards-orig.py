#!/usr/bin/env python

# Script to extract signal efficiencies and set up the necessary cards for running limits.
#
# Copied from https://github.com/DisplacedSUSY/DisplacedSUSY/blob/master/Configuration/scripts/makeDatacards.py

import time
import os
import sys
import math
import copy
import re
from array import *
from optparse import OptionParser
from DisplacedSUSY.Configuration.systematicsDefinitions import *




parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-d", "--d0Cut", dest="d0Cut",
                  help="lepton impact parameter requirement in cm")
parser.add_option("-m", "--maxD0", action="store_true", dest="maxD0", default=False,
                  help="uses d0 cut as a maximum instead of a minimum")
parser.add_option("-s", "--systematicsChannel", dest="systematicsChannel",
                  help="channel name used in getting systematics values from text files")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.outputDir:
    if not os.path.exists("limits/"+arguments.outputDir):
        os.system("mkdir limits/"+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

if not arguments.d0Cut:
    print "No d0 cut specified, how could you?"
    sys.exit(0)

if not arguments.systematicsChannel:
    print "Please specify channel for systematic uncertainties"
    sys.exit(0)


if arguments.maxD0:
    integrateOutwardX = False
    integrateOutwardY = False
else:
    integrateOutwardX = True
    integrateOutwardY = True


from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double


def fancyTable(arrays):

    def areAllEqual(lst):
        return not lst or [lst[0]] * len(lst) == lst

    if not areAllEqual(map(len, arrays)):
        exit('Cannot print a table with unequal array lengths.')

    verticalMaxLengths = [max(value) for value in map(lambda * x:x, *[map(len, a) for a in arrays])]

    spacedLines = []

    for array in arrays:
        spacedLine = ''
        for i, field in enumerate(array):
            diff = verticalMaxLengths[i] - len(field)
            spacedLine += field + ' ' * diff + '\t'
        spacedLines.append(spacedLine)

    return '\n'.join(spacedLines)



def GetYieldAndError(condor_dir, process, channel):
    inputFile = TFile("condor/"+condor_dir+"/"+process+".root")
    d0Histogram = inputFile.Get("OSUAnalysis/"+channel+"/"+d0histogramName).Clone()
    d0Histogram.SetDirectory(0)
    inputFile.Close()
    yieldAndErrorList = {}
    nBinsX = d0Histogram.GetNbinsX()
    nBinsY = d0Histogram.GetNbinsY()
    x0 = x1 = y0 = y1 = 0

    d0CutBinX = d0Histogram.GetXaxis ().FindBin (float(arguments.d0Cut))
    d0CutBinY = d0Histogram.GetYaxis ().FindBin (float(arguments.d0Cut))
    xValue = d0Histogram.GetXaxis().GetBinCenter(d0CutBinX)
    yValue = d0Histogram.GetYaxis().GetBinCenter(d0CutBinY)

    if ((xValue >= 0) == integrateOutwardX):
        x0 = d0CutBinX
        x1 = nBinsX + 1
    else:
        x0 = 0
        x1 = d0CutBinX
    if ((yValue >= 0) == integrateOutwardY):
        y0 = d0CutBinY
        y1 = nBinsY + 1
    else:
        y0 = 0
        y1 = d0CutBinY
    intError = Double (0.0)
    integral = d0Histogram.IntegralAndError(x0,x1,y0,y1,intError)
    fracError = 0.0
    if integral > 0.0:
        fracError = 1.0 + (intError / integral)

    #print channel + ", " + d0histogramName + ", " + process + ": " + str (integral) + " +- " + str (intError) + " (" + str (fracError) + ")"

    yieldAndErrorList['yield'] = integral
    yieldAndErrorList['error'] = fracError
    return yieldAndErrorList


def writeDatacard(mass,lifetime,branching_ratio):


    signal_dataset = "stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio
    signalYieldAndError = GetYieldAndError(signal_condor_dir, signal_dataset, signal_channel)
    signal_yield = signalYieldAndError['yield']
    
    default_channel_name = "EMu"

    os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt")
    datacard = open("limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt", 'w')
    datacard.write('imax 1 number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds)) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    #################
    bin_row = [ 'bin', ' ', ' ',default_channel_name]
    observation_row = [ 'observation', ' ', ' ', str(round(observation,0)) ]
    #################
    datacard.write('\n----------------------------------------\n')
    datacard.write(fancyTable([ bin_row, observation_row ]))
    datacard.write('\n----------------------------------------\n')

    bin_row_2 = [ 'bin', ' ', ' ' ]
    process_name_row  = [ 'process', ' ', ' ' ]
    process_index_row = [ 'process', ' ', ' ' ]
    rate_row = [ 'rate', ' ', ' ' ]
    datacard_data = [ bin_row_2, process_name_row, process_index_row, rate_row ]

    empty_row = ['','','']

    process_index = 0

    #add signal yield
    bin_row_2.append(default_channel_name)
    process_name_row.append(signal_dataset)
    process_index_row.append(str(process_index))
    process_index = process_index + 1
    rate_row.append(str(round(signal_yield,4)))
    empty_row.append('')

    #add background yields
    for background in backgrounds:
        #print background
        bin_row_2.append(default_channel_name)
        process_name_row.append(background)
        process_index_row.append(str(process_index))
        process_index = process_index + 1
        rate_row.append(str(round(background_yields[background],4)))
        empty_row.append('')
        
    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# STATISTICAL UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)
    
    #add a row for the statistical error of the signal
    signal_error = signalYieldAndError['error']
    signal_error_string = str(round(signal_error,3))
    row = ['signal_stat','lnN','',signal_error_string]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

    #add a row for the statistical error of each background
    for background in backgrounds:
        row = [background+"_stat",'lnN','','-']
        for process_name in backgrounds:
            if background is process_name:
                row.append(str(round(background_errors[process_name],3)))
            else:
                row.append('-')
        datacard_data.append(row)

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# NORMALIZATION UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    #add a row for the cross-section error for the signal
    row = ['signal_cross_sec','lnN','',str(round(float(signal_cross_sections[mass]['error']),3))]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

    #add a row for the normalization error for each background
    for process_name in sorted(background_normalization_uncertainties):
        row = [process_name+"_norm",background_normalization_uncertainties[process_name]['type'],'','-']
        for background in backgrounds:
            if process_name is background:
                row.append(background_normalization_uncertainties[process_name]['value'])
            else:
                row.append('-')
        datacard_data.append(row)

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# SYSTEMATIC UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    
    #add a new row for each uncertainty specified in configuration file
    for uncertainty in global_systematic_uncertainties:
        row = [uncertainty,'lnN','']
        if 'signal' in global_systematic_uncertainties[uncertainty]['applyList']:
            row.append(global_systematic_uncertainties[uncertainty]['value'])
        else:
            row.append('-')
        for background in backgrounds:
            if background in global_systematic_uncertainties[uncertainty]['applyList']:
                row.append(global_systematic_uncertainties[uncertainty]['value'])
            else:
                row.append('-')
        datacard_data.append(row)

    #add a new row for each uncertainty defined in external text files
    for uncertainty in systematics_dictionary:
        row = [uncertainty,'lnN','']
        if signal_dataset in systematics_dictionary[uncertainty]:
            row.append(systematics_dictionary[uncertainty][signal_dataset])
        else:
            row.append('-')
        for background in backgrounds:
            if background in systematics_dictionary[uncertainty]:
                row.append(systematics_dictionary[uncertainty][background])
            else:
                row.append('-')
        datacard_data.append(row)



    #write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')





########################################################################################
########################################################################################



###setting up background yields and statistical errors
background_yields = {}
background_errors = {}

backgrounds.sort()

for background in backgrounds:

    yieldAndError = {}
    yieldAndError = GetYieldAndError(background_sources[background]['condor_dir'], background, background_sources[background]['channel'])
    #print yieldAndError
        
    background_yields[background] = yieldAndError['yield']
    background_errors[background] = yieldAndError['error']

    #print background+" yield = "+str(background_yields[background])+" +- "+str(background_errors[background])+"%"


###getting all the systematic errors and putting them in a dictionary
systematics_dictionary = {}
for systematic in external_systematic_uncertainties:
    input_file = open(os.environ['CMSSW_BASE']+"/src/DisplacedSUSY/Configuration/data/systematic_values__" + systematic + "__" + arguments.systematicsChannel + ".txt")
    systematics_dictionary[systematic] = {}
    for line in input_file:
        line = line.rstrip("\n").split(" ")
        dataset = line[0]
        if len(line) is 2:
            systematics_dictionary[systematic][dataset] = line[1]
        elif len(line) is 3:
            systematics_dictionary[systematic][dataset]= line[1]+"/"+line[2]

        # turn off systematic when the central yield is zero
        if systematics_dictionary[systematic][dataset] == '0' or systematics_dictionary[systematic][dataset] == '0/0':
            systematics_dictionary[systematic][dataset] = '-'
            
            
#print systematics_dictionary


###setting up observed number of events
if run_blind_limits:
    background_sum = 0
    for background in backgrounds:
        background_sum = background_sum + round(float(background_yields[background]),1)
    observation = background_sum
else:
    #print GetYieldAndError(data_condor_dir, data_dataset, data_channel)
    observation = GetYieldAndError(data_condor_dir, data_dataset, data_channel)['yield']




###looping over signal models and writing a datacard for each
for mass in masses:
  for lifetime in lifetimes:
    for branching_ratio in branching_ratios:
        print "making datacard_stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio+".txt"
        writeDatacard(mass,lifetime,branching_ratio)
