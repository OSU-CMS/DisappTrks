from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2017_cfg.py"

intLumi = lumi["SingleElectron_2017"]

datasetsData = [
    'SingleEle_2017B',
    'SingleEle_2017C',
    'SingleEle_2017D',
    'SingleEle_2017E',
    'SingleEle_2017F',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
