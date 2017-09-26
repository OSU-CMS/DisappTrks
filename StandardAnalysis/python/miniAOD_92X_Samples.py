#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 92X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {

    # Remade PromptReco ntuples are commented out for now.

    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################

    # MET 2017 PromptReco

    # SingleEle PromptReco

    # SingleMu PromptReco
    'SingleMu_2017B' : ["/SingleMuon/Run2017B-PromptReco-v1/MINIAOD", "/SingleMuon/Run2017B-PromptReco-v2/MINIAOD"],
    'SingleMu_2017C' : ["/SingleMuon/Run2017C-PromptReco-v1/MINIAOD", "/SingleMuon/Run2017C-PromptReco-v2/MINIAOD", "/SingleMuon/Run2017C-PromptReco-v3/MINIAOD"],
    'SingleMu_2017D' : "/SingleMuon/Run2017D-PromptReco-v1/MINIAOD",

    # Tau PromptReco

    # ZeroBias PromptReco
}

dataset_names_bkgd = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
}

dataset_names_sig = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
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
