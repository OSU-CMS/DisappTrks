#!/usr/bin/env python

# Local options file to be used with makeLimitPlots.py 
# Usage:
# > makeLimitPlots.py -l amsbLimitPlotConfigNew.py -c limitDir 
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *

##################################
### Event Selection Parameters ###
##################################

from amsbLimitPlotConfigNew import *
# Keep most settings the same

masses = ['100', '200', '300', '400', '500']
lifetimes = ['2','3','4','5','6','7','8', '9', '10','20','30','40','50','70','80','90','100','200','300','400','500','600','700','800','900','1000','2000','3000','4000','5000','6000','8000','9000','10000']


outputName = "limit_plotCol.root"

makeColorPlot = True

# description of all the plots to be made
plotDefinitions = [

    #each entry corresponds to a canvas in the output file    
    
    ######################LIFETIME (ns) VS MASS
     {
     # this will be the name of the canvas in the output root file
     'title' : 'lifetimeNs_vs_mass_color',

      # current options are 'mass' and 'lifetime'
     'xAxisType' : 'mass',
     'yAxisType' : 'lifetime',

     'xAxisLabel' : 'm_{#chi^{#pm}_{1}} [GeV]',
     'yAxisLabel' : '#tau_{#chi^{#pm}_{1}} [ns]',
     'xAxisFixMin' : 100, 
     'xAxisFixMax' : 600,
     'yAxisFixMin' : 300, 
     'yAxisFixMax' : 0.07,
     


     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

     'showTheory' : True,

     'th2fs' : [
                {
    'source' : [limit_dir],
    'br'   : 100,
#    'th2fsToInclude' : ['exp','obs'],
    'th2fsToInclude' : ['obs'],
                },
                        ], 
     'graphs' : [
    {
    'source' : [limit_dir], #output directory from limit running
    'graphsToInclude' : ['plusOneSigma'],  # Needed to prevent some kind of error
    'colorScheme' : 'brazilian',
    },
    ],
     },


     ]
