from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

config_file = "protoConfig_cfg.py"

intLumi = 628.76



datasetsBkgd = [
    'WJetsToLNu_MiniAOD',
    'TTJets_Lept_MiniAOD',
    'SingleTop_MiniAOD',
    'VV_MiniAOD',

    'DYJetsToNuNu_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
]

datasetsData = [
    'MET_2015D_05Oct2015',
]

datasetsSig = [
    'AMSB_chargino_100GeV_10cm',
    'AMSB_chargino_100GeV_100cm',
    'AMSB_chargino_100GeV_1000cm',

    'AMSB_chargino_300GeV_10cm',
    'AMSB_chargino_300GeV_100cm',
    'AMSB_chargino_300GeV_1000cm',

    'AMSB_chargino_500GeV_10cm',
    'AMSB_chargino_500GeV_100cm',
    'AMSB_chargino_500GeV_1000cm',

    'AMSB_chargino_700GeV_10cm',
    'AMSB_chargino_700GeV_100cm',
    'AMSB_chargino_700GeV_1000cm',
]

datasets = datasetsBkgd + datasetsData + datasetsSig  

composite_dataset_definitions["WW_MiniAOD"] = [
    'WWToLNuQQ_MiniAOD',
    'WWToLNuLNu_MiniAOD',
]

composite_dataset_definitions["WZ_MiniAOD"] = [
    'WZToLNuQQ_MiniAOD',
    #'WZToLLQQ_MiniAOD',
    'WZToLNuNuNu_MiniAOD',
    'WZToLLLNu_MiniAOD',
]

composite_dataset_definitions["ZZ_MiniAOD"] = [
    'ZZToNuNuQQ_MiniAOD',
    'ZZToLLQQ_MiniAOD',
    'ZZToLLNuNu_MiniAOD',
    'ZZToLLLL_MiniAOD',
]

composite_dataset_definitions["VG_MiniAOD"] = [
    'WG_MiniAOD',
    'ZG_MiniAOD',
]

composite_dataset_definitions["VV_MiniAOD"] = [
    'WWToLNuQQ_MiniAOD',
    'WWToLNuLNu_MiniAOD',
    'WZToLNuQQ_MiniAOD',
    #'WZToLLQQ_MiniAOD',
    'WZToLNuNuNu_MiniAOD',
    'WZToLLLNu_MiniAOD',
    'ZZToNuNuQQ_MiniAOD',
    'ZZToLLQQ_MiniAOD',
    'ZZToLLNuNu_MiniAOD',
    'ZZToLLLL_MiniAOD',
    'WG_MiniAOD',
    'ZG_MiniAOD',
]

types["WW_MiniAOD"] = "bgMC"
types["WZ_MiniAOD"] = "bgMC"
types["ZZ_MiniAOD"] = "bgMC"
types["VG_MiniAOD"] = "bgMC"
types["VV_MiniAOD"] = "bgMC"

colors["WW_MiniAOD"] = 390
colors["WZ_MiniAOD"] = 393
colors["ZZ_MiniAOD"] = 397
colors["VG_MiniAOD"] = 400
colors["VV_MiniAOD"] = 393

labels["DYJetsToLL_50_MiniAOD"] = "Z#rightarrowl^{+}l^{-}"
labels["DYJetsToNuNu_MiniAOD"] = "Z#rightarrow#nu#bar{#nu}"
labels["WJetsToLNu_MiniAOD"] = "W#rightarrowl#nu"
labels["WW_MiniAOD"] = "WW"
labels["WZ_MiniAOD"] = "WZ"
labels["ZZ_MiniAOD"] = "ZZ"
labels["VG_MiniAOD"] = "V#gamma"
labels["VV_MiniAOD"] = "Diboson"
