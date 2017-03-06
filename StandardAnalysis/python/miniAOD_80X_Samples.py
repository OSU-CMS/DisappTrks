#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2016 80X DATASETS  ##################################################################
############################################################################################################

dataset_names_data = {

    # Remade PromptReco ntuples are commented out for now.

    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################

    # MET 23Sep2016
    'MET_2016B'       : "/MET/ahart-Run2016B-23Sep2016-v3-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER",
    'MET_2016C'       : "/MET/ahart-Run2016C-23Sep2016-v1-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER",
    'MET_2016D'       : "/MET/ahart-Run2016D-23Sep2016-v1-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER",
    'MET_2016E'       : "/MET/ahart-Run2016E-23Sep2016-v1-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER",
    'MET_2016F'       : "/MET/ahart-Run2016F-23Sep2016-v1-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER",
    'MET_2016G'       : "/MET/ahart-Run2016G-23Sep2016-v1-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER",
    'MET_2016H'       : ["/MET/ahart-Run2016H-PromptReco-v2-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER", "/MET/ahart-Run2016H-PromptReco-v3-DisappTrks-v1-58d73df75df4f7c009ddc0cc54b0773f/USER"],

    # MET 2016 PromptReco
    #'MET_2016C'       : "/MET/ahart-Run2016C-PromptReco-v2-DisappTrks-v8-58d73df75df4f7c009ddc0cc54b0773f/USER",
    #'MET_2016F'       : "/MET/ahart-Run2016F-PromptReco-v1-DisappTrks-v8-58d73df75df4f7c009ddc0cc54b0773f/USER",
    #'MET_2016G'       : "/MET/ahart-Run2016G-PromptReco-v1-DisappTrks-v8-58d73df75df4f7c009ddc0cc54b0773f/USER",

    # SingleEle PromptReco
    #'SingleEle_2016B' : "/SingleElectron/bfrancis-Run2016B-PromptReco-v2-DisappTrks-v8-addfbe4d6f0cf1056130ceadde75d969/USER",
    #'SingleEle_2016C' : "/SingleElectron/bfrancis-Run2016C-PromptReco-v2-DisappTrks-v8-addfbe4d6f0cf1056130ceadde75d969/USER",
    #'SingleEle_2016D' : "/SingleElectron/bfrancis-Run2016D-PromptReco-v2-DisappTrks-v8-addfbe4d6f0cf1056130ceadde75d969/USER",
    #'SingleEle_2016E' : "/SingleElectron/bfrancis-Run2016E-PromptReco-v2-DisappTrks-v8-addfbe4d6f0cf1056130ceadde75d969/USER",
    #'SingleEle_2016F' : "/SingleElectron/bfrancis-Run2016F-PromptReco-v1-DisappTrks-v8-addfbe4d6f0cf1056130ceadde75d969/USER",
    #'SingleEle_2016G' : "/SingleElectron/bfrancis-Run2016G-PromptReco-v1-DisappTrks-v8-v2-addfbe4d6f0cf1056130ceadde75d969/USER",
    #'SingleEle_2016H' : ["/SingleElectron/bfrancis-Run2016H-PromptReco-v2-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER", "/SingleElectron/bfrancis-Run2016H-PromptReco-v3-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER"],

    # SingleEle 23Sep2016 rereco
    'SingleEle_2016B' : "/SingleElectron/bfrancis-Run2016B-23Sep2016-v3-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER",
    'SingleEle_2016C' : "/SingleElectron/bfrancis-Run2016C-23Sep2016-v1-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER",
    'SingleEle_2016D' : "/SingleElectron/bfrancis-Run2016D-23Sep2016-v1-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER",
    'SingleEle_2016E' : "/SingleElectron/bfrancis-Run2016E-23Sep2016-v1-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER",
    'SingleEle_2016F' : "/SingleElectron/bfrancis-Run2016F-23Sep2016-v1-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER",
    'SingleEle_2016G' : "/SingleElectron/bfrancis-Run2016G-23Sep2016-v1-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER",
    'SingleEle_2016H' : ["/SingleElectron/bfrancis-Run2016H-PromptReco-v2-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER", "/SingleElectron/bfrancis-Run2016H-PromptReco-v3-DisappTrks-v1-addfbe4d6f0cf1056130ceadde75d969/USER"],

    # SingleMu 23Sep2016
    'SingleMu_2016B'  : "/SingleMuon/ahart-Run2016B-23Sep2016-v3-DisappTrks-v1-ba21f67961b05c35438052e716a22b53/USER",
    'SingleMu_2016C'  : "/SingleMuon/wulsin-Run2016C-23Sep2016-v1-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER",
    'SingleMu_2016D'  : "/SingleMuon/wulsin-Run2016D-23Sep2016-v1-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER",
    'SingleMu_2016E'  : "/SingleMuon/wulsin-Run2016E-23Sep2016-v1-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER",
    'SingleMu_2016F'  : "/SingleMuon/wulsin-Run2016F-23Sep2016-v1-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER",
    'SingleMu_2016G'  : "/SingleMuon/wulsin-Run2016G-23Sep2016-v1-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER",
    'SingleMu_2016H'  : ["/SingleMuon/ahart-Run2016H-PromptReco-v2-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER", "/SingleMuon/wulsin-Run2016H-PromptReco-v3-DisappTrks-v2-c0937f7e1b09431ec4046954bdd16494/USER"],

    # SingleMu 2016 PromptReco
    #'SingleMu_2016C'  : "/SingleMuon/ahart-Run2016C-PromptReco-v2-DisappTrks-v8-c0937f7e1b09431ec4046954bdd16494/USER",
    #'SingleMu_2016G'  : "/SingleMuon/ahart-Run2016G-PromptReco-v1-DisappTrks-v8-c0937f7e1b09431ec4046954bdd16494/USER",

    # Tau PromptReco
    #'Tau_2016B'        : "/Tau/bfrancis-Run2016B-PromptReco-v2-DisappTrks-v8-e69bca4a9575e4a5110aaa47eb9af51b/USER",
    #'Tau_2016C'        : "/Tau/bfrancis-Run2016C-PromptReco-v2-DisappTrks-v8-e69bca4a9575e4a5110aaa47eb9af51b/USER",
    #'Tau_2016D'        : "/Tau/bfrancis-Run2016D-PromptReco-v2-DisappTrks-v8-e69bca4a9575e4a5110aaa47eb9af51b/USER",
    #'Tau_2016E'        : "/Tau/bfrancis-Run2016E-PromptReco-v2-DisappTrks-v8-e69bca4a9575e4a5110aaa47eb9af51b/USER",
    #'Tau_2016F'        : "/Tau/bfrancis-Run2016F-PromptReco-v1-DisappTrks-v8-e69bca4a9575e4a5110aaa47eb9af51b/USER",
    #'Tau_2016G'        : "/Tau/bfrancis-Run2016G-PromptReco-v1-DisappTrks-v8-v2-e69bca4a9575e4a5110aaa47eb9af51b/USER",
    #'Tau_2016H'        :  ["/Tau/ahart-Run2016H-PromptReco-v2-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER", "/Tau/ahart-Run2016H-PromptReco-v3-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER"],

    # Tau 23Sep2016
    'Tau_2016B'        :  "/Tau/ahart-Run2016B-23Sep2016-v3-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER",
    'Tau_2016C'        :  "/Tau/ahart-Run2016C-23Sep2016-v1-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER",
    'Tau_2016D'        :  "/Tau/ahart-Run2016D-23Sep2016-v1-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER",
    'Tau_2016E'        :  "/Tau/ahart-Run2016E-23Sep2016-v1-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER",
    'Tau_2016F'        :  "/Tau/ahart-Run2016F-23Sep2016-v1-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER",
    'Tau_2016G'        :  "/Tau/ahart-Run2016G-23Sep2016-v1-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER",
    'Tau_2016H'        :  ["/Tau/ahart-Run2016H-PromptReco-v2-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER", "/Tau/ahart-Run2016H-PromptReco-v3-DisappTrks-v1-baeccab93c8c5cab5837a97f96996439/USER"],

    'ZeroBias_2016C' : "/ZeroBias/ahart-Run2016C-PromptReco-v2-DisappTrks-v8-369b4fc9d4b0224d59848b34d927552e/USER",
    'ZeroBias_2016D' : "/ZeroBias/ahart-Run2016D-PromptReco-v2-DisappTrks-v8-369b4fc9d4b0224d59848b34d927552e/USER",
    'ZeroBias_2016E' : "/ZeroBias/ahart-Run2016E-PromptReco-v2-DisappTrks-v8-369b4fc9d4b0224d59848b34d927552e/USER",
    'ZeroBias_2016F' : "/ZeroBias/ahart-Run2016F-PromptReco-v1-DisappTrks-v8-369b4fc9d4b0224d59848b34d927552e/USER",
    'ZeroBias_2016H' : ["/ZeroBias/ahart-Run2016H-PromptReco-v2-DisappTrks-v8-369b4fc9d4b0224d59848b34d927552e/USER", "/ZeroBias/ahart-Run2016H-PromptReco-v3-DisappTrks-v8-369b4fc9d4b0224d59848b34d927552e/USER"],
}

dataset_names_bkgd = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
    'DYJetsToLL_50'      :  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM",
    'WJetsToLNu'  :  "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM",
}

dataset_names_sig = {
    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################
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
