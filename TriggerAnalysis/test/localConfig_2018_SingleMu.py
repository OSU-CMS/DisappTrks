from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2018_cfg.py"

intLumi = lumi["SingleMuon_2018"]

datasetsData = [
    'SingleMu_2018A',
    'SingleMu_2018B',
    'SingleMu_2018C',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
