from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAODV2Samples import *

config_file = "protoConfig_cfg.py"

intLumi = 2590.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/595

datasetsBkgd = [
    'DYJetsToLL',
    'ZJetsToNuNu',
    'VV',
    'SingleTop',
    'TTJets',
    'WJetsToLNu_HT',
    # 'WJetsToLNu',
]

datasetsData = [
    'MET_2015D',
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

datasetsSigShort = [
    'AMSB_chargino_500GeV_10cm',
    'AMSB_chargino_500GeV_100cm',
    'AMSB_chargino_500GeV_1000cm',
]

datasets = datasetsBkgd + datasetsData + datasetsSig  

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

types["WW"] = "bgMC"
types["WZ"] = "bgMC"
types["ZZ"] = "bgMC"
types["VG"] = "bgMC"
types["VV"] = "bgMC"

colors["WW"] = 390
colors["WZ"] = 393
colors["ZZ"] = 397
colors["VG"] = 400
colors["VV"] = 393

labels["DYJetsToLL_50"] = "Z#rightarrowl^{+}l^{-}"
labels["DYJetsToNuNu"] = "Z#rightarrow#nu#bar{#nu}"
labels["WJetsToLNu"] = "W#rightarrowl#nu"
labels["WW"] = "WW"
labels["WZ"] = "WZ"
labels["ZZ"] = "ZZ"
labels["VG"] = "V#gamma"
labels["VV"] = "Diboson"
