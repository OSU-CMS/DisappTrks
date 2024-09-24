from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2022_cfg.py"

intLumi = lumi["Muon_2022F"]

datasetsData = ["Muon_2022F"]

# datasetsSig = ["AMSB_chargino_700GeV_10000cm_124X"]
# datasetsSig = ["AMSB_chargino_700GeV_1000cm_124X"]
# datasetsSig = ["AMSB_chargino_700GeV_100cm_124X"]
# datasetsSig = ["AMSB_chargino_700GeV_10cm_124X"]
# datasetsSig = ["AMSB_chargino_Pythia700GeV_100cm_124X"]
# datasetsSig = ["AMSB_chargino_Pythia100GeV_100cm_124X"]
datasetsSig = ["AMSB_chargino_100GeV_100cm_124X"]

# datasetsBG = ["WToLNu_4Jets_PostEE"]
# datasetsBG = ["WToLNu_2Jets_PostEE"]
# datasetsBG = ["DYJetsToLL_M50_PostEE"]
# datasetsBG = ["WW_PostEE"]
# datasetsBG = ["WZ_PostEE"]
# datasetsBG = ["ZZ_PostEE"]
# datasetsBG = ["TTto2L2Nu_PostEE"]
# datasetsBG = ["TTtoLNu2Q_PostEE"]
# datasetsBG = ["TTto4Q_PostEE"]
# datasetsBG = ["QCD_PT15to30_PostEE"]
# datasetsBG = ["QCD_PT30to50_PostEE"]
# datasetsBG = ["QCD_PT50to80_PostEE"]
# datasetsBG = ["QCD_PT80to120_PostEE"]
# datasetsBG = ["QCD_PT120to170_PostEE"]
# datasetsBG = ["QCD_PT170to300_PostEE"]
# datasetsBG = ["QCD_PT300to470_PostEE"]
# datasetsBG = ["QCD_PT470to600_PostEE"]
# datasetsBG = ["QCD_PT600to800_PostEE"]
# datasetsBG = ["QCD_PT800to1000_PostEE"]
# datasetsBG = ["QCD_PT1000to1400_PostEE"]
# datasetsBG = ["QCD_PT1400to1800_PostEE"]
# datasetsBG = ["QCD_PT1800to2400_PostEE"]
# datasetsBG = ["QCD_PT2400to3200_PostEE"]
# datasetsBG = ["Zto2Nu_4Jets_HT100to200_PostEE"]
# datasetsBG = ["Zto2Nu_4Jets_HT200to400_PostEE"]
# datasetsBG = ["Zto2Nu_4Jets_HT400to800_PostEE"]
# datasetsBG = ["Zto2Nu_4Jets_HT800to1500_PostEE"]
# datasetsBG = ["Zto2Nu_4Jets_HT1500to2500_PostEE"]
# datasetsBG = ["WtoMuNu_M100to200"]
# datasetsBG = ["WtoMuNu_M200to500"]
datasetsBG = ["WtoMuNu_M500to1000"]

# datasets = datasetsSig
#datasets = datasetsBG
datasets = datasetsData

#setNJobs (datasets, composite_dataset_definitions, nJobs, 500)
#setDatasetType (datasets, composite_dataset_definitions, types, "bgMC")
#InputCondorArguments["hold"] = "True"
