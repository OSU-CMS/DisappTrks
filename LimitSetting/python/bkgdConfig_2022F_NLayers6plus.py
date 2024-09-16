#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

lumiScaling = (5010.409016184 + 2970.045129108 + 5806.955207286 + 17781.598893382 + 3082.753035617 + 17794.0 + 9451.0) / (14024.176505487 + 7060.764380203) # target_lumi / 2018AB_lumi

backgrounds = {
    'Fake' : {
        'N' : str(round(1.0*lumiScaling)), # '1',
        'alpha' : '0.0354151129416',
    },
    'Elec' : {
        'N' : str(round(234700.0*lumiScaling)), # '234700',
        'alpha' : '6.05334846411e-06',
    },
    'Muon' : {
        'N' : str(round(428980.0*lumiScaling)), # '428980',
        'alpha' : '8.78345986154e-07',
    },
    'Tau' : {
        'N' : str(round(0.0*lumiScaling)), # '0',
        'alpha' : '0.048',
    },
}

# Still using 2018AB values; NEEDS TO BE UPDATED
background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00074624437',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.3689209328',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.39533579372',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '0.000001/2.77468239654', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.52067231799',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
    'value' : str (1.0 + abs(0.035 - 0.087) / 0.035),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.937307135 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 24.8215525905 / 100.0),
        'background' : 'Tau',
    },
}
