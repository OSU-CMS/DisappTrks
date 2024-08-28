#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py
backgrounds = {
    'Fake' : {
        'N' : '13',
        'alpha' : '0.0354151129416',
    },
    'Elec' : {
        'N' : '5098',
        'alpha' : '2.95225133864e-05',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.0334303587209',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.00221629130184',
    },
}

background_systematics = {
    'Fake_alpha_NLayers5' : { # error on alpha
        'value' : '1.00074624437',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '0.000001/2.73537178939', # 0 --> 0.000001 numerical safety
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers5' : { # error on alpha
        'value' : '0.436265235168/1.56373476484',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers5' : { # error on alpha
        'value' : '0.000001/3.15161960947', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.52067231799',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers5' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + abs(0.46 - 0.52) / 0.46),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers5' : { # error on energy assumption
        'value' : str (1.0 + 14.9618157954 / 100.0),
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
