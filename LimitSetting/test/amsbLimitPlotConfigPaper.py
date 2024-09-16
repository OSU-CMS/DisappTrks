#!/usr/bin/env python3

# Local options file to be used with makeLimitPlots.py
# Usage:
# > makeLimitPlots.py -l amsbLimitPlotConfigNew.py -c limitDir
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

import os

if not (os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_")):
    exec("from DisappTrks.SignalMC.signalCrossSecs import *")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    exec("from DisappTrks.SignalMC.signalCrossSecs13p6TeV import *")
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *

from ROOT import TMath

##################################
### Event Selection Parameters ###
##################################

intLumi = lumi["MET_2015"] + lumi["MET_2016"]

#########################
### Signal Parameters ###
#########################

#NOTE: These are the chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700', '800', '900']

#chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

convertCmToNs = True
makeColorPlot = False
convertToMassSplitting = False
outputName = "limit_plot.root"
#yAxisRangeFor1DMassLimits = [0.01, 10000]
yAxisRangeFor1DMassLimits = [5.0e-3, 2.0e3]

speedLightCmPerNs = TMath.C () * 1.0e-7
convertToNs = (lambda a : round (a / speedLightCmPerNs, 2))

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
        'xAxisFixMax' : 900,
        'yAxisFixMin' : 0.067,
        'yAxisFixMax' : 333,  # The last point is 10000cm = 333 ns

        'theoryLabel' : [
            'tan #beta = 5, #mu > 0',
            "#bf{#it{#Beta}} (#tilde{#chi}^{#pm}_{1} #rightarrow #tilde{#chi}^{0}_{1} #pi^{#pm}) = 100%",
        ],

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
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 10 cm',

        'theoryLabel' : [
            'tan #beta = 5, #mu > 0',
            "#bf{#it{#Beta}} (#tilde{#chi}^{#pm}_{1} #rightarrow #tilde{#chi}^{0}_{1} #pi^{#pm}) = 100%",
            '#tau_{#tilde{#chi}^{#pm}_{1}} = 10 cm/c (' + str (convertToNs (10.0)) + ' ns)',
        ],

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
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 100 cm',

        'theoryLabel' : [
            'tan #beta = 5, #mu > 0',
            "#bf{#it{#Beta}} (#tilde{#chi}^{#pm}_{1} #rightarrow #tilde{#chi}^{0}_{1} #pi^{#pm}) = 100%",
            '#tau_{#tilde{#chi}^{#pm}_{1}} = 100 cm/c (' + str (convertToNs (100.0)) + ' ns)',
        ],

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
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 1000 cm',

        'theoryLabel' : [
            'tan #beta = 5, #mu > 0',
            "#bf{#it{#Beta}} (#tilde{#chi}^{#pm}_{1} #rightarrow #tilde{#chi}^{0}_{1} #pi^{#pm}) = 100%",
            '#tau_{#tilde{#chi}^{#pm}_{1}} = 1000 cm/c (' + str (convertToNs (1000.0)) + ' ns)',
        ],

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

    ###################### CTAU = 10000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_10000cm',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 10000 cm',

        'theoryLabel' : [
            'tan #beta = 5, #mu > 0',
            "#bf{#it{#Beta}} (#tilde{#chi}^{#pm}_{1} #rightarrow #tilde{#chi}^{0}_{1} #pi^{#pm}) = 100%",
            '#tau_{#tilde{#chi}^{#pm}_{1}} = 10000 cm/c (' + str (convertToNs (10000.0)) + ' ns)',
        ],

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
