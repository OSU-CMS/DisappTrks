#!/usr/bin/env python
#
# Usage:

# ~/workdir76]$ makeEfficiencyPlots.py -b 4 -p -l plotEffMuonVeto.py -o condor/ZtoMuDisTrk/eff_muonTightVeto.root 

cutName  = 'tight muon veto' 

input_sources = [

    { 'condor_dir'     : 'ZtoMuDisTrk', 
      'condor_dir_den' : 'ZtoMuProbeTrkWithZCuts', 
      'dataset' : 'allBkgd', 
      'num_channel' : 'ZtoMuProbeTrkTightVeto', 
      'den_channel' : 'ZtoMuProbeTrkWithZCuts', 
      'legend_entry' : 'all MC', 
      'marker' : 'square',
      'fill' : 'hollow',
      'color' : 'red', 
          },

    { 'condor_dir'     : 'ZtoMuDisTrk', 
      'condor_dir_den' : 'ZtoMuProbeTrkWithZCuts', 
      'dataset' : 'SingleMu_2015D', 
      'num_channel' : 'ZtoMuProbeTrkTightVeto', 
      'den_channel' : 'ZtoMuProbeTrkWithZCuts', 
      'legend_entry' : 'data', 
      'marker' : 'circle',
      'fill' : 'solid',
      'color' : 'black', 
          },

    ]



