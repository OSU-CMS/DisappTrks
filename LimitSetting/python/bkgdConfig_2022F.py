#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : { #needs to be updated
        'N' : '1',
        'alpha' : '0.0354151129416',
    },
    'Elec' : {
        'N' : '95330',
        'alpha' : '5.21512553549e-06',
    },
    'Muon' : { #needs to be updated
        'N' : '428980',
        'alpha' : '8.78345986154e-07',
    },
    'Tau' : { #needs to be updated
        'N' : '0',
        'alpha' : '0.048',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00074624437', #needs to be updated
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '0.000001 / 4.60563261666',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.39533579372', #needs to be updated
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '0.000001/2.77468239654', # 0 --> 0.000001 numerical safety #needs to be updated
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.52067231799', #needs to be updated
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
    'value' : str (1.0 + abs(0.035 - 0.087) / 0.035), #needs to be updated
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.937307135 / 100.0), #needs to be updated
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 24.8215525905 / 100.0), #needs to be updated
        'background' : 'Tau',
    },
}
