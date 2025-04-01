#!/usr/bin/env python3

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '271',
        'alpha' : '0.0925491099217114',
    },
    'Elec' : {
        'N' : '7588',
        'alpha' : '3.5742996762093184e-05',
    },
    'Muon' : {
        'N' : '2',
        'alpha' : '0.058105150338232395',
    },
    'Tau' : {
        'N' : '0',
        'alpha' : '0.0098',
    },
}

background_systematics = {
    'Fake_alpha_NLayers4' : { # error on alpha
        'value' : '1.0006237139562497',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.888450029113432', # 0 --> 0.000001 numerical safety
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers4' : { # error on alpha
        'value' : '0.000001/2.071000634110142', # 0 --> 0.000001 numerical safety
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers4' : { # error on alpha
        'value' : '1.8095110981171811', # 0 --> 0.000001 numerical safety
        'background' : 'Tau',
    },

    # Still using 2018AB values; NEEDS TO BE UPDATED
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
