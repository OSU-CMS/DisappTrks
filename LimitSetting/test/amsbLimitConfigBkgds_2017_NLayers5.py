#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '14',
        'alpha' : '0.423370525738',
    },
    'Elec' : {
        'N' : '11',
        'alpha' : '0.0682509529662',
    },
    'Muon' : {
        'N' : '7', # 5 (BCDE) * 1.4823110077656325 fixme
        'alpha' : '0.00384068366346',
    },
    'Tau' : {
        'N' : '9',
        'alpha' : '0.0142843468156',
    },
}

background_systematics = {
    'Fake_alpha_NLayers5' : { # error on alpha
        'value' : '1.01698139546',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '1.06823259842',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers5' : { # error on alpha
        'value' : '3.23692454446',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers5' : { # error on alpha
        'value' : '2.89768028819', # two-sided? alpha: 0.0142843468156 - 0.0267462803562 + 0.0271071233817
        'background' : 'Tau',
    },



    'Fake_syst_NLayers5' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 100.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 99.3 / 100.0),
        'background' : 'Fake',
    },
    'Elec_energy_NLayers5' : { # error on energy assumption
        'value' : str (1.0 + 13.6631899742 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers5' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },
}
