#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFG' : {
        'N' : '6',
        'alpha' : '0.661830275689',
    },
    'Elec2016DEFG' : {
        'N' : '19',
        'alpha' : '0.115972937871',
    },
    'Muon2016DEFG' : {
        'N' : '37',
        'alpha' : '0.088005132021',
    },
    'Tau2016DEFG' : {
        'N' : '8',
        'alpha' : '0.0128195952619',
    },
}

background_systematics = {
    'Fake2016DEFG_alpha' : { # error on alpha
        'value' : '1.00062310167',
        'background' : 'Fake2016DEFG',
    },
    'Elec2016DEFG_alpha' : { # error on alpha
        'value' : '1.01598292145',
        'background' : 'Elec2016DEFG',
    },
    'Muon2016DEFG_alpha' : { # error on alpha
        'value' : '1.00540255412',
        'background' : 'Muon2016DEFG',
    },
    'Tau2016DEFG_alpha' : { # error on alpha
        'value' : '1.25287915869',
        'background' : 'Tau2016DEFG',
    },



    'Fake2016DEFG_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background' : 'Fake2016DEFG',
    },
    'Elec2016DEFG_energy' : { # error on energy assumption
        'value' : str (1.0 + 12.2898761658 / 100.0),
        'background' : 'Elec2016DEFG',
    },
    'Tau2016DEFG_energy' : { # error on energy assumption
        'value' : str (1.0 + 16.7956213268 / 100.0),
        'background' : 'Tau2016DEFG',
    },
}
