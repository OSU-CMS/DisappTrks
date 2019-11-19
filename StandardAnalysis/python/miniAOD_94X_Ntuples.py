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
    'TTJets_2L2Nu'        : "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER", # about 60% done, give it the weekend
    'TTJets_Hadronic'     : "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER", # ~10% done...

    # QCD
    'QCD_15to30'      : "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_30to50'      : "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_50to80'      : "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_80to120'     : "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_120to170'    : "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_170to300'    : "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_300to470'    : "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_470to600'    : "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-try3-de5f02ec0d0d96345889b201db21b7db/USER", # @ 35.1% @ OSU
    'QCD_600to800'    : "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_800to1000'   : "/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_1000to1400'  : "/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-try3-de5f02ec0d0d96345889b201db21b7db/USER", # 97.8% @ OSU
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
    'WJetsToLNu_HT400to600'        :  "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT600to800'        :  "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu_HT800to1200'       :  "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    #'WJetsToLNu_HT1200to2500'      :
    'WJetsToLNu_HT2500toInf'       :  "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WJetsToLNu'                   :  "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WW'                           :  "/WW_TuneCP5_13TeV-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'WZ'                           :  "/WZ_TuneCP5_13TeV-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT100to200'       :  "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT200to400'       :  "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT400to600'       :  "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT600to800'       :  "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT800to1200'      :  "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT1200to2500'     :  "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZJetsToNuNu_HT2500toInf'      :  "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'ZZ'                           :  "/ZZ_TuneCP5_13TeV-pythia8/ahart-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
}

bkgd_crabSeen = { # run framework job with CandidateTrackProducer/test/analyzeSkimCutFlow.py, use -j 1 for one job per file
    "DYJetsToLL_5to50"            : 8872686.0,
    "DYJetsToLL_50"               : 97938808.0,
    "ZJetsToNuNu_HT100to200"      : 22880098.0,
    "ZJetsToNuNu_HT200to400"      : 21722423.0,
    "ZJetsToNuNu_HT400to600"      : 9784358.0,
    "ZJetsToNuNu_HT600to800"      : 5320715.0,
    "ZJetsToNuNu_HT800to1200"     : 2056072.0,
    "ZJetsToNuNu_HT1200to2500"    : 362910.0,
    "ZJetsToNuNu_HT2500toInf"     : 6734.0,
    #WJetsToLNu
    "WJetsToLNu_HT100to200"       : 32798545.0,
    "WJetsToLNu_HT200to400"       : 7470850.0,
    "WJetsToLNu_HT400to600"       : 14188270.0,
    "WJetsToLNu_HT600to800"       : 226135.0,
    "WJetsToLNu_HT800to1200"      : 748930.0,
    # 1200to2500
    "WJetsToLNu_HT2500toInf"      : 304113.0,
    "WW"                          : 7791498.0,
    "WZ"                          : 3928630.0,
    "ZZ"                          : 1949768.0,
    "SingleTop_s_channel"         : 9592285.0,
    "SingleTop_t_channel_top"     : 5865875.0,
    "SingleTop_t_channel_antitop" : 3939990.0,
    "SingleTop_tW"                : 4898094.0,
    "SingleTop_tbarW"             : 11502515.0,
    "TTJets_2L2Nu"                : 61047620.0,
    "TTJets_SemiLeptonic"         : 41203181.0,
    "TTJets_Hadronic"             : 42756552.0,
    "QCD_15to30"                  : 19965965.0,
    "QCD_30to50"                  : 19947765.0,
    "QCD_50to80"                  : 19291423.0,
    "QCD_80to120"                 : 28824064.0,    
    "QCD_120to170"                : 26858626.0,
    "QCD_170to300"                : 29854232.0,
    "QCD_300to470"                : 53900458.0,
    "QCD_470to600"                : 9795684.0,
    "QCD_600to800"                : 60461924.0,
    "QCD_800to1000"               : 4664088.0,
    "QCD_1000to1400"              : 19190760.0,
    "QCD_1400to1800"              : 5685270.0,    
    "QCD_1800to2400"              : 2983915.0,
    "QCD_2400to3200"              : 1228744.0,    
    "QCD_3200toInf"               : 757837.0,
}

