from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFG_cfg.py"

intLumi = lumi["MET_2016DEFG"]

datasetsData = [
    'MET_2016D',
    'MET_2016E',
    'MET_2016F',
    'MET_2016G',
]

datasets = datasetsBkgdForMET + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 50)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
