#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '123',
        'alpha' : '0.423370525738',
    },
    'Elec' : {
        'N' : '15',
        'alpha' : '0.0756021250521',
    },
    'Muon' : {
        'N' : '99', # 67 (BCDE) * 1.4823110077656325 fixme
        'alpha' : '0.00001', # estimate is zero due to lack of stats in P(trigger) FIXME
    },
    'Tau' : {
        'N' : '50',
        'alpha' : '0.00001', # fixme
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.01698139546',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.10006941274',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '2.0', # fixme
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '2.0', # fixme
        'background' : 'Tau',
    },

    'Fake_syst_NLayers4' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 100.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 99.3 / 100.0),
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
}
