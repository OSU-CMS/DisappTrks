from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFGH_cfg.py"

intLumi = lumi["MET_2016DEFGH"]

datasetsData = [
    'MET_2016D',
    'MET_2016E',
    'MET_2016F',
    'MET_2016G',
    'MET_2016H',
]

datasets = datasetsBkgdForMET + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
