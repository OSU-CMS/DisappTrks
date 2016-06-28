#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC_cfg.py'  # For MC only

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1'

config.Site.storageSite = 'T3_US_OSU'

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

##########################################################################
    ## Now do data
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_cfg.py'

    config.Data.unitsPerJob = 4

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
    config.Data.outputDatasetTag = 'Run2016B-PromptReco-v2-DisappTrks-v2'

    config.Site.storageSite = 'T2_US_Purdue'

    config.General.requestName = 'candidateTrackProducer_MET_2016B_PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016B-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016B_PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016B_PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2016B-PromptReco-v2/AOD'
    #forkAndSubmit(config)
