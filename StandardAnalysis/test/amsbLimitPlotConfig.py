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
intLumi = 2457  

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
    
# NOTE: The chargino masses are used when actually making the limit plots
#limit_dir = AndrewDir+'limits_20151201'  # LHC-type full CLs
limit_dir = WellsDir+'limits_20160331'  # LHC-type full CLs 

masses = ['100', '300', '500', '700']

#chargino tau values
lifetimes = ['10', '100', '1000']



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
        'xAxisFixMax' : 600,
        'yAxisFixMin' : 0.05, 
        'yAxisFixMax' : 300,  # The last point is 10000cm = 333 ns   
        
        'theoryLabel' : 'tan #beta = 5, #mu > 0', 
        
        'graphs' : [
            {
                'source' : [limit_dir], #output directory from limit running
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
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
                'source' : [limit_dir], #output directory from limit running
                'lifetime' : 10.0,
                'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
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
                'source' : [limit_dir], #output directory from limit running
                'lifetime' : 100.0,
                'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
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
                'source' : [limit_dir], #output directory from limit running
                'lifetime' : 1000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },
        
]


