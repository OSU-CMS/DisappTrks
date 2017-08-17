from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2017_cfg.py"

intLumi = lumi["SingleMuon_2017"]

datasetsData = [
    'SingleMu_2017C',
]

datasets = datasetsBkgd + datasetsData + datasetsSig
#datasets = datasetsData

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
