#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'AMSB_chargino_step2_cfg.py'

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15GS-MCRUN2_71_V1-v3_step2'

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

    config.General.requestName = 'AMSB_chargino900GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-900_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-9be42cee2e08d751ff195ac87d1d151d/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino800GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-800_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-b0e57e752f3cbca910deefd391deeca3/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino700GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-700_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-a219c2edcf40f2199ac70bc9eaf2b73b/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino600GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-600_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-4e220d81cd27aadcf6f00d707de24868/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino500GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-500_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-bcff589125d95f9bed54d9c09385b725/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino400GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-400_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-0dd8ac90fa6d462cb1f41c50299b5e48/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino300GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-300_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-2a84f4655311d149154d1e41c9f2a36a/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino200GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-200_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-7c46c12cca755f7ab1d10ada1218c2b5/USER'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino100GeV_ctau10000cm_step2'
    config.Data.inputDataset = '/AMSB_chargino_M-100_CTau-10000_TuneZ2star_13TeV_pythia6/bfrancis-RunIISummer15GS-MCRUN2_71_V1-v2-d0b1d9b93bb96afce67dc8aa5305a14c/USER'
    #forkAndSubmit(config)
