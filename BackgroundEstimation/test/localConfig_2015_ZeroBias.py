from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2015_cfg.py"

intLumi = lumi["HLT_ZeroBias_v*"]["ZeroBias_2015D"]

datasetsData = [
    'ZeroBias_2015D',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
