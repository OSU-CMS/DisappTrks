#!/usr/bin/env python

import os
import sys

if notos.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
if os.environ["CMSSW_VERSION"] != "CMSSW_9_2_12_patch1"
    print "Please switch to CMSSW_9_2_12_patch1!"
    sys.exit (0)

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
config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-DisappTrks-v1'

config.Site.storageSite = 'T2_US_Purdue'
#config.Site.storageSite = 'T3_US_FNALLPC'

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

    ## data
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/PromptReco/Cert_294927-304507_13TeV_PromptReco_Collisions17_JSON.txt'

    # Run2017C-v1

    config.Data.outputDatasetTag = 'Run2017C-PromptReco-v1-DisappTrks-v1'
    config.Data.unitsPerJob = 53 # 2017C has ~53k lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017C-PromptReco-v1'
    config.Data.inputDataset = '/MET/Run2017C-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017C-PromptReco-v1'
    config.Data.inputDataset = '/Tau/Run2017C-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017C-PromptReco-v1'
    config.Data.inputDataset = '/SingleMuon/Run2017C-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017C-PromptReco-v1'
    config.Data.inputDataset = '/SingleElectron/Run2017C-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2017C-v2

    config.Data.outputDatasetTag = 'Run2017C-PromptReco-v2-DisappTrks-v1'
    config.Data.unitsPerJob = 53 # 2017C has ~53k lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017C-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2017C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017C-PromptReco-v2'
    config.Data.inputDataset = '/Tau/Run2017C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017C-PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2017C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017C-PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2017C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2017C-v3

    config.Data.outputDatasetTag = 'Run2017C-PromptReco-v3-DisappTrks-v1'
    config.Data.unitsPerJob = 53 # 2017C has ~53k lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017C-PromptReco-v3'
    config.Data.inputDataset = '/MET/Run2017C-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017C-PromptReco-v3'
    config.Data.inputDataset = '/Tau/Run2017C-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017C-PromptReco-v3'
    config.Data.inputDataset = '/SingleMuon/Run2017C-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017C-PromptReco-v3'
    config.Data.inputDataset = '/SingleElectron/Run2017C-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)
