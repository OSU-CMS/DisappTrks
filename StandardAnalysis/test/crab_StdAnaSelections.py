#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'Skimming' # this is the name of the crab folder; useful to keep track of what is happening

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v3/MINIAODSIM'

config.Data.inputDBS = 'global'
# config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 # leave this as one to avoid too much wall time and jobs failing

config.Data.publication = True
config.Data.outputDatasetTag = 'Skimming' # this is just an example; it will be part of the name of the output dataset

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (user_name)
#config.Site.storageSite = 'T2_US_Purdue'

#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
#config.Site.storageSite = 'T2_CH_CERN'

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'
