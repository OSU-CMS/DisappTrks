#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  
from lumiMet2012 import *

config_file = "trackAnalyzerStandard_cfg.py"

datasets = [
    
    'AMSB_mGrav50K_0p5ns_Reco',
    'AMSB_mGrav50K_1ns_Reco',
    'AMSB_mGrav50K_5ns_Reco',
    
    # put bkgd datasets in roughly ascending order of size of contribution after preselection
    'QCD',    
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu', 
    'DY_PtZ100',    
    'Diboson',
    'WjetsHighPt',
    
    'MET',
    
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

labels['DY_PtZ100']   = "Z#rightarrowll"
labels['WjetsHighPt'] = "W#rightarrowl#nu"

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


