#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *

import os

cwd = os.getcwd()
#print "Current directory: " + cwd

if "wulsin" in cwd:
    WellsDir = ""
    AndrewDir = "AndrewCondor/"
elif "hart" in cwd:
    WellsDir = "WellsCondorNew/"
    AndrewDir = ""
else:
    print "Error:  could not identify user as wulsin or hart."
    os.exit(0)


##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
integrateHistogramName = "metPt"

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,TAU
# named "datacard_AMSB_mGravMASSK_TAUns.txt"

samplesByGravitinoMass = False


#NOTE: These are the chargino masses
masses = ['100', '200', '300', '400', '500', '600', '700']

#chargino tau values
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

lumi = 2590.0 + 12884.361

#condor directory in which to find signal root files
signal_condor_dir = AndrewDir + '/2015/disappearingTracks/'

#name of event selection from which to take signal yields
signal_channel = 'DisTrkSelectionPlotter/Met Plots'


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = True

data_dataset = "MET"

#condor directory in which to find data root file
data_condor_dir = signal_condor_dir   # not yet unblinded 

#name of event selection from which to take observed events
data_channel = 'DisTrkSelection'

#############################
### Background Parameters ###
#############################



#############################
### Systematic Uncertainties ###
#############################


