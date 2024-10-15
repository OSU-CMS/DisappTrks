from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.Color import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
import copy
import os
import re

# Change this to False if you want to use IsolatedTracks instead of CandidateTracks in ntuples
# This is perhaps a weird place to put this switch, but this is the first DisappTrks module imported in protoConfig
UseCandidateTracks = False

# If this is true (76X and 80X) then prunedGenParticlePlusGeant will be used for hardInteractionMcparticles
# instead of prunedGenParticles
UseGeantDecays = (not os.environ['CMSSW_VERSION'].startswith('CMSSW_9_4_') and not os.environ['CMSSW_VERSION'].startswith('CMSSW_10_2_') and not os.environ['CMSSW_VERSION'].startswith('CMSSW_12_4_') and not os.environ['CMSSW_VERSION'].startswith('CMSSW_13_0_'))

print("########################################################################")
print("# Switching the following since the release is " + A_BRIGHT_BLUE + os.environ["CMSSW_VERSION"] + A_RESET + ":")
print("#")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_80X_Samples" + A_RESET)
    from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
    print("# Backgorund samples from: " + A_BRIGHT_CYAN + "miniAODV2Samples" + A_RESET)
    from DisappTrks.StandardAnalysis.miniAODV2Samples import dataset_names_bkgd
    dataset_names.update (dataset_names_bkgd)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    if UseCandidateTracks:
        print("# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_94X_Ntuples" + A_RESET)
        print("# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_94X_Ntuples" + A_RESET)
        from DisappTrks.StandardAnalysis.miniAOD_94X_Ntuples import *
    else:
        print("# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_94X_Samples" + A_RESET)
        print("# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_94X_Samples" + A_RESET)
        from DisappTrks.StandardAnalysis.miniAOD_94X_Samples import *
        lumi.update (CreateCompositeLumis (lumi_2017, '2017', 'BCDEF'))
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    if UseCandidateTracks:
        print("# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_102X_Ntuples" + A_RESET)
        print("# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_102X_Ntuples" + A_RESET)
        from DisappTrks.StandardAnalysis.miniAOD_102X_Ntuples import *
    else:
        print("# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_102X_Samples" + A_RESET)
        print("# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_102X_Samples" + A_RESET + " (" + A_BRIGHT_YELLOW + "empty!" + A_RESET + ")")
        from DisappTrks.StandardAnalysis.miniAOD_102X_Samples import *
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    if UseCandidateTracks:
        print("CandidateTracks not supported please change UseCandidaeTracks bool to false in config_cfg.py")
    else:
        print("# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_124X_Samples" + A_RESET)
        print("# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_124X_Samples" + A_RESET + " (" + A_BRIGHT_YELLOW + "empty!" + A_RESET + ")")
        from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import *
else:
    print("# Datasets and background samples from: " + A_BRIGHT_CYAN + "miniAODV2Samples" + A_RESET)
    from DisappTrks.StandardAnalysis.miniAODV2Samples import *

config_file = "config_cfg.py"

InputCondorArguments = {
    'request_memory': '2048MB',
    'request_cpus': '1',
}

datasetsBkgd = [
    'QCD',
    'DYJetsToLL',
    'ZJetsToNuNu',
    'VV',
    'SingleTop',
]
#TODO: need to check what this does and if it is useful or not for run3 CMSSW_12_4_ CMSSW_13_0_
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
#    datasetsBkgd.append('TTJetsComposite')
#else:
#    datasetsBkgd.append('TTJets')

datasetsBkgdForMET = copy.deepcopy(datasetsBkgd)

datasetsBkgd.append ('WJetsToLNu')
datasetsBkgdForMET.append ('WJetsToLNu_HT')

