from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
import copy
import os
import re

# Change this to True if you want to use CandidateTracks in ntuples instead of IsolatedTracks in standard MINIAOD
# This is perhaps a weird place to put this switch, but this is the first DisappTrks module imported in protoConfig
UseCandidateTracks = False

# Change this to True if you want to use prunedGenParticlePlusGeant for hardInteractionMcparticles 
# instead of prunedGenParticles
UseGeantDecays = False

print "########################################################################"
print "# Switching the following since the release is " + os.environ["CMSSW_VERSION"] + ":"
print "#"

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Datasets from: miniAOD_80X_Samples"
    from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
    print "# Backgorund samples from: miniAODV2Samples"
    from DisappTrks.StandardAnalysis.miniAODV2Samples import dataset_names_bkgd
    dataset_names.update (dataset_names_bkgd)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Datasets from: miniAOD_94X_Samples"
    print "# Background samples from: miniAOD_94X_Samples (should be updated with MiniAODv2!)"
    from DisappTrks.StandardAnalysis.miniAOD_94X_Samples import *
    if UseCandidateTracks:
        print "#                (using CandidateTrack ntuples from miniAOD_94X_Samples in data)"
        dataset_names.update(datasets_names_data_ntuples)
        dataset_names.update(dataset_names_sig_ntuples)
else:
    print "# Datasets and background samples from: miniAODV2Samples"
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
    'TTJets',
]
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
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Signal samples: 80X samples"
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_80X", datasetsSig[i])
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Signal samples: 94X samples"
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_94X", datasetsSig[i])
else:
    print "# Signal samples: 76X samples"

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigShort100 = datasetsSig[0:4]
datasetsSigShort200 = datasetsSig[4:8]
datasetsSigShort300 = datasetsSig[8:12]
datasetsSigShort400 = datasetsSig[12:16]
datasetsSigShort500 = datasetsSig[16:20]
datasetsSigShort600 = datasetsSig[20:24]
datasetsSigShort700 = datasetsSig[24:28]
datasetsSigShort800 = datasetsSig[28:32]
datasetsSigShort900 = datasetsSig[32:36]

addLifetimeReweighting (datasetsSig)

composite_dataset_definitions["allBkgd"] = datasetsBkgd

composite_dataset_definitions['SingleTop'] = [
    'SingleTop_s_channel',
    'SingleTop_t_channel',
    'SingleTop_tW',
    'SingleTop_tbarW',
]

composite_dataset_definitions["WW"] = [
    'WWToLNuQQ',
    'WWToLNuLNu',
]

composite_dataset_definitions["VG"] = [
    'WG',
    'ZG',
]

composite_dataset_definitions["VV"] = [
    'WWToLNuQQ',
    'WWToLNuLNu',
    'WZ',
    'ZZ',
    'WG',
    'ZG',
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    composite_dataset_definitions['ZJetsToNuNu'] = [
        'ZJetsToNuNu_HT100to200',
        'ZJetsToNuNu_HT200to400',
        'ZJetsToNuNu_HT400to600',
        'ZJetsToNuNu_HT600to800',
        'ZJetsToNuNu_HT800to1200',
        'ZJetsToNuNu_HT1200to2500',
        'ZJetsToNuNu_HT2500toInf',
    ]
    composite_dataset_definitions['TTJets'] = [
        'TTJets_2L2Nu',
        'TTJets_SemiLeptonic',
        'TTJets_Hadronic',
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
        if re.match (r"DYJetsToLL_50", a) or re.match (r"WZ", a) or re.match (r"WZToLNuNuNu", a):
            b = re.sub (r"(.*)", r"\1_2016MC", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and attribute == "labels":
                newKeys[b] = re.sub (r"(.*)", r"\1 (2016 MC)", newKeys[b])
    locals ()[attribute].update (newKeys)
