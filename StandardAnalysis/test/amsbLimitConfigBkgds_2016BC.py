#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016BC' : {
        'N' : '2',
        'alpha' : '0.630096969409',
    },
    'Elec2016BC' : {
        'N' : '59',
        'alpha' : '0.113816582832',
    },
    'Muon2016BC' : {
        'N' : '58',
        'alpha' : '0.0561605154146',
    },
    'Tau2016BC' : {
        'N' : '11',
        'alpha' : '0.608004037285',
    },
}

background_systematics = {
    'Fake2016BC' : { # error on alpha
        'value' : '1.00085175859',
    },
    'Elec2016BC' : { # error on alpha
        'value' : '1.01357926012',
    },
    'Muon2016BC' : { # error on alpha
        'value' : '1.00671905222',
    },
    'Tau2016BC' : { # error on alpha
        'value' : '1.03333510823',
    },
}
