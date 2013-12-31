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

#chargino masses
masses = ['32', '50', '75', '100', '150']

#chargino tau values
lifetimes = ['0.5', '1.0', '5.0']

lumi  = 19519  # in /pb  

signalErrFrac = 0.25  # dummy 25% error 

signal_cross_sections = { # in pb 
    '32' : {
         'value' : '11.0',
         'error' : '1.1', # dummy 10% error
         },
    '50' : {
         'value' : '2.0',
         'error' : '0.2', # dummy 10% error
         },
    '75' : {
         'value' : '0.3',
         'error' : '0.03', # dummy 10% error
         },
    '100' : {
         'value' : '0.101',
         'error' : '0.0101', # dummy 10% error
         },
    '150' : {
         'value' : '0.015',
         'error' : '0.0015', # dummy 10% error
         }, 
    }

#condor directory in which to find signal root files
#signal_condor_dir = 'condor_2013_12_17_FullSelectionAllSig' # old
signal_condor_dir = 'condor_2013_12_24_FullSelectionNoMet'   

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
    'elec',
    'muon',
    'tau',
    'fake',
    ]


# Use with condor_2013_12_17_FullSelectionAllSig  
#backgroundEst    = 1.5 
#backgroundEstErr = 2.1 


backgroundEst    = 13.6 
backgroundEstErr = 2.1 





