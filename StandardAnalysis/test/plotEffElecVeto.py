#!/usr/bin/env python
#
# Usage:
# ~/workdir76]$ makeEfficiencyPlots.py -b 8 --ylog --ymin=1.0e-8 --ymax=1.0 -p -l plotEffElecVeto.py -o condor/condor_2013_12_15_FakeTrkBkgd/eff_histograms.root 
# ~/workdir76]$ makeEfficiencyPlots.py -b 8 -p -l plotEffElecVeto.py -o condor/ElecBkgdClosureTestWjets/eff_elecVeto.root 

cutName  = 'electron veto' 

input_sources = [

    { 'condor_dir' : 'ElecBkgdClosureTestWjets', 
      'condor_dir_den' : 'ElectronTagPt35',  
      'dataset' : 'WJetsToLNu', 
      'num_channel' : 'CandTrkIdElecPt35NoMet', 
      'den_channel' : 'ElectronTagPt35', 
      'legend_entry' : 'W+jets MC', 
      'marker' : 'square',
      'fill' : 'solid',
      'color' : 'red', 
          },

    { 'condor_dir' : 'ElecBkgdClosureTestWjets', 
      'condor_dir_den' : 'ElectronTagPt35',  
      'dataset' : 'TTJets', 
      'num_channel' : 'CandTrkIdElecPt35NoMet', 
      'den_channel' : 'ElectronTagPt35', 
      'legend_entry' : 'TTJets', 
      'marker' : 'circle',
      'fill' : 'solid',
      'color' : 'blue', 
          },

    ]



