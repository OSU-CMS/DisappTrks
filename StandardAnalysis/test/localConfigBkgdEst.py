#!/usr/bin/env python

from localConfig import * 

datasets = [
    'MET', 

#   'OthrBkgd',
    'FakeBkgd',
    'ElecBkgd',
    'MuonBkgd', 
    'TauBkgd',
    
    ]

types['MuonBkgd'] = "bgMC"
types['ElecBkgd'] = "bgMC"
types['TauBkgd']  = "bgMC"
types['OthrBkgd'] = "bgMC"
types['FakeBkgd'] = "bgMC"

colors['MuonBkgd'] = 898    # kPink - 2
colors['ElecBkgd'] = 417    # kGreen + 1
colors['TauBkgd']  = 858    # kAzure -2 
colors['OthrBkgd'] = 616    # kMagenta
colors['FakeBkgd'] = 432    # kCyan 

labels['MuonBkgd'] = "#mu bkgd" 
labels['ElecBkgd'] = "e bkgd"
labels['TauBkgd']  = "#tau bkgd"
labels['OthrBkgd'] = "other bkgd"
labels['FakeBkgd'] = "Misid. bkgd"  


composite_dataset_definitions['FakeBkgd'] = [
    'FakeMuMuBkgd',
    'FakeEEBkgd', 
]

composite_dataset_definitions['Background'] = [
    'OthrBkgd',
    'FakeBkgd',
    'ElecBkgd',
    'MuonBkgd', 
    'TauBkgd',
    ]


histsToBlind = [
#    'CaloTot',
    ]



