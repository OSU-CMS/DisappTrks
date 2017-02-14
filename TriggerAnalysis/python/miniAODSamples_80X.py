#!/usr/bin/env python

dataset_names = {

    'SingleMu_2016B'  : "/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD",
    'SingleMu_2016C'  : "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD",
    'SingleMu_2016D'  : "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD",
    'SingleMu_2016E'  : "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD",
    'SingleMu_2016F'  : "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD",
    'SingleMu_2016G'  : "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD",
    'SingleMu_2016H'  : ["/SingleMuon/Run2016H-PromptReco-v2/MINIAOD", "/SingleMuon/Run2016H-PromptReco-v3/MINIAOD"],

    'WJetsToLNu'  :  '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM',

    'AMSB_chargino_100GeV_10cm_80X'    :  "/AMSB_chargino_M-100_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_100cm_80X'   :  "/AMSB_chargino_M-100_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_1000cm_80X'  :  "/AMSB_chargino_M-100_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_10000cm_80X'  :  "/AMSB_chargino_M-100_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_200GeV_10cm_80X'    :  "/AMSB_chargino_M-200_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_200GeV_100cm_80X'   :  "/AMSB_chargino_M-200_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_200GeV_1000cm_80X'  :  "/AMSB_chargino_M-200_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_200GeV_10000cm_80X'  :  "/AMSB_chargino_M-200_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_300GeV_10cm_80X'    :  "/AMSB_chargino_M-300_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_100cm_80X'   :  "/AMSB_chargino_M-300_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_1000cm_80X'  :  "/AMSB_chargino_M-300_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_10000cm_80X'  :  "/AMSB_chargino_M-300_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_400GeV_10cm_80X'    :  "/AMSB_chargino_M-400_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_400GeV_100cm_80X'   :  "/AMSB_chargino_M-400_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_400GeV_1000cm_80X'  :  "/AMSB_chargino_M-400_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_400GeV_10000cm_80X'  :  "/AMSB_chargino_M-400_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_500GeV_10cm_80X'    :  "/AMSB_chargino_M-500_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_100cm_80X'   :  "/AMSB_chargino_M-500_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_1000cm_80X'  :  "/AMSB_chargino_M-500_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_10000cm_80X'  :  "/AMSB_chargino_M-500_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_600GeV_10cm_80X'    :  "/AMSB_chargino_M-600_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_600GeV_100cm_80X'   :  "/AMSB_chargino_M-600_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_600GeV_1000cm_80X'  :  "/AMSB_chargino_M-600_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_600GeV_10000cm_80X'  :  "/AMSB_chargino_M-600_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_700GeV_10cm_80X'    :  "/AMSB_chargino_M-700_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_100cm_80X'   :  "/AMSB_chargino_M-700_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_1000cm_80X'  :  "/AMSB_chargino_M-700_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_10000cm_80X'  :  "/AMSB_chargino_M-700_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
}

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
