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

gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
lifetimes = ['10', '100', '1000', '10000']
allLifetimes = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1',
               '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '20', '30', '40', '50', '60', '70', '80', '90', '100',
               '200', '300', '400', '500', '600', '700', '800', '900', '1000',
               '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
# masses = [700]
# lifetimes = ['1','10']
# allLifetimes = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1',
            #    '2', '3', '4', '5', '6', '7', '8', '9', '10']
suffix = "130X"

extraSamples = getExtraSamples(suffix, False, lifetimes)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

nLayersWord = "NLayers4"
if len(sys.argv) > 2:
    nLayersWord = sys.argv[2]

lumi = lumi["MET_2023C"]

if systematic == "PILEUP" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating pileup systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2023C_" + nLayersWord + ".txt", "w")

    pileupSystematic = WeightSystematicFromTrees(masses, lifetimes, lumi)
    pileupSystematic.addExtraSamples(extraSamples)
    pileupSystematic.addFout(fout)
    pileupSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    pileupSystematic.defineWeightToFluctuate('eventvariable_puScalingFactor')
    pileupSystematic.printSystematic ()

    print("********************************************************************************")

    fout.close ()

    print("\n\n")

if systematic == "MET" or systematic == "ALL":
    
    print("********************************************************************************")
    print("evaluating met systematics (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

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
    metSystematic.addChannel("central", "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    metSystematic.addChannel("up",      "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    metSystematic.addChannel("down",    "DisTrkNoMetSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    metSystematic.addMetTypes(metVaryTypes)
    metSystematic.setMetCut(120.0)
    metSystematic.setFoutNames(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__metVary", "2023C_" + nLayersWord + ".txt")
    metSystematic.printSystematic()

    print("********************************************************************************")

    print("\n\n")

if systematic == "JEC" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating JEC systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jec_2023C_" + nLayersWord + ".txt", "w")

    jecSystematic = SystematicCalculator(masses, lifetimes)
    jecSystematic.addFout(fout)
    jecSystematic.addExtraSamples(extraSamples)
    jecSystematic.addChannel("central", "disTrkSelectionSmearedJets"        + nLayersWord, suffix,  dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    jecSystematic.addChannel("down",    "disTrkSelectionSmearedJetsJECUp"   + nLayersWord, suffix,  dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    jecSystematic.addChannel("up",      "disTrkSelectionSmearedJetsJECDown" + nLayersWord, suffix,  dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    jecSystematic.printSystematic()

    print("********************************************************************************")

    fout.close ()

    print("\n\n")

if systematic == "JER" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating JER systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jer_2023C_" + nLayersWord + ".txt", "w")

    jerSystematic = SystematicCalculator(masses, lifetimes)
    jerSystematic.addFout(fout)
    jerSystematic.addExtraSamples(extraSamples)
    jerSystematic.addChannel("central",  "disTrkSelectionSmearedJets"     + nLayersWord, suffix,  dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    jerSystematic.addChannel("down",     "disTrkSelectionSmearedJetsUp"   + nLayersWord, suffix,  dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    jerSystematic.addChannel("up",       "disTrkSelectionSmearedJetsDown" + nLayersWord, suffix,  dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigJecJerNoMet_v2")
    jerSystematic.printSystematic()

    print("********************************************************************************")

    fout.close ()

    print("\n\n")

if systematic == "ISR" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating ISR systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__isr_2023C_" + nLayersWord + ".txt", "w")

    isrSystematic = WeightSystematicFromTrees(masses, lifetimes, lumi)
    isrSystematic.addExtraSamples(extraSamples)
    isrSystematic.addFout(fout)
    isrSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    isrSystematic.defineWeightToFluctuate('eventvariable_isrWeight')
    isrSystematic.printSystematic ()

    print("********************************************************************************")

    fout.close ()

    print("\n\n")

if systematic == "TRIGGER" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating trigger efficiency systematics (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    for flux in ['Data', 'MC']:
        fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_grandOrWeight" + flux + '_2023C_' + nLayersWord + ".txt", "w")

        triggerSystematic = WeightSystematicFromTrees(masses, lifetimes, lumi)
        triggerSystematic.addExtraSamples(extraSamples)
        triggerSystematic.addFout(fout)
        triggerSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
        triggerSystematic.defineFluctuationUp  ('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Up')
        triggerSystematic.defineFluctuationDown('eventvariable_grandOrWeight', 'eventvariable_grandOrWeight' + flux + 'Down')
        triggerSystematic.printSystematic()

    print("********************************************************************************\n\n")

    fout.close ()

    print("\n\n")

if systematic == "ECALO" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating ECalo systematic (2023C)")
    print("--------------------------------------------------------------------------------")

    ecaloSystematic = ECaloSystematic ()
    ecaloSystematic.addChannel  ("Data",  "ZtoMuMuDisTrkNLayers4NoECaloCut",  "hist_merged_Muon_2023C_ECaloMissHits",  dirs['Breno'] + "BGData/Run3/2023/MuonSigSyst")
    ecaloSystematic.addChannel  ("MC",    "ZtoMuMuDisTrkNLayers4NoECaloCut",  "hist_merged_DY_2023_ECaloMissHits",  dirs['Breno'] + "BGMC/Run3/2023/DYSigSyst")

    print("********************************************************************************")

    ecaloSystematic.printSystematic ()

    print("********************************************************************************")

    print("\n\n")

if systematic == "HITS" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating hits systematic (2023C)")
    print("--------------------------------------------------------------------------------")

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2023C",  dirs['Mike'] + "abyss/MET_run3/MET_2023C_MissingHitsSelection")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "MissingHits_2023C",     dirs['Mike'] + "abyss/MissingHitsCorrections/2023_preBpix")
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleVsInner")
    print("--------------------------------------------------------------------------------")
    print("before correction to missing middle hits")
    hitsSystematic.printSystematic ()
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleCorrectedVsInner")
    print("--------------------------------------------------------------------------------")
    print("after correction to missing middle hits")
    hitsSystematic.printSystematic ()

    print("********************************************************************************")

    print("\n\n")

# use the larger of HITS and HITS_V2 (EXO-19-010 ARC) # TODO: check this cut
if systematic == "HITS_V2" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating hits systematic V2 (2023C)")
    print("--------------------------------------------------------------------------------")

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel    ("Data",  "ZtoEETauHitsSystematicSelection"   + nLayersWord,  "hist_merged_EGamma_2023C_MissHits",  dirs['Breno'] + "BGData/Run3/2023/EGammaSigSyst")
    hitsSystematic.appendChannel ("Data",  "ZtoMuMuTauHitsSystematicSelection" + nLayersWord,  "hist_merged_Muon_2023C_ECaloMissHits",   dirs['Breno'] + "BGData/Run3/2023/MuonSigSyst")
    hitsSystematic.addChannel    ("MC",    "ZtoEETauHitsSystematicSelection"   + nLayersWord,  "hist_merged_DY_2023_ECaloMissHits",   dirs['Breno'] + "BGMC/Run3/2023/DYSigSyst")
    hitsSystematic.appendChannel ("MC",    "ZtoMuMuTauHitsSystematicSelection" + nLayersWord,  "hist_merged_DY_2023_ECaloMissHits",   dirs['Breno'] + "BGMC/Run3/2023/DYSigSyst")
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleVsInner")
    print("--------------------------------------------------------------------------------")
    print("before correction to missing middle hits")
    hitsSystematic.printSystematic ()
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleCorrectedVsInner")
    print("--------------------------------------------------------------------------------")
    print("after correction to missing middle hits")
    hitsSystematic.printSystematic ()

    print("********************************************************************************")

    print("\n\n")

if systematic == "MISSING_OUTER_HITS" or systematic == "ALL":

    print("********************************************************************************")
    print("evaluating missing outer hits systematic (2023C)")
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__nMissOut_2023C_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("nMissOutSystematic_2023C_" + nLayersWord + ".root", "recreate")

    missingOuterHitsSystematic = MissingOuterHitsSystematic (masses, allLifetimes, lumi)
    missingOuterHitsSystematic.addFout (fout)
    missingOuterHitsSystematic.addFoutForPlot (foutForPlot)
    missingOuterHitsSystematic.addSignalSuffix ("_" + suffix)
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    missingOuterHitsSystematic.addChannel  ("Data",    "MuonCtrlSelection",                "MET_2023C",  dirs['Mike'] + "abyss/MET_run3/MET_2023C_MissingHitsSelection")
    missingOuterHitsSystematic.addChannel  ("MC",      "MuonCtrlSelection",                "MissingHits_2023C",     dirs['Mike'] + "abyss/MissingHitsCorrections/2023_preBpix")
    missingOuterHitsSystematic.addChannel  ("Signal",  "DisTrkNoNMissOut" + nLayersWord,   "",             dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")

    missingOuterHitsSystematic.printSystematic ()

    print("********************************************************************************")

    fout.close ()
    foutForPlot.Close ()

    print("\n\n")

if systematic == "MUON_VETO_SCALE_FACTOR" or systematic == "ALL": # TODO: check this cut

    print("********************************************************************************")
    print("evaluating muon veto scale factor systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__muonVetoScaleFactor_2023C_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("muonVetoScaleFactors_2023C_" + nLayersWord + ".root", "recreate")

    muonVetoSFSystematic = LeptonVetoScaleFactorSystematic("Muon", masses, allLifetimes, lumi)
    muonVetoSFSystematic.addFout(fout)
    muonVetoSFSystematic.addFoutForPlot(foutForPlot)
    muonVetoSFSystematic.addChannel("Signal", "disTrkSelectionSmearedJetsLooseVetoes" + nLayersWord, "",               dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    muonVetoSFSystematic.addChannel("Data",   "ZtoEleProbeTrkWithLooseFilter"   + nLayersWord, "hist_merged_EGamma_2023C_LepVeto", dirs['Breno'] + "BGData/Run3/2023/EGammaSigSyst")
    muonVetoSFSystematic.addSignalSuffix("_" + suffix)
    muonVetoSFSystematic.setPOGPayload(os.environ["CMSSW_BASE"] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root', 'muonID2023CLoose')
    muonVetoSFSystematic.printSystematic()

    print("********************************************************************************\n\n")

    fout.close ()

    print("\n\n")

if systematic == "ELECTRON_VETO_SCALE_FACTOR" or systematic == "ALL": # TODO: check this cut

    print("********************************************************************************")
    print("evaluating electron veto scale factor systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__electronVetoScaleFactor_2023C_" + nLayersWord + ".txt", "w")
    foutForPlot = TFile.Open ("electronVetoScaleFactors_2023C_" + nLayersWord + ".root", "recreate")

    electronVetoSFSystematic = LeptonVetoScaleFactorSystematic("Electron", masses, allLifetimes, lumi)
    electronVetoSFSystematic.addFout(fout)
    electronVetoSFSystematic.addFoutForPlot(foutForPlot)
    electronVetoSFSystematic.addChannel("Signal", "disTrkSelectionSmearedJetsLooseVetoes" + nLayersWord, "",              dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    electronVetoSFSystematic.addChannel("Data",   "ZtoMuProbeTrkWithLooseFilter"          + nLayersWord, "hist_merged_Muon_2023C_LepVeto", dirs['Breno'] + "BGData/Run3/2023/MuonSigSyst")
    electronVetoSFSystematic.addSignalSuffix("_" + suffix)
    electronVetoSFSystematic.setPOGPayload(os.environ["CMSSW_BASE"] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root', 'electronID2023CVeto')
    electronVetoSFSystematic.printSystematic()

    print("********************************************************************************\n\n")

    fout.close ()

    print("\n\n")

if (systematic == "TRIGGER_TURN_ON" or systematic == "ALL") and nLayersWord != 'NLayers6plus':

    # first calculate the trigger turn-on curves for this category and NLayers6plus
    print("********************************************************************************")
    print("evaluating trigger turn-on curves (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

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

    foutForEfficienciesThisNLayers = TFile('triggerEfficiency_AMSB_chargino_' + nLayersWord + '_2023C.root', 'recreate')
    foutForEfficienciesNLayers6plus = TFile('triggerEfficiency_AMSB_chargino_NLayers6plus_2023C.root', 'recreate')

    for mass in masses:
        inputFile = 'AMSB_chargino_' + str(mass) + 'GeV_allLifetimes'

        grandOrEfficiency = TriggerEfficiency('GrandOr', [], 'METPath')
        grandOrEfficiency.addTFile(foutForEfficienciesThisNLayers, nameSuffix = 'AMSB_' + str(mass) + 'GeV')
        grandOrEfficiency.addTCanvas(canvas)
        grandOrEfficiency.addChannel("Numerator",   "GrandOrNumeratorTrk4"   + nLayersWord, inputFile, dirs['Breno'] + 'SignalMC/Run3/2023/signalAcceptance_sigTrigTurnOn_v2')
        grandOrEfficiency.addChannel("Denominator", "GrandOrDenominatorTrk" + nLayersWord, inputFile, dirs['Breno'] + 'SignalMC/Run3/2023/signalAcceptance_sigTrigTurnOn_v2')
        grandOrEfficiency.setDatasetLabel(inputFile)
        grandOrEfficiency.setIsMC(True)
        grandOrEfficiency.plotEfficiency()

        grandOrEfficiencyNLayers6plus = TriggerEfficiency('GrandOr', [], 'METPath')
        grandOrEfficiencyNLayers6plus.addTFile(foutForEfficienciesNLayers6plus, nameSuffix = 'AMSB_' + str(mass) + 'GeV')
        grandOrEfficiencyNLayers6plus.addTCanvas(canvas)
        grandOrEfficiencyNLayers6plus.addChannel("Numerator",   "GrandOrNumeratorTrk4NLayers6plus",   inputFile, dirs['Breno'] + 'SignalMC/Run3/2023/signalAcceptance_sigTrigTurnOn_v2')
        grandOrEfficiencyNLayers6plus.addChannel("Denominator", "GrandOrDenominatorTrkNLayers6plus", inputFile, dirs['Breno'] + 'SignalMC/Run3/2023/signalAcceptance_sigTrigTurnOn_v2')
        grandOrEfficiencyNLayers6plus.setDatasetLabel(inputFile)
        grandOrEfficiencyNLayers6plus.setIsMC(True)
        grandOrEfficiencyNLayers6plus.plotEfficiency()

    # now calculate the systematic based on the difference between this category and NLayers6plus
    print("********************************************************************************")
    print("evaluating trigger turn-on systematic (2023C) " + nLayersWord)
    print("--------------------------------------------------------------------------------")

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__triggerTurnOn_2023C_" + nLayersWord + ".txt", "w")

    foutForSystematics  = TFile('triggerTurnOnSystematic_2023C_' + nLayersWord + '.root', 'recreate')

    turnOnSystematic = TriggerTurnOnSystematic(masses, lifetimes, lumi)
    turnOnSystematic.addExtraSamples(extraSamples)
    turnOnSystematic.addFout(fout)
    turnOnSystematic.addSignalSuffix ("_" + suffix)
    turnOnSystematic.addChannel("central", "disTrkSelectionSmearedJets" + nLayersWord, suffix, dirs['Breno'] + "SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2")
    turnOnSystematic.addEfficiencies("Denominator", "GrandOr_METPath_AMSB_XYZGeV", 'triggerEfficiency_AMSB_chargino_NLayers6plus_2023C.root')
    turnOnSystematic.addEfficiencies("Numerator",   "GrandOr_METPath_AMSB_XYZGeV", 'triggerEfficiency_AMSB_chargino_' + nLayersWord + '_2023C.root')
    turnOnSystematic.printSystematic()

    print("********************************************************************************\n\n")

    fout.close ()

    print("\n\n")
