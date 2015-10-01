import FWCore.ParameterSet.Config as cms
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('DISAPPTRKS')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
      "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_0.root"
    )
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.candidateDisappearingTracks = cms.EDProducer ("CandidateTrackProducer",
  tracks = cms.InputTag ("generalTracks", ""),
)

process.myPath = cms.Path (process.candidateDisappearingTracks)

process.load('Configuration.EventContent.EventContent_cff')
process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string("miniAODWithCandidateTracks.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
)
process.MINIAODSIMoutput.outputCommands.append ("keep *_candidateDisappearingTracks_*_*")

process.myEndPath = cms.EndPath (process.MINIAODSIMoutput)
