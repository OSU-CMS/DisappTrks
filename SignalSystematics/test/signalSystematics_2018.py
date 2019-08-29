#!/usr/bin/env python

import math
from DisappTrks.SignalSystematics.signalSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from ROOT import TFile, TCanvas
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
lifetimes = ['1', '10', '100', '1000', '10000']
allLifetimes = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1',
               '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '20', '30', '40', '50', '60', '70', '80', '90', '100',
               '200', '300', '400', '500', '600', '700', '800', '900', '1000',
               '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
suffix = "102X"

extraSamples = getExtraSamples(suffix)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

nLayersWord = "NLayers4"
if len(sys.argv) > 2:
    nLayersWord = sys.argv[2]

lumi = lumi["MET_2018"]

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2018_" + nLayersWord + ".txt", "w")

    pileupSystematic = WeightSystematicFromTrees(masses, allLifetimes, lumi)
    pileupSystematic.addFout(fout)
    pileupSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2018/signalAcceptance_v3")
    pileupSystematic.defineWeightToFluctuate('eventvariable_puScalingFactor')
    pileupSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if (systematic == "MET" or systematic == "ALL") and False:

    print "********************************************************************************"
    print "evaluating met systematics (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    metVaryTypes = [
        'JetRes',
        'JetEn',
        'ElectronEn',
        'TauEn',
        'UnclusteredEn',
        'PhotonEn',
    ]

    metSystematic = MetSystematic(masses, lifetimes)
    metSystematic.addExtraSamples(extraSamples)
    metSystematic.addChannel("central", "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2018/signalAcceptance_v3_metSyst")
    metSystematic.addChannel("up",      "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2018/signalAcceptance_v3_metSyst")
    metSystematic.addChannel("down",    "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2018/signalAcceptance_v3_metSyst")
    metSystematic.addMetTypes(metVaryTypes)
    metSystematic.setMetCut(120.0)
    metSystematic.setFoutNames(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__metVary", "2018_" + nLayersWord + ".txt")
    metSystematic.printSystematic()

    print "********************************************************************************"

    print "\n\n"

if (systematic == "JEC" or systematic == "ALL") and False:

    print "********************************************************************************"
    print "evaluating JEC systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jec_2018_" + nLayersWord + ".txt", "w")

    jecSystematic = SystematicCalculator(masses, lifetimes)
    jecSystematic.addFout(fout)
    jecSystematic.addExtraSamples(extraSamples)
    jecSystematic.addChannel("central", "disTrkSelectionSmearedJets"        + nLayersWord, suffix,  dirs['Brian'] + "2018/signalAcceptance_v3")
    jecSystematic.addChannel("down",    "disTrkSelectionSmearedJetsJECUp"   + nLayersWord, suffix,  dirs['Kai'] + "2018/signalAcceptance_v3_jecSyst")
    jecSystematic.addChannel("up",      "disTrkSelectionSmearedJetsJECDown" + nLayersWord, suffix,  dirs['Kai'] + "2018/signalAcceptance_v3_jecSyst")
    jecSystematic.printSystematic()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if (systematic == "JER" or systematic == "ALL") and False:

    print "********************************************************************************"
    print "evaluating JER systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jer_2018_" + nLayersWord + ".txt", "w")

    jerSystematic = SystematicCalculator(masses, lifetimes)
    jerSystematic.addFout(fout)
    jerSystematic.addExtraSamples(extraSamples)
    jerSystematic.addChannel("central",  "disTrkSelectionSmearedJets"     + nLayersWord, suffix,  dirs['Brian'] + "2018/signalAcceptance_full_v3")
    jerSystematic.addChannel("down",     "disTrkSelectionSmearedJetsUp"   + nLayersWord, suffix,  dirs['Kai'] + "2018/signalAcceptance_v3_jerSyst")
    jerSystematic.addChannel("up",       "disTrkSelectionSmearedJetsDown" + nLayersWord, suffix,  dirs['Kai'] + "2018/signalAcceptance_v3_jerSyst")
    jerSystematic.printSystematic()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__isr_2018_" + nLayersWord + ".txt", "w")

    isrSystematic = WeightSystematicFromTrees(masses, allLifetimes, lumi)
    isrSystematic.addFout(fout)
    isrSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2018/signalAcceptance_v3")
    isrSystematic.defineWeightToFluctuate('eventvariable_isrWeight')
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "TRIGGER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    for flux in ['Data', 'MC']:
        fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_grandOrWeight" + flux + '_2018_' + nLayersWord + ".txt", "w")

        triggerSystematic = WeightSystematicFromTrees(masses, allLifetimes, lumi)
        triggerSystematic.addFout(fout)
        triggerSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2018/signalAcceptance_v3")
        triggerSystematic.defineFluctuationUp  ('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Up')
        triggerSystematic.defineFluctuationDown('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Down')
        triggerSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if systematic == "ECALO" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ECalo systematic (2018)"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic = ECaloSystematic ()
    ecaloSystematic.addChannel  ("Data",  "ZtoMuMuDisTrkNLayers4NoECaloCut",  "SingleMu_2018",  dirs['Brian'] + "2018/fromLPC/ecaloSystematic")
    ecaloSystematic.addChannel  ("MC",    "ZtoMuMuDisTrkNLayers4NoECaloCut",  "DYJetsToLL_50",  dirs['Brian'] + "2018/fromLPC/ecaloSystematic")

    print "********************************************************************************"

    ecaloSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating hits systematic (2018)"
    print "--------------------------------------------------------------------------------"

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2018",  dirs['Brian'] + "2018/fromLPC/missingHitsCorrectionCorrected")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "AllMC",     dirs['Brian'] + "2018/fromLPC/missingHitsCorrectionCorrected")
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleVsInner")
    print "--------------------------------------------------------------------------------"
    print "before correction to missing middle hits"
    hitsSystematic.printSystematic ()
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleCorrectedVsInner")
    print "--------------------------------------------------------------------------------"
    print "after correction to missing middle hits"
    hitsSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if (systematic == "MISSING_OUTER_HITS" or systematic == "ALL") and False:

    print "********************************************************************************"
    print "evaluating missing outer hits systematic (2018)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__nMissOut_2018_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("nMissOutSystematic_2018_" + nLayersWord + ".root", "recreate")

    missingOuterHitsSystematic = MissingOuterHitsSystematic (masses, allLifetimes, lumi)
    missingOuterHitsSystematic.addFout (fout)
    missingOuterHitsSystematic.addFoutForPlot (foutForPlot)
    missingOuterHitsSystematic.addSignalSuffix ("_" + suffix)
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    missingOuterHitsSystematic.addChannel  ("Data",    "MuonCtrlSelection",                "MET_2018",     dirs['Brian'] + "2018/fromLPC/missingHitsCorrectionCorrected")
    missingOuterHitsSystematic.addChannel  ("MC",      "MuonCtrlSelection",                "AllMC",        dirs['Brian'] + "2018/fromLPC/missingHitsCorrectionCorrected")
    missingOuterHitsSystematic.addChannel  ("Signal",  "DisTrkNoNMissOut" + nLayersWord,   "",             dirs['Brian'] + "2018/signalAcceptance_v3_noNMissOutCut")
    missingOuterHitsSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()
    foutForPlot.Close ()

    print "\n\n"

