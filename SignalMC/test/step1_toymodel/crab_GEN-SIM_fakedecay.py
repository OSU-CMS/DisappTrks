#!/usr/bin/env python3

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = ''
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = ''
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 4000
NJOBS = 300  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
print getUsernameFromSiteDB()
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15GS-MCRUN2_71_V1-v1'

config.Site.storageSite = 'T2_US_Purdue'

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

    config.General.requestName = 'Fakedecay_chargino100GeV_ctau100cm_pt50GeV_neutralino40GeV_3bd_step1'
    config.JobType.psetName = 'Fakedecay_chargino100GeV_ctau100cm_pt50GeV_neutralino40GeV_3bd_step1.py'
    config.Data.outputPrimaryDataset = 'Fakedecay_chargino100GeV_ctau100cm_pt50GeV_neutralino40GeV_3bd_TuneZ2star_13TeV_pythia6'
    forkAndSubmit(config)

    config.General.requestName = 'Fakedecay_chargino100GeV_ctau100cm_pt60GeV_neutralino40GeV_3bd_step1'
    config.JobType.psetName = 'Fakedecay_chargino100GeV_ctau100cm_pt60GeV_neutralino40GeV_3bd_step1.py'
    config.Data.outputPrimaryDataset = 'Fakedecay_chargino100GeV_ctau100cm_pt60GeV_neutralino40GeV_3bd_TuneZ2star_13TeV_pythia6'
    forkAndSubmit(config)

    config.General.requestName = 'Fakedecay_chargino100GeV_ctau100cm_pt70GeV_neutralino40GeV_3bd_step1'
    config.JobType.psetName = 'Fakedecay_chargino100GeV_ctau100cm_pt70GeV_neutralino40GeV_3bd_step1.py'
    config.Data.outputPrimaryDataset = 'Fakedecay_chargino100GeV_ctau100cm_pt70GeV_neutralino40GeV_3bd_TuneZ2star_13TeV_pythia6'
    forkAndSubmit(config)

    config.General.requestName = 'Fakedecay_chargino100GeV_ctau100cm_pt80GeV_neutralino40GeV_3bd_step1'
    config.JobType.psetName = 'Fakedecay_chargino100GeV_ctau100cm_pt80GeV_neutralino40GeV_3bd_step1.py'
    config.Data.outputPrimaryDataset = 'Fakedecay_chargino100GeV_ctau100cm_pt80GeV_neutralino40GeV_3bd_TuneZ2star_13TeV_pythia6'
    forkAndSubmit(config)

    config.General.requestName = 'Fakedecay_chargino100GeV_ctau100cm_pt90GeV_neutralino40GeV_3bd_step1'
    config.JobType.psetName = 'Fakedecay_chargino100GeV_ctau100cm_pt90GeV_neutralino40GeV_3bd_step1.py'
    config.Data.outputPrimaryDataset = 'Fakedecay_chargino100GeV_ctau100cm_pt90GeV_neutralino40GeV_3bd_TuneZ2star_13TeV_pythia6'
    forkAndSubmit(config)

