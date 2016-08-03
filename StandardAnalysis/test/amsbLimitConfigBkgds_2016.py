#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
'Elec2016' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/739
    'N' : '47529',
    'alpha' : '0.00010171511993',
        },
'Muon2016' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/739
    'N' : '2402',
    'alpha' : '0.000436801817075',
        },
'Tau2016' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/739
    'N' : '23',
    'alpha' : '0.00246760800619',
        },
'Fake2016' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/739
    'N' : '0',
    'alpha' : '0.639722728258',
        },
}

background_systematics = {
    'Elec2016' : { # error on alpha
    'value' : '1.16427229934',
                 },
    'Muon2016' : { # error on alpha
    'value' : '1.32086958369',
                 },
    'Tau2016' : { # error on alpha
    'value' : '2.78189831197',
                 },
    'Fake2016' : { # error on alpha
    'value' : '1.0009896082',
                 },
}
