#!/usr/bin/env python

from DisappTrks.LimitSetting.limitOptions import *

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,TAU
# named "datacard_AMSB_mGravMASSK_TAUns.txt"

# chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700', '800', '900']

# chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

# name of histogram to integrate to get yields
integrateHistogramName = "metPt"

samplesByGravitinoMass = False

intLumi = 0.0
signal_condor_dir = signal_suffix = signal_channel = signal_channel_tree = actual_bin_name = ""
nLayersWord = ""

# define integrated luminosity
if "MET_" + arguments.era in lumi:
	intLumi = lumi["MET_" + arguments.era]
elif arguments.era.startswith("2017"):
	intLumi = lumi["MET_2017"]
	masses.extend(['1000', '1100'])
	if False: # not ready yet
		lifetimes = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1'] + lifetimes
elif arguments.era == "20156":
	intLumi = lumi["MET_2015"] + lumi["MET_2016"]
elif arguments.era == "run2":
	intLumi = lumi["MET_2015"] + lumi["MET_2016"] + lumi["MET_2017"]

# condor directory in which to find signal root files
if arguments.era == "2015":
	signal_condor_dir = dirs["Brian"] + '/2015/signalAcceptance_final/'
	signal_suffix = signal_suffix_in_datacard = '76X'
	signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'
	actual_bin_name = 'Bin2015'
	intLumi = lumi["MET_2015"]
elif arguments.era == "2016BC":
	signal_condor_dir = dirs["Brian"] + '/2016_final/signalAcceptance_BC_final/'
	signal_suffix = '80X'
	signal_suffix_in_datacard = '80X_BC'
	signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'
	actual_bin_name = 'Bin2016BC'
	intLumi = lumi["MET_2016BC"]
elif arguments.era == "2016DEFGH":
	signal_condor_dir = dirs["Brian"] + '/2016_final/signalAcceptance_DEFGH_final/'
	signal_suffix = '80X'
	signal_suffix_in_datacard = '80X_DEFGH'
	signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'
	actual_bin_name = 'Bin2016DEFGH'
	intLumi = lumi["MET_2016DEFGH"]
elif arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	signal_condor_dir = dirs["Andrew"] + '/2017/signalAcceptance/'
	signal_suffix = signal_suffix_in_datacard = '94X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2017' + nLayersWord
	intLumi = lumi["MET_2017"]

lumi = intLumi

#######################
### Data Parameters ###
#######################

# Get the backgrounds for this era
if arguments.era in ["2015", "2016BC", "2016DEFGH", "2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	exec('from bkgdConfig_' + arguments.era + ' import *')

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = data_condor_dir = data_channel = ""

#condor directory in which to find data root file
if arguments.era == "2015":
	data_dataset = "MET_2015"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'
elif arguments.era == "2016BC":
	data_dataset = "MET_2016BC"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'
elif arguments.era == "2016DEFGH":
	data_dataset = "MET_2016DEFGH"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'
elif arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	# STILL BLINDED, use 2016 as junk
	data_dataset = "MET_2016"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'

################################
### Systematic Uncertainties ###
################################

# Use order of AN
external_systematic_uncertainties = [
    "isr",
    "jec",
    "jer",
    "metVaryElectronEn",
    "metVaryJetEn",
    "metVaryJetRes",
    "metVaryPhotonEn",
    "metVaryTauEn",
    "metVaryUnclusteredEn",
    "nMissOut",
    "pileup",
    "trigger_grandOrWeightData",
    "trigger_grandOrWeightMC",
]

if not arguments.era in ["20156", "2017_all", "run2"]:
	for i in range(len(external_systematic_uncertainties)):
		external_systematic_uncertainties[i] += "_" + arguments.era
if arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	external_systematic_uncertainties.append("L1ECALPrefiringWeight_" + arguments.era)

if arguments.era == "2015":
	signal_systematic_uncertainties = {
    	'lumi' :  {
    	    'value' : '1.023',
    	},
    	'trkReco' :  {
    	    'value' : '1.015',
    	},
    	'Ecalo' : {
    	    'value' : str (1.0 + 0.626555065492 / 100.0),
    	},
    	'Nmissin' :  {
    	    'value' : str (1.0 + 1.16347975146 / 100.0),
    	},
    	'Nmissmid' :  {
    	    'value' : str (1.0 + 0.26902546109 / 100.0),
    	},
	}
elif arguments.era == "2016BC":
	signal_systematic_uncertainties = {
    	'lumi' :  {
    	    'value' : '1.025',
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
elif arguments.era == "2016DEFGH":
	signal_systematic_uncertainties = {
    	'lumi' :  {
    	    'value' : '1.025',
    	},
    	'trkReco' :  {
    	    'value' : '1.045',
    	},
    	'Ecalo' : {
    	    'value' : str (1.0 + 1.01724553994 / 100.0),
    	},
    	'Nmissin' :  {
    	    'value' : str (1.0 + 2.93113227546 / 100.0),
    	},
    	'Nmissmid' :  {
    	    'value' : str (1.0 + 1.23438446885 / 100.0),
    	},
	}
elif arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2017_' + nLayersWord :  {
	        'value' : '1.023',
	    },
	    'trkReco_Bin2017_' + nLayersWord :  {
	        'value' : '1.045', # use value from 2016
	    },
	    'Ecalo_Bin2017_' + nLayersWord : {
	        'value' : str (1.0 + 0.956275783525 / 100.0),
	    },
	    'Nmissin_Bin2017_' + nLayersWord :  {
	        'value' : str (1.0 + 0.0227345880789 / 100.0),
	    },
	    'Nmissmid_Bin2017_' + nLayersWord :  {
	        'value' : str (1.0 + 5.1633269796 / 100.0),
	    },
	}
