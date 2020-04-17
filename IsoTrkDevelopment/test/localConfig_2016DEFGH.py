from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFGH_cfg.py"

intLumi = lumi["MET_2016DEFGH"]

datasets = [
	'FakeDecay_MC_chargino_100GeV',
]

#setNJobs (datasets, composite_dataset_definitions, nJobs, 50)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
