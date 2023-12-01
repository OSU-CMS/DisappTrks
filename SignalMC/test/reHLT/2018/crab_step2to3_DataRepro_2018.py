#!/usr/bin/env python3

import os
import sys

#if os.environ["CMSSW_VERSION"] != "CMSSW_10_2_14":
#    print "Please switch to CMSSW_10_2_14!"
#    sys.exit (0)

from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DATA_step2to3_2018_cfg.py'  # For MC only
config.JobType.allowUndistributedCMSSW = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 8000
config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
#config.Data.outLFNDirBase = '/store/user/kwei/'# % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1'

#config.Site.storageSite = 'T2_US_Purdue'
#config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T3_US_Rutgers'
#config.Site.storageSite = 'T2_CH_CERN'

###### ignore locality
#config.Data.ignoreLocality = True
#config.Site.whitelist =  ['T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_CH_CERN', 'T2_CH_CSCS', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FR_CCIN2P3', 'T2_FR_GRIF_IRFU', 'T2_FR_GRIF_LLR', 'T2_FR_IPHC', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome', 'T2_PT_NCG_Lisbon', 'T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol', 'T2_UK_SGrid_RALPP']
#config.Site.whitelist =  ['T1_US_*', 'T2_US_*', 'T3_US_*']
#config.Site.whitelist = ["T1_DE_KIT", "T1_ES_PIC", "T1_FR_CCIN2P3", "T1_IT_CNAF", "T1_UK_RAL", "T2_AT_Vienna", "T2_BE_IIHE", "T2_BE_UCL", "T2_CH_CERN", "T2_CH_CERN_AI", "T2_CH_CERN_HLT", "T2_CH_CSCS", "T2_DE_DESY", "T2_DE_RWTH", "T2_EE_Estonia", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_FI_HIP", "T2_FR_CCIN2P3", "T2_FR_GRIF_IRFU", "T2_FR_GRIF_LLR", "T2_FR_IPHC", "T2_GR_Ioannina", "T2_HU_Budapest", "T2_IT_Bari", "T2_IT_Legnaro", "T2_IT_Pisa", "T2_IT_Rome", "T2_PL_Swierk", "T2_PL_Warsaw", "T2_PT_NCG_Lisbon", "T2_UA_KIPT", "T2_UK_London_Brunel", "T2_UK_London_IC", "T2_UK_SGrid_Bristol", "T2_UK_SGrid_RALPP", "T3_BG_UNI_SOFIA", "T3_BY_NCPHEP", "T3_CH_CERN_CAF", "T3_CH_CERN_DOMA", "T3_CH_PSI", "T3_FR_IPNL", "T3_HU_Debrecen", "T3_IT_Bologna", "T3_IT_Perugia", "T3_IT_Trieste", "T3_UK_London_QMUL", "T3_UK_London_RHUL", "T3_UK_SGrid_Oxford", "T3_UK_ScotGrid_GLA"]

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


    #############################################################################################
    ## Data
    #############################################################################################

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
    config.JobType.numCores = 8

    # RERUN Run2018A

    config.Data.outputDatasetTag = 'Run2018A-102X_dataRun2_v12-v3'
    config.Data.unitsPerJob  =  3

    config.JobType.psetName     = 'DATA_step2to3_2018_cfg.py'
    config.General.requestName  = 'reprocess_SingleMu_Run2018A-17Jun2020v1'
    config.Data.inputDataset    = '/SingleMuon/Run2018A-v1/RAW'
    config.Data.runRange        = '315252,315255,316716,316715,316702,316701,316700,316667,316666,316665,316664,316638,316200'
    #forkAndSubmit(config)


