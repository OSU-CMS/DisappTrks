#!/usr/bin/env python

import os
import sys

if os.environ["CMSSW_VERSION"] != "CMSSW_10_2_11_patch1":
    print "Please switch to CMSSW_10_2_11_patch1!"
    sys.exit (0)

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC2018_cfg.py'  # For MC only
config.JobType.allowUndistributedCMSSW = True

config.JobType.numCores = 8
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

    ## Do MC first

    ## FILL IN WITH 2018 MC ##

    #############################################################################################
    ## Data
    #############################################################################################

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'

    # Run2018A

    config.Data.outputDatasetTag = 'Run2018A-17Sep2018'
    config.Data.unitsPerJob = 62 # 61133 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018A-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018A-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018A-17Sep2018-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018A-17Sep2018-v2/AOD'
    #forkAndSubmit(config)

    # Run2018B

    config.Data.outputDatasetTag = 'Run2018B-17Sep2018'
    config.Data.unitsPerJob = 30 # 29913 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    # Run2018C

    config.Data.outputDatasetTag = 'Run2018C-17Sep2018'
    config.Data.unitsPerJob = 28 # 27721 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    # Run2018D

    config.Data.outputDatasetTag = 'Run2018D-17Sep2018'
    config.Data.unitsPerJob = 71 # 140735 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)
