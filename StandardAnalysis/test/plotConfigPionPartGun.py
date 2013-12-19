#!/usr/bin/env python

# Config file to make plots from tau particle gun study.
#
# Usage:
# /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test > makeComparisonPlots.py -f -g -l plotConfigPionPartGun.py -o condor/JessTauStudy/comparison_PionPartGun.root 

input_sources = [
    { 'condor_dir' : 'JessTauStudy',
      'dataset' : 'PionPartGunPt30',
      'channel' : 'demo',
      'legend_entry' : "#pi gun, p_{T}=30 GeV, 5 hits", 
      ## 'marker' : 'triangle',
      'fill' : 'solid', 
      'color' : 'black',  
    },
]


## input_sources = [
##     { 'condor_dir' : 'JessTauStudy',
##       'dataset' : 'PionPartGunPt30SixHit',
##       'channel' : 'demo',
##       'legend_entry' : "#pi gun, p_{T}=30 GeV, 6 hits", 
##       ## 'marker' : 'circle',
##       'fill' : 'solid',
##       'color' : 'black',     
##     },
## ]


