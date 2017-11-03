import FWCore.ParameterSet.Config as cms
import glob

###########################################################
##### Setup process #####
###########################################################

process = cms.Process ('BkgdMC')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append ("GenZPtAnalyzer")
process.MessageLogger.cerr.GenZPtAnalyzer = cms.untracked.PSet(
    limit = cms.untracked.int32(0),
)
process.source = cms.Source ('PoolSource',
    skipBadFiles = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring (
        glob.glob ("/store/user/ahart/DYToMuMu_M_20_13TeV_step1/DYToMuMu_M_20_13TeV_step1_*.root")
        #glob.glob ("/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/*/miniAODWithCandidateTracks_*.root")
    )
)
process.TFileService = cms.Service ("TFileService",
    fileName = cms.string ('hist.root')
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

###########################################################
##### Setup the analyzers #####
###########################################################

process.GenZPtAnalyzer = cms.EDAnalyzer ('GenZPtAnalyzer',
    genParticles = cms.InputTag ("genParticles", ""),
    #genParticles = cms.InputTag ("prunedGenParticles", ""),
)

###########################################################
##### Setup paths #####
###########################################################

process.mypath = cms.Path (process.GenZPtAnalyzer)
