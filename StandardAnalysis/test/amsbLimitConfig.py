#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -R -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

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

#NOTE: These are the gravitino masses
masses = ['32', '50', '75', '100', '125', '150']

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

    '125' : {
    'value' : '408',
        },

    '150' : {
    'value' : '488',
        },
    
    }

signal_cross_sections = { # in pb 
     '32' : {
          'value' : '14.0',
          'error' : '1.25', # dummy 10% error
          },
     '50' : {
          'value' : '2.4',
          'error' : '1.25', # dummy 10% error
          },

     '75' : {
          'value' : '0.4',
          'error' : '1.25', # dummy 10% error
          },
     '100' : {
          'value' : '0.125',
          'error' : '1.25', # dummy 10% error
          },
     '125' : {
          'value' : '0.0438',
          'error' : '1.25', # dummy 10% error
          },
     '150' : {
          'value' : '0.0175',
          'error' : '1.25', # dummy 10% error
          }, 
     }

#condor directory in which to find signal root files
#signal_condor_dir = 'condor_2013_12_17_FullSelectionAllSig' # old
#signal_condor_dir = 'condor_2013_12_24_FullSelectionNoMet'   
#signal_condor_dir = 'WellsCondorNew/condor_2013_12_24_FullSelectionNoMet'   
#signal_condor_dir = 'allSigNewSigma'   
#signal_condor_dir = 'WellsCondorNew/condor_2014_02_11_FullSelectionAllSig'   
signal_condor_dir = WellsCondorDir + 'condor_2014_02_11_FullSelectionAllSig'   

#name of event selection from which to take signal yields
signal_channel = 'FullSelection'


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
#All values are taken from 'Total Bkgd' sheet
#Errors include statistical and systematic and are fractional errors

## For gamma function option, these are just read in.
## alpha = (data yield without lepton veto)*(mc yield with lepton veto)/(mc yield without lepton veto)
backgrounds = {

     'Elec' : {
     'N' : '1',
     'alpha' : '0.44',
               },
      'Muon' : {
      'N' : '1',
      'alpha' : '0.66',
                    },
      'Tau' : {
      'N' : '1',
      'alpha' : '0.003',
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
     'condor_dir'  : JessCondorDir + 'bkgdFromData_20Feb',
     },
     'Muon' : {
     'condor_dir'  : JessCondorDir + 'bkgdFromData_20Feb',
         },
     'Tau' : {
     'condor_dir'  : JessCondorDir + 'bkgdFromData_20Feb',
         },
     'Fake' : {
     'condor_dir'  : JessCondorDir + 'bkgdFromData_20Feb',
         },


     }
totalBkgd = 1.97
totalBkgdErr = 0.5


#############################
### Systematic Uncertainties ###
#############################

background_systematics = {
    'Elec' : {
    'value'  : '1.26',
         },
    'Muon' : {
    'value'  : '1.52',
             },
    'Tau' : {
    'value'  : '1.19',
             },
    'Fake' : {
    'value'  : '1.18',
             },


         }

external_systematic_uncertainties = [
            'IsrRewtPt', 
            'JER',
            'JES',
            'PDFWt',
#            'trigEff',
            'Ecalo',
            'NMissOut',
            'pileup',
            'trackReco',
        ]

#uncertainties on signal only (we can alter this if we need to)
signal_systematic_uncertainties = {
    'lumi' :  {
    'value' : '1.026',
        },
    }

