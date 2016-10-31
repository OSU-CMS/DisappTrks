from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAODV2Samples import *
import copy

config_file = "protoConfig_76X.py"

intLumi = 2590.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/595

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

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
    'SingleMu_2016D',
]

datasets = datasetsBkgd + datasetsData

composite_dataset_definitions["allBkgd"] = datasetsBkgd

composite_dataset_definitions["SingleTop"] = [
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
colors["VV"] = 393
colors["allBkgd"] = 601

labels["DYJetsToLL_50"] = "Z#rightarrowl^{+}l^{-}"
labels["DYJetsToNuNu"] = "Z#rightarrow#nu#bar{#nu}"
labels["WJetsToLNu"] = "W#rightarrowl#nu"
labels["WW"] = "WW"
labels["WZ"] = "WZ"
labels["ZZ"] = "ZZ"
labels["VG"] = "V#gamma"
labels["VV"] = "Diboson"
labels["allBkgd"] = "Total bkgd"
