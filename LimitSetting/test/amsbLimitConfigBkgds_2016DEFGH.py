#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '7',
        'alpha' : '0.130421403538',
    },
    'Elec' : {
        'N' : '32',
        'alpha' : '0.103375125392',
    },
    'Muon' : {
        'N' : '25',
        'alpha' : '0.0587235923671',
    },
    'Tau' : {
        'N' : '10',
        'alpha' : '0.0115340679454',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.02707897077',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.00976018491',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.00383974957',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.28855882146',
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
