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

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EEDRPremix-forPOG_124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'


config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 8
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v3_EXODisappTrkPAT'

config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/skim/2022/'
config.Site.storageSite = 'T3_US_FNALLPC'

config.Site.whitelist = ["T2_BR_SPRACE"]
config.Data.inputDBS = 'global'
