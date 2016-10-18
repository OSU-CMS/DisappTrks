#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2015' : {
        'N' : '0',
        'alpha' : '0.690288446943',
    },
    'Elec2015' : {
        'N' : '5',
        'alpha' : '0.112423654635',
    },
    'Muon2015' : {
        'N' : '1',
        'alpha' : '0.0566583653823',
    },
    'Tau2015' : {
        'N' : '3',
        'alpha' : '0.263672025001',
    },
}

background_systematics = {
    'Fake2015_alpha' : { # error on alpha
        'value' : '1.00140266199',
        'background'  : 'Fake2015',
    },
    'Elec2015_alpha' : { # error on alpha
        'value' : '1.02162895304',
        'background'  : 'Elec2015',
    },
    'Muon2015_alpha' : { # error on alpha
        'value' : '1.01006789935',
        'background'  : 'Muon2015',
    },
    'Tau2015_alpha' : { # error on alpha
        'value' : '1.06119675327',
        'background'  : 'Tau2015',
    },

    'Elec2015_energy' : { # error on energy assumption
        'value' : '1.106',
        'background'  : 'Elec2015',
    },
    'Tau2015_energy' : { # error on energy assumption
        'value' : '1.187',
        'background'  : 'Tau2015',
    },

    'Fake2015_syst' : { # error on fake track rate assumption
        'value' : '1.373',
        'background'  : 'Fake2015',
    },
}
