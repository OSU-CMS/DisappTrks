#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '1',
        'alpha' : '0.0470347041845',
    },
    'Elec' : {
        'N' : '663040',
        'alpha' : '8.67086211783e-06',
    },
    'Muon' : {
        'N' : '1184700',
        'alpha' : '7.43867597659e-07',
    },
    'Tau' : {
        'N' : '6500',
        'alpha' : '7.88906709106e-05',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00039624234',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.18456798398',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.27349597197',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '0.000001/2.0049301189', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.33272782539',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
    'value' : str (1.0 + abs(0.047 - 0.096) / 0.047),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.8496947621 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 22.1600192288 / 100.0),
        'background' : 'Tau',
    },
}
