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

samplesByGravitinoMass = True


#NOTE: These are the gravitino masses
masses = ['32', '50', '75', '100', '125', '150']

#chargino tau values
lifetimes = ['0.5', '1.0', '5.0']

lumi = 19500

#signalErrFrac = 0.25  # dummy 25% error 

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


#values and errors taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections8TeVcharginocharginoCMS and
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections8TeVcharginoneutralinoCMS

#Also recorded in Sig Cross Sec spreadsheet

signal_cross_sections = { # in pb 
     '32' : {
          'value' : '15.9',
          'error' : '1.10',
          },
     '50' : {
          'value' : '2.73',
          'error' : '1.07',
          },

     '75' : {
          'value' : '0.478',
          'error' : '1.05',
          },
     '100' : {
          'value' : '0.185',
          'error' : '1.05',
          },
     '125' : {
          'value' : '0.0525',
          'error' : '1.05',

          },
     '150' : {
          'value' : '0.0221',
          'error' : '1.05',
          }, 
     }

#condor directory in which to find signal root files
#signal_condor_dir = 'condor_2013_12_17_FullSelectionAllSig' # old
#signal_condor_dir = 'condor_2013_12_24_FullSelectionNoMet'   
#signal_condor_dir = 'WellsCondorNew/condor_2013_12_24_FullSelectionNoMet'   
#signal_condor_dir = 'allSigNewSigma'   
#signal_condor_dir = 'WellsCondorNew/condor_2014_02_11_FullSelectionAllSig'   
#signal_condor_dir = 'fullSelectionAllSig_5March'   
#signal_condor_dir = 'fullSelectionAllSig_7March'
signal_condor_dir = WellsCondorDir + 'condor_2014_02_11_FullSelectionAllSig'

#name of event selection from which to take signal yields
signal_channel = 'FullSelection'


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
#     'condor_dir'  :  JessCondorDir + 'bkgdFromData_20Feb',
     'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
     },
     'Muon' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
     #'condor_dir'  :  JessCondorDir + 'bkgdFromData_20Feb',
         },
     'Tau' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
    #'condor_dir'  :  JessCondorDir + 'bkgdFromData_20Feb',
         },
     'Fake' : {
    'condor_dir'  :  WellsCondorDir + 'condor_2014_05_07_BkgdEstFullSelUnblind',
     #'condor_dir'  :  JessCondorDir + 'bkgdFromData_20Feb',
         },


     }
## totalBkgd = 1.97
## totalBkgdErr = 0.5


#############################
### Systematic Uncertainties ###
#############################

background_systematics = {
    'Elec' : {
#    'value'  : '1.26',
    'value'  : '1.31',
         },
    'ElecWjets' : {
    'value'  : '1.31',
             },
    'Muon' : {
#    'value'  : '1.52',
    'value'  : '1.37',
             },
    'Tau' : {
#    'value'  : '1.19',
    'value'  : '1.37',
             },
    'Fake' : {
    'value'  : '1.18',
             },


         }

external_systematic_uncertainties = [
    # Use order of AN
    'IsrRewtPt',
    'JES',
    'JER',
    'PDFWt',
    'trigEff',
    'EcaloRewt',
    'NmissoutRewt',
    'pileup',
    ]

#uncertainties on signal only (we can alter this if we need to)
signal_systematic_uncertainties = {
    'lumi' :  {
    'value' : '1.026',
        },
    'trkReco' :  {
    'value' : '1.017',
        },
    }

