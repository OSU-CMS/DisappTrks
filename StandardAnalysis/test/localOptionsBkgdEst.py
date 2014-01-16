#!/usr/bin/env python

from localOptionsAll import * 

datasets = [
    'MET', 

    'OthrBkgd',
    'TauBkgd',
    'MuonBkgd', 
    'ElecBkgd',
    'FakeBkgd',

    
    ]

types['MuonBkgd'] = "bgMC"
types['ElecBkgd'] = "bgMC"
types['TauBkgd']  = "bgMC"
types['OthrBkgd']  = "bgMC"
types['FakeBkgd'] = "bgMC"

colors['MuonBkgd'] = 632 
colors['ElecBkgd'] = 419
colors['TauBkgd']  = 600
colors['OthrBkgd']  = 616
colors['FakeBkgd'] = 432

labels['MuonBkgd'] = "#mu bkgd" 
labels['ElecBkgd'] = "e bkgd"
labels['TauBkgd']  = "#tau bkgd"
labels['OthrBkgd']  = "other bkgd"
labels['FakeBkgd'] = "fake bkgd"  




