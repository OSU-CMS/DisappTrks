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


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-R", "--runRooStatsCl95", action="store_true", dest="runRooStatsCl95", default=False,
                  help="create scripts to run RooStatsCl95")

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
    hist = inputFile.Get("OSUAnalysis/"+channel+"/"+integrateHistogramName).Clone()
    if not hist:
        print "Could not find hist OSUAnalysis/"+channel+"/"+integrateHistogramName + " in " + inputFile.GetName() 
    hist.SetDirectory(0)
    inputFile.Close()
    yieldAndErrorList = {}
    nBinsX = hist.GetNbinsX()

    intError = Double (0.0)
    integral = hist.IntegralAndError(1,nBinsX,intError)
    fracError = 0.0
    if integral > 0.0:
        fracError = 1.0 + (intError / integral)

    #print channel + ", " + integrateHistogramName + ", " + process + ": " + str (integral) + " +- " + str (intError) + " (" + str (fracError) + ")"

    yieldAndErrorList['yield'] = integral
    yieldAndErrorList['error'] = fracError
    return yieldAndErrorList




def writeDatacard(mass,lifetime):

    lifetime = lifetime.replace(".0", "")  
    lifetime = lifetime.replace(".", "p")  
    signal_dataset = "AMSB_mGrav" + mass + "K_" + lifetime + "ns" 
    signalYieldAndError = GetYieldAndError(signal_condor_dir, signal_dataset, signal_channel)
    signal_yield = signalYieldAndError['yield']
    
    default_channel_name = "MyChan"

    if not arguments.runRooStatsCl95:
        print "making limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt" 
    os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt")
    datacard = open("limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt", 'w')
    datacard.write('imax 1 number of channels\n')
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
        
    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# STATISTICAL UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)
    
    #add a row for the statistical error of the signal
    signal_error = signalYieldAndError['error']
    signal_error_string = str(round(signal_error,3))
    row = ['signal_stat','lnN','',signal_error_string]

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# NORMALIZATION UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    #add a row for the cross-section error for the signal
    row = ['signal_cross_sec','lnN','',str(round(float(signal_cross_sections[mass]['error']),3))]
    datacard_data.append(row)

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# SYSTEMATIC UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    #write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')

    signalOrigYield = lumi * float(signal_cross_sections[mass]['value'])  
    signalEff = signal_yield / signalOrigYield
    signalEffErr = signalEff * signalErrFrac

    datacard.write('# lumi = ' + str(lumi) + '\n')
    datacard.write('# sig cross sec = ' + signal_cross_sections[mass]['value'] + '\n')
    datacard.write('# signalOrigYield = ' + str(signalOrigYield) + '\n')
    datacard.write('# signalEff = ' + str(signalEff) + '\n')
    datacard.write('# signalEffErr = ' + str(signalEffErr) + '\n')

    useBatch = False 

    if arguments.runRooStatsCl95:
        os.system("rm -f limits/"+arguments.outputDir+"/runRooStats_"+signal_dataset+".src")
        datacard95 = open("limits/"+arguments.outputDir+"/runRooStats_"+signal_dataset+".src", 'w')
        logfile = 'limitResults/tau' + lifetime + '/mGrav' + mass + 'K/limitExpDisTrk.log'
        if useBatch: 
            command = 'bsub -q 8nm -oo ' + logfile
        else:
            command = '' 
        command = command + 'root -l -b -q \'limitScanDisTrk.C+(\"limitResults/tau' + lifetime + '/mGrav' + mass + 'K/\",'
        command = command + str(signalEff) + ',' + str(signalEffErr) + ',' + str(backgroundEst) + ',' + str(backgroundEstErr) + ')\''
        if not useBatch: 
            command = command + ' | tee ' + logfile
        print command 
        datacard95.write(command)
        

########################################################################################
########################################################################################

            
            
###setting up observed number of events
if run_blind_limits:
    observation = backgroundEst
else:
    observation = GetYieldAndError(data_condor_dir, data_dataset, data_channel)['yield']




###looping over signal models and writing a datacard for each
for mass in masses:
    for lifetime in lifetimes:
        writeDatacard(mass,lifetime)



