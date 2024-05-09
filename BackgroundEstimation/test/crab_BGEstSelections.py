#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Test2CRAB-6c2551f7c8575c19e6da935800c0d62f/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5 # this is the amount of files processed per output file

config.Data.publication = True
config.Data.outputDatasetTag = 'MuonTagPt55' # this is just an example; it will be part of the name of the output dataset

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (user_name)
#config.Site.storageSite = 'T2_US_Purdue'

#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
#config.Site.storageSite = 'T2_CH_CERN'

#config.Data.outLFNDirBase = '/store/user/borzari/'
#config.Site.storageSite = 'T2_BR_SPRACE'
