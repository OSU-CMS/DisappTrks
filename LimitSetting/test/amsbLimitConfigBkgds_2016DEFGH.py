#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '7',
        'alpha' : '0.130421403538',
    },
    'Elec' : {
        'N' : '24',
        'alpha' : '0.0797170656855',
    },
    'Muon' : {
        'N' : '19',
        'alpha' : '0.0573424518265',
    },
    'Tau' : {
        'N' : '9',
        'alpha' : '0.0070580055967',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.02707897077',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.0076156265',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.00489949308',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.63421982906',
        'background' : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 100.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 99.3 / 100.0),
        'background' : 'Fake',
    },
    'Elec_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.7113892531 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },
}
