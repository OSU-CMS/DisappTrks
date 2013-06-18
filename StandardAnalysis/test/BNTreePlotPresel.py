#!/usr/bin/env python
#from localOptionsAll import *
from localOptionsAll import *


datasets = [
     
## ## ##      'SingleMu_2012A_1',
##     'SingleMu_2012A_2',
'ZZ',

##     'SingleMu',
##     'Wjets',
## #    'ZJetsToNuNu',
##     'DYToBB_50',
##     'Diboson',
##     'QCD_MuEnriched',
##     'TTbar',
##     'DY',
    
    
    ]           

BNTreeUseScript = False
BNTreeScript = 'BNTreePreselRun.C'  

BNTreeChannel = 'WToMuSimple'  
#BNTreeChannel = 'PreSelectionWithTrigJetMet'  
BNTreeWt = 'events_puScaleFactor * events_muonScaleFactor * events_electronScaleFactor'   # excludes lumi weight, which is included automatically 

input_histograms = [


     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_caloTotDeltaRp5RhoCorr',
       'histName'      : 'tracks_caloTotDeltaRp5RhoCorr',
       'nbins'         : 100,
       'xMin'          : 20,
       'xMax'          : 400,
       'cutString'     : BNTreeWt, 
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_caloTotDeltaRp5ByPRhoCorr',
       'histName'      : 'tracks_caloTotDeltaRp5ByPRhoCorr',
       'nbins'         : 100,
       'xMin'          : 0.2,
       'xMax'          : 6,
       'cutString'     : BNTreeWt, 
       },


    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'events_puScaleFactor',  
      'histName'      : 'events_puScaleFactor', 
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 5,  
      'cutString'     :'',  
      },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'events_muonScaleFactor',  
##       'histName'      : 'events_muonScaleFactor', 
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 5,  
##       'cutString'     : '',  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'events_electronScaleFactor',  
##       'histName'      : 'events_electronScaleFactor', 
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 5,  
##       'cutString'     : '',  
##       },



    ]


