#!/usr/bin/env python

# Code for impurities is not yet implemented  
impurities = [
]


# ../scripts/bkgdFromData.py -l bkgdFromDataAll.py -c condor_2014_01_15_BkgdEstFromData5New
bkgd_sources = {

    'ElecBkgd' :  { 'inputDir'   : 'condor_2014_01_14_PreSelectionElec',  
                    'datasetsIn'  : ['MET'], 
                    'scale_factor' :       13.1e-4,
                    'scale_factor_error' :  8.2e-4,
                    'channel_map' : {
    'PreSelectionElec' : ['PreSelection'],
    }
                    },

    'MuonBkgd' :  { 'inputDir'   : 'condor_2014_01_14_PreSelectionMuon',  
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        2.0e-4,
                    'scale_factor_error' :  1.4e-4,
                    'channel_map' : {
    'PreSelectionMuon' : ['PreSelection'],
    }
                    },

    'TauBkgd' :  { 'inputDir'   : 'condor_2014_01_14_PreSelectionTau', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        0.147,
                    'scale_factor_error' :  0.098,
                    'channel_map' : {
    'PreSelectionTau' : ['PreSelection'],
    }
                    },

    'FakeBkgd' :  { 'inputDir'   : 'condor_2014_01_13_ZtoMuMuFakeTrkPreSel',  
                    'datasetsIn'  : ['SingleMu'],
                    'scale_factor' :        0.29112, 
                    'scale_factor_error' :  1.9e-4, 
                    'channel_map' : {
    'ZtoMuMuFakeTrkPreSel' : ['PreSelection'],
    }
                    },

    'OthrBkgd' :  { 'inputDir'   : 'condor_2014_01_14_PreSelId',  
                    'datasetsIn'  : ['MET'],
                    'scale_factor'       : 1.0,
                    'scale_factor_error' : 0,
                    'channel_map' : {
    'PreSelIdOther' : ['PreSelection'],
    }
                    },

    }



