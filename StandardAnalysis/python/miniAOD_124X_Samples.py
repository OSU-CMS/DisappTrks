#!/usr/bin/env python3

############################################################################################################
#########  LIST OF MINIAOD 2022 12_4_X DATASETS  ###########################################################
###########################################################################################################


dataset_names_data = {
    # MET
    'MET_2022A' : '/MET/Run2022A-PromptReco-v1/MINIAOD',
    'MET_2022B' : '/MET/Run2022B-PromptReco-v1/MINIAOD',
    'MET_2022C' : '/MET/Run2022C-PromptReco-v1/MINIAOD',

    #SingleMuon
    'SingleMu_2022A' : '/SingleMuon/Run2022A-PromptReco-v1/MINIAOD',
    'SingleMu_2022B' : '/SingleMuon/Run2022B-PromptReco-v1/MINIAOD',
    'SingleMu_2022C' : '/SingleMuon/Run2022C-PromptReco-v1/MINIAOD',

}
run3_skim_sibling_datasets = { # Fixme
    'MET_2022A' : '/MET/Run2022A-EXOHighMET-PromptReco-v1/RAW-RECO',
    'MET_2022B' : '/MET/Run2022B-EXOHighMET-PromptReco-v1/RAW-RECO',
    'MET_2022C' : '/MET/Run2022C-EXOHighMET-PromptReco-v1/RAW-RECO',
}

dataset_names_sig = {}

dataset_names_bkgd = {}

dataset_names = {}
dataset_names.update (dataset_names_data)
dataset_names.update (dataset_names_bkgd)
dataset_names.update (dataset_names_sig)

import re

'''
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
                                                                                                                                                                                                 180,1         Bot
'''
