#!/usr/bin/env python3

import os
import sys

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC2017_cfg.py'  # For MC only
config.JobType.allowUndistributedCMSSW = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 2500
config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2'

config.Site.storageSite = 'T2_US_Purdue'
#config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T3_US_Rutgers'
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

    #############################################################################################
    ## Data
    #############################################################################################

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'

    # The AOD re-reco is labeled 17Nov17, however the re-reco campaign is labeled 31Mar2018

    # Run2017F-v1

    config.Data.outputDatasetTag = 'Run2017F-31Mar2018-v1-DisappTrks-v3'
    config.Data.unitsPerJob = 31 # 61275 lumis

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017F-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleElectron/Run2017F-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    forkAndSubmit(config)
