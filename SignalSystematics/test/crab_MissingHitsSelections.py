#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'MissingHits_QCD-3200' # this is the name of the crab folder; useful to keep track of what is happening

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True
# List of files that are in the repos, but are used for the selections
config.JobType.inputFiles = [os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Collections/data/Fall15_25nsV2_MC_SF_AK4PFchs.txt', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Collections/data/Fall15_25nsV2_MC_PtResolution_AK4PFchs.txt', os.environ['CMSSW_BASE']+'/src/DisappTrks/SignalSystematics/test/Summer22EE_23Sep2023_RunEFG_v1.root', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/graph.pb', os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/graph_oct25.pb']

# always use MINIAOD as inputDataset and AOD as secondaryInputDataset

#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/borzari-3Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/WZ_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
#config.Data.inputDataset = '/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'
config.Data.inputDataset = '/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER'

#config.Data.secondaryInputDataset = '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EEDRPremix-forPOG_124X_mcRun3_2022_realistic_postEE_v1-v3/AODSIM'

#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 50000 # leave this as one to avoid too much wall time and jobs failing

config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4

config.Data.publication = False
config.Data.outputDatasetTag = 'MissingHits_QCD-3200' # this is just an example; it will be part of the name of the output dataset

# Uncomment one of the following pairs

config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (user_name)
#config.Site.storageSite = 'T2_US_Purdue'

#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
#config.Site.storageSite = 'T2_CH_CERN'

# config.Data.outLFNDirBase = '/store/user/borzari/'
# config.Site.storageSite = 'T2_BR_SPRACE'
