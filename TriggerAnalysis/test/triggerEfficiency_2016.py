#!/usr/bin/env python

from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile
import os
import re

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

datasets = ['2016BC', '2016DEFGH', 'WJetsToLNu']

# Use HT/MHT/PFMET/etc correctly, or use metNoMu for everything?
useCorrectVariables = True

for dataset in datasets:

    inputFile = "SingleMu_" + dataset
    inputFolder = "2016_final/triggerEfficiency_allPaths_v3"
    grandORInputFolder = "2016_final/triggerEfficiency_grandOr"
    if not "2016" in dataset:
        inputFile = dataset
        inputFolder = "2015/triggerEfficiency_allPaths_v2"
        grandORInputFolder = "2015/triggerEfficiency_grandOr"

    fout = TFile.Open("triggerEfficiency_" + inputFile + ".root", "recreate")

    if path == 'GrandOr' or path == "all":

        print "********************************************************************************"
        print "Calculating efficiency of the Grand Or in search region (", dataset, ")"
        print "--------------------------------------------------------------------------------"

        grandEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandEfficiency.addTFile(fout)
        grandEfficiency.addTCanvas(canvas)
        if "2016" in dataset:
            grandEfficiency.addLuminosityInInvPb(lumi["SingleMuon_" + dataset])
        grandEfficiency.addChannel("Numerator",
                                   "GrandOrNumerator",
                                   inputFile,
                                   dirs['Brian'] + grandORInputFolder)
        grandEfficiency.addChannel("Denominator",
                                   "METLegDenominator",
                                   inputFile,
                                   dirs['Brian'] + grandORInputFolder)
        grandEfficiency.setDatasetLabel(inputFile)
        grandEfficiency.plotEfficiency()
        print "********************************************************************************"

    for trigger in triggersMet:

        triggerWithoutUnderscores = re.sub(r"_", "", trigger)

        if path == trigger or path == "all":

            print "********************************************************************************"
            print "Calculating efficiency of", trigger, " in search region (", dataset, ")"
            print "--------------------------------------------------------------------------------"

            legs = ["METLeg", "TrackLeg"] if "IsoTrk50" in trigger else ["METPath"]

            for leg in legs:

                numeratorName = triggerWithoutUnderscores + "METLegNumerator"
                denominatorName = "METLegDenominator"

                if leg == "TrackLeg":
                    numeratorName = triggerWithoutUnderscores + "TrackLegNumeratorWithMuons"
                    denominatorName = triggerWithoutUnderscores + "TrackLegDenominatorWithMuons"

                efficiency = TriggerEfficiency(trigger, triggerFiltersMet[trigger], leg)
                efficiency.addTFile(fout)
                efficiency.addTCanvas(canvas)
                if "2016" in dataset:
                    efficiency.addLuminosityInInvPb(lumi["SingleMuon_" + dataset])
                if useCorrectVariables:
                    if 'PFMHTNoMu' in trigger:
                        efficiency.setMetLegHistName('Eventvariable Plots/MHTNoMuLogX')
                        efficiency.setMetLegAxisTitle('H_{T}^{miss, no #mu} [GeV]')
                    elif 'PFMHT' in trigger:
                        efficiency.setMetLegHistName('Eventvariable Plots/MHTLogX')
                        efficiency.setMetLegAxisTitle('H_{T}^{miss} [GeV]')
                    elif 'PFMET' in trigger:
                        efficiency.setMetLegHistName('Met Plots/metLogX')
                        efficiency.setMetLegAxisTitle('PF E_{T}^{miss} [GeV]')
                    else:
                        efficiency.setMetLegHistName('Met Plots/metNoMuLogX')
                        efficiency.setMetLegAxisTitle('PF E_{T}^{miss, no #mu} [GeV]')

                efficiency.addChannel("Numerator",
                                      numeratorName,
                                      inputFile,
                                      dirs['Brian'] + inputFolder)
                efficiency.addChannel("Denominator",
                                      denominatorName,
                                      inputFile,
                                      dirs['Brian'] + inputFolder)
                efficiency.setDatasetLabel(inputFile)
                efficiency.plotEfficiency()
                print "********************************************************************************"


    fout.Close()

# Compare MC to data

metAxisTitle = 'PF E_{T}^{miss, no #mu}'

for trigger in triggersMet:

    if useCorrectVariables:
        if 'PFMHTNoMu' in trigger:
            metAxisTitle = 'H_{T}^{miss, no #mu} [GeV]'
        elif 'PFMHT' in trigger:
            metAxisTitle = 'H_{T}^{miss} [GeV]'
        elif 'PFMET' in trigger:
            metAxisTitle = 'PF E_{T}^{miss}'
        else:
            metAxisTitle = 'PF E_{T}^{miss, no #mu}'

    legName = 'METLeg' if 'IsoTrk' in trigger else 'METPath'

    compare(trigger, legName, 'SingleMu_2016BC', 'WJetsToLNu', metAxisTitle, canvas, lumi["SingleMuon_2016BC"], triggerFiltersMet[trigger])
    compare(trigger, legName, 'SingleMu_2016DEFGH', 'WJetsToLNu', metAxisTitle, canvas, lumi["SingleMuon_2016DEFGH"], triggerFiltersMet[trigger])

for trigger in triggersMetAndIsoTrk:
    compare(trigger, 'TrackLeg', 'SingleMu_2016BC', 'WJetsToLNu', 'Muon p_{T} [GeV]', canvas, lumi["SingleMuon_2016BC"], triggerFiltersMet[trigger])
    compare(trigger, 'TrackLeg', 'SingleMu_2016DEFGH', 'WJetsToLNu', 'Muon p_{T} [GeV]', canvas, lumi["SingleMuon_2016DEFGH"], triggerFiltersMet[trigger])

emptyFilters = []
compare('GrandOr', 'METPath', 'SingleMu_2016BC', 'WJetsToLNu', 'PF E_{T}^{miss, no #mu}', canvas, lumi["SingleMuon_2016BC"], emptyFilters)
compare('GrandOr', 'METPath', 'SingleMu_2016DEFGH', 'WJetsToLNu', 'PF E_{T}^{miss, no #mu}', canvas, lumi["SingleMuon_2016DEFGH"], emptyFilters)
