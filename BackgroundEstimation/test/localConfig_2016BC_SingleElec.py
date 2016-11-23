from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016BC_cfg.py"

# 5883.947 (B) + 2645.968 (C)
# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/788
intLumi = 8529.915

datasetsData = [
    'SingleEle_2016B',
    'SingleEle_2016C',
]

datasets = datasetsData + datasetsSig
