import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.source = cms.Source ('PoolSource',
    fileNames = cms.untracked.vstring (
        "file:/data/users/hart/condor/signalMC/2016/AMSB_chargino_M-700_CTau-100_TuneZ2star_13TeV_pythia6_step4/hist_0.root",
    )
)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10)
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.particleListDrawer = cms.EDAnalyzer ('ParticleListDrawer',
    maxEventsToPrint = cms.untracked.int32(-1),
    printOnlyHardInteraction = cms.untracked.bool(False),
    printVertex = cms.untracked.bool(True),
    printFlags = cms.untracked.bool(False),
    useMessageLogger = cms.untracked.bool(False),
    src = cms.InputTag("genParticles")
#    src = cms.InputTag("genParticlePlusGeant")
#    src = cms.InputTag("prunedGenParticles")
#    src = cms.InputTag("prunedGenParticlePlusGeant")
#    src = cms.InputTag("packedGenParticles")
#    src = cms.InputTag("packedGenParticlePlusGeant")
)

process.myPath = cms.Path (process.particleListDrawer)
