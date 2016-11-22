#!/usr/bin/env python

# Local options file to be used with makeLimitPlots.py 
# Usage:
# > makeLimitPlots.py -l amsbLimitPlotConfig1DShort.py -c limitDir 
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *

##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
#integrateHistogramName = "numEvents"
intLumi = 19500

#########################
### Signal Parameters ###
#########################


from amsbLimitPlotConfigNew import *
# Keep most settings the same

convertCmToNs = False
outputName = "limit_plot1DShort.root"


# description of all the plots to be made
plotDefinitions = [
    
##     #each entry corresponds to a canvas in the output file

     ######################
        {
    'title' : 'limits_1D90',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 90 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 90,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ]
