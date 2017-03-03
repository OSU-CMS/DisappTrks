from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016BC_cfg.py"

intLumi = lumi["SingleMuon_2016BC"]

datasetsData = [
    'SingleMu_2016B',
    'SingleMu_2016C',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
