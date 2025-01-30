#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'DY_ZToMuMuISR' # this is the name of the crab folder; useful to keep track of what is happening

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True

# always use MINIAOD as inputDataset and AOD as secondaryInputDataset

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/borzari-ZToMuMuISR-ce40d0a594f47a28c579da1a61d72f38/USER'

config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 # leave this as one to avoid too much wall time and jobs failing

config.JobType.maxMemoryMB = 4000

config.Data.publication = True
config.Data.outputDatasetTag = 'ZToMuMuISR' # this is just an example; it will be part of the name of the output dataset

# Uncomment one of the following pairs

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'
