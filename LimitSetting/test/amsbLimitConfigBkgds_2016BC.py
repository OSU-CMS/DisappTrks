#!/usr/bin/env python
# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '254',
        'alpha' : '0.00150705915868',
    },
    'Elec' : {
        'N' : '13',
        'alpha' : '0.0420600923851',
    },
    'Muon' : {
        'N' : '18',
        'alpha' : '0.0263138553455',
    },
    'Tau' : {
        'N' : '4',
        'alpha' : '0.00293348863686',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.50058032627',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.02396905829',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.01049244309',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.37860343927',
        'background' : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 7.01139237387396 / 100.0),
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
