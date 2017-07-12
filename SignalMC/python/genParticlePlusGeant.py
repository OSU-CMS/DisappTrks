import FWCore.ParameterSet.Config as cms
import copy

def customizeKeep (process):
  outputTypes = ["RAWSIM", "PREMIXRAW", "RECOSIM", "AODSIM", "MINIAODSIM"]
  for a in outputTypes:
    b = a + "output"
    if hasattr (process, b):
      getattr (process, b).outputCommands.append ("keep *_genParticlePlusGeant_*_*")
      getattr (process, b).outputCommands.append ("keep *_packedGenParticlePlusGeant_*_*")
      getattr (process, b).outputCommands.append ("keep *_prunedGenParticlePlusGeant_*_*")

  return process


def customizeProduce (process):
    process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",
                                                  src = cms.InputTag("g4SimHits"),            # use "famosSimHits" for FAMOS
                                                  setStatus = cms.int32(8),                   # set status = 8 for GEANT GPs
                                                  filter = cms.vstring("pt > 10.0"),          # just for testing (optional)
                                                  genParticles = cms.InputTag("genParticles") # original genParticle list
                                                  )

    if hasattr (process, "simulation_step") and hasattr(process, "psim"):
      getattr(process, "simulation_step")._seq = getattr(process,"simulation_step")._seq * process.genParticlePlusGeant

    return process

def customizeMiniAOD (process):
    process.packedGenParticlePlusGeant = copy.deepcopy (process.packedGenParticles)
    process.packedGenParticlePlusGeant._TypedParameterizable__type = "PATPackedGenParticlePlusGeantProducer"
    process.packedGenParticlePlusGeant.inputCollection = cms.InputTag ("prunedGenParticlePlusGeantWithStatusOne")
    process.packedGenParticlePlusGeant.inputOriginal = cms.InputTag ("genParticlePlusGeant")
    process.packedGenParticlePlusGeant.map = cms.InputTag ("prunedGenParticlePlusGeant")

    process.prunedGenParticlePlusGeant = copy.deepcopy (process.prunedGenParticles)
    process.prunedGenParticlePlusGeant.src = cms.InputTag ("prunedGenParticlePlusGeantWithStatusOne")

    process.prunedGenParticlePlusGeantWithStatusOne = copy.deepcopy (process.prunedGenParticlesWithStatusOne)
    process.prunedGenParticlePlusGeantWithStatusOne.select.append ("keep status == 8")
    process.prunedGenParticlePlusGeantWithStatusOne.src = cms.InputTag ("genParticlePlusGeant")

    return process
