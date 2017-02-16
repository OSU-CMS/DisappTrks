# Crab script to copy files from one site to another
#
# Usage:
# $ python crab_copy.py

#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'copy_cfg.py'

config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite = 'T3_US_OSU'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################
    config.Data.outputDatasetTag = 'Run2015D-PromptReco-v3'
    config.General.requestName = 'copy_MET_2015D_PromptReco_v3'
    config.Data.inputDataset = '/MET/wulsin-Run2015D-PromptReco-v3-5e1b2f90f66dd8f324805a21b41c0bb6/USER'
    submit(config)

    config.General.requestName = 'copy_SingleMuon_2015D_PromptReco_v3'
    config.Data.inputDataset = '/SingleMuon/wulsin-Run2015D-PromptReco-v4-5e1b2f90f66dd8f324805a21b41c0bb6/USER'
    submit(config)

    config.General.requestName = 'copy_SingleElectron_2015D_PromptReco_v3'
    config.Data.inputDataset = '/SingleElectron/wulsin-Run2015D-PromptReco-v3-5e1b2f90f66dd8f324805a21b41c0bb6/USER'
    submit(config)

    config.Data.outputDatasetTag = 'Run2015D-PromptReco-v4'
    config.General.requestName = 'copy_MET_2015D_PromptReco_v4'
    config.Data.inputDataset = '/MET/wulsin-Run2015D-PromptReco-v4-5e1b2f90f66dd8f324805a21b41c0bb6/USER'
    submit(config)

    config.General.requestName = 'copy_SingleMuon_2015D_PromptReco_v4'
    config.Data.inputDataset = '/SingleMuon/wulsin-Run2015D-PromptReco-v4-5e1b2f90f66dd8f324805a21b41c0bb6/USER'
    submit(config)

    config.General.requestName = 'copy_SingleElectron_2015D_PromptReco_v4'
    config.Data.inputDataset = '/SingleElectron/wulsin-Run2015D-PromptReco-v4-5e1b2f90f66dd8f324805a21b41c0bb6/USER'
    submit(config)






