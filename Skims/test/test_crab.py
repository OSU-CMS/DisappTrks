#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crabPAT'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'test_EXODisappTrk_MC2022_PAT.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000

# config.Data.inputDataset = '/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EEDRPremix-forPOG_124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'
# config.Data.inputDataset = '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'

# config.Data.inputDataset = '/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDR-EpsilonPU_124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDR-EpsilonPU_124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'

# config.Data.inputDataset = '/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'
# config.Data.inputDataset = '/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM'

# config.Data.inputDataset = '/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v1/AODSIM'
# config.Data.inputDataset = '/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'

# config.Data.inputDataset = '/WtoMuNu_M-100to200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
# config.Data.inputDataset = '/WtoMuNu_M-200to500_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'
config.Data.inputDataset = '/WtoMuNu_M-500to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM'


config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 8
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3_EXODisappTrkPAT'

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'

config.Site.whitelist = ["T2_BR_SPRACE"]
