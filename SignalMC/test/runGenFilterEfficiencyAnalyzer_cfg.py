import FWCore.ParameterSet.Config as cms

process = cms.Process("GenFilterEfficiency")

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:AMSB_chargino_test_GEN.root')
    fileNames = cms.untracked.vstring('file:AMSB_chargino_test_GEN_SIM.root')
)

process.dummy = cms.EDAnalyzer("GenFilterEfficiencyAnalyzer")

process.p = cms.Path(process.dummy)

