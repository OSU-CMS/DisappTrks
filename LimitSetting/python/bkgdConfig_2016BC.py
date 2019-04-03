#!/usr/bin/env python
# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '4',
        'alpha' : '0.095698256576',
    },
    'Elec' : {
        'N' : '12',
        'alpha' : '0.0792429114411',
    },
    'Muon' : {
        'N' : '16',
        'alpha' : '0.063105605617',
    },
    'Tau' : {
        'N' : '4',
        'alpha' : '0.00801094482172',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.06721362153',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.01082287584',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.00863695923',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.4524468474',
        'background' : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 100.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 108.0 / 100.0),
        'background' : 'Fake',
    },
    'Elec_energy' : { # error on energy assumption
        'value' : str (1.0 + 11.7154379658 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy' : { # error on energy assumption
        'value' : str (1.0 + 17.9781025482 / 100.0),
        'background' : 'Tau',
    },
}
