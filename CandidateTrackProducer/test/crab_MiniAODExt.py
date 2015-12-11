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
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-DisappearingTracks-v1'

#config.Site.storageSite = 'T3_US_OSU'
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

    ## Do MC first  
    config.JobType.pyCfgParams = ['runOnMC=1']  

    config.Data.unitsPerJob = 10  # MC samples usually have ~150 events per lumi section
    # This parameter may need to be modified to avoid the 10K jobs limit.  


    # config.General.requestName = 'candidateTrackProducer_DYToLL'
    # config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_DYToNuNu'
    # config.Data.inputDataset = '/DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WToLNu'
    # config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WToLNu_HT100To200'
    # config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM' 
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WToLNu_HT200To400'
    # config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM' 
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WToLNu_HT400To600'
    # config.Data.inputDataset = '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WToLNu_HT600ToInf'
    # config.Data.inputDataset = '/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'  
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WWToLNuQQ'
    # config.Data.inputDataset = '/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WWToLNuLNu'
    # config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLNuQQ'
    # config.Data.inputDataset = '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLLQQ'
    # config.Data.inputDataset = '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLNuNuNu'
    # config.Data.inputDataset = '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WZToLLLNu'
    # config.Data.inputDataset = '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToNuNuQQ'
    # config.Data.inputDataset = '/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToLLQQ'
    # config.Data.inputDataset = '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToLLNuNu'
    # config.Data.inputDataset = '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_ZZToLLLL'
    # config.Data.inputDataset = '/ZZTo4L_13TeV_powheg_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_WG'
    # config.Data.inputDataset = '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_ZG'
    # config.Data.inputDataset = '/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_TTbarToLFromT'
    # config.Data.inputDataset = '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_TTbarToLFromTbar'
    # config.Data.inputDataset = '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_TTbarToLL'
    # config.Data.inputDataset = '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_TW'
    # config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_TbarW'
    # config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleT_s-channel'
    # config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleT_t-channel'
    # config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1/MINIAODSIM'
    # forkAndSubmit(config)

##########################################################################
    ## Now do data 
    config.Data.useParent = False  # This does not yet work; see https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/1168/1.html  
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_cfg.py' 
    config.Data.splitting = 'LumiBased' 
    config.JobType.pyCfgParams = ['runOnMC=0']  
    ## Warning:  changing pyCfgParams may trigger an error.  See for documentation:
    ## https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Multiple_submission_fails_with_a  

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt'
    # 2.46 /fb from https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/2544.html

    config.Data.unitsPerJob = 2
    config.Data.outputDatasetTag = 'Run2015D-PromptReco-v3' 

    # config.General.requestName = 'candidateTrackProducer_MET_2015D_PromptReco_v3'  
    # config.Data.inputDataset = '/MET/Run2015D-PromptReco-v3/AOD' 
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleMuon_2015D_PromptReco_v3'   
    # config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v3/AOD' 
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleElectron_2015D_PromptReco_v3'  
    # config.Data.inputDataset = '/SingleElectron/Run2015D-PromptReco-v3/AOD'  
    # forkAndSubmit(config)

    config.Data.unitsPerJob = 3
    config.Data.outputDatasetTag = 'Run2015D-PromptReco-v4' 
    # config.General.requestName = 'candidateTrackProducer_MET_2015D_PromptReco_v4'  
    # config.Data.inputDataset = '/MET/Run2015D-PromptReco-v4/AOD' 
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleMuon_2015D_PromptReco_v4'   
    # config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v4/AOD' 
    # forkAndSubmit(config)

    # config.General.requestName = 'candidateTrackProducer_SingleElectron_2015D_PromptReco_v4'  
    # config.Data.inputDataset = '/SingleElectron/Run2015D-PromptReco-v4/AOD'  
    # forkAndSubmit(config)






