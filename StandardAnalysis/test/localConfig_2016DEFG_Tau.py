from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFG_cfg.py"

intLumi = lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFG"]

datasetsData = [
    'Tau_2016D',
    'Tau_2016E',
    'Tau_2016F',
    'Tau_2016G',
]

datasets = datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
