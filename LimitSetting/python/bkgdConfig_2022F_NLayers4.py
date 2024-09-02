#!/usr/bin/env python3

lumiScaling = (5010.409016184 + 2970.045129108 + 5806.955207286 + 17781.598893382 + 3082.753035617 + 17794.0 + 9451.0) / (14024.176505487 + 7060.764380203) # target_lumi / 2018AB_lumi

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : str(round(175*lumiScaling)), # '175',
        'alpha' : '0.0354151132521',
    },
    'Elec' : {
        'N' : str(round(2436*lumiScaling)), # '2436',
        'alpha' : '0.000406325164861',
    },
    'Muon' : {
        'N' : str(round(2*lumiScaling)), # '2',
        'alpha' : '0.0439062314998',
    },
    'Tau' : {
        'N' : str(round(0*lumiScaling)), # '0',
        'alpha' : '0.0035259179802',
    },
}

# Still using 2018AB values; NEEDS TO BE UPDATED
background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.00074624437',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '1.62439135989',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.04721541252', # 0 --> 0.000001 numerical safety
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.92516712991', # 0 --> 0.000001 numerical safety
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
        'value' : str (1.0 + 14.4101362584 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers4' : { # error on energy assumption
        'value' : str (1.0 + 24.8215525905 / 100.0),
        'background' : 'Tau',
    },

    'Muon_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.7517 - 0.714) / 0.7517)),
        'background' : 'Muon',
    },
    'Tau_lowStatPoffline_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.7517 - 0.714) / 0.7517)),
        'background' : 'Tau',
    },

    'Muon_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.429 - 0.384) / 0.429)),
        'background' : 'Muon',
    },
    'Tau_lowStatPtrigger_NLayers4' : {
        'value' : '1.0/' + str(1.0 + abs((0.429 - 0.384) / 0.429)),
        'background' : 'Tau',
    },


}
