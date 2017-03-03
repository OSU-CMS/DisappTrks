#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFGH' : {
        'N' : '15',
        'alpha' : '0.698083620114',
    },
    'Elec2016DEFGH' : {
        'N' : '40',
        'alpha' : '0.109039329171',
    },
    'Muon2016DEFGH' : {
        'N' : '70',
        'alpha' : '0.072919244329',
    },
    'Tau2016DEFGH' : {
        'N' : '36',
        'alpha' : '0.00992294715715',
    },
}

background_systematics = {
    'Fake2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00053905695',
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_alpha' : { # error on alpha
        'value' : '1.0156845001',
        'background' : 'Elec2016DEFGH',
    },
    'Muon2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00460548426',
        'background' : 'Muon2016DEFGH',
    },
    'Tau2016DEFGH_alpha' : { # error on alpha
        'value' : '1.22039895914',
        'background' : 'Tau2016DEFGH',
    },



    'Fake2016DEFGH_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 12.1390341949 / 100.0),
        'background' : 'Elec2016DEFGH',
    },
    'Tau2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 16.831056317 / 100.0),
        'background' : 'Tau2016DEFGH',
    },
}
