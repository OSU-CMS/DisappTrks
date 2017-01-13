#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016BC' : {
        'N' : '0',
        'alpha' : '0.613186900771',
    },
    'Elec2016BC' : {
        'N' : '19',
        'alpha' : '0.112543527986',
    },
    'Muon2016BC' : {
        'N' : '25',
        'alpha' : '0.056900137794',
    },
    'Tau2016BC' : {
        'N' : '8',
        'alpha' : '0.0135152593502',
    },
}

background_systematics = {
    'Fake2016BC_alpha' : { # error on alpha
        'value' : '1.00084739905',
        'background' : 'Fake2016BC',
    },
    'Elec2016BC_alpha' : { # error on alpha
        'value' : '1.01452781398',
        'background' : 'Elec2016BC',
    },
    'Muon2016BC_alpha' : { # error on alpha
        'value' : '1.00714427592',
        'background' : 'Muon2016BC',
    },
    'Tau2016BC_alpha' : { # error on alpha
        'value' : '1.16704422709',
        'background' : 'Tau2016BC',
    },



    'Fake2016BC_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 31.3831354534 / 100.0),
        'background' : 'Fake2016BC',
    },
    'Elec2016BC_energy' : { # error on energy assumption
        'value' : str (1.0 + 10.8548021022 / 100.0),
        'background' : 'Elec2016BC',
    },
    'Tau2016BC_energy' : { # error on energy assumption
        'value' : str (1.0 + 20.0071895962 / 100.0),
        'background' : 'Tau2016BC',
    },
}
