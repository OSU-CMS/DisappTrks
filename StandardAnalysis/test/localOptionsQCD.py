#!/usr/bin/env python

config_file = "trackAnalyzerStandard_cfg.py"
#config_file = "trackAnalyzerQuick_cfg.py"

intLumi = 19783.

datasets = [
    
    'QCD_0to5',
    'QCD_5to15',
    
    'QCD_15to30',
    'QCD_30to50',
    'QCD_80to120',
    'QCD_120to170',
    'QCD_170to300',
    'QCD_300to470',
    'QCD_470to600',
    'QCD_600to800',
    'QCD_800to1000',
    'QCD_1000to1400',
    'QCD_1400to1800',
    'QCD_1800',
    ]


composite_dataset_definitions['QCD'] = [
    'QCD_170to300',
    'QCD_300to470',
    'QCD_470to600',
    'QCD_600to800',
    'QCD_800to1000',
    'QCD_1000to1400',
    'QCD_1400to1800',
    'QCD_1800',
    ]
colors = {
   'QCD_0to5_Reco'        : 791,
   'QCD_5to15_Reco'       : 872,
   'QCD_15to30_Reco'      : 410,
   'QCD_30to50_Reco'      : 628,
   'QCD_50to80_Reco'      : 596,
   'QCD_80to120_Reco'     : 622,
   'QCD_120to170_Reco'    : 590,
   'QCD_170to300_Reco'    : 920,
   'QCD_300to470_Reco'    : 632,
   'QCD_470to600_Reco'    : 600,
   'QCD_600to800_Reco'    : 593,
   'QCD_800to1000_Reco'   : 798,
   'QCD_1000to1400_Reco'  : 794,
   'QCD_1400to1800_Reco'  : 410,
   'QCD_1800_Reco'        : 407,
   

    }

#maxEvents = {
#'DYJetsToLL'     : 100,
#'WJetsToLNu'     : 100,
#'QCD_0to5'       : 0,
#'QCD_5to15_Reco'      : 100,
#'QCD_15to30'     : 100,
#'QCD_30to50'     : 0,
#'QCD_80to120'    : 0,
#'QCD_120to170_Reco'   : 100,
#'QCD_170to300'   : 0,
#'QCD_470to600'   : 0,
#'QCD_600to800'   : 0,
#'QCD_800to1000'  : 0,
#'QCD_1000to1400_Reco' : 100,
#'QCD_1400to1800_Reco' : 100,
#'QCD_1800_Reco'       : 100,
#}

