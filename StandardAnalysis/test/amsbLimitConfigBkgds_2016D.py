#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016D' : {
        'N' : '0',
        'alpha' : '1.7758885739',
    },
    'Elec2016D' : {
        'N' : '13',
        'alpha' : '0.0771229551724',
    },
    'Muon2016D' : {
        'N' : '7',
        'alpha' : '0.0566361051983',
    },
    'Tau2016D' : {
        'N' : '1',
        'alpha' : '1.40110768497',
    },
}

background_systematics = {
    'Fake2016D' : { # error on alpha
        'value' : '1.00156590275',
    },
    'Elec2016D' : { # error on alpha
        'value' : '1.02076086108',
    },
    'Muon2016D' : { # error on alpha
        'value' : '1.01684539919',
    },
    'Tau2016D' : { # error on alpha
        'value' : '1.08654141461',
    },
}
