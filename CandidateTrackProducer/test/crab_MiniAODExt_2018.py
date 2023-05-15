#!/usr/bin/env python3

import os
import sys

if os.environ["CMSSW_VERSION"] != "CMSSW_10_2_14":
    print "Please switch to CMSSW_10_2_14!"
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
config.JobType.maxMemoryMB = 3000
config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased' # for both MC and data
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1'

config.Site.storageSite = 'T2_US_Purdue'
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

    ## Do MC first

    config.Data.unitsPerJob = 10  # MC samples usually have ~150 events per lumi section
    # This parameter may need to be modified to avoid the 10K jobs limit.

    # DY
    config.Data.unitsPerJob = 4 # 3835 lumis
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-10to50'
    config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 100 # 100019 lumis
    config.General.requestName = 'candidateTrackProducer_DYToLL_M-50'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    # ZJetsToNuNu
    config.Data.unitsPerJob = 12 # 12245 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-100To200'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 30 # 29112 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-200To400'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 9678 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-400To600'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 9 # 9057 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-600To800'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 4 # 4323 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-800To1200'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 850 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-1200To2500'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 921 lumis
    config.General.requestName = 'candidateTrackProducer_ZJetsToNuNu_HT-2500ToInf'
    config.Data.inputDataset = '/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    # WJets
    config.Data.unitsPerJob = 25 # 25337 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu'
    config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
    #forkAndSubmit(config)

    # WJets_HT
    config.Data.unitsPerJob = 19 # 198621 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-70to100'
    config.Data.inputDataset = '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 294 # 294582 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-100To200'
    config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 43 # 43838 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-200To400'
    config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 78 # 78437 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-400To600'
    config.Data.inputDataset = '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 40 # 40588 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-600To800'
    config.Data.inputDataset = '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 151 # 151091 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-800To1200'
    config.Data.inputDataset = '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 73 # 73823 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-1200To2500'
    config.Data.inputDataset = '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 10460 lumis
    config.General.requestName = 'candidateTrackProducer_WJetsToLNu_HT-2500ToInf'
    config.Data.inputDataset = '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    # WW
    config.Data.unitsPerJob = 2 # 1584 lumis
    config.General.requestName = 'candidateTrackProducer_WW'
    config.Data.inputDataset = '/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
    #forkAndSubmit(config)

    # WZ
    config.Data.unitsPerJob = 3 # 3885 lumis
    config.General.requestName = 'candidateTrackProducer_WZ'
    config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v3/AODSIM'
    #forkAndSubmit(config)

    # ZZ
    config.Data.unitsPerJob = 1 # 283 lumis
    config.General.requestName = 'candidateTrackProducer_ZZ'
    config.Data.inputDataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
    #forkAndSubmit(config)

    # VG
    config.Data.unitsPerJob = 9 # 9937 lumis
    config.General.requestName = 'candidateTrackProducer_WG'
    config.Data.inputDataset = '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    # No acceptable ZG sample exist yet... Please check later.
    #'/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #'/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v1/AODSIM'

    # Single Top
    config.Data.unitsPerJob = 3 # 3334 lumis
    config.General.requestName = 'candidateTrackProducer_ST_s-channel'
    config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v4/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 154 # 1544703 lumis
    config.General.requestName = 'candidateTrackProducer_ST_t-channel_top'
    config.Data.inputDataset = '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 792 # 792636 lumis
    config.General.requestName = 'candidateTrackProducer_ST_t-channel_antitop'
    config.Data.inputDataset = '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 7 # 7819 lumis
    config.General.requestName = 'candidateTrackProducer_ST_tW_top'
    config.Data.inputDataset = '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v3/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 5 # 5970 lumis
    config.General.requestName = 'candidateTrackProducer_ST_tW_antitop'
    config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v3/AODSIM'
    #forkAndSubmit(config)

    # TTJets
    # 'TTJets' : a proper '/TT_TuneCP..." doesn't exist!
    config.Data.unitsPerJob = 12 # 12866 lumis
    config.General.requestName = 'candidateTrackProducer_TTTo2L2Nu'
    config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 20 # 20346 lumis
    config.General.requestName = 'candidateTrackProducer_TTToSemiLeptonic'
    config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 16 # 16770 lumis
    config.General.requestName = 'candidateTrackProducer_TTToHadronic'
    config.Data.inputDataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    # QCD
    #'QCD_5to10'       :  doesn't exist!
    #'QCD_10to15'      :  doesn't exist!
    config.Data.unitsPerJob = 2 # 2207 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_15to30'
    config.Data.inputDataset = '/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 4 # 4766 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_30to50'
    config.Data.inputDataset = '/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 2 # 1854
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_50to80'
    config.Data.inputDataset = '/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 2 # 1811
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_50to80_ext1'
    config.Data.inputDataset = '/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 5 # 5907 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_80to120'
    config.Data.inputDataset = '/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 5 # 5083 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_120to170'
    config.Data.inputDataset = '/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 6 # 5948 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_170to300'
    config.Data.inputDataset = '/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 10 # 10594 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_300to470'
    config.Data.inputDataset = '/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 4 # 4448 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_470to600'
    config.Data.inputDataset = '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 36 # 36396 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_470to600_ext1'
    config.Data.inputDataset = '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 21 # 21365 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_600to800'
    config.Data.inputDataset = '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 23 # 23569 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_800to1000_ext3'
    config.Data.inputDataset = '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext3-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 6 # 6167 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1000to1400'
    config.Data.inputDataset = '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 1080 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1400to1800'
    config.Data.inputDataset = '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 2 # 2392 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1400to1800_ext1'
    config.Data.inputDataset = '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 4 # 3805 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1800to2400'
    config.Data.inputDataset = '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 2 # 2622 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_1800to2400_ext1'
    config.Data.inputDataset = '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 720 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_2400to3200'
    config.Data.inputDataset = '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 477 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_2400to3200_ext1'
    config.Data.inputDataset = '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext1-v2/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 800 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_3200toInf'
    config.Data.inputDataset = '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM'
    #forkAndSubmit(config)

    config.Data.unitsPerJob = 1 # 63 lumis
    config.General.requestName = 'candidateTrackProducer_QCD_Pt_3200toInf_ext1'
    config.Data.inputDataset = '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_ext2-v2/AODSIM'
    #forkAndSubmit(config)

    #############################################################################################
    ## Data
    #############################################################################################

    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
    config.JobType.numCores = 8

    # Run2018A

    config.Data.outputDatasetTag = 'Run2018A-17Sep2018-v2'
    config.Data.unitsPerJob = 62 # 61133 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018A-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018A-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018A-17Sep2018-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018A-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018A-17Sep2018-v2/AOD'
    #forkAndSubmit(config)

    # Run2018B

    config.Data.outputDatasetTag = 'Run2018B-17Sep2018-v2'
    config.Data.unitsPerJob = 30 # 29913 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018B-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018B-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    # Run2018C

    config.Data.outputDatasetTag = 'Run2018C-17Sep2018-v2'
    config.Data.unitsPerJob = 28 # 27721 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018ABC_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018C-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018C-17Sep2018-v1/AOD'
    #forkAndSubmit(config)

    # Run2018D

    config.Data.outputDatasetTag = 'Run2018D-17Sep2018-v2'
    config.Data.unitsPerJob = 71 # 140735 lumis

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018D_METSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_MET_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/MET/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018D_TauSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_Tau_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/Tau/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018D_MuonSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_SingleMuon_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/SingleMuon/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)

    config.JobType.psetName    = 'candidateTrackProducer_RunMiniAOD_Data2018D_ElectronSkim_cfg.py'
    config.General.requestName = 'candidateTrackProducer_EGamma_Run2018D-17Sep2018'
    config.Data.inputDataset   = '/EGamma/Run2018D-PromptReco-v2/AOD'
    #forkAndSubmit(config)
