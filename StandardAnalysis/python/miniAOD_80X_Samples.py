#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2016 80X DATASETS  ##################################################################
############################################################################################################

dataset_names = {
    ############################################################################
    # MiniAOD stored on T3.
    ############################################################################

    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################

    'MET_2016B'       : "/MET/ahart-Run2016B-PromptReco-v2-DisappTrks-v4-27e60d501ab86bf058faa389ff7c9e96/USER",
    'MET_2016C'       : "/MET/ahart-Run2016C-PromptReco-v2-DisappTrks-v4-27e60d501ab86bf058faa389ff7c9e96/USER",

    'SingleEle_2016B' : "/SingleElectron/bfrancis-Run2016B-PromptReco-v2-DisappTrks-v3-cff4671457ee5a0055a79ab442e4ac0e/USER",
    'SingleEle_2016C' : "/SingleElectron/bfrancis-Run2016C-PromptReco-v2-DisappTrks-v3-cff4671457ee5a0055a79ab442e4ac0e/USER",

    'SingleMu_2016B'  : "/SingleMuon/bfrancis-Run2016B-PromptReco-v2-DisappTrks-v3-a122bd715be38b4e27d893051cb4ea68/USER",
    'SingleMu_2016C'  : "/SingleMuon/bfrancis-Run2016C-PromptReco-v2-DisappTrks-v3-a122bd715be38b4e27d893051cb4ea68/USER",

    'Tau_2016B'        :  "/Tau/ahart-Run2016B-PromptReco-v2-DisappTrks-v4-90c2077fe78eb415d8089072325db2f1/USER",
    'Tau_2016C'        :  "/Tau/ahart-Run2016C-PromptReco-v2-DisappTrks-v4-90c2077fe78eb415d8089072325db2f1/USER",
}

# dummy copies of the 2016B datasets used to organize the two trigger versions:
# HLT_MET75_IsoTrk50_v2 and HLT_MET75_IsoTrk50_v3 which have different L1 MET
# seeds

dataset_names['MET_2016B_v2'] = dataset_names['MET_2016B']
dataset_names['MET_2016B_v3'] = dataset_names['MET_2016B']

dataset_names['SingleMu_2016B_v2'] = dataset_names['SingleMu_2016B']
dataset_names['SingleMu_2016B_v3'] = dataset_names['SingleMu_2016B']

dataset_names['SingleEle_2016B_v2'] = dataset_names['SingleEle_2016B']
dataset_names['SingleEle_2016B_v3'] = dataset_names['SingleEle_2016B']

dataset_names['Tau_2016B_v2'] = dataset_names['Tau_2016B']
dataset_names['Tau_2016B_v3'] = dataset_names['Tau_2016B']
