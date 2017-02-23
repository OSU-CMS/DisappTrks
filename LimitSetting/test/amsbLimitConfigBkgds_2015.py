#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2015' : {
        'N' : '0',
        'alpha' : '0.712247674396',
    },
    'Elec2015' : {
        'N' : '5',
        'alpha' : '0.116004948731',
    },
    'Muon2015' : {
        'N' : '1',
        'alpha' : '0.0584607625367',
    },
    'Tau2015' : {
        'N' : '3',
        'alpha' : '0.272032185914',
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



    'Fake2015_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background'  : 'Fake2015',
    },
    'Elec2015_energy' : { # error on energy assumption
        'value' : str (1.0 + 10.589318523 / 100.0),
        'background'  : 'Elec2015',
    },
    'Tau2015_energy' : { # error on energy assumption
        'value' : str (1.0 + 18.6935586566 / 100.0),
        'background'  : 'Tau2015',
    },
}
