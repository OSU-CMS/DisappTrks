#!/usr/bin/env python3

from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.integrated_luminosity import *
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

datasets = ['2018']

# Use HT/MHT/PFMET/etc correctly, or use metNoMu for everything?
useCorrectVariables = True

for dataset in datasets:

    inputFile = "EGamma_" + dataset
    grandORInputFolder = "2018/fromLPC/triggerEfficiencyWithElectrons"

    fout = TFile.Open("triggerEfficiency_" + inputFile + ".root", "recreate")

    if path == 'GrandOr' or path == "all":

        print "********************************************************************************"
        print "Calculating efficiency of the Grand Or in dataset:", dataset, ")"
        print "--------------------------------------------------------------------------------"

        grandEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandEfficiency.addTFile(fout)
        grandEfficiency.addTCanvas(canvas)
        grandEfficiency.addLuminosityInInvPb(lumi["EGamma_" + dataset])
        grandEfficiency.addChannel("Numerator",
                                   "GrandOrNumeratorWithElectrons",
                                   inputFile,
                                   dirs['Brian'] + grandORInputFolder)
        grandEfficiency.addChannel("Denominator",
                                   "GrandOrDenominatorWithElectrons",
                                   inputFile,
                                   dirs['Brian'] + grandORInputFolder)
        grandEfficiency.setDatasetLabel(inputFile)
        grandEfficiency.plotEfficiency()
        print "********************************************************************************"

