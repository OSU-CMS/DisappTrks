#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '1634',
        'alpha' : '0.000558720822988',
    },
    'Elec' : {
        'N' : '32',
        'alpha' : '0.0493887359699',
    },
    'Muon' : {
        'N' : '25',
        'alpha' : '0.0291223965337',
    },
    'Tau' : {
        'N' : '10',
        'alpha' : '0.00246390955317',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.37812487145',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.01398595188',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.00541901138',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.42810786104',
        'background' : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 8.58441294376118 / 100.0),
        'background' : 'Fake',
    },
    'Elec_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.7113892531 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },
}
