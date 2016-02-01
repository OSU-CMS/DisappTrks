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
limit_dir = WellsDir+'limits_20160121' # LHC-type full CLs 

masses = ['100', '300', '500', '700']

#chargino tau values
lifetimes = ['10', '100', '1000']



convertCmToNs = True 
makeColorPlot = False 
convertToMassSplitting = False
outputName = "limit_plot.root"

# description of all the plots to be made
plotDefinitions = [
    
    #each entry corresponds to a canvas in the output file
           
    ######################LIFETIME (ns) VS MASS
    {
    # this will be the name of the canvas in the output root file
    'title' : 'lifetimeNs_vs_mass',
    
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
    

        ######################TAU = 0.5 NS

##      {
##                 # this will be the name of the canvas in the output root file
##     'title' : 'limits_vs_0p5ns',

##                 # current options are 'mass' and 'lifetime'
##     'xAxisType' : 'mass',

##                 # xmin, xmax, label
##     'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
##     'yAxisLabel' : '#tau = 0.5 ns',

##                 # optional (scaled automatically if not included)
##                 #'yAxis' : [0.0001,100],

##                 # optional (False if not included)
##                 # currently only works if the x-axis is mass
##     'showTheory' : True,

##                 #define all the curves to include on this canvas
##     'graphs' : [
##                     {
##     'source' : [limit_dir], #output directory from limit running
##     'lifetime' : 0.5,
##     'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'colorScheme' : 'brazilian',
##     'legendEntry' : '',
##     },
##                     ],
##     },
     

##      ######################TAU = 1 NS     
##         {
##             # this will be the name of the canvas in the output root file
##     'title' : 'limits_vs_1ns',

##             # current options are 'mass' and 'lifetime'
## #    'yAxisType' : 'lifetime',
##     'xAxisType' : 'mass',

##             # xmin, xmax, label
##     'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
##     'yAxisLabel' : '#tau = 1 ns',

##             # optional (scaled automatically if not included)
##             #'yAxis' : [0.0001,100],

##             # optional (False if not included)
##             # currently only works if the x-axis is mass
##     'showTheory' : True,

##             #define all the curves to include on this canvas
##     'graphs' : [
##                 {
##     'source' : [limit_dir], #output directory from limit running
##     'lifetime' : 1.0,
##     'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'colorScheme' : 'brazilian',
##     'legendEntry' : '',
##                 },
##                 ],
##     },

##      ###################### CTAU = 15 cm 
##         {
##                 # this will be the name of the canvas in the output root file
##     'title' : 'limits_vs_0p5ns',

##                 # current options are 'mass' and 'lifetime'
##     #    'xAxisType' : 'lifetime',
##     'xAxisType' : 'mass',

##                 # xmin, xmax, label
##     'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
##     'yAxisLabel' : 'c#tau = 15 cm',

##     'theoryLabel' : '#tau_{#chi^{#pm}} = 0.5 ns', 

##                 # optional (scaled automatically if not included)
##                 #'yAxis' : [0.0001,100],

##                 # optional (False if not included)
##                 # currently only works if the x-axis is mass
##     'showTheory' : True,

##                 #define all the curves to include on this canvas
##     'graphs' : [
##                     {
##     'source' : [limit_dir], #output directory from limit running
##     'lifetime' : 15.0,
##     'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'colorScheme' : 'brazilian',
##     'legendEntry' : '',
##                     },
##                                     ],
##         },

##      ###################### CTAU = 30 cm 
##         {
##                 # this will be the name of the canvas in the output root file
##     'title' : 'limits_vs_1ns',

##                 # current options are 'mass' and 'lifetime'
##     #    'xAxisType' : 'lifetime',
##     'xAxisType' : 'mass',

##                 # xmin, xmax, label
##     'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
##     'yAxisLabel' : 'c#tau = 30 cm',

##     'theoryLabel' : '#tau_{#chi^{#pm}} = 1 ns', 

##                 # optional (scaled automatically if not included)
##                 #'yAxis' : [0.0001,100],

##                 # optional (False if not included)
##                 # currently only works if the x-axis is mass
##     'showTheory' : True,

##                 #define all the curves to include on this canvas
##     'graphs' : [
##                     {
##     'source' : [limit_dir], #output directory from limit running
##     'lifetime' : 30.0,
##     'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'colorScheme' : 'brazilian',
##     'legendEntry' : '',
##                     },
##                                     ],
##         },

##      ###################### CTAU = 150 cm 
##         {
##                 # this will be the name of the canvas in the output root file
##     'title' : 'limits_vs_5ns',

##                 # current options are 'mass' and 'lifetime'
##     #    'xAxisType' : 'lifetime',
##     'xAxisType' : 'mass',

##                 # xmin, xmax, label
##     'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
##     'yAxisLabel' : 'c#tau = 150 cm',

##     'theoryLabel' : '#tau_{#chi^{#pm}} = 5 ns', 

##                 # optional (scaled automatically if not included)
##                 #'yAxis' : [0.0001,100],

##                 # optional (False if not included)
##                 # currently only works if the x-axis is mass
##     'showTheory' : True,

##                 #define all the curves to include on this canvas
##     'graphs' : [
##                     {
##     'source' : [limit_dir], #output directory from limit running
##     'lifetime' : 150.0,
##     'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'colorScheme' : 'brazilian',
##     'legendEntry' : '',
##                     },
##                                     ],
##         },


##  ######################LIFETIME (cm) VS MASS
##      {
##      # this will be the name of the canvas in the output root file
##      'title' : 'lifetimeCm_vs_mass',

##       # current options are 'mass' and 'lifetime'
##      'xAxisType' : 'mass',
##      'yAxisType' : 'lifetime',

##      'xAxisLabel' : 'chargino mass [GeV]',
##      'yAxisLabel' : 'chargino #LTc#tau#GT [cm]',
     
##      'showTheory' : True,
##      'graphs' : [
##     {
##     'source' : [limit_dir], #output directory from limit running
##     'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
##     'colorScheme' : 'brazilian',
##     },
##     ],
##      },
     


     
##  ######################LIFETIME (ns) VS MASS
##      {
##      # this will be the name of the canvas in the output root file
##      'title' : 'compareObsBayesianVsAysmptotic',

##       # current options are 'mass' and 'lifetime'
##      'xAxisType' : 'mass',
##      'yAxisType' : 'lifetime',

##      'xAxisLabel' : 'm_{#chi^{#pm}_{1}} [GeV]',
##      'yAxisLabel' : '#tau_{#chi^{#pm}_{1}} [ns]',

##      'xAxisFixMin' : 75, 
##      'xAxisFixMax' : 600,
##      'yAxisFixMin' : 0.05, 
##      'yAxisFixMax' : 15,

## #     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

##      'showTheory' : True,
##      'graphs' : [
##     {
##     'source' : ['limits_2014_02_20NewMCMC'], #output directory from limit running
##     'graphsToInclude' : ['obs'],
##     'colorScheme' : 'red',
##     'legendEntry' : 'Bayesian',
##     },
##     {
##     'source' : ['limits_2014_02_20New'], #output directory from limit running
##     'graphsToInclude' : ['obs'],
##     'colorScheme' : 'blue',
##     'legendEntry' : 'asymptotic CLs',
##     },
##     ],
##      },
     

     
##  ######################LIFETIME (ns) VS MASS
##      {
##      # this will be the name of the canvas in the output root file
##      'title' : 'compareExpBayesianVsAysmptotic',

##       # current options are 'mass' and 'lifetime'
##      'xAxisType' : 'mass',
##      'yAxisType' : 'lifetime',

##      'xAxisLabel' : 'm_{#chi^{#pm}_{1}} [GeV]',
##      'yAxisLabel' : '#tau_{#chi^{#pm}_{1}} [ns]',

##      'xAxisFixMin' : 75, 
##      'xAxisFixMax' : 600,
##      'yAxisFixMin' : 0.05, 
##      'yAxisFixMax' : 15,

## #     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

##      'showTheory' : True,
##      'graphs' : [
##     {
##     'source' : ['limits_2014_02_20NewMCMC'], #output directory from limit running
##     'graphsToInclude' : ['exp'],
##     'colorScheme' : 'red',
##     'legendEntry' : 'Bayesian',
##     },
##     {
##     'source' : ['limits_2014_02_20New'], #output directory from limit running
##     'graphsToInclude' : ['exp'],
##     'colorScheme' : 'blue',
##     'legendEntry' : 'asymptotic CLs',
##     },
##     ],
##      },

##  ######################LIFETIME (ns) VS MASS
##      {
##      # this will be the name of the canvas in the output root file
##      'title' : 'compareTwoSigmaBayesianVsAysmptotic',

##       # current options are 'mass' and 'lifetime'
##      'xAxisType' : 'mass',
##      'yAxisType' : 'lifetime',

##      'xAxisLabel' : 'm_{#chi^{#pm}_{1}} [GeV]',
##      'yAxisLabel' : '#tau_{#chi^{#pm}_{1}} [ns]',

##      'xAxisFixMin' : 75, 
##      'xAxisFixMax' : 600,
##      'yAxisFixMin' : 0.05, 
##      'yAxisFixMax' : 15,

## #     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

##      'showTheory' : True,
##      'graphs' : [
##     {
##     'source' : ['limits_2014_02_20New'], #output directory from limit running
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'graphsToInclude' : ['twoSigma'], 
##     'colorScheme' : 'blue',
##     'legendEntry' : 'asymptotic CLs',
##     },
##     {
##     'source' : ['limits_2014_02_20NewMCMC'], #output directory from limit running
##     'graphsToInclude' : ['twoSigma'],  
##     'colorScheme' : 'red',
##     'legendEntry' : 'Bayesian',
##     },
##     ],
##      },
     
##  ######################LIFETIME (ns) VS MASS
##      {
##      # this will be the name of the canvas in the output root file
##      'title' : 'compareOneSigmaBayesianVsAysmptotic',

##       # current options are 'mass' and 'lifetime'
##      'xAxisType' : 'mass',
##      'yAxisType' : 'lifetime',

##      'xAxisLabel' : 'm_{#chi^{#pm}_{1}} [GeV]',
##      'yAxisLabel' : '#tau_{#chi^{#pm}_{1}} [ns]',

##      'xAxisFixMin' : 75, 
##      'xAxisFixMax' : 600,
##      'yAxisFixMin' : 0.05, 
##      'yAxisFixMax' : 15,

## #     'theoryLabel' : 'tan#beta = 5, #mu > 0', 

##      'showTheory' : True,
##      'graphs' : [
##     {
##     'source' : ['limits_2014_02_20New'], #output directory from limit running
##     'graphsToInclude' : ['oneSigma'], 
##     'colorScheme' : 'blue',
##     'legendEntry' : 'asymptotic CLs',
##     },
##     {
##     'source' : ['limits_2014_02_20NewMCMC'], #output directory from limit running
##     'graphsToInclude' : ['oneSigma'],  
##     'colorScheme' : 'red',
##     'legendEntry' : 'Bayesian',
##     },
##     ],
##      },
     

     ]
