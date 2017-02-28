from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFGH_cfg.py"

intLumi = lumi["HLT_ZeroBias_v*"]["ZeroBias_2016DEFGH"]

datasetsData = [
    'ZeroBias_2016D',
    'ZeroBias_2016E',
    'ZeroBias_2016F',
    'ZeroBias_2016G',
    'ZeroBias_2016H',
]

datasets = datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
