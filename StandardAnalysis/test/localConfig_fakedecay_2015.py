from DisappTrks.StandardAnalysis.localConfigFakeDecay import *

config_file = "config_fakedecay_2015_cfg.py"

intLumi = lumi["MET_2015D"]

datasetsData = [
    'MET_2015D',
]

datasets = datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
