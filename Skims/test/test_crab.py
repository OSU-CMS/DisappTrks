#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crabPAT2'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'test_EXODisappTrk_MC2022_PAT.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000

# config.Data.inputDataset = '/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EEDRPremix-forPOG_124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
config.Data.inputDataset = '/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDR-EpsilonPU_124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 8
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3_EXODisappTrkPAT2'

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'

config.Site.whitelist = ["T2_BR_SPRACE"]