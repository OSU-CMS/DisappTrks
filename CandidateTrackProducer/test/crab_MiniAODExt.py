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

    ## Do MC first
    config.JobType.pyCfgParams = ['runOnMC=1']

    config.Data.unitsPerJob = 10  # MC samples usually have ~150 events per lumi section
    # This parameter may need to be modified to avoid the 10K jobs limit.


    config.General.requestName = 'candidateTrackProducer_DYToLL'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_DYToLL_M-5to50'
    config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_DYToLL_M-5to50_ext1'
    config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-100to200'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-200to400'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-400to600'
    config.Data.inputDataset = '' # not yet available
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-600toInf'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-100to200'
    config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-200to400'
    config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-400to600'
    config.Data.inputDataset = '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-600toInf'
    config.Data.inputDataset = '/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WWToLNuQQ'
    config.Data.inputDataset = '/WWToLNuQQ_13TeV-powheg/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WWToLNuLNu'
    config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WZ'
    config.Data.inputDataset = '/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_ZZ'
    config.Data.inputDataset = '/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_WG'
    config.Data.inputDataset = '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_ZG'
    config.Data.inputDataset = '/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_TTbar'
    config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_TW'
    config.Data.inputDataset = '/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_TbarW'
    config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleT_s-channel'
    config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleT_t-channel'
    config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleT_t-channel_ext1'
    config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM'
    #forkAndSubmit(config)

##########################################################################
    ## Now do data
    config.JobType.pyCfgParams = ['runOnMC=0']
    ## Warning:  changing pyCfgParams may trigger an error.  See for documentation:
    ## https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Multiple_submission_fails_with_a

    config.Data.splitting = 'LumiBased'
    config.Data.unitsPerJob = 4
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2.txt'
    config.Data.outputDatasetTag = 'Run2015D-16Dec2015-v1-DisappTrks-v1'

    config.Site.storageSite = 'T2_US_Purdue'

    config.General.requestName = 'candidateTrackProducer_MET_2015D_16Dec2015'
    config.Data.inputDataset = '/MET/Run2015D-16Dec2015-v1/MINIAOD'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2015D_16Dec2015'
    config.Data.inputDataset = '/SingleMuon/Run2015D-16Dec2015-v1/MINIAOD'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2015D_16Dec2015'
    config.Data.inputDataset = '/SingleElectron/Run2015D-16Dec2015-v1/MINIAOD'
    #forkAndSubmit(config)
