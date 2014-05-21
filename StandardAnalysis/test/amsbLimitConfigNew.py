#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *

# For Wells's running:
JessCondorDir = "JessCondor/"
WellsCondorDir = ""

## # For Jess's running:
## JessCondorDir = ""
## WellsCondorDir = "WellsCondorNew/"   




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

samplesByGravitinoMass = False  


#NOTE: These are the chargino masses
masses = ['100', '200', '300', '400', '500', '600']  

#chargino tau values
lifetimes = ['1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']

lumi = 19500

#condor directory in which to find signal root files
signal_condor_dir = WellsCondorDir + 'condor_2014_05_19_FullSelectionFilterMC_AllMC'

#name of event selection from which to take signal yields
signal_channel = 'FullSelectionFilterMC'  


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = "MET" 

#condor directory in which to find data root file
data_condor_dir = WellsCondorDir + 'condor_2014_04_29_FullSelectionUnBlinded' 

#name of event selection from which to take observed events
data_channel = 'FullSelection'

#############################
### Background Parameters ###
#############################
#All values are taken from 'Total Bkgd' sheet
#Errors include statistical and systematic and are fractional errors

## For gamma function option, these are just read in.
## alpha = (data yield without lepton veto)*(mc yield with lepton veto)/(mc yield without lepton veto)
backgrounds = {
    
    'Elec' : {
    'N' : '1',
    'alpha' : '0.44',
    },
    'ElecWjets' : {
    'N' : '0',
    'alpha' : '0.37',
    },
    'Muon' : {
    'N' : '1',
    'alpha' : '0.66',
    },
    'Tau' : {
    #'N' : '1',
    'N' : '0',
    #'alpha' : '0.003',
    'alpha' : '0.3',
    },
    'Fake' : {
    'N' : '3',
    'alpha' : '0.29',
    },
    }              

##To be used with log normal
##Select condor directory from which the yields after the full selection will be taken
background_sources = {
    'Elec' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
    },
    'Muon' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
    },
    'Tau' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
    },
    'Fake' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
    },
    }


#############################
### Systematic Uncertainties ###
#############################

background_systematics = {
    'Elec' : {
    'value'  : '1.31',
         },
    'ElecWjets' : {
    'value'  : '1.31',
             },
    'Muon' : {
    'value'  : '1.37',
             },
    'Tau' : {
    'value'  : '1.37',
             },
    'Fake' : {
    'value'  : '1.18',
             },


         }

external_systematic_uncertainties = [
    # Use order of AN
##     'IsrRewtPt',
##     'JES',
##     'JER',
##     'PDFWt',
##     'trigEff',
##     'EcaloRewt',
##     'NmissoutRewt',
##     'pileup',
##     'trackReco',
    ]

#uncertainties on signal only (we can alter this if we need to)
signal_systematic_uncertainties = {
    'lumi' :  {
    'value' : '1.026',
        },
    'IsrRewtPt' :  {
    'value' : '1.095',
        },
    'JES' :  {
    'value' : '1.03',
        },
    'trigEff' :  {
    'value' : '1.10',
        },
    'EcaloRewt' :  {
    'value' : '1.05',
        },
    'NmissoutRewt' :  {
    'value' : '1.09',
        },
    'pileup' :  {
    'value' : '1.03',
        },
    'trkReco' :  {
    'value' : '1.017',
        },
    
    }

