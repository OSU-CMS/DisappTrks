from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *

config_file = "protoConfig_cfg.py"

intLumi = 804.562

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'MET_2016B',
    'SingleEle_2016B',
    'SingleMu_2016B',
]

datasets = datasetsData
