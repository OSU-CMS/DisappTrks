#!/usr/bin/env python
#from localOptionsAll import *
from localOptionsAll import *


## datasets = [
     
#   'MET',
#    'MET_data_Reco',                                                                                                                                                                                    

##     'AMSB_mGrav50K_0p5ns_Reco',                                                                                                                                                                       
##     'AMSB_mGrav50K_1ns_Reco',                                                                                                                                                                         
##     'AMSB_mGrav50K_5ns_Reco',                                                                                                                                                                         

##     'Wjets',                                                                                                                                                                                          
##     'ZJetsToNuNu',                                                                                                                                                                                    
##     'TTbar',                                                                                                                                                                                          
##     'QCD',                                                                                                                                                                                            
##     'DY',                                                                                                                                                                                             
##     'Diboson',                                                                                                                                                                                         
    
##     ]           

BNTreeUseScript = True
BNTreeScript = 'BNTreeMonojetRun.C'  

BNTreeChannel = 'MonoJet'  
BNTreeWt = 'events_puScaleFactor * events_muonScaleFactor * events_electronScaleFactor'   # excludes lumi weight, which is included automatically 

input_histograms = [


    ]


