#!/usr/bin/env python3

from CRABClient.UserUtilities import config

config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'NeutrinoGun_step2.py'
config.JobType.numCores = 4

config.Data.inputDataset = '/NeutrinoGun_TuneCP5_13TeV_pythia8/micarrig-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-ac4bb90274d44042007fb9a3ea8f416f/USER'
config.Data.useParent = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step2'

config.JobType.maxMemoryMB = 8000

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
    
    config.General.requestName = 'NeutrinoGun_step2'
    forkAndSubmit(config)

