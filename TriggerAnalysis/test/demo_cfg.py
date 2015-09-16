import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('Demo')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring ('/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4.root')
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.demo = cms.EDAnalyzer ("MiniAODTriggerAnalyzer",
  bits = cms.InputTag("TriggerResults","","HLT"),
  prescales = cms.InputTag("patTrigger"),
  objects = cms.InputTag("selectedPatTrigger"),
)

process.p = cms.Path (process.demo)
