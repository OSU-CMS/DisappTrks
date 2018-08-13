import FWCore.ParameterSet.Config as cms
import sys

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('CUTFLOW')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (
        "cutFlow.root",
    )
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
      '/store/user/bfrancis/SingleElectron/Run2017B-31Mar2018-v1-DisappTrks-v2/180806_191508/0000/REMINIAOD_PAT_1.root',
    )
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.CutFlowAnalyzer = cms.EDAnalyzer("CutResultsAnalyzer",
  skimName = cms.InputTag("electronSkimFilter"),
)
process.myPath = cms.Path(process.CutFlowAnalyzer)
