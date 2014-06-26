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
    JessDir = "JessCondor/"
elif "jbrinson" in cwd:
    WellsDir = "WellsCondorNew/"
    JessDir = ""
else:
    print "Error:  could not identify user as wulsin or jbrinson."
    os.exit(0)


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
#masses = ['300']  

#chargino tau values
#lifetimes = ['1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']
lifetimes = ['1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000','2000','3000','4000','5000','6000','7000','8000','9000','10000']    
#lifetimes = ['1','5','10','50','100','500','1000']
#lifetimes = ['1','5','10','100','500','1000']
#lifetimes = ['2000','3000','4000','5000','6000','7000','8000','9000','10000']  
#lifetimes = ['100']  

lumi = 19500

#condor directory in which to find signal root files
#signal_condor_dir = WellsDir + 'condor_2014_05_19_FullSelectionFilterMC_AllMC'
#signal_condor_dir = WellsDir + 'condor_2014_06_12_FullSelection_AllMC'  
signal_condor_dir = JessDir + 'fullSelectionAllSigBothTrig'  

#name of event selection from which to take signal yields
#signal_channel = 'FullSelectionFilterMC'  
signal_channel = 'FullSelection'  


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = "MET" 

#condor directory in which to find data root file
#data_condor_dir = WellsDir + 'condor_2014_04_29_FullSelectionUnBlinded' 
data_condor_dir = JessDir + 'fullSelectionSkim_24June' 

#name of event selection from which to take observed events
data_channel = 'FullSelection'

#############################
### Background Parameters ###
#############################

##To be used with log normal
##Select condor directory from which the yields after the full selection will be taken
## #  ../scripts/bkgdFromData.py -l bkgdOptions.py -c condor_2014_06_12_bkgdEstUnblind
## #bkgdDir = 'condor_2014_05_07_BkgdEstFullSelUnblind'  
bkgdDir = 'condor_2014_06_12_bkgdEstUnblind'  
background_sources = {
    'Elec' : {
    'condor_dir'  :  WellsDir + bkgdDir,
    },
    'Muon' : {
    'condor_dir'  :  WellsDir + bkgdDir,
    },
    'Tau' : {
    'condor_dir'  :  WellsDir + bkgdDir,
    },
    'Fake' : {
    'condor_dir'  :  WellsDir + bkgdDir,
    },
    }


#############################
### Systematic Uncertainties ###
#############################


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
##     'trackReco',
    ]

#uncertainties on signal only (we can alter this if we need to)
signal_systematic_uncertainties = {
    'lumi' :  {
    'value' : '1.026',
        },
##     'IsrRewtPt' :  {
##     'value' : '1.095',
##         },
##     'JES' :  {
##     'value' : '1.03',
##         },
##     'trigEff' :  {
##     'value' : '1.05',
##         },
##     'EcaloRewt' :  {
##     'value' : '1.05',
##         },
##     'NmissoutRewt' :  {
##     'value' : '1.09',
##         },
##     'pileup' :  {
##     'value' : '1.03',
##         },
    'trkReco' :  {
    'value' : '1.017',
        },
    'Nmissin' :  {
    'value' : '1.028',
        },
    'Nmissmid' :  {
    'value' : '1.018',
        },
    
    }

