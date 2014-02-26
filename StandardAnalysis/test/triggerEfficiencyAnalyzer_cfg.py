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
#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2013_12_20_SkimMet90/AMSB_mGrav61K_0p5ns/SkimMet90/bean_0.root')  
process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2013_12_30_SkimFullTrkSelection/AMSB_mGrav61K_0p5ns/FullTrkSelection/bean_0.root')  

#uncomment these 3 lines to add all files in a given directory to be processed
#dir = "/data/users/wulsin/condor/analysisTemplateV3/condor_2013_12_20_Skim\
#Met90/AMSB_mGrav61K_0p2ns/"

#for file in os.listdir(dir):
#    if file.find(".root") != -1:  # Skip over files that do not contain .root.  
#        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.TFileService = cms.Service ('TFileService',
m                                    fileName = cms.string ('hist.root')
    )

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
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
## 	"HLT_MET80_Track60_dEdx3p7_v",
## 	"HLT_MET80_Track50_dEdx3p6_v", 
## 	"HLT_HT650_Track60_dEdx3p7_v", 
## 	"HLT_HT650_Track50_dEdx3p6_v", 
## ## 	"HLT_IsoTrackHB_v",  # Commissioning stream 
## ## 	"HLT_IsoTrackHE_v",  # Commissioning stream 
## 	"HLT_MET200_v", 
## 	"HLT_PFMET150_v", 
## 	"HLT_MET120_HBHENoiseCleaned_v",
## 	"HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v",
## 	"HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v", 




    "HLT_HT250_AlphaT0p55_v",
    "HLT_HT250_AlphaT0p57_v",
#    "HLT_HT300_AlphaT0p53_v",
#    "HLT_HT300_AlphaT0p54_v",
#    "HLT_HT350_AlphaT0p52_v",
#    "HLT_HT350_AlphaT0p53_v",
#    "HLT_HT400_AlphaT0p51_v",

    "HLT_PFNoPUHT350_PFMET100_v",
    "HLT_PFNoPUHT400_PFMET100_v",

##    "HLT_RsqMR40_Rsq0p04_v",  #this trigger is prescaled
    "HLT_RsqMR45_Rsq0p09_v",
    "HLT_RsqMR55_Rsq0p09_MR150_v",
    "HLT_RsqMR60_Rsq0p09_MR150_v",
    "HLT_DiPFJetAve400_v",
    "HLT_MET80_v", # in trigger menu for jet ht, prescaled
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",

        ),
    )
process.TriggerEfficiencyAnalyzer.triggers.append(DisappTrk);

process.myPath = cms.Path (process.TriggerEfficiencyAnalyzer)


