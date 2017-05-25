#!/usr/bin/env python

import os
import sys
if os.environ["CMSSW_VERSION"] != "CMSSW_8_0_20":
    print "Please switch to CMSSW_8_0_20!"
    sys.exit (0)

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = ''
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Data.publication = False
config.Data.outputDatasetTag = 'DisappTrks-HLTPurity-2016'

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


    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.Data.unitsPerJob = 10
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'

    config.Site.storageSite = 'T3_US_FNALLPC'

    config.Data.outputDatasetTag = 'Run2016B-PromptReco-v2-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016B-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016B-PromptReco-v2/MINIAOD'
    config.JobType.psetName = 'config_2016BC_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016C-PromptReco-v2-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016C-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016C-PromptReco-v2/MINIAOD'
    config.JobType.psetName = 'config_2016BC_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016D-PromptReco-v2-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016D-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016D-PromptReco-v2/MINIAOD'
    config.JobType.psetName = 'config_2016DEFGH_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016E-PromptReco-v2-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016E-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016E-PromptReco-v2/MINIAOD'
    config.JobType.psetName = 'config_2016DEFGH_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016F-PromptReco-v1-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016F-PromptReco-v1'
    config.Data.inputDataset = '/MET/Run2016F-PromptReco-v1/MINIAOD'
    config.JobType.psetName = 'config_2016DEFGH_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016G-PromptReco-v1-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016G-PromptReco-v1'
    config.Data.inputDataset = '/MET/Run2016G-PromptReco-v1/MINIAOD'
    config.JobType.psetName = 'config_2016DEFGH_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016H-PromptReco-v2-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016H-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016H-PromptReco-v2/MINIAOD'
    config.JobType.psetName = 'config_2016DEFGH_cfg.py'
    #forkAndSubmit(config)

    config.Data.outputDatasetTag = 'Run2016H-PromptReco-v3-DisappTrks_hltPurity'
    config.General.requestName = 'hltPurity_MET_2016H-PromptReco-v3'
    config.Data.inputDataset = '/MET/Run2016H-PromptReco-v3/MINIAOD'
    config.JobType.psetName = 'config_2016DEFGH_cfg.py'
    #forkAndSubmit(config)
