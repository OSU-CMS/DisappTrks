#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerCtrlMuon_cfg.py"  

#intLumi = 876.225  # For SingleMu_2012A, /SingleMu/Run2012A-22Jan2013-v1/AOD 
#intLumi = 19783.   # MET ReReco data

intLumi = 18295.  # For SingleMu data as of 2013-12-07  

datasets = [
    
#    'QCD',
    'QCD_MuEnriched', 
    'SingleTop',
#    'WjetsHighPt',
    'TTbar',
    'ZJetsToNuNu', 
    'Wjets',  
    'Diboson',
#    'TTbar_Inclusive',
#    'DY_PtZ100',    
    'DY',
##    # 'DYToMuMu_20',  

##    #    'MET',

#    'SingleMu_2012A', 
     'SingleMu', 
  
## ## 'AMSB_mGrav50K_0p5ns_Reco',
## ## 'AMSB_mGrav50K_1ns_Reco',
## ## 'AMSB_mGrav50K_5ns_Reco',


]



composite_dataset_definitions['Background'] = [
    'DY',
    'TTbar_Inclusive',
    'Diboson',
    'Wjets',
    'SingleTop',
    'QCD',
    'ZJetsToNuNu',
    ]


composite_dataset_definitions['SingleMu'] = [
        'SingleMu_2012A',
]



