#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016BC' : {
        'N' : '1',
        'alpha' : '0.629547132408',
    },
    'Elec2016BC' : {
        'N' : '18',
        'alpha' : '0.0797038926066',
    },
    'Muon2016BC' : {
        'N' : '24',
        'alpha' : '0.0560294594353',
    },
    'Tau2016BC' : {
        'N' : '9',
        'alpha' : '0.328950658721',
    },
}

background_systematics = {
    'Fake2016BC_alpha' : { # error on alpha
        'value' : '1.000851615',
        'background' : 'Fake2016BC',
    },
    'Elec2016BC_alpha' : { # error on alpha
        'value' : '1.01383679285',
        'background' : 'Elec2016BC',
    },
    'Muon2016BC_alpha' : { # error on alpha
        'value' : '1.00687178273',
        'background' : 'Muon2016BC',
    },
    'Tau2016BC_alpha' : { # error on alpha
        'value' : '1.03365705835',
        'background' : 'Tau2016BC',
    },

    'Elec2016BC_energy' : { # error on energy assumption
        'value' : '1.109',
        'background' : 'Elec2016BC',
    },
    'Tau2016BC_energy' : { # error on energy assumption
        'value' : '1.168',
        'background' : 'Tau2016BC',
    },

    'Fake2016BC_syst' : { # error on fake track rate assumption
        'value' : '1.371',
        'background' : 'Fake2016BC',
    },
}
