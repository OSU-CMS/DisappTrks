#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016DEFGH' : {
        'N' : '1634',
        'alpha' : '0.000558720822988',
    },
    'Elec2016DEFGH' : {
        'N' : '32',
        'alpha' : '0.0493887359699',
    },
    'Muon2016DEFGH' : {
        'N' : '25',
        'alpha' : '0.0291223965337',
    },
    'Tau2016DEFGH' : {
        'N' : '10',
        'alpha' : '0.00246390955317',
    },
}

background_systematics = {
    'Fake2016DEFGH_alpha' : { # error on alpha
        'value' : '1.37812487145',
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_alpha' : { # error on alpha
        'value' : '1.01398595188',
        'background' : 'Elec2016DEFGH',
    },
    'Muon2016DEFGH_alpha' : { # error on alpha
        'value' : '1.00541901138',
        'background' : 'Muon2016DEFGH',
    },
    'Tau2016DEFGH_alpha' : { # error on alpha
        'value' : '1.42810786104',
        'background' : 'Tau2016DEFGH',
    },



    'Fake2016DEFGH_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 8.58441294376118 / 100.0),
        'background' : 'Fake2016DEFGH',
    },
    'Elec2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.7113892531 / 100.0),
        'background' : 'Elec2016DEFGH',
    },
    'Tau2016DEFGH_energy' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau2016DEFGH',
    },
}
