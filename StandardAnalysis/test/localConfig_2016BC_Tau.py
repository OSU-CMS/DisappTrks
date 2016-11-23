from DisappTrks.StandardAnalysis.localConfig import *

config_file = "config_2016BC_cfg.py"

# unprescaled: 8526.330 (B&C)
intLumi = 813.478 # luminosity for HLT_LooseIsoPFTau50_Trk30_eta2p1_v* path

datasetsData = [
    'Tau_2016B',
    'Tau_2016C',
]

datasets = datasetsData + datasetsSig
