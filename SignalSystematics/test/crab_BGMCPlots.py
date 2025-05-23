#!/usr/bin/env python

from CRABClient.UserUtilities import config
import os
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'config_2022_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = ''
# config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'

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

    # valid_datasets contain the keys of the dictionary that defines the MiniAOD datasets in DisappTrks.StandardAnalysis.miniAOD_124X_Samples.
    # Every dataset that is inside valid_datasets will be used to create a CRAB task. The only needed changes are in config.Data.inputDataset,
    # config.Data.outputDatasetTag and config.General.requestName to assign different names to each task. The way they are separated is because
    # Not more than ~10k jobs can be submitted at once to T2_BR_SPRACE. Not sure what is the case for the OSU T3.
    # A similar procedure is done for collected data datasets, but the dictionary containing the dataset paths on DAS is set here as data_datasets.

    # valid_datasets = ['WToLNu_4Jets_2022EE','DYJetsToLL_M50_2022EE','DYto2L_4jets_M10to50_2022EE','TbarBtoLminusNuB_2022EE','TBbartoLplusNuBbar_2022EE','TbarQtoLNu_2022EE','TQbartoLNu_2022EE','TbarWplusto2L2Nu_2022EE','TbarWplustoLNu2Q_2022EE','TWminusto2L2Nu_2022EE','TWminustoLNu2Q_2022EE','WW_2022EE','WZ_2022EE','ZZ_2022EE','TTto2L2Nu_2022EE','TTtoLNu2Q_2022EE','TTto4Q_2022EE','QCD_PT15to30_2022EE','QCD_PT30to50_2022EE','QCD_PT50to80_2022EE','QCD_PT80to120_2022EE','QCD_PT120to170_2022EE','QCD_PT170to300_2022EE','QCD_PT300to470_2022EE','QCD_PT470to600_2022EE','QCD_PT600to800_2022EE','QCD_PT800to1000_2022EE','QCD_PT1000to1400_2022EE','QCD_PT1400to1800_2022EE','QCD_PT1800to2400_2022EE','QCD_PT2400to3200_2022EE','QCD_PT3200_2022EE','Zto2Nu_4Jets_HT100to200_2022EE','Zto2Nu_4Jets_HT200to400_2022EE','Zto2Nu_4Jets_HT400to800_2022EE','Zto2Nu_4Jets_HT800to1500_2022EE','Zto2Nu_4Jets_HT1500to2500_2022EE','Zto2Nu_4Jets_HT2500_2022EE']

    # valid_datasets = ['DYJetsToLL_M50_2023','DYto2L_4jets_M10to50_2023','TbarBtoLminusNuB_2023','TBbartoLplusNuBbar_2023','TbarQtoLNu_2023','TQbartoLNu_2023','TbarWplusto2L2Nu_2023','TbarWplustoLNu2Q_2023','TWminusto2L2Nu_2023','TWminustoLNu2Q_2023','WW_2023','WZ_2023','ZZ_2023']

    # valid_datasets = ['WToLNu_4Jets_2023']

    # valid_datasets = ['TTto2L2Nu_2023','TTtoLNu2Q_2023','TTto4Q_2023']

    # valid_datasets = ['Zto2Nu_4Jets_HT100to200_2023','Zto2Nu_4Jets_HT200to400_2023','Zto2Nu_4Jets_HT400to800_2023','Zto2Nu_4Jets_HT800to1500_2023','Zto2Nu_4Jets_HT1500to2500_2023','Zto2Nu_4Jets_HT2500_2023','QCD_PT15to30_2023','QCD_PT30to50_2023','QCD_PT50to80_2023','QCD_PT80to120_2023','QCD_PT120to170_2023','QCD_PT170to300_2023','QCD_PT300to470_2023','QCD_PT470to600_2023','QCD_PT600to800_2023','QCD_PT800to1000_2023','QCD_PT1000to1400_2023','QCD_PT1400to1800_2023','QCD_PT1800to2400_2023','QCD_PT2400to3200_2023','QCD_PT3200_2023']

    data_datasets = {

        'Muon0Cv1' : '/Muon0/Run2023C-22Sep2023_v1-v1/MINIAOD',
        'Muon0Cv2' : '/Muon0/Run2023C-22Sep2023_v2-v1/MINIAOD',
        'Muon0Cv3' : '/Muon0/Run2023C-22Sep2023_v3-v1/MINIAOD',
        'Muon0Cv4' : '/Muon0/Run2023C-22Sep2023_v4-v1/MINIAOD',
        'Muon1Cv1' : '/Muon1/Run2023C-22Sep2023_v1-v1/MINIAOD',
        'Muon1Cv2' : '/Muon1/Run2023C-22Sep2023_v2-v1/MINIAOD',
        'Muon1Cv3' : '/Muon1/Run2023C-22Sep2023_v3-v1/MINIAOD',
        'Muon1Cv4' : '/Muon1/Run2023C-22Sep2023_v4-v2/MINIAOD',

    }

    from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import dataset_names_bkgd_MiniAOD

    # for dataset in dataset_names_bkgd_MiniAOD:
    #     if dataset in valid_datasets:
    #         # config.Data.outputDatasetTag = dataset + '_basicPlotsv2'
    #         # config.General.requestName = dataset + '_basicPlotsv2'
    #         config.Data.outputDatasetTag = dataset + '_ZToMuMuISR'
    #         config.General.requestName = dataset + '_ZToMuMuISR'
    #         config.Data.inputDataset = dataset_names_bkgd_MiniAOD[dataset]
    #         forkAndSubmit(config)
    for dataset in data_datasets:
        config.Data.outputDatasetTag = dataset + '_ZToMuMuISR'
        config.General.requestName = dataset + '_ZToMuMuISR'
        config.Data.inputDataset = data_datasets[dataset]
        forkAndSubmit(config)
