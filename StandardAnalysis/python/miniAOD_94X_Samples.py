#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 94X DATASETS  ##############################################################
############################################################################################################

# N.B.: while we should use the most recent datasets, 31Mar2018 seems to have poor availability. 
#       Once it's been transferred to some T2s we should change this and re-run.

#rerecoName = "31Mar2018-v1"
rerecoName = "17Nov2017-v1"

dataset_names_data = {
    # MET 2017 PromptReco
    'MET_2017B' : "/MET/Run2017B-" + rerecoName + "/MINIAOD",
    'MET_2017C' : "/MET/Run2017C-" + rerecoName + "/MINIAOD",
    'MET_2017D' : "/MET/Run2017D-" + rerecoName + "/MINIAOD",
    'MET_2017E' : "/MET/Run2017E-" + rerecoName + "/MINIAOD",
    'MET_2017F' : "/MET/Run2017F-" + rerecoName + "/MINIAOD",

    # SingleEle PromptReco
    'SingleEle_2017B' : "/SingleElectron/Run2017B-" + rerecoName + "/MINIAOD",
    'SingleEle_2017C' : "/SingleElectron/Run2017C-" + rerecoName + "/MINIAOD",
    'SingleEle_2017D' : "/SingleElectron/Run2017D-" + rerecoName + "/MINIAOD",
    'SingleEle_2017E' : "/SingleElectron/Run2017E-" + rerecoName + "/MINIAOD",
    'SingleEle_2017F' : "/SingleElectron/Run2017F-" + rerecoName + "/MINIAOD",

    # SingleMu PromptReco
    'SingleMu_2017B' : "/SingleMuon/Run2017B-" + rerecoName + "/MINIAOD",
    'SingleMu_2017C' : "/SingleMuon/Run2017C-" + rerecoName + "/MINIAOD",
    'SingleMu_2017D' : "/SingleMuon/Run2017D-" + rerecoName + "/MINIAOD",
    'SingleMu_2017E' : "/SingleMuon/Run2017E-" + rerecoName + "/MINIAOD",
    'SingleMu_2017F' : "/SingleMuon/Run2017F-" + rerecoName + "/MINIAOD",

    # Tau PromptReco
    'Tau_2017B' : "/Tau/Run2017B-" + rerecoName + "/MINIAOD",
    'Tau_2017C' : "/Tau/Run2017C-" + rerecoName + "/MINIAOD",
    'Tau_2017D' : "/Tau/Run2017D-" + rerecoName + "/MINIAOD",
    'Tau_2017E' : "/Tau/Run2017E-" + rerecoName + "/MINIAOD",
    'Tau_2017F' : "/Tau/Run2017F-" + rerecoName + "/MINIAOD",

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
    # N.B. There is a RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1 campaign ongoing that should be used. 
    #      Pay attention and replace MiniAOD V1 samples when they show up.

    # DY
    'DYJetsToLL_10to50' : "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM",
    'DYJetsToLL_50'     : ["/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"],

    # ZJetsToNuNu
    'ZJetsToNuNu_HT100to200'   : "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'ZJetsToNuNu_HT200to400'   : "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",
    'ZJetsToNuNu_HT400to600'   : "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",
    'ZJetsToNuNu_HT600to800'   : "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'ZJetsToNuNu_HT800to1200'  : "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'ZJetsToNuNu_HT1200to2500' : "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",
    'ZJetsToNuNu_HT2500toInf'  : "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    # WJets
    # 'WJetsToLNu' : doesn't exist yet!

    # WJets_HT
    # 'WJetsToLNu_HT100to200' : doesn't exist yet!
    # 'WJetsToLNu_HT200to400' : doesn't exist yet!
    # 'WJetsToLNu_HT400to600' : doesn't exist yet!
    # 'WJetsToLNu_HT600toInf' : doesn't exist yet!

    # WW
    'WWToLNuQQ' : ["/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"],
    'WWToLNuLNu' : "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",

    # WZ
    'WZ' : "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    # 'WZToLLLNu' : doesn't exist! never used this anyway...

    # ZZ
    'ZZ' : "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    # VG
    # 'WG' : doesn't exist yet!
    # 'ZG' : doesn't exist yet!

    # Single Top
    'SingleTop_s_channel'         : "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'SingleTop_t_channel_top'     : "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", 
    'SingleTop_t_channel_antitop' : "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'SingleTop_tW'                : "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",
    'SingleTop_tbarW'             : ["/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"],

    # TTJets
    # 'TTJets' : a proper "/TT_TuneCP..." doesn't exist yet!
    'TTJets_2L2Nu' : "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'TTJets_SemiLeptonic' : "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'TTJets_Hadronic' : "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    # QCD
    #'QCD_5to10'       :  doesn't exist yet!
    #'QCD_10to15'      :  doesn't exist yet!
    'QCD_15to30'      :  "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_30to50'      :  "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_50to80'      :  "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_80to120'     :  "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_120to170'    :  "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",
    'QCD_170to300'    :  "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_300to470'    :  "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_470to600'    :  "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM",
    'QCD_600to800'    :  "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_800to1000'   :  "/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM",
    'QCD_1000to1400'  :  "/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_1400to1800'  :  "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_1800to2400'  :  "/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_2400to3200'  :  "/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'QCD_3200toInf'   :  "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

}

dataset_names_sig = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
    #'AMSB_chargino_300GeV_100cm_94X'   : "/AMSB_chargino_M-300_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1/MINIAODSIM",

    #'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1/MINIAODSIM",
    #'AMSB_chargino_700GeV_1000cm_94X'  : "/AMSB_chargino_M-700_CTau-1000_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1/MINIAODSIM",

    # ~50k events as per the central production request
    'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v4/MINIAODSIM",
}

# CandidateTracks ntuple version
dataset_names_sig_ntuples = {
    #'AMSB_chargino_300GeV_100cm_94X'   : "/AMSB_chargino_M-300_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1-candTracks/MINIAODSIM",

    #'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1-candTracks/MINIAODSIM",
    #'AMSB_chargino_700GeV_1000cm_94X'  : "/AMSB_chargino_M-700_CTau-1000_TuneCUEP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3p1-candTracks/MINIAODSIM",

    # ~50k events as per the central production request
    'AMSB_chargino_700GeV_100cm_94X'   : "/AMSB_chargino_M-700_CTau-100_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-94X_mc2017_realistic_v10-v4/MINIAODSIM",
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
