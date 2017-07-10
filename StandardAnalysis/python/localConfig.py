from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
import copy
import os
import re

from DisappTrks.StandardAnalysis.miniAODV2Samples import *
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Using datasets from miniAOD_80X_Samples since we are in " + os.environ["CMSSW_VERSION"] + "..."
    from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
    print "# Using background samples from miniAODV2Samples..."
    from DisappTrks.StandardAnalysis.miniAODV2Samples import dataset_names_bkgd
    dataset_names.update (dataset_names_bkgd)
else:
    print "# Using datasets from miniAODV2Samples since we are in " + os.environ["CMSSW_VERSION"] + "..."

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
    print "# Switching to 80X signal samples since we are in " + os.environ["CMSSW_VERSION"] + "..."
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_80X", datasetsSig[i])
else:
    print "# Using 76X signal samples since we are in " + os.environ["CMSSW_VERSION"] + "..."

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigVeryShort = datasetsSig[-4:]

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
    if not isinstance (locals ()[attribute], dict) or attribute == "lumi":
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
