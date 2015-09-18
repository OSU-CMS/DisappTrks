import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:myfile.root'
    )
)

process.myProducerLabel = cms.EDProducer('CandidateTrackProducer'
     , muons = cms.InputTag('muons')
     , electrons = cms.InputTag('pixelMatchGsfElectrons')
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
     , outputCommands = cms.untracked.vstring(
         'drop *',
         'keep *_muons_*_*',
         'keep *_pixelMatchGsfElectrons_*_*', 
         'keep *_*_*_OWNPARTICLES'
     )
)

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
