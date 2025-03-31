#!/usr/bin/env python3

from DisappTrks.LimitSetting.limitOptions import *

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,TAU
# named "datacard_AMSB_mGravMASSK_TAUns.txt"

# chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700', '800', '900']

# chargino tau values in cm
lifetimes = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1',
             '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

if arguments.era.startswith("2022") or arguments.era.startswith("2023") or arguments.era == "run2run3" or arguments.era == "run3":
	masses.extend(['1000'])

# define maximal set of masses/lifetimes for datacard combinations
allMasses = masses + ['1000']
allLifetimes = lifetimes
'''datacardCombinations = {
	'2017_all' : ['2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus'],
	'2018AB_all' : ['2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus'],
	'2018CD_all' : ['2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'2018_all' : ['2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'all20178' : ['2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'2022CD_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus'],
	'2022EFG_all'  : ['2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'2022_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'run3'  	: ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'run2run3' : ['2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus',
				  '2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				  '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
}'''
#debugging
datacardCombinations = {
	'2022EFG_all'  : ['2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
}

# name of histogram to integrate to get yields
integrateHistogramName = "metNoMu"

samplesByGravitinoMass = False

intLumi = 0.0
signal_condor_dir = signal_suffix = signal_channel = signal_channel_tree = actual_bin_name = ""
nLayersWord = ""

# define integrated luminosity
if "MET_" + arguments.era in lumi:
	intLumi = lumi["MET_" + arguments.era]
elif arguments.era.startswith("2017"):
	intLumi = lumi["MET_2017"]
elif arguments.era.startswith("2018AB"):
	intLumi = lumi["MET_2018AB"]
elif arguments.era.startswith("2018CD"):
	intLumi = lumi["MET_2018CD"]
elif arguments.era.startswith("2018_"):
	intLumi = lumi["MET_2018"]
elif arguments.era == "all20178":
	intLumi = lumi["MET_2017"] + lumi["MET_2018"]
elif arguments.era == "run2":
	intLumi = lumi["MET_2017"] + lumi["MET_2018"]
elif arguments.era.startswith("2022CD"):
	intLumi = lumi["MET_2022CD"]
elif arguments.era.startswith("2022EFG"):
	intLumi = lumi["MET_2022EFG"]
elif arguments.era == "2022_all":
	intLumi = lumi["MET_2022CD"] + lumi["MET_2022EFG"]
elif arguments.era == "run3":
	intLumi = lumi["MET_2022CD"] + lumi["MET_2022EFG"] + 17794.0 + 9451
elif arguments.era == "run2run3":
	intLumi = lumi["MET_2017"] + lumi["MET_2018"] + lumi["MET_2022CD"] + lumi["MET_2022EFG"] + 17794.0 + 9451

# condor directory in which to find signal root files
if arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	signal_condor_dir = dirs["Brian"] + '/2017/signalAcceptance_higgsino/'
	signal_suffix = signal_suffix_in_datacard = '94X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2017' + nLayersWord
	intLumi = lumi["MET_2017"]
elif arguments.era in ["2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus"]:
	signal_condor_dir = dirs["Brian"] + '/2018/signalAcceptance_higgsino_newISRweights/'
	signal_suffix = signal_suffix_in_datacard = '102X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2018AB' + nLayersWord
	intLumi = lumi["MET_2018AB"]
elif arguments.era in ["2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus"]:
	signal_condor_dir = dirs["Brian"] + '/2018/signalAcceptance_higgsino_HEMveto_newISRweights/'
	signal_suffix = signal_suffix_in_datacard = '102X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJetsHEMveto' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJetsHEMveto' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2018CD' + nLayersWord
	intLumi = lumi["MET_2018CD"]
elif arguments.era in ["2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus"]: # This has to be updated
	signal_condor_dir = dirs["Breno"] + '/SignalMC/Run3/2022/signalAcceptance_higgsino_sigCentralLooseNoMissOut_v2/'
	signal_suffix = signal_suffix_in_datacard = '130X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2022CD' + nLayersWord
	intLumi = lumi["MET_2022CD"]
elif arguments.era in ["2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	signal_condor_dir = dirs["Breno"] + '/SignalMC/Run3/2022/signalAcceptance_higgsino_sigCentralLooseNoMissOut_v2/'
	signal_suffix = signal_suffix_in_datacard = '130X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2022EFG' + nLayersWord
	intLumi = lumi["MET_2022EFG"]
	# intLumi = lumi["MET_2022EFG"] + lumi["MET_2022F"] + lumi["MET_2022G"] # scaling to 2022 lumi
	# intLumi = lumi["MET_2022EFG"] + lumi["MET_2022F"] + lumi["MET_2022G"] + 17794.0 + 9451.0 # scaling to 2022+2023 lumi

lumi = intLumi

#######################
### Data Parameters ###
#######################

# Get the backgrounds for this era
if arguments.era in [ "2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus", 
					 "2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus",
					 "2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus",
					 "2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus",
					 "2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	exec('from DisappTrks.LimitSetting.bkgdConfig_' + arguments.era + ' import *')

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = data_condor_dir = data_channel = ""

useHistogramForObservation = True # integrate MET for the observed counts

#condor directory in which to find data root file
if arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	data_dataset = "MET_2017"
	data_condor_dir = dirs["Brian"] + '/2017/unblindedResults/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2017_NLayers4":
		rawObservation = 17
	elif arguments.era == "2017_NLayers5":
		rawObservation = 4
	elif arguments.era == "2017_NLayers6plus":
		rawObservation = 6
elif arguments.era in ["2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus"]:
	data_dataset = "MET_2018AB"
	data_condor_dir = dirs["Brian"] + '/2018/unblindNoHEMveto/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2018AB_NLayers4":
		rawObservation = 5
	elif arguments.era == "2018AB_NLayers5":
		rawObservation = 0
	elif arguments.era == "2018AB_NLayers6plus":
		rawObservation = 2
elif arguments.era in ["2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus"]:
	data_dataset = "MET_2018CD"
	data_condor_dir = dirs["Brian"] + '/2018/unblindWithHEMveto/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2018CD_NLayers4":
		rawObservation = 11
	elif arguments.era == "2018CD_NLayers5":
		rawObservation = 2
	elif arguments.era == "2018CD_NLayers6plus":
		rawObservation = 1
# Still using 2018AB values; NEEDS TO BE UPDATED
elif arguments.era in ["2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus"]:
	data_dataset = "MET_2018AB"
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/unblindNoHEMveto/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2022CD_NLayers4":
		rawObservation = 5
	elif arguments.era == "2022CD_NLayers5":
		rawObservation = 0
	elif arguments.era == "2022CD_NLayers6plus":
		rawObservation = 2
# Still using 2018AB values; NEEDS TO BE UPDATED
elif arguments.era in ["2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	data_dataset = "MET_2018AB"
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/unblindNoHEMveto/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2022EFG_NLayers4":
		rawObservation = 5
	elif arguments.era == "2022EFG_NLayers5":
		rawObservation = 0
	elif arguments.era == "2022EFG_NLayers6plus":
		rawObservation = 2

################################
### Systematic Uncertainties ###
################################

# Use order of AN
external_systematic_uncertainties = [
    "higgsino_isr",
    "higgsino_jec",
    "higgsino_jer",
    "higgsino_metVaryElectronEn",
    "higgsino_metVaryJetEn",
    "higgsino_metVaryJetRes",
    "higgsino_metVaryPhotonEn",
    "higgsino_metVaryTauEn",
    "higgsino_metVaryUnclusteredEn",
    "higgsino_nMissOut",
    "higgsino_pileup",
    "higgsino_trigger_grandOrWeightData",
    "higgsino_trigger_grandOrWeightMC",
    "higgsino_electronVetoScaleFactor",
    "higgsino_muonVetoScaleFactor",
]

if not arguments.era in ["2017_all", "2018_all", "2018AB_all", "2018CD_all", "all20178", "run2", "2022CD_all", "2022EFG_all", "2022_all", "run3", "run2run3"]:
	for i in range(len(external_systematic_uncertainties)):
		if arguments.era.startswith("2018"):
			external_systematic_uncertainties[i] += "_2018_" + arguments.era[7:]
		elif arguments.era.startswith("2022CD"):
			external_systematic_uncertainties[i] += "_2022CD_" + arguments.era[7:]
		elif arguments.era.startswith("2022EFG"):
			external_systematic_uncertainties[i] += "_2022EFG_" + arguments.era[8:]
		else:
			external_systematic_uncertainties[i] += "_" + arguments.era

if arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	external_systematic_uncertainties.append("higgsino_L1ECALPrefiringWeight_"   + arguments.era)
	if arguments.era != "2017_NLayers6plus":
		external_systematic_uncertainties.append("higgsino_triggerTurnOn_"           + arguments.era)
if arguments.era in ["2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus",
					 "2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus"]:
	if arguments.era != "2018AB_NLayers6plus" and arguments.era != "2018CD_NLayers6plus":
		external_systematic_uncertainties.append("higgsino_triggerTurnOn_2018_"       + arguments.era[7:])
if arguments.era in ["2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	external_systematic_uncertainties.append("higgsino_electronVetoScaleFactor_2022EFG_" + arguments.era[8:])
	external_systematic_uncertainties.append("higgsino_muonVetoScaleFactor_2022EFG_"     + arguments.era[8:])
	if arguments.era != "2022EFG_NLayers6plus":
		external_systematic_uncertainties.append("higgsino_triggerTurnOn_2022EFG_"       + arguments.era[8:])

if arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2017_' + nLayersWord :  {
	        'value' : '1.023',
	    },
	    'trkReco_Bin2017_' + nLayersWord :  {
	        'value' : '1.021',
	    },
	    'Ecalo_Bin2017_' + nLayersWord : {
	        'value' : str (1.0 + 0.956275783525 / 100.0),
	    },
	    'Nmissmid_Bin2017_' + nLayersWord : {
	    	'value' : '1.051633269796',
	    },
	}
	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2017_' + nLayersWord] =  {'value' : str (1.0 + 4.20586172635 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2017_' + nLayersWord] =  {'value' : str (1.0 + 1.61290322581 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2017_' + nLayersWord] =  {'value' : str (1.0 + 0.0868040086816 / 100.0)}
elif arguments.era in ["2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus",
					   "2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2018_' + nLayersWord :  {
	        'value' : '1.025',
	    },
	    'trkReco_Bin2018_' + nLayersWord :  {
	        'value' : '1.025', # result not yet approved: https://indico.cern.ch/event/827655/contributions/3467109/attachments/1863791/3063951/Tracking_2018Zmm_Jpsi.pdf
	    },
	    'Ecalo_Bin2018_' + nLayersWord : {
	        'value' : str (1.0 + 0.373129152421 / 100.0),
	    },
	}

	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2018_'  + nLayersWord] =  {'value' : str (1.0 + 0.430847539825 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2018_' + nLayersWord] =  {'value' : str (1.0 + 2.52100840336 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2018_'  + nLayersWord] =  {'value' : str (1.0 + 2.94117647059 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2018_' + nLayersWord] =  {'value' : str (1.0 + 4.87652492286 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2018_'  + nLayersWord] =  {'value' : str (1.0 + 0.928855948344 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2018_' + nLayersWord] =  {'value' : str (1.0 + 3.72041349824 / 100.0)}
elif arguments.era in ["2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2022CD_' + nLayersWord :  {
	        'value' : '1.014',
	    },
	    'trkReco_Bin2022CD_' + nLayersWord :  {
	        'value' : '1.0073', # result not yet approved: https://indico.cern.ch/event/827655/contributions/3467109/attachments/1863791/3063951/Tracking_2018Zmm_Jpsi.pdf
	    },
		# Still using 2018AB values; NEEDS TO BE UPDATED
	    'Ecalo_Bin2022CD_' + nLayersWord : {
	        'value' : str (1.0 + 3.4553713335066223 / 100.0),
	    },
	}

	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2022CD_'  + nLayersWord] =  {'value' : str (1.0 + 0.03155349668257941 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022CD_' + nLayersWord] =  {'value' : str (1.0 + 3.8267556376462535 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2022CD_'  + nLayersWord] =  {'value' : str (1.0 + 2.94117647059 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022CD_' + nLayersWord] =  {'value' : str (1.0 + 3.8267556376462535 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2022CD_'  + nLayersWord] =  {'value' : str (1.0 + 0.928855948344 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022CD_' + nLayersWord] =  {'value' : str (1.0 + 3.8267556376462535 / 100.0)}
elif arguments.era in ["2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2022EFG_' + nLayersWord :  {
	        'value' : '1.014',
	    },
	    'trkReco_Bin2022EFG_' + nLayersWord :  {
	        'value' : '1.0073', # result not yet approved: https://indico.cern.ch/event/827655/contributions/3467109/attachments/1863791/3063951/Tracking_2018Zmm_Jpsi.pdf
	    },
		# Still using 2018AB values; NEEDS TO BE UPDATED
	    'Ecalo_Bin2022EFG_' + nLayersWord : {
	        'value' : str (1.0 + 3.4553713335066223 / 100.0),
	    },
	}

	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2022EFG_'  + nLayersWord] =  {'value' : str (1.0 + 0.0315534966825794 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022EFG_' + nLayersWord] =  {'value' : str (1.0 + 3.8267556376462535 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2022EFG_'  + nLayersWord] =  {'value' : str (1.0 + 1.4794127782809223 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022EFG_' + nLayersWord] =  {'value' : str (1.0 + 3.8267556376462535 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2022EFG_'  + nLayersWord] =  {'value' : str (1.0 + 0.6460479699310757 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022EFG_' + nLayersWord] =  {'value' : str (1.0 + 3.8267556376462535 / 100.0)}
