#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016BC' : {
        'N' : '1',
        'alpha' : '0.629547132408',
    },
    'Elec2016BC' : {
        'N' : '18',
        'alpha' : '0.0796346826171',
    },
    'Muon2016BC' : {
        'N' : '33',
        'alpha' : '0.0560296717579',
    },
    'Tau2016BC' : {
        'N' : '8',
        'alpha' : '0.611173285421',
    },
}

background_systematics = {
    'Fake2016BC' : { # error on alpha
        'value' : '1.000851615',
    },
    'Elec2016BC' : { # error on alpha
        'value' : '1.01383592566',
    },
    'Muon2016BC' : { # error on alpha
        'value' : '1.00687178331',
    },
    'Tau2016BC' : { # error on alpha
        'value' : '1.03400048458',
    },
}
