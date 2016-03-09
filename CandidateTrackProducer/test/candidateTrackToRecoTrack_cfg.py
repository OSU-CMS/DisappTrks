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
        'file:/mnt/hadoop/se/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/0000/miniAODWithCandidateTracks_613.root',
        'file:/mnt/hadoop/se/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/0000/miniAODWithCandidateTracks_614.root',
        'file:/mnt/hadoop/se/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/0000/miniAODWithCandidateTracks_615.root',
        'file:/mnt/hadoop/se/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/0000/miniAODWithCandidateTracks_616.root',
        'file:/mnt/hadoop/se/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/0000/miniAODWithCandidateTracks_617.root',
    ),
    eventsToProcess = cms.untracked.VEventRange ('1:14762:8535110'),
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

process.myEndPath = cms.EndPath (process.poolOutputModule)
