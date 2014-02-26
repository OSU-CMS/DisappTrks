#!/usr/bin/env python

# Code for impurities is not yet implemented  
impurities = [
]


# ../scripts/bkgdFromData.py -l bkgdFromDataPreSel.py -c condor_2014_01_23_BkgdEstFromData
# makePlots.py    -y -r      -l localOptionsBkgdEst.py -c condor_2014_01_23_BkgdEstFromData -o stacked_histogramsRebin10.root -b 10 -E 100

# Get scale factors from "Total bkgd" spreadsheet



condorDirJess  = ""
condorDirWells = "WellsCondorNew/"

                
bkgd_sources = {

    'MET' :  { 'inputDir'   : condorDirJess + 'preselSkim_9Feb',
               'datasetsIn'  : ['MET'],
               'scale_factor' :       1.0,
               'scale_factor_error' : 0.0,
               'channel_map' : {
    'PreSelection' : ['PreSelection'],
        }
                                   },

    'ElecBkgd' :  { 'inputDir'   : condorDirJess + 'preselElecSkim_9Feb', 
                    'datasetsIn'  : ['MET'], 
#                    'scale_factor' :        8.0e-4, #unscaled by systematic
#                    'scale_factor_error' :  1.2e-4, 
                    'scale_factor' :        3.8e-4,
                    'scale_factor_error' :  8.4e-5,
                    'channel_map' : {
    'PreSelectionElec' : ['PreSelection'],
    }
                    },

    'MuonBkgd' :  { 'inputDir'   : condorDirJess + 'preselMuonMet_9Feb',  
                    'datasetsIn'  : ['MET'],
#                    'scale_factor' :        1.60e-4,
                    'scale_factor' :        1.51e-4,
#                    'scale_factor_error' :  0.43e-4,
                    'scale_factor_error' :  4.06e-5,
                    'channel_map' : {
    'PreSelectionMuonMet' : ['PreSelection'],
    }
                    },

    'TauBkgd' :  { 'inputDir'   : condorDirJess +'preselTauSkim_11Feb', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        0.184,
                    'scale_factor_error' :  0.0318,
                    'channel_map' : {
    'PreSelectionTau' : ['PreSelection'],
    }
                    },

    'FakeBkgd' :  { 'inputDir'   : condorDirWells +  'condor_2014_02_10_ZtoMuMuFakeTrkPreSel',  
                    'datasetsIn'  : ['SingleMu'],
                    'scale_factor' :        0.29112, 
                    'scale_factor_error' :  1.9e-4, 
                    'channel_map' : {
    'ZtoMuMuFakeTrkPreSel' : ['PreSelection'],
    }
                    },

    'OthrBkgd' :  { 'inputDir'   : condorDirJess + 'preselId_11Feb',   
                    'datasetsIn'  : ['Background'],
                    'scale_factor'       : 1.0,
                    'scale_factor_error' : 0,
                    'channel_map' : {
    'PreSelIdOther' : ['PreSelection'],
    }
                    },

    }



