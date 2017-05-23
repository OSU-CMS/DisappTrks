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

# '' will gives you Dataset_2016.root for the whole year
datasets = ['SingleMu_2015D', 'WJetsToLNu']

# Use HT/MHT/PFMET/etc correctly, or use metNoMu for everything?
useCorrectVariables = True

for dataset in datasets:

    fout = TFile.Open("triggerEfficiency_" + dataset + ".root", "recreate")

    if path == 'GrandOr' or path == "all":

        print "********************************************************************************"
        print "Calculating efficiency of the Grand Or in search region (", dataset, ")"
        print "--------------------------------------------------------------------------------"

        grandEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandEfficiency.addTFile(fout)
        grandEfficiency.addTCanvas(canvas)
        if 'SingleMu' in dataset:
            grandEfficiency.addLuminosityInInvPb(lumi["SingleMuon_2015D"])
        grandEfficiency.addChannel("Numerator", "GrandOrNumerator", dataset, dirs['Brian'] + "2015/triggerEfficiency_grandOr")
        grandEfficiency.addChannel("Denominator", "METLegDenominator", dataset, dirs['Brian'] + "2015/triggerEfficiency_grandOr")
        grandEfficiency.setDatasetLabel(dataset)
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
                if 'SingleMu' in dataset:
                    efficiency.addLuminosityInInvPb(lumi["SingleMuon_2015D"])
                if useCorrectVariables:
                    if 'PFMHTNoMu' in trigger:
                        efficiency.setMetLegHistName('Eventvariable Plots/MHTNoMuLogX')
                        efficiency.setMetLegAxisTitle('H_{T}^{miss, no #mu} [GeV]')
                    elif 'PFMHT' in trigger:
                        efficiency.setMetLegHistName('Eventvariable Plots/MHTLogX')
                        efficiency.setMetLegAxisTitle('H_{T}^{miss} [GeV]')
                    elif 'PFMET' in trigger:
                        efficiency.setMetLegHistName('Met Plots/metLogX')
                        efficiency.setMetLegAxisTitle('PF E_{T}^{miss}')

                efficiency.addChannel("Numerator", numeratorName, dataset, dirs['Brian'] + "2015/triggerEfficiency_allPaths")
                efficiency.addChannel("Denominator", denominatorName, dataset, dirs['Brian'] + "2015/triggerEfficiency_allPaths")
                efficiency.setDatasetLabel(dataset)
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

    compare(trigger, legName, 'SingleMu_2015D', 'WJetsToLNu', metAxisTitle, canvas, lumi["SingleMuon_2015D"], triggerFiltersMet[trigger])

for trigger in triggersMetAndIsoTrk:
    compare(trigger, 'TrackLeg', 'SingleMu_2015D', 'WJetsToLNu', 'Muon p_{T} [GeV]', canvas, lumi["SingleMuon_2015D"], triggerFiltersMet[trigger])

emptyFilters = []
compare('GrandOr', 'METPath', 'SingleMu_2015D', 'WJetsToLNu', 'PF E_{T}^{miss, no #mu}', canvas, lumi["SingleMuon_2015D"], emptyFilters)
