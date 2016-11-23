from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016DEFG_cfg.py"

# unprescaled: 8526.330 (B&C) + 18662.158 (D&E&F&G) = 27188.488
intLumi = 427.067 # luminosity for HLT_LooseIsoPFTau50_Trk30_eta2p1_v* path

datasetsData = [
    'Tau_2016D',
    'Tau_2016E',
    'Tau_2016F',
    'Tau_2016G',
]

datasets = datasetsData + datasetsSig
