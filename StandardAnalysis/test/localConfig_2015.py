from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2015_cfg.py"

intLumi = 2590.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/595

datasetsData = [
    'MET_2015D',
]

datasets = datasetsBkgdForMET + datasetsData + datasetsSig
