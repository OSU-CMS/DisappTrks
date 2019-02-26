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
        "file:/data/users/hart/weirdData/weirdMuons.root",
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
    electrons = cms.InputTag ("gedGsfElectrons", ""),
    muons = cms.InputTag ("muons", ""),
    dEdxPixel = cms.InputTag ("dedxPixelHarmonic2", ""),
    dEdxStrip = cms.InputTag ("dedxHarmonic2", ""),
    minPt = cms.double (55.0),
    requiredNumLayers = cms.int32 (-1),
    vetoElectronsOrMuons = cms.string ("both")
)

process.myPath = cms.Path (process.dEdxAnalyzer)
