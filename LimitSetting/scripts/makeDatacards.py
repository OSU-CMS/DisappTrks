#!/usr/bin/env python3

# Script to extract signal efficiencies and set up the necessary cards for running limits.

import time
import os
import sys
import math
import copy
import re
from array import *
from threading import Thread, Lock, Semaphore
from multiprocessing import cpu_count
import ctypes

from DisappTrks.LimitSetting.limitOptions import *

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, TChain, TH2D

if not arguments.era in validEras:
  print( "\nInvalid or empty data-taking era specific (-e). Allowed eras:\n")
  print( str(validEras))
  sys.exit(0)

if arguments.limitType not in validLimitTypes:
    print( "\nInvalid or empty limit type to plot (-l). Allowed types:\n")
    print( str(validLimitTypes))
    sys.exit(0)

if arguments.limitType == "wino":
    from DisappTrks.LimitSetting.winoElectroweakLimits import *
elif arguments.limitType == "higgsino":
    from DisappTrks.LimitSetting.higgsinoElectroweakLimits import *

if arguments.outputDir:
    if not os.path.exists("limits/" + arguments.outputDir):
        os.system("mkdir limits/" + arguments.outputDir)
else:
    print( "No output directory specified, shame on you")
    sys.exit(0)

def fancyTable(arrays):

    def areAllEqual(lst):
        return not lst or [lst[0]] * len(lst) == lst

    if not areAllEqual(list(map(len, arrays))):
        exit('Cannot print a table with unequal array lengths.')

    verticalMaxLengths = [max(value) for value in map(lambda * x:x, *[map(len, a) for a in arrays])]

    spacedLines = []

    for a in arrays:
        spacedLine = ''
        for i, field in enumerate(a):
            diff = verticalMaxLengths[i] - len(field)
            spacedLine += field + ' ' * diff + '\t'
        spacedLines.append(spacedLine)

    return '\n'.join(spacedLines)

# 10cmTo1cm not available...
def GetMissingLifetimeWeight(chain):
        w = 0
        # how is this possible otherwise? one event in /data/users/kwei/2017/signalAcceptance_full_v2/AMSB_chargino_100GeV_10cm_94X/
        if chain.eventvariable_cTau_1000024_0 > 0:
            srcPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_0 / 10.0) / 10.0
            dstPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_0 / 1.0) / 1.0
            w = dstPDF / srcPDF
        if chain.eventvariable_cTau_1000024_1 > 0:
            srcPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_1 / 10.0) / 10.0
            dstPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_1 / 1.0) / 1.0
            w *= dstPDF / srcPDF
        return w

def GetReweightedYieldAndError(condor_dir, process, channel, srcCTau, dstCTau, limitType):
    global printLock

    if os.path.isfile('condor/' + condor_dir + '/' + process + '.root') and not '_1cm_' in process:
        return GetYieldAndError(condor_dir, process, channel)

    realProcessName = process.replace(dstCTau, srcCTau)

    if arguments.verbose:
        printLock.acquire ()
        print( 'Reweighting yield from ' + realProcessName + ' to ' + process + ' ...')
        printLock.release ()

    chain = TChain(signal_channel_tree)
    chain.Add('condor/' + condor_dir + '/' + realProcessName + '/hist_*.root')

    lifetimeWeightName = 'eventvariable_lifetimeWeight_1000024_' + srcCTau + 'To' + dstCTau

    realInputFile = TFile('condor/' + condor_dir + '/' + realProcessName + '.root')
    nGenerated = realInputFile.Get(channel.replace('Plotter/Met Plots', 'CutFlowPlotter/eventCounter')).GetEntries()
    crossSectionWeight = 1.0 
    if process != data_dataset:
        crossSectionWeight *= lumi / nGenerated
        if arguments.limitType == "higgsino":
            crossSectionWeight *= float(signal_cross_sections_higgsino[process.split('_')[1][:-3]]['value'])
        elif arguments.limitType == "wino":
            crossSectionWeight *= float(signal_cross_sections[process.split('_')[2][:-3]]['value'])

    totalWeight = 0.0
    totalWeight2 = 0.0

    for iEvent in range(chain.GetEntries()):
        chain.GetEntry(iEvent)
        if lifetimeWeightName == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
            lifetimeWeight = GetMissingLifetimeWeight(chain)
        else:
            lifetimeWeight = getattr(chain, lifetimeWeightName)
        if chain.eventvariable_cTau_1000024_0 < 0:
            printLock.acquire()
            print( 'WARNING: somehow event number ' + str(iEvent) + ' in sample ' + process + ' has no charginos at all! Ignoring this event...')
            printLock.release()
            continue # or lifetimeWeight = 0 really
        thisWeight = crossSectionWeight * lifetimeWeight * chain.eventvariable_isrWeight * chain.eventvariable_grandOrWeight * chain.eventvariable_puScalingFactor
        if arguments.era.startswith('2017_'):
            thisWeight *= chain.eventvariable_L1ECALPrefiringWeight
        totalWeight += thisWeight
        totalWeight2 += thisWeight * thisWeight

    yieldAndError = {
        'yield'      : totalWeight,
        'rawYield'   : chain.GetEntries(),
        'error'      : 1.0 + (math.sqrt(totalWeight2) / totalWeight) if totalWeight > 0.0 else 1.0,
        'absError'   : math.sqrt(totalWeight2) if totalWeight2 > 0.0 else 1.1,
        'weight'     : totalWeight / chain.GetEntries() if chain.GetEntries() > 0.0 else 0.0,
        'acceptance' : totalWeight / nGenerated / crossSectionWeight,
        'acceptanceError' : (math.sqrt(totalWeight2) if totalWeight2 > 0.0 else 1.1) / nGenerated / crossSectionWeight,
    }

    return yieldAndError

