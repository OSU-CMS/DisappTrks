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
outputName = "limit_plot1D.root"

# description of all the plots to be made
plotDefinitions = [

##     #each entry corresponds to a canvas in the output file


     ######################
        {
    'title' : 'limits_1D10000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 10000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 10000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D9000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 9000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 9000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D8000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 8000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 8000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D7000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 7000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 7000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D6000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 6000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 6000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D5000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 5000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 5000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D4000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 4000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 4000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D3000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 3000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 3000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D2000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 2000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 2000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D1000',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 1000 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 1000,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D900',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 900 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 900,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D800',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 800 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 800,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D700',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 700 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 700,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D600',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 600 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 600,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D500',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 500 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 500,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D400',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 400 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 400,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D300',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 300 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 300,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D200',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 200 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 200,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },


     ######################
        {
    'title' : 'limits_1D100',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 100 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 100,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

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

     ######################
        {
    'title' : 'limits_1D80',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 80 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 80,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D70',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 70 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 70,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D60',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 60 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 60,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D50',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 50 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 50,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D40',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 40 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 40,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D30',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 30 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 30,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D20',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 20 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 20,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D10',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 10 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 10,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D9',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 9 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 9,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D8',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 8 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 8,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D7',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 7 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 7,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D6',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 6 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 6,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D5',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 5 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 5,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D4',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 4 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 4,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D3',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 3 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 3,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D2',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 2 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 2,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },

     ######################
        {
    'title' : 'limits_1D1',
    'xAxisType' : 'mass',
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '  #tau = 1 cm',
    'showTheory' : True,
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 1,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
    'colorScheme' : 'blue',
    'legendEntry' : '',
    },
                ],
    },



     ]
