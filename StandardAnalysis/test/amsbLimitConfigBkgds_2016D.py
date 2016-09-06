#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016D' : {
        'N' : '0',
        'alpha' : '1.7758885739',
    },
    'Elec2016D' : {
        'N' : '25',
        'alpha' : '0.114955637328',
    },
    'Muon2016D' : {
        'N' : '13',
        'alpha' : '0.0567567673528',
    },
    'Tau2016D' : {
        'N' : '1',
        'alpha' : '1.40811575833',
    },
}

background_systematics = {
    'Fake2016D' : { # error on alpha
        'value' : '1.00156590275',
    },
    'Elec2016D' : { # error on alpha
        'value' : '1.02030608421',
    },
    'Muon2016D' : { # error on alpha
        'value' : '1.01646994135',
    },
    'Tau2016D' : { # error on alpha
        'value' : '1.08494583554',
    },
}
