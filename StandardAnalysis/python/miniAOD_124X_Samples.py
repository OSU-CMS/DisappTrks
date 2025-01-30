#!/usr/bin/env python3

############################################################################################################
#########  LIST OF MINIAOD 2022 12_4_X DATASETS  ###########################################################
###########################################################################################################



run3_skim_sibling_datasets = {
    # EGamma
    "EGamma_2022C": "/EGamma/Run2022C-EXODisappTrk-27Jun2023-v1/AOD",
    "EGamma_2022D": "/EGamma/Run2022D-EXODisappTrk-27Jun2023-v2/AOD",
    "EGamma_2022E": "/EGamma/Run2022E-EXODisappTrk-27Jun2023-v1/AOD",
    "EGamma_2022F": "/EGamma/Run2022F-EXODisappTrk-PromptReco-v1/AOD",
    "EGamma_2022G": "/EGamma/Run2022G-EXODisappTrk-PromptReco-v1/AOD",
    # Tau
    "Tau_2022C": "/Tau/Run2022C-EXODisappTrk-27Jun2023-v2/AOD",
    "Tau_2022D": "/Tau/Run2022D-EXODisappTrk-27Jun2023-v2/AOD",
    "Tau_2022E": "/Tau/Run2022E-EXODisappTrk-27Jun2023-v1/AOD",
    "Tau_2022F": "/Tau/Run2022F-EXODisappTrk-PromptReco-v1/AOD",
    "Tau_2022G": "/Tau/Run2022G-EXODisappTrk-PromptReco-v1/AOD",
    # MET
    #'MET_2022A' : '/MET/lpclonglived-Skim_EXODisappTrks_MET_Run2022A-485942db884bb77e20d203394ccaa614/USER',
    #'MET_2022B' : '/MET/lpclonglived-Skim_EXODisappTrks_MET_Run2022B-485942db884bb77e20d203394ccaa614/USER',
    #'MET_2022C' : '/MET/lpclonglived-Skim_EXODisappTrks_MET_Run2022C-485942db884bb77e20d203394ccaa614/USER',
    #'MET_2022D' : '',
    #'MET_2022E' : '/JetMET/Run2022E-EXODisappTrk-PromptReco-v1/AOD',
    #'MET_2022F' : '/JetMET/Run2022F-EXODisappTrk-PromptReco-v1/AOD',
    #'MET_2022G' : '/JetMET/Run2022G-EXODisappTrk-PromptReco-v1/AOD',
    # temporary
    "MET_2022A": "/MET/Run2022A-27Jun2023-v1/AOD",
    "MET_2022B": "/MET/Run2022B-16Jun2023-v2/AOD",
    "MET_2022C": "/MET/Run2022C-27Jun2023-v2/AOD",
    "MET_2022D": "/JetMET/Run2022D-EXODisappTrk-27Jun2023-v2/AOD",
    "MET_2022E": "/JetMET/Run2022E-EXODisappTrk-27Jun2023-v1/AOD",
    "MET_2022F": "/JetMET/Run2022F-EXODisappTrk-PromptReco-v1/AOD",
    "MET_2022G": "/JetMET/Run2022G-EXODisappTrk-PromptReco-v1/AOD",
    # Muon
    "Muon_2022C": "/Muon/Run2022C-EXODisappTrk-27Jun2023-v1/AOD",
    "Muon_2022D": "/Muon/Run2022D-EXODisappTrk-27Jun2023-v2/AOD",
    "Muon_2022E": "/Muon/Run2022E-EXODisappTrk-27Jun2023-v1/AOD",
    "Muon_2022F": "/Muon/Run2022F-EXODisappTrk-PromptReco-v1/AOD",
    "Muon_2022G": "/Muon/Run2022G-EXODisappTrk-PromptReco-v1/AOD",

    # SignalMC
    'AMSB_chargino_700GeV_10000cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/10000cm/700GeV/AMSB_chargino_M_700GeV_CTau_10000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/',
    'AMSB_chargino_700GeV_1000cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/1000cm/700GeV/AMSB_chargino_M_700GeV_CTau_1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/',
    'AMSB_chargino_700GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/100cm/700GeV/AMSB_chargino_M_700GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/',
    'AMSB_chargino_700GeV_10cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/10cm/700GeV/AMSB_chargino_M_700GeV_CTau_10cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/',
    'AMSB_chargino_100GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/100cm/100GeV/AMSB_chargino_M_100GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/',
    'AMSB_chargino_Pythia700GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/100cm/Pythia700GeV/AMSB_chargino_M_700GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_pythia8/',
    'AMSB_chargino_Pythia100GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step3/100cm/Pythia100GeV/AMSB_chargino_M_100GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_pythia8/',
}

