#!/usr/bin/env python

from CRABClient.UserUtilities import config
import os
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = ''
config.Data.secondaryInputDataset = ''
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 2000
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from http.client import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print("Failed submitting task: %s" % (hte.headers))
        except ClientException as cle:
            print("Failed submitting task: %s" % (cle))

    def forkAndSubmit(config):
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    ## This works fine for 2022EE campaign; it will need to be updated to 2022 and 2023/BPix.  ##
    #############################################################################################

    # These need to be set True for the blocks below to work
    reallySubmitEWK = False
    reallySubmitHiggsinoEWK = False

    reallySubmitMass = { x : True for x in range(100, 2100, 100)}
    reallySubmitLifetime = { x : True for x in [1, 10, 100, 1000, 10000]}

    if reallySubmitEWK:
        for mass in range(100, 1300, 100):
        # for mass in range(700, 800, 100): # for testing
            for ctau in [10,100,1000,10000]:
            # for ctau in [10]: # for testing; 10cm is good to check if the lifetime reweighting works from 0.1cm up to 9cm
                config.Data.outputDatasetTag = 'AMSB_Wino%dGeV_ctau%dcm_2022EE' % (mass, ctau)
                config.General.requestName = 'AMSB_Wino%dGeV_ctau%dcm_2022EE' % (mass, ctau)
                config.Data.inputDataset = '/AMSB_Wino_M%dGeV_ctau%dcm_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM' % (mass, ctau)
                config.Data.secondaryInputDataset = '/AMSB_Wino_M%dGeV_ctau%dcm_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM' % (mass, ctau)
                if mass == 100 and ctau == 10: # AMSB_Wino_100GeV_10cm original dataset only has 10k events; ext was created to fix it and has ~50k events
                    config.Data.inputDataset = '/AMSB_Wino_M%dGeV_ctau%dcm_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM' % (mass, ctau)
                    config.Data.secondaryInputDataset = '/AMSB_Wino_M%dGeV_ctau%dcm_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1_ext1-v2/AODSIM' % (mass, ctau)
                config.JobType.pyCfgParams=["doLifetimeReweighting=True","massForLifetimeReweighting="+str(mass),"lifetimeForLifetimeReweighting="+str(ctau)]
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print('Skipping submission of request:', config.General.requestName)

    if reallySubmitHiggsinoEWK:
        for mass in range(100, 1100, 100):
            for ctau in [10, 100, 1000, 10000]:
                config.General.outputDatasetTag = 'AMSB_Higgsino%dGeV_ctau%dcm_2022EE' % (mass, ctau)
                config.General.requestName = 'AMSB_Higgsino%dGeV_ctau%dcm_2022EE' % (mass, ctau)
                config.Data.inputDataset = '/AMSB_Higgsino_M%dGeV_ctau%dcm_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM' % (mass, ctau)
                config.Data.secondaryInputDataset = '/AMSB_Higgsino_M%dGeV_ctau%dcm_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM' % (mass, ctau)
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print('Skipping submission of request:', config.General.requestName)

