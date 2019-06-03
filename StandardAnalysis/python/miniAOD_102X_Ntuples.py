#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 94X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {
    #"MET_2018A" :
    #"MET_2018B" :
    #"MET_2018C" :
    #"MET_2018D" :

    #"EGamma_2018A"
    #"EGamma_2018B"
    "EGamma_2018C"  : "/EGamma/kwei-Run2018C-17Sep2018-v2-487fd77bb7c60ed3ff81debc3418af81/USER",
    #"EGamma_2018D"

    #"SingleMu_2018A"
    "SingleMu_2018B" : "/SingleMuon/bfrancis-Run2018B-17Sep2018-v2-c93e9ee70511413295b863cbd96e3fa5/USER",
    "SingleMu_2018C" : "/SingleMuon/bfrancis-Run2018C-17Sep2018-v2-c93e9ee70511413295b863cbd96e3fa5/USER",
    #"SingleMu_2018D"

    "Tau_2018A"  : "/Tau/kwei-Run2018A-17Sep2018-v2-134ed1c8518933d56bc124df945e0135/USER",
    #"Tau_2018B"
    #"Tau_2018C"
    #"Tau_2018D"
}

dataset_names_bkgd = {

    # TTJets

    # QCD
    'QCD_15to30'      : "",
    'QCD_30to50'      : "",
    'QCD_50to80'      : "",
    'QCD_80to120'     : "",
    'QCD_120to170'    : "",
    'QCD_170to300'    : "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'QCD_300to470'    : "",
    'QCD_470to600'    : "",
    'QCD_600to800'    : "",
    'QCD_800to1000'   : "",
    'QCD_1000to1400'  : "",
    'QCD_1400to1800'  : "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER", # includes ext1
    'QCD_1800to2400'  : "",
    'QCD_2400to3200'  : "/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER", # includes ext1
    'QCD_3200toInf'   : "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER", # includes ext1

    'DYJetsToLL_50'    : "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/bfrancis-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-DisappTrks-v1-64a04fda89c1c1eeaec69b5836717950/USER",
    'DYJetsToLL_5to50' : "",

}

bkgd_crabSeen = { # run framework job with CandidateTrackProducer/test/analyzeSkimCutFlow.py, use -j 1 for one job per file

    # QCD
    'QCD_170to300'   : 29740000.0,
    'QCD_1400to1800' : 6944000.0,
    'QCD_2400to3200' : 2394000.0,
    'QCD_3200toInf'  : 925000.0,

    'DYJetsToLL_50' : 99793463.0,

}

bkgd_crabSkimmed = { # taken from DAS, checked with framework jobs' datasetInfo files

    # QCD
    'QCD_170to300'   : 31143.0,
    'QCD_1400to1800' : 1348627.0,
    'QCD_2400to3200' : 812733.0,
    'QCD_3200toInf'  : 399922.0,

    'DYJetsToLL_50' : 27267842.0,
    
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
