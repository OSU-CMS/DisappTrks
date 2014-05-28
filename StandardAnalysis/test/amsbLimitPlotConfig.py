
#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -R -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py


##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
#integrateHistogramName = "numEvents"
intLumi = 19500

#########################
### Signal Parameters ###
#########################

# NOTE: The chargino masses are used when actually making the limit plots
masses = ['103', '164', '247', '328','408',  '488']
#limit_dir = 'limits_8May'
limit_dir = 'limits_2014_02_20Gamma'  

#chargino tau values
lifetimes = ['0.5', '1.0', '5.0']

signal_cross_sections = { # in pb 
   '103' : {
         'value' : '15.9',
          'error' : '1.1', # dummy 10% error
         },
    '164' : {
         'value' : '2.73',
          'error' : '1.07',
         },

    '247' : {
         'value' : '0.478',
         'error' : '1.05',
         },
    '328' : {
         'value' : '0.185',
         'error' : '1.05',
         },
   '408' : {
         'value' : '0.052',
         'error' : '1.05',
         },
   
    '488' : {
         'value' : '0.0221',
         'error' : '1.05',
         }, 
    }



# description of all the plots to be made
plotDefinitions = [

        #each entry corresponds to a canvas in the output file

        ######################TAU = 0.5 NS

     {
                # this will be the name of the canvas in the output root file
    'title' : 'limits_vs_0p5ns',

                # current options are 'mass' and 'lifetime'
    'xAxisType' : 'mass',

                # xmin, xmax, label
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '#tau = 0.5 ns',

                # optional (scaled automatically if not included)
                #'yAxis' : [0.0001,100],

                # optional (False if not included)
                # currently only works if the x-axis is mass
    'showTheory' : True,

                #define all the curves to include on this canvas
    'graphs' : [
                    {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 0.5,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
#    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
    'colorScheme' : 'brazilian',
    'legendEntry' : '',
    },
                    ],
    },
     

     ######################TAU = 1 NS     
        {
            # this will be the name of the canvas in the output root file
    'title' : 'limits_vs_1ns',

            # current options are 'mass' and 'lifetime'
#    'yAxisType' : 'lifetime',
    'xAxisType' : 'mass',

            # xmin, xmax, label
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '#tau = 1 ns',

            # optional (scaled automatically if not included)
            #'yAxis' : [0.0001,100],

            # optional (False if not included)
            # currently only works if the x-axis is mass
    'showTheory' : True,

            #define all the curves to include on this canvas
    'graphs' : [
                {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 1.0,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
#    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
    'colorScheme' : 'brazilian',
    'legendEntry' : '',
                },
                ],
    },

     ######################TAU = 5 NS     
        {
                # this will be the name of the canvas in the output root file
    'title' : 'limits_vs_5ns',

                # current options are 'mass' and 'lifetime'
    #    'xAxisType' : 'lifetime',
    'xAxisType' : 'mass',

                # xmin, xmax, label
    'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
    'yAxisLabel' : '#tau = 5 ns',

                # optional (scaled automatically if not included)
                #'yAxis' : [0.0001,100],

                # optional (False if not included)
                # currently only works if the x-axis is mass
    'showTheory' : True,

                #define all the curves to include on this canvas
    'graphs' : [
                    {
    'source' : [limit_dir], #output directory from limit running
    'lifetime' : 5.0,
    'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
#    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
    'colorScheme' : 'brazilian',
    'legendEntry' : '',
                    },
                                    ],
        },


 ######################LIFETIME VS MAS
     {
     # this will be the name of the canvas in the output root file
     'title' : 'limits_vs_mass',

      # current options are 'mass' and 'lifetime'
     'xAxisType' : 'mass',
     'yAxisType' : 'lifetime',

     'xAxisLabel' : 'chargino mass [GeV]',
     'yAxisLabel' : 'chargino #LT#tau#GT [ns]',
     
    'showTheory' : True,
     'graphs' : [
    {
    'source' : [limit_dir], #output directory from limit running
    'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
    'colorScheme' : 'brazilian',
#    'legendEntry' : '',
    },
    ],
     },

     
        ]
