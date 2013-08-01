#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerCtrlElec_cfg.py"  

intLumi = 99999.  # Need to get this  

datasets = [
    
'SingleElec_data_Reco', 

'AMSB_mGrav50K_0p5ns_Reco',
'AMSB_mGrav50K_1ns_Reco',
'AMSB_mGrav50K_5ns_Reco',

#    'WjetsHighPt',
'Wjets',  
'TTbar',
#    'DY_PtZ100',    
'DY',
'Diboson',
'TTbar',
'ZJetsToNuNu', 
'QCD',

]

