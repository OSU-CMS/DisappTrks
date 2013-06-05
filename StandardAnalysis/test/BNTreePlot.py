#!/usr/bin/env python
#from localOptionsAll import *
from localOptionsAODCtrlMuon import *


datasets = [

#    'SingleMu_2012A_2',
     'ZZ',

]           



input_histograms = [
##     { 'channel'       : 'PreSelMuonMatchTrigMuonV2',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'metsNumJets0',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     :'@jets_pt.size() == 0',
## #      'cutString'     :'mets_met > 50 && mets_met < 70', #for multiple cuts
##       },

#    { 'channel'       : 'PreSelMuonMatchTrigMuonV2',
#      'varToPlot'     : 'mets_pt',
#      'histName'      : 'metsNumJets1',
#      'nbins'         : 100,
#      'xMin'          : 0,
#      'xMax'          : 500,
#      'cutString'     :'@jets_pt.size() == 1',
      #      'cutString'     :'mets_met > 50 && mets_met < 70', #for multiple cuts
#            },
#    { 'channel'       : 'PreSelMuonMatchTrigMuonV2',
#       'varToPlot'     : 'mets_pt',
#       'histName'      : 'metsNumJets2',
#       'nbins'         : 100,
#       'xMin'          : 0,
#       'xMax'          : 500,
#       'cutString'     :'@jets_pt.size() == 2',
             #      'cutString'     :'mets_met > 50 && mets_met < 70', #for multiple cuts
#                   },
##     { 'channel'       : 'PreSelMuonMatchTrigMuonV2',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'metsNumJets3',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     :'@jets_pt.size() == 3',
##                   #      'cutString'     :'mets_met > 50 && mets_met < 70', #for multiple cuts
##                         },
##     { 'channel'       : 'PreSelMuonMatchTrigMuonV2',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'metsNumJets4',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     :'@jets_pt.size() == 4',
##                         #      'cutString'     :'mets_met > 50 && mets_met < 70', #for multiple cuts
##       },


#################


     { 'channel'       : 'WToMuSimple',
       'varToPlot'     : '@muons_eta.size()',
       'histName'      : 'muonsSize',
       'nbins'         : 11,
       'xMin'          : -0.5,
       'xMax'          : 10.5,
       'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',  
       },

##      { 'channel'       : 'WToMuSimple',
##        'varToPlot'     : 'muons_eta',
##        'histName'      : 'muonsEta',
##        'nbins'         : 100,
##        'xMin'          : -3,
##        'xMax'          :  3,
##        'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',    
##        },


     BNTreeStdWt = 'events_puScaleFactor * events_muonScaleFactor' 

     { 'channel'       : 'WToMuSimple',
       'varToPlot'     : 'muons_pt',
       'histName'      : 'muons_pt',
       'nbins'         : 100,
       'xMin'          : 0,
       'xMax'          : 500,
       'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',    
       },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : '@mets_pt.size()',
      'histName'      : 'metsSize',
      'nbins'         : 11,
      'xMin'          : -0.5,
      'xMax'          : 10.5,
      'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',    
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'mets_pt',
      'histName'      : 'mets_pt',
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 500,
      'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',    
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'mets_pt',
      'histName'      : 'mets_pt_cut',
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 500,
      'cutString'     : '(mets_pt < 200) * events_puScaleFactor * events_muonScaleFactor',    
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'events_sample',  
      'histName'      : 'eventsSample', 
      'nbins'         : 100,
      'xMin'          : -100,
      'xMax'          : 100,  
      'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',    
      },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'events_run',  
##       'histName'      : 'events_run', 
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 1000000,  
##       'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',  
##       },


    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'events_puScaleFactor',  
      'histName'      : 'eventsPUScaleFactor', 
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 5,  
      'cutString'     :'',  
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'events_muonScaleFactor',  
      'histName'      : 'events_muonScaleFactor', 
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 5,  
      'cutString'     : '',  
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'events_electronScaleFactor',  
      'histName'      : 'events_electronScaleFactor', 
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 5,  
      'cutString'     : '',  
      },


    ]


