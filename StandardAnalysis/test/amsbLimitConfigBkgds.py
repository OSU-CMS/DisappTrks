#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
'Elec2015' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/715
    'N' : '44129',
    'alpha' : '6.276016681071405e-5',
        },
'Muon2015' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/705
    'N' : '379',
    'alpha' : '1.465250659630607e-5',
        },
'Tau' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/710
    'N' : '0',
    'alpha' : '0.0124190476190749',
        },
'Fake' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/659
    'N' : '0',
    'alpha' : '0.571428571428571',
        },

'Elec2016' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/732
    'N' : '32361',
    'alpha' : '8.07167905141992e-05',
        },
'Muon2016' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/732
    'N' : '1615',
    'alpha' : '2.40472787764706e-05',
        },
}

background_systematics = {
    'Elec2015' : { # error on alpha
    'value' : '1.2057287367251016',
                 },
    'Muon2015' : { # error on alpha
    'value' : '1.4641395609543109',
                 },
    'Tau' : { # error on alpha
    'value' : '1.5115259540529666',
                 },
    'Fake' : { # error on alpha + systematic error
    'value' : '1.220005252038150',
                 },

    'Elec2016' : { # error on alpha
    'value' : '1.1695386695260912',
                 },
    'Muon2016' : { # error on alpha
    'value' : '1.2508672533825393',
                 },
}
