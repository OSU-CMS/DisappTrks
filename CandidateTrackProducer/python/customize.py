import FWCore.ParameterSet.Config as cms

disappTrksOutputCommands = cms.untracked.vstring(
    "keep recoCaloMETs_*_*_*",
    "keep recoMETs_*_*_*",
    "keep recoPFMETs_pfChMet_*_*",
    "keep recoPFMETs_pfMet_*_*",
    "keep recoPFMETs_pfMetEI_*_*",
    "keep *_generalTracks_*_*",
    "keep CandidateTracks_*_*_*", 
    "keep *_reducedEcalRecHitsEE_*_*",
    "keep *_reducedEcalRecHitsEB_*_*",
    "keep *_reducedHcalRecHits_*_*",
    "keep *_dt4DSegments_*_*",
    "keep *_cscSegments_*_*",
)

def customizeMiniAODSIMOutput(process):

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
    process.MINIAODSIMoutput.outputCommands.extend (disappTrksOutputCommands)  

