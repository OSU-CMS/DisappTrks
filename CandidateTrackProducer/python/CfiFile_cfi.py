import FWCore.ParameterSet.Config as cms

demo = cms.EDProducer('CandidateTrackProducer'
     , muons = cms.InputTag('muons')
     , electrons = cms.InputTag('pixelMatchGsfElectrons')
)
