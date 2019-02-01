#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 94X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {

    # MET
    'MET_2017B' : "/MET/ahart-Run2017B-31Mar2018-v1-DisappTrks-v2-afd6bacb5bc8e2ef45f0b08cd350328e/USER",
    'MET_2017C' : "/MET/ahart-Run2017C-31Mar2018-v1-DisappTrks-v2-afd6bacb5bc8e2ef45f0b08cd350328e/USER",
    'MET_2017D' : "/MET/ahart-Run2017D-31Mar2018-v1-DisappTrks-v2-afd6bacb5bc8e2ef45f0b08cd350328e/USER",
    'MET_2017E' : "/MET/ahart-Run2017E-31Mar2018-v1-DisappTrks-v2-afd6bacb5bc8e2ef45f0b08cd350328e/USER",
    'MET_2017F' : "/MET/ahart-Run2017F-31Mar2018-v1-DisappTrks-v3-afd6bacb5bc8e2ef45f0b08cd350328e/USER",

    # SingleEle
    'SingleEle_2017B' : "/SingleElectron/bfrancis-Run2017B-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017C' : "/SingleElectron/bfrancis-Run2017C-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017D' : "/SingleElectron/bfrancis-Run2017D-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017E' : "/SingleElectron/bfrancis-Run2017E-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017F' : "/SingleElectron/bfrancis-Run2017F-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",

    # SingleMu
    'SingleMu_2017B' : "/SingleMuon/zpollock-Run2017B-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",
    'SingleMu_2017C' : "/SingleMuon/zpollock-Run2017C-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER", #only 99.6% of jobs
    'SingleMu_2017D' : "/SingleMuon/zpollock-Run2017D-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",
    'SingleMu_2017E' : "/SingleMuon/kwei-Run2017E-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",
    'SingleMu_2017F' : "/SingleMuon/bfrancis-Run2017F-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",

    # Tau
    'Tau_2017B' : "/Tau/bfrancis-Run2017B-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017C' : "/Tau/bfrancis-Run2017C-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017D' : "/Tau/bfrancis-Run2017D-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017E' : "/Tau/bfrancis-Run2017E-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017F' : "/Tau/bfrancis-Run2017F-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
}

dataset_names_bkgd = {
    # N.B. There is a RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1 campaign ongoing that should be used. 
    #      Pay attention and replace MiniAOD V1 samples when they show up.

    # TTJets
    # 'TTJets' : a proper "/TT_TuneCP..." doesn't exist!
    'TTJets_SemiLeptonic' : "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'TTJets_2L2Nu'        : "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER", # ???
    'TTJets_Hadronic'     : "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER", # ???

    # QCD
    'QCD_15to30'      : "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_30to50'      : "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_50to80'      : "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_80to120'     : "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_120to170'    : "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_170to300'    : "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_300to470'    : "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_470to600'    : "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_600to800'    : "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_800to1000'   : "/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_1000to1400'  : "/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-try3-de5f02ec0d0d96345889b201db21b7db/USER", # 97.8%% @ OSU
    'QCD_1400to1800'  : "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_1800to2400'  : "/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_2400to3200'  : "/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-try3-de5f02ec0d0d96345889b201db21b7db/USER", # 66.3% @ OSU
    'QCD_3200toInf'   : "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",

    'DYJetsToLL_50'                :  "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'DYJetsToLL_5to50'             :  "/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'SingleTop_s_channel'          :  "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'SingleTop_t_channel_antitop'  :  "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'SingleTop_t_channel_top'      :  "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'SingleTop_tW'                 :  "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'SingleTop_tbarW'              :  "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT100to200'        :  "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT200to400'        :  "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT200to400'        :  "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT200to400'        :  "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT600to800'        :  "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT800to1200'       :  "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu'                   :  "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WW'                           :  "/WW_TuneCP5_13TeV-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WZ'                           :  "/WZ_TuneCP5_13TeV-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT100to200'       :  "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT1200to2500'     :  "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT200to400'       :  "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT2500toInf'      :  "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT400to600'       :  "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT600to800'       :  "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT800to1200'      :  "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZZ'                           :  "/ZZ_TuneCP5_13TeV-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
}

