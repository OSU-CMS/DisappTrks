#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2018 10_2_X DATASETS  ###########################################################
############################################################################################################

dataset_names_data = {

    'MET_2018A' : '/MET/Run2018A-17Sep2018-v1/MINIAOD',
    'MET_2018B' : '/MET/Run2018B-17Sep2018-v1/MINIAOD',
    'MET_2018C' : '/MET/Run2018C-17Sep2018-v1/MINIAOD',
    'MET_2018D' : '/MET/Run2018D-PromptReco-v2/MINIAOD',

    'EGamma_2018A' : '/EGamma/Run2018A-17Sep2018-v2/MINIAOD',
    'EGamma_2018B' : '/EGamma/Run2018B-17Sep2018-v1/MINIAOD',
    'EGamma_2018C' : '/EGamma/Run2018C-17Sep2018-v1/MINIAOD',
    'EGamma_2018D' : '/EGamma/Run2018D-PromptReco-v2/MINIAOD',

    'SingleMu_2018A' : '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD',
    'SingleMu_2018B' : '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD',
    'SingleMu_2018C' : '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD',
    'SingleMu_2018D' : '/SingleMuon/Run2018D-PromptReco-v2/MINIAOD',

    'Tau_2018A' : '/Tau/Run2018A-17Sep2018-v1/MINIAOD',
    'Tau_2018B' : '/Tau/Run2018B-17Sep2018-v1/MINIAOD',
    'Tau_2018C' : '/Tau/Run2018C-17Sep2018-v1/MINIAOD',
    'Tau_2018D' : '/Tau/Run2018D-PromptReco-v2/MINIAOD',

}

sibling_datasets = {
    "MET_2018A" : "/MET/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "MET_2018B" : "/MET/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "MET_2018C" : "/MET/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "MET_2018D" : "/MET/ahart-Run2018D-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",

    "EGamma_2018A" : "/EGamma/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "EGamma_2018B" : "/EGamma/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "EGamma_2018C" : "/EGamma/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "EGamma_2018D" : "/EGamma/ahart-Run2018D-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",

    "SingleMuon_2018A" : "/SingleMuon/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "SingleMuon_2018B" : "/SingleMuon/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "SingleMuon_2018C" : "/SingleMuon/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "SingleMuon_2018D" : "/SingleMuon/ahart-Run2018D-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",

    "Tau_2018A" : "/Tau/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "Tau_2018B" : "/Tau/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "Tau_2018C" : "/Tau/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "Tau_2018D" : "/Tau/ahart-Run2018D-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
}

dataset_names_bkgd = {
    # TTJets
    'TTJets_inclusive'          : '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM', #72M
    #'TTJets_SingleLeptFromT'    : '/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #46M status:PRODUCTION
    #'TTJets_DiLept'             : '/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #24M status:PRODUCTION
    'TTJets_SingleLeptFromTbar' : '/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #59M

    # QCD

    # DY
    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',# 39M
    'DYJetsToLL_50'     : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#100M

    # WJets
    'WJetsToLNu_HT-100to200' : '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #29M
    'WJetsToLNu_HT-200to400' : '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #25M
    'WJetsToLNu_HT-400to600' : '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #5M
    #'WJetsToLNu_HT-600to800' : '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #19M status: PRODUCTION
    'WJetsToLNu_HT-800to1200' : '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #8M
    #'WJetsToLNu_HT-1200to2500' : '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #6M status: PRODUCTION
    'WJetsToLNu_HT-2500toInf' : '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', #3M

    # WW
    'WWToLNuLNu' : "",#['/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',#2M DOESN'T EXIST YET
                      #'/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'],#2M DOESN'T EXIST YET
    'WWToLNuQQ'  : "",#['/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#9M DOESN'T EXIST YET
                      #'/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',#10M DOESN'T EXIST YET
                      #'/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM'],#9M DOESN'T EXIST YET

    # WZ
    'WZToLNu2QorQQ2L' : "",#['/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',#19M DOESN'T EXIST YET
                           #'/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'],#28M DOESN'T EXIST YET
    'WZToLNuNuNu'     : "",#'/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#5M DOESN'T EXIST YET
    'WZToLLLNu'       : "",#['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#9M status: PRODUCTION
                           #'/WZTo3LNu_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'],#1M # DOESN'T EXIST YET

    # ZZ
    'ZZToNuNuQQ' : "",#'/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#56M status: PRODUCTION
    'ZZToLLQQ'   : "",#'/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#28M DOESN'T EXIST YET
    'ZZToLLNuNu' : ['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#400K
                     '/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#8M
    'ZZToLLLL'   : ['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#800K
                    '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#6M

    # VG
    'WG' : "",
    'ZG' : "",

    #SingleTop
    'SingleTop_s_channel'         : ['/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM',#19M
                     '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4/MINIAODSIM'],#19M
    'SingleTop_t_channel_top'     : "",#'/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#6M DOESN'T EXIST YET
    'SingleTop_t_channel_antitop' : "",#'/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#4M DOESN'T EXIST YET
    'SingleTop_tbarW'             : ['/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#600K
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM',#5M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#1M
    'SingleTop_tW'                : ['/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#600K
                                     '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM',#7M
                                     '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#1M
}

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
