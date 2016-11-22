#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016D' : {
        'N' : '0',
        'alpha' : '1.7758885739',
    },
    'Elec2016D' : {
        'N' : '10',
        'alpha' : '0.0771650936081',
    },
    'Muon2016D' : {
        'N' : '7',
        'alpha' : '0.0566361051983',
    },
    'Tau2016D' : {
        'N' : '1',
        'alpha' : '0.505203966966',
    },
}

background_systematics = {
    'Fake2016D_alpha' : { # error on alpha
        'value' : '1.00156590275',
        'background' : 'Fake2016D',
    },
    'Elec2016D_alpha' : { # error on alpha
        'value' : '1.02077835384',
        'background' : 'Elec2016D',
    },
    'Muon2016D_alpha' : { # error on alpha
        'value' : '1.01684539919',
        'background' : 'Muon2016D',
    },
    'Tau2016D_alpha' : { # error on alpha
        'value' : '1.08557700949',
        'background' : 'Tau2016D',
    },

    'Elec2016D_energy' : { # error on energy assumption
        'value' : '1.108',
        'background' : 'Elec2016D',
    },
    'Tau2016D_energy' : { # error on energy assumption
        'value' : '1.180',
        'background' : 'Tau2016D',
    },

    'Fake2016D_syst' : { # error on fake track rate assumption
        'value' : '1.448',
        'background' : 'Fake2016D',
    },
}
