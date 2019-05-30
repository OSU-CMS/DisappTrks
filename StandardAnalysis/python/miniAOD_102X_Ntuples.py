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
    "EGamma_2018C"  : "/EGamma/kwei-Run2018C-17Sep2018-v2-487fd77bb7c60ed3ff81debc3418af81/USER"
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
