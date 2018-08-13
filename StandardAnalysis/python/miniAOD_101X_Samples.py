#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2018 10_1_X DATASETS  ###########################################################
############################################################################################################

dataset_names_data = {
    # SingleMu PromptReco
    'SingleMu_2018A' : ["/SingleMuon/Run2018A-PromptReco-v1/MINIAOD", "/SingleMuon/Run2018A-PromptReco-v2/MINIAOD", "/SingleMuon/Run2018A-PromptReco-v3/MINIAOD"],
    'SingleMu_2018B' : ["/SingleMuon/Run2018B-PromptReco-v1/MINIAOD", "/SingleMuon/Run2018B-PromptReco-v2/MINIAOD"],
    'SingleMu_2018C' : ["/SingleMuon/Run2018C-PromptReco-v1/MINIAOD", "/SingleMuon/Run2018C-PromptReco-v2/MINIAOD", "/SingleMuon/Run2018C-PromptReco-v3/MINIAOD"],
    'SingleMu_2018D' : "/SingleMuon/Run2018D-PromptReco-v2/MINIAOD",
}

dataset_names_bkgd = {
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
