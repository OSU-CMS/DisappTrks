from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2022_cfg.py"

# intLumi = lumi["EGamma_2022G"]
#intLumi = lumi["Muon_2022F"]

# datasetsData = ['EGamma_2022G']
datasetsData = ["Muon_2022F"]

#datasetsBG = ["WToLNu_4Jets_PostEE"]
# datasetsBG = ["DYJetsToLL_M50_PostEE"]
# datasetsBG = ["WW_PostEE"]
# datasetsBG = ["WZ_PostEE"]
# datasetsBG = ["ZZ_PostEE"]
# datasetsBG = ["TTto2L2Nu_PostEE"]
# datasetsBG = ["TTtoLNu2Q_PostEE"]
# datasetsBG = ["TTto4Q_PostEE"]
datasetsBG = ["DYJetsToLL_M50_merged"]

#datasets = datasetsBkgd + datasetsData + datasetsSig
# datasets = datasetsData
datasets = datasetsBG

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