bkgd_crabSkimmed = { # taken from DAS, checked with framework jobs' datasetInfo files
    "DYJetsToLL_5to50"            : 3330,
    "DYJetsToLL_50"               : 31383830,
    "ZJetsToNuNu_HT100to200"      : 1753723,
    "ZJetsToNuNu_HT200to400"      : 6233463,
    "ZJetsToNuNu_HT400to600"      : 3971362,
    "ZJetsToNuNu_HT600to800"      : 2398370,
    "ZJetsToNuNu_HT1200to2500"    : 202618,
    "ZJetsToNuNu_HT800to1200"     : 1013793,
    "ZJetsToNuNu_HT2500toInf"     : 4392,
    "WJetsToLNu"                  : 13059223,
    "WJetsToLNu_HT100to200"       : 9826611,
    "WJetsToLNu_HT200to400"       : 3018479,
    "WJetsToLNu_HT400to600"       : 6845079,
    "WJetsToLNu_HT600to800"       : 117800,
    "WJetsToLNu_HT800to1200"      : 415458,
    # 1200to2500
    "WJetsToLNu_HT2500toInf"      : 215040,
    "WW"                          : 1341501,
    "WZ"                          : 567018,
    "ZZ"                          : 228870,
    "SingleTop_s_channel"         : 2750749,
    "SingleTop_t_channel_top"     : 619647,
    "SingleTop_t_channel_antitop" : 423939,
    "SingleTop_tW"                : 2242909,
    "SingleTop_tbarW"             : 5259432,
    "TTJets_2L2Nu"                : 37400815,
    "TTJets_SemiLeptonic"         : 16489701,
    "TTJets_Hadronic"             : 194873,
    "QCD_15to30"                  : 181,
    "QCD_30to50"                  : 497,
    "QCD_50to80"                  : 1861,
    "QCD_80to120"                 : 5954,
    "QCD_120to170"                : 12398,
    "QCD_170to300"                : 53886,
    "QCD_300to470"                : 568138,
    "QCD_470to600"                : 301321,
    "QCD_600to800"                : 3379827,
    "QCD_800to1000"               : 444740,
    "QCD_1000to1400"              : 2772636,
    "QCD_1400to1800"              : 1240176,
    "QCD_1800to2400"              : 837603,
    "QCD_2400to3200"              : 426470,
    "QCD_3200toInf"               : 321896,
}

optional_dict_ntupleEff = { x : bkgd_crabSkimmed[x] / bkgd_crabSeen[x] for x in bkgd_crabSeen }

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

    'AMSB_chargino_1000GeV_1cm_94X'     : "/AMSB_chargino_M-1000_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1000GeV_10cm_94X'    : "/AMSB_chargino_M-1000_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1000GeV_100cm_94X'   : "/AMSB_chargino_M-1000_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1000GeV_1000cm_94X'  : "/AMSB_chargino_M-1000_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1000GeV_10000cm_94X' : "/AMSB_chargino_M-1000_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",

    'AMSB_chargino_1100GeV_1cm_94X'     : "/AMSB_chargino_M-1100_CTau-1_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1100GeV_10cm_94X'    : "/AMSB_chargino_M-1100_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1100GeV_100cm_94X'   : "/AMSB_chargino_M-1100_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1100GeV_1000cm_94X'  : "/AMSB_chargino_M-1100_CTau-1000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
    'AMSB_chargino_1100GeV_10000cm_94X' : "/AMSB_chargino_M-1100_CTau-10000_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v11-v1/MINIAODSIM",
}

