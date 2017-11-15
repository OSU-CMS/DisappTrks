import FWCore.ParameterSet.Config as cms
import sys

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('L1TINFOPRINTER')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.categories.append ("L1GlobalTriggerReadoutRecord")
process.MessageLogger.categories.append ("L1TriggerInfoPrinter")
process.MessageLogger.cerr.threshold = cms.untracked.string ("DEBUG")
process.MessageLogger.debugModules = cms.untracked.vstring ("*")

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "file:local2015_numEvent5.root",
    ),
)

###########################################################
##### Set up the global tag #####
###########################################################

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016SeptRepro_v6', '')

###########################################################
##### Set up the analyzer #####
###########################################################

process.L1TriggerInfoPrinter = cms.EDAnalyzer ("L1TriggerInfoPrinter",
    l1GtReadoutRecord = cms.InputTag ("gtDigis", ""),
)

process.myPath = cms.Path (process.L1TriggerInfoPrinter)
