# Bkgd configuration file for limit-setting produced with makeANTables.py 
#!/usr/bin/env python  
backgrounds = {
'Elec' : {
    'N' : '37',
    'alpha' : '0.0979428781339',
        },
'Muon' : {
    'N' : '1',
    'alpha' : '0.101157268045',
        },
'Tau' : {
    'N' : '5',
    'alpha' : '0.157085111161',
        },
'Fake' : {
    'N' : '3',
    'alpha' : '1.3419234778',
        },
    }
background_systematics = { 
    'Elec' : {
    'value' : '1.86',
                 },
    'Muon' : {
    'value' : '4.0', # set by hand
                 },
    'Tau' : {
    'value' : '1.71', # set by hand  
                 },
    'Fake' : {
    'value' : '1.22',
                 },
    }
