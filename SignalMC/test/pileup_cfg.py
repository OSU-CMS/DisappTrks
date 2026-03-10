import FWCore.ParameterSet.Config as cms

process = cms.Process("PileupDist")

# Need a dummy input source
process.source = cms.Source("PoolSource",
    fileNames=cms.untracked.vstring(
        '/store/mc/RunIIISummer24PrePremix/Neutrino_E-10_gun/PREMIX/Premixlib2024_140X_mcRun3_2024_realistic_v26-v1/140007/6b22f430-90d3-4e66-99f1-7fccdae45317.root'  # dummy file for CRAB validation
    )
)

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

process.TFileService = cms.Service("TFileService",
    fileName=cms.string("pileup_output.root")
)

process.pileupDist = cms.EDAnalyzer("PileupDistAnalyzer",
    pileupInfoTag=cms.InputTag("addPileupInfo", "", "DIGI"),
)

process.p = cms.Path(process.pileupDist)

