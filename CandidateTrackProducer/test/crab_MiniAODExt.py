#!/usr/bin/env python3

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC_cfg.py'  # For MC only

config.Data.inputDataset = ''
config.Data.useParent = False
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

    config.Data.unitsPerJob = 10  # MC samples usually have ~150 events per lumi section
    # This parameter may need to be modified to avoid the 10K jobs limit.


    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_DYToLL'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 20  # big sample
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-5to50'
    config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 40  # very big sample
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-5to50_ext1'
    config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-100to200'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-200to400'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-400to600'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_DYToNuNu_HT-600toInf'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-100to200'
    config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-200to400'
    config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-400to600'
    config.Data.inputDataset = '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-600toInf'
    config.Data.inputDataset = '/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-600to800'
    config.Data.inputDataset = '/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-800to1200'
    config.Data.inputDataset = '/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-1200to2500'
    config.Data.inputDataset = '/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WToLNu_HT-2500toInf'
    config.Data.inputDataset = '/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 30  # very big sample
    config.General.requestName = 'candidateTrackProducer_WToLNu'
    config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WWToLNuQQ'
    config.Data.inputDataset = '/WWToLNuQQ_13TeV-powheg/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WWToLNuLNu'
    config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WZ'
    config.Data.inputDataset = '/WZ_TuneCUETP8M1_13TeV-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_ZZ'
    config.Data.inputDataset = '/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_WG'
    config.Data.inputDataset = '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_ZG'
    config.Data.inputDataset = '/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 50  # very big sample
    config.General.requestName = 'candidateTrackProducer_TTbar'
    config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_TW'
    config.Data.inputDataset = '/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_TbarW'
    config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_SingleT_s-channel'
    config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_SingleT_t-channel'
    config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_SingleT_t-channel_ext1'
    config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_5to10'
    config.Data.inputDataset = '/QCD_Pt_5to10_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_10to15'
    config.Data.inputDataset = '/QCD_Pt_10to15_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_15to30'
    config.Data.inputDataset = '/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_30to50'
    config.Data.inputDataset = '/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_50to80'
    config.Data.inputDataset = '/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_80to120'
    config.Data.inputDataset = '/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_120to170'
    config.Data.inputDataset = '/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_170to300'
    config.Data.inputDataset = '/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_300to470'
    config.Data.inputDataset = '/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_470to600'
    config.Data.inputDataset = '/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_600to800'
    config.Data.inputDataset = '/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_800to1000'
    config.Data.inputDataset = '/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1000to1400'
    config.Data.inputDataset = '/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1400to1800'
    config.Data.inputDataset = '/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1800to2400'
    config.Data.inputDataset = '/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_2400to3200'
    config.Data.inputDataset = '/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_3200toInf'
    config.Data.inputDataset = '/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
    #forkAndSubmit(config)


##########################################################################
    ## Now do data
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data_cfg.py'

    config.Data.unitsPerJob = 4
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_v2.txt'
    config.Data.outputDatasetTag = 'Run2015D-16Dec2015-v1-DisappTrks-v1'

    config.Site.storageSite = 'T2_US_Purdue'


    config.General.requestName = 'candidateTrackProducer_MET_2015D_16Dec2015'
    config.Data.inputDataset = '/MET/Run2015D-16Dec2015-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2015D_16Dec2015'
    config.Data.inputDataset = '/SingleMuon/Run2015D-16Dec2015-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2015D_16Dec2015'
    config.Data.inputDataset = '/SingleElectron/Run2015D-16Dec2015-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2015D_16Dec2015'
    config.Data.inputDataset = '/Tau/Run2015D-16Dec2015-v1/AOD'
    config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_Data_TauSkim_cfg.py'
    #forkAndSubmit(config)
