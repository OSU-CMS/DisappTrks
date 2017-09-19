#!/usr/bin/env python
# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '4',
        'alpha' : '0.095698256576',
    },
    'Elec' : {
        'N' : '13',
        'alpha' : '0.0870270864348',
    },
    'Muon' : {
        'N' : '18',
        'alpha' : '0.0529112162311',
    },
    'Tau' : {
        'N' : '4',
        'alpha' : '0.00582997402504',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.06721362153',
        'background' : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.0168262496',
        'background' : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.00743634832',
        'background' : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.74768153715',
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
