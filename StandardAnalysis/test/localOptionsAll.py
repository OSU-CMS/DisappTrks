#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  

config_file = "trackAnalyzerStandard_cfg.py"
#config_file = "trackAnalyzerQuick_cfg.py"

intLumi = 19783.  # For all 2012 data
intLumi = 5097.541 # For 2012A,B data 

datasets = [

#      'MET',
       'MET_2012A',
       'MET_2012B',
    
      'AMSB_mGrav50K_0p5ns_Reco',
      'AMSB_mGrav50K_1ns_Reco',
      'AMSB_mGrav50K_5ns_Reco',

      'WjetsHighPt',
 #    'Wjets_PtW220',
 #    'TTbar_Inclusive',

      'TTbar',
      'SingleTop',
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

##     'QCD_0to5',
##     'QCD_5to15',
##     'QCD_15to30',
##     'QCD_30to50',
##     'QCD_50to80',
##     'QCD_80to120',
##     'QCD_120to170',

composite_dataset_definitions['QCD'] = [
    'QCD_170to300',
    'QCD_300to470',
    'QCD_470to600',
    'QCD_600to800',
    'QCD_800to1000',
    'QCD_1000to1400',
    'QCD_1400to1800',
    'QCD_1800'
    ]


histsToBlind = [
    'caloTot', 

    ]


