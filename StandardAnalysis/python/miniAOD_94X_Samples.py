#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 92X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {

    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################

    # MET 2017 PromptReco
    'MET_2017B' : "/MET/Run2017B-31Mar2018-v1/MINIAOD",
    'MET_2017C' : "/MET/Run2017C-31Mar2018-v1/MINIAOD",
    'MET_2017D' : "/MET/Run2017D-31Mar2018-v1/MINIAOD",
    'MET_2017E' : "/MET/Run2017E-31Mar2018-v1/MINIAOD",
    'MET_2017F' : "/MET/Run2017F-31Mar2018-v1/MINIAOD",

    # SingleEle PromptReco
    'SingleEle_2017B' : "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD",
    'SingleEle_2017C' : "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD",
    'SingleEle_2017D' : "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD",
    'SingleEle_2017E' : "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD",
    'SingleEle_2017F' : "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD",

    # SingleMu PromptReco
    'SingleMu_2017B' : "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD",
    'SingleMu_2017C' : "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD",
    'SingleMu_2017D' : "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD",
    'SingleMu_2017E' : "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD",
    'SingleMu_2017F' : "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD",

    # Tau PromptReco
    'Tau_2017B' : "/Tau/Run2017B-31Mar2018-v1/MINIAOD",
    'Tau_2017C' : "/Tau/Run2017C-31Mar2018-v1/MINIAOD",
    'Tau_2017D' : "/Tau/Run2017D-31Mar2018-v1/MINIAOD",
    'Tau_2017E' : "/Tau/Run2017E-31Mar2018-v1/MINIAOD",
    'Tau_2017F' : "/Tau/Run2017F-31Mar2018-v1/MINIAOD",

    # ZeroBias PromptReco
}

# ntuples of 2017C -- currently these are optional,
# so the usuer needs to exchange dataset_names_data
# with this if CandidateTracks are to be used
# only PromptReco available currently
datasets_names_data_ntuples = {
    
    'MET_2017C' : ["/MET/bfrancis-Run2017C-PromptReco-v1-DisappTrks-v1-22a0670d7fe97c6e01bf4e8339ab9566/USER", "/MET/bfrancis-Run2017C-PromptReco-v2-DisappTrks-v1-22a0670d7fe97c6e01bf4e8339ab9566/USER", "/MET/bfrancis-Run2017C-PromptReco-v3-DisappTrks-v1-22a0670d7fe97c6e01bf4e8339ab9566/USER"],

    'SingleEle_2017C' : ["/SingleElectron/bfrancis-Run2017C-PromptReco-v1-DisappTrks-v1-cfc215649d70368428bc7a3d641280a7/USER", "/SingleElectron/bfrancis-Run2017C-PromptReco-v2-DisappTrks-v1-cfc215649d70368428bc7a3d641280a7/USER", "/SingleElectron/bfrancis-Run2017C-PromptReco-v3-DisappTrks-v1-cfc215649d70368428bc7a3d641280a7/USER"],

    'SingleMu_2017C' : ["/SingleMuon/bfrancis-Run2017C-PromptReco-v1-DisappTrks-v1-f03047f866f83fdce5d5f13e4fbf8606/USER", "/SingleMuon/bfrancis-Run2017C-PromptReco-v2-DisappTrks-v1-f03047f866f83fdce5d5f13e4fbf8606/USER", "/SingleMuon/bfrancis-Run2017C-PromptReco-v3-DisappTrks-v1-f03047f866f83fdce5d5f13e4fbf8606/USER"],

    'Tau_2017C' : ["/Tau/bfrancis-Run2017C-PromptReco-v1-DisappTrks-v1-a30e1733f02bb89cdbef4204fa1a7612/USER", "/Tau/bfrancis-Run2017C-PromptReco-v2-DisappTrks-v1-a30e1733f02bb89cdbef4204fa1a7612/USER", "/Tau/bfrancis-Run2017C-PromptReco-v3-DisappTrks-v1-a30e1733f02bb89cdbef4204fa1a7612/USER"],

}

dataset_names_bkgd = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
}

dataset_names_bkgd = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
    'WJetsToLNu_2017' : "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1/MINIAODSIM",

    'DYJetsToLL_50_2017' : "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v7-v1/MINIAODSIM",
    #'DYJetsToLL_50_2017' : {"/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v7-v1/MINIAODSIM", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1/MINIAODSIM", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v2/MINIAODSIM"},
}

dataset_names_sig = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
    'AMSB_chargino_300GeV_100cm_94X'   : "/AMSB_chargino_M-300_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1/MINIAODSIM",

    'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1/MINIAODSIM",
    'AMSB_chargino_700GeV_1000cm_94X'  : "/AMSB_chargino_M-700_CTau-1000_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1/MINIAODSIM",
}

# CandidateTracks ntuple version
dataset_names_sig_ntuples = {
    'AMSB_chargino_300GeV_100cm_94X'   : "/AMSB_chargino_M-300_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1-candTracks/MINIAODSIM",

    'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1-candTracks/MINIAODSIM",
    'AMSB_chargino_700GeV_1000cm_94X'  : "/AMSB_chargino_M-700_CTau-1000_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1-candTracks/MINIAODSIM",
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
