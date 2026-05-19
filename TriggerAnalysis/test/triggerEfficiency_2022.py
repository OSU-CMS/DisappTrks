#!/usr/bin/env python3

from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.integrated_luminosity import *
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

path = "PFMET105IsoTrk"
skipTrackLeg = False

if len (sys.argv) > 1:
    path = sys.argv[1]

datasets = ['2022C','2022D', 'WJetsToLNu']
datasets = ['2022C']
# Use HT/MHT/PFMET/etc correctly, or use metNoMu for everything?
useCorrectVariables = True

for dataset in datasets:

    inputFile = "SingleMu_" + dataset
    inputFolder = "2022/TrackLeg_v2"
    grandORInputFolder = "2022/GrandOrTrigger_v2"
    PFMETIsoTrkInputFolder = "2022/TrigEff_PFMET_IsoTrk"

    if dataset == 'WJetsToLNu':
        inputFile = dataset
        grandORInputFolder = "2018/grandOrEfficiency_WJets"

    fout = TFile.Open("triggerEfficiency_" + inputFile + ".root", "recreate")

    if path == 'GrandOr' or path == "all":

        print( "********************************************************************************")
        print( "Calculating efficiency of the Grand Or in dataset (", dataset, ")")
        print( "--------------------------------------------------------------------------------")

        grandEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandEfficiency.addTFile(fout)
        grandEfficiency.addTCanvas(canvas)
        if "2022" in dataset:
            grandEfficiency.addLuminosityInInvPb(lumi["SingleMu_" + dataset])
        grandEfficiency.addChannel("Numerator",
                                   "GrandOrNumerator",
                                   inputFile,
                                   dirs['Kai'] + grandORInputFolder)
        grandEfficiency.addChannel("Denominator",
                                   "GrandOrDenominator",
                                   inputFile,
                                   dirs['Kai'] + grandORInputFolder)
        grandEfficiency.setDatasetLabel(inputFile)
        grandEfficiency.plotEfficiency()
        print( "********************************************************************************")

    if path == 'PFMET105IsoTrk':

        print( "********************************************************************************")
        print( "Calculating efficiency of the HLT_PFMET105_IsoTrk50_v* in dataset (", dataset, ")")
        print( "--------------------------------------------------------------------------------")

        legs = ["hltMETLeg","TrackLeg","hltPFMETLeg"]

        for leg in legs:
            if leg == "hltMETLeg":
                numeratorName = "HLTPFMET105IsoTrk50vhltMETLegNumeratorWithMuons"
                denominatorName = "METLegDenominator"
                filters = []
            if leg == "TrackLeg":
                numeratorName = "HLTPFMET105IsoTrk50visoTrkLegNumeratorWithMuons"
                denominatorName = "HLTPFMET105IsoTrk50vhltMETLegNumeratorWithMuons"
                filters = ['hltMET75']
            if leg == "hltPFMETLeg":
                numeratorName = "HLTPFMET105IsoTrk50vPFMETLegNumeratorWithMuons"
                denominatorName = "HLTPFMET105IsoTrk50visoTrkLegNumeratorWithMuons"
                filters = ['hltMET75','hltTrk50Filter']

            PFMETIsoTrkEfficiency = TriggerEfficiency('HLT_PFMET105_IsoTrk50_v*',filters , leg)
            PFMETIsoTrkEfficiency.addTFile(fout)
            PFMETIsoTrkEfficiency.addTCanvas(canvas)

            if leg != "TrackLeg":
                PFMETIsoTrkEfficiency.setMetLegHistName('Met Plots/metLogX')
                PFMETIsoTrkEfficiency.setMetLegAxisTitle('PF E_{T}^{miss} [GeV]')

            if "2022" in dataset:
                PFMETIsoTrkEfficiency.addLuminosityInInvPb(lumi["SingleMu_" + dataset])
            PFMETIsoTrkEfficiency.addChannel("Numerator",
                                   numeratorName,
                                   inputFile,
                                   dirs['Kai'] + PFMETIsoTrkInputFolder)
            PFMETIsoTrkEfficiency.addChannel("Denominator",
                                   denominatorName,
                                   inputFile,
                                   dirs['Kai'] + PFMETIsoTrkInputFolder)
            PFMETIsoTrkEfficiency.setDatasetLabel(inputFile)
            PFMETIsoTrkEfficiency.plotEfficiency()
        print( "********************************************************************************")

    if dataset == 'WJetsToLNu':
        continue

    for trigger in triggerFiltersMet:

        triggerWithoutUnderscores = re.sub(r"_", "", trigger)

        if path == trigger or path == "all" or (path == "main" and "IsoTrk50" in trigger):

            print( "********************************************************************************")
            print( "Calculating efficiency of", trigger, " in search region (", dataset, ")")
            print( "--------------------------------------------------------------------------------")


            legs = ["METLeg", "TrackLeg"] if "IsoTrk50" in trigger else ["METPath"]

            for leg in legs:

                numeratorName = triggerWithoutUnderscores + "METLegNumerator"
                denominatorName = "METLegDenominator"

                if leg == "TrackLeg" and not skipTrackLeg:
                    numeratorName = triggerWithoutUnderscores + "TrackLegNumeratorWithMuons"
                    denominatorName = triggerWithoutUnderscores + "TrackLegDenominatorWithMuons"

                efficiency = TriggerEfficiency(trigger, triggerFiltersMet[trigger], leg)
                efficiency.addTFile(fout)
                efficiency.addTCanvas(canvas)
                if "2022" in dataset:
                    efficiency.addLuminosityInInvPb(lumi["SingleMu_" + dataset])
                if useCorrectVariables:
                    if 'PFMETNoMu' in trigger:
                        efficiency.setMetLegHistName('Met Plots/metNoMuLogX')
                        efficiency.setMetLegAxisTitle('PF E_{T}^{miss, no #mu} [GeV]')
                    elif 'PFMHTNoMu' in trigger:
                        efficiency.setMetLegHistName('Eventvariable Plots/MHTNoMuLogX')
                        efficiency.setMetLegAxisTitle('H_{T}^{miss, no #mu} [GeV]')
                    elif 'PFMET' in trigger:
                        efficiency.setMetLegHistName('Met Plots/metLogX')
                        efficiency.setMetLegAxisTitle('PF E_{T}^{miss} [GeV]')
                    elif 'PFMHT' in trigger:
                        efficiency.setMetLegHistName('Eventvariable Plots/MHTLogX')
                        efficiency.setMetLegAxisTitle('H_{T}^{miss} [GeV]')
                    else:
                        if 'IsoTrk50' not in trigger:
                            print( 'Not clear what the correct x-axis data should be for this trigger. Using metNoMu.')
                        efficiency.setMetLegHistName('Met Plots/metNoMuLogX')
                        efficiency.setMetLegAxisTitle('PF E_{T}^{miss, no #mu} [GeV]')

                efficiency.addChannel("Numerator",
                                      numeratorName,
                                      inputFile,
                                      dirs['Kai'] + inputFolder)
                efficiency.addChannel("Denominator",
                                      denominatorName,
                                      inputFile,
                                      dirs['Kai'] + inputFolder)
                efficiency.setDatasetLabel(inputFile)
                efficiency.plotEfficiency()
                print( "********************************************************************************")


    fout.Close()

# Compare MC to data
metAxisTitle = 'PF E_{T}^{miss, no #mu}'

#compare('GrandOr', 'METPath', 'SingleMu_2018BC', 'WJetsToLNu', 'PF E_{T}^{miss, no #mu}', canvas, lumi["SingleMuon_2018BC"], [])
