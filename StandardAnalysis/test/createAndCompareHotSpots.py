#!/usr/bin/python

# Create new lepton veto maps and compare to previous hot spots
# Usage:
# createAndCompareHotSpots.py MYCONDORDIR

from ROOT import gROOT, gStyle, TFile, TH2D, TCanvas, TEllipse
import os
import sys
import math
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *

doPlots = True

gROOT.SetBatch()

def MakePlots(filePath, plotName, hotSpotsList):
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)
    can = TCanvas('can', 'can', 10, 10, 800, 600)

    inputFile = TFile(filePath, 'read')

    beforeVeto = inputFile.Get('beforeVeto')
    afterVeto = inputFile.Get('afterVeto')

    beforeVeto.Draw('colz')
    can.SaveAs('test_beforeVeto_' + plotName + '.pdf')

    afterVeto.Draw('colz')
    can.SaveAs('test_afterVeto_' + plotName + '.pdf')

    a = 0
    aErr2 = 0
    b = 0
    bErr2 = 0

    for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
        for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):

            contentBeforeVeto = beforeVeto.GetBinContent(xbin, ybin)
            errorBeforeVeto = beforeVeto.GetBinError(xbin, ybin)

            if contentBeforeVeto == 0:
                continue

            contentAfterVeto = afterVeto.GetBinContent(xbin, ybin)
            errorAfterVeto = afterVeto.GetBinError(xbin, ybin)

            a += contentAfterVeto
            aErr2 += errorAfterVeto * errorAfterVeto

            b += contentBeforeVeto
            bErr2 += errorBeforeVeto * errorBeforeVeto

    mean = a / b
    meanErr = mean * math.hypot(math.sqrt(aErr2) / a, math.sqrt(bErr2) / b)

    afterVeto.Divide(beforeVeto)
    can.SetLogz(True)
    afterVeto.Draw('colz')
    can.SaveAs('test_efficiency_' + plotName + '.pdf')

    for xbin in range(1, afterVeto.GetXaxis().GetNbins()):
        for ybin in range(1, afterVeto.GetYaxis().GetNbins()):
            content = afterVeto.GetBinContent(xbin, ybin)
            error = afterVeto.GetBinError(xbin, ybin)

            if content == 0:
                continue

            valueInSigma = (content - mean) / math.hypot(error, meanErr)
            if valueInSigma < 0:
                valueInSigma = 0

            afterVeto.SetBinContent(xbin, ybin, valueInSigma)

    can.SetLogz(False)
    afterVeto.Draw('colz')

    circles = []

    for spots in hotSpotsList:
        circle = TEllipse(float(spots[0]), float(spots[1]), 0.05)
        circle.SetLineColor(2)
        circle.SetLineWidth(1)
        circle.SetFillStyle(0)
        circle.Draw("same")
        circles.append(circle)

    can.SaveAs('test_efficiencyInSigma_' + plotName + '.pdf')

    inputFile.Close()

def FindHotSpots(filePath):

    minDeltaR = 0.05
    threshold = 2.0

    inputFile = TFile(filePath, 'read')

    beforeVeto = inputFile.Get('beforeVeto')
    afterVeto = inputFile.Get('afterVeto')

    a = 0
    aErr2 = 0
    b = 0
    bErr2 = 0

    nRegionsWithTag = 0

    for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
        for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):
            binRadius = math.hypot(0.5 * beforeVeto.GetXaxis().GetBinWidth(xbin), 0.5 * beforeVeto.GetYaxis().GetBinWidth(ybin))
            if binRadius > minDeltaR:
                minDeltaR = binRadius

            contentBeforeVeto = beforeVeto.GetBinContent(xbin, ybin)
            errorBeforeVeto = beforeVeto.GetBinError(xbin, ybin)

            if contentBeforeVeto == 0:
                continue

            nRegionsWithTag += 1

            contentAfterVeto = afterVeto.GetBinContent(xbin, ybin)
            errorAfterVeto = afterVeto.GetBinError(xbin, ybin)

            a += contentAfterVeto
            aErr2 += errorAfterVeto * errorAfterVeto

            b += contentBeforeVeto
            bErr2 += errorBeforeVeto * errorBeforeVeto

    print 'For file ', os.path.basename(filePath), ' total regions with tag activity = ', nRegionsWithTag

    mean = a / b
    meanErr = mean * math.hypot(math.sqrt(aErr2) / a, math.sqrt(bErr2) / b)

    print 'For file ', os.path.basename(filePath), ' the overall inefficiency is: ', mean, ' +/- ', meanErr

    afterVeto.Divide(beforeVeto)

    hotSpots = []

    for xbin in range(1, afterVeto.GetXaxis().GetNbins()):
        for ybin in range(1, afterVeto.GetYaxis().GetNbins()):
            content = afterVeto.GetBinContent(xbin, ybin)
            error = afterVeto.GetBinError(xbin, ybin)
            eta = "{0:0.2f}".format(afterVeto.GetXaxis().GetBinCenter(xbin))
            phi = "{0:0.2f}".format(afterVeto.GetYaxis().GetBinCenter(ybin))

            if content == 0:
                continue

            if (content - mean) > threshold * math.hypot(error, meanErr):
                hotSpots.append((eta, phi))

    inputFile.Close()

    return hotSpots

