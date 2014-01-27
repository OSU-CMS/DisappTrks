#!/usr/bin/env python

# Code for impurities is not yet implemented  
impurities = [
]


# ../scripts/bkgdFromData.py -l bkgdFromDataFullSel.py -c condor_2014_01_23_BkgdEstFullSel1
# makePlots.py    -y -r      -l localOptionsBkgdEst.py -c condor_2014_01_23_BkgdEstFullSel1 -o stacked_histogramsRebin10.root -b 10 -E 100

# Get scale factors from "Total bkgd" spreadsheet

condorDirJess  = "JessCondor/"
condorDirWells = ""  
                
bkgd_sources = {

##     'MET' :  { 'inputDir'   : 'condor_FullSelection', # not yet run  
##                'datasetsIn'  : ['MET'],
##                'scale_factor' :       1.0,
##                'scale_factor_error' : 0.0,
##                'channel_map' : {
##     'PreSelection' : ['PreSelection'],
##         }
##                                    },

    'ElecBkgd' :  { 'inputDir'   : condorDirJess + 'fullSelectionNoElecVeto_23Jan',  
                    'datasetsIn'  : ['MET'], 
                    'scale_factor' :        1.75e-4, 
                    'scale_factor_error' :  9.3e-5, 
                    'channel_map' : {
    'FullSelectionElecPreveto' : ['FullSelection'],
    }
                    },

    'MuonBkgd' :  { 'inputDir'   : condorDirWells + 'condor_2014_01_20_FullSelectionMuPreveto', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        6.8e-5, 
                    'scale_factor_error' :  4.8e-5, 
                    'channel_map' : {
    'FullSelectionMuPreveto' : ['FullSelection'],
    }
                    },

    'TauBkgd' :  { 'inputDir'   : condorDirWells + 'condor_2014_01_24_FullSelectionTauPreveto', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        7.0e-3, 
                    'scale_factor_error' :  5.4e-3,  
                    'channel_map' : {
    'FullSelectionTauPreveto' : ['FullSelection'],
    }
                    },

    'FakeBkgd' :  { 'inputDir'   : condorDirWells + 'condor_2014_01_12_ZtoMuMuFakeTrk', 
                    'datasetsIn'  : ['SingleMu'],
                    'scale_factor' :        0.29112,
                    'scale_factor_error' :  1.9e-4,
                    'channel_map' : {
    'ZtoMuMuFakeTrk' : ['FullSelection'],
    }
                    },

    'OthrBkgd' :  { 'inputDir'   : condorDirWells + 'condor_2014_01_20_FullSelId',  
                    'datasetsIn'  : ['Background'],
                    'scale_factor'       : 1.0,
                    'scale_factor_error' : 0,
                    'channel_map' : {
    'FullSelIdOther' : ['FullSelection'],
    }
                    },

    }



