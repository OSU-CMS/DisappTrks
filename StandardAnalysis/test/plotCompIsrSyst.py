#!/usr/bin/env python  
#

input_sources = [    

## ## # ~/workdirTemplateDisTrk]$ makeComparisonPlots.py -g -r -l plotCompIsrSyst.py -o condor/condor_2014_03_06_IsrSyst/compareIsr75KStdVsDn.root -b 5
##     { 'condor_dir' : 'condor_2014_03_06_IsrSyst',  
##       'dataset' : 'hist_charginoIsrDn_amsb_mGrav75K_1ns_GEN',  
##       'channel' : 'demo', 
##       'legend_entry' : '#chi, 247 GeV, ISR vary down',  
##       'marker' : 'triangle',
##       'fill' : 'hollow',
##       'color' : 'black', 
##           },
##     { 'condor_dir' : 'condor_2014_03_06_IsrSyst',   
##       'dataset' : 'hist_chargino_amsb_mGrav75K_1ns_GEN',   
##       'channel' : 'demo', 
##       'legend_entry' : '#chi, 247 GeV, default',  
##       'marker' : 'circle',
##       'fill' : 'solid',
##       'color' : 'red', 
##           },


## ## # ~/workdirTemplateDisTrk]$ makeComparisonPlots.py -g -r -l plotCompIsrSyst.py -o condor/condor_2014_03_06_IsrSyst/compareIsr75KStdVsUp.root -b 5
##     { 'condor_dir' : 'condor_2014_03_06_IsrSyst',  
##       'dataset' : 'hist_charginoIsrUp_amsb_mGrav75K_1ns_GEN',  
##       'channel' : 'demo', 
##       'legend_entry' : '#chi, 247 GeV, ISR vary up',  
##       'marker' : 'triangle',
##       'fill' : 'hollow',
##       'color' : 'black', 
##           },
##     { 'condor_dir' : 'condor_2014_03_06_IsrSyst',   
##       'dataset' : 'hist_chargino_amsb_mGrav75K_1ns_GEN',   
##       'channel' : 'demo', 
##       'legend_entry' : '#chi, 247 GeV, default',  
##       'marker' : 'circle',
##       'fill' : 'solid',
##       'color' : 'red', 
##           },

## # ~/workdirTemplateDisTrk]$ makeComparisonPlots.py -g -r -l plotCompIsrSyst.py -o condor/condor_2014_03_06_IsrSyst/compareIsr150KStdVsDn.root -b 5
    { 'condor_dir' : 'condor_2014_03_06_IsrSyst',  
      'dataset' : 'hist_charginoIsrDn_amsb_mGrav150K_1ns_GEN',  
      'channel' : 'demo', 
      'legend_entry' : '#chi, 488 GeV, ISR vary down',  
      'marker' : 'triangle',
      'fill' : 'hollow',
      'color' : 'black', 
          },
    { 'condor_dir' : 'condor_2014_03_06_IsrSyst',   
      'dataset' : 'hist_chargino_amsb_mGrav150K_1ns_GEN',   
      'channel' : 'demo', 
      'legend_entry' : '#chi, 488 GeV, default',  
      'marker' : 'circle',
      'fill' : 'solid',
      'color' : 'red', 
          },


    ]



