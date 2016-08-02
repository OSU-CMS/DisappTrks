#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
'Elec2015' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/715
    'N' : '16916',
    'alpha' : '0.000125822768015',
        },
'Muon2015' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/705
    'N' : '368',
    'alpha' : '0.000489246316558',
        },
'Tau2015' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/710
    'N' : '201',
    'alpha' : '0.000339872143174',
        },
'Fake2015' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/659
    'N' : '0',
    'alpha' : '0.669605647035',
        },
}

background_systematics = {
    'Elec2015' : { # error on alpha
    'value' : '1.20422601774',
                 },
    'Muon2015' : { # error on alpha
    'value' : '1.72033300526',
                 },
    'Tau2015' : { # error on alpha
    'value' : '2.77509559118',
                 },
    'Fake2015' : { # error on alpha
    'value' : '1.00140266199',
                 },
}
