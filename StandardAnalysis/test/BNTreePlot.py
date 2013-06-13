#!/usr/bin/env python
#from localOptionsAll import *
from localOptionsAODCtrlMuon import *


datasets = [

#     'SingleMu_2012A_2',
'ZZ',

]           


BNTreeUseScript = True  
BNTreeChannel = 'WToMuSimple' 
BNTreeScript = 'BNTreeRun.C'  

BNTreeWt = 'events_puScaleFactor * events_muonScaleFactor * events_electronScaleFactor'   # excludes lumi weight, which is included automatically 

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


     ## { 'channel'       : 'WToMuSimple',
     ##   'varToPlot'     : '@muons_eta.size()',
     ##   'histName'      : 'muonsSize',
     ##   'nbins'         : 11,
     ##   'xMin'          : -0.5,
     ##   'xMax'          : 10.5,
     ##   'cutString'     : BNTreeWt, 
     ##   },

##      { 'channel'       : 'WToMuSimple',
##        'varToPlot'     : 'muons_eta',
##        'histName'      : 'muonsEta',
##        'nbins'         : 100,
##        'xMin'          : -3,
##        'xMax'          :  3,
##        'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',    
##        },



##      { 'channel'       : 'WToMuSimple',
##        'varToPlot'     : 'muons_pt',
##        'histName'      : 'muons_pt',
##        'nbins'         : 100,
##        'xMin'          : 0,
##        'xMax'          : 500,
##        'cutString'     : BNTreeWt, 
##        },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : '@mets_pt.size()',
##       'histName'      : 'metsSize',
##       'nbins'         : 11,
##       'xMin'          : -0.5,
##       'xMax'          : 10.5,
##       'cutString'     : BNTreeWt, 
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : '@jets_pt.size()',
##       'histName'      : 'jetsSize',
##       'nbins'         : 15,
##       'xMin'          : 0,
##       'xMax'          : 15,
##       'cutString'     : BNTreeWt,  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'jets_pt',
##       'histName'      : 'jets_pt',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : BNTreeWt,  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : BNTreeWt, 
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt_cut',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : '(mets_pt < 200) * ' + BNTreeWt,  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt_cutNJets01',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : '(@jets_pt.size() >= 0 && @jets_pt.size() <= 1 ) * ' + BNTreeWt,  
##       },


    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'mets_pt',
      'histName'      : 'mets_pt_cutNJets0',
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 500,
      'cutString'     : '(@jets_pt.size() == 0 ) * ' + BNTreeWt,  
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'mets_pt',
      'histName'      : 'mets_pt_cutNJets1',
      'nbins'         : 100,
      'xMin'          : 0,
      'xMax'          : 500,
      'cutString'     : '(@jets_pt.size() == 1 ) * ' + BNTreeWt,  
      },

    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'mets_phi - muons_phi', 
      'histName'      : 'deltaPhi_metsVsMuon', 
      'nbins'         : 100, 
      'xMin'          : -0.2, 
      'xMax'          :  3.17, 
      'cutString'     : BNTreeWt,  
      },


    { 'channel'       : 'WToMuSimple',
      'varToPlot'     : 'mets_pt:mets_phi', 
      'histName'      : 'mets_pt:mets_phi',  
      'nbins'         : 100, 
      'xMin'          : -3.17, 
      'xMax'          :  3.17, 
      'nbinsY'        : 100, 
      'yMin'          :   0, 
      'yMax'          : 500, 
      'cutString'     : BNTreeWt,  
      },


##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt_cutNJets23',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : '(@jets_pt.size() >= 2 && @jets_pt.size() <= 3 ) * ' + BNTreeWt,  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt_cutNJets45',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : '(@jets_pt.size() >= 4 && @jets_pt.size() <= 5 ) * ' + BNTreeWt,  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt_cutNJets67',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : '(@jets_pt.size() >= 6 && @jets_pt.size() <= 7 ) * ' + BNTreeWt,  
##       },

##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'mets_pt',
##       'histName'      : 'mets_pt_cutNJets8',
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 500,
##       'cutString'     : '(@jets_pt.size() >= 8 ) * ' + BNTreeWt,  
##       },

##     ## { 'channel'       : 'WToMuSimple',
##     ##   'varToPlot'     : 'events_sample',  
##     ##   'histName'      : 'events_sample', 
##     ##   'nbins'         : 100,
##     ##   'xMin'          : -100,
##     ##   'xMax'          : 100,  
##     ##   'cutString'     : BNTreeWt, 
##     ##   },

## ##     { 'channel'       : 'WToMuSimple',
## ##       'varToPlot'     : 'events_run',  
## ##       'histName'      : 'events_run', 
## ##       'nbins'         : 100,
## ##       'xMin'          : 0,
## ##       'xMax'          : 1000000,  
## ##       'cutString'     : 'events_puScaleFactor * events_muonScaleFactor',  
## ##       },


##     { 'channel'       : 'WToMuSimple',
##       'varToPlot'     : 'events_puScaleFactor',  
##       'histName'      : 'events_puScaleFactor', 
##       'nbins'         : 100,
##       'xMin'          : 0,
##       'xMax'          : 5,  
##       'cutString'     :'',  
##       },

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


