#!/usr/bin/env python

# Usage:
# > makeLimitPlots.py -l amsbLimitPlotConfig3D.py -c limitDir 



##################################
### Event Selection Parameters ###
##################################

from amsbLimitPlotConfigNew import *
# Keep most settings the same

lifetimes.remove('1')

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

     'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
     'yAxisLabel' : '#tau_{#tilde{#chi}^{#pm}_{1}} [ns]',
     'zAxisLabel' : '95% CL upper limit on cross section [pb]', 
     'xAxisFixMin' : 50, 
     'xAxisFixMax' : 650,
     'yAxisFixMin' : 0.07, 
     'yAxisFixMax' : 300,
     'zAxisFixMin' : 0.015, 
     'zAxisFixMax' : 10,
     
     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

     'th2fs' : {
    'source' : [limit_dir],
    'th2fsToInclude' : ['obs'],
    }, 
     },
     
     ]
