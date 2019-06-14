#!/usr/bin/env python

from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile
import os
import re
import sys

gROOT.SetBatch()

dirs = getUser()

canvas = TCanvas("c1", "c1", 561, 482, 800, 830)
canvas.Range(0.644391, -0.1480839, 3.167468, 1.19299)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetBorderSize(2)
canvas.SetLogx()
canvas.SetTickx(1)
canvas.SetTicky(1)
canvas.SetLeftMargin(0.122807)
canvas.SetRightMargin(0.05012531)
canvas.SetTopMargin(0.06947891)
canvas.SetBottomMargin(0.1104218)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)

path = "all"
if len (sys.argv) > 1:
    path = sys.argv[1]

masses = [300, 700, 1100]
lifetimes = [10, 100, 1000, 10000]
datasetsDict = { (mass, lifetime) : ('AMSB_chargino_' + str(mass) + 'GeV_' + str(lifetime) + 'cm_94X') for mass in masses for lifetime in lifetimes }
labelsDict = { (mass, lifetime) : (str(mass) + ' GeV, c#tau = ' + str(lifetime) + ' cm') for mass in masses for lifetime in lifetimes }
datasets = datasetsDict.values()

inputFolder = dirs['Brian'] + '2017/triggerEfficiencySignal_v3'

for nLayersWord in ["NLayers4", "NLayers5", "NLayers6plus"]:
    for dataset in datasets:
        inputFile = dataset
        fout = TFile.Open("triggerEfficiency_" + inputFile + "_" + nLayersWord + ".root", "recreate")
        if path == 'GrandOr' or path == "all":
            print "********************************************************************************"
            print "Calculating efficiency of the Grand Or in dataset:", dataset, ")"
            print "--------------------------------------------------------------------------------"
            grandEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
            grandEfficiency.addTFile(fout)
            grandEfficiency.addTCanvas(canvas)
            grandEfficiency.addChannel("Numerator",   "GrandOrNumeratorTrk4" + nLayersWord, inputFile, inputFolder)
            grandEfficiency.addChannel("Denominator", "GrandOrDenominatorTrk" + nLayersWord, inputFile, inputFolder)
            grandEfficiency.setDatasetLabel(inputFile)
            grandEfficiency.setIsMC(True)
            grandEfficiency.plotEfficiency()
            print "********************************************************************************"
        for trigger in triggerFiltersTrack:
            triggerWithoutUnderscores = re.sub(r"_", "", trigger)
            if path == trigger or path == "all":
                print "********************************************************************************"
                print "Calculating efficiency of", trigger, "in dataset:", dataset, ")"
                print "--------------------------------------------------------------------------------"
                for leg in ["METLeg", "TrackLeg"]:
                    numeratorName = triggerWithoutUnderscores + "METLegNumeratorTrk" + nLayersWord
                    denominatorName = "METLegDenominatorTrk" + nLayersWord
                    if leg == "TrackLeg":
                        numeratorName = triggerWithoutUnderscores + "TrackLegNumeratorWithTracks" + nLayersWord
                        denominatorName = triggerWithoutUnderscores + "TrackLegDenominatorWithTracks" + nLayersWord
                    efficiency = TriggerEfficiency(trigger, triggerFiltersMet[trigger], leg)
                    efficiency.addTFile(fout)
                    efficiency.addTCanvas(canvas)
                    efficiency.setMetLegHistName('Met Plots/metNoMuLogX')
                    efficiency.setMetLegAxisTitle('PF E_{T}^{miss, no #mu} [GeV]')
                    efficiency.addChannel("Numerator",   numeratorName, inputFile, inputFolder)
                    efficiency.addChannel("Denominator", denominatorName, inputFile, inputFolder)
                    efficiency.setDatasetLabel(inputFile)
                    efficiency.setIsMC(True)
                    efficiency.plotEfficiency()
                    print "********************************************************************************"
        fout.Close()

###############################################
# make comparison plots
###############################################

def makeSpecificComparisonPlots(trigger, leg, nLayersWord, canvas, mass = -1, lifetime = -1):
    lineColors = [1, 632, 600, 8]
    xaxisLabel = 'Track p_{T} [GeV]' if leg is 'TrackLeg' else 'PF E_{T}^{miss, no #mu}'
    filtersList = []
    if leg is 'METLeg':
        filtersList = triggerFiltersMet[trigger]
    elif leg is 'TrackLeg':
        filtersList = triggerFiltersTrack[trigger]
    # for nLayersWord at one given mass, compare lifetimes
    if mass > 0:
        compareDatasets(trigger, leg, 
                        [datasetsDict[(mass, x)] + '_' + nLayersWord for x in lifetimes],
                        lineColors,
                        [labelsDict[(mass, x)] for x in lifetimes],
                        xaxisLabel, canvas, -1, filtersList, str(mass) + 'GeV_' + nLayersWord)
    # for nLayersWord at one given lifetime, compare masses
    elif lifetime > 0:
        compareDatasets(trigger, leg,
                        [datasetsDict[(x, lifetime)] + '_' + nLayersWord for x in masses],
                        lineColors,
                        [labelsDict[(x, lifetime)] for x in masses],
                        xaxisLabel, canvas, -1, filtersList, str(lifetime) + 'cm_' + nLayersWord)

for nLayersWord in ["NLayers4", "NLayers5", "NLayers6plus"]:
    makeSpecificComparisonPlots('GrandOr', 'METPath', nLayersWord, canvas, mass = 700)
    makeSpecificComparisonPlots('GrandOr', 'METPath', nLayersWord, canvas, lifetime = 100)

    makeSpecificComparisonPlots('HLT_MET105_IsoTrk50_v', 'METLeg', nLayersWord, canvas, mass = 700)
    makeSpecificComparisonPlots('HLT_MET105_IsoTrk50_v', 'METLeg', nLayersWord, canvas, lifetime = 100)

    makeSpecificComparisonPlots('HLT_MET105_IsoTrk50_v', 'TrackLeg', nLayersWord, canvas, mass = 700)
    makeSpecificComparisonPlots('HLT_MET105_IsoTrk50_v', 'TrackLeg', nLayersWord, canvas, lifetime = 100)

compareDatasets('GrandOr', 'METPath',
                ['AMSB_chargino_700GeV_100cm_94X_NLayers' + x for x in ['4', '5', '6plus']],
                [1, 632, 600, 8],
                ['NLayers' + x for x in ['4', '5', '6plus']],
                'PF E_{T}^{miss, no #mu}', canvas, -1, [], 'compareNLayers_700_100')
