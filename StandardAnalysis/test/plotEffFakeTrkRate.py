#!/usr/bin/env python
#
# Usage:
# ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 4 -l plotEffFakeTrkRate.py  -o condor/condor_2013_11_20_FullSelectionFakeTrkRate/eff_histograms.root  

cutName  = 'fake track rate' 

input_sources = [


#    { 'condor_dir' : 'condor_2013_11_20_FullSelectionFakeTrkRate', 
    { 'condor_dir' : 'condor_2013_12_15_FakeTrkBkgd',   
      'dataset' : 'Background',
      'num_channel' : 'FullSelectionFakeTrk', 
      'den_channel' : 'FullSelectionNoTrkCuts', 
      'legend_entry' : 'Bkgd Sum',  
      'marker' : 'square',
      'fill' : 'solid',
      'color' : 'red', 
          },



    ]



