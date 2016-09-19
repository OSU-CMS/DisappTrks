#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2015' : {
        'N' : '1',
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
        'alpha' : '0.466653966922',
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
        'value' : '1.06223981866',
    },
}