datasetsSig = [
    'AMSB_chargino_100GeV_10cm_76X',
    'AMSB_chargino_100GeV_100cm_76X',
    'AMSB_chargino_100GeV_1000cm_76X',
    'AMSB_chargino_100GeV_10000cm_76X',

    'AMSB_chargino_200GeV_10cm_76X',
    'AMSB_chargino_200GeV_100cm_76X',
    'AMSB_chargino_200GeV_1000cm_76X',
    'AMSB_chargino_200GeV_10000cm_76X',

    'AMSB_chargino_300GeV_10cm_76X',
    'AMSB_chargino_300GeV_100cm_76X',
    'AMSB_chargino_300GeV_1000cm_76X',
    'AMSB_chargino_300GeV_10000cm_76X',

    'AMSB_chargino_400GeV_10cm_76X',
    'AMSB_chargino_400GeV_100cm_76X',
    'AMSB_chargino_400GeV_1000cm_76X',
    'AMSB_chargino_400GeV_10000cm_76X',

    'AMSB_chargino_500GeV_10cm_76X',
    'AMSB_chargino_500GeV_100cm_76X',
    'AMSB_chargino_500GeV_1000cm_76X',
    'AMSB_chargino_500GeV_10000cm_76X',

    'AMSB_chargino_600GeV_10cm_76X',
    'AMSB_chargino_600GeV_100cm_76X',
    'AMSB_chargino_600GeV_1000cm_76X',
    'AMSB_chargino_600GeV_10000cm_76X',

    'AMSB_chargino_700GeV_10cm_76X',
    'AMSB_chargino_700GeV_100cm_76X',
    'AMSB_chargino_700GeV_1000cm_76X',
    'AMSB_chargino_700GeV_10000cm_76X',

    'AMSB_chargino_800GeV_10cm_76X',
    'AMSB_chargino_800GeV_100cm_76X',
    'AMSB_chargino_800GeV_1000cm_76X',
    'AMSB_chargino_800GeV_10000cm_76X',

    'AMSB_chargino_900GeV_10cm_76X',
    'AMSB_chargino_900GeV_100cm_76X',
    'AMSB_chargino_900GeV_1000cm_76X',
    'AMSB_chargino_900GeV_10000cm_76X',

    'AMSB_chargino_1000GeV_10cm_76X',
    'AMSB_chargino_1000GeV_100cm_76X',
    'AMSB_chargino_1000GeV_1000cm_76X',
    'AMSB_chargino_1000GeV_10000cm_76X',

    'AMSB_chargino_1100GeV_10cm_76X',
    'AMSB_chargino_1100GeV_100cm_76X',
    'AMSB_chargino_1100GeV_1000cm_76X',
    'AMSB_chargino_1100GeV_10000cm_76X',

    'AMSB_chargino_1200GeV_10cm_76X',
    'AMSB_chargino_1200GeV_100cm_76X',
    'AMSB_chargino_1200GeV_1000cm_76X',
    'AMSB_chargino_1200GeV_10000cm_76X',

    'AMSB_chargino_700GeV_100cm_124X',
]

datasetsSigHiggsino = []

if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith("CMSSW_13_0_"):
    datasetsSigHiggsino = [
        'Higgsino_100GeV_10cm_76X',
        'Higgsino_100GeV_100cm_76X',
        'Higgsino_100GeV_1000cm_76X',
        'Higgsino_100GeV_10000cm_76X',

        'Higgsino_200GeV_10cm_76X',
        'Higgsino_200GeV_100cm_76X',
        'Higgsino_200GeV_1000cm_76X',
        'Higgsino_200GeV_10000cm_76X',

        'Higgsino_300GeV_10cm_76X',
        'Higgsino_300GeV_100cm_76X',
        'Higgsino_300GeV_1000cm_76X',
        'Higgsino_300GeV_10000cm_76X',

        'Higgsino_400GeV_10cm_76X',
        'Higgsino_400GeV_100cm_76X',
        'Higgsino_400GeV_1000cm_76X',
        'Higgsino_400GeV_10000cm_76X',

        'Higgsino_500GeV_10cm_76X',
        'Higgsino_500GeV_100cm_76X',
        'Higgsino_500GeV_1000cm_76X',
        'Higgsino_500GeV_10000cm_76X',

        'Higgsino_600GeV_10cm_76X',
        'Higgsino_600GeV_100cm_76X',
        'Higgsino_600GeV_1000cm_76X',
        'Higgsino_600GeV_10000cm_76X',

        'Higgsino_700GeV_10cm_76X',
        'Higgsino_700GeV_100cm_76X',
        'Higgsino_700GeV_1000cm_76X',
        'Higgsino_700GeV_10000cm_76X',

        'Higgsino_800GeV_10cm_76X',
        'Higgsino_800GeV_100cm_76X',
        'Higgsino_800GeV_1000cm_76X',
        'Higgsino_800GeV_10000cm_76X',
    
        'Higgsino_900GeV_10cm_76X',
        'Higgsino_900GeV_100cm_76X',
        'Higgsino_900GeV_1000cm_76X',
        'Higgsino_900GeV_10000cm_76X',

        'Higgsino_1000GeV_10cm_76X',
        'Higgsino_1000GeV_100cm_76X',
        'Higgsino_1000GeV_1000cm_76X',
        'Higgsino_1000GeV_10000cm_76X',
    ]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# Signal samples: " + A_BRIGHT_CYAN + "80X samples" + A_RESET)
    for i in range (0, len (datasetsSig)):
        datasetsSig[i]         = re.sub (r"(.*)_76X$", r"\1_80X", datasetsSig[i])
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print("# Signal samples: " + A_BRIGHT_CYAN + "94X samples" + A_RESET)
    for i in range (0, len (datasetsSig)):
        datasetsSig[i]         = re.sub (r"(.*)_76X$", r"\1_94X", datasetsSig[i])
    for i in range (0, len (datasetsSigHiggsino)):
        datasetsSigHiggsino[i] = re.sub (r"(.*)_76X$", r"\1_94X", datasetsSigHiggsino[i])
    for i in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]:
        datasetsSig.append('AMSB_chargino_' + str(i) + 'GeV_1cm_94X')
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print("# Signal samples: " + A_BRIGHT_CYAN + "102X samples" + A_RESET)
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_102X", datasetsSig[i])
    for i in range (0, len (datasetsSigHiggsino)):
        datasetsSigHiggsino[i] = re.sub (r"(.*)_76X$", r"\1_102X", datasetsSigHiggsino[i])
    for i in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]:
        datasetsSig.append('AMSB_chargino_' + str(i) + 'GeV_1cm_102X')
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("# Signal samples: " + A_BRIGHT_CYAN + "130X samples" + A_RESET)
    for i in range(0, len(datasetsSig)):
       datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_130X", datasetsSig[i])
    for i in range (0, len (datasetsSigHiggsino)):
       datasetsSigHiggsino[i] = re.sub (r"(.*)_76X$", r"\1_130X", datasetsSigHiggsino[i])
    for i in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]:
       datasetsSig.append('AMSB_chargino_' + str(i) + 'GeV_1cm_130X')
