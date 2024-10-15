#!/usr/bin/env python3

from DisappTrks.LimitSetting.limitOptions import *
from DisappTrks.LimitSetting.winoElectroweakLimits import *

from ROOT import TMath

convertCmToNs = True
outputName = "limit_plots.root"
yAxisRangeFor1DMassLimits = [1.e-3, 1.e3]

roundLumiText = True

speedLightCmPerNs = TMath.C () * 1.0e-7
convertToNs = (lambda a : round (a / speedLightCmPerNs, 2))

showObserved = True

theoryComments = ['tan #beta = 5, #mu > 0', 'pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, wino-like #tilde{#chi}_{0}']

# description of all the plots to be made
plotDefinitions = [

    #each entry corresponds to a canvas in the output file

    ######################LIFETIME (ns) VS MASS
    {
        # this will be the name of the canvas in the output root file
        'title' : 'lifetime_vs_mass',

        'convertToMassSplitting' : False,
        'makeColorPlot' : False,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : '#tau_{#tilde{#chi}^{#pm}_{1}} [ns]',

        'xAxisFixMin' : 100,
        'xAxisFixMax' : 1250,
        #'yAxisFixMin' : 0.1 / TMath.C() / 1e-7,
        'yAxisFixMin' : 2e-2, # lowest that looks good
        'yAxisFixMax' : 10000.0 / TMath.C() / 1e-7,

        'theoryLabel' : theoryComments,
        #'theoryHeader' : 'pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{1,2}, higgsino-like #tilde{#chi}_{0}',

        'graphs' : [
            {
                'graphsToInclude' : ['twoSigma','oneSigma','exp'] + (['obs'] if showObserved else []),
                'colorScheme' : 'brazilian',
            },
        ],
    },

    ###################### CTAU = 10 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_10cm',

        'convertToMassSplitting' : False,
        'makeColorPlot' : False,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 10 cm',

        'theoryLabel' : [
            'c#tau_{#tilde{#chi}^{#pm}_{1}} = 10 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = ' + str (convertToNs (10.0)) + ' ns)',
            'pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, wino-like #tilde{#chi}_{0}',
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
                'graphsToInclude' : ['twoSigma','oneSigma','exp'] + (['obs'] if showObserved else []),
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 100 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_100cm',

        'convertToMassSplitting' : False,
        'makeColorPlot' : False,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 100 cm',


        'theoryLabel' : [
            'c#tau_{#tilde{#chi}^{#pm}_{1}} = 100 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = ' + str (convertToNs (100.0)) + ' ns)',
            'pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, wino-like #tilde{#chi}_{0}',
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
                'graphsToInclude' : ['twoSigma','oneSigma','exp'] + (['obs'] if showObserved else []),
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 1000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_1000cm',

        'convertToMassSplitting' : False,
        'makeColorPlot' : False,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 1000 cm',

        'theoryLabel' : [
            'c#tau_{#tilde{#chi}^{#pm}_{1}} = 1000 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = ' + str (convertToNs (1000.0)) + ' ns)',
            'pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, wino-like #tilde{#chi}_{0}',
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
                'graphsToInclude' : ['twoSigma','oneSigma','exp'] + (['obs'] if showObserved else []),
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ###################### CTAU = 10000 cm
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_10000cm',

        'convertToMassSplitting' : False,
        'makeColorPlot' : False,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : 'c#tau = 10000 cm',

        'theoryLabel' : [
            'c#tau_{#tilde{#chi}^{#pm}_{1}} = 10000 cm (#tau_{#tilde{#chi}^{#pm}_{1}} = ' + str (convertToNs (10000.0)) + ' ns)',
            'pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{#mp}_{1}, wino-like #tilde{#chi}_{0}',
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
                'graphsToInclude' : ['twoSigma','oneSigma','exp'] + (['obs'] if showObserved else []),
                'colorScheme' : 'brazilian',
                'legendEntry' : '',
            },
        ],
    },

    ######################LIFETIME (ns) VS MASS
    # "3D" plot
    {
        # this will be the name of the canvas in the output root file
        'title' : 'lifetimeNs_vs_mass_color',

        'convertToMassSplitting' : False,
        'makeColorPlot' : True,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : '#tau_{#tilde{#chi}^{#pm}_{1}} [ns]',
        'zAxisLabel' : '95% CL upper limit on #sigma #bf{#it{#Beta}} [pb]',
        #'zAxisFixMin' : 0.005,
        'zAxisFixMax' : 5,

        'fillPotHoles' : True,

        #'extraDrawOptions' : "text",

         #'theoryLabel' : 'tan#beta = 5, #mu > 0',

        'th2fs' : {
            'th2fsToInclude' : ['exp'] + (['obs'] if showObserved else []),
        },
    },

    # only plotted if option "--plotSignificance"
    {
        'title' : 'significance_vs_mass_color',

        'convertToMassSplitting' : False,
        'makeColorPlot' : True,

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        'xAxisLabel' : 'm_{#tilde{#chi}^{#pm}_{1}} [GeV]',
        'yAxisLabel' : '#tau_{#tilde{#chi}^{#pm}_{1}} [ns]',
        'zAxisLabel' : 'significance p-value',
        #'zAxisFixMin' : 0.005,
        'zAxisFixMax' : 1,

        'fillPotHoles' : True,

        #'extraDrawOptions' : "text",

         #'theoryLabel' : 'tan#beta = 5, #mu > 0',

        'th2fs' : {
            'th2fsToInclude' : ['exp'] + (['obs'] if showObserved else []),
        },
    }

]
