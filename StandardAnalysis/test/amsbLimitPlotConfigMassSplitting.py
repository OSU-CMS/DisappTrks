#!/usr/bin/env python

# Local options file to be used with makeLimitPlots.py 
# Usage:
# > makeLimitPlots.py -l amsbLimitPlotConfigMassSplitting.py -c limitDir 

from amsbLimitPlotConfigNew import * 
# Keep most settings the same

convertCmToNs = False
convertToMassSplitting = True
outputName = "limit_plotMassSplitting.root"


lifetimes = ['2','3','4','6','7','8','9','10','20','30','40','50','70','100']  


# description of all the plots to be made
plotDefinitions = [

        #each entry corresponds to a canvas in the output file
     
 ######################LIFETIME (ns) VS MASS
     {
     # this will be the name of the canvas in the output root file
     'title' : 'massSplit_vs_mass',

      # current options are 'mass' and 'lifetime'
     'xAxisType' : 'mass',
     'yAxisType' : 'lifetime',

     'xAxisLabel' : 'm_{#chi^{#pm}_{1}} [GeV]',
     'yAxisLabel' : '#Delta m_{#chi_{1}} [MeV]',

     'xAxisFixMin' : 100, 
     'xAxisFixMax' : 600,
     'yAxisFixMin' : 140, 
     'yAxisFixMax' : 220,

     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

     'showTheory' : True,
     'drawTheoryCurve' : True, 
     
     'graphs' : [
    {
    'source' : [limit_dir], #output directory from limit running
    'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
    'colorScheme' : 'brazilian',
    },
    ],
     },
    
     ]
