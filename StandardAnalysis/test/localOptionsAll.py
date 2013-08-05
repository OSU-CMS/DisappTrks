#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerStandard_cfg.py"
#config_file = "trackAnalyzerQuick_cfg.py"

intLumi = 18046.  # MET 2012 data registered as of 2013-05-07

datasets = [

    'MET_data_Reco',

    'AMSB_mGrav50K_0p5ns_Reco',
    'AMSB_mGrav50K_1ns_Reco',
    'AMSB_mGrav50K_5ns_Reco',

    'WjetsHighPt',
    'TTbar',
    'SingleTop',
    'DY_PtZ100',    
    #    'DY',
    'Diboson',
    #    'Wjets',  
    'ZJetsToNuNu', 
    'QCD',
    
    ]

histsToBlind = [
    'caloTot', 

    ]


