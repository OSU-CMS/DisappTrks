#!/usr/bin/env python
#
# Usage:
# ~/workdir76]$ makeEfficiencyPlots.py -b 2 -p -l plotEffElecVeto.py -o condor/ZtoEleDisTrk/eff_elecVeto.root 

cutName  = 'electron veto' 

input_sources = [

    { 'condor_dir'     : 'ZtoEleDisTrk', 
      'condor_dir_den' : 'ZtoEleProbeTrkWithZCuts', 
      'dataset' : 'allBkgd', 
      'num_channel' : 'ZtoEleDisTrk', 
      'den_channel' : 'ZtoEleProbeTrkWithZCuts', 
      'legend_entry' : 'all MC', 
      'marker' : 'square',
      'fill' : 'hollow',
      'color' : 'red', 
          },

    { 'condor_dir'     : 'ZtoEleDisTrk', 
      'condor_dir_den' : 'ZtoEleProbeTrkWithZCuts', 
      'dataset' : 'SingleEle_2015D', 
      'num_channel' : 'ZtoEleDisTrk', 
      'den_channel' : 'ZtoEleProbeTrkWithZCuts', 
      'legend_entry' : 'data', 
      'marker' : 'circle',
      'fill' : 'solid',
      'color' : 'black', 
          },

    ]



