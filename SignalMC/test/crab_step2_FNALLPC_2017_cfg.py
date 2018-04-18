#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2/AMSB_chargino_step2_2017_cfg.py'
config.JobType.numCores = 4

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1_step2'

config.Site.storageSite = 'T3_US_FNALLPC'

config.JobType.maxMemoryMB = 8000

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


    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'AMSB_chargino700GeV_ctau100cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-700_CTau-100_TuneCUEP8M1_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-94X_mc2017_realistic_v10-v3-8f3a8657071e90c6a17a2fb14d07aeb5/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino700GeV_ctau1000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-700_CTau-1000_TuneCUEP8M1_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-94X_mc2017_realistic_v10-v3-15a26dfbf2810ea023e4b06ebe64c27e/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino300GeV_ctau100cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-300_CTau-100_TuneCUEP8M1_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-94X_mc2017_realistic_v10-v3-508e13cba294da224a49b3f7ba92121a/USER'
    #forkAndSubmit(config)
