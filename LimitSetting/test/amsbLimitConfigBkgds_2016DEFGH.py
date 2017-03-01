#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFGH' : {
        'N' : '15',
        'alpha' : '0.698083620114',
    },
    'Elec2016DEFGH' : {
        'N' : '40',
        'alpha' : '0.0477671531131',
    },
    'Muon2016DEFGH' : {
        'N' : '70',
        'alpha' : '0.0320408223978',
    },
    'Tau2016DEFGH' : {
        'N' : '36',
        'alpha' : '0.0362799589318',
    },
}

background_systematics = {
    'Fake2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00053905695',
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_alpha' : { # error on alpha
        'value' : '1.01382669814',
        'background' : 'Elec2016DEFGH',
    },
    'Muon2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00429522169',
        'background' : 'Muon2016DEFGH',
    },
    'Tau2016DEFGH_alpha' : { # error on alpha
        'value' : '1.19101194579',
        'background' : 'Tau2016DEFGH',
    },



    'Fake2016DEFGH_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 12.1625167129 / 100.0),
        'background' : 'Elec2016DEFGH',
    },
    'Tau2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 19.085523118 / 100.0),
        'background' : 'Tau2016DEFGH',
    },
}
