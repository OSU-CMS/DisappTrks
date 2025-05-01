#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '3',
        'alpha' : '0.0346',
    },
    'Elec' : {
        'N' : '189755',
        'alpha' : '1.0254e-06',
    },
    'Muon' : {
        'N' : '157933',
        'alpha' : '5.108440377186679e-07',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.016346457364598346',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.5731',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.7455',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.7071521048664238',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.2328297999146418', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    # Still using 2018AB values; NEEDS TO BE UPDATED
    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '2.822',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : '3.000',
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : '1.128',
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 24.8215525905 / 100.0),
        'background' : 'Tau',
    },
}
