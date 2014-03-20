import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.source = cms.Source ('PoolSource',
    fileNames = cms.untracked.vstring (
#        'file:AMSB_chargino_GEN.root', 
#        'file:AMSB_chargino_GEN_SIM_RECO.root',
        'file:TestMuonDecay_GEN.root', 
    )
)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.particleListDrawer = cms.EDAnalyzer ('ParticleListDrawer',
    maxEventsToPrint = cms.untracked.int32(-1),
    printVertex = cms.untracked.bool(True),
    src = cms.InputTag("genParticles")
)

process.myPath = cms.Path (process.particleListDrawer)
