#!/usr/bin/env python

from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2/AMSB_chargino_step2_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ''
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 650 ###how many files to analyze
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v12-v1_step2'

config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = 200

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (user_name
#config.Site.storageSite = 'T2_US_Purdue'

#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
#config.Site.storageSite = 'T2_CH_CERN'

#config.Data.outLFNDirBase = '/store/user/borzari/'
#config.Site.storageSite = 'T2_BR_SPRACE'

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
    #############################################################################################

    reallySubmitEWK = False
    reallySubmitHiggsinoEWK = False

    reallySubmitMass = { x : False for x in range(100, 2100, 100)}
    reallySubmitLifetime = { x : False for x in [1, 10, 100, 1000, 10000]}

    if reallySubmitEWK:
        for mass in range(100, 2100, 100):
            for ctau in [1, 10, 100, 1000, 10000]:
                config.General.requestName = 'AMSB_chargino%dGeV_ctau%dcm_step2' % (mass, ctau)
                config.Data.inputDataset = '/AMSB_chargino_M-500GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/borzari-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1-052a807048eed62b1fdd283e23804bdd/USER' # Input the correct path for the GEN-SIM dataset and check the mass/lifetime points of the jobs
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print('Skipping submission of request:', config.General.requestName)
    if reallySubmitHiggsinoEWK:
        for mass in range(100, 1000, 100):
            for ctau in [1, 10, 100, 1000, 10000]:
                config.General.requestName = 'Higgsino%dGeV_ctau%dcm_step2' % (mass, ctau)
                config.Data.inputDataset = step1.higgsinoRun3[(mass, ctau)]
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print('Skipping submission of request:', config.General.requestName)
