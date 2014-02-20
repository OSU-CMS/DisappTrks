#!/usr/bin/env python

# Code for impurities is not yet implemented  
impurities = [
]


# ../scripts/bkgdFromData.py -l bkgdFromDataFullSel.py -c condor_2014_01_23_BkgdEstFullSel1
# makePlots.py    -y -r      -l localOptionsBkgdEst.py -c condor_2014_01_23_BkgdEstFullSel1 -o stacked_histogramsRebin10.root -b 10 -E 100
# makePlots.py    -y -r      -l localOptionsBkgdEst.py -c condor_2014_01_23_BkgdEstFullSel1 -o stacked_histograms.root              -E 100

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

    'ElecBkgd' :  { 'inputDir'   : condorDirJess + 'fullSelElecPrevetoSkim', 
                    'datasetsIn'  : ['MET'], 
                    'scale_factor' :        5.5e-5,
                    'scale_factor_error' :  5.5e-5, 
                    'channel_map' : {
    'FullSelectionElecPreveto' : ['FullSelection'],
    }
                    },

    'MuonBkgd' :  { 'inputDir'   : condorDirJess + 'fullSelMuPrevetoSkim', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        1.6e-4, 
                    'scale_factor_error' :  1.6e-4, 
                    'channel_map' : {
    'FullSelectionMuPreveto' : ['FullSelection'],
    }
                    },

    'TauBkgd' :  { 'inputDir'   : condorDirJess +  'fullSelTauPrevetoSkim', 
                    'datasetsIn'  : ['MET'],
                    'scale_factor' :        9.1e-5, 
                    'scale_factor_error' :  9.2e-5, 
                    'channel_map' : {
    'FullSelectionTauPreveto' : ['FullSelection'],
    }
                    },

    'FakeBkgd' :  { 'inputDir'   : condorDirWells + 'condor_2014_02_10_ZtoMuMuFakeTrk',  
                    'datasetsIn'  : ['SingleMu'],
                    'scale_factor' :        0.29112,
                    'scale_factor_error' :  1.9e-4,
                    'channel_map' : {
    'ZtoMuMuFakeTrk' : ['FullSelection'],
    }
                    },

    'OthrBkgd' :  { 'inputDir'   : condorDirJess + 'fullSelId',  
                    'datasetsIn'  : ['Background'],
                    'scale_factor'       : 1.0,
                    'scale_factor_error' : 0,
                    'channel_map' : {
    'FullSelIdOther' : ['FullSelection'],
    }
                    },

    }



