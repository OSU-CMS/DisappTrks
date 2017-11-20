import FWCore.ParameterSet.Config as cms
import sys, os

globalTag = '76X_dataRun2_v15'
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    globalTag = '80X_dataRun2_2016SeptRepro_v6'
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    globalTag = '92X_dataRun2_Prompt_v8'

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('L1TINFOPRINTER')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append ("L1GlobalTriggerReadoutRecord")
process.MessageLogger.categories.append ("L1TriggerInfoPrinter")
process.MessageLogger.cerr.threshold = cms.untracked.string ("DEBUG")
process.MessageLogger.debugModules = cms.untracked.vstring ("*")

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "file:pickevents.root",
    ),
)

###########################################################
##### Set up the global tag #####
###########################################################

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globalTag, '')

###########################################################
##### Set up the analyzer #####
###########################################################

process.L1TriggerInfoPrinter = cms.EDAnalyzer ("L1TriggerInfoPrinter",
    l1GtReadoutRecord = cms.InputTag ("gtDigis", ""),
)

process.myPath = cms.Path (process.L1TriggerInfoPrinter)
