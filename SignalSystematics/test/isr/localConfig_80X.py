from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAODV2Samples import *
import copy

config_file = "protoConfig_80X.py"

# ICHEP 2016 dataset
# 5877.897 (B) + 2645.968 (C) + 4353.449 (D)
# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/738
intLumi = 12877.314

datasets = [
    'SingleMu_2016B',
    'SingleMu_2016C',
    'SingleMu_2016D',
    'SingleMu_2016E',
    'SingleMu_2016F',
    'SingleMu_2016G',
]
