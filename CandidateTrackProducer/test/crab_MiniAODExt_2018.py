#!/usr/bin/env python

import os
import sys

if os.environ["CMSSW_VERSION"] != "CMSSW_10_2_11_patch1":
    print "Please switch to CMSSW_10_2_11_patch1!"
    sys.exit (0)

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'candidateTrackProducer_RunMiniAOD_MC2018_cfg.py'  # For MC only
config.JobType.allowUndistributedCMSSW = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 2500
config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2'

#config.Site.storageSite = 'T2_US_Purdue'
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T3_US_Rutgers'
#config.Site.storageSite = 'T2_CH_CERN'

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

    # DY
    config.Data.unitsPerJob = 10 # 9871 lumis
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-5to50'
    config.Data.inputDataset = '/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 54 # 53321 lumis
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-50'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-RECOSIMstep_94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 50 # 49283 lumis
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-50_ext1'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    # ZJetsToNuNu
    config.Data.unitsPerJob = 27 # 26223 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-100To200'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 26 # 25284 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-200To400'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 18 # 17663 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-400To600'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 12 # 11254 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-600To800'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 3 # 2772 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-800To1200'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 613 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-1200To2500'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 13 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-2500ToInf'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    # WJets
    config.Data.unitsPerJob = 29 # 28284 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu'
    config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 48 # 47711 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_ext1'
    config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    # WJets_HT
    config.Data.unitsPerJob = 364 # 363157 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-100To200'
    config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 17 # 16504 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-200To400'
    config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 190 # 189374 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-400To600'
    config.Data.inputDataset = '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 193 # 192463 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-600To800'
    config.Data.inputDataset = '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 192 # 191075 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-800To1200'
    config.Data.inputDataset = '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 195 # 194344 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-1200To2500'
    config.Data.inputDataset = '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 157 # 156763 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-2500ToInf'
    config.Data.inputDataset = '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v3/AODSIM'
    #forkAndSubmit(config)

    # WW
    config.Data.unitsPerJob = 8 # 7923 lumis
    config.General.requestName = 'candidateTrackProducer_WW'
    config.Data.inputDataset = '/WW_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    # WZ
    config.Data.unitsPerJob = 5 # 4294 lumis
    config.General.requestName = 'candidateTrackProducer_WZ'
    config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    # ZZ
    config.Data.unitsPerJob = 3 # 2174 lumis
    config.General.requestName = 'candidateTrackProducer_ZZ'
    config.Data.inputDataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    # VG
    # No acceptable WG or ZG samples exist yet... Please check later.

    # Single Top
    config.Data.unitsPerJob = 12 # 11646 lumis
    config.General.requestName = 'candidateTrackProducer_ST_s-channel'
    config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 11 # 10461 lumis
    config.General.requestName = 'candidateTrackProducer_ST_t-channel_top'
    config.Data.inputDataset = '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 7 # 6733 lumis
    config.General.requestName = 'candidateTrackProducer_ST_t-channel_antitop'
    config.Data.inputDataset = '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 6 # 5541 lumis
    config.General.requestName = 'candidateTrackProducer_ST_tW_top'
    config.Data.inputDataset = '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 6 # 5710 lumis
    config.General.requestName = 'candidateTrackProducer_ST_tW_antitop'
    config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 7 # 6017 lumis
    config.General.requestName = 'candidateTrackProducer_ST_tW_antitop_ext1'
    config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10_ext1-v1/AODSIM'
    #forkAndSubmit(config)

    # TTJets
    # 'TTJets' : a proper '/TT_TuneCP..." doesn't exist!
    config.Data.unitsPerJob = 10 # 8989 lumis
    config.General.requestName = 'candidateTrackProducer_TTTo2L2Nu'
    config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 47 # 46603 lumis
    config.General.requestName = 'candidateTrackProducer_TTToSemiLeptonic'
    config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 63 # 62795 lumis
    config.General.requestName = 'candidateTrackProducer_TTToHadronic'
    config.Data.inputDataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    # QCD
    #'QCD_5to10'       :  doesn't exist!
    #'QCD_10to15'      :  doesn't exist!
    config.Data.unitsPerJob = 21 # 20481 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_15to30'
    config.Data.inputDataset = '/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 23 # 22144 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_30to50'
    config.Data.inputDataset = '/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 21507
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_50to80'
    config.Data.inputDataset = '/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 33 # 32248 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_80to120'
    config.Data.inputDataset = '/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 35 # 34151 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_120to170'
    config.Data.inputDataset = '/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 45 # 44175 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_170to300'
    config.Data.inputDataset = '/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 61 # 60698 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_300to470'
    config.Data.inputDataset = '/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 29 # 28016 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_470to600'
    config.Data.inputDataset = '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 77 # 76505 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_600to800'
    config.Data.inputDataset = '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 50 # 49734 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_800to1000'
    config.Data.inputDataset = '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 24 # 23610 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1000to1400'
    config.Data.inputDataset = '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 7514 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1400to1800'
    config.Data.inputDataset = '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 3114 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1800to2400'
    config.Data.inputDataset = '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 3289 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_2400to3200'
    config.Data.inputDataset = '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 1080 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_3200toInf'
    config.Data.inputDataset = '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v1/AODSIM'
    #forkAndSubmit(config)

    #############################################################################################
    ## Data
    #############################################################################################

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'

    # The AOD re-reco is labeled 17Nov17, however the re-reco campaign is labeled 31Mar2018

    # Run2017B-v1

    config.Data.outputDatasetTag = 'Run2017B-31Mar2018-v1-DisappTrks-v2'
    config.Data.unitsPerJob = 27 # 26559 lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017B-31Mar2018-v1'
    config.Data.inputDataset   = '/MET/Run2017B-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017B-31Mar2018-v1'
    config.Data.inputDataset   = '/Tau/Run2017B-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017B-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleMuon/Run2017B-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017B-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleElectron/Run2017B-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2017C-v1

    config.Data.outputDatasetTag = 'Run2017C-31Mar2018-v1-DisappTrks-v2'
    config.Data.unitsPerJob = 58 # 57761 lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017C-31Mar2018-v1'
    config.Data.inputDataset   = '/MET/Run2017C-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017C-31Mar2018-v1'
    config.Data.inputDataset   = '/Tau/Run2017C-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017C-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleMuon/Run2017C-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017C-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleElectron/Run2017C-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2017D-v1

    config.Data.outputDatasetTag = 'Run2017D-31Mar2018-v1-DisappTrks-v2'
    config.Data.unitsPerJob = 29 # 28337 lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017D-31Mar2018-v1'
    config.Data.inputDataset   = '/MET/Run2017D-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017D-31Mar2018-v1'
    config.Data.inputDataset   = '/Tau/Run2017D-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017D-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleMuon/Run2017D-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017D-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleElectron/Run2017D-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2017E-v1

    config.Data.outputDatasetTag = 'Run2017E-31Mar2018-v1-DisappTrks-v2'
    config.Data.unitsPerJob = 46 # 45460 lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017E-31Mar2018-v1'
    config.Data.inputDataset   = '/MET/Run2017E-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017E-31Mar2018-v1'
    config.Data.inputDataset   = '/Tau/Run2017E-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017E-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleMuon/Run2017E-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017E-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleElectron/Run2017E-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)

    # Run2017F-v1

    config.Data.outputDatasetTag = 'Run2017F-31Mar2018-v1-DisappTrks-v2'
    config.Data.unitsPerJob = 31 # 61275 lumis

    config.General.requestName = 'candidateTrackProducer_MET_2017F-31Mar2018-v1'
    config.Data.inputDataset   = '/MET/Run2017F-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_METSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_Tau_2017F-31Mar2018-v1'
    config.Data.inputDataset   = '/Tau/Run2017F-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_TauSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleMuon_2017F-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleMuon/Run2017F-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_MuonSkim_cfg.py'
    #forkAndSubmit(config)

    config.General.requestName = 'candidateTrackProducer_SingleElectron_2017F-31Mar2018-v1'
    config.Data.inputDataset   = '/SingleElectron/Run2017F-17Nov2017-v1/AOD'
    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2017_ElectronSkim_cfg.py'
    #forkAndSubmit(config)
