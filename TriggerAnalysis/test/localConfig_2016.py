from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.TriggerAnalysis.miniAODSamples import *

config_file = "protoConfig_2016_cfg.py"

# 28629.903 = B (6108.362) + C (2963.704) + D (4485.279) + E (4243.920) + F (3177.925) + G (7650.713)
intLumi = 28629.903

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'SingleMu_2016B',
    'SingleMu_2016C',
    'SingleMu_2016D',
    'SingleMu_2016E',
    'SingleMu_2016F',
    'SingleMu_2016G',
]

datasets = datasetsData
