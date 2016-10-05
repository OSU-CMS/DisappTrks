#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC_cfg.py'  # For MC only
config.JobType.allowUndistributedCMSSW = True

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
    config.Data.unitsPerJob = 8
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt'

    config.Site.storageSite = 'T2_US_Purdue'

    # Run2016B

    config.Data.outputDatasetTag = 'Run2016B-PromptReco-v2-DisappTrks-v6'

    config.General.requestName = 'candidateTrackProducer_MET_2016B_PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016B-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016B_PromptReco-v2'
    config.Data.inputDataset = '/Tau/Run2016B-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016B_PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016B_PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2016B-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016C

    config.Data.outputDatasetTag = 'Run2016C-PromptReco-v2-DisappTrks-v6'

    config.General.requestName = 'candidateTrackProducer_MET_2016C_PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016C_PromptReco-v2'
    config.Data.inputDataset = '/Tau/Run2016C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016C_PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2016C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016C_PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2016C-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016D

    config.Data.outputDatasetTag = 'Run2016D-PromptReco-v2-DisappTrks-v6'

    config.General.requestName = 'candidateTrackProducer_MET_2016D_PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016D-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016D_PromptReco-v2'
    config.Data.inputDataset = '/Tau/Run2016D-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016D_PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2016D-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016D_PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2016D-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016E

    config.Data.outputDatasetTag = 'Run2016E-PromptReco-v2-DisappTrks-v6'

    config.General.requestName = 'candidateTrackProducer_MET_2016E_PromptReco-v2'
    config.Data.inputDataset = '/MET/Run2016E-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016E_PromptReco-v2'
    config.Data.inputDataset = '/Tau/Run2016E-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016E_PromptReco-v2'
    config.Data.inputDataset = '/SingleMuon/Run2016E-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016E_PromptReco-v2'
    config.Data.inputDataset = '/SingleElectron/Run2016E-PromptReco-v2/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016F
    # NOTE: this indeed is PromptReco-v1, there is no v2 is DAS for these datasets

    config.Data.outputDatasetTag = 'Run2016F-PromptReco-v1-DisappTrks-v6'

    config.General.requestName = 'candidateTrackProducer_MET_2016F_PromptReco-v1'
    config.Data.inputDataset = '/MET/Run2016F-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016F_PromptReco-v1'
    config.Data.inputDataset = '/Tau/Run2016F-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016F_PromptReco-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016F-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016F_PromptReco-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016F-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2016G
    # NOTE: this indeed is PromptReco-v1, there is no v2 is DAS for these datasets

    config.Data.outputDatasetTag = 'Run201G-PromptReco-v1-DisappTrks-v6'

    config.General.requestName = 'candidateTrackProducer_MET_2016G_PromptReco-v1'
    config.Data.inputDataset = '/MET/Run2016G-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2016G_PromptReco-v1'
    config.Data.inputDataset = '/Tau/Run2016G-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2016G_PromptReco-v1'
    config.Data.inputDataset = '/SingleMuon/Run2016G-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2016G_PromptReco-v1'
    config.Data.inputDataset = '/SingleElectron/Run2016G-PromptReco-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data2016_ElectronSkim_cfg.py'
    #forkAndSubmit(config)
