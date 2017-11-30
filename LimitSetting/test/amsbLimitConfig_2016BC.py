#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from amsbLimitConfigBkgds_2016BC import *    # Produced with ../scripts/makeANTables.py

dirs = getUser ()

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

#NOTE: These are the chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700', '800', '900']

#chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

lumi = lumi["MET_2016BC"]

#condor directory in which to find signal root files
signal_condor_dir = dirs["Brian"] + '/2016_final/signalAcceptance_BC_final/'

signal_suffix = '80X'
signal_suffix_in_datacard = '80X_BC'

#name of event selection from which to take signal yields
signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'

#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = "MET_2016BC"

#condor directory in which to find data root file
data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'

#name of event selection from which to take observed events
data_channel = 'DisTrkSelectionPlotter/Met Plots'

actual_bin_name = '2016BC'

#############################
### Systematic Uncertainties ###
#############################

external_systematic_uncertainties = [
    # Use order of AN
    "isr_2016BC",
    "jec_2016BC",
    "jer_2016BC",
    "metVaryElectronEn_2016BC",
    "metVaryJetEn_2016BC",
    "metVaryJetRes_2016BC",
    "metVaryPhotonEn_2016BC",
    "metVaryTauEn_2016BC",
    "metVaryUnclusteredEn_2016BC",
    "nMissOut_2016BC",
    "pileup_2016BC",
    "trigger_grandOrWeightData_2016BC",
    "trigger_grandOrWeightMC_2016BC",
]

#uncertainties on signal only (we can alter this if we need to)
# For now, use the largest value of the uncertainty range from Run 1
signal_systematic_uncertainties = {
    'lumi' :  {
        'value' : '1.026',
    },
    'trkReco' :  {
        'value' : '1.045',
    },
    'Ecalo' : {
        'value' : str (1.0 + 0.979019194585 / 100.0),
    },
    'Nmissin' :  {
        'value' : str (1.0 + 1.93428533987 / 100.0),
    },
    'Nmissmid' :  {
        'value' : str (1.0 + 2.94687501319 / 100.0),
    },
}
