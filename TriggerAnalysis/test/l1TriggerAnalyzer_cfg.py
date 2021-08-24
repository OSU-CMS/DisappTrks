import FWCore.ParameterSet.Config as cms
import sys
import os

process = cms.Process("L1REPACKANA")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.categories.append ("L1EmulationInfoPrinter")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
     #"file:l1Ntuple_RAW2DIGI.root"
     #"file:l1Ntuple_AMSB_RAW2DIGI.root"
     #"file:l1Ntuple_AMSB_RAW2DIGI_noCustomed.root"
     #"file:l1Ntuple_AMSB_RAW2DIGI_Customized.root"
     #"file:/uscms/home/kwei726/nobackup/DisappTrksRun3_Dev/CMSSW_11_2_0/src/DisappTrks/TriggerAnalysis/test/SampleFiles/l1Ntuple_RAW2DIGI_fromRECO_v11.root"
     "file:/uscms/home/kwei726/nobackup/DisappTrksRun3_Dev/CMSSW_11_2_0/src/DisappTrks/TriggerAnalysis/test/SampleFiles/l1Ntuple_RAW2DIGI_fromRECO_N1300.root"
    ),
    inputCommands = cms.untracked.vstring(
      'keep *',
      'drop *_gmtStage2Digis_EMTF_RAW2DIGI',
    )
)

process.options = cms.untracked.PSet (
    SkipEvent = cms.untracked.vstring ("ProductNotFound")
)
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.printer = cms.EDAnalyzer("L1EmulationInfoPrinter",
                              L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
                              AlgInputTag         = cms.InputTag("gtStage2Digis","","RAW2DIGI"),
                              triggers  = cms.InputTag('TriggerResults',    '',     'RAW2DIGI'),
                              l1GtBits  = cms.InputTag('gtDigis',           '',     'RAW2DIGI'),
                              sumEt     = cms.InputTag('caloStage2Digis',   'EtSum','RAW2DIGI'),
                              jets      = cms.InputTag('caloStage2Digis',   'Jet',  'RAW2DIGI'),
                              vertices  = cms.InputTag('offlinePrimaryVertices',   '',     'RECO'),                        
                              pfMet     = cms.InputTag('pfMet',             '',     'RECO'),
                              pfJets    = cms.InputTag('ak4PFJets',         '',     'RECO'),
                              recoMuons = cms.InputTag('muons',             '',     'RECO'),
                              l1etmhfThreshold = cms.untracked.double(90.),
                              l1jetThreshold   = cms.untracked.double(60.),
                              l1httThreshold   = cms.untracked.double(60.),
                              mindPhiETMHFJet  = cms.untracked.double(3.),
                              )

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histo_N1300.root')
                                    )

process.p = cms.Path(process.printer)
