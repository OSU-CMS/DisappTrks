# Modeled from:
# https://twiki.cern.ch/twiki/pub/CMSPublic/WorkBookEDMTutorialProducer/trackandpointsproducer_332_cfg.py.txt 
# in: 
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookEDMTutorialProducer

import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:/data/users/wulsin/condor/signalMCGenV3/AMSB_chargino_200GeV_ctau100cm_FilterSumPt50_RECO/AMSB_chargino_RECO_0.root',
    )
)

process.genParticlePlusGEANT = cms.EDProducer("GenPlusSimParticleProducer",
                                              src           = cms.InputTag("g4SimHits"),   # use "famosSimHits" for FAMOS
                                              setStatus     = cms.int32(8),                # set status = 8 for GEANT GPs
                                              filter        = cms.vstring("pt > 0.0"),     # just for testing (optional)
                                              genParticles  = cms.InputTag("genParticles") # original genParticle list
                                              )


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
    ,outputCommands = cms.untracked.vstring(
    'drop *',   # Remove the 'drop *' command if you want to keep all collections
    "keep *_genParticles_*_*",
    "keep *_generalTracks_*_*",
    "keep *_genParticlePlusGEANT_*_*" 
    )                              
                               )
  
process.p = cms.Path(process.genParticlePlusGEANT)  

process.e = cms.EndPath(process.out)


