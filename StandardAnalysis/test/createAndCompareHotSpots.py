#!/usr/bin/python

# Create new lepton veto maps and compare to previous hot spots
# Usage:
# createAndCompareHotSpots.py MYCONDORDIR

from ROOT import TFile, TH2D
import os
import sys
import math

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

    for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
        for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):
            binRadius = math.hypot(0.5 * beforeVeto.GetXaxis().GetBinWidth(xbin), 0.5 * beforeVeto.GetYaxis().GetBinWidth(ybin))
            if binRadius > minDeltaR:
                minDeltaR = binRadius

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
    oldNotNew = []
    for old in oldHotSpots:
        thisInNew = False
        for new in newHotSpots:
            if old == new:
                thisInNew = True
                break
        if not thisInNew:
            print old

    print '\nNew hot spots:'
    newNotOld = []
    for new in newHotSpots:
        thisInOld = False
        for old in oldHotSpots:
            if new == old:
                thisInOld = True
                break
        if not thisInOld:
            print new

    print '\nHot spots that are in both maps:'
    both = []
    for old in oldHotSpots:
        for new in newHotSpots:
            if old == new:
                print old

if len(sys.argv) < 2:
    print "ERROR:  Must specify name of condor directory as argument."
    exit(0)

condorDir = "condor/" + sys.argv[1]

datasetList = os.listdir(condorDir)

beforeVetoEle = TH2D()
afterVetoEle = TH2D()

beforeVetoMu = TH2D()
afterVetoMu = TH2D()

foundHistogramsEle = False
foundHistogramsMu = False

beforeHistName = 'FiducialCalcBeforePlotter/Track Plots/trackEtaVsPhi'
afterHistName = 'FiducialCalcAfterPlotter/Track Plots/trackEtaVsPhi'

for dataset in datasetList:
    if not dataset.endswith('.root'):
        continue

    inputFile = TFile(os.getcwd() + '/' + condorDir + '/' + dataset, 'read')

    print 'Adding trackEtaVsPhi from ', dataset

    if 'SingleEle' in dataset:
        if not foundHistogramsEle:
            beforeVetoEle = inputFile.Get('Electron' + beforeHistName)
            beforeVetoEle.SetDirectory(0)
            afterVetoEle = inputFile.Get('Electron' + afterHistName)
            afterVetoEle.SetDirectory(0)
            foundHistogramsEle = True
        else:
            beforeVetoEle.Add(inputFile.Get('Electron' + beforeHistName))
            afterVetoEle.Add(inputFile.Get('Electron' + afterHistName))

    elif 'SingleMu' in dataset:
        if not foundHistogramsMu:
            beforeVetoMu = inputFile.Get('Muon' + beforeHistName)
            beforeVetoMu.SetDirectory(0)
            afterVetoMu = inputFile.Get('Muon' + afterHistName)
            afterVetoMu.SetDirectory(0)
            foundHistogramsMu = True
        else:
            beforeVetoMu.Add(inputFile.Get('Muon' + beforeHistName))
            afterVetoMu.Add(inputFile.Get('Muon' + afterHistName))

    inputFile.Close()

if foundHistogramsEle:
    print 'Creating map file test_newElectronMap.root'
    outputFileEle = TFile('test_newElectronMap.root', 'recreate')
    outputFileEle.cd()
    beforeVetoEle.Write('beforeVeto')
    afterVetoEle.Write('afterVeto')
    outputFileEle.Close()

if foundHistogramsMu:
    print 'Creating map file test_newMuonMap.root'
    outputFileMu = TFile('test_newMuonMap.root', 'recreate')
    outputFileMu.cd()
    beforeVetoMu.Write('beforeVeto')
    afterVetoMu.Write('afterVeto')

# now compare to the existing maps
if foundHistogramsEle:
    existingMapEle = FindHotSpots(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root')
    newMapEle = FindHotSpots(os.getcwd() + '/test_newElectronMap.root')

    CompareHotSpots(existingMapEle, newMapEle)

if foundHistogramsMu:
    existingMapMu = FindHotSpots(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root')
    newMapMu = FindHotSpots(os.getcwd() + '/test_newMuonMap.root')

    CompareHotSpots(existingMapMu, newMapMu)

