#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '1',
        'alpha' : '0.0925491099217114',
    },
    'Elec' : {
        'N' : '563300',
        'alpha' : '5.359647795299747e-06',
    },
    'Muon' : {
        'N' : '489700',
        'alpha' : '2.097221659020428e-07',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.0047',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.0006237139562497',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.177028879393033',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.7071321137275632',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.3715814958318515', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    # Still using 2018AB values; NEEDS TO BE UPDATED
    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.52067231799',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
    'value' : str (1.0 + abs(0.035 - 0.087) / 0.035),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.937307135 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 24.8215525905 / 100.0),
        'background' : 'Tau',
    },
}
