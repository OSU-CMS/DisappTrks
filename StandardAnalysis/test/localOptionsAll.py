#!/usr/bin/env python

config_file = "trackAnalyzerStandard_cfg.py"
#config_file = "trackAnalyzerQuick_cfg.py"

#intLumi = 19500.
intLumi = 18046.  # MET 2012 data registered as of 2013-05-07


datasets = [

    'MET_data_Reco',
    
    'AMSB_mGrav50K_0p5ns_Reco',
    'AMSB_mGrav50K_1ns_Reco',
    'AMSB_mGrav50K_5ns_Reco',
    
    'WJetsToLNu_Reco',
    'TTbar_Reco',
    'QCD_Reco',
    'DYJetsToLL_Reco',
    'ZJetsToNuNu', 
    
    ]


#maxEvents = {
#'DYJetsToLL'     : 100,
#'WJetsToLNu'     : 100,
#'QCD_0to5'       : 100,
#'QCD_5to15'      : 100,
#'QCD_15to30'     : 100,
#'QCD_30to50'     : 100,
#'QCD_80to120'    : 100,
#'QCD_120to170'   : 100,
#'QCD_170to300'   : 100,
#'QCD_470to600'   : 100,
#'QCD_600to800'   : 100,
#'QCD_800to1000'  : 100,
#'QCD_1000to1400' : 100,
#'QCD_1400to1800' : 100,
#'QCD_1800'       : 100,
#}

