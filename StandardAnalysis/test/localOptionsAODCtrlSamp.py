#!/usr/bin/env python

config_file = "trackAnalyzerCtrlSamp_cfg.py"

intLumi = 8310.9 #SingleMu
#intLumi = 6376. #SingleElectron


datasets = [
    'SingleElectron',
    'SingleMu',

    'DY',
    'Wjets',
    'TTbar',
    'Diboson',
    'QCD_BCtoE',
    'QCD_EMEnriched',
    'QCD_MuEnriched',
    
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

