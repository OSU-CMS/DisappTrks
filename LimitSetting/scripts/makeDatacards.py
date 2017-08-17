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
parser.add_option("-g", "--gamma", action="store_true", dest="runGamma", default=False,
                  help="run with gamma function instead of log normal")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")

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
    hist = inputFile.Get(channel+"/"+integrateHistogramName)
    if not hist:
        print "Could not find hist "+channel+"/"+integrateHistogramName + " in " + inputFile.GetName()
    hist.SetDirectory(0)
    inputFile.Close()
    yieldAndErrorList = {}
    nBinsX = hist.GetNbinsX()

    intError = Double (0.0)
    integral = hist.IntegralAndError(0,nBinsX+1,intError)
    fracError = 1.0 + (intError / integral) if integral > 0.0 else 1.0

    raw_integral = hist.GetEntries ()

    yieldAndErrorList['yield'] = integral
    yieldAndErrorList['rawYield'] = raw_integral
    yieldAndErrorList['error'] = fracError
    yieldAndErrorList['absError'] = intError
    yieldAndErrorList['weight'] = integral / raw_integral if raw_integral > 0.0 else 0.0
    return yieldAndErrorList


def ReadYieldAndError(condor_dir, process):
    inputTxtFile = open("condor/"+condor_dir+"/yields.txt", "r")
    if not inputTxtFile:
        print "Could not find yields.txt in condor/"+condor_dir

    yieldAndErrorList = {}
    bkgdError = Double (0.0)
    bkgdYield = Double (0.0)


    for line in inputTxtFile:
        if process + "Bkgd Yield" in line:
            bkgdYield =  line.split(" ")[5]
            bkgdError = line.split(" ")[7]
    fracError = 0.0

    if bkgdYield > 0.0:
        fracError = str(1.0 + (Double(bkgdError) / Double(bkgdYield)))
    yieldAndErrorList['yield'] = bkgdYield
    yieldAndErrorList['error'] = fracError
    return yieldAndErrorList