else:
    print("# Signal samples: " + A_BRIGHT_CYAN + "76X samples" + A_RESET)

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigShort100 = [x for x in datasetsSig if x.startswith('AMSB_chargino_100GeV_')]
datasetsSigShort200 = [x for x in datasetsSig if x.startswith('AMSB_chargino_200GeV_')]
datasetsSigShort300 = [x for x in datasetsSig if x.startswith('AMSB_chargino_300GeV_')]
datasetsSigShort400 = [x for x in datasetsSig if x.startswith('AMSB_chargino_400GeV_')]
datasetsSigShort500 = [x for x in datasetsSig if x.startswith('AMSB_chargino_500GeV_')]
datasetsSigShort600 = [x for x in datasetsSig if x.startswith('AMSB_chargino_600GeV_')]
datasetsSigShort700 = [x for x in datasetsSig if x.startswith('AMSB_chargino_700GeV_')]
datasetsSigShort800 = [x for x in datasetsSig if x.startswith('AMSB_chargino_800GeV_')]
datasetsSigShort900 = [x for x in datasetsSig if x.startswith('AMSB_chargino_900GeV_')]
datasetsSigShort1000 = [x for x in datasetsSig if x.startswith('AMSB_chargino_1000GeV_')]
datasetsSigShort1100 = [x for x in datasetsSig if x.startswith('AMSB_chargino_1100GeV_')]
datasetsSigShort1200 = [x for x in datasetsSig if x.startswith('AMSB_chargino_1200GeV_')]

datasetsSigHiggsinoShort = copy.deepcopy(datasetsSigHiggsino)

datasetsSigHiggsinoShort100 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_100GeV_')]
datasetsSigHiggsinoShort200 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_200GeV_')]
datasetsSigHiggsinoShort300 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_300GeV_')]
datasetsSigHiggsinoShort400 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_400GeV_')]
datasetsSigHiggsinoShort500 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_500GeV_')]
datasetsSigHiggsinoShort600 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_600GeV_')]
datasetsSigHiggsinoShort700 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_700GeV_')]
datasetsSigHiggsinoShort800 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_800GeV_')]
datasetsSigHiggsinoShort900 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_900GeV_')]
datasetsSigHiggsinoShort1000 = [x for x in datasetsSigHiggsino if x.startswith('Higgsino_1000GeV_')]

#TODO: update this to use the existing MC signal samples when everything works!!!
#addLifetimeReweighting (datasetsSig)
#addLifetimeReweighting (datasetsSigHiggsino, isHiggsino = True)

higgsino_xsecs = { # [pb]
    '100' : 13.53557,
    '200' : 1.092653,
    '300' : 0.2342024,
    '400' : 0.0731865,
    '500' : 0.02798925,
    '600' : 0.0121587,
    '700' : 0.00572751,
    '800' : 0.002878806,
    '900' : 0.001502429,
    '1000' : 0.001502429,
}

