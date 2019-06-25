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

masses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
datasetsDict = { mass : ('AMSB_chargino_' + str(mass) + 'GeV_allLifetimes') for mass in masses }
labelsDict = { mass : (str(mass) + ' GeV') for mass in masses }
datasets = datasetsDict.values()

inputFolder = dirs['Brian'] + '2017/grandOr_signal_full'

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
        fout.Close()

###############################################
# make comparison plots
###############################################

def makeSpecificComparisonPlots(trigger, leg, nLayersWord, canvas, mass = -1):
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
                        [datasetsDict[mass] + '_' + nLayersWord],
                        lineColors,
                        [labelsDict[(mass, x)] for x in lifetimes],
                        xaxisLabel, canvas, -1, filtersList, str(mass) + 'GeV_' + nLayersWord)

compareDatasets('GrandOr', 'METPath',
                ['AMSB_chargino_700GeV_allLifetimes_NLayers' + x for x in ['4', '5', '6plus']],
                [1, 632, 600, 8],
                ['NLayers' + x for x in ['4', '5', '6plus']],
                'PF E_{T}^{miss, no #mu}', canvas, -1, [], 'compareNLayers_700_100')
