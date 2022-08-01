#!/usr/bin/env python

from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3/AMSB_chargino_step3_Run3_124X_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 650 ###how many files to analyze
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Summer22DRMiniAOD-FlatPU20to70_124X_mcRun3_2021_realistic_v1_step3'

config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = 200

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
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

    reallySubmitMass = { x : False for x in range(100, 1200, 100)}
    reallySubmitLifetime = { x : False for x in [1, 10, 100, 1000, 10000]}

    if reallySubmitEWK:
        for mass in range(100, 1200, 100):
            for ctau in [1, 10, 100, 1000, 10000]:
                config.General.requestName = 'AMSB_chargino%dGeV_ctau%dcm_step3' % (mass, ctau)
                config.Data.inputDataset = '/AMSB_chargino_M-1000GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/borzari-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER' # Input the correct path for the GEN-SIM dataset and check the mass/lifetime points of the jobs
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print('Skipping submission of request:', config.General.requestName)
    if reallySubmitHiggsinoEWK:
        for mass in range(100, 1000, 100):
            for ctau in [1, 10, 100, 1000, 10000]:
                config.General.requestName = 'Higgsino%dGeV_ctau%dcm_step3' % (mass, ctau)
                config.Data.inputDataset = step2.higgsino2018[(mass, ctau)]
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print('Skipping submission of request:', config.General.requestName)
