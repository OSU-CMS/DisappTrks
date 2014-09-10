#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerCtrlMuon_cfg.py"  

intLumi = 19423.  # For DoubleMu data as of 2014-04-11

datasets = [

    
#   'QCD_MuEnriched', 
    'ZJetsToNuNu', 
     'SingleTop',
     'TTbar',
     'Wjets',  
     'Diboson',
     'DY',
#      'DYToEE_20',     # Powheg + Pythia
##  #    'DYToMuMu_20',   # Powheg + Pythia
#      'DYToTauTau_20', # Powheg + Pythia

## ##  ##     # Testing:
#     'DYToMuMu_20_Pythia', 

      'DoubleMu_22Jan2013',  
##     'DoubleMu_2012A_22Jan2013',
##     'DoubleMu_2012B_22Jan2013',
##     'DoubleMu_2012C_22Jan2013',
##     'DoubleMu_2012D_22Jan2013',
# 'Background',   


]


composite_dataset_definitions['Background'] = [
    'QCD_MuEnriched', 
    'ZJetsToNuNu', 
    'SingleTop',
    'TTbar',
    'Wjets',  
    'Diboson',
#    'DY',
    'DYToEE_20',
    'DYToTauTau_20',
    'DYToMuMu_20_Pythia', 
    ]



