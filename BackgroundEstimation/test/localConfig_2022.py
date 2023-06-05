from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2022_cfg.py"

intLumi = lumi["SingleMu_2022G"]

datasetsData = ['SingleMu_2022G']

#datasets = datasetsBkgd + datasetsData + datasetsSig
datasets = datasetsData

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