dataset_names_data = {  # Fixme -> added those that exist as of Nov 14, 2022
    # MET
    #'MET_2022A' : '/MET/Run2022A-PromptReco-v1/MINIAOD',
    #'MET_2022B' : '/MET/Run2022B-PromptReco-v1/MINIAOD',
    #'MET_2022C' : '/MET/Run2022C-PromptReco-v1/MINIAOD',
    #'MET_2022D' : '/JetMET/Run2022D-10Dec2022-v1/MINIAOD',
    #'MET_2022E' : '/JetMET/Run2022E-PromptReco-v1/MINIAOD',
    #'MET_2022F' : '/JetMET/Run2022F-PromptReco-v1/MINIAOD',
    #'MET_2022G' : '/JetMET/Run2022G-PromptReco-v1/MINIAOD',
    # Muonon
    "Muon_2022A": "/SingleMuon/Run2022A-PromptReco-v1/MINIAOD",
    "Muon_2022B": "/SingleMuon/Run2022B-PromptReco-v1/MINIAOD",
    "Muon_2022C": "/Muon/Run2022C-22Sep2023-v1/MINIAOD",
    "Muon_2022D": "/Muon/Run2022D-22Sep2023-v1/MINIAOD",
    "Muon_2022E": "/Muon/Run2022E-22Sep2023-v1/MINIAOD",
    "Muon_2022F": "/Muon/Run2022F-19Dec2023-v1/MINIAOD",
    "Muon_2022G": "/Muon/Run2022G-19Dec2023-v2/MINIAOD",
    # EGamma
    "EGamma_2022A": "/EGamma/Run2022A-22Sep2023-v1/MINIAOD",
    "EGamma_2022B": "/EGamma/Run2022B-22Sep2023-v2/MINIAOD",
    "EGamma_2022C": "/EGamma/Run2022C-22Sep2023-v1/MINIAOD",
    "EGamma_2022D": "/EGamma/Run2022D-22Sep2023-v1/MINIAOD",
    "EGamma_2022E": "/EGamma/Run2022E-22Sep2023-v1/MINIAOD",
    "EGamma_2022F": "/EGamma/Run2022F-22Sep2023-v1/MINIAOD",
    "EGamma_2022G": "/EGamma/Run2022G-19Dec2023-v1/MINIAOD",
    # Tau
    "Tau_2022C": "/Tau/Run2022C-22Sep2023-v1/MINIAOD",
    "Tau_2022D": "/Tau/Run2022D-22Sep2023-v1/MINIAOD",
    "Tau_2022E": "/Tau/Run2022E-22Sep2023-v1/MINIAOD",
    "Tau_2022F": "/Tau/Run2022F-22Sep2023-v1/MINIAOD",
    "Tau_2022G": "/Tau/Run2022G-22Sep2023-v1/MINIAOD",

    "MET_2022A": "/MET/Run2022A-22Sep2023-v1/MINIAOD",
    "MET_2022B": "/MET/Run2022B-22Sep2023-v1/MINIAOD",
    "MET_2022C": "/MET/Run2022C-22Sep2023-v1/MINIAOD",
    "MET_2022D": "/JetMET/Run2022D-22Sep2023-v1/MINIAOD",
    "MET_2022E": "/JetMET/Run2022E-22Sep2023-v1/MINIAOD",
    "MET_2022F": "/JetMET/Run2022F-PromptReco-v1/MINIAOD",
    "MET_2022G": "/JetMET/Run2022G-22Sep2023-v2/MINIAOD",

}