dataset_names_sig = {
    'AMSB_chargino_100GeV_1cm_94X'     : "/AMSB_chargino_M-100_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_10cm_94X'    : "/AMSB_chargino_M-100_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_100cm_94X'   : "/AMSB_chargino_M-100_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_1000cm_94X'  : "/AMSB_chargino_M-100_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_10000cm_94X' : "/AMSB_chargino_M-100_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",

    'AMSB_chargino_200GeV_10000cm_94X' : "/AMSB_chargino_M-200_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_200GeV_1000cm_94X'  : "/AMSB_chargino_M-200_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_200GeV_100cm_94X'   : "/AMSB_chargino_M-200_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_200GeV_10cm_94X'    : "/AMSB_chargino_M-200_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_200GeV_1cm_94X'     : "/AMSB_chargino_M-200_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",

    'AMSB_chargino_300GeV_1cm_94X'     : "/AMSB_chargino_M-300_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_10cm_94X'    : "/AMSB_chargino_M-300_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_100cm_94X'   : "/AMSB_chargino_M-300_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_1000cm_94X'  : "/AMSB_chargino_M-300_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_10000cm_94X' : "/AMSB_chargino_M-300_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",

    'AMSB_chargino_400GeV_10000cm_94X' : "/AMSB_chargino_M-400_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_400GeV_1000cm_94X'  : "/AMSB_chargino_M-400_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_400GeV_100cm_94X'   : "/AMSB_chargino_M-400_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_400GeV_10cm_94X'    : "/AMSB_chargino_M-400_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_400GeV_1cm_94X'     : "/AMSB_chargino_M-400_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",

    'AMSB_chargino_500GeV_1cm_94X'     : "/AMSB_chargino_M-500_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_10cm_94X'    : "/AMSB_chargino_M-500_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_100cm_94X'   : "/AMSB_chargino_M-500_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_1000cm_94X'  : "/AMSB_chargino_M-500_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_10000cm_94X' : "/AMSB_chargino_M-500_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",

    'AMSB_chargino_600GeV_10000cm_94X' : "/AMSB_chargino_M-600_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_600GeV_1000cm_94X'  : "/AMSB_chargino_M-600_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_600GeV_100cm_94X'   : "/AMSB_chargino_M-600_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_600GeV_10cm_94X'    : "/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_600GeV_1cm_94X'     : "/AMSB_chargino_M-600_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",

    'AMSB_chargino_700GeV_1cm_94X'     : "/AMSB_chargino_M-700_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_10cm_94X'    : "/AMSB_chargino_M-700_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_1000cm_94X'  : "/AMSB_chargino_M-700_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_10000cm_94X' : "/AMSB_chargino_M-700_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",

    'AMSB_chargino_800GeV_10000cm_94X' : "/AMSB_chargino_M-800_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_800GeV_1000cm_94X'  : "/AMSB_chargino_M-800_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_800GeV_100cm_94X'   : "/AMSB_chargino_M-800_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_800GeV_10cm_94X'    : "/AMSB_chargino_M-800_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",
    'AMSB_chargino_800GeV_1cm_94X'     : "/AMSB_chargino_M-800_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER",

    'AMSB_chargino_900GeV_1cm_94X'     : "/AMSB_chargino_M-900_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_900GeV_10cm_94X'    : "/AMSB_chargino_M-900_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_900GeV_100cm_94X'   : "/AMSB_chargino_M-900_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_900GeV_1000cm_94X'  : "/AMSB_chargino_M-900_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_900GeV_10000cm_94X' : "/AMSB_chargino_M-900_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
}

dataset_names = {}
dataset_names.update (dataset_names_data)
dataset_names.update (dataset_names_bkgd)
dataset_names.update (dataset_names_sig)

import re

new_dataset_names = {}
for dataset0 in dataset_names:
    if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_.*', dataset0):
        continue
    mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_.*', r'\1', dataset0)
    ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_.*', r'\1', dataset0))
    suffix = re.sub (r'AMSB_chargino_[^_]*GeV_[^_]*cm_(.*)', r'\1', dataset0)
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

        new_dataset_names[dataset] = dataset_names[dataset0]

dataset_names.update (new_dataset_names)
