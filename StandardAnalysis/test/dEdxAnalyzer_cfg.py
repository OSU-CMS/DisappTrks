import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('ANA2')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "file:/data/users/hart/pickevents_data.root",
    ),
)
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('dEdx.root')
)

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.dEdxAnalyzer = cms.EDAnalyzer ("DEdxAnalyzer",
    tracks = cms.InputTag ("generalTracks", ""),
    dEdx = cms.InputTag ("dedxHarmonic2", ""),
)

process.myPath = cms.Path (process.dEdxAnalyzer)
