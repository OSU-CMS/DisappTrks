from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2018_cfg.py"

intLumi = lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018"]

datasetsData = [
    'Tau_2018A',
    'Tau_2018B',
    'Tau_2018C',
    'Tau_2018D',
]

datasets = datasetsBkgd + datasetsData + datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
