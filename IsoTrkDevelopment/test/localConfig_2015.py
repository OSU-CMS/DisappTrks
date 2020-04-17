from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2015_cfg.py"

intLumi = lumi["MET_2015D"]

datasets = [
	'FakeDecay_MC_chargino_100GeV',
]

#setNJobs (datasets, composite_dataset_definitions, nJobs, 50)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
