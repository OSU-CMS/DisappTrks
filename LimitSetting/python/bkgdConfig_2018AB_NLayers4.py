#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '175',
        'alpha' : '0.0354151132521',
    },
    'Elec' : {
        'N' : '2436',
        'alpha' : '0.000341313138484',
    },
    'Muon' : {
        'N' : '2',
        'alpha' : '0.0412718576098 ',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.00317332618218',
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.00074624437',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.62436298695',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.04720676682', # 0 --> 0.000001 numerical safety
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.92515558686', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.52067687913',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers4' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + abs(6.2 - 7.59) / 6.2),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 13.8438107161 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 22.1600192288 / 100.0),
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers4' : {
        'value' : str(1.073677),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : str(1.073677),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : str(1.014094),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : str(1.014094),
        'background' : 'Tau',
    },


}