def GetYieldAndError(condor_dir, process, channel):
    inputFile = TFile("condor/" + condor_dir + "/" + process + ".root")
    hist = inputFile.Get(channel + "/" + integrateHistogramName)
    if not hist:
        print( "Could not find hist " + channel + "/" + integrateHistogramName + " in " + inputFile.GetName())
    hist.SetDirectory(0)
    nGenerated = inputFile.Get(channel.replace('Plotter/Met Plots', 'CutFlowPlotter/eventCounter')).GetEntries()
    inputFile.Close()

    intError = 0.0
    integral = hist.IntegralAndError(0, hist.GetNbinsX() + 1, ctypes.c_double(intError))
    fracError = float(1.0 + (intError / integral)) if integral > 0.0 else 1.0

    raw_integral = hist.GetEntries ()

    # don't need cross section uncertainties, since that is its own nuisance parameter
    crossSectionWeight = 1.0 
    if process != data_dataset:
        crossSectionWeight *= lumi / nGenerated
        if arguments.limitType == "higgsino":
            crossSectionWeight *= float(signal_cross_sections_higgsino[process.split('_')[1][:-3]]['value'])
        elif arguments.limitType == "wino":
            crossSectionWeight *= float(signal_cross_sections[process.split('_')[2][:-3]]['value'])


    if process != data_dataset:
        datasetInfo = open("condor/" + condor_dir + "/" + process + "/datasetInfo_" + process + "_cfg.py")
        xsec = [x for x in list(datasetInfo) if x.startswith('crossSection = ')]
        datasetInfo.close()
        if len(xsec) > 0:
            xsec = float(xsec[-1].split('=')[-1])
        if xsec < 0:
            integral *= crossSectionWeight
            intError *= crossSectionWeight

    acceptance = integral / nGenerated / crossSectionWeight

    yieldAndError = {
        'yield'      : integral,
        'rawYield'   : raw_integral,
        'error'      : fracError,
        'absError'   : intError,
        'weight'     : integral / raw_integral if raw_integral > 0.0 else 0.0,
        'acceptance' : integral / nGenerated / crossSectionWeight,
        'acceptanceError' : (integral if integral > 0.0 else 1.1) / nGenerated / crossSectionWeight,
    }

    return yieldAndError

