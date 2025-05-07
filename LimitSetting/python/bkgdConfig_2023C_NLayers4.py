#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '276',
        'alpha' : '0.0293',
    },
    'Elec' : {
        'N' : '0',
        'alpha' : '0.0273',
    },
    'Muon' : {
        'N' : '1',
        'alpha' : '0.0666',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.0204',
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.6708',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.0936', # 0 --> 0.000001 numerical safety
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.208477976691147', # 0 --> 0.000001 numerical safety
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '1.5783', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    # Still using 2018AB values; NEEDS TO BE UPDATED
    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '2.822',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers4' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : '1.016',
        'background' : 'Fake',
    },

    'Elec_energy_NLayers4' : { # error on energy assumption
        'value' : '1.132',
        'background' : 'Elec',
    },
    'Tau_energy_NLayers4' : { # error on energy assumption
        'value' : '1.021',
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.708 - 0.634) / 0.708)),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.708 - 0.634) / 0.708)),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.530 - 0.501) / 0.429)),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.530 - 0.501) / 0.429)),
        'background' : 'Tau',
    },


}
