#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '0',
        'alpha' : '0.0364907468969',
    },
    'Elec' : {
        'N' : '428330',
        'alpha' : '1.09656193307e-05',
    },
    'Muon' : {
        'N' : '755690',
        'alpha' : '5.99288423277e-07',
    },
    'Tau' : {
        'N' : '3800',
        'alpha' : '0.000138744043434',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00054076926',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.21330899396',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.37487629459',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '0.000001/2.13483262792', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.45037201176',
        'background' : 'Fake',
    },
# 0 - 0 --> no systematic
#    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
#        'value' : str (1.0 + abs(0.035 - 0.087) / 0.035),
#        'background' : 'Fake',
#    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.8097922621 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 20.0296757865 / 100.0),
        'background' : 'Tau',
    },
}