def writeDatacard(mass, lifetime, observation, dictionary, ignoreSignalScaleFactor):
    global semaphore
    global printLock

    semaphore.acquire ()

    lifetimeFloat = float(lifetime)

    lifetime = lifetime.replace(".0", "")
    lifetime = lifetime.replace("0.", "0p")
    if arguments.limitType == "wino":
        if samplesByGravitinoMass:
            signal_dataset = "AMSB_mGrav" + mass + "K_" + lifetime + "ns_" + signal_suffix
            shorter_signal_dataset = "AMSB_mGrav" + mass + "K_" + lifetime + "ns"
        else:
            signal_dataset = "AMSB_chargino_" + mass + "GeV_" + lifetime + "cm_" + signal_suffix
            shorter_signal_dataset = "AMSB_chargino_" + mass + "GeV_" + lifetime + "cm"
    elif arguments.limitType == "higgsino":
        signal_dataset = "Higgsino_" + mass + "GeV_" + lifetime + "cm_" + signal_suffix
        shorter_signal_dataset = "Higgsino_" + mass + "GeV_" + lifetime + "cm"

    srcCTau = int(math.pow(10 , math.ceil((math.log10( lifetimeFloat )))))
    # acceptance is too low for 1cm, so here just reweight from 10cm...
    if lifetime.startswith('0p') or lifetime == '1':
        srcCTau = 10
    signalYieldAndError = GetReweightedYieldAndError(signal_condor_dir, 
                                                     signal_dataset, 
                                                     signal_channel, 
                                                     str(srcCTau) + 'cm', 
                                                     lifetime + 'cm',
                                                     arguments.limitType)

    signal_yield = signalYieldAndError['yield']
    signal_yield_raw = signalYieldAndError['rawYield']
    signal_yield_weight = signalYieldAndError['weight']

    target_signal_yield = 10.0
    if ignoreSignalScaleFactor:
        signal_yield_sf = 1.0
    else:
        signal_yield_sf = target_signal_yield / signal_yield if signal_yield > 0.0 else 1.0

    try:
        if adhocSignalScaling[signal_dataset] > 0:
            signal_yield_sf /= adhocSignalScaling[signal_dataset]
    except:
        pass

    signal_yield_without_sf = signal_yield
    signal_yield *= signal_yield_sf
    signal_yield_weight *= signal_yield_sf

    background_yields = { }
    background_errors = { }
    totalBkgd = 0
    for background in backgrounds :
        if 'alpha' in backgrounds[background]:
            background_yields[background] = str(float(backgrounds[background]['alpha']) * float(backgrounds[background]['N']) * (backgrounds[background]['adhocScaling'] if 'adhocScaling' in backgrounds[background] else 1.0))
            background_errors[background] = str(float(backgrounds[background]['alpha']) * (backgrounds[background]['adhocScaling'] if 'adhocScaling' in backgrounds[background] else 1.0))
        else:
            background_yields[background] = str(float(backgrounds[background]['yield']) * (backgrounds[background]['adhocScaling'] if 'adhocScaling' in backgrounds[background] else 1.0))
            background_errors[background] = str(backgrounds[background]['error'])

        if arguments.verbose:
            printLock.acquire ()
            print("Debug:  for bkgd: " + str(background) + ", yield = " + str(background_yields[background]) + ", error = " + str(background_errors[background]))
            printLock.release ()

        totalBkgd += float(background_yields[background])

    if run_blind_limits:
        observation = totalBkgd

    default_channel_name = "MyChan"
    if arguments.limitType == "wino":
        if samplesByGravitinoMass:
            fSuffix = "AMSB_mChi" + chiMasses[mass]['value'] + "_" + lifetime + "ns.txt"
        else:
            fSuffix = "AMSB_mChi" + mass + "_" + lifetime + "cm.txt"
    elif arguments.limitType == "higgsino":
        fSuffix = "Higgsino_mChi" + mass + "_" + lifetime + "cm.txt"
    os.system("rm -f limits/" + arguments.outputDir + "/datacard_" + fSuffix)
    datacard = open("limits/" + arguments.outputDir + "/datacard_" + fSuffix, "w")
    os.system("rm -f limits/" + arguments.outputDir + "/signalSF_" + fSuffix)
    signalSF = open("limits/" + arguments.outputDir + "/signalSF_" + fSuffix, "w")

    datacard.write('imax 1 number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds)) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    signalSF.write (str (signal_yield_sf) + "\n")
    signalSF.close ()

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
        if 'alpha' in backgrounds[str(background)]:
            rate_row.append(str(background_yields[background]))
            if arguments.verbose:
                print( "Debug: for background " + str(background))
                print( "Debug: for background " + str(background) + ": " + str(background_yields[background]))
                print( "Debug: for background " + str(background) + ": " + str(background_yields[background]))
        else:
            rate_row.append(background_yields[background])
        empty_row.append('')

    datacard_data.append(empty_row)
    comment_row = empty_row
    comment_row[0] = "# STATISTICAL UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)

    #add a row for the statistical error of the signal
    if arguments.runSignalAsGamma:
        signal_error_string = str(round(signal_yield_weight,12))
    else:
        signal_error = signalYieldAndError['error']
        signal_error_string = str(round(signal_error,12))
    if arguments.runSignalAsGamma:
        row = ['signal_stat_'+actual_bin_name,'gmN ' + str(int(round(signal_yield_raw,0))),' ',signal_error_string]
    else:
        row = ['signal_stat','lnN','',signal_error_string]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

     #add a row for the statistical error of each background
    for background in backgrounds:
        row = [background + '_stat', 'lnN', '', '-']
        if 'alpha' in backgrounds[str(background)]:
            row = [background + '_' + actual_bin_name + '_stat', 'gmN ' + backgrounds[str(background)]['N'], '', '-']
        for process_name in backgrounds:
            if background is process_name:
                row.append(background_errors[process_name])
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
    row = ['signal_cross_sec', 'lnN', '', str(round(float(signal_cross_sections[mass]['error'] if arguments.limitType == "wino" else signal_cross_sections_higgsino[mass]['error']), 6))]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

    #add a new row for each uncertainty specified in configuration file
    for uncertainty in signal_systematic_uncertainties:
        row = [uncertainty,'lnN','']
        row.append(signal_systematic_uncertainties[uncertainty]['value'])
        for background in backgrounds:
            row.append('-')
        datacard_data.append(row)

    # add a new row for each uncertainty defined in external text files
    for uncertainty in systematics_dictionary:
        row = [uncertainty, 'lnN', '']
        if signal_dataset in systematics_dictionary[uncertainty]:
            row.append(systematics_dictionary[uncertainty][signal_dataset])
        else:
            row.append('-')
        for background in backgrounds:
            if background in systematics_dictionary[uncertainty]:
                row.append(systematics_dictionary[uncertainty][background])
            else:
                row.append('-')
        # if there are no values for this uncertainty (ie all 0% or the yield is 0%), skip this
        if row.count('-') == len(backgrounds)+1:
            continue
        datacard_data.append(row)

    #write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')

    #################

    signalOrigYield = lumi * float(signal_cross_sections[mass]['value'] if arguments.limitType == "wino" else signal_cross_sections_higgsino[mass]['value'])
    signalEff = signal_yield / signalOrigYield if signalOrigYield > 0.0 else 1.0
    signalEffErr = signalEff * (float(signal_cross_sections[mass]['value'] if arguments.limitType == "wino" else signal_cross_sections_higgsino[mass]['value']) - 1.0)

    datacard.write('# lumi = ' + str(lumi) + '\n')
    datacard.write('# sig cross sec = ' + (signal_cross_sections[mass]['value'] if arguments.limitType == "wino" else signal_cross_sections_higgsino[mass]['value']) + '\n')
    datacard.write('# signalOrigYield = ' + str(signalOrigYield) + '\n')
    datacard.write('# signalYield = '     + str(signal_yield) + '\n')
    datacard.write('# signalEff = ' + str(signalEff) + '\n')
    datacard.write('# signalEffErr = ' + str(signalEffErr) + '\n')
    datacard.write('# signalYieldWithoutSF = ' + str(signal_yield_without_sf) + '\n')

    datacard.close ()

    useBatch = True

    if arguments.runRooStatsCl95:
        os.system("rm -f limits/"+arguments.outputDir+"/runRooStats_"+signal_dataset+".src")
        datacard95 = open("limits/"+arguments.outputDir+"/runRooStats_"+signal_dataset+".src", 'w')
        logfile = 'limitResults/tau' + lifetime + '/mGrav' + mass + 'K/limitExpDisTrk.log'
        if useBatch:
            command = 'bsub -q 8nm -oo '
            #command += '%50s ' % logfile
            command += '{0: <50}'.format(logfile)
        else:
            command = ''
        command += 'limitScanDisTrk.sh '
        #command += '%18s ' % str(signalEff)
        #command += '%18s ' % str(signalEffErr)
        command += '{0: <18}'.format(str(signalEff))
        command += '{0: <18}'.format(str(signalEffErr))
        command += '{0: <18}'.format(str(backgroundEst))
        command += '{0: <18}'.format(str(backgroundEstErr))
        #command = command + 'root -l -b -q \'limitScanDisTrk.C+(\"limitResults/tau' + lifetime + '/mGrav' + mass + 'K/\",'
        #command = command + str(signalEff) + ',' + str(signalEffErr) + ',' + str(backgroundEst) + ',' + str(backgroundEstErr) + ')\''
        if not useBatch:
            command = command + ' | tee ' + logfile
        if arguments.verbose:
            print( command)
        datacard95.write(command)
        datacard95.close(command)

    dictionary[(float(mass), float(lifetime.replace('0p', '0.')))] = signalYieldAndError

    semaphore.release ()


########################################################################################
########################################################################################
### getting all the systematic errors and putting them in a dictionary
systematics_dictionary = {}
for systematic in external_systematic_uncertainties:
    input_file = open(os.environ['CMSSW_BASE']+"/src/DisappTrks/SignalSystematics/data/systematic_values__" + systematic + ".txt")
    systematics_dictionary[systematic] = {}
    for line in input_file:
        intermediateLine = '~'.join(line.rstrip("\n").split())
        newLine = intermediateLine.rstrip("\n").split("~")

        dataset = newLine[0]
        if len(newLine) == 2:
            systematics_dictionary[systematic][dataset] = newLine[1]
        elif len(newLine) == 3:
            systematics_dictionary[systematic][dataset]= newLine[1] + "/" + newLine[2]

            # turn off systematic when the central yield is zero
            if systematics_dictionary[systematic][dataset] == '0' or systematics_dictionary[systematic][dataset] == '0/0' \
            or systematics_dictionary[systematic][dataset] == '0.0' or systematics_dictionary[systematic][dataset] == '0.0/0.0':
                systematics_dictionary[systematic][dataset] = '-'

            # turn off systematic when its fluctuations are exactly zero
            if systematics_dictionary[systematic][dataset] == '1.0' or systematics_dictionary[systematic][dataset] == '1.0/1.0':
                systematics_dictionary[systematic][dataset] = '-'

    input_file.close ()

###setting up observed number of events
observation = 0
if not run_blind_limits:
    if not useHistogramForObservation:
        observation = rawObservation
    else:
        observation = GetYieldAndError(data_condor_dir, data_dataset, data_channel)['yield']

allYieldsAndErrors = {}

###looping over signal models and writing a datacard for each
threads = []
printLock = Lock ()
semaphore = Semaphore (cpu_count () + 1)

print('\nWriting cards for era', arguments.era, '...\n')

for mass in masses:
    for lifetime in lifetimes:
        threads.append (Thread (target = writeDatacard, args = (mass, lifetime, observation, allYieldsAndErrors, arguments.ignoreSignalScaleFactor)))
        threads[-1].start ()
for thread in threads:
    thread.join ()

acceptanceOutput = TFile('limits/' + arguments.outputDir + '/acceptancePlots.root', 'recreate')

xBin = [float(a) for a in masses]
yBin = [float(a) for a in lifetimes]
xBin.sort()
yBin.sort()
xBin.append(xBin[-1] + (xBin[-1] - xBin[-2]))  # Add an additional bin boundary, so that the last bin has equal witdth to the second to last bin
yBin.append(yBin[-1] + (yBin[-1] - yBin[-2]))  # Add an additional bin boundary, so that the last bin has equal witdth to the second to last bin
# Offset the xaxis bins so that mass values are in center of each bin
xBinHalfWidth = (xBin[1] - xBin[0]) / 2
for i in range(0, len(xBin)):
    xBin[i] -= xBinHalfWidth
xBinArray = array('d', xBin)
yBinArray = array('d', yBin)

hYields =      TH2D('yields',      'yields',      len(xBin) - 1, xBinArray, len(yBin) - 1, yBinArray)
hAcceptances = TH2D('acceptances', 'acceptances', len(xBin) - 1, xBinArray, len(yBin) - 1, yBinArray)

for yld in allYieldsAndErrors:
    mass = yld[0]
    lifetime = yld[1]
    ibinX = hYields.GetXaxis().FindBin(mass)
    ibinY = hYields.GetYaxis().FindBin(lifetime)
    hYields.SetBinContent(ibinX, ibinY, allYieldsAndErrors[yld]['yield'])
    if allYieldsAndErrors[yld]['acceptance'] > 0:
        hYields.SetBinError(ibinX, ibinY, allYieldsAndErrors[yld]['yield'] * allYieldsAndErrors[yld]['acceptanceError'] / allYieldsAndErrors[yld]['acceptance'])
    hAcceptances.SetBinContent(ibinX, ibinY, allYieldsAndErrors[yld]['acceptance'])
    hAcceptances.SetBinError(ibinX, ibinY, allYieldsAndErrors[yld]['acceptanceError'])

hYields.Write('yields')
hAcceptances.Write('acceptances')
acceptanceOutput.Close()