if (systematic == "MUON_VETO_SCALE_FACTOR" or systematic == "ALL") and False:

    print "********************************************************************************"
    print "evaluating muon veto scale factor systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__muonVetoScaleFactor_2018_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("muonVetoScaleFactors_2018_" + nLayersWord + ".root", "recreate")

    muonVetoSFSystematic = LeptonVetoScaleFactorSystematic("Muon", masses, allLifetimes, lumi)
    muonVetoSFSystematic.addFout(fout)
    muonVetoSFSystematic.addFoutForPlot(foutForPlot)
    muonVetoSFSystematic.addChannel("Signal", "disTrkSelectionSmearedJetsLooseVetoes" + nLayersWord, "",               dirs['Brian'] + "2018/signalAcceptance_v3_looseVetoes")
    muonVetoSFSystematic.addChannel("Data",   "ZtoEleProbeTrkWithFilterLooseVetoes" + nLayersWord,   "SingleEle_2018", dirs['Brian'] + "2018/fromLPC/eleBkgdNoFilterBinnedLayers_looseVetoes")
    muonVetoSFSystematic.addSignalSuffix("_" + suffix)
    muonVetoSFSystematic.setPOGPayload(os.environ["CMSSW_BASE"] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root', 'muonID2018Loose')
    muonVetoSFSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if (systematic == "ELECTRON_VETO_SCALE_FACTOR" or systematic == "ALL") and False:

    print "********************************************************************************"
    print "evaluating electron veto scale factor systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__electronVetoScaleFactor_2018_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("electronVetoScaleFactors_2018_" + nLayersWord + ".root", "recreate")

    electronVetoSFSystematic = LeptonVetoScaleFactorSystematic("Electron", masses, allLifetimes, lumi)
    electronVetoSFSystematic.addFout(fout)
    electronVetoSFSystematic.addFoutForPlot(foutForPlot)
    electronVetoSFSystematic.addChannel("Signal", "disTrkSelectionSmearedJetsLooseVetoes" + nLayersWord, "",                 dirs['Brian'] + "2018/signalAcceptance_v3_looseVetoes")
    electronVetoSFSystematic.addChannel("Data",   "ZtoMuProbeTrkWithLooseFilter" + nLayersWord,          "SingleMu_2018", dirs['Brian'] + "2018/muonBackgroundNoFilterBinnedLayers_looseVetoes")
    electronVetoSFSystematic.addSignalSuffix("_" + suffix)
    electronVetoSFSystematic.setPOGPayload(os.environ["CMSSW_BASE"] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root', 'electronID2018Veto')
    electronVetoSFSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if (systematic == "TRIGGER_TURN_ON" or systematic == "ALL") and nLayersWord != 'NLayers6plus' and False:

    # first calculate the trigger turn-on curves for this category and NLayers6plus
    print "********************************************************************************"
    print "evaluating trigger turn-on curves (2018) " + nLayersWord
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

    foutForEfficienciesThisNLayers = TFile('triggerEfficiency_AMSB_chargino_' + nLayersWord + '.root', 'recreate')
    foutForEfficienciesNLayers6plus = TFile('triggerEfficiency_AMSB_chargino_NLayers6plus.root', 'recreate')

    for mass in masses:
        inputFile = 'AMSB_chargino_' + str(mass) + 'GeV_allLifetimes'

        grandOrEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandOrEfficiency.addTFile(foutForEfficienciesThisNLayers, nameSuffix = 'AMSB_' + str(mass) + 'GeV')
        grandOrEfficiency.addTCanvas(canvas)
        grandOrEfficiency.addChannel("Numerator",   "GrandOrNumeratorTrk4"   + nLayersWord, inputFile, dirs['Brian'] + '2018/grandOr_signal_full')
        grandOrEfficiency.addChannel("Denominator", "GrandOrDenominatorTrk" + nLayersWord, inputFile, dirs['Brian'] + '2018/grandOr_signal_full')
        grandOrEfficiency.setDatasetLabel(inputFile)
        grandOrEfficiency.setIsMC(True)
        grandOrEfficiency.plotEfficiency()

        grandOrEfficiencyNLayers6plus = TriggerEfficiency('GrandOr', [], 'METPath')
        grandOrEfficiencyNLayers6plus.addTFile(foutForEfficienciesNLayers6plus, nameSuffix = 'AMSB_' + str(mass) + 'GeV')
        grandOrEfficiencyNLayers6plus.addTCanvas(canvas)
        grandOrEfficiencyNLayers6plus.addChannel("Numerator",   "GrandOrNumeratorTrk4NLayers6plus",   inputFile, dirs['Brian'] + '2018/grandOr_signal_full')
        grandOrEfficiencyNLayers6plus.addChannel("Denominator", "GrandOrDenominatorTrkNLayers6plus", inputFile, dirs['Brian'] + '2018/grandOr_signal_full')
        grandOrEfficiencyNLayers6plus.setDatasetLabel(inputFile)
        grandOrEfficiencyNLayers6plus.setIsMC(True)
        grandOrEfficiencyNLayers6plus.plotEfficiency()

    # now calculate the systematic based on the difference between this category and NLayers6plus
    print "********************************************************************************"
    print "evaluating trigger turn-on systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__triggerTurnOn_2018_" + nLayersWord + ".txt", "w")

    foutForSystematics  = TFile('triggerTurnOnSystematic_2018_' + nLayersWord + '.root', 'recreate')

    turnOnSystematic = TriggerTurnOnSystematic(masses, allLifetimes, lumi)
    turnOnSystematic.addExtraSamples(extraSamples)
    turnOnSystematic.addFout(fout)
    turnOnSystematic.addSignalSuffix ("_" + suffix)
    turnOnSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2018/signalAcceptance_v3")
    turnOnSystematic.addEfficiencies("Denominator", "GrandOr_METPath_AMSB_XYZGeV", 'triggerEfficiency_AMSB_chargino_NLayers6plus.root')
    turnOnSystematic.addEfficiencies("Numerator",   "GrandOr_METPath_AMSB_XYZGeV", 'triggerEfficiency_AMSB_chargino_' + nLayersWord + '.root')
    turnOnSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if systematic == "HEM_15_16_WEIGHT" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating HEM 15/16 weight systematic (2018) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__HEM1516Weight_2018_" + nLayersWord + ".txt", "w")

    l1ECALPrefiringWeightSystematic = WeightSystematicFromTrees(masses, allLifetimes, lumi)
    l1ECALPrefiringWeightSystematic.addFout(fout)
    l1ECALPrefiringWeightSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2018/signalAcceptance_v3")
    l1ECALPrefiringWeightSystematic.defineFluctuationUp  ('eventvariable_hem1516weight', 'eventvariable_hem1516weightUp')
    l1ECALPrefiringWeightSystematic.defineFluctuationDown('eventvariable_hem1516weight', 'eventvariable_hem1516weightDown')
    l1ECALPrefiringWeightSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"
