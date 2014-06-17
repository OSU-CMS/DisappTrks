#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  
from OSUT3Analysis.Configuration.processingUtilities import *
from lumiMet2012 import *

config_file = "trackAnalyzerStandard_cfg.py"

datasets = [
    
    'AMSB_mGrav50K_0p5ns',
    'AMSB_mGrav50K_1ns',
    'AMSB_mGrav50K_5ns',

##     # put bkgd datasets in roughly ascending order of size of contribution after preselection
    'QCD',    
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu', 
    'DY',  
    'Diboson',
    'WjetsHighPt',

    'MET',
    ]

composite_dataset_definitions['Background'] = [
    'QCD',    
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu', 
    'DY', 
    'Diboson',
    'WjetsHighPt',
    ]

labels['WjetsHighPt'] = "W#rightarrowl#nu"

composite_dataset_definitions['QCD'] = [
    'QCD_80to120',
    'QCD_120to170',
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
    'CaloTot', 
    ]





