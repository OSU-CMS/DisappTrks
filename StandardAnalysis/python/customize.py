import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.Triggers import *
from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.BackgroundEstimation.EventMETTriggerProducer_cfi import customizeForMETTriggerProducer
from DisappTrks.BackgroundEstimation.EventL1ETMProducer_cfi import customizeForL1ETMProducer
import os

def customize (process,
               runPeriod,
               applyPUReweighting = True,
               applyISRReweighting = True,
               applyTriggerReweighting = True,
               applyMissingHitsCorrections = True,
               runMETFilters = True,
               runEcalBadCalibFilters = True):

    if osusub.batchMode and (osusub.datasetLabel in types) and types[osusub.datasetLabel] != "signalMC":
        applyISRReweighting = False

    if runPeriod == "2015":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2015")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2015Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2015Down")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2015D')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2015D')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2015_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2015_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)

        setMissingHitsCorrection (process, "2015")

    elif runPeriod == "2016BC":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_BC")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_BCUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_BCDown")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016BC')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016BC")

        if hasattr (process, "prefiringweight"):
            process.prefiringweight.DataEra = cms.string("2016BtoH")
            process.L1PrefiringWeightProducer.DataEra = cms.string("2016BtoH")

    elif runPeriod == "2016DEFGH":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_DEFGH")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_DEFGHUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_DEFGHDown")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFGH')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016DEFGH")

        if hasattr (process, "prefiringweight"):
            process.prefiringweight.DataEra = cms.string("2016BtoH")
            process.L1PrefiringWeightProducer.DataEra = cms.string("2016BtoH")

    elif runPeriod == "2017":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2017")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2017Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2017Down")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia8_94X', 'SingleMu_2017')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2017')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu_94X')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2017_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2017_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)
        setUseEraByEraFiducialMaps (process, True)

        setMissingHitsCorrection (process, "2017")

        if hasattr (process, "prefiringweight"):
            process.prefiringweight.DataEra = cms.string("2017BtoF")
            process.L1PrefiringWeightProducer.DataEra = cms.string("2017BtoF")

    # fixme, all set to 2017 values
    elif runPeriod == "2018":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2018")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2018Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2018Down")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia8_94X', 'SingleMu_2018') # fixme
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2018')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu_102X')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        # fixme incomplete
        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2018_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2018_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)
        setUseEraByEraFiducialMaps (process, True)

        setMissingHitsCorrection (process, "2017") # fixme

    if not applyPUReweighting:
        process.PUScalingFactorProducer.PU     = cms.string ("")
        process.PUScalingFactorProducer.target = cms.string ("")
        process.PUScalingFactorProducer.targetUp = cms.string ("")
        process.PUScalingFactorProducer.targetDown = cms.string ("")

    if not applyISRReweighting:
        process.ISRWeightProducer.weightFile = cms.string("")
        process.ISRWeightProducer.weightHist = cms.vstring()

    if not applyTriggerReweighting:
        process.TriggerWeightProducer.efficiencyFile  =  cms.string  ("")
        process.TriggerWeightProducer.dataset         =  cms.string  ("")
        process.TriggerWeightProducer.target          =  cms.string  ("")
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(False)

    if not applyMissingHitsCorrections:
        setMissingHitsCorrection (process, "uncorrected")

    for channel in getListOfChannels (process):
        moveVariableProducer (process, "TriggerWeightProducer", channel)

        doFilter    = ("WithFilter" in channel)
        doLooseFilter    = ("WithLooseFilter" in channel)
        doSSFilter  = ("WithSSFilter" in channel)
        doLooseSSFilter  = ("WithLooseSSFilter" in channel)
        doJetFilter = ("WithJetFilter" in channel)

        if hasattr (process, "EventElectronTPProducer"):
            getattr (process, "EventElectronTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventElectronTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventElectronTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventElectronTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventElectronTPProducer").doJetFilter = cms.bool (doJetFilter)
            moveVariableProducer (process, "EventElectronTPProducer", channel)
        if hasattr (process, "EventMuonTPProducer"):
            getattr (process, "EventMuonTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventMuonTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventMuonTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventMuonTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventMuonTPProducer").doJetFilter = cms.bool (doJetFilter)
            moveVariableProducer (process, "EventMuonTPProducer", channel)
        if hasattr (process, "EventTauToElectronTPProducer"):
            getattr (process, "EventTauToElectronTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventTauToElectronTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventTauToElectronTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventTauToElectronTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventTauToElectronTPProducer").doJetFilter = cms.bool (doJetFilter)
            moveVariableProducer (process, "EventTauToElectronTPProducer", channel)
        if hasattr (process, "EventTauToMuonTPProducer"):
            getattr (process, "EventTauToMuonTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventTauToMuonTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventTauToMuonTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventTauToMuonTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventTauToMuonTPProducer").doJetFilter = cms.bool (doJetFilter)
            moveVariableProducer (process, "EventTauToMuonTPProducer", channel)

        if hasattr (process, "EventElectronMETTriggerProducer"):
            customizeForMETTriggerProducer (getattr (process, "EventElectronMETTriggerProducer"))
            moveVariableProducer (process, "EventElectronMETTriggerProducer", channel)
        if hasattr (process, "EventMuonMETTriggerProducer"):
            customizeForMETTriggerProducer (getattr (process, "EventMuonMETTriggerProducer"))
            moveVariableProducer (process, "EventMuonMETTriggerProducer", channel)
        if hasattr (process, "EventTauMETTriggerProducer"):
            customizeForMETTriggerProducer (getattr (process, "EventTauMETTriggerProducer"))
            moveVariableProducer (process, "EventTauMETTriggerProducer", channel)

        if hasattr (process, "EventElectronL1ETMProducer"):
            customizeForL1ETMProducer (getattr (process, "EventElectronL1ETMProducer"))
            moveVariableProducer (process, "EventElectronL1ETMProducer", channel)
        if hasattr (process, "EventMuonL1ETMProducer"):
            customizeForL1ETMProducer (getattr (process, "EventMuonL1ETMProducer"))
            moveVariableProducer (process, "EventMuonL1ETMProducer", channel)
        if hasattr (process, "EventTauL1ETMProducer"):
            customizeForL1ETMProducer (getattr (process, "EventTauL1ETMProducer"))
            moveVariableProducer (process, "EventTauL1ETMProducer", channel)

        moveArbitrationToEnd (process, channel)

    if runMETFilters:
        process.schedule.insert (0, process.metFilterPath)

    if runEcalBadCalibFilters:
        process.schedule.insert (0, process.passecalBadCalibFilterUpdatePath)

    if hasattr (process, "EventJetVarProducer") and not hasattr (process.EventJetVarProducer, "triggerNames"):
        process.EventJetVarProducer.triggerNames = cms.vstring ()

    return process
