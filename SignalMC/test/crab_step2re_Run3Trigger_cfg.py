#!/usr/bin/env python3

from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
import DisappTrks.SignalMC.step2 as step2
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'reHLT/run3Trigger/MC_step2_Run3_customizeL1.py'
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16_step2_reHLT'

config.JobType.maxMemoryMB = 8000

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Site.storageSite = 'T2_US_Purdue'

#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
#config.Site.storageSite = 'T2_CH_CERN'

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

    reallySubmitEWK = True
    reallySubmitHiggsinoEWK = False

    reallySubmitMass = { x : True for x in range(100, 1200, 100)}
    reallySubmitLifetime = { x : True for x in [1, 10, 100, 1000, 10000]}

    if reallySubmitEWK:
        for mass in range(100, 1000, 100):
            for ctau in [100]:
                if not (mass, ctau) in step2.amsbRun3TriggerStudy:
                    print 'Skipping (%d GeV, %d cm)' % (mass, ctau)
                    continue
                config.General.requestName = 'AMSB_chargino%dGeV_ctau%dcm_step2_reHLT' % (mass, ctau)
                config.Data.inputDataset = step2.amsbRun3TriggerStudy[(mass, ctau)]
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print 'Skipping submission of request:', config.General.requestName
    if reallySubmitHiggsinoEWK:
        for mass in range(100, 1000, 100):
            for ctau in [1, 10, 100, 1000, 10000]:
                if not (mass, ctau) in step1.higgsino2018:
                    print 'Skipping (%d GeV, %d cm)' % (mass, ctau)
                    continue
                config.General.requestName = 'Higgsino%dGeV_ctau%dcm_step2_reHLT' % (mass, ctau)
                config.Data.inputDataset = step2.higgsino2018[(mass, ctau)]
                if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                    forkAndSubmit(config)
                else:
                    print 'Skipping submission of request:', config.General.requestName
