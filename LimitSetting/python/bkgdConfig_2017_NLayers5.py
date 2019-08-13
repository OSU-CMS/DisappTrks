#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py
backgrounds = {
    'Fake' : {
        'yield' : '0.91',
        'error' : str (1.0 - 0.22/0.91) + '/' + str (1.0 + 0.26/0.91),
    },
    'Elec' : {
        'N' : '11',
        'alpha' : '0.0684446948292',
    },
    'Muon' : {
        'N' : '14',
        'alpha' : '0.00212289996843',
    },
    'Tau' : {
        'N' : '29',
        'alpha' : '0.016979672619',
    },
}

background_systematics = {
    'Fake_alpha_NLayers5' : { # error on alpha
        'value' : '1.00052390363',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '1.06823383556',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers5' : { # error on alpha
        'value' : '1.70866307346',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers5' : { # error on alpha
        'value' : '1.51717569732',
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.38923987949',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers5' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + (0.91 - 0.60) / 0.91),
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

    'Muon_lowStatPoffline_NLayers5' : {
        'value' : str(1.0593),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers5' : {
        'value' : str(1.0593),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers5' : {
        'value' : str(1.0097),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers5' : {
        'value' : str(1.0097),
        'background' : 'Tau',
    },
}
