from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016BC_cfg.py"

intLumi = lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"]

datasetsData = [
    'Tau_2016B',
    'Tau_2016C',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
