#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerStandard_cfg.py"
#config_file = "trackAnalyzerQuick_cfg.py"

intLumi = 19783.

datasets = [

#    'MET_data_Reco',
    'MET',
    
    'AMSB_mGrav50K_0p5ns_Reco',
    'AMSB_mGrav50K_1ns_Reco',
    'AMSB_mGrav50K_5ns_Reco',
    
    'WjetsHighPt',
    'TTbar_Inclusive',
    
    #    'TTbar',
    #  'SingleTop',
    'DY_PtZ100',    
    #    'DY',
    'Diboson',
    #    'Wjets',  
    'ZJetsToNuNu', 
    'QCD',
    #   'Background',
    
    ]

composite_dataset_definitions['Background'] = [
    'DY_PtZ100',
    'WjetsHighPt',
    'SingleTop',
    'QCD',
    'TTbar_Inclusive',
    'ZJetsToNuNu',
    'Diboson',
    ]

histsToBlind = [
    'caloTot', 

    ]


