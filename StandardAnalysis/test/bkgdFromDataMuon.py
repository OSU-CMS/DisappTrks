#!/usr/bin/env python

datasets = [
    'MET', 
]
impurities = [
]
bkgd_from_data = {
    'scale_factor' : 1.66e-4,  # Take from spreadsheet  
    'scale_factor_error' : (0.44e-4),
    'channel_map' : {
        'PreSelectionMuon' : ['PreSelection'],
    }
}
