from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2015_cfg.py"

#intLumi = 2672.2 # unprescaled
intLumi = 225.17 # luminosity for HLT_LooseIsoPFTau50_Trk30_eta2p1_v* path

datasetsData = [
    'Tau_2015D',  
]

datasets = datasetsBkgd + datasetsData + datasetsSig
