#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'yield' : '11.22',
        'error' : str (1.0 + 0.82/10.84),
    },
    'Elec' : {
        'N' : '15',
        'alpha' : '0.0768231831901',
    },
    'Muon' : {
        'N' : '104',
        'alpha' : '0.0011607222849',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.022230490',
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.00052390363',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.1000826002',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '2.00120350117',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '0.00508931961', # 0 +0.00508931961 -0
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.38923987949',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers4' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + (11.22 - 10.80) / 11.22),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 13.8466686504 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers4' : {
        'value' : str(1.0951),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : str(1.0951),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : str(1.0841),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : str(1.0841),
        'background' : 'Tau',
    },


}
