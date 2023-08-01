from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2022_cfg.py"

intLumi = lumi["EGamma_2022G"]

datasetsData = ["EGamma_2022G"]

datasetsSig = ["AMSB_chargino_700GeV_100cm_124X"]

datasets = datasetsData

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
