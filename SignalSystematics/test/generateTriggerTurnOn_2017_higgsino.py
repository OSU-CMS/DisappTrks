#!/usr/bin/env python3

import math
from DisappTrks.SignalSystematics.signalSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.integrated_luminosity import *
from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from ROOT import TFile, TCanvas
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700, 800, 900]
lifetimes = ['10', '100', '1000', '10000']
allLifetimes = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1',
               '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '20', '30', '40', '50', '60', '70', '80', '90', '100',
               '200', '300', '400', '500', '600', '700', '800', '900', '1000',
               '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
suffix = "94X"

extraSamples = getExtraSamples(suffix, isHiggsino = True)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

nLayersWord = "NLayers4"
if len(sys.argv) > 2:
    nLayersWord = sys.argv[2]

lumi = lumi["MET_2017"]


if (systematic == "TRIGGER_TURN_ON" or systematic == "ALL") and nLayersWord != 'NLayers6plus':

    # first calculate the trigger turn-on curves for this category and NLayers6plus
    print "********************************************************************************"
    print "evaluating trigger turn-on curves (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

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

    foutForEfficienciesThisNLayers = TFile('triggerEfficiency_Higgsino_' + nLayersWord + '.root', 'recreate')
    foutForEfficienciesNLayers6plus = TFile('triggerEfficiency_Higgsino_NLayers6plus.root', 'recreate')

    for mass in masses:
        inputFile = 'Higgsino_' + str(mass) + 'GeV_allLifetimes'

        grandOrEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandOrEfficiency.addTFile(foutForEfficienciesThisNLayers, nameSuffix = 'Higgsino_' + str(mass) + 'GeV')
        grandOrEfficiency.addTCanvas(canvas)
        grandOrEfficiency.addChannel("Numerator",   "GrandOrNumeratorTrk4"   + nLayersWord, inputFile, dirs['Kai'] + '2017/grandOr_signal_verB')
        grandOrEfficiency.addChannel("Denominator", "GrandOrDenominatorTrk" + nLayersWord, inputFile, dirs['Kai'] + '2017/grandOr_signal_verB')
        grandOrEfficiency.setDatasetLabel(inputFile)
        grandOrEfficiency.setIsMC(True)
        grandOrEfficiency.plotEfficiency()

        grandOrEfficiencyNLayers6plus = TriggerEfficiency('GrandOr', [], 'METPath')
        grandOrEfficiencyNLayers6plus.addTFile(foutForEfficienciesNLayers6plus, nameSuffix = 'Higgsino_' + str(mass) + 'GeV')
        grandOrEfficiencyNLayers6plus.addTCanvas(canvas)
        grandOrEfficiencyNLayers6plus.addChannel("Numerator",   "GrandOrNumeratorTrk4NLayers6plus",   inputFile, dirs['Kai'] + '2017/grandOr_signal_verB')
        grandOrEfficiencyNLayers6plus.addChannel("Denominator", "GrandOrDenominatorTrkNLayers6plus", inputFile, dirs['Kai'] + '2017/grandOr_signal_verB')
        grandOrEfficiencyNLayers6plus.setDatasetLabel(inputFile)
        grandOrEfficiencyNLayers6plus.setIsMC(True)
        grandOrEfficiencyNLayers6plus.plotEfficiency()


    print "********************************************************************************\n\n"


    print "\n\n"
