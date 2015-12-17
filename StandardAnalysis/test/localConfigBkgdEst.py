#!/usr/bin/env python

from localConfig import * 

datasets = [
    'MET', 

#   'OthrBkgd',
    'FakeMuMuBkgd',
    'ElecBkgd',
    'MuonBkgd', 
    'TauBkgd',
    
    ]

types['MuonBkgd'] = "bgMC"
types['ElecBkgd'] = "bgMC"
types['TauBkgd']  = "bgMC"
types['OthrBkgd'] = "bgMC"
types['FakeMuMuBkgd'] = "bgMC"
types['MET']      = "data" 

colors['MuonBkgd'] = 898    # kPink - 2
colors['ElecBkgd'] = 417    # kGreen + 1
colors['TauBkgd']  = 858    # kAzure -2 
colors['OthrBkgd'] = 616    # kMagenta
colors['FakeMuMuBkgd'] = 432    # kCyan 
colors['MET']      =   1    # kCyan 

labels['MuonBkgd'] = "#mu bkgd" 
labels['ElecBkgd'] = "e bkgd"
labels['TauBkgd']  = "#tau bkgd"
labels['OthrBkgd'] = "other bkgd"
labels['FakeMuMuBkgd'] = "Misid. bkgd"  
labels['MET']      = "2015D MET data" 


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



