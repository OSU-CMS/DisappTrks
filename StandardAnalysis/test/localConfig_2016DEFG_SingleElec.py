from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFG_cfg.py"

# 4352.417 (D) + 4049.732 (E) + 3148.581 (F) + 7108.192 (G)
# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/788
intLumi = 18658.922

datasetsData = [
    'SingleEle_2016D',
    'SingleEle_2016E',
    'SingleEle_2016F',
    'SingleEle_2016G',
]

datasets = datasetsData + datasetsSig
