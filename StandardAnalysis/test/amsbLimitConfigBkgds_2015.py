#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2015' : {
        'N' : '1',
        'alpha' : '0.690288446943',
    },
    'Elec2015' : {
        'N' : '47',
        'alpha' : '0.0912946308288',
    },
    'Muon2015' : {
        'N' : '7',
        'alpha' : '0.0565962923904',
    },
    'Tau2015' : {
        'N' : '3',
        'alpha' : '0.470548642117',
    },
}

background_systematics = {
    'Fake2015' : { # error on alpha
        'value' : '1.00140266199',
    },
    'Elec2015' : { # error on alpha
        'value' : '1.02352499182',
    },
    'Muon2015' : { # error on alpha
        'value' : '1.0098255571',
    },
    'Tau2015' : { # error on alpha
        'value' : '1.0604915536',
    },
}
