#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *
from amsbLimitConfigBkgds import *    # Produced with ../scripts/makeANTables.py

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
masses = ['100', '300', '500', '700']

#chargino tau values
lifetimes = ['10', '100', '1000']

lumi = 2457

#condor directory in which to find signal root files
signal_condor_dir = WellsDir + 'disTrkSelection'

#name of event selection from which to take signal yields
signal_channel = 'DisTrkSelectionPlotter/Met Plots'


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = True

data_dataset = "MET"

#condor directory in which to find data root file
#data_condor_dir = WellsDir + 'condor_2014_04_29_FullSelectionUnBlinded'
data_condor_dir = WellsDir + 'disTrkSelection' 

#name of event selection from which to take observed events
data_channel = 'DisTrkSelection'

#############################
### Background Parameters ###
#############################



#############################
### Systematic Uncertainties ###
#############################


external_systematic_uncertainties = [
    # Use order of AN
    ]

#uncertainties on signal only (we can alter this if we need to)
# For now, use the largest value of the uncertainty range from Run 1  
signal_systematic_uncertainties = {
     'Isr' : { 
        'value' :'1.11', 
        }, 
     'JES' : { 
        'value' : '1.07', 
        }, 
     # 'JER' : { 
     #    'value' : '', 
     #    }, 
     'PDFWt' : { 
        'value' : '1.10', 
        }, 
     'trigEff' : { 
        'value' : '1.08', 
        }, 
     'NMissOut' : { 
        'value' : '1.07', 
        }, 
     'pileup' : { 
        'value' : '1.02', 
        }, 
     'lumi' :  {
        'value' : '1.046',  # Value for 2015D  
        },
     'trkReco' :  {
        'value' : '1.017',
        },
     'Nmissin' :  {
        'value' : '1.028', # from tables/systNmissIn.tex from makeANTables.py
        },
     'Nmissmid' :  {
        'value' : '1.018', # from tables/systNmissMid.tex from makeANTables.py
        },
     'Ecalo' : {
        'value' : '1.065', # from tables/systEcalo.tex from makeANTables.py
        },
     }

