#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerCtrlElec_cfg.py"  

intLumi = 19657  # For SingleElectron 2012A,B,C,D (as of 2014-02-07)  

datasets = [
    
    'QCD',
    'ZJetsToNuNu', 
    'SingleTop',
    'TTbar',
    'Wjets',  
    'Diboson',
    'DY',
    
    'SingleElectron',
    
]


composite_dataset_definitions['Background'] = [
    'QCD',
    'ZJetsToNuNu', 
    'SingleTop',
    'TTbar',
    'Wjets',  
    'Diboson',
    'DY',
    ]



