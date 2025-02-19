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
config.JobType.maxMemoryMB = 3500

config.Data.inputDataset = ''
# config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/borzari/'
config.Site.storageSite = 'T2_BR_SPRACE'
config.Site.blacklist = ['T2_ES_CIEMAT']

# debug = True
debug = False

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

    # valid_datasets = ['WToLNu_4Jets_2022EE','DYJetsToLL_M50_2022EE','DYto2L_4jets_M10to50_2022EE','TbarBtoLminusNuB_2022EE','TBbartoLplusNuBbar_2022EE','TbarQtoLNu_2022EE','TQbartoLNu_2022EE','TbarWplusto2L2Nu_2022EE','TbarWplustoLNu2Q_2022EE','TWminusto2L2Nu_2022EE','TWminustoLNu2Q_2022EE','WW_2022EE','WZ_2022EE','ZZ_2022EE','TTto2L2Nu_2022EE','TTtoLNu2Q_2022EE','TTto4Q_2022EE','QCD_PT15to30_2022EE','QCD_PT30to50_2022EE','QCD_PT50to80_2022EE','QCD_PT80to120_2022EE','QCD_PT120to170_2022EE','QCD_PT170to300_2022EE','QCD_PT300to470_2022EE','QCD_PT470to600_2022EE','QCD_PT600to800_2022EE','QCD_PT800to1000_2022EE','QCD_PT1000to1400_2022EE','QCD_PT1400to1800_2022EE','QCD_PT1800to2400_2022EE','QCD_PT2400to3200_2022EE','QCD_PT3200_2022EE','Zto2Nu_4Jets_HT100to200_2022EE','Zto2Nu_4Jets_HT200to400_2022EE','Zto2Nu_4Jets_HT400to800_2022EE','Zto2Nu_4Jets_HT800to1500_2022EE','Zto2Nu_4Jets_HT1500to2500_2022EE','Zto2Nu_4Jets_HT2500_2022EE']

    # valid_datasets = ['DYJetsToLL_M50_2022EE','DYto2L_4jets_M10to50_2022EE']

    # valid_datasets = ['WToLNu_4Jets_2022EE','TbarBtoLminusNuB_2022EE','TBbartoLplusNuBbar_2022EE','TbarQtoLNu_2022EE','TQbartoLNu_2022EE','TbarWplusto2L2Nu_2022EE','TbarWplustoLNu2Q_2022EE','TWminusto2L2Nu_2022EE','TWminustoLNu2Q_2022EE']

    # valid_datasets = ['WW_2022EE','WZ_2022EE','ZZ_2022EE','TTto2L2Nu_2022EE','TTtoLNu2Q_2022EE','TTto4Q_2022EE']

    # valid_datasets = ['Zto2Nu_4Jets_HT100to200_2022EE','Zto2Nu_4Jets_HT200to400_2022EE','Zto2Nu_4Jets_HT400to800_2022EE','Zto2Nu_4Jets_HT800to1500_2022EE','Zto2Nu_4Jets_HT1500to2500_2022EE','Zto2Nu_4Jets_HT2500_2022EE']

    # valid_datasets = ['QCD_PT15to30_2022EE','QCD_PT30to50_2022EE','QCD_PT50to80_2022EE','QCD_PT80to120_2022EE','QCD_PT120to170_2022EE','QCD_PT170to300_2022EE','QCD_PT300to470_2022EE','QCD_PT470to600_2022EE','QCD_PT600to800_2022EE','QCD_PT800to1000_2022EE','QCD_PT1000to1400_2022EE','QCD_PT1400to1800_2022EE','QCD_PT1800to2400_2022EE','QCD_PT2400to3200_2022EE','QCD_PT3200_2022EE']

    # valid_datasets = ['DYJetsToLL_M50_2022','DYto2L_4jets_M10to50_2022','WToLNu_4Jets_2022','TbarBtoLminusNuB_2022','TBbartoLplusNuBbar_2022','TbarQtoLNu_2022','TQbartoLNu_2022','TbarWplusto2L2Nu_2022','TbarWplustoLNu2Q_2022','TWminusto2L2Nu_2022','TWminustoLNu2Q_2022','WW_2022','WZ_2022','ZZ_2022','TTto2L2Nu_2022','TTtoLNu2Q_2022','TTto4Q_2022']

    # valid_datasets = ['Zto2Nu_4Jets_HT100to200_2022','Zto2Nu_4Jets_HT200to400_2022','Zto2Nu_4Jets_HT400to800_2022','Zto2Nu_4Jets_HT800to1500_2022','Zto2Nu_4Jets_HT1500to2500_2022','Zto2Nu_4Jets_HT2500_2022','QCD_PT15to30_2022','QCD_PT30to50_2022','QCD_PT50to80_2022','QCD_PT80to120_2022','QCD_PT120to170_2022','QCD_PT170to300_2022','QCD_PT300to470_2022','QCD_PT470to600_2022','QCD_PT600to800_2022','QCD_PT800to1000_2022','QCD_PT1000to1400_2022','QCD_PT1400to1800_2022','QCD_PT1800to2400_2022','QCD_PT2400to3200_2022','QCD_PT3200_2022']

    # valid_datasets = ['TQbartoLNu_2022']

    # valid_datasets = ['DYJetsToLL_M50_2023','DYto2L_4jets_M10to50_2023','WToLNu_4Jets_2023','TbarBtoLminusNuB_2023','TBbartoLplusNuBbar_2023','TbarQtoLNu_2023','TQbartoLNu_2023','TbarWplusto2L2Nu_2023','TbarWplustoLNu2Q_2023','TWminusto2L2Nu_2023','TWminustoLNu2Q_2023','WW_2023','WZ_2023','ZZ_2023']

    valid_datasets = ['TTto2L2Nu_2023','TTtoLNu2Q_2023','TTto4Q_2023','Zto2Nu_4Jets_HT100to200_2023','Zto2Nu_4Jets_HT200to400_2023','Zto2Nu_4Jets_HT400to800_2023','Zto2Nu_4Jets_HT800to1500_2023','Zto2Nu_4Jets_HT1500to2500_2023','Zto2Nu_4Jets_HT2500_2023']

    # valid_datasets = ['QCD_PT15to30_2023','QCD_PT30to50_2023','QCD_PT50to80_2023','QCD_PT80to120_2023','QCD_PT120to170_2023','QCD_PT170to300_2023','QCD_PT300to470_2023','QCD_PT470to600_2023','QCD_PT600to800_2023','QCD_PT800to1000_2023','QCD_PT1000to1400_2023','QCD_PT1400to1800_2023','QCD_PT1800to2400_2023','QCD_PT2400to3200_2023','QCD_PT3200_2023']

    from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import dataset_names_bkgd_MiniAOD

    for dataset in dataset_names_bkgd_MiniAOD:
        if dataset in valid_datasets:
            config.Data.outputDatasetTag = dataset + '_ClosureTests_Fake'
            config.General.requestName = dataset + '_ClosureTests_Fake'
            config.Data.inputDataset = dataset_names_bkgd_MiniAOD[dataset]
            if not debug: forkAndSubmit(config)
            else:
                print(config.Data.outputDatasetTag)
                print(config.General.requestName)
                print(config.Data.inputDataset)
