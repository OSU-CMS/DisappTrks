#!/usr/bin/env python

import os
from CRABClient.UserUtilities import config
config = config()

step = 2

requestName = ''
psetName = ''
outputPrimaryDataset = ''
outputDatasetTag = ''
inputDataset = ''
pluginName = ''

if step==1:
    requestName = 'DisappTrks-neutrinoGun-step1-124X-v1'
    psetName = 'neutrinoGun2022/neutrinoGun_step1_cfg.py'
    outputPrimaryDataset = 'DisappTrks_neutrinoGun_step1_124X_v1'
    outputDatasetTag = 'DisappTrksRun3-neutrinoGunE10-124X_mcRun3_2022_v1'
    pluginName = 'PrivateMC'
elif step==2:
    requestName = 'DisappTrks-neutrinoGun-step2-124X-v1p3'
    #psetName = 'minBias_summer22_step2_cfg.py'
    psetName = 'neutrinoGun2022/neutrinoGun_step2_cfg.py'
    outputDatasetTag = 'DisappTrksRun3-neutrinoGunE10-124X_mcRun3_2022_v1'
    inputDataset = '/DisappTrks_neutrinoGun_step1_124X_v1/lpclonglived-DisappTrksRun3-neutrinoGunE10-124X_mcRun3_2022_v1-17c935b08a332af07d2dd3fa4c1279e1/USER'
    pluginName = 'Analysis'
elif step==3:
    requestName = 'DisappTrks-minBias-step3-124X-v2'
    psetName = 'minBias_summer22_step3_cfg.py'
    outputDatasetTag = 'DisappTrksRun3-minBias-124X_mcRun3_2022_realistic_v12-v2'
    inputDataset = '/DisappTrks_minBias_step1_124X_v2/lpclonglived-DisappTrksRun3-minBias-124X_mcRun3_2022_realistic_v12-v2-886b8a79b45104bd8649977c50ed13ef/USER'
    pluginName = 'Analysis'
elif step==4:
    requestName = 'DisappTrks-minBias-step4-124X-v2'
    psetName = 'minBias_summer22_step4_cfg.py'
    outputDatasetTag = 'DisappTrksRun3-minBias-124X_mcRun3_2022_realistic_v12-v2'
    inputDataset = '/DisappTrks_minBias_step1_124X_v2/lpclonglived-DisappTrksRun3-minBias-124X_mcRun3_2022_realistic_v12-v2-a13a68cb1d57966dd997a646be034d9c/USER'
    pluginName = 'Analysis'

if requestName=='' or psetName == '' or outputDatasetTag == '' or pluginName == '':
    print("Need to specify the requestName, psetName, pluginName, and outputDatasetTag")
    sys.exit(0)
if step!=1 and inputDataset == '':
    print("Need to give an input dataset")
    sys.exit(0)
if step==1 and outputPrimaryDataset == '':
    print("Need to give outputPrimaryDataset")
    sys.exit(0)

config.General.requestName = requestName
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = pluginName
config.JobType.psetName = psetName
config.JobType.allowUndistributedCMSSW = True

config.Data.publication = True
config.Data.outputDatasetTag = outputDatasetTag

config.Data.useParent = False
config.Data.inputDBS = 'phys03'

if step==1:
    config.Data.unitsPerJob = 1000
    config.JobType.maxJobRuntimeMin = 200
    NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
    config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
    config.Data.splitting = 'EventBased'
    config.Data.outputPrimaryDataset = outputPrimaryDataset
elif step==2:
    config.JobType.maxMemoryMB = 4000
    config.Data.unitsPerJob = 1
    config.Data.splitting = 'FileBased'
    config.Data.inputDataset = inputDataset
    config.Data.outputPrimaryDataset = outputPrimaryDataset
    config.JobType.numCores = 1
else:
    config.Data.unitsPerJob = 1
    config.Data.splitting = 'LumiBased'
    config.Data.inputDataset = inputDataset
    config.JobType.numCores = 4

config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Site.storageSite = 'T3_US_FNALLPC'




