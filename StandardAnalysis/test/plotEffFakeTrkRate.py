#!/usr/bin/env python
#
# Usage:
# ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 8 --ylog --ymin=1.0e-8 --ymax=1.0 -p -l plotEffFakeTrkRate.py -o condor/condor_2013_12_15_FakeTrkBkgd/eff_histograms.root 

cutName  = 'fake track rate' 

input_sources = [


#    { 'condor_dir' : 'condor_2013_11_20_FullSelectionFakeTrkRate', 
    { 'condor_dir' : 'condor_2013_12_15_FakeTrkBkgd',   
      'dataset' : 'Background',
      'num_channel' : 'FullSelectionNoMetFakeTrk',  
      'den_channel' : 'FullSelectionNoMetNoTrkCuts', 
      'legend_entry' : 'Total Bkgd MC',  
      'marker' : 'square',
      'fill' : 'solid',
      'color' : 'red', 
          },



    ]



