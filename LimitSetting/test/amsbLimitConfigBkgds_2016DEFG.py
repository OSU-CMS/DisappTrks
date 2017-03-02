#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFG' : {
        'N' : '6',
        'alpha' : '0.661830275689',
    },
    'Elec2016DEFG' : {
        'N' : '19',
        'alpha' : '0.0902670805844',
    },
    'Muon2016DEFG' : {
        'N' : '37',
        'alpha' : '0.0689431207809',
    },
    'Tau2016DEFG' : {
        'N' : '8',
        'alpha' : '0.0486588451592',
    },
}

background_systematics = {
    'Fake2016DEFG_alpha' : { # error on alpha
        'value' : '1.00062310167',
        'background' : 'Fake2016DEFG',
    },
    'Elec2016DEFG_alpha' : { # error on alpha
        'value' : '1.01546123791',
        'background' : 'Elec2016DEFG',
    },
    'Muon2016DEFG_alpha' : { # error on alpha
        'value' : '1.00531024728',
        'background' : 'Muon2016DEFG',
    },
    'Tau2016DEFG_alpha' : { # error on alpha
        'value' : '1.21817575234',
        'background' : 'Tau2016DEFG',
    },



    'Fake2016DEFG_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background' : 'Fake2016DEFG',
    },
    'Elec2016DEFG_energy' : { # error on energy assumption
        'value' : str (1.0 + 12.3449633749 / 100.0),
        'background' : 'Elec2016DEFG',
    },
    'Tau2016DEFG_energy' : { # error on energy assumption
        'value' : str (1.0 + 22.0840456491 / 100.0),
        'background' : 'Tau2016DEFG',
    },
}
