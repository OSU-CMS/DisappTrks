#!/usr/bin/env python3

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

datasets = ['2017CDEF']

# Use HT/MHT/PFMET/etc correctly, or use metNoMu for everything?
useCorrectVariables = True

for dataset in datasets:

    inputFile = "SingleMu_" + dataset
    inputFolder = "2017/triggerEfficiencyData"
    grandORInputFolderDeno = "2017/triggerEfficiencyGrandOr_SingleMu_Deno"
    grandORInputFolderNum = "2017/triggerEfficiencyGrandOr_SingleMu"

    fout = TFile.Open("triggerEfficiency_" + inputFile + ".root", "recreate")

    if path == 'GrandOr' or path == "all":

        print "********************************************************************************"
        print "Calculating efficiency of the Grand Or in dataset:", dataset, ")"
        print "--------------------------------------------------------------------------------"

        grandEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandEfficiency.addTFile(fout)
        grandEfficiency.addTCanvas(canvas)
        if "2017" in dataset:
            grandEfficiency.addLuminosityInInvPb(lumi["SingleMuon_" + dataset])
        grandEfficiency.addChannel("Numerator",
                                   "GrandOrNumerator",
                                   inputFile,
                                   dirs['Kai'] + grandORInputFolderNum)
        grandEfficiency.addChannel("Denominator",
                                   "GrandOrDenominator",
                                   inputFile,
                                   dirs['Kai'] + grandORInputFolderDeno)
        grandEfficiency.setDatasetLabel(inputFile)
        grandEfficiency.plotEfficiency()
        print "********************************************************************************"

    for trigger in triggerFiltersMet:

        triggerWithoutUnderscores = re.sub(r"_", "", trigger)

        if path == trigger or path == "all" or (path == "main" and "IsoTrk50" in trigger):

            print "********************************************************************************"
            print "Calculating efficiency of", trigger, " in dataset:", dataset, ")"
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
                if "2017" in dataset:
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

compareTriggers("HLT_MET105_IsoTrk50_v", "HLT_MET120_IsoTrk50_v", "TrackLeg", "SingleMu_2017CDEF", "Muon p_{T} [GeV]", canvas, lumi["SingleMuon_2017CDEF"], ['hltMET105/120', 'hltMETClean65'])
compareTriggers("HLT_MET105_IsoTrk50_v", "HLT_MET120_IsoTrk50_v", "METLeg", "SingleMu_2017CDEF", "PF E_{T}^{miss, no #mu}", canvas, lumi["SingleMuon_2017CDEF"], ['hltMET105/120', 'hltMETClean65'])
