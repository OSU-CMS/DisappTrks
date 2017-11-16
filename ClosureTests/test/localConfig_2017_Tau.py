from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2017_cfg.py"

intLumi = lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2017"]

datasetsData = [
    'Tau_2017B',
    'Tau_2017C',
    'Tau_2017D',
    'Tau_2017E',
    'Tau_2017F',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
