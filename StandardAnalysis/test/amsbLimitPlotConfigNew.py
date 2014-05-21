
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
#limit_dir = 'limits_8May'
limit_dir = 'limits_2014_02_20New'  

#masses = ['100', '200', '300', '400', '500', '600']
masses = ['200', '300', '400', '500', '600']

#chargino tau values
lifetimes = ['1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']
#lifetimes = ['1','2','3','4','5','6','7','8','9','10','30','40','50','60','70','80','90','100','200','400','500','600','700','800','900','1000']
#lifetimes = ['10','20']  



signal_cross_sections = { # in pb, in terms of chargino mass
    # Should match values in registerSigMCT3.src!
    '100' : {
    'value' : '16.65',
    'error' : '1.10',
    },
    '200' : {
    'value' : '1.165',
    'error' : '1.10',
            },
    '300' : {
    'value' : '0.2147',
    'error' : '1.10',
            },
    '400' : {
    'value' : '0.0575',
    'error' : '1.10',
            },
    '500' : {
    'value' : '0.01817',
    'error' : '1.10',
            },
    '600' : {
    'value' : '0.00685',
    'error' : '1.10',
            },
            }



# description of all the plots to be made
plotDefinitions = [

        #each entry corresponds to a canvas in the output file

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

##      ######################TAU = 5 NS     
##         {
##                 # this will be the name of the canvas in the output root file
##     'title' : 'limits_vs_5ns',

##                 # current options are 'mass' and 'lifetime'
##     #    'xAxisType' : 'lifetime',
##     'xAxisType' : 'mass',

##                 # xmin, xmax, label
##     'xAxisLabel' : '  M_{#chi^{#pm}} [GeV]',
##     'yAxisLabel' : '#tau = 5 ns',

##                 # optional (scaled automatically if not included)
##                 #'yAxis' : [0.0001,100],

##                 # optional (False if not included)
##                 # currently only works if the x-axis is mass
##     'showTheory' : True,

##                 #define all the curves to include on this canvas
##     'graphs' : [
##                     {
##     'source' : [limit_dir], #output directory from limit running
##     'lifetime' : 5.0,
##     'graphsToInclude' : ['twoSigma','oneSigma','obs','exp'],
## #    'graphsToInclude' : ['twoSigma','oneSigma','exp'],
##     'colorScheme' : 'brazilian',
##     'legendEntry' : '',
##                     },
##                                     ],
##         },


 ######################LIFETIME VS MAS
     {
     # this will be the name of the canvas in the output root file
     'title' : 'limits_vs_mass',

      # current options are 'mass' and 'lifetime'
     'xAxisType' : 'mass',
     'yAxisType' : 'lifetime',

     'xAxisLabel' : 'chargino mass [GeV]',
     'yAxisLabel' : 'chargino #LTc#tau#GT [cm]',
     
     'showTheory' : True,
     'graphs' : [
    {
    'source' : [limit_dir], #output directory from limit running
    'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
    'colorScheme' : 'brazilian',
    },
    ],
     },
     
     
     ]
