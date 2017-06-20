#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2015' : {
        'N' : '0',
        'alpha' : '0.14406779661',
    },
    'Elec2015' : {
        'N' : '2',
        'alpha' : '0.0820705096373',
    },
    'Muon2015' : {
        'N' : '0',
        'alpha' : '0.0478442018429',
    },
    'Tau2015' : {
        'N' : '3',
        'alpha' : '0.00423196041967',
    },
}

background_systematics = {
    'Fake2015_alpha' : { # error on alpha
        'value' : '1.25941878437',
        'background'  : 'Fake2015',
    },
    'Elec2015_alpha' : { # error on alpha
        'value' : '1.02335227884',
        'background'  : 'Elec2015',
    },
    'Muon2015_alpha' : { # error on alpha
        'value' : '1.01098379748',
        'background'  : 'Muon2015',
    },
    'Tau2015_alpha' : { # error on alpha
        'value' : '1.52406965983',
        'background'  : 'Tau2015',
    },



    'Fake2015_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background'  : 'Fake2015',
    },
    'Elec2015_energy' : { # error on energy assumption
        'value' : str (1.0 + 10.2310902711 / 100.0),
        'background'  : 'Elec2015',
    },
    'Tau2015_energy' : { # error on energy assumption
        'value' : str (1.0 + 20.0749726096 / 100.0),
        'background'  : 'Tau2015',
    },
}
