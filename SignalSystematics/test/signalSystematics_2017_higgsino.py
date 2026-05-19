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

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_pileup_2017_" + nLayersWord + ".txt", "w")

    pileupSystematic = WeightSystematicFromTrees(masses, lifetimes, lumi, isHiggsino = True)
    pileupSystematic.addExtraSamples(extraSamples)
    pileupSystematic.addFout(fout)
    pileupSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_higgsino")
    pileupSystematic.defineWeightToFluctuate('eventvariable_puScalingFactor')
    pileupSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "MET" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating met systematics (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    metVaryTypes = [
        'JetRes',
        'JetEn',
        'ElectronEn',
        'TauEn',
        'UnclusteredEn',
        'PhotonEn',
    ]

    metSystematic = MetSystematic(masses, lifetimes, isHiggsino = True)
    metSystematic.addExtraSamples(extraSamples)
    metSystematic.addChannel("central", "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2017/signalAcceptance_higgsino_metSyst")
    metSystematic.addChannel("up",      "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2017/signalAcceptance_higgsino_metSyst")
    metSystematic.addChannel("down",    "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Brian']+"2017/signalAcceptance_higgsino_metSyst")
    metSystematic.addMetTypes(metVaryTypes)
    metSystematic.setMetCut(120.0)
    metSystematic.setFoutNames(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_metVary", "2017_" + nLayersWord + ".txt")
    metSystematic.printSystematic()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_jec_2017_" + nLayersWord + ".txt", "w")

    jecSystematic = SystematicCalculator(masses, lifetimes, isHiggsino = True)
    jecSystematic.addFout(fout)
    jecSystematic.addExtraSamples(extraSamples)
    jecSystematic.addChannel("central", "disTrkSelectionSmearedJets"        + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_higgsino")
    jecSystematic.addChannel("down",    "disTrkSelectionSmearedJetsJECUp"   + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_higgsino_jecSyst")
    jecSystematic.addChannel("up",      "disTrkSelectionSmearedJetsJECDown" + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_higgsino_jecSyst")
    jecSystematic.printSystematic()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "JER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JER systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_jer_2017_" + nLayersWord + ".txt", "w")

    jerSystematic = SystematicCalculator(masses, lifetimes, isHiggsino = True)
    jerSystematic.addFout(fout)
    jerSystematic.addExtraSamples(extraSamples)
    jerSystematic.addChannel("central",  "disTrkSelectionSmearedJets"     + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_higgsino")
    jerSystematic.addChannel("down",     "disTrkSelectionSmearedJetsUp"   + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_higgsino_jerSyst")
    jerSystematic.addChannel("up",       "disTrkSelectionSmearedJetsDown" + nLayersWord, suffix,  dirs['Brian'] + "2017/signalAcceptance_higgsino_jerSyst")
    jerSystematic.printSystematic()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_isr_2017_" + nLayersWord + ".txt", "w")

    isrSystematic = WeightSystematicFromTrees(masses, lifetimes, lumi, isHiggsino = True)
    isrSystematic.addExtraSamples(extraSamples)
    isrSystematic.addFout(fout)
    isrSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_higgsino")
    isrSystematic.defineWeightToFluctuate('eventvariable_isrWeight')
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "TRIGGER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    for flux in ['Data', 'MC']:
        fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_trigger_grandOrWeight" + flux + '_2017_' + nLayersWord + ".txt", "w")

        triggerSystematic = WeightSystematicFromTrees(masses, lifetimes, lumi, isHiggsino = True)
        triggerSystematic.addExtraSamples(extraSamples)
        triggerSystematic.addFout(fout)
        triggerSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_higgsino")
        triggerSystematic.defineFluctuationUp  ('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Up')
        triggerSystematic.defineFluctuationDown('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Down')
        triggerSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if systematic == "MISSING_OUTER_HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating missing outer hits systematic (2017)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_nMissOut_2017_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("nMissOutSystematic_2017_" + nLayersWord + ".root", "recreate")

    missingOuterHitsSystematic = MissingOuterHitsSystematic (masses, allLifetimes, lumi, isHiggsino = True)
    missingOuterHitsSystematic.addFout (fout)
    missingOuterHitsSystematic.addFoutForPlot (foutForPlot)
    missingOuterHitsSystematic.addSignalSuffix ("_" + suffix)
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    missingOuterHitsSystematic.addChannel  ("Data",    "MuonCtrlSelection",                "MET_2017",     dirs['Brian'] + "2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
    missingOuterHitsSystematic.addChannel  ("MC",      "MuonCtrlSelection",                "AllMC_scaled", dirs['Brian'] + "2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
    missingOuterHitsSystematic.addChannel  ("Signal",  "DisTrkNoNMissOut" + nLayersWord,   "",             dirs['Brian'] + "2017/signalAcceptance_higgsino_noNMissOutCut")
    missingOuterHitsSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()
    foutForPlot.Close ()

    print "\n\n"

if systematic == "L1_ECAL_PREFIRING_WEIGHT" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating L1 ECAL prefiring weight systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_L1ECALPrefiringWeight_2017_" + nLayersWord + ".txt", "w")

    l1ECALPrefiringWeightSystematic = WeightSystematicFromTrees(masses, allLifetimes, lumi, isHiggsino = True)
    l1ECALPrefiringWeightSystematic.addFout(fout)
    l1ECALPrefiringWeightSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Brian'] + "2017/signalAcceptance_higgsino")
    l1ECALPrefiringWeightSystematic.defineFluctuationUp  ('eventvariable_L1ECALPrefiringWeight', 'eventvariable_L1ECALPrefiringWeightUp')
    l1ECALPrefiringWeightSystematic.defineFluctuationDown('eventvariable_L1ECALPrefiringWeight', 'eventvariable_L1ECALPrefiringWeightDown')
    l1ECALPrefiringWeightSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if systematic == "MUON_VETO_SCALE_FACTOR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating muon veto scale factor systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_muonVetoScaleFactor_2017_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("muonVetoScaleFactors_2017_" + nLayersWord + ".root", "recreate")

    muonVetoSFSystematic = LeptonVetoScaleFactorSystematic("Muon", masses, allLifetimes, lumi, isHiggsino = True)
    muonVetoSFSystematic.addFout(fout)
    muonVetoSFSystematic.addFoutForPlot(foutForPlot)
    muonVetoSFSystematic.addChannel("Signal", "disTrkSelectionSmearedJetsLooseVetoes" + nLayersWord, "",               dirs['Brian'] + "2017/signalAcceptance_higgsino_looseVetoes")
    muonVetoSFSystematic.addChannel("Data",   "ZtoEleProbeTrkWithFilterLooseVetoes" + nLayersWord,   "SingleEle_2017", dirs['Brian'] + "2017/fromLPC/eleBkgdNoFilterBinnedLayers_looseVetoes")
    muonVetoSFSystematic.addSignalSuffix("_" + suffix)
    muonVetoSFSystematic.setPOGPayload(os.environ["CMSSW_BASE"] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root', 'muonID2017Loose')
    muonVetoSFSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

if systematic == "ELECTRON_VETO_SCALE_FACTOR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating electron veto scale factor systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_electronVetoScaleFactor_2017_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("electronVetoScaleFactors_2017_" + nLayersWord + ".root", "recreate")

    electronVetoSFSystematic = LeptonVetoScaleFactorSystematic("Electron", masses, allLifetimes, lumi, isHiggsino = True)
    electronVetoSFSystematic.addFout(fout)
    electronVetoSFSystematic.addFoutForPlot(foutForPlot)
    electronVetoSFSystematic.addChannel("Signal", "disTrkSelectionSmearedJetsLooseVetoes" + nLayersWord, "",                 dirs['Brian'] + "2017/signalAcceptance_higgsino_looseVetoes")
    electronVetoSFSystematic.addChannel("Data",   "ZtoMuProbeTrkWithLooseFilter" + nLayersWord,          "SingleMu_2017", dirs['Brian'] + "2017/muonBackgroundNoFilterBinnedLayers_looseVetoes")
    electronVetoSFSystematic.addSignalSuffix("_" + suffix)
    electronVetoSFSystematic.setPOGPayload(os.environ["CMSSW_BASE"] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root', 'electronID2017Veto')
    electronVetoSFSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"

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

    #for mass in masses:
    #    inputFile = 'Higgsino_' + str(mass) + 'GeV_allLifetimes'

    #    grandOrEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
    #    grandOrEfficiency.addTFile(foutForEfficienciesThisNLayers, nameSuffix = 'Higgsino_' + str(mass) + 'GeV')
    #    grandOrEfficiency.addTCanvas(canvas)
    #    grandOrEfficiency.addChannel("Numerator",   "GrandOrNumeratorTrk4"   + nLayersWord, inputFile, dirs['Brian'] + '2017/grandOr_signal_higgsino')
    #    grandOrEfficiency.addChannel("Denominator", "GrandOrDenominatorTrk" + nLayersWord, inputFile, dirs['Brian'] + '2017/grandOr_signal_higgsino')
    #    grandOrEfficiency.setDatasetLabel(inputFile)
    #    grandOrEfficiency.setIsMC(True)
    #    grandOrEfficiency.plotEfficiency()

    #    grandOrEfficiencyNLayers6plus = TriggerEfficiency('GrandOr', [], 'METPath')
    #    grandOrEfficiencyNLayers6plus.addTFile(foutForEfficienciesNLayers6plus, nameSuffix = 'Higgsino_' + str(mass) + 'GeV')
    #    grandOrEfficiencyNLayers6plus.addTCanvas(canvas)
    #    grandOrEfficiencyNLayers6plus.addChannel("Numerator",   "GrandOrNumeratorTrk4NLayers6plus",   inputFile, dirs['Brian'] + '2017/grandOr_signal_higgsino')
    #    grandOrEfficiencyNLayers6plus.addChannel("Denominator", "GrandOrDenominatorTrkNLayers6plus", inputFile, dirs['Brian'] + '2017/grandOr_signal_higgsino')
    #    grandOrEfficiencyNLayers6plus.setDatasetLabel(inputFile)
    #    grandOrEfficiencyNLayers6plus.setIsMC(True)
    #    grandOrEfficiencyNLayers6plus.plotEfficiency()

    # now calculate the systematic based on the difference between this category and NLayers6plus
    print "********************************************************************************"
    print "evaluating trigger turn-on systematic (2017) " + nLayersWord
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__higgsino_triggerTurnOn_2017_" + nLayersWord + ".txt", "w")

    foutForSystematics  = TFile('triggerTurnOnSystematic_2017_higgsino_' + nLayersWord + '.root', 'recreate')

    turnOnSystematic = TriggerTurnOnSystematic(masses, lifetimes, lumi, isHiggsino = True)
    turnOnSystematic.addExtraSamples(extraSamples)
    turnOnSystematic.addFout(fout)
    turnOnSystematic.addLumis({"central":35864.601, "central1":4822.568, "central2":868.626})
    turnOnSystematic.addSignalSuffix ("_" + suffix)
    turnOnSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Kai'] + "2017/signalAcceptance_full_higgsino")
    turnOnSystematic.addEfficiencies("Denominator", "GrandOr_METPath_Higgsino_XYZGeV", 'triggerEfficiency_Higgsino_NLayers6plus.root')
    turnOnSystematic.addEfficiencies("Numerator",   "GrandOr_METPath_Higgsino_XYZGeV", 'triggerEfficiency_Higgsino_' + nLayersWord + '.root')
    turnOnSystematic.addChannel("central1", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Kai'] + "2017/signalAcceptance_full_higgsino_verA")
    turnOnSystematic.addEfficiencies("Denominator1", "GrandOr_METPath_Higgsino_XYZGeV", 'triggerEfficiency_Higgsino_NLayers6plus.root')
    turnOnSystematic.addEfficiencies("Numerator1",   "GrandOr_METPath_Higgsino_XYZGeV", 'triggerEfficiency_Higgsino_' + nLayersWord + '.root')
    turnOnSystematic.addChannel("central2", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Kai'] + "2017/signalAcceptance_full_higgsino_verB")
    turnOnSystematic.addEfficiencies("Denominator2", "GrandOr_METPath_Higgsino_XYZGeV", 'triggerEfficiency_Higgsino_NLayers6plus.root')
    turnOnSystematic.addEfficiencies("Numerator2",   "GrandOr_METPath_Higgsino_XYZGeV", 'triggerEfficiency_Higgsino_' + nLayersWord + '.root')
    turnOnSystematic.printSystematic()

    print "********************************************************************************\n\n"

    fout.close ()

    print "\n\n"
