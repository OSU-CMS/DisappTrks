#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'MuonTagPt55' # this is the name of the crab folder; useful to keep track of what is happening

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True
# List of files that are in the repos, but are used for the selections
config.JobType.inputFiles = [os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Collections/data/Fall15_25nsV2_MC_SF_AK4PFchs.txt', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Collections/data/Fall15_25nsV2_MC_PtResolution_AK4PFchs.txt', '/data/users/mcarrigan/condor/run3Inputs/Summer22EE_23Sep2023_RunEFG_v1.root']

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
