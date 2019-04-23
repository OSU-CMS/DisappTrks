from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2018_cfg.py"

intLumi = lumi["MET_2018"]

datasets = [
	'FakeDecay_MC_chargino_100GeV',
]

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
