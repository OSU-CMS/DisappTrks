#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFG' : {
        'N' : '6',
        'alpha' : '0.661830275689',
    },
    'Elec2016DEFG' : {
        'N' : '16',
        'alpha' : '0.126214658384',
    },
    'Muon2016DEFG' : {
        'N' : '37',
        'alpha' : '0.0710305889952',
    },
    'Tau2016DEFG' : {
        'N' : '8',
        'alpha' : '0.0180731308251',
    },
}

background_systematics = {
    'Fake2016DEFG_alpha' : { # error on alpha
        'value' : '1.00062310167',
        'background' : 'Fake2016DEFG',
    },
    'Elec2016DEFG_alpha' : { # error on alpha
        'value' : '1.01241747438',
        'background' : 'Elec2016DEFG',
    },
    'Muon2016DEFG_alpha' : { # error on alpha
        'value' : '1.00511767979',
        'background' : 'Muon2016DEFG',
    },
    'Tau2016DEFG_alpha' : { # error on alpha
        'value' : '1.23274943284',
        'background' : 'Tau2016DEFG',
    },



    'Fake2016DEFG_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 42.9312574306 / 100.0),
        'background' : 'Fake2016DEFG',
    },
    'Elec2016DEFG_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.1844265418 / 100.0),
        'background' : 'Elec2016DEFG',
    },
    'Tau2016DEFG_energy' : { # error on energy assumption
        'value' : str (1.0 + 18.3795697837 / 100.0),
        'background' : 'Tau2016DEFG',
    },
}
