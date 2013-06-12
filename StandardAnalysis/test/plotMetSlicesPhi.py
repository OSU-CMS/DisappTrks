#!/usr/bin/env python
# Plot of the distribution of MET, for different cuts on the phi

mydataset = 'SingleMu' 
#mydataset = 'Wjets'  
myChannel = 'WToMuSimple'
myCondorDir = 'condor_2013_06_04_AODCtrlMuonNewTrig' 

input_histograms = [
    { 'condor_dir' : myCondorDir,
      'dataset' : mydataset, 
      'channel' : myChannel,
      'name' : 'mets_pt_metPhiLo',  
      'legend_entry' : '|#phi|<1.0',
      'color' : 2,
                },
    { 'condor_dir' : myCondorDir,
      'dataset' : mydataset, 
      'channel' : myChannel,
      'name' : 'mets_pt_metPhiMed',  
      'legend_entry' : '1.0<|#phi|<2.0',
      'color' : 4,
                },
    { 'condor_dir' : myCondorDir,
      'dataset' : mydataset, 
      'channel' : myChannel,
      'name' : 'mets_pt_metPhiHi',  
      'legend_entry' : '|#phi|>2.0',
      'color' : 1,
                },
    ]



