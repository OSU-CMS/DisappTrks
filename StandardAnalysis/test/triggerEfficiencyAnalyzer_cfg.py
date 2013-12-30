# Usage:  
# cmsRun triggerEfficiencyAnalyzer_cfg.py | tee triggerEfficiencyAnalyzer_cfg.log
#
import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import os

process = cms.Process ('TriggerEfficiencyAnalyzer')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100


process.source = cms.Source ('PoolSource',
    fileNames = cms.untracked.vstring ()
)
#uncomment this line to add a single file to be processed
process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2013_12_20_SkimMet90/AMSB_mGrav61K_0p2ns/SkimMet90/bean_0.root')  

#uncomment these 3 lines to add all files in a given directory to be processed
## dir = "/store/user/abrinke1/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v1_BEAN_53xOn53x_V02_CV01/894bf83260076a22df0c97ce24c6bb58/"
## for file in os.listdir(dir):
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.TFileService = cms.Service ('TFileService',
                                    fileName = cms.string ('hist.root')
    )

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

process.TriggerEfficiencyAnalyzer = cms.EDAnalyzer ('TriggerEfficiencyAnalyzer',
    Trigger = cms.InputTag ('BNproducer', 'HLT'),
    triggers = cms.VPSet(),
)


#####################################################################
##### Define and Add the Desired Triggers to the List to be Run #####
##### One histogram will be made for each trigger type          #####  
#####################################################################
DisappTrk = cms.PSet(
    trigType = cms.string("DisappTrk"),
    trigs = cms.vstring(
	"HLT_MET80_Track60_dEdx3p7_v",
	"HLT_MET80_Track50_dEdx3p6_v", 
	"HLT_HT650_Track60_dEdx3p7_v", 
	"HLT_HT650_Track50_dEdx3p6_v", 
## 	"HLT_IsoTrackHB_v",  # Commissioning stream 
## 	"HLT_IsoTrackHE_v",  # Commissioning stream 
	"HLT_MET200_v", 
	"HLT_PFMET150_v", 
	"HLT_MET120_HBHENoiseCleaned_v",
	"HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v",
	"HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v", 
	"HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
        ),
    )
process.TriggerEfficiencyAnalyzer.triggers.append(DisappTrk);

process.myPath = cms.Path (process.TriggerEfficiencyAnalyzer)