# set the cross sections for Higgsino samples
for x in types:
    if not x.startswith('Higgsino_'):
        continue
    mass = re.sub (r'Higgsino_([^_]*)GeV_[^_]*cm_.*', r'\1', x)
    crossSections[x] = higgsino_xsecs[mass]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasetsSigOSU         = copy.deepcopy([x for x in datasetsSig      if x.split('_')[2][:-3] in ['100', '300', '500', '700', '900', '1000', '1100']])
    datasetsSigShortOSU    = copy.deepcopy([x for x in datasetsSigShort if x.split('_')[2][:-3] in ['100', '300', '500', '700', '900', '1000', '1100']])
    datasetsSigPurdue      = copy.deepcopy([x for x in datasetsSig      if x.split('_')[2][:-3] in ['200', '400', '600', '800']])
    datasetsSigShortPurdue = copy.deepcopy([x for x in datasetsSigShort if x.split('_')[2][:-3] in ['200', '400', '600', '800']])

composite_dataset_definitions["allBkgd"] = datasetsBkgd
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    composite_dataset_definitions['DYJetsToLL'] = [
        'DYJetsToLL_50',
        'DYJetsToLL_10to50',
    ]
    composite_dataset_definitions['SingleTop'] = [
        'SingleTop_s_channel',
        'SingleTop_t_channel_top',
        'SingleTop_t_channel_antitop',
        'SingleTop_tW',
        'SingleTop_tbarW',
    ]
    composite_dataset_definitions['TTJetsComposite'] = [
        'TTJets_SemiLeptonic',
        'TTJets_2L2Nu',
        'TTJets_Hadronic',        
    ]
    # no 5-10, 10-15 samples in 102X
    composite_dataset_definitions['QCD'] = [
        'QCD_15to30',
        'QCD_30to50',
        'QCD_50to80',
        'QCD_80to120',
        'QCD_120to170',
        'QCD_170to300',
        'QCD_300to470',
        'QCD_470to600',
        'QCD_600to800',
        'QCD_800to1000',
        'QCD_1000to1400',
        'QCD_1400to1800',
        'QCD_1800to2400',
        'QCD_2400to3200',
        'QCD_3200toInf',
    ]
    composite_dataset_definitions['ZJetsToNuNu'] = [
        'ZJetsToNuNu_HT100to200',
        'ZJetsToNuNu_HT200to400',
        'ZJetsToNuNu_HT400to600',
        'ZJetsToNuNu_HT600to800',
        'ZJetsToNuNu_HT800to1200',
        'ZJetsToNuNu_HT1200to2500',
        'ZJetsToNuNu_HT2500toInf',
    ]
    composite_dataset_definitions["VV"] = [
        'WW',
        'WZ',
        'ZZ',
    ]
    composite_dataset_definitions["VG"] = [
        'WG',
        'ZG',
    ]
    composite_dataset_definitions['WJetsToLNu_HT'] = [
        'WJetsToLNu_HT70to100',
        'WJetsToLNu_HT100to200',
        'WJetsToLNu_HT200to400',
        'WJetsToLNu_HT400to600',
        'WJetsToLNu_HT600to800',
        'WJetsToLNu_HT800to1200',
        'WJetsToLNu_HT1200to2500',
        'WJetsToLNu_HT2500toInf',
    ]
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    composite_dataset_definitions['DYJetsToLL'] = [
        'DYJetsToLL_50',
        'DYJetsToLL_5to50',
    ]
    composite_dataset_definitions['SingleTop'] = [
        'SingleTop_s_channel',
        'SingleTop_t_channel_top',
        'SingleTop_t_channel_antitop',
        'SingleTop_tW',
        'SingleTop_tbarW',
    ]
    composite_dataset_definitions['TTJetsComposite'] = [
        'TTJets_2L2Nu',
        'TTJets_SemiLeptonic',
        'TTJets_Hadronic',
    ]
    # no 5-10, 10-15 samples in 94X
    composite_dataset_definitions['QCD'] = [
        'QCD_15to30',
        'QCD_30to50',
        'QCD_50to80',
        'QCD_80to120',
        'QCD_120to170',
        'QCD_170to300',
        'QCD_300to470',
        'QCD_470to600',
        'QCD_600to800',
        'QCD_800to1000',
        'QCD_1000to1400',
        'QCD_1400to1800',
        'QCD_1800to2400',
        'QCD_2400to3200',
        'QCD_3200toInf',
    ]
    composite_dataset_definitions['ZJetsToNuNu'] = [
        'ZJetsToNuNu_HT100to200',
        'ZJetsToNuNu_HT200to400',
        'ZJetsToNuNu_HT400to600',
        'ZJetsToNuNu_HT600to800',
        'ZJetsToNuNu_HT800to1200',
        'ZJetsToNuNu_HT1200to2500',
        'ZJetsToNuNu_HT2500toInf',
    ]
    composite_dataset_definitions["VV"] = [
        #'WWToLNuQQ',
        #'WWToLNuLNu',
        'WW',
        'WZ',
        'ZZ',
        #'WG',
        #'ZG',
    ]
    composite_dataset_definitions["VG"] = [
        'WG',
        #'ZG',
    ]
    composite_dataset_definitions['WJetsToLNu_HT'] = [
        'WJetsToLNu_HT100to200',
        'WJetsToLNu_HT200to400',
        'WJetsToLNu_HT400to600',
        'WJetsToLNu_HT600to800',
        'WJetsToLNu_HT800to1200',
        #'WJetsToLNu_HT1200to2500',
        'WJetsToLNu_HT2500toInf',
    ]
