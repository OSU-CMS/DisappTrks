# Config file to produce the candidate track collection.
# Similar to candidateTrackProducer_AODInput_cfg.py but uses 
# MINIAOD as well as AOD files as input and 
# does not run the MINIAOD steps.  
# 
# Usage:
# To run over data:
# > cmsRun candidateTrackProducer_cfg.py print runOnMC=0

import FWCore.ParameterSet.Config as cms
import os


###########################################################
##### Set up process #####
###########################################################

import FWCore.ParameterSet.VarParsing as VarParsing 
options = VarParsing.VarParsing ('analysis')
options.register ('runOnMC',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Whether jobs will run over MC (1) or data (0)"
              )
options.parseArguments()


process = cms.Process ('DISAPPTRKS')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (101)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_0.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_1.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_2.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_3.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_4.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_5.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_6.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_7.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_8.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_9.root",
    ),
    secondaryFileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_0.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_1.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_2.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_3.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_4.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_5.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_6.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_7.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_8.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_9.root",
    ),
)

if not options.runOnMC:
    process.source.fileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/MINIAOD/05Oct2015-v1/30000/04F50A91-B46F-E511-A2A3-002618943923.root", 
        )
    process.source.secondaryFileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/1A77484B-DB68-E511-AEF6-02163E012456.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/564310C7-F868-E511-BD21-02163E014227.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/F0519CD5-D868-E511-B0BE-02163E014208.root",
        )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if options.runOnMC:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_Prompt_v4', '')


###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
process.candidateTracks = cms.Path (process.candidateTrackProducer)  

from DisappTrks.CandidateTrackProducer.customize import customizeMiniAODSIMOutput
customizeMiniAODSIMOutput(process)  

process.myEndPath = cms.EndPath (process.MINIAODSIMoutput)
