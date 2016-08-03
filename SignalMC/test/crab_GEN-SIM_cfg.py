#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = ''

config.Data.outputPrimaryDataset = ''
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15GS-MCRUN2_71_V1-v1'

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

    config.General.requestName = 'AMSB_chargino900GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino900GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-900_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino900GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino900GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-900_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino900GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino900GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-900_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino900GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino900GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-900_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino800GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino800GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-800_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino800GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino800GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-800_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino800GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino800GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-800_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino800GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino800GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-800_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino700GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino700GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-700_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino700GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino700GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-700_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino700GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino700GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-700_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino700GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino700GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-700_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino600GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino600GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-600_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino600GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino600GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-600_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino600GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino600GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-600_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino600GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino600GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-600_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino500GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino500GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-500_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino500GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino500GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-500_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino500GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino500GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-500_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino500GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino500GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-500_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino400GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino400GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-400_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino400GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino400GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-400_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino400GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino400GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-400_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino400GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino400GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-400_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino300GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino300GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-300_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino300GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino300GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-300_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino300GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino300GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-300_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino300GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino300GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-300_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino200GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino200GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-200_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino200GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino200GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-200_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino200GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino200GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-200_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino200GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino200GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-200_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino100GeV_ctau10000cm_step1'
    config.JobType.psetName = 'AMSB_chargino100GeV_ctau10000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-100_CTau-10000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino100GeV_ctau1000cm_step1'
    config.JobType.psetName = 'AMSB_chargino100GeV_ctau1000cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-100_CTau-1000_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino100GeV_ctau100cm_step1'
    config.JobType.psetName = 'AMSB_chargino100GeV_ctau100cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-100_CTau-100_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)

    config.General.requestName = 'AMSB_chargino100GeV_ctau10cm_step1'
    config.JobType.psetName = 'AMSB_chargino100GeV_ctau10cm_step1.py'
    config.Data.outputPrimaryDataset = 'AMSB_chargino_M-100_CTau-10_TuneZ2star_13TeV_pythia6'
    #forkAndSubmit(config)
