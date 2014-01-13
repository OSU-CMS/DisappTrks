#!/usr/bin/env python

datasets = [
    'WjetsHighPt',   
]
impurities = [
]
bkgd_from_data = {
    'scale_factor' : 0.02209,
    'scale_factor_error' : (0),

    # This is a map from channels in the output from data to the channels you
    # want in QCDFromData.root; e.g., below, the histograms in the
    # "AntiIsolated" channel will be used to create an "Isolated" and
    # "AntiIsolated" channel in QCDFromData.root.
    'channel_map' : {
        'PreSelection' : ['PreSelectionBkgdEst'],
    }
}
