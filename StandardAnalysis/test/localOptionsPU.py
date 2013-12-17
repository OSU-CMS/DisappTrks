#!/usr/bin/env python

# For usage instructions, see:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Pile_Up_Reweighting

import os

config_file = os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/AnaTools/test/pu_cfg.py'  

#intLumi = 30000.

datasets = [
    'AMSB_mGrav75K_0p5ns_Reco',
    'AMSB_mGrav75K_1ns_Reco',
    'AMSB_mGrav75K_5ns_Reco',

###Samples commented out here have already been done####

##     'DY_PtZ220',
##     'Wjets_PtW220', 


#    'WG', 
##     'AMSB_mGrav50K_0p5ns_Reco',
##     'AMSB_mGrav50K_1ns_Reco',
##     'AMSB_mGrav50K_5ns_Reco',
#    'DYJetsToLL_Reco',
#    'WJetsToLNu_Reco',
#    'QCD_Reco',
#    'QCD_0to5_Reco',
#    'QCD_5to15_Reco',
#    'QCD_30to50_Reco',
#    'QCD_80to120_Reco',
#    'QCD_120to170_Reco',
#    'QCD_170to300_Reco',
#    'QCD_300to470_Reco',
#    'QCD_470to600_Reco',
#    'QCD_600to800_Reco',
#    'QCD_800to1000_Reco',
#    'QCD_1000to1400_Reco',
#    'QCD_1400to1800_Reco',
#    'QCD_1800_Reco',   
###Add any new samples for pileup reweighting here####
    

]


