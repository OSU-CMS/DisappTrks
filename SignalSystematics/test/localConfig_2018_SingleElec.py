from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2018_cfg.py"

intLumi = lumi["SingleElectron_2018"]

datasetsData = [
    'SingleEle_2018A',
    'SingleEle_2018B',
    'SingleEle_2018C',
    'SingleEle_2018D',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
