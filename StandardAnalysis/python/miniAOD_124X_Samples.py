#!/usr/bin/env python3

############################################################################################################
#########  LIST OF MINIAOD 2022 12_4_X DATASETS  ###########################################################
###########################################################################################################


dataset_names_data = {
    #EGamma
    'EGamma_2022A' : '/EGamma/Run2022A-EXODisappTrk-10Dec2022-v1/AOD',
    'EGamma_2022E' : '/EGamma/Run2022E-EXODisappTrk-PromptReco-v1/AOD',
    'EGamma_2022F' : '/EGamma/Run2022F-EXODisappTrk-PromptReco-v1/AOD',
    'EGamma_2022G' : '/EGamma/Run2022G-EXODisappTrk-PromptReco-v1/AOD',

    #Tau
    'Tau_2022B' : '/Tau/Run2022B-PromptReco-v1/MINIAOD',
    'Tau_2022E' : '/Tau/Run2022E-EXODisappTrk-PromptReco-v1/AOD',
    'Tau_2022F' : '/Tau/Run2022F-EXODisappTrk-PromptReco-v1/AOD',

    #MET
    #'MET_2022A' : '/MET/lpclonglived-Skim_EXODisappTrks_MET_Run2022A-485942db884bb77e20d203394ccaa614/USER',
    #'MET_2022B' : '/MET/lpclonglived-Skim_EXODisappTrks_MET_Run2022B-485942db884bb77e20d203394ccaa614/USER',
    #'MET_2022C' : '/MET/lpclonglived-Skim_EXODisappTrks_MET_Run2022C-485942db884bb77e20d203394ccaa614/USER',
    #'MET_2022D' : '',
    #'MET_2022E' : '/JetMET/Run2022E-EXODisappTrk-PromptReco-v1/AOD',
    #'MET_2022F' : '/JetMET/Run2022F-EXODisappTrk-PromptReco-v1/AOD',
    #'MET_2022G' : '/JetMET/Run2022G-EXODisappTrk-PromptReco-v1/AOD',

    #temporary
    'MET_2022A' : '/MET/Run2022A-10Dec2022-v2/MINIAOD',
    'MET_2022B' : '/MET/Run2022B-PromptReco-v1/MINIAOD',
    'MET_2022C' : '/MET/Run2022C-10Dec2022-v2/MINIAOD',
    'MET_2022D' : '/JetMET/Run2022D-10Dec2022-v1/MINIAOD',
    'MET_2022E' : '/JetMET/Run2022E-PromptReco-v1/MINIAOD',
    'MET_2022F' : '/JetMET/Run2022F-PromptReco-v1/MINIAOD',
    'MET_2022G' : '/JetMET/Run2022G-PromptReco-v1/MINIAOD',
}

run3_skim_sibling_datasets = { # Fixme -> added those that exist as of Nov 14, 2022
    # MET
    #'MET_2022A' : '/MET/Run2022A-PromptReco-v1/MINIAOD',
    #'MET_2022B' : '/MET/Run2022B-PromptReco-v1/MINIAOD',
    #'MET_2022C' : '/MET/Run2022C-PromptReco-v1/MINIAOD',
    #'MET_2022D' : '/JetMET/Run2022D-10Dec2022-v1/MINIAOD',
    #'MET_2022E' : '/JetMET/Run2022E-PromptReco-v1/MINIAOD',
    #'MET_2022F' : '/JetMET/Run2022F-PromptReco-v1/MINIAOD',
    #'MET_2022G' : '/JetMET/Run2022G-PromptReco-v1/MINIAOD',

    #SingleMuon
    'SingleMu_2022A' : '/SingleMuon/Run2022A-PromptReco-v1/MINIAOD',
    'SingleMu_2022B' : '/SingleMuon/Run2022B-PromptReco-v1/MINIAOD',
    'SingleMu_2022C' : '/SingleMuon/Run2022C-PromptReco-v1/MINIAOD',

    #EGamma
    'EGamma_2022A' : '/EGamma/Run2022A-10Dec2022-v1/MINIAOD',
    'EGamma_2022B' : '/EGamma/Run2022B-PromptReco-v1/MINIAOD',
    'EGamma_2022C' : '/EGamma/Run2022C-PromptReco-v1/MINIAOD',
    'EGamma_2022D' : '/EGamma/Run2022D-PromptReco-v3/MINIAOD',
    'EGamma_2022E' : '/EGamma/Run2022E-PromptReco-v1/MINIAOD',
    'EGamma_2022F' : '/EGamma/Run2022F-PromptReco-v1/MINIAOD',
    'EGamma_2022G' : '/EGamma/Run2022G-PromptReco-v1/MINIAOD',


    #Tau
    'Tau_2022A' : '/Tau/Run2022A-PromptReco-v1/MINIAOD',
    'Tau_2022B' : '/Tau/Run2022B-PromptReco-v1/MINIAOD',
    'Tau_2022C' : '/Tau/Run2022C-PromptReco-v1/MINIAOD',
    'Tau_2022D' : '/Tau/Run2022D-PromptReco-v3/MINIAOD',
    'Tau_2022E' : '/Tau/Run2022E-PromptReco-v1/MINIAOD',
    'Tau_2022F' : '/Tau/Run2022F-PromptReco-v1/MINIAOD',

    'AMSB_chargino_700GeV_100cm_124X' : '/AMSB_chargino_M-700GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/borzari-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2022_realistic_v12-v1_step3/USER',

}

dataset_names_sig = {

    'AMSB_chargino_700GeV_100cm_124X' : '/AMSB_chargino_M-700GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/borzari-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2022_realistic_v12-v1_step4/USER',

}

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
