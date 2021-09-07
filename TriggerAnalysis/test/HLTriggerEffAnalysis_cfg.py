import FWCore.ParameterSet.Config as cms
#from HLTrigger.HLTfilters.hltHighLevel_cfi import *
import sys
import os
#from ROOT import TFile
process = cms.Process("Demo3")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

#TriggerName = "HLT_MET105_IsoTrk50_v10"
TriggerName = "HLT_PFMET105_IsoTrk50_v10"
#TriggerName = "HLT_MET105_PFJet80_Recoiling_v0"
#TriggerName = "HLT_PFMET105_PFJet80_Recoiling_v0"
#TriggerName = "HLT_MET120_IsoTrk50_v10"
#TriggerName = "HLT_PFMET120_IsoTrk50_v10"
#TriggerName = "HLT_MET120_PFJet80_Recoiling_v0"
#TriggerName = "HLT_PFMET120_PFJet80_Recoiling_v0"

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'file:/eos/uscms/store/group/lpclonglived/DisappTrks/SingleMuon/Run2018C-102X_dataRun2_v12-v4-MINIAOD/210112_092844/0000/DATA_step4_2018_12.root'
    #'root://cms-xrd-global.cern.ch//store/data/Run2018D/SingleMuon/MINIAOD/PromptReco-v2/000/320/500/00000/12C8CC7E-8C95-E811-BDA3-FA163EA1F576.root'
    #'root://cms-xrd-global.cern.ch//store/data/Run2018D/EGamma/MINIAOD/PromptReco-v2/000/325/111/00000/C6B23C6D-90B7-3C4A-9230-5025E26ED7DE.root'
    'file:/afs/cern.ch/work/k/kwei/public/HLTtriggerStudy/run3/CMSSW_11_3_0/src/DisappTrks/SignalMC/test/step4/AMSB_chargino700GeV_ctau100cm_step4.root'
    )
)

process.options = cms.untracked.PSet (
    SkipEvent = cms.untracked.vstring ("ProductNotFound")
)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')



process.efficiency = cms.EDAnalyzer("HLTrigEffAnalyzer",
                              mets = cms.InputTag('slimmedMETs'),
                              primaryvertexs =  cms.InputTag('offlineSlimmedPrimaryVertices'),
                              tracks  = cms.InputTag('isolatedTracks'),
                              pfCandidates = cms.InputTag('packedPFCandidates'),
                              jets = cms.InputTag('slimmedJets'),
                              triggers = cms.InputTag('TriggerResults','','HLT'),
                              trigobjs = cms.InputTag('slimmedPatTrigger'),
                              secondaryTriggers = cms.InputTag('TriggerResults','','HLTX'),
                              triggerName = cms.string(TriggerName)
                              )

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histo_'+TriggerName+'.root')
                                    )


#process.p = cms.Path(process.triggerSelection + process.demo)
process.p = cms.Path(process.efficiency)
