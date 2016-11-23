from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
import copy

config_file = "protoConfig_80X.py"

# 8530.912 (B&C) + 11545.996 (D&E&F) + 7101.431 (G)
intLumi = 27178.339

datasets = [
    'SingleMu_2016B',
    'SingleMu_2016C',
    'SingleMu_2016D',
    'SingleMu_2016E',
    'SingleMu_2016F',
    'SingleMu_2016G',
]
