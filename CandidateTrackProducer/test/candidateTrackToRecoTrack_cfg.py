import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('ANA')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "file:/home/hart/rereco/CMSSW_7_6_6/src/singleElectron.root",
        "file:/home/hart/rereco/CMSSW_7_6_6/src/singleMuon.root",
    ),
#    eventsToProcess = cms.untracked.VEventRange ('1:14762:8535110'),
)

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.candidateTrackToRecoTrack = cms.EDProducer ("CandidateTrackToRecoTrack",
    tracks = cms.InputTag ("candidateTrackProducer", "")
)

process.myPath = cms.Path (process.candidateTrackToRecoTrack)

process.load('Configuration.EventContent.EventContent_cff')
process.poolOutputModule = cms.OutputModule ("PoolOutputModule",
    splitLevel = cms.untracked.int32 (0),
    eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
    SelectEvents = cms.untracked.PSet (),
    dropMetaData = cms.untracked.string ("ALL"),
    fileName = cms.untracked.string ("skim.root"),
    outputCommands = process.MINIAODEventContent.outputCommands,
)
process.poolOutputModule.outputCommands.append ("keep recoTracks*_*_*_*")
process.poolOutputModule.outputCommands.append ("keep recoGsfTracks*_*_*_*")

process.myEndPath = cms.EndPath (process.poolOutputModule)
