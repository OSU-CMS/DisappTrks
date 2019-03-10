#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 94X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {
    "MET_2018A" : "/MET/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "MET_2018B" : "/MET/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "MET_2018C" : "/MET/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",

    "EGamma_2018A" : "/EGamma/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "EGamma_2018B" : "/EGamma/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "EGamma_2018C" : "/EGamma/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",

    "SingleMuon_2018A" : "/SingleMuon/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "SingleMuon_2018B" : "/SingleMuon/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "SingleMuon_2018C" : "/SingleMuon/ahart-Run2018C-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",

    "Tau_2018A" : "/Tau/ahart-Run2018A-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
    "Tau_2018B" : "/Tau/ahart-Run2018B-17Sep2018-e1ce198dd6f8c89a1f35f11f9d9665d4/USER",
}

#sibling_datasets = {
#    "MET_2018A" : "/MET/Run2018A-17Sep2018-v1/MINIAOD",
#    "MET_2018B" : "/MET/Run2018B-17Sep2018-v1/MINIAOD",
#    "MET_2018C" : "/MET/Run2018C-17Sep2018-v1/MINIAOD",
#
#    "EGamma_2018A" : "/EGamma/Run2018A-17Sep2018-v2/MINIAOD",
#    "EGamma_2018B" : "/EGamma/Run2018B-17Sep2018-v1/MINIAOD",
#    "EGamma_2018C" : "/EGamma/Run2018C-17Sep2018-v1/MINIAOD",
#
#    "SingleMuon_2018A" : "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD",
#    "SingleMuon_2018B" : "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD",
#    "SingleMuon_2018C" : "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD",
#
#    "Tau_2018A" : "/Tau/Run2018A-17Sep2018-v1/MINIAOD",
#    "Tau_2018B" : "/Tau/Run2018B-17Sep2018-v1/MINIAOD",
#}

dataset_names_bkgd = {
}

bkgd_crabSeen = { # run framework job with CandidateTrackProducer/test/analyzeSkimCutFlow.py, use -j 1 for one job per file
}

bkgd_crabSkimmed = { # taken from DAS, checked with framework jobs' datasetInfo files
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
