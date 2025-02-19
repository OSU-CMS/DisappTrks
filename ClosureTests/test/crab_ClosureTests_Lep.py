#!/usr/bin/env python

from CRABClient.UserUtilities import config
import os
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = ''
# config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

# process = 'DY'
process = 'ttbar'

channel = 'TauTagPt55NoJetCuts'

if process == 'DY':

    # dataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-forPOG_130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM'
    # datasetName = 'DYJetsToLL_M50_2022EE'

    # dataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22MiniAODv4-forPOG_130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
    # datasetName = 'DYJetsToLL_M50_2022'

    dataset = '/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM'
    datasetName = 'DYJetsToLL_M50_2023'

if process == 'ttbar':

    # dataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM'
    # datasetName = 'TTtoLNu2Q_2022EE'

    # dataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
    # datasetName = 'TTtoLNu2Q_2022'

    dataset = '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM'
    datasetName = 'TTtoLNu2Q_2023'

config.Data.outputDatasetTag = datasetName + '_ClosureTests_' + channel
config.General.requestName = datasetName + '_ClosureTests_' + channel
config.Data.inputDataset = dataset

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'
config.Site.blacklist = ['T2_ES_CIEMAT']

