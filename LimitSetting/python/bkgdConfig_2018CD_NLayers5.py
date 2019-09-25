#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py
backgrounds = {
    'Fake' : {
        'N' : '17',
        'alpha' : '0.0364907468969',
    },
    'Elec' : {
        'N' : '8816',
        'alpha' : '3.37553907656e-05',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.02262756942',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.00348701989921',
    },
}

background_systematics = {
    'Fake_alpha_NLayers5' : { # error on alpha
        'value' : '1.00054076926',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers5' : { # error on alpha
        'value' : '1.79881998866',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers5' : { # error on alpha
        'value' : '0.355455996563/1.64454400344',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers5' : { # error on alpha
        'value' : '0.000001/2.36930657969', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.45037201176',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers5' : { # difference between ZtoMuMu and ZtoEE methods
        'value' : str (1.0 + abs(0.62 - 0.45) / 0.62),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers5' : { # error on energy assumption
        'value' : str (1.0 + 14.6326094591 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers5' : { # error on energy assumption
        'value' : str (1.0 + 20.0296757865 / 100.0),
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.7474 - 0.700) / 0.7474)),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.7474 - 0.700) / 0.7474)),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.4677 - 0.464) / 0.4677)),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.4677 - 0.464) / 0.4677)),
        'background' : 'Tau',
    },

    'Muon_lowStatPhemveto_NLayers5' : {
        'value' : '1.0/' + str(1.0 + abs((0.794 - 0.729) / 0.794)),
        'background' : 'Muon',
    },

}
