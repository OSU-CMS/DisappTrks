#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '68',
        'alpha' : '0.0293',
    },
    'Elec' : {
        'N' : '13715',
        'alpha' : '2.2143e-05',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.0133',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.006',
    },
}

background_systematics = {
    'Fake_alpha_NLayers5' : { # error on alpha
        'value' : '1.6708',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '1.6008', # 0 --> 0.000001 numerical safety
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers5' : { # error on alpha
        'value' : '1.722069941609909',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers5' : { # error on alpha
        'value' : '1.7900919400408384', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    # Still using 2018AB values; NEEDS TO BE UPDATED
    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '2.822',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers5' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : '1.124',
        'background' : 'Fake',
    },

    'Elec_energy_NLayers5' : { # error on energy assumption
        'value' : '1.146',
        'background' : 'Elec',
    },
    'Tau_energy_NLayers5' : { # error on energy assumption
        'value' : str (1.0 + 24.8215525905 / 100.0),
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.7517 - 0.693) / 0.7517)),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.7517 - 0.693) / 0.7517)),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.429 - 0.416) / 0.429)),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.429 - 0.416) / 0.429)),
        'background' : 'Tau',
    },
}
