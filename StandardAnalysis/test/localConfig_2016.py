from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *

config_file = "protoConfig_2016_cfg.py"

# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/741
intLumi = 12884.361

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'MET_2016B',
    'MET_2016C',
    'MET_2016D',
    'MET_2016E',
    'MET_2016F',
    'MET_2016G',
]

datasets = datasetsData
