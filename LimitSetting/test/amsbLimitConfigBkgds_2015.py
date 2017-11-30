#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '0',
        'alpha' : '0.0694017067366',
    },
    'Elec' : {
        'N' : '2',
        'alpha' : '0.0597330883522',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.0633866216375',
    },
    'Tau' : {
        'N' : '1',
        'alpha' : '0.00367659323017',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.17035368779',
        'background'  : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.01388234152',
        'background'  : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.01098188019',
        'background'  : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.96043850698',
        'background'  : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 0.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 112.0 / 100.0),
        'background'  : 'Fake',
    },
    'Elec_energy' : { # error on energy assumption
        'value' : str (1.0 + 10.2310902711 / 100.0),
        'background'  : 'Elec',
    },
    'Tau_energy' : { # error on energy assumption
        'value' : str (1.0 + 20.0749726096 / 100.0),
        'background'  : 'Tau',
    },
}
