#!/usr/bin/env python

# Local options file to be used with makeLimitPlots.py
# Usage:
# > makeLimitPlots.py -l amsbLimitPlotConfigNew.py -c limitDir
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *

##################################
### Event Selection Parameters ###
##################################

intLumi = lumi["MET_2015"] + lumi["MET_2016"]

#########################
### Signal Parameters ###
#########################

#NOTE: These are the chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700']

#chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

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
        'yAxisFixMin' : 0.01,
        'yAxisFixMax' : 1000,  # The last point is 10000cm = 333 ns

        'theoryLabel' : 'tan #beta = 5, #mu > 0',

        'graphs' : [
            {
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
                'lifetime' : 10.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
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
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
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
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 2000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_2000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 2000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 2000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 2000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 3000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_3000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 3000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 3000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 3000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 4000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_4000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 4000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 4000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 4000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 5000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_5000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 5000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 5000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 5000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 6000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_6000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 6000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 6000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 6000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 7000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_7000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 7000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 7000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 7000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 8000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_8000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 8000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 8000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 8000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 9000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_9000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 9000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 9000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 9000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 10000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_10000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
        'yAxisLabel' : 'c#tau = 10000 cm',

        'theoryLabel' : '#tau_{#chi^{#pm}} = 10000 cm',

        # optional (scaled automatically if not included)
        'yAxis' : yAxisRangeFor1DMassLimits,

        # optional (False if not included)
        # currently only works if the x-axis is mass
        'showTheory' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'lifetime' : 10000.0,
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },
]
