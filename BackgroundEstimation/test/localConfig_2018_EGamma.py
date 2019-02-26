from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2018_cfg.py"

intLumi = lumi["EGamma_2018"]

datasetsData = [
    'EGamma_2018A',
    'EGamma_2018B',
    'EGamma_2018C',
    'EGamma_2018D',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
