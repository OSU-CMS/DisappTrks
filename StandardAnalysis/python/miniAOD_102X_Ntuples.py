#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 94X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {
    "MET_2018A" : "/MET/ahart-Run2018A-17Sep2018-v2-4a666b96e844710047f00452b66377b0/USER",
    "MET_2018B" : "/MET/ahart-Run2018B-17Sep2018-v2-4a666b96e844710047f00452b66377b0/USER",
    "MET_2018C" : "/MET/ahart-Run2018C-17Sep2018-v2-4a666b96e844710047f00452b66377b0/USER",
    "MET_2018D" : "/MET/ahart-Run2018D-17Sep2018-v2-4a666b96e844710047f00452b66377b0/USER",

    #"EGamma_2018A"
    #"EGamma_2018B"
    "EGamma_2018C"  : "/EGamma/kwei-Run2018C-17Sep2018-v2-487fd77bb7c60ed3ff81debc3418af81/USER",
    #"EGamma_2018D"

    #"SingleMu_2018A"
    "SingleMu_2018B" : "/SingleMuon/bfrancis-Run2018B-17Sep2018-v2-c93e9ee70511413295b863cbd96e3fa5/USER",
    "SingleMu_2018C" : "/SingleMuon/bfrancis-Run2018C-17Sep2018-v2-c93e9ee70511413295b863cbd96e3fa5/USER",
    "SingleMu_2018D" : "/SingleMuon/bfrancis-Run2018D-17Sep2018-v2-c93e9ee70511413295b863cbd96e3fa5/USER",

    "Tau_2018A"  : "/Tau/kwei-Run2018A-17Sep2018-v2-134ed1c8518933d56bc124df945e0135/USER",
    #"Tau_2018B"
    #"Tau_2018C"
    #"Tau_2018D"
}

dataset_names_bkgd = {

    # TTJets
    'TTJets_SemiLeptonic'  :  "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-459ed261fc2a3db7f584aa89b8cb658b/USER",
    'TTJets_2L2Nu'         :  "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-459ed261fc2a3db7f584aa89b8cb658b/USER",
    'TTJets_Hadronic'      :  "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/ahart-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-459ed261fc2a3db7f584aa89b8cb658b/USER",

    # QCD
    'QCD_15to30'      : "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_30to50'      : "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_50to80'      : "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_80to120'     : "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v2-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_120to170'    : "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_170to300'    : "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_300to470'    : "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_470to600'    : "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_600to800'    : "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_800to1000'   : "", # accidentally ran MuEnriched
    'QCD_1000to1400'  : "",
    'QCD_1400to1800'  : "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER", # includes ext1
    'QCD_1800to2400'  : "/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_2400to3200'  : "/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER", # includes ext1
    'QCD_3200toInf'   : "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER", # includes ext1

    'DYJetsToLL_50'     : "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'DYJetsToLL_10to50' : "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",

    'SingleTop_s_channel'         : "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'SingleTop_t_channel_antitop' : "",
    'SingleTop_t_channel_top'     : "",
    'SingleTop_tW'                : "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'SingleTop_tbarW'             : "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",

    'WJetsToLNu_HT70to100'     : "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'WJetsToLNu_HT100to200'   : "",
    'WJetsToLNu_HT200to400'   : "",
    'WJetsToLNu_HT400to600'   : "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'WJetsToLNu_HT600to800'   : "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'WJetsToLNu_HT800to1200'  : "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'WJetsToLNu_HT1200to2500' : "",
    'WJetsToLNu_HT2500toInf'  : "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",

    'WJetsToLNu' : "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",

    'WW' : "/WW_TuneCP5_13TeV-pythia8/ahart-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-459ed261fc2a3db7f584aa89b8cb658b/USER",
    'WZ' : "/WZ_TuneCP5_13TeV-pythia8/ahart-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-459ed261fc2a3db7f584aa89b8cb658b/USER",
    'ZZ' : "/ZZ_TuneCP5_13TeV-pythia8/ahart-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-459ed261fc2a3db7f584aa89b8cb658b/USER",

    'ZJetsToNuNu_HT100to200'   : "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'ZJetsToNuNu_HT200to400'   : "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'ZJetsToNuNu_HT400to600'   : "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'ZJetsToNuNu_HT600to800'   : "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'ZJetsToNuNu_HT800to1200'  : "",
    'ZJetsToNuNu_HT1200to2500' : "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'ZJetsToNuNu_HT2500toInf'  : "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/kwei-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",

}

