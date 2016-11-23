from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2015_cfg.py"

intLumi = 2670.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/670

datasetsData = [
    'SingleEle_2015D', 
]

datasets = datasetsBkgd + datasetsData + datasetsSig
