import FWCore.ParameterSet.Config as cms

###########################################################
##### Setup process #####
###########################################################

process = cms.Process ('SignalMC')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.source = cms.Source ('PoolSource',
    fileNames = cms.untracked.vstring ("root://xrootd-cms.infn.it//store/mc/RunIISpring15MiniAODv2/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2_ext1-v1/10000/06C6F736-BB71-E511-AAB4-6C3BE5B59060.root"),
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

process.PUAnalyzer = cms.EDAnalyzer ('PUAnalyzer',
    pileUpInfos = cms.InputTag ("slimmedAddPileupInfo","","PAT" ),
)

###########################################################
##### Setup paths #####
###########################################################

process.mypath = cms.Path (process.PUAnalyzer)