def CompareHotSpots(oldHotSpots, newHotSpots):

    print '\n\nHot spots that went away with new data:'
    nWentAway = 0
    # look through all the old hot spots
    for old in oldHotSpots:
        thisInNew = False

        # look through all the new ones and see if we find the old one
        for new in newHotSpots:
            if old == new:
                thisInNew = True
                break

        # if you didn't find the old spot in the new list, it went away
        if not thisInNew:
            print old
            nWentAway += 1

    print 'Total hot spots that went away = ', nWentAway

    print '\nNew hot spots:'
    nNewSpots = 0
    # look through new hot spots
    for new in newHotSpots:
        thisInOld = False

        # look through all the old ones and see if we find the new one
        for old in oldHotSpots:
            if new == old:
                thisInOld = True
                break

        # if you didn't find the new spot in the old list, it appeared as a new one
        if not thisInOld:
            print new
            nNewSpots += 1

    print 'Total new hot spots = ', nNewSpots

    print '\nHot spots that are in both maps:'
    nInBoth = 0

    # look thorugh old list
    for old in oldHotSpots:

        # look through the new list and see if we find the new one
        for new in newHotSpots:
            if old == new:
                print old
                nInBoth += 1

    print 'Total that were in both = ', nInBoth

def BreakdownHotSpots(hotSpots, afterVeto_PerRun):

    # afterVeto_PerRun is a list of tuples like ('B', TH2D)
    # first sort this by the run period to be in order
    afterVeto_PerRun.sort()

    outputName = 'HotSpots_breakdown.txt'
    lumiName = afterVeto_PerRun[0][0]

    if 'SingleEle' in lumiName:
        outputName = 'ele' + outputName
        lumiName = lumiName.replace('Ele', 'Electron')
    elif 'SingleMu' in lumiName:
        outputName = 'muon' + outputName
        lumiName = lumiName.replace('Mu', 'Muon')

    output = open(outputName, 'w')

    output.write('Events per inverse femtobarn\n')

    overallRatesPerRun = {}
    for period, after in afterVeto_PerRun:
	overallRatesPerRun[period] = [0, 0]

    for eta, phi in hotSpots:

        # for each hot spot, we want to print something like:
        # (eta, phi) -- B 0.5 / C 0.25 / D 0.30 ...
        # in units of events per inverse picobarn

        breakdown = '(' + eta + ', ' + phi + ') -- '

        for period, after in afterVeto_PerRun:

            breakdown += period[-1] + ' '

            nEvents = after.GetBinContent( after.FindBin(float(eta), float(phi)) )
            nPicobarns = lumi[lumiName] / 1000

#            breakdown += str('%.2g' % nEvents / nPicobarns)

	    breakdown += "{0:0.2f}".format(nEvents / nPicobarns)
            breakdown += ' / '

	    overallRatesPerRun[period][0] = overallRatesPerRun[period][0] + nEvents / nPicobarns
	    overallRatesPerRun[period][1] = math.hypot( overallRatesPerRun[period][1], math.sqrt(nEvents) / nPicobarns )

	breakdown += '\n'

        output.write(breakdown)

    output.write('\nOverall:\n')
    for period in overallRatesPerRun:
	output.write(period + ' -- ')
	output.write("{0:0.2f}".format(overallRatesPerRun[period][0]))
	output.write(' +/- ')
	output.write("{0:0.2f}".format(overallRatesPerRun[period][1]))
	output.write('\n')

    output.close()

