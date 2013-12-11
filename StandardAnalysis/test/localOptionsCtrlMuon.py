#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

#config_file = "trackAnalyzerCtrlMuon_cfg.py"  
config_file = "trackAnalyzerStandard_cfg.py"  

#intLumi = 19783  # For /SingleMu/Run2012A-22Jan2013-v1/AOD 
intLumi = 876.225
datasets = [
    

## ## 'AMSB_mGrav50K_0p5ns_Reco',
## ## 'AMSB_mGrav50K_1ns_Reco',
## ## 'AMSB_mGrav50K_5ns_Reco',

#    'WjetsHighPt',
#    'DY_PtZ100',
    'DY',
    'SingleMu',
 #   'TTbar_Inclusive',
# 'Wjets',  
## 'TTbar',
# 'SingleTop',
## #    'DY_PtZ100',    
# 'DY',
# 'DYToMuMu_20',  
 #   'Diboson',
#'ZJetsToNuNu', 
# 'QCD',

]

composite_dataset_definitions['SingleMu'] = [
        'SingleMu_2012A',
]
