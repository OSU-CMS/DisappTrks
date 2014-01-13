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
integrateHistogramName = "numEvents"

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,TAU
# named "datacard_AMSB_mGravMASSK_TAUns.txt" 

#NOTE: These are the gravitino masses
masses = ['32', '50', '75', '100', '150']

#chargino tau values
lifetimes = ['0.5', '1.0', '5.0']

lumi = 19500

signalErrFrac = 0.25  # dummy 25% error 

chiMasses = {

    '32' : {
    'value' : '103',
    },

    '50' : {
    'value' : '164',
    },

    '75' : {
    'value' : '247',
    },

    '100' : {
    'value' : '328',
        },

    '150' : {
    'value' : '488',
        },
    
    }

signal_cross_sections = { # in pb 
     '32' : {
          'value' : '14.0',
          'error' : '1.4', # dummy 10% error
 #         'value' : '11.0',
 #         'error' : '1.1', # dummy 10% error
          },
     '50' : {
          'value' : '2.4',
          'error' : '0.24', # dummy 10% error

 #         'value' : '2.0',
 #         'error' : '0.2', # dummy 10% error
          },

     '75' : {
          'value' : '0.4',
          'error' : '0.04', # dummy 10% error

 #         'value' : '0.3',
 #         'error' : '0.03', # dummy 10% error
          },
     '100' : {
          'value' : '0.125',
          'error' : '0.0125', # dummy 10% error

 #         'value' : '0.101',
 #         'error' : '0.0101', # dummy 10% error
          },
     '150' : {
          'value' : '0.0175',
          'error' : '0.00175', # dummy 10% error

 #         'value' : '0.015',
 #         'error' : '0.0015', # dummy 10% error
          }, 
     }

#condor directory in which to find signal root files
#signal_condor_dir = 'condor_2013_12_17_FullSelectionAllSig' # old
#signal_condor_dir = 'condor_2013_12_24_FullSelectionNoMet'   
signal_condor_dir = 'WellsCondorNew/condor_2013_12_24_FullSelectionNoMet'   

#name of event selection from which to take signal yields
#signal_channel = 'FullSelection'
signal_channel = 'FullSelectionNoMet'


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = True

data_dataset = "" 

#condor directory in which to find data root file
data_condor_dir = '' 

#name of event selection from which to take observed events
data_channel = 'FullSelection'

#############################
### Background Parameters ###
#############################

#list of backgrounds that will be added into the datacards
backgrounds = [
#    'elec',
#    'muon',
#    'tau',
#    'fake',
    'total',
     ]

background = 'tot'

# Use with condor_2013_12_17_FullSelectionAllSig  
#backgroundEst    = 1.5 
#backgroundEstErr = 2.1 


backgroundEst    = 13.6 
backgroundEstErr = 2.1 


## plotDefinitions = [
## {
##     'title' : 'limits_vs_mass',
##     'xAxisType' : 'mass',
##     'xAxisLabel' : 'mass [GeV]',


##     'graphs' : [
##                  {
##      'source' : ['DEC9_200um_MarkovChainMC'],
##      'br'   : 50,
##      'lifetime' : 5,
##      'graphsToInclude' : ['exp','obs','oneSigma','twoSigma'],
##      'colorScheme' : 'red',
##      'legendEntry' : 'Markov Chain MC',
##      },
##                  ],
    
## },
## ]




