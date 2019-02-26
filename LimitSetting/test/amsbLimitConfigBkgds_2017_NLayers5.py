#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '32',
        'alpha' : '0.0652335906261',
    },
    'Elec' : {
        'N' : '11',
        'alpha' : '0.0682509529662',
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
        'value' : '1.03440874366',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '1.06823259842',
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


    'Fake_syst_sampleDiff_NLayers5' : { # difference between ZtoMuMu and (ZtoEE, BasicSelection) methods
        'value' : str(1.49760766),
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
