import FWCore.ParameterSet.Config as cms

process = cms.Process ('GLOBALCLUSTERS')

process.load ('FWCore.MessageService.MessageLogger_cfi')
process.load ('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load ('Configuration.EventContent.EventContent_cff')
process.load ('Configuration.StandardSequences.GeometryRecoDB_cff')

process.source = cms.Source ("PoolSource",
    bypassVersionCheck = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring ([
        "file:/home/bfrancis/public/pickevents_ttjetsDebug_justDisTrkNHits3.root",
    ]),
)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "80X_dataRun2_Prompt_v15", '')

process.siGlobalClusterProducer = cms.EDProducer ("SiGlobalClusterProducer",
    siPixelClusters = cms.InputTag ("siPixelClusters", ""),
)

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECODEBUG'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    fileName = cms.untracked.string('test.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)
process.FEVTDEBUGoutput.outputCommands.append ("keep *_*_*_GLOBALCLUSTERS")

process.myPath = cms.Path (process.siGlobalClusterProducer)

process.myEndPath = cms.EndPath (process.FEVTDEBUGoutput)
