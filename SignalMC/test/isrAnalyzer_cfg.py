import FWCore.ParameterSet.Config as cms

process = cms.Process ("ISR")

process.load ("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet ( input = cms.untracked.int32 (-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring (
        '/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step0.root',
    )
)

process.ISRAnalyzer = cms.EDAnalyzer ('ISRAnalyzer',
    genParticles = cms.InputTag ("genParticles", ""),
)

process.TFileService = cms.Service ("TFileService",
    fileName = cms.string ('hist.root')
)

process.p = cms.Path (process.ISRAnalyzer)
