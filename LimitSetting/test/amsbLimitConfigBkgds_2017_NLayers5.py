#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '14',
        'alpha' : '0.423370525738',
    },
    'Elec' : {
        'N' : '12',
        'alpha' : '0.06791666666666667',
    },
    'Muon' : {
        'N' : '7', # 5 (BCDE) * 1.4823110077656325 fixme
        'alpha' : '0.00384068366346',
    },
    'Tau' : {
        'N' : '9',
        'alpha' : '0.0160698901676',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.01698139546',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.0899618452700002',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '3.23692454446',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '2.90277053642', # fixme
        'background' : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 100.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 99.3 / 100.0),
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
