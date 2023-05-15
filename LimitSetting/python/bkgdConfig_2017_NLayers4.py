#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py
# If 'adhocScaling' is supplied, the background will be scaled by the value -- for normal limits, don't use it!

backgrounds = {
    'Fake' : {
        'N' : '271',
        'alpha' : '0.0401045591548',
    },
    'Elec' : {
        'N' : '4690',
        'alpha' : '0.000292513276465',
    },
    'Muon' : {
        # really should be N=1, alpha=0.0 - 0.0 + 0.00189403535617
        # re-parameterize with N = 0 (p_veto numerator)
        'N' : '0',
        'alpha' : '0.0017',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.00754775945537',
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.00052390363',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.63670563535',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '2.00320619491',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '0.236358797246/2.22040993894',
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.42537586979',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers4' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + (10.87 - 10.17) / 10.87),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 13.8466686504 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0951),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0951),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0841),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0841),
        'background' : 'Tau',
    },


}

# Any entries here will scale the sample's signal yields, via signalSF.txt, by the given value
# This should be empty or not exist at all in normal operation!
# { datasetLabel : value }
adhocSignalScaling = {

}
