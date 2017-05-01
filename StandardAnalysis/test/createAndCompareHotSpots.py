#!/usr/bin/python

# Create new lepton veto maps and compare to previous hot spots
# Usage:
# createAndCompareHotSpots.py MYCONDORDIR

from ROOT import gROOT, gStyle, TFile, TH2D, TCanvas, TEllipse, TLatex
import os
import sys
import math
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *

doPlots = True

gROOT.SetBatch()

def MakePlots(filePath, plotName, hotSpotsList):
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)
    can = TCanvas('can', 'can', 10, 10, 800, 800)

    circles = []

    for spots in hotSpotsList:
        circle = TEllipse(float(spots[0]), float(spots[1]), 0.06)
        circle.SetLineColor(2)
        circle.SetLineWidth(1)
        circle.SetFillStyle(0)
        circles.append(circle)

    topLeft_x_left    = 0.16129
    topLeft_y_bottom  = 0.832117
    topLeft_x_right   = 0.512673
    topLeft_y_top     = 0.892944
    topLeft_y_offset  = 0.04

    nFemtobarns = lumi['SingleElectron_2016'] / 1000.
    if 'muon' in plotName:
        nFemtobarns = lumi['SingleMuon_2016'] / 1000.

    LumiText = str.format('{0:.1f}', nFemtobarns) + " fb^{-1} (13 TeV)"

    pasLumiLatex = TLatex()
    pasLumiLatex.SetNDC()
    pasLumiLatex.SetTextAngle(0)
    #pasLumiLatex.SetTextColor(kBlack)
    pasLumiLatex.SetTextFont(42)
    pasLumiLatex.SetTextAlign(32)
    pasLumiLatex.SetTextSize(0.04)

    pasCMSLatex = TLatex()
    pasCMSLatex.SetNDC()
    pasCMSLatex.SetTextAngle(0)
    #pasCMSLatex.SetTextColor(kBlack)
    pasCMSLatex.SetTextFont(62)
    pasCMSLatex.SetTextAlign(12)
    pasCMSLatex.SetTextSize(0.04)

    pasPrelimLatex = TLatex()
    pasPrelimLatex.SetNDC()
    pasPrelimLatex.SetTextAngle(0)
    #pasPrelimLatex.SetTextColor(kBlack)
    pasPrelimLatex.SetTextFont(62)
    pasPrelimLatex.SetTextAlign(12)
    pasPrelimLatex.SetTextSize(0.04)

    inputFile = TFile(filePath, 'read')

    beforeVeto = inputFile.Get('beforeVeto')
    afterVeto = inputFile.Get('afterVeto')

    beforeVeto.Draw('colz')
    pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
    pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
    #pasPrelimLatex.DrawLatex(0.23, 0.925, "Preliminary")
    can.SaveAs('test_beforeVeto_' + plotName + '.pdf')

    afterVeto.Draw('colz')
    pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
    pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
    #pasPrelimLatex.DrawLatex(0.23, 0.925, "Preliminary")
    can.SaveAs('test_afterVeto_' + plotName + '.pdf')

    totalEventsBeforeVeto = 0
    totalEventsAfterVeto = 0

    nRegionsWithTag = 0

    # loop over all bins in eta-phi and count events before/after to calculate the mean inefficiency
    for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
        for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):

            if beforeVeto.GetBinContent(xbin, ybin) > 0:
                nRegionsWithTag += 1
            else:
                continue

            totalEventsBeforeVeto += beforeVeto.GetBinContent(xbin, ybin)
            totalEventsAfterVeto  += afterVeto.GetBinContent(xbin, ybin)

    meanInefficiency = totalEventsAfterVeto / totalEventsBeforeVeto

    # now with the mean, calculate the standard deviation as stdDev^2 = 1/(N-1) * sum(inefficiency - meanInefficiency)^2

    stdDevInefficiency = 0

    afterVeto.Divide(beforeVeto)

    for xbin in range(1, afterVeto.GetXaxis().GetNbins()):
        for ybin in range(1, afterVeto.GetYaxis().GetNbins()):

            if beforeVeto.GetBinContent(xbin, ybin) == 0:
                continue

            thisInefficiency = afterVeto.GetBinContent(xbin, ybin)

            stdDevInefficiency += (thisInefficiency - meanInefficiency)**2

    if nRegionsWithTag < 2:
        print 'Only ', nRegionsWithTag, ' regions with a tag lepton exist, cannot calculate fiducial map!!!'
        exit()

    stdDevInefficiency /= nRegionsWithTag - 1
    stdDevInefficiency = math.sqrt(stdDevInefficiency)

    if 'ele' in plotName:
        afterVeto.GetZaxis().SetRangeUser(0, 0.5)
    elif 'muon' in plotName:
        afterVeto.GetZaxis().SetRangeUser(0, 0.05)
    afterVeto.GetZaxis().SetLabelSize(0.025)
    afterVeto.Draw('colz')

    for circle in circles:
        circle.Draw("same")

    pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
    pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
    #pasPrelimLatex.DrawLatex(0.23, 0.925, "Preliminary")
    can.SaveAs('test_efficiency_' + plotName + '.pdf')

    for xbin in range(1, afterVeto.GetXaxis().GetNbins()):
        for ybin in range(1, afterVeto.GetYaxis().GetNbins()):

            thisInefficiency = afterVeto.GetBinContent(xbin, ybin)
            if thisInefficiency == 0:
                continue

            valueInSigma = (thisInefficiency - meanInefficiency) / stdDevInefficiency
            if valueInSigma < 0:
                valueInSigma = 0

            afterVeto.SetBinContent(xbin, ybin, valueInSigma)

    can.SetLogz(False)
    afterVeto.GetZaxis().SetLabelSize(0.04)
    afterVeto.Draw('colz')

    for circle in circles:
        circle.Draw("same")

    pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
    pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
    #pasPrelimLatex.DrawLatex(0.23, 0.925, "Preliminary")
    can.SaveAs('test_efficiencyInSigma_' + plotName + '.pdf')

    inputFile.Close()

