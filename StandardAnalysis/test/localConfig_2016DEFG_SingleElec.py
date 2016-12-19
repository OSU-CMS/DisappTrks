from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFG_cfg.py"

intLumi = lumi["SingleElectron_2016DEFG"]

datasetsData = [
    'SingleEle_2016D',
    'SingleEle_2016E',
    'SingleEle_2016F',
    'SingleEle_2016G',
]

datasets = datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
