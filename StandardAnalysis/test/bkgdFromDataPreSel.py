#!/usr/bin/env python

# Code for impurities is not yet implemented  
impurities = [
]


# ../scripts/bkgdFromData.py -l bkgdFromDataPreSel.py -c condor_2014_01_23_BkgdEstFromData
# makePlots.py    -y -r      -l localOptionsBkgdEst.py -c condor_2014_01_23_BkgdEstFromData -o stacked_histogramsRebin10.root -b 10 -E 100

# Get scale factors from "Total bkgd" spreadsheet

                
bkgd_sources = {

    'MET' :  { 'inputDir'   : 'condor_2014_01_14_PreSelection',
               'datasetsIn'  : ['MET'],
               'scale_factor' :       1.0,
               'scale_factor_error' : 0.0,
               'channel_map' : {
    'PreSelection' : ['PreSelection'],
        }
                                   },

    'ElecBkgd' :  { 'inputDir'   : 'JessCondor/preselFullSelNoElecVeto', 
                    'datasetsIn'  : ['MET'], 
                    'scale_factor' :        8.0e-4,
                    'scale_factor_error' :  1.2e-4,
                    'channel_map' : {
    'PreSelNoElecVeto' : ['PreSelection'],
    }
                    },

    'MuonBkgd' :  { 'inputDir'   : 'condor_2014_01_19_PreSelectionMuon',  
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        4.5e-5,
                    'scale_factor_error' :  1.2e-5,
                    'channel_map' : {
    'PreSelectionMuon' : ['PreSelection'],
    }
                    },

    'TauBkgd' :  { 'inputDir'   : 'condor_2014_01_14_PreSelectionTau', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        0.238,
                    'scale_factor_error' :  0.029,
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

    'OthrBkgd' :  { 'inputDir'   : 'condor_2014_01_20_PreSelId',   
                    'datasetsIn'  : ['Background'],
                    'scale_factor'       : 1.0,
                    'scale_factor_error' : 0,
                    'channel_map' : {
    'PreSelIdOther' : ['PreSelection'],
    }
                    },

    }



