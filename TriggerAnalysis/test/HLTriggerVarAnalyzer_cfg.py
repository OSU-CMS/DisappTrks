import FWCore.ParameterSet.Config as cms
#from HLTrigger.HLTfilters.hltHighLevel_cfi import *
import sys
import os
#from ROOT import TFile
process = cms.Process("Demo3")
process.load("FWCore.MessageLogger.MessageLogger_cfi")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://cms-xrd-global.cern.ch//store/data/Run2018D/EGamma/MINIAOD/PromptReco-v2/000/325/111/00000/C6B23C6D-90B7-3C4A-9230-5025E26ED7DE.root'
    )
)

process.options = cms.untracked.PSet (
    SkipEvent = cms.untracked.vstring ("ProductNotFound")
)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')



process.demo = cms.EDAnalyzer("HLTrigVarProducer",
                              mets = cms.InputTag('slimmedMETs'),
                              #l1mets = cms.InputTag('l1extraParticles','MET','RECO'),
                              photons = cms.InputTag('slimmedPhotons'),
                              triggers = cms.InputTag('TriggerResults','','HLT'),
                              trigobjs = cms.InputTag('slimmedPatTrigger')
                              )
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET0_*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET75_IsoTrk50_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET60_IsoTrk35_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET75_IsoTrk50_v*", "HLT_PFMET170_NoiseCleaned_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET75_IsoTrk50_v*", "HLT_PFCenJet140_PFMETNoMu100_PFMHTNoMu140_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::RECO", HLTPaths = ["HLT_PFCenJet140_PFMETNoMu100_PFMHTNoMu140_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_CaloMET200_NoiseCleaned_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFMET170_NoiseCleaned_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*"])

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histo.root')
                                    )


#process.p = cms.Path(process.triggerSelection + process.demo)
process.p = cms.Path(process.demo)
