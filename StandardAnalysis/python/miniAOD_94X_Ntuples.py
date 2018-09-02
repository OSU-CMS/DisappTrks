#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2017 94X DATASETS  ##############################################################
############################################################################################################

dataset_names_data = {

    # SingleEle
    'SingleEle_2017B' : "/SingleElectron/bfrancis-Run2017B-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017C' : "/SingleElectron/bfrancis-Run2017C-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017D' : "/SingleElectron/bfrancis-Run2017D-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017E' : "/SingleElectron/bfrancis-Run2017E-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",
    'SingleEle_2017F' : "/SingleElectron/bfrancis-Run2017F-31Mar2018-v1-DisappTrks-v2-277c0e41a920dae7141f6c4d24521354/USER",

    # SingleMu
    'SingleMu_2017B' : "/SingleMuon/zpollock-Run2017B-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",
    'SingleMu_2017C' : "/SingleMuon/zpollock-Run2017C-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER", #only 99.6% of jobs
    'SingleMu_2017D' : "/SingleMuon/zpollock-Run2017D-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",
    'SingleMu_2017E' : "/SingleMuon/kwei-Run2017E-31Mar2018-v1-DisappTrks-v2-ebcd108112d2d6fbb0554e6a6a3b8e45/USER",

    # Tau
    'Tau_2017B' : "/Tau/bfrancis-Run2017B-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017C' : "/Tau/bfrancis-Run2017C-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017D' : "/Tau/bfrancis-Run2017D-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017E' : "/Tau/bfrancis-Run2017E-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
    'Tau_2017F' : "/Tau/bfrancis-Run2017F-31Mar2018-v1-DisappTrks-v2-d1b12f551b2a33d683277c01457a2688/USER",
}

dataset_names_bkgd = {
    # N.B. There is a RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1 campaign ongoing that should be used. 
    #      Pay attention and replace MiniAOD V1 samples when they show up.

    # TTJets
    # 'TTJets' : a proper "/TT_TuneCP..." doesn't exist!
    'TTJets_SemiLeptonic' : "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",

    # QCD
    #'QCD_5to10'       :  doesn't exist!
    #'QCD_10to15'      :  doesn't exist!
    'QCD_15to30'      : "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_30to50'      : "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_50to80'      : "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_80to120'     : "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_120to170'    : "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_170to300'    : "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_300to470'    : "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_470to600'    : "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_600to800'    : "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_800to1000'   : "/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    #'QCD_1000to1400'  :
    'QCD_1400to1800'  : "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    'QCD_1800to2400'  : "/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",
    #'QCD_2400to3200'  :
    'QCD_3200toInf'   : "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-DisappTrks-v2-de5f02ec0d0d96345889b201db21b7db/USER",


}

dataset_names_sig = {
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
