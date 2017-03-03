#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake2016BC' : {
        'N' : '0',
        'alpha' : '0.613186900771',
    },
    'Elec2016BC' : {
        'N' : '19',
        'alpha' : '0.0746763147406',
    },
    'Muon2016BC' : {
        'N' : '25',
        'alpha' : '0.049856860573',
    },
    'Tau2016BC' : {
        'N' : '8',
        'alpha' : '0.00789987996823',
    },
}

background_systematics = {
    'Fake2016BC_alpha' : { # error on alpha
        'value' : '1.00084739905',
        'background' : 'Fake2016BC',
    },
    'Elec2016BC_alpha' : { # error on alpha
        'value' : '1.01637012989',
        'background' : 'Elec2016BC',
    },
    'Muon2016BC_alpha' : { # error on alpha
        'value' : '1.00684383431',
        'background' : 'Muon2016BC',
    },
    'Tau2016BC_alpha' : { # error on alpha
        'value' : '1.18721776651',
        'background' : 'Tau2016BC',
    },



    'Fake2016BC_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 25.0 / 100.0), # set to 25% for now
        'background' : 'Fake2016BC',
    },
    'Elec2016BC_energy' : { # error on energy assumption
        'value' : str (1.0 + 12.3565749086 / 100.0),
        'background' : 'Elec2016BC',
    },
    'Tau2016BC_energy' : { # error on energy assumption
        'value' : str (1.0 + 14.2109057314 / 100.0),
        'background' : 'Tau2016BC',
    },
}
