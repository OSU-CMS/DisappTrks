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
masses = ['100', '200', '300', '400', '500', '600', '700', '800', '900']

#chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

convertCmToNs = True
makeColorPlot = True
convertToMassSplitting = False
outputName = "limit_plotCol.root"
yAxisRangeFor1DMassLimits = [0.01, 10000]

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
     'zAxisLabel' : '95% CL upper limit on #sigma #bf{#it{#Beta}} [pb]',
     'zAxisFixMin' : 0.005,
     'zAxisFixMax' : 1000,

     'fillPotHoles' : True,

     #'extraDrawOptions' : "text",

     #'theoryLabel' : 'tan#beta = 5, #mu > 0',

     'th2fs' : {
        'th2fsToInclude' : ['obs', 'exp'],
      },
    },
]
