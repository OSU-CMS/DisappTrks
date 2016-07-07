#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
'Elec' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/715
    'N' : '44129',
    'alpha' : '6.276016681071405e-5',
        },
'Muon' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/705
    'N' : '379',
    'alpha' : '1.465250659630607e-5',
        },
'Tau' : { # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/710
    'N' : '0',
    'alpha' : '0.0124190476190749',
        },
'Fake' : {
    'N' : '0',
    'alpha' : '0.569361757681',
        },
}

background_systematics = {
    'Elec' : {
    'value' : '1.2057287367251016',
                 },
    'Muon' : {
    'value' : '1.4641395609543109',
                 },
    'Tau' : {
    'value' : '1.5115259540529666',
                 },
    'Fake' : {
    'value' : '1.22',    # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/659
                 },
}
