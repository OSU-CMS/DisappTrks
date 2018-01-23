import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.BackgroundEstimation.EventMETTriggerProducer_cfi import customizeForMETTriggerProducer
from DisappTrks.BackgroundEstimation.EventL1ETMProducer_cfi import customizeForL1ETMProducer
import os

def customize (process, runPeriod, applyPUReweighting = True, applyISRReweighting = True, applyTriggerReweighting = True, applyMissingHitsCorrections = True, runMETFilters = True):

    if runPeriod == "2015":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2015")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2015Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2015Down")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2015D')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2015D')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2015_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2015_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2015")

    elif runPeriod == "2016BC":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_BC")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_BCUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_BCDown")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016BC')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016BC")

    elif runPeriod == "2016DEFGH":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_DEFGH")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_DEFGHUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_DEFGHDown")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFGH')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016DEFGH")

    # fixme
    elif runPeriod == "2017":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_DEFGH")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_DEFGHUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_DEFGHDown")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFGH')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016DEFGH")

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

        doFilter = False
        doSSFilter = False
        if channel.endswith ("WithFilter"):
            doFilter = True
        if channel.endswith ("WithSSFilter"):
            doSSFilter = True

        if hasattr (process, "EventElectronTPProducer"):
            getattr (process, "EventElectronTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventElectronTPProducer").doSSFilter = cms.bool (doSSFilter)
            moveVariableProducer (process, "EventElectronTPProducer", channel)
        if hasattr (process, "EventMuonTPProducer"):
            getattr (process, "EventMuonTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventMuonTPProducer").doSSFilter = cms.bool (doSSFilter)
            moveVariableProducer (process, "EventMuonTPProducer", channel)
        if hasattr (process, "EventTauToElectronTPProducer"):
            getattr (process, "EventTauToElectronTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventTauToElectronTPProducer").doSSFilter = cms.bool (doSSFilter)
            moveVariableProducer (process, "EventTauToElectronTPProducer", channel)
        if hasattr (process, "EventTauToMuonTPProducer"):
            getattr (process, "EventTauToMuonTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventTauToMuonTPProducer").doSSFilter = cms.bool (doSSFilter)
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

    if runMETFilters:
        process.schedule.insert (0, process.metFilterPath)

    if hasattr (process, "EventJetVarProducer") and not hasattr (process.EventJetVarProducer, "triggerNames"):
        process.EventJetVarProducer.triggerNames = cms.vstring ()

    return process
