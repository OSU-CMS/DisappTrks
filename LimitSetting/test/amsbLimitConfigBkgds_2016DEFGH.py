#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFGH' : {
        'N' : '6',
        'alpha' : '0.661830275689',
    },
    'Elec2016DEFGH' : {
        'N' : '16',
        'alpha' : '0.126214658384',
    },
    'Muon2016DEFGH' : {
        'N' : '37',
        'alpha' : '0.0710305889952',
    },
    'Tau2016DEFGH' : {
        'N' : '8',
        'alpha' : '0.0180731308251',
    },
}

background_systematics = {
    'Fake2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00062310167',
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_alpha' : { # error on alpha
        'value' : '1.01241747438',
        'background' : 'Elec2016DEFGH',
    },
    'Muon2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00511767979',
        'background' : 'Muon2016DEFGH',
    },
    'Tau2016DEFGH_alpha' : { # error on alpha
        'value' : '1.23274943284',
        'background' : 'Tau2016DEFGH',
    },



    'Fake2016DEFGH_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 42.9312574306 / 100.0),
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.1844265418 / 100.0),
        'background' : 'Elec2016DEFGH',
    },
    'Tau2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 18.3795697837 / 100.0),
        'background' : 'Tau2016DEFGH',
    },
}
