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
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC2016_cfg.py'  # For MC only
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-DisappTrks-v1'

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
    ## Do the MC first

    config.Site.storageSite = 'T2_US_Purdue'

    config.Data.unitsPerJob = 75
    config.General.requestName = 'candidateTrackProducer_DYToLL'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 75
    config.General.requestName = 'candidateTrackProducer_WToLNu'
    config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 2
    config.General.requestName = 'candidateTrackProducer_TT_RecoDebug'
    config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16DR80-PUSpring16_RECODEBUG_80X_mcRun2_asymptotic_2016_v3_ext1-v1/GEN-SIM-RECODEBUG'
    #forkAndSubmit(config)

##########################################################################
    ## Now do data
    config.JobType.numCores = 4

    config.Data.unitsPerJob = 10
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

    config.Site.storageSite = 'T2_US_Purdue'

    # Run2016B-v3

    config.Data.outputDatasetTag = 'Run2016B-23Sep2016-v3-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016B-23Sep2016-v3'
    config.Data.inputDataset = '/MET/Run2016B-23Sep2016-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016B-23Sep2016-v3'
    config.Data.inputDataset = '/Tau/Run2016B-23Sep2016-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016B-23Sep2016-v3'
    config.Data.inputDataset = '/SingleMuon/Run2016B-23Sep2016-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016B-23Sep2016-v3'
    config.Data.inputDataset = '/SingleElectron/Run2016B-23Sep2016-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016C

    config.Data.outputDatasetTag = 'Run2016C-23Sep2016-v1-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016C-23Sep2016-v1'
    config.Data.inputDataset = '/MET/Run2016C-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016C-23Sep2016-v1'
    config.Data.inputDataset = '/Tau/Run2016C-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016C-23Sep2016-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016C-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016C-23Sep2016-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016C-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016D

    config.Data.outputDatasetTag = 'Run2016D-23Sep2016-v1-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016D-23Sep2016-v1'
    config.Data.inputDataset = '/MET/Run2016D-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016D-23Sep2016-v1'
    config.Data.inputDataset = '/Tau/Run2016D-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016D-23Sep2016-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016D-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016D-23Sep2016-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016D-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016E

    config.Data.outputDatasetTag = 'Run2016E-23Sep2016-v1-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016E-23Sep2016-v1'
    config.Data.inputDataset = '/MET/Run2016E-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016E-23Sep2016-v1'
    config.Data.inputDataset = '/Tau/Run2016E-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016E-23Sep2016-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016E-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016E-23Sep2016-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016E-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016F

    config.Data.outputDatasetTag = 'Run2016F-23Sep2016-v1-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016F-23Sep2016-v1'
    config.Data.inputDataset = '/MET/Run2016F-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016F-23Sep2016-v1'
    config.Data.inputDataset = '/Tau/Run2016F-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016F-23Sep2016-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016F-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016F-23Sep2016-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016F-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016G

    config.Data.outputDatasetTag = 'Run2016G-23Sep2016-v1-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016G-23Sep2016-v1'
    config.Data.inputDataset = '/MET/Run2016G-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016G-23Sep2016-v1'
    config.Data.inputDataset = '/Tau/Run2016G-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016G-23Sep2016-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016G-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016G-23Sep2016-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016G-23Sep2016-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016H-v2 (no lumi sections from the Golden JSON are in PromptReco-v1)

    config.Data.outputDatasetTag = 'Run2016H-PromptReco-v2-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016H-PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016H-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016H-PromptReco-v2'
    config.Data.inputDataset = '/Tau/Run2016H-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016H-PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2016H-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016H-PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2016H-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016H-v3

    config.Data.outputDatasetTag = 'Run2016H-PromptReco-v3-DisappTrks-v2'

    config.General.requestName = 'candidateTrackProducer_MET_2016H-PromptReco-v3'
    config.Data.inputDataset = '/MET/Run2016H-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016H-PromptReco-v3'
    config.Data.inputDataset = '/Tau/Run2016H-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016H-PromptReco-v3'
    config.Data.inputDataset = '/SingleMuon/Run2016H-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016H-PromptReco-v3'
    config.Data.inputDataset = '/SingleElectron/Run2016H-PromptReco-v3/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)
