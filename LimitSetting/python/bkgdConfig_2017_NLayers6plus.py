#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '1',
        'alpha' : '0.0401045591525',
    },
    'Elec' : {
        'N' : '487280',
        'alpha' : '9.68654274291e-06',
    },
    'Muon' : {
        'N' : '851260',
        'alpha' : '5.62966412617e-07',
    },
    'Tau' : {
        'N' : '5130',
        'alpha' : '9.80525123437e-05',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00052390363',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.18461799309',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.424276463',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.46083926013',
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.42537586979',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
    'value' : str (1.0 + abs(0.04 - 0.122) / 0.04),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.4474529027 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },
}
