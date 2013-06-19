#!/usr/bin/env python
#from localOptionsAll import *
from localOptionsAll import *


## datasets = [
     
## ## ## ##      'SingleMu_2012A_1',
## ##     'SingleMu_2012A_2',
## 'ZZ',

## ##     'SingleMu',
## ##     'Wjets',
## ## #    'ZJetsToNuNu',
## ##     'DYToBB_50',
## ##     'Diboson',
## ##     'QCD_MuEnriched',
## ##     'TTbar',
## ##     'DY',
    
    
##     ]           

BNTreeUseScript = True
BNTreeScript = 'BNTreePreselRun.C'  

#BNTreeChannel = 'WToMuSimple'  
BNTreeChannel = 'PreSelectionWithTrigJetMet'  
BNTreeWt = 'events_puScaleFactor * events_muonScaleFactor * events_electronScaleFactor'   # excludes lumi weight, which is included automatically 
BNTreeCutIso      = '(tracks_depTrkRp5MinusPt < 7) * '  
BNTreeCutIsoNHits = '(tracks_depTrkRp5MinusPt < 7 && tracks_nHitsMissingOuter >= 3) * '  

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

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_depTrkRp5MinusPt',
       'histName'      : 'tracks_depTrkRp5MinusPt',
       'nbins'         : 100,
       'xMin'          : 0,
       'xMax'          : 100,
       'cutString'     : BNTreeWt, 
       },


     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_nHitsMissingOuter',
       'histName'      : 'tracks_nHitsMissingOuter',
       'nbins'         : 16,
       'xMin'          : -0.5,
       'xMax'          : 15.5,
       'cutString'     : BNTreeWt, 
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_caloTotDeltaRp5RhoCorr',
       'histName'      : 'tracks_caloTotDeltaRp5RhoCorrCutIso',
       'nbins'         : 100,
       'xMin'          : 20,
       'xMax'          : 400,
       'cutString'     : BNTreeWt, 
       'cutString'     : BNTreeCutIso + BNTreeWt,
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_caloTotDeltaRp5ByPRhoCorr',
       'histName'      : 'tracks_caloTotDeltaRp5ByPRhoCorrCutIso',
       'nbins'         : 100,
       'xMin'          : 0.2,
       'xMax'          : 6,
       'cutString'     : BNTreeWt, 
       'cutString'     : BNTreeCutIso + BNTreeWt,
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_depTrkRp5MinusPt',
       'histName'      : 'tracks_depTrkRp5MinusPtCutIso',
       'nbins'         : 100,
       'xMin'          : 0,
       'xMax'          : 100,
       'cutString'     : BNTreeWt, 
       'cutString'     : BNTreeCutIso + BNTreeWt,
       },


     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_nHitsMissingOuter',
       'histName'      : 'tracks_nHitsMissingOuterCutIso',
       'nbins'         : 16,
       'xMin'          : -0.5,
       'xMax'          : 15.5,
       'cutString'     : BNTreeCutIso + BNTreeWt,
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_caloTotDeltaRp5RhoCorr',
       'histName'      : 'tracks_caloTotDeltaRp5RhoCorrCutIsoNHits',
       'nbins'         : 100,
       'xMin'          : 20,
       'xMax'          : 400,
       'cutString'     : BNTreeCutIsoNHits + BNTreeWt,
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_caloTotDeltaRp5ByPRhoCorr',
       'histName'      : 'tracks_caloTotDeltaRp5ByPRhoCorrCutIsoNHits',
       'nbins'         : 100,
       'xMin'          : 0.2,
       'xMax'          : 6,
       'cutString'     : BNTreeCutIsoNHits + BNTreeWt,
       },

     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_depTrkRp5MinusPt',
       'histName'      : 'tracks_depTrkRp5MinusPtCutIsoNHits',
       'nbins'         : 100,
       'xMin'          : 0,
       'xMax'          : 100,
       'cutString'     : BNTreeCutIsoNHits + BNTreeWt,
       },


     { 'channel'       : BNTreeChannel, 
       'varToPlot'     : 'tracks_nHitsMissingOuter',
       'histName'      : 'tracks_nHitsMissingOuterCutIsoNHits',
       'nbins'         : 16,
       'xMin'          : -0.5,
       'xMax'          : 15.5,
       'cutString'     : BNTreeCutIsoNHits + BNTreeWt,
       },



     { 'channel'       : BNTreeChannel, 
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


