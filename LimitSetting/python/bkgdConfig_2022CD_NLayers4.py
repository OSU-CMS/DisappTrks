#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '125',
        'alpha' : '0.0422',
    },
    'Elec' : {
        'N' : '0',
        'alpha' : '0.0223',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.1730',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.0126',
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.5963',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.1335', 
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '0.41258178048856287/1.587418219589611',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '1.7260',
        'background' : 'Tau',
    },

    # Still using 2018AB values; NEEDS TO BE UPDATED
    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.760',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers4' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : '1.066',
        'background' : 'Fake',
    },

    'Elec_energy_NLayers4' : { # error on energy assumption
        'value' : '1.118',
        'background' : 'Elec',
    },
    'Tau_energy_NLayers4' : { # error on energy assumption
        'value' : '1.031',
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.721 - 0.644) / 0.721)),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.721 - 0.644) / 0.721)),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.405 - 0.370) / 0.405)),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.405 - 0.370) / 0.405)),
        'background' : 'Tau',
    },


}