def writeDatacard(mass,lifetime,observation):

    lifetime = lifetime.replace(".0", "")
    lifetime = lifetime.replace("0.5", "0p5")
    if samplesByGravitinoMass:
        signal_dataset = "AMSB_mGrav" + mass + "K_" + lifetime + "ns_" + signal_suffix
	shorter_signal_dataset = "AMSB_mGrav" + mass + "K_" + lifetime + "ns"
    else:
        signal_dataset = "AMSB_chargino_" + mass + "GeV_" + lifetime + "cm_" + signal_suffix
	shorter_signal_dataset = "AMSB_chargino_" + mass + "GeV_" + lifetime + "cm"
    signalYieldAndError = GetYieldAndError(signal_condor_dir, signal_dataset, signal_channel)
    signal_yield = signalYieldAndError['yield']
    signal_yield_raw = signalYieldAndError['rawYield']
    signal_yield_weight = signalYieldAndError['weight']

    signal_yield *= signalScaleFactor
    signal_yield_weight *= signalScaleFactor

    background_yields = { }
    background_errors = { }
    totalBkgd = 0
    for background in backgrounds :
        yieldAndError = {}
        if not arguments.runGamma:
            yieldAndError = ReadYieldAndError(background_sources[background]['condor_dir'], background)
            background_yields[background] = yieldAndError['yield']
            background_errors[background] = yieldAndError['error']
        else:
            yieldAndError['yield'] = str(float(backgrounds[str(background)]['alpha']) * float(backgrounds[str(background)]['N']))
            yieldAndError['error'] = str(backgrounds[str(background)]['alpha'])
            background_yields[background] = yieldAndError['yield']
            if arguments.verbose:
                print "Debug:  for bkgd: " + str(background) + ", yield = " + str(yieldAndError['yield']) + ", error = " + str(yieldAndError['error'])
            background_errors[background] = backgrounds[str(background)]['alpha']
        totalBkgd += float(background_yields[background])

    if run_blind_limits:
        observation = totalBkgd

    default_channel_name = "MyChan"
    if samplesByGravitinoMass:
        os.system("rm -f limits/"+arguments.outputDir+"/datacard_AMSB_mChi"+chiMasses[mass]['value']+"_"+lifetime+"ns.txt")
        datacard = open("limits/"+arguments.outputDir+"/datacard_AMSB_mChi"+chiMasses[mass]['value']+"_"+lifetime+"ns.txt","w")
    else:
        os.system("rm -f limits/"+arguments.outputDir+"/datacard_AMSB_mChi"+mass+"_"+lifetime+"cm.txt")
        datacard = open("limits/"+arguments.outputDir+"/datacard_AMSB_mChi"+mass+"_"+lifetime+"cm.txt","w")

    datacard.write('imax 1 number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds)) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    #################
    bin_row = [ 'bin', ' ', ' ',actual_bin_name]
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
    bin_row_2.append(actual_bin_name)
    process_name_row.append(shorter_signal_dataset)
    process_index_row.append(str(process_index))
    process_index = process_index + 1
    rate_row.append(str(round(signal_yield,12)))
    empty_row.append('')

    #add background yields
    for background in backgrounds:
        bin_row_2.append(actual_bin_name)
        process_name_row.append(background)
        process_index_row.append(str(process_index))
        process_index = process_index + 1
        if not arguments.runGamma:
            rate_row.append(background_yields[background])
        if arguments.runGamma:
            rate_row.append(str(background_yields[background]))
            if arguments.verbose:
                print "Debug: for background " + str(background)
                print "Debug: for background " + str(background) + ": " + str(background_yields[background])
                print "Debug: for background " + str(background) + ": " + str(background_yields[background])
        empty_row.append('')

    datacard_data.append(empty_row)
    comment_row = empty_row
    comment_row[0] = "# STATISTICAL UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)

    #add a row for the statistical error of the signal
    if arguments.runGamma:
        signal_error_string = str(round(signal_yield_weight,12))
    else:
        signal_error = signalYieldAndError['error']
        signal_error_string = str(round(signal_error,12))
    if arguments.runGamma:
        row = ['signal_stat_'+actual_bin_name,'gmN ' + str(int(round(signal_yield_raw,0))),' ',signal_error_string]
    else:
        row = ['signal_stat','lnN','',signal_error_string]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

     #add a row for the statistical error of each background
    for background in backgrounds:
        row = [background+"_stat",'lnN','','-']
        if arguments.runGamma:
            row = [background+"_"+actual_bin_name+"_stat",'gmN ' + backgrounds[str(background)]['N'],' ', '-']
        for process_name in backgrounds:
            if background is process_name:

                if arguments.runGamma:
                    row.append(background_errors[process_name])
                else:
                    row.append(background_errors[process_name])
                    #row.append(str(round(background_errors[process_name],2)))
            else:
                row.append('-')
        datacard_data.append(row)




    datacard_data.append(empty_row)
    comment_row = empty_row
    comment_row[0] = "# NORMALIZATION UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    datacard_data.append(empty_row)
    comment_row = empty_row
    comment_row[0] = "# SYSTEMATIC UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)

    #add a row for the systematic error of each background
    for background in background_systematics:
        row = [background,'lnN','','-']
        for process_name in backgrounds:
            if background_systematics[background]['background'] is process_name:
                row.append(background_systematics[background]['value'])
            else:
                row.append('-')
        datacard_data.append(row)


    #add a row for the cross-section error for the signal
    row = ['signal_cross_sec','lnN','',str(round(float(signal_cross_sections[mass]['error']),6))]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

 #add a new row for each uncertainty specified in configuration file
    for uncertainty in signal_systematic_uncertainties:
        row = [uncertainty,'lnN','']
##          if 'signal' in global_systematic_uncertainties[uncertainty]['applyList']:
        row.append(signal_systematic_uncertainties[uncertainty]['value'])
##          else:
##              row.append('-')
        for background in backgrounds:
##              if background in global_systematic_uncertainties[uncertainty]['applyList']:
##                  row.append(global_systematic_uncertainties[uncertainty]['value'])
##              else:
            row.append('-')
        datacard_data.append(row)

# add a new row for each uncertainty defined in external text files
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

######
#####


    signalOrigYield = lumi * float(signal_cross_sections[mass]['value'])
    signalEff = signal_yield / signalOrigYield
    signalEffErr = signalEff * (float(signal_cross_sections[mass]['error']) - 1.0)

    datacard.write('# lumi = ' + str(lumi) + '\n')
    datacard.write('# sig cross sec = ' + signal_cross_sections[mass]['value'] + '\n')
    datacard.write('# signalOrigYield = ' + str(signalOrigYield) + '\n')
    datacard.write('# signalYield = '     + str(signal_yield) + '\n')
    datacard.write('# signalEff = ' + str(signalEff) + '\n')
    datacard.write('# signalEffErr = ' + str(signalEffErr) + '\n')

    useBatch = True

    if arguments.runRooStatsCl95:
        os.system("rm -f limits/"+arguments.outputDir+"/runRooStats_"+signal_dataset+".src")
        datacard95 = open("limits/"+arguments.outputDir+"/runRooStats_"+signal_dataset+".src", 'w')
        logfile = 'limitResults/tau' + lifetime + '/mGrav' + mass + 'K/limitExpDisTrk.log'
        if useBatch:
            command = 'bsub -q 8nm -oo '
#            command += '%50s ' % logfile
            command += '{0: <50}'.format(logfile)
        else:
            command = ''
        command += 'limitScanDisTrk.sh '
##         command += '%18s ' % str(signalEff)
##         command += '%18s ' % str(signalEffErr)
        command += '{0: <18}'.format(str(signalEff))
        command += '{0: <18}'.format(str(signalEffErr))
        command += '{0: <18}'.format(str(backgroundEst))
        command += '{0: <18}'.format(str(backgroundEstErr))
##         command = command + 'root -l -b -q \'limitScanDisTrk.C+(\"limitResults/tau' + lifetime + '/mGrav' + mass + 'K/\",'
##         command = command + str(signalEff) + ',' + str(signalEffErr) + ',' + str(backgroundEst) + ',' + str(backgroundEstErr) + ')\''
        if not useBatch:
            command = command + ' | tee ' + logfile
        print command
        datacard95.write(command)

    return totalBkgd


########################################################################################
########################################################################################
###getting all the systematic errors and putting them in a dictionary
systematics_dictionary = {}
for systematic in external_systematic_uncertainties:
    input_file = open(os.environ['CMSSW_BASE']+"/src/DisappTrks/SignalSystematics/data/systematic_values__" + systematic + ".txt")
    systematics_dictionary[systematic] = {}
    for line in input_file:
        intermediateLine = '~'.join(line.rstrip("\n").split())
        newLine = intermediateLine.rstrip("\n").split("~")

        dataset = newLine[0]
        if len(newLine) is 2:
            systematics_dictionary[systematic][dataset] = newLine[1]
        elif len(newLine) is 3:
            systematics_dictionary[systematic][dataset]= newLine[1]+"/"+newLine[2]

            # turn off systematic when the central yield is zero
            if systematics_dictionary[systematic][dataset] == '0' or systematics_dictionary[systematic][dataset] == '0/0' \
            or systematics_dictionary[systematic][dataset] == '0.0' or systematics_dictionary[systematic][dataset] == '0.0/0.0':
                systematics_dictionary[systematic][dataset] = '-'



###setting up observed number of events
observation = 0
if not run_blind_limits:
    observation = GetYieldAndError(data_condor_dir, data_dataset, data_channel)['yield']




###looping over signal models and writing a datacard for each
for mass in masses:
    for lifetime in lifetimes:
        writeDatacard(mass,lifetime,observation)