bkgd_crabSeen = { # run framework job with CandidateTrackProducer/test/analyzeSkimCutFlow.py, use -j 1 for one job per file

    # TTJets
    'TTJets_SemiLeptonic' : -1,
    'TTJets_2L2Nu'        : -1,
    'TTJets_2L2Nu'        : -1,

    # QCD
    'QCD_15to30'     : 19856000.0,
    'QCD_30to50'     : 5640000.0,
    'QCD_50to80'     : 25643000.0,
    'QCD_80to120'    : 29535000.0,
    'QCD_120to170'   : 25390000.0,
    'QCD_170to300'   : 29740000.0,
    'QCD_300to470'   : 17400000.0,
    'QCD_470to600'   : 42624665.0,
    'QCD_600to800'   : 64094000.0,
    'QCD_800to1000'  : -1,
    'QCD_1000to1400' : -1,
    'QCD_1400to1800' : 6944000.0,
    'QCD_1800to2400' : 4063800.0,
    'QCD_2400to3200' : 2394000.0,
    'QCD_3200toInf'  : 925000.0,

    'DYJetsToLL_50'     : 99793463.0,
    'DYJetsToLL_10to50' : 39309948.0,

    'SingleTop_s_channel'         : 20000000.0,
    'SingleTop_t_channel_antitop' : -1,
    'SingleTop_t_channel_top'     : -1,
    'SingleTop_tW'                : 7740170.0,
    'SingleTop_tbarW'             : 5813561.0,

    'WJetsToLNu_HT70to100'     : 28159421.0,
    'WJetsToLNu_HT100to200'   : -1,
    'WJetsToLNu_HT200to400'   : -1,
    'WJetsToLNu_HT400to600'   : 5932701.0,
    'WJetsToLNu_HT600to800'   : 20079356.0,
    'WJetsToLNu_HT800to1200'  : 8441662.0,
    'WJetsToLNu_HT1200to2500' : -1,
    'WJetsToLNu_HT2500toInf'  : 3281971.0,

    'WJetsToLNu' : 71122242.0,

    'WW' : 7920000.0,
    'WZ' : 3885000.0,
    'ZZ' : 1979000.0,

    'ZJetsToNuNu_HT100to200'   : 24287910.0,
    'ZJetsToNuNu_HT200to400'   : 23760670.0,
    'ZJetsToNuNu_HT400to600'   : 9527919.0,
    'ZJetsToNuNu_HT600to800'   : 5761094.0,
    'ZJetsToNuNu_HT800to1200'  : -1,
    'ZJetsToNuNu_HT1200to2500' : 342781.0,
    'ZJetsToNuNu_HT2500toInf'  : 359639.0,

}

bkgd_crabSkimmed = { # taken from DAS, checked with framework jobs' datasetInfo files

    # TTJets
    'TTJets_SemiLeptonic' : -1,
    'TTJets_2L2Nu'        : -1,
    'TTJets_2L2Nu'        : -1,

    # QCD
    'QCD_15to30'     : 29.0,
    'QCD_30to50'     : 61.0,
    'QCD_50to80'     : 963.0,
    'QCD_80to120'    : 2297.0, # ??? from crab report only
    'QCD_120to170'   : 4587.0,
    'QCD_170to300'   : 31143.0,
    'QCD_300to470'   : 142147.0,
    'QCD_470to600'   : 1078049.0,
    'QCD_600to800'   : 3013230.0,
    'QCD_800to1000'  : -1,
    'QCD_1000to1400' : -1,
    'QCD_1400to1800' : 1348627.0,
    'QCD_1800to2400' : 1054557.0,
    'QCD_2400to3200' : 812733.0,
    'QCD_3200toInf'  : 399922.0,

    'DYJetsToLL_50'     : 27267842.0,
    'DYJetsToLL_10to50' : 146282.0,

    'SingleTop_s_channel'         : 5142126.0,
    'SingleTop_t_channel_antitop' : -1,
    'SingleTop_t_channel_top'     : -1,
    'SingleTop_tW'                : 3210565.0,
    'SingleTop_tbarW'             : 2412622.0,

    'WJetsToLNu_HT70to100'     : 6561102.0,
    'WJetsToLNu_HT100to200'   : -1,
    'WJetsToLNu_HT200to400'   : -1,
    'WJetsToLNu_HT400to600'   : 2576579.0,
    'WJetsToLNu_HT600to800'   : 9408834.0,
    'WJetsToLNu_HT800to1200'  : 4224073.0,
    'WJetsToLNu_HT1200to2500' : -1,
    'WJetsToLNu_HT2500toInf'  : 2110654.0,

    'WJetsToLNu' : 11787702.0,

    'WW' : 1241393.0,
    'WZ' : 495668.0,
    'ZZ' : 194508.0,

    'ZJetsToNuNu_HT100to200'   : 1288439.0,
    'ZJetsToNuNu_HT200to400'   : 6145021.0,
    'ZJetsToNuNu_HT400to600'   : 3678612.0,
    'ZJetsToNuNu_HT600to800'   : 2500168.0,
    'ZJetsToNuNu_HT800to1200'  : -1,
    'ZJetsToNuNu_HT1200to2500' : 186609.0,
    'ZJetsToNuNu_HT2500toInf'  : 232040.0,
    
}

optional_dict_ntupleEff = { x : bkgd_crabSkimmed[x] / bkgd_crabSeen[x] for x in bkgd_crabSeen }

dataset_names_sig = {
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
