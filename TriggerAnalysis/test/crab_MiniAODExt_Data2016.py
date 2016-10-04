#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'triggerEfficiency2016'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'triggerEfficiency_withMuons_crab2016_cfg.py'

config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v2/MINIAOD'
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISpring16MiniAODv2-Data2016v2_80X-DisappTrks-v2'

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

    config.Data.unitsPerJob = 7

    config.Site.storageSite = 'T2_US_Purdue'

    config.General.requestName = 'trigEff_2016B_IsoTrk50'
    config.Data.outputDatasetTag = 'Run2016B-PromptReco-v2_TrigEfficiency-IsoTrk50'
    config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v2/MINIAOD'
    forkAndSubmit(config)

    config.General.requestName = 'trigEff_2016C_IsoTrk50'
    config.Data.outputDatasetTag = 'Run2016C-PromptReco-v2_TrigEfficiency-IsoTrk50'
    config.Data.inputDataset = '/SingleMuon/Run2016C-PromptReco-v2/MINIAOD'
    forkAndSubmit(config)

    config.General.requestName = 'trigEff_2016D_IsoTrk50'
    config.Data.outputDatasetTag = 'Run2016D-PromptReco-v2_TrigEfficiency-IsoTrk50'
    config.Data.inputDataset = '/SingleMuon/Run2016D-PromptReco-v2/MINIAOD'
    forkAndSubmit(config)

    config.General.requestName = 'trigEff_2016E_IsoTrk50'
    config.Data.outputDatasetTag = 'Run2016E-PromptReco-v2_TrigEfficiency-IsoTrk50'
    config.Data.inputDataset = '/SingleMuon/Run2016E-PromptReco-v2/MINIAOD'
    forkAndSubmit(config)

    # NOTE: this indeed is PromptReco-v1, there is no v2 is DAS for these datasets

    config.General.requestName = 'trigEff_2016F_IsoTrk50'
    config.Data.outputDatasetTag = 'Run2016F-PromptReco-v1_TrigEfficiency-IsoTrk50'
    config.Data.inputDataset = '/SingleMuon/Run2016F-PromptReco-v1/MINIAOD'
    forkAndSubmit(config)

    config.General.requestName = 'trigEff_2016G_IsoTrk50'
    config.Data.outputDatasetTag = 'Run2016G-PromptReco-v1_TrigEfficiency-IsoTrk50'
    config.Data.inputDataset = '/SingleMuon/Run2016G-PromptReco-v1/MINIAOD'
    forkAndSubmit(config)