dataset_names_sig_higgsino = {
    'Higgsino_100GeV_1cm_102X'     : "",
    'Higgsino_100GeV_10cm_102X'    : "/Higgsino_M-100GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_100GeV_100cm_102X'   : "/Higgsino_M-100GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_100GeV_1000cm_102X'  : "/Higgsino_M-100GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_100GeV_10000cm_102X' : "/Higgsino_M-100GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_200GeV_1cm_102X'     : "",
    'Higgsino_200GeV_10cm_102X'    : "/Higgsino_M-200GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_200GeV_100cm_102X'   : "/Higgsino_M-200GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_200GeV_1000cm_102X'  : "/Higgsino_M-200GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_200GeV_10000cm_102X' : "/Higgsino_M-200GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_300GeV_1cm_102X'     : "",
    'Higgsino_300GeV_10cm_102X'    : "/Higgsino_M-300GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_300GeV_100cm_102X'   : "/Higgsino_M-300GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_300GeV_1000cm_102X'  : "/Higgsino_M-300GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_300GeV_10000cm_102X' : "/Higgsino_M-300GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_400GeV_1cm_102X'     : "",
    'Higgsino_400GeV_10cm_102X'    : "/Higgsino_M-400GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_400GeV_100cm_102X'   : "/Higgsino_M-400GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_400GeV_1000cm_102X'  : "/Higgsino_M-400GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_400GeV_10000cm_102X' : "/Higgsino_M-400GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_500GeV_1cm_102X'     : "",
    'Higgsino_500GeV_10cm_102X'    : "/Higgsino_M-500GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_500GeV_100cm_102X'   : "/Higgsino_M-500GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_500GeV_1000cm_102X'  : "/Higgsino_M-500GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_500GeV_10000cm_102X' : "/Higgsino_M-500GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_600GeV_1cm_102X'     : "",
    'Higgsino_600GeV_10cm_102X'    : "/Higgsino_M-600GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_600GeV_100cm_102X'   : "/Higgsino_M-600GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_600GeV_1000cm_102X'  : "/Higgsino_M-600GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_600GeV_10000cm_102X' : "/Higgsino_M-600GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_700GeV_1cm_102X'     : "",
    'Higgsino_700GeV_10cm_102X'    : "/Higgsino_M-700GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_700GeV_100cm_102X'   : "/Higgsino_M-700GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_700GeV_1000cm_102X'  : "/Higgsino_M-700GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_700GeV_10000cm_102X' : "/Higgsino_M-700GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_800GeV_1cm_102X'     : "",
    'Higgsino_800GeV_10cm_102X'    : "/Higgsino_M-800GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_800GeV_100cm_102X'   : "/Higgsino_M-800GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_800GeV_1000cm_102X'  : "/Higgsino_M-800GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_800GeV_10000cm_102X' : "/Higgsino_M-800GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",

    'Higgsino_900GeV_1cm_102X'     : "",
    'Higgsino_900GeV_10cm_102X'    : "/Higgsino_M-900GeV_CTau-10cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_900GeV_100cm_102X'   : "/Higgsino_M-900GeV_CTau-100cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_900GeV_1000cm_102X'  : "/Higgsino_M-900GeV_CTau-1000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
    'Higgsino_900GeV_10000cm_102X' : "/Higgsino_M-900GeV_CTau-10000cm_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3/MINIAODSIM",
}

dataset_names = {}
dataset_names.update (dataset_names_data)
dataset_names.update (dataset_names_bkgd)
dataset_names.update (dataset_names_sig)
dataset_names.update (dataset_names_sig_higgsino)

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

# higgsino
for dataset0 in dataset_names:
    if not re.match (r'Higgsino_[^_]*GeV_[^_]*cm_.*', dataset0):
        continue
    mass = re.sub (r'Higgsino_([^_]*)GeV_[^_]*cm_.*', r'\1', dataset0)
    ctau0 = float (re.sub (r'Higgsino_[^_]*GeV_([^_]*)cm_.*', r'\1', dataset0))
    suffix = re.sub (r'Higgsino_[^_]*GeV_[^_]*cm_(.*)', r'\1', dataset0)
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'Higgsino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

        new_dataset_names[dataset] = dataset_names[dataset0]

dataset_names.update (new_dataset_names)
