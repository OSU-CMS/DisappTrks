#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '0',
        'alpha' : '0.14406779661',
    },
    'Elec' : {
        'N' : '2',
        'alpha' : '0.0820705096373',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.0478442018429',
    },
    'Tau' : {
        'N' : '3',
        'alpha' : '0.00423196041967',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.25941878437',
        'background'  : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.02335227884',
        'background'  : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.01098379748',
        'background'  : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.52406965983',
        'background'  : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 100.0 / 100.0),
        'background'  : 'Fake',
    },
    'Elec_energy' : { # error on energy assumption
        'value' : str (1.0 + 10.2310902711 / 100.0),
        'background'  : 'Elec',
    },
    'Tau_energy' : { # error on energy assumption
        'value' : str (1.0 + 20.0749726096 / 100.0),
        'background'  : 'Tau',
    },
}
