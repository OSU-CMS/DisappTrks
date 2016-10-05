#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2015' : {
        'N' : '0',
        'alpha' : '0.690288446943',
    },
    'Elec2015' : {
        'N' : '5',
        'alpha' : '0.0914729171781',
    },
    'Muon2015' : {
        'N' : '1',
        'alpha' : '0.0566583653823',
    },
    'Tau2015' : {
        'N' : '3',
        'alpha' : '0.288474656965',
    },
}

background_systematics = {
    'Fake2015' : { # error on alpha
        'value' : '1.00140266199',
    },
    'Elec2015' : { # error on alpha
        'value' : '1.02410792821',
    },
    'Muon2015' : { # error on alpha
        'value' : '1.01006789935',
    },
    'Tau2015' : { # error on alpha
        'value' : '1.06184727973',
    },
}
