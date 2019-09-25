#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py
backgrounds = {
    'Fake' : {
        'N' : '25',
        'alpha' : '0.0401045591525',
    },
    'Elec' : {
        'N' : '10450',
        'alpha' : '7.20208271646e-05',
    },
    'Muon' : {
        'N' : '2',
        'alpha' : '0.0153213683826',
    },
    'Tau' : {
        'N' : '29',
        'alpha' : '0.00637758523765',
    },
}

background_systematics = {
    'Fake_alpha_NLayers5' : { # error on alpha
        'value' : '1.00052390363',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '1.40197623285',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers5' : { # error on alpha
        'value' : '1.41938707971',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers5' : { # error on alpha
        'value' : '0.553078347914/1.47374344707',
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.42537586979',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers5' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + (1.00 - 0.55) / 1.00),
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
        'value' : '1.0/' + str(1.0593),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers5' : {
        'value' : '1.0/' + str(1.0593),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers5' : {
        'value' : '1.0/' + str(1.0097),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers5' : {
        'value' : '1.0/' + str(1.0097),
        'background' : 'Tau',
    },
}
