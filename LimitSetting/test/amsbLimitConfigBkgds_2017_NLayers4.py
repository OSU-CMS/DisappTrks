#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '68',
        'alpha' : '0.135815631144',
    },
    'Elec' : {
        'N' : '15',
        'alpha' : '0.0756021250521',
    },
    'Muon' : {
        'N' : '104',
        'alpha' : '0.0011607222849',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.00000001', # really zero
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.00053097569',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.10006941274',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '2.00120350117',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '0.00508931961', # 0 +0.00508931961 -0
        'background' : 'Tau',
    },

    'Fake_syst_fit_NLayers4' : { # error from fit
        'value' : '1.38923987949',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers4' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : '1.17391',
        'background' : 'Fake',
    },
    'Fake_syst_d0Diff_NLayers4' : { # largest difference between ZtoMuMu nominal and changing d0 sideband
        'value' : '1.075',
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
        'value' : str(1.0951),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : str(1.0951),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : str(1.0841),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : str(1.0841),
        'background' : 'Tau',
    },


}