else:
    composite_dataset_definitions['SingleTop'] = [
        'SingleTop_s_channel',
        'SingleTop_t_channel',
        'SingleTop_tW',
        'SingleTop_tbarW',
    ]
    composite_dataset_definitions["VV"] = [
        'WWToLNuQQ',
        'WWToLNuLNu',
        'WZ',
        'ZZ',
        'WG',
        'ZG',
    ]
    composite_dataset_definitions["VG"] = [
        'WG',
        'ZG',
    ]
    composite_dataset_definitions['WJetsToLNu_HT'] = [
        'WJetsToLNu_HT100to200',
        'WJetsToLNu_HT200to400',
        'WJetsToLNu_HT400to600',
        'WJetsToLNu_HT600toInf',
    ]

types["WW"] = "bgMC"
types["WZ"] = "bgMC"
types["ZZ"] = "bgMC"
types["VG"] = "bgMC"
types["VV"] = "bgMC"
types["allBkgd"] = "bkMC"

colors["WW"] = 390
colors["WZ"] = 393
colors["ZZ"] = 397
colors["VG"] = 400
colors["VV"] = 800
colors["TTJets"] = 870 # kAzure+10
colors["allBkgd"] = 601

labels["DYJetsToLL_50"] = "Z#rightarrowll"
labels["DYJetsToLL"] = "Z#rightarrowll"
labels["DYJetsToNuNu"] = "Z#rightarrow#nu#bar{#nu}"
labels["WJetsToLNu"] = "W#rightarrowl#nu"
labels["WJetsToLNu_HT"] = "W#rightarrowl#nu"
labels["WW"] = "WW"
labels["WZ"] = "WZ"
labels["ZZ"] = "ZZ"
labels["VG"] = "V#gamma"
labels["VV"] = "Diboson"
labels["allBkgd"] = "Total bkgd"

# add dataset attributes for 2016BC and 2016DEFGH
for attribute in list (locals ()):
    if not isinstance (locals ()[attribute], dict) or attribute.startswith ("lumi"):
        continue
    newKeys = {}
    for a in locals ()[attribute]:
        if not type(a) is str:
            continue
        if re.match (r".*2016B.*", a):
            b = re.sub (r"(.*)2016B(.*)", r"\g<1>2016BC\2", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and re.match (r".*2016B.*", newKeys[b]):
                newKeys[b] = re.sub (r"(.*)2016B(.*)", r"\g<1>2016B+C\2", newKeys[b])
        if re.match (r".*2016D.*", a):
            b = re.sub (r"(.*)2016D(.*)", r"\g<1>2016DEFGH\2", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and re.match (r".*2016D.*", newKeys[b]):
                newKeys[b] = re.sub (r"(.*)2016D(.*)", r"\g<1>2016D-H\2", newKeys[b])
    locals ()[attribute].update (newKeys)

# add dataset attributes for 2016 MC
for attribute in list (locals ()):
    if not isinstance (locals ()[attribute], dict) or attribute.startswith ("lumi") or attribute == "dataset_names":
        continue
    newKeys = {}
    for a in locals ()[attribute]:
        if not type(a) is str:
            continue
        if re.match (r"DYJetsToLL_50", a) or re.match (r"WZ", a) or re.match (r"WZToLNuNuNu", a):
            b = re.sub (r"(.*)", r"\1_2016MC", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and attribute == "labels":
                newKeys[b] = re.sub (r"(.*)", r"\1 (2016 MC)", newKeys[b])
    locals ()[attribute].update (newKeys)
