from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFGH_cfg.py"

intLumi = lumi["SingleMuon_2016DEFGH"]

datasetsData = [
    'SingleMu_2016D',
    'SingleMu_2016E',
    'SingleMu_2016F',
    'SingleMu_2016G',
    'SingleMu_2016H',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
