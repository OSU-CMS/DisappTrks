import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackCollection")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
                                    'file:/home/rsantos/scratch0/CMSSW_12_4_11_patch3/src/DisappTrks/BackgroundEstimation/test/condor/2022/EGammaFiducialMapWithoutIsoCut/EGamma_2022G/ElectronFiducialCalcBeforeOldCuts/skim_9.root')
                )


process.trackCollectionAnalyzer = cms.EDAnalyzer("TrackCollectionAnalyzer",
    tracks           = cms.InputTag("candidateTrackProducer"),
    packedCandidates = cms.InputTag("packedPFCandidates"),
    lostTracks       = cms.InputTag("lostTracks"),
    isolatedTracks   = cms.InputTag("isolatedTracks"),
    genParticles     = cms.InputTag("genParticles"),

    vertices	   = cms.InputTag("offlineSlimmedPrimaryVertices", ""),
    electrons	   = cms.InputTag("slimmedElectrons", ""),
    muons          = cms.InputTag("slimmedMuons", ""),
    taus           = cms.InputTag("slimmedTaus", ""),
    jets           = cms.InputTag("slimmedJets", ""),
)

process.p = cms.Path(process.trackCollectionAnalyzer)
