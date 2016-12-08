import FWCore.ParameterSet.Config as cms
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
import sys
import os
#from ROOT import TFile
process = cms.Process("Demo3")
process.load("FWCore.MessageLogger.MessageLogger_cfi")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(#'file:/afs/cern.ch/work/j/jbrinson/public/triggerDevEmulator/CMSSW_7_1_6/src/testSigFiles_NoPU/AMSB_chargino_NoFilter_13TeV_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_82.root',
#'file:/afs/cern.ch/work/j/jbrinson/public/triggerDevEmulator/CMSSW_7_2_0/src/AMSB_chargino_NoFilter_13TeV_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO.root',
#'file:/afs/cern.ch/work/j/jbrinson/public/triggerDevEmulator/CMSSW_7_2_0/src/outputFULLOther.root',
#'file:/afs/cern.ch/work/j/jbrinson/public/triggerDevEmulator/CMSSW_7_2_0/src/outputFULLWithMet.root',
#'file:/afs/cern.ch/work/j/jbrinson/public/triggerDevEmulator/CMSSW_7_2_0/src/outputFULL.root',
#'file:/home/jbrinson/DisTrack/mainAN/triggerDev/CMSSW_7_2_0/src/outputFULLAllEventsNoMet720.root'
#'file:/home/jbrinson/DisTrack/mainAN/triggerDev/CMSSW_7_2_0/src/outputFULLAllEventsNoMet720TrkIso.root'
'file:/home/jbrinson/DisTrack/mainAN/triggerDev/CMSSW_7_2_0/src/outputFULLAllEventsNoMet720MissInMissMidCalo.root'
#'file:/afs/cern.ch/work/j/jbrinson/public/triggerDevEmulator/CMSSW_7_2_0/src/outputFULLSimple.root',
)
                            )
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')



process.demo = cms.EDAnalyzer("MyTrigAnalyzer",
                              tracks = cms.untracked.InputTag("generalTracks"),
                              hltTracks = cms.untracked.InputTag("hltIter2Merged"),
                              muons = cms.untracked.InputTag("muons"),
                              mets = cms.untracked.InputTag("pfMet"),
                              genMets = cms.untracked.InputTag("genMetTrue"),
                              hltmets = cms.untracked.InputTag("hltMetClean"),
#                              l1mets = cms.untracked.InputTag("l1extraParticles"),
                              l1mets = cms.untracked.InputTag("hltL1extraParticles"),
                              genParts = cms.untracked.InputTag("genParticles"),
                              trigOn = cms.untracked.bool(True),
                              triggerResults = cms.untracked.InputTag("TriggerResults::TEST"),


                              )
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET0_*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET75_IsoTrk50_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET60_IsoTrk35_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET75_IsoTrk50_v*", "HLT_PFMET170_NoiseCleaned_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MET75_IsoTrk50_v*", "HLT_PFCenJet140_PFMETNoMu100_PFMHTNoMu140_v*"])
process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFCenJet140_PFMETNoMu100_PFMHTNoMu140_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_CaloMET200_NoiseCleaned_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFMET170_NoiseCleaned_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*"])
#process.triggerSelection = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::TEST", HLTPaths = ["HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*"])

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histo.root')
                                    )


process.p = cms.Path(process.triggerSelection + process.demo)
#process.p = cms.Path(process.demo)