dataset_names_sig = {
    'AMSB_chargino_700GeV_10000cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/10000cm/700GeV/',
    'AMSB_chargino_700GeV_1000cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/1000cm/700GeV/',
    'AMSB_chargino_700GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/100cm/700GeV/',
    'AMSB_chargino_700GeV_10cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/10cm/700GeV/',
    'AMSB_chargino_100GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/100cm/100GeV/',
    'AMSB_chargino_Pythia700GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/100cm/Pythia700GeV/',
    'AMSB_chargino_Pythia100GeV_100cm_124X' : '/data/users/borzari/condor/SignalMC/Run3/2022/step4/100cm/Pythia100GeV/',
}

dataset_names_bkgd = {

    'WToLNu_4Jets_2022EE' : '/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    'DYto2L_4jets_M10to50_2022EE' : '/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming-961090dd68da90db16dc3ce116f1abf9/USER',
    'DYJetsToLL_M50_2022EE' : '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/borzari-3Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    'TbarBtoLminusNuB_2022EE' : '/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TBbartoLplusNuBbar_2022EE' : '/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TbarQtoLNu_2022EE' : '/TbarQtoLNu-t-channel_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TQbartoLNu_2022EE' : '/TQbartoLNu-t-channel_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TbarWplusto2L2Nu_2022EE' : '/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TbarWplustoLNu2Q_2022EE' : '/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TWminusto2L2Nu_2022EE' : '/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TWminustoLNu2Q_2022EE' : '/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    'WW_2022EE' : '/WW_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'WZ_2022EE' : '/WZ_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'ZZ_2022EE' : '/ZZ_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    'TTto2L2Nu_2022EE' : '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TTtoLNu2Q_2022EE' : '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'TTto4Q_2022EE' : '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    'QCD_PT15to30_2022EE' : '/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT30to50_2022EE' : '/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT50to80_2022EE' : '/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT80to120_2022EE' : '/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT120to170_2022EE' : '/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT170to300_2022EE' : '/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT300to470_2022EE' : '/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT470to600_2022EE' : '/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT600to800_2022EE' : '/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT800to1000_2022EE' : '/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT1000to1400_2022EE' : '/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT1400to1800_2022EE' : '/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT1800to2400_2022EE' : '/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT2400to3200_2022EE' : '/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'QCD_PT3200_2022EE' : '/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    'Zto2Nu_4Jets_HT100to200_2022EE' : '/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'Zto2Nu_4Jets_HT200to400_2022EE' : '/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'Zto2Nu_4Jets_HT400to800_2022EE' : '/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'Zto2Nu_4Jets_HT800to1500_2022EE' : '/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'Zto2Nu_4Jets_HT1500to2500_2022EE' : '/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',
    'Zto2Nu_4Jets_HT2500_2022EE' : '/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/borzari-Skimming_2022EE-3a8953c6b719d6563fe908b4ea7a6705/USER',

    # 'DYJetsToLL_M50_merged' : '/abyss/users/mcarrigan/DYJetsToLL_M-50-merged/',

}

