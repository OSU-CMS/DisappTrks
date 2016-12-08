# Modeled from:
# https://twiki.cern.ch/twiki/pub/CMSPublic/WorkBookEDMTutorialProducer/trackandpointsproducer_332_cfg.py.txt
# in:
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookEDMTutorialProducer

import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:/data/users/wulsin/condor/signalMCGenV3/AMSB_chargino_200GeV_ctau100cm_FilterSumPt50_RECO/AMSB_chargino_RECO_0.root',
    )
)


process.source.fileNames = cms.untracked.vstring()
dir = 'condor/AMSB_chargino_200GeV_ctau10cm_FilterSumPt50_RECO/'
for file in os.listdir(dir):
    if file.find(".root") != -1 and file.find("RECO") != -1: # Skip over files that do not contain .root.
        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.genParticlePlusGEANT = cms.EDProducer("GenPlusSimParticleProducer",
                                              src           = cms.InputTag("g4SimHits"),   # use "famosSimHits" for FAMOS
                                              setStatus     = cms.int32(8),                # set status = 8 for GEANT GPs
                                              filter        = cms.vstring("pt > 0.0"),     # just for testing (optional)
                                              genParticles  = cms.InputTag("genParticles") # original genParticle list
                                              )


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myGenPlusSimFile.root')
    ,outputCommands = cms.untracked.vstring(
    #    'drop *',   # Remove the 'drop *' command if you want to keep all collections
    "keep *_*_*_*",
    "keep *_genParticles_*_*",
    "keep *_generalTracks_*_*",
    "keep *_genParticlePlusGEANT_*_*"
    )
                               )

process.p = cms.Path(process.genParticlePlusGEANT)

process.e = cms.EndPath(process.out)


