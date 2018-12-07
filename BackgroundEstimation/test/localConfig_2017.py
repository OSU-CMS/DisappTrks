from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2017_cfg.py"

intLumi = lumi["MET_2017"]

datasetsData = [
    'MET_2017B',
    'MET_2017C',
    'MET_2017D',
    'MET_2017E',
    'MET_2017F',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
