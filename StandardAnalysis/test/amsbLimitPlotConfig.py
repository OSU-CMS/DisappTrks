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

#name of histogram to integrate to get yields
#integrateHistogramName = "numEvents"
intLumi = 6919.2


#########################
### Signal Parameters ###
#########################


import os

cwd = os.getcwd()

if "wulsin" in cwd:
    WellsDir = ""
    AndrewDir = "AndrewCondor/"
elif "hart" in cwd:
    WellsDir = "WellsCondorNew/"
    AndrewDir = ""
else:
    print "Error:  could not identify user as wulsin or hart."
    os.exit(0)
    
#NOTE: These are the chargino masses
masses = ['100', '200', '300', '400', '500', '600', '700']

#chargino tau values
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000']

convertCmToNs = True 
makeColorPlot = False 
convertToMassSplitting = False
outputName = "limit_plot.root"
yAxisRangeFor1DMassLimits = [0.01, 10000]  


# description of all the plots to be made
plotDefinitions = [
    
    #each entry corresponds to a canvas in the output file
    
    ######################LIFETIME (ns) VS MASS
    {
        # this will be the name of the canvas in the output root file
        'title' : 'lifetime_vs_mass',
        
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',
        
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : '#tau_{#tilde{#chi}^{#pm}_{1}} [ns]',
        
        'xAxisFixMin' : 100, 
        'xAxisFixMax' : 1000,
        'yAxisFixMin' : 0.2, 
        'yAxisFixMax' : 1000,  # The last point is 10000cm = 333 ns   
        
        'theoryLabel' : 'tan #beta = 5, #mu > 0', 
        
        'graphs' : [
            {
                'graphsToInclude' : ['twoSigma','oneSigma','exp'],
                'colorScheme' : 'brazilian',
            },
        ],
    },
    

    ###################### CTAU = 10 cm 
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_10cm',
        
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        
        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 10 cm',
        
        'theoryLabel' : '#tau_{#chi^{#pm}} = 10 cm', 
        
        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits, 
        
        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,
        
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 10.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },
    
    ###################### CTAU = 100 cm 
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_100cm',
        
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        
        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 100 cm',
        
        'theoryLabel' : '#tau_{#chi^{#pm}} = 100 cm', 
        
        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,  
        
        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,
        
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 100.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 1000 cm 
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_1000cm',
        
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        
        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 1000 cm',
        
        'theoryLabel' : '#tau_{#chi^{#pm}} = 1000 cm', 
        
        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits, 
        
        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,
        
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 1000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },
        
]


