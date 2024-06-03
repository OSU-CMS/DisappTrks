from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2022_cfg.py"

intLumi = lumi["MET_2022F"]

datasetsData = [
    'MET_2018A',
    'MET_2018B',
    'MET_2018C',
    'MET_2018D',
]

# datasetsSig = ["AMSB_chargino_700GeV_10000cm_124X"]
# datasetsSig = ["AMSB_chargino_700GeV_1000cm_124X"]
# datasetsSig = ["AMSB_chargino_700GeV_100cm_124X"]
# datasetsSig = ["AMSB_chargino_700GeV_10cm_124X"]
# datasetsSig = ["AMSB_chargino_400GeV_10000cm_124X"]
# datasetsSig = ["AMSB_chargino_400GeV_1000cm_124X"]
# datasetsSig = ["AMSB_chargino_400GeV_100cm_124X"]
# datasetsSig = ["AMSB_chargino_400GeV_10cm_124X"]
# datasetsSig = ["AMSB_chargino_100GeV_10000cm_124X"]
# datasetsSig = ["AMSB_chargino_100GeV_1000cm_124X"]
# datasetsSig = ["AMSB_chargino_100GeV_100cm_124X"]
datasetsSig = ["AMSB_chargino_100GeV_10cm_124X"]
# datasetsSig = ["AMSB_chargino_1100GeV_10000cm_124X"]
# datasetsSig = ["AMSB_chargino_1100GeV_1000cm_124X"]
# datasetsSig = ["AMSB_chargino_1100GeV_100cm_124X"]
# datasetsSig = ["AMSB_chargino_1100GeV_10cm_124X"]

# datasets = datasetsBkgd + datasetsData + datasetsSig
datasets = datasetsSig

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
