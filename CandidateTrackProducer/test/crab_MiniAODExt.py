#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_cfg.py'

config.Data.inputDataset = ''
config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-DisappearingTracks-v1'
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt'
# 2.46 /fb from https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/2544.html

#config.Site.storageSite = 'T3_US_OSU'
config.Site.storageSite = 'T2_US_Purdue'

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

    ## Do MC first  
    config.JobType.pyCfgParams = ['runOnMC=1']  

    # config.General.requestName = 'candidateTrackProducer_DYToLL'
    # config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_DYToNuNu'
    # config.Data.inputDataset = '/DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WToLNu'
    # config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WWToLNuQQ'
    # config.Data.inputDataset = '/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WWToLNuLNu'
    # config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLNuQQ'
    # config.Data.inputDataset = '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLLQQ'
    # config.Data.inputDataset = '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLNuNuNu'
    # config.Data.inputDataset = '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLLLNu'
    # config.Data.inputDataset = '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToNuNuQQ'
    # config.Data.inputDataset = '/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToLLQQ'
    # config.Data.inputDataset = '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToLLNuNu'
    # config.Data.inputDataset = '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToLLLL'
    # config.Data.inputDataset = '/ZZTo4L_13TeV_powheg_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_WG'
    # config.Data.inputDataset = '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_ZG'
    # config.Data.inputDataset = '/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_TTbarToLFromT'
    # config.Data.inputDataset = '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_TTbarToLFromTbar'
    # config.Data.inputDataset = '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_TTbarToLL'
    # config.Data.inputDataset = '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_TW'
    # config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_TbarW'
    # config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleT_s-channel'
    # config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # submit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleT_t-channel'
    # config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # submit(config)

##########################################################################
    ## Now do data 
    ## Warning:  changing pyCfgParams may trigger an error.  See for documentation:
    ## https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Multiple_submission_fails_with_a  
    config.Data.splitting = 'LumiBased' 
    config.JobType.pyCfgParams = ['runOnMC=0']  

    config.Data.outputDatasetTag = 'Run2015D-05Oct2015-v1'  

    config.General.requestName = 'candidateTrackProducer_MET_2015D_05Oct2015'  
    config.Data.inputDataset = '/MET/Run2015D-05Oct2015-v1/MINIAOD' 
    submit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2015D_05Oct2015'  
    config.Data.inputDataset = '/SingleMuon/Run2015D-05Oct2015-v1/MINIAOD' 
    submit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2015D_05Oct2015'  
    config.Data.inputDataset = '/SingleElectron/Run2015D-05Oct2015-v1/MINIAOD'  
    submit(config)

    config.Data.useParent = False
    config.Data.outputDatasetTag = 'Run2015D-PromptReco-v4' 

    config.General.requestName = 'candidateTrackProducer_MET_2015D_PromptRecov4'  
    config.Data.inputDataset = '/MET/Run2015D-PromptReco-v4/MINIAOD' # Parent is /MET/Run2015D-v1/RAW
    config.Data.secondaryInputDataset = '/MET/Run2015D-PromptReco-v4/AOD' # This may not work; see https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters 
    submit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2015D_PromptRecov4'   
    config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v4/MINIAOD' 
    submit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2015D_PromptRecov4'  
    config.Data.inputDataset = '/SingleElectron/Run2015D-PromptReco-v4/MINIAOD'  
    submit(config)




