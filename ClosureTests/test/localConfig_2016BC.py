from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016BC_cfg.py"

intLumi = lumi["MET_2016BC"]

datasetsData = [
    'MET_2016B',
    'MET_2016C',
]

datasets = datasetsBkgdForMET + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