def FindHotSpots(filePath):

    threshold = 2.0

    inputFile = TFile(filePath, 'read')

    beforeVeto = inputFile.Get('beforeVeto')
    afterVeto = inputFile.Get('afterVeto')

    totalEventsBeforeVeto = 0
    totalEventsAfterVeto = 0

    nRegionsWithTag = 0

    # loop over all bins in eta-phi and count events before/after to calculate the mean inefficiency
    for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
        for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):

            if beforeVeto.GetBinContent(xbin, ybin) > 0:
                nRegionsWithTag += 1
            else:
                continue

            totalEventsBeforeVeto += beforeVeto.GetBinContent(xbin, ybin)
            totalEventsAfterVeto  += afterVeto.GetBinContent(xbin, ybin)

    meanInefficiency = totalEventsAfterVeto / totalEventsBeforeVeto

    # now with the mean, calculate the standard deviation as stdDev^2 = 1/(N-1) * sum(inefficiency - meanInefficiency)^2

    stdDevInefficiency = 0

    afterVeto.Divide(beforeVeto)

    for xbin in range(1, afterVeto.GetXaxis().GetNbins()):
        for ybin in range(1, afterVeto.GetYaxis().GetNbins()):

            if beforeVeto.GetBinContent(xbin, ybin) == 0:
                continue

            thisInefficiency = afterVeto.GetBinContent(xbin, ybin)

            stdDevInefficiency += (thisInefficiency - meanInefficiency)**2

    if nRegionsWithTag < 2:
        print 'Only ', nRegionsWithTag, ' regions with a tag lepton exist, cannot calculate fiducial map!!!'
        exit()

    stdDevInefficiency /= nRegionsWithTag - 1
    stdDevInefficiency = math.sqrt(stdDevInefficiency)

    # now find hot spots where the inefficiency is larger than the meanInefficiency by at least threshold * stdDevInefficiency

    hotSpots = []

    for xbin in range(1, afterVeto.GetXaxis().GetNbins()):
        for ybin in range(1, afterVeto.GetYaxis().GetNbins()):

            thisInefficiency = afterVeto.GetBinContent(xbin, ybin)
            if thisInefficiency == 0:
                continue

            if (thisInefficiency - meanInefficiency) > threshold * stdDevInefficiency:
                eta = "{0:0.2f}".format(afterVeto.GetXaxis().GetBinCenter(xbin))
                phi = "{0:0.2f}".format(afterVeto.GetYaxis().GetBinCenter(ybin))
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

    breakdown = ''

    for eta, phi in hotSpots:

        # for each hot spot, we want to print something like:
        # (eta, phi) -- B 0.5 / C 0.25 / D 0.30 ...
        # in units of events per inverse picobarn

        breakdown = '(' + eta + ', ' + phi + ') -- '

        for period, after in afterVeto_PerRun:

            breakdown += period[-1] + ' '

            nEvents = after.GetBinContent( after.FindBin(float(eta), float(phi)) )
            nPicobarns = lumi[lumiName] / 1000

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