# Put in the order they are in https://docs.google.com/spreadsheets/d/19JS0zfIoQxH8sVOvsY1mg-Ct1Aw80Fm0TCgxewafGp8/edit?gid=371784835#gid=371784835
dataset_names_bkgd_MiniAOD = {

    'DYto2L_4jets_M10to50_2022EE' : '/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v3/MINIAODSIM',
    'DYJetsToLL_M50_2022EE' : '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-forPOG_130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',

    'TbarBtoLminusNuB_2022EE' : '/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'TBbartoLplusNuBbar_2022EE' : '/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'TbarQtoLNu_2022EE' : '/TbarQtoLNu-t-channel_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'TQbartoLNu_2022EE' : '/TQbartoLNu-t-channel_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'TbarWplusto2L2Nu_2022EE' : '/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'TbarWplustoLNu2Q_2022EE' : '/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'TWminusto2L2Nu_2022EE' : '/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'TWminustoLNu2Q_2022EE' : '/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',

    'TTto2L2Nu_2022EE' : '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'TTtoLNu2Q_2022EE' : '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'TTto4Q_2022EE' : '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',

    'WW_2022EE' : '/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'WZ_2022EE' : '/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'ZZ_2022EE' : '/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',

    'WToLNu_4Jets_2022EE' : '/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',

    'Zto2Nu_4Jets_HT100to200_2022EE' : '/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT200to400_2022EE' : '/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT400to800_2022EE' : '/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT800to1500_2022EE' : '/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM',
    'Zto2Nu_4Jets_HT1500to2500_2022EE' : '/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT2500_2022EE' : '/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',

    'QCD_PT15to30_2022EE' : '/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-EpsilonPU_130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'QCD_PT30to50_2022EE' : '/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-EpsilonPU_130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'QCD_PT50to80_2022EE' : '/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'QCD_PT80to120_2022EE' : '/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    'QCD_PT120to170_2022EE' : '/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT170to300_2022EE' : '/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT300to470_2022EE' : '/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT470to600_2022EE' : '/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT600to800_2022EE' : '/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT800to1000_2022EE' : '/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT1000to1400_2022EE' : '/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT1400to1800_2022EE' : '/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT1800to2400_2022EE' : '/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT2400to3200_2022EE' : '/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
    'QCD_PT3200_2022EE' : '/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',



    'DYto2L_4jets_M10to50_2022' : '/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1/MINIAODSIM',
    'DYJetsToLL_M50_2022' : '/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22MiniAODv4-forPOG_130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',

    'TbarBtoLminusNuB_2022' : '/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TBbartoLplusNuBbar_2022' : '/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TbarQtoLNu_2022' : '/TbarQtoLNu-t-channel_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TQbartoLNu_2022' : '/TQbartoLNu-t-channel_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TbarWplusto2L2Nu_2022' : '/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TbarWplustoLNu2Q_2022' : '/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TWminusto2L2Nu_2022' : '/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TWminustoLNu2Q_2022' : '/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',

    'TTto2L2Nu_2022' : '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TTtoLNu2Q_2022' : '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'TTto4Q_2022' : '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',

    'WW_2022' : '/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'WZ_2022' : '/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'ZZ_2022' : '/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',

    'WToLNu_4Jets_2022' : '/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',

    'Zto2Nu_4Jets_HT100to200_2022' : '/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT200to400_2022' : '/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT400to800_2022' : '/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT800to1500_2022' : '/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT1500to2500_2022' : '/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    'Zto2Nu_4Jets_HT2500_2022' : '/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',

    'QCD_PT15to30_2022' : '/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT30to50_2022' : '/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-EpsilonPU_130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT50to80_2022' : '/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT80to120_2022' : '/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT120to170_2022' : '/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT170to300_2022' : '/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT300to470_2022' : '/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT470to600_2022' : '/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT600to800_2022' : '/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT800to1000_2022' : '/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT1000to1400_2022' : '/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT1400to1800_2022' : '/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT1800to2400_2022' : '/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT2400to3200_2022' : '/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
    'QCD_PT3200_2022' : '/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',

}

dataset_names = {}
dataset_names.update(dataset_names_data)
dataset_names.update(dataset_names_bkgd)
dataset_names.update(dataset_names_sig)

import re

"""
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
"""
