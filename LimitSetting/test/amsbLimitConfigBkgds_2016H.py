#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016H' : {
        'N' : '9',
        'alpha' : '0.821237225603',
    },
    'Elec2016H' : {
        'N' : '21',
        'alpha' : '0.0950158541534',
    },
    'Muon2016H' : {
        'N' : '33',
        'alpha' : '0.0529549524991',
    },
    'Tau2016H' : {
        'N' : '28',
        'alpha' : '0.0242831283708',
    },
}

background_systematics = {
    'Fake2016H_alpha' : { # error on alpha
        'value' : '1.00107928806',
        'background' : 'Fake2016H',
    },
    'Elec2016H_alpha' : { # error on alpha
        'value' : '1.01642498767',
        'background' : 'Elec2016H',
    },
    'Muon2016H_alpha' : { # error on alpha
        'value' : '1.00586212108',
        'background' : 'Muon2016H',
    },
    'Tau2016H_alpha' : { # error on alpha
        'value' : '1.40723999369',
        'background' : 'Tau2016H',
    },



    'Fake2016H_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background' : 'Fake2016H',
    },
    'Elec2016H_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.9194536874 / 100.0),
        'background' : 'Elec2016H',
    },
    'Tau2016H_energy' : { # error on energy assumption
        'value' : str (1.0 + 16.9537674561 / 100.0),
        'background' : 'Tau2016H',
    },
}
