#!/usr/bin/env python


dataset = 'AMSB_chargino_MASSGeV_RewtCtauLIFETIMEcm'

#masses = [500]
masses = [100, 200, 300, 400, 500, 600]
#lifetimes = [10, 100, 200, 400, 600, 800, 1000]  
lifetimes = [10, 100, 1000]  
#lifetimes = [10, 20, 40, 60, 80, 100, 200, 400, 600, 800, 1000]

input_sources = [

## ~/workdirTemplateDisTrk]$ makeSigEffPlot.py -r -l plotSigEffModelIndep.py  -o condor/condor_2014_08_27_NoCutsFilterMCTrack/sigEffComparison.root
## ~/workdirTemplateDisTrk]$ makeSigEffPlot.py -r -l plotSigEffModelIndep.py  -o condor/condor_2014_09_02_NoCutsFilterMCTrack/sigEffComparison.root  -x signalCrossSecs.py  
     { 'condor_dir' : 'condor_2014_09_02_NoCutsFilterMCTrack',  
#     { 'condor_dir' : 'condor_2014_08_27_NoCutsFilterMCTrack', 
       'channel' : 'NoCutsFilterMCTrack', 
       'legend_entry' : 'fast technique', 
       'marker' : 'star',
       'fill' : 'solid',
       'color' : 'blue', 
           },
#     { 'condor_dir' : 'condor_2014_08_20_FullSelectionFilterMCTrack', 
#       'channel' : 'FullSelectionFilterMCTrack', 
     { 'condor_dir' : 'JessCondor/fullSelectionAllSigBothTrig_24July', 
       'channel' : 'FullSelection',
       'legend_entry' : 'full simulation',   
       'marker' : 'circSmall',
       'color' : 'red', 
           },


## ## ~/workdirTemplateDisTrk]$ makeSigEffPlot.py -r -l plotSigEffModelIndep.py  -o condor/condor_2014_09_01_NoCutsFilterMCTrackBasicSelOnly/sigEffComparison.root -x signalCrossSecs.py  
## #     { 'condor_dir' : 'condor_2014_08_28_NoCutsFilterMCTrackBasicSelOnly',  
##      { 'condor_dir' : 'condor_2014_09_01_NoCutsFilterMCTrackBasicSelOnly',  
##        'channel' : 'NoCutsFilterMCTrack', 
##        'legend_entry' : 'fast technique', 
##        'marker' : 'star',
##        'fill' : 'solid',
##        'color' : 'blue', 
##            },
## #     { 'condor_dir' : 'condor_2014_01_25_MetJetSkim', 
##      { 'condor_dir' : 'condor_2014_08_28_MetJet',   
##        'channel' : 'MetJet', 
##        'legend_entry' : 'full simulation',   
##        'marker' : 'circSmall',
##        'color' : 'red', 
##        },

     ]



