#!/usr/bin/env python

import os
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = ''

config.Data.outputPrimaryDataset = ''
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1'

config.Data.outLFNDirBase = '/store/user/micarrig/'
config.Site.storageSite = 'T3_US_FNALLPC'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    def forkAndSubmit(config):
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
    
    config.General.requestName = 'NeutrinoGun_step1'
    config.JobType.psetName = 'NeutrinoGun_step1.py'
    config.Data.outputPrimaryDataset = 'NeutrinoGun_TuneCP5_13TeV_pythia8'
    config.Data.totalUnits = config.Data.unitsPerJob * numJobsPerLifetime[ctau]
    forkAndSubmit(config)

