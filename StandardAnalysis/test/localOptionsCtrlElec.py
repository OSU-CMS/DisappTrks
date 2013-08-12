#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerCtrlElec_cfg.py"  

# intLumi = 2240.  # For SingleElec_data_Reco dataset 
intLumi = 883.273  # For /SingleElectron/Run2012A-22Jan2013-v1/AOD 

datasets = [
    
'SingleElectron_2012A',
# 'SingleElec_data_Reco', 

## 'AMSB_mGrav50K_0p5ns_Reco',
## 'AMSB_mGrav50K_1ns_Reco',
## 'AMSB_mGrav50K_5ns_Reco',

#    'WjetsHighPt',
'Wjets',  
'TTbar',
'SingleTop',
#    'DY_PtZ100',    
'DY',
'Diboson',
'ZJetsToNuNu', 
'QCD',

]

