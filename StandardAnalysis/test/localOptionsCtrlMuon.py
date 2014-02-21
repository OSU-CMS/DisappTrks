#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerCtrlMuon_cfg.py"  

intLumi = 19698.  # For SingleMu data as of 2014-01-10

datasets = [
    
    'QCD_MuEnriched', 
    'ZJetsToNuNu', 
    'SingleTop',
    'TTbar',
    'Wjets',  
    'Diboson',
    'DY',

    'SingleMu',   

]


composite_dataset_definitions['Background'] = [
    'QCD_MuEnriched', 
    'ZJetsToNuNu', 
    'SingleTop',
    'TTbar',
    'Wjets',  
    'Diboson',
    'DY',
    ]



