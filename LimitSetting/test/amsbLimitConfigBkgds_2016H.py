#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016H' : {
        'N' : '9',
        'alpha' : '0.821237225603',
    },
    'Elec2016H' : {
        'N' : '21',
        'alpha' : '0.0950270508264',
    },
    'Muon2016H' : {
        'N' : '33',
        'alpha' : '0.0529927613521',
    },
    'Tau2016H' : {
        'N' : '28',
        'alpha' : '0.00753667767931',
    },
}

background_systematics = {
    'Fake2016H_alpha' : { # error on alpha
        'value' : '1.00107928806',
        'background' : 'Fake2016H',
    },
    'Elec2016H_alpha' : { # error on alpha
        'value' : '1.01642464001',
        'background' : 'Elec2016H',
    },
    'Muon2016H_alpha' : { # error on alpha
        'value' : '1.0058620186',
        'background' : 'Muon2016H',
    },
    'Tau2016H_alpha' : { # error on alpha
        'value' : '1.45843076991',
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
