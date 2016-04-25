# Bkgd configuration file for limit-setting produced with makeANTables.py 
#!/usr/bin/env python  
backgrounds = {
'Elec' : {
    'N' : '2',
    'alpha' : '0.1279087414',
        },
'Muon' : {
    'N' : '0',
    'alpha' : '0.134569932947',
        },
'Tau' : {
    'N' : '0',
    'alpha' : '0.196531791908',
        },
'Fake' : {
    'N' : '0',
    'alpha' : '0.569361757681',
        },
    }
background_systematics = { 
    'Elec' : {
    'value' : '2.5',     # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/637 
                 },
    'Muon' : {
    'value' : '2.5',     # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/635 
                 },
    'Tau' : {
    'value' : '1.71',    # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/621 
                 },
    'Fake' : {
    'value' : '1.22',    # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/659 
                 },
    }