if len(sys.argv) < 2:
    print "ERROR:  Must specify name of condor directory as argument."
    exit(0)

condorDir = "condor/" + sys.argv[1]

datasetList = os.listdir(condorDir)

beforeVeto = TH2D()
afterVeto = TH2D()
afterVeto_PerRun = []

foundEleDataset = False
foundMuonDataset = False
foundFirstDataset = False

beforeHistName = 'FiducialCalcBeforePlotter/Track Plots/trackEtaVsPhi'
afterHistName = 'FiducialCalcAfterPlotter/Track Plots/trackEtaVsPhi'

for dataset in datasetList:

    # skip non-ROOT files
    if not dataset.endswith('.root'):
        continue

    # skip any hadd-ed data periods
    if dataset.endswith('BC.root') or dataset.endswith('DEFGH.root') or dataset.endswith('2016.root'):
       continue

    # figure out what type of lepton dataset this is from the file name
    if 'SingleEle' in dataset:
        if not foundEleDataset:
            beforeHistName = 'Electron' + beforeHistName
            afterHistName = 'Electron' + afterHistName
        foundEleDataset = True

    if 'SingleMu' in dataset:
        if not foundMuonDataset:
            beforeHistName = 'Muon' + beforeHistName
            afterHistName = 'Muon' + afterHistName
        foundMuonDataset = True

    # If a directory has both ele and muon datasets, bail
    if foundEleDataset and foundMuonDataset:
        print 'Found both electron and muon datasets -- would create a bad map, quitting!'
        break

    # If directory has something besides ele/muon datasets, bail
    if not foundEleDataset and not foundMuonDataset:
        print 'Found a dataset other than SingleEle or SingleMu -- would create a bad map, quitting!'
        break

    inputFile = TFile(os.getcwd() + '/' + condorDir + '/' + dataset, 'read')
    print 'Adding trackEtaVsPhi from ', dataset

    thisBefore = inputFile.Get(beforeHistName)
    thisBefore.SetDirectory(0)

    thisAfter = inputFile.Get(afterHistName)
    thisAfter.SetDirectory(0)
    afterVeto_PerRun.append( (dataset[:-5], thisAfter) )

    if not foundFirstDataset:
        beforeVeto = thisBefore
        afterVeto = thisAfter
        foundFirstDataset = True
    else:
        beforeVeto.Add(thisBefore)
        afterVeto.Add(thisAfter)

    inputFile.Close()

if not foundEleDataset and not foundMuonDataset:
    exit()

outputName = 'test_newElectronMap.root'
if foundMuonDataset:
    outputName = 'test_newMuonMap.root'

print 'Creating map file ', outputName
outputFile = TFile(outputName, 'recreate')
beforeVeto.Write('beforeVeto')
afterVeto.Write('afterVeto')
outputFile.Close()

# now compare to the existing maps
if foundEleDataset:

    existingMapEle = FindHotSpots(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/electronFiducialMap_2016ReReco_data.root')
    newMapEle = FindHotSpots(os.getcwd() + '/test_newElectronMap.root')

    CompareHotSpots(existingMapEle, newMapEle)
    BreakdownHotSpots(newMapEle, afterVeto_PerRun)

    if doPlots:
        MakePlots(os.getcwd() + '/test_newElectronMap.root', 'ele', newMapEle)

if foundMuonDataset:
    existingMapMu = FindHotSpots(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/muonFiducialMap_2016ReReco_data.root')
    newMapMu = FindHotSpots(os.getcwd() + '/test_newMuonMap.root')

    CompareHotSpots(existingMapMu, newMapMu)
    BreakdownHotSpots(newMapMu, afterVeto_PerRun)

    if doPlots:
        MakePlots(os.getcwd() + '/test_newMuonMap.root', 'muon', newMapMu)
