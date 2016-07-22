from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *

config_file = "protoConfig_2016_cfg.py"

intLumi = 4329.2 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/726
# Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'MET_2016B',
    #'MET_2016C',
]

datasets = datasetsData
