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
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

if arguments.era.startswith("2017") or arguments.era.startswith("2018") or arguments.era.startswith("2022") or arguments.era.startswith("2023") or arguments.era == "all20178" or arguments.era == "run2" or arguments.era == "run2run3" or arguments.era == "run3":
	masses.extend(['1000', '1100'])
	lifetimes = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1'] + lifetimes
if arguments.era.startswith("2022") or arguments.era.startswith("2023") or arguments.era == "run2run3" or arguments.era == "run3":
	masses.extend(['1200'])

# define maximal set of masses/lifetimes for datacard combinations
allMasses = masses + ['1000', '1100', '1200']

allLifetimes = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1'] + lifetimes
'''datacardCombinations = {
	'all20156' : ['2015', '2016BC', '2016DEFGH'],
	'2017_all' : ['2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus'],
	'2018AB_all' : ['2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus'],
	'2018CD_all' : ['2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'2018_all' : ['2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'all20178' : ['2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'run2'     : ['2015',
				  '2016BC', '2016DEFGH',
				  '2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'2022CD_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus'],
	'2022EFG_all'  : ['2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'2022_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'2023C_all'  : ['2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus'],
	'2023D_all'  : ['2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
	'2023_all'  : ['2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus',
				   '2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
	'run3'  	: ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus',
				   '2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus',
				   '2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
	'run2run3' : ['2015',
				  '2016BC', '2016DEFGH',
				  '2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus',
				  '2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				  '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus',
				  '2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus',
				  '2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
}'''
#debugging
# datacardCombinations = {
# 	'2022CD_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus'],
# 	'2022EFG_all'  : ['2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
# 	'2022_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
# 				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
# 	'run3'  	: ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
# 				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
# 	'run2run3' : ['2015',
# 				  '2016BC', '2016DEFGH',
# 				  '2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
# 				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
# 				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus',
# 				  '2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
# 				  '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
# }
datacardCombinations = {
	# 'all20156' : ['2015', '2016BC', '2016DEFGH'],
	# '2017_all' : ['2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus'],
	# '2018AB_all' : ['2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus'],
	# '2018CD_all' : ['2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	# 'run2'     : ['2015',
	# 			  '2016BC', '2016DEFGH',
	# 			  '2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
	# 			  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
	# 			  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus'],
	'2022CD_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus'],
	'2022EFG_all'  : ['2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'2022_all'  : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				   '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus'],
	'2023C_all'  : ['2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus'],
	'2023D_all'  : ['2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
	'2023_all'   : ['2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus',
					'2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
	'run3'  	 : ['2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				    '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus',
				    '2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus',
					'2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
	'run2run3' : ['2015',
				  '2016BC', '2016DEFGH',
				  '2017_NLayers4', '2017_NLayers5', '2017_NLayers6plus',
				  '2018AB_NLayers4', '2018AB_NLayers5', '2018AB_NLayers6plus',
				  '2018CD_NLayers4', '2018CD_NLayers5', '2018CD_NLayers6plus',
				  '2022CD_NLayers4', '2022CD_NLayers5', '2022CD_NLayers6plus',
				  '2022EFG_NLayers4', '2022EFG_NLayers5', '2022EFG_NLayers6plus',
				  '2023C_NLayers4', '2023C_NLayers5', '2023C_NLayers6plus',
				  '2023D_NLayers4', '2023D_NLayers5', '2023D_NLayers6plus'],
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
elif arguments.era == "20156":
	intLumi = lumi["MET_2015"] + lumi["MET_2016"]
elif arguments.era == "all20178":
	intLumi = lumi["MET_2017"] + lumi["MET_2018"]
elif arguments.era == "run2":
	intLumi = lumi["MET_2015"] + lumi["MET_2016"] + lumi["MET_2017"] + lumi["MET_2018"]
elif arguments.era.startswith("2022CD"):
	intLumi = lumi["MET_2022CD"]
elif arguments.era.startswith("2022EFG"):
	intLumi = lumi["MET_2022EFG"]
elif arguments.era == "2022_all":
	intLumi = lumi["MET_2022CD"] + lumi["MET_2022EFG"]
elif arguments.era.startswith("2023C"):
	intLumi = lumi["MET_2023C"]
elif arguments.era.startswith("2023D"):
	intLumi = lumi["MET_2023D"]
elif arguments.era == "2023_all":
	intLumi = lumi["MET_2023C"] + lumi["MET_2023D"]
elif arguments.era == "run3":
	intLumi = lumi["MET_2022CD"] + lumi["MET_2022EFG"] + lumi["MET_2023C"] + lumi["MET_2023D"]
elif arguments.era == "run2run3":
	intLumi = lumi["MET_2015"] + lumi["MET_2016"] + lumi["MET_2017"] + lumi["MET_2018"] + lumi["MET_2022CD"] + lumi["MET_2022EFG"] + lumi["MET_2023C"] + lumi["MET_2023D"]

# condor directory in which to find signal root files
if arguments.era == "2015":
	signal_condor_dir = dirs['Breno'] + '/bfrancisStore/2015/signalAcceptance_final/'
	signal_suffix = signal_suffix_in_datacard = '76X'
	signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'
	actual_bin_name = 'Bin2015'
	intLumi = lumi["MET_2015"]
elif arguments.era == "2016BC":
	signal_condor_dir = dirs['Breno'] + '/bfrancisDeepStore/2016_final/signalAcceptance_BC_final/'
	signal_suffix = '80X'
	signal_suffix_in_datacard = '80X_BC'
	signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'
	actual_bin_name = 'Bin2016BC'
	intLumi = lumi["MET_2016BC"]
elif arguments.era == "2016DEFGH":
	signal_condor_dir = dirs['Breno'] + '/bfrancisDeepStore/2016_final/signalAcceptance_DEFGH_final/'
	signal_suffix = '80X'
	signal_suffix_in_datacard = '80X_DEFGH'
	signal_channel = 'disTrkSelectionSmearedJetsPlotter/Met Plots'
	actual_bin_name = 'Bin2016DEFGH'
	intLumi = lumi["MET_2016DEFGH"]
elif arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	signal_condor_dir = dirs['Breno'] + '/bfrancisDeepStore/2017/signalAcceptance_full_v9_newISRweights/'
	signal_suffix = signal_suffix_in_datacard = '94X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2017' + nLayersWord
	intLumi = lumi["MET_2017"]
elif arguments.era in ["2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus"]:
	signal_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/signalAcceptance_v3_newISRweights/'
	signal_suffix = signal_suffix_in_datacard = '102X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2018AB' + nLayersWord
	intLumi = lumi["MET_2018AB"]
elif arguments.era in ["2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus"]:
	signal_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/signalAcceptance_v3_HEMveto_newISRweights/'
	signal_suffix = signal_suffix_in_datacard = '102X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJetsHEMveto' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJetsHEMveto' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2018CD' + nLayersWord
	intLumi = lumi["MET_2018CD"]
elif arguments.era in ["2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus"]: # This has to be updated
	signal_condor_dir = dirs["Breno"] + '/SignalMC/Run3/2022preEE/signalAcceptance_sigCentralLooseNoMissOut_v2/'
	signal_suffix = signal_suffix_in_datacard = '130X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2022CD' + nLayersWord
	intLumi = lumi["MET_2022CD"]
elif arguments.era in ["2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	signal_condor_dir = dirs["Breno"] + '/SignalMC/Run3/2022/signalAcceptance_sigCentralLooseNoMissOut_v2/'
	signal_suffix = signal_suffix_in_datacard = '130X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2022EFG' + nLayersWord
	intLumi = lumi["MET_2022EFG"]
elif arguments.era in ["2023C_NLayers4", "2023C_NLayers5", "2023C_NLayers6plus"]: # This has to be updated
	signal_condor_dir = dirs["Breno"] + '/SignalMC/Run3/2023/signalAcceptance_sigCentralLooseNoMissOut_v2/'
	signal_suffix = signal_suffix_in_datacard = '130X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2023C' + nLayersWord
	intLumi = lumi["MET_2023C"]
elif arguments.era in ["2023D_NLayers4", "2023D_NLayers5", "2023D_NLayers6plus"]:
	signal_condor_dir = dirs["Breno"] + '/SignalMC/Run3/2023BPix/signalAcceptance_sigCentralLooseNoMissOut_v2/'
	signal_suffix = signal_suffix_in_datacard = '130X'
	nLayersWord = arguments.era.split('_')[1]
	signal_channel = 'disTrkSelectionSmearedJets' + nLayersWord + 'Plotter/Met Plots'
	signal_channel_tree = 'disTrkSelectionSmearedJets' + nLayersWord + 'TreeMaker/Tree'
	actual_bin_name = 'Bin2023D' + nLayersWord
	intLumi = lumi["MET_2023D"]



lumi = intLumi

#######################
### Data Parameters ###
#######################

# Get the backgrounds for this era
if arguments.era in ["2015", "2016BC", "2016DEFGH", 
					 "2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus", 
					 "2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus",
					 "2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus",
					 "2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus",
					 "2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus",
					 "2023C_NLayers4", "2023C_NLayers5", "2023C_NLayers6plus",
					 "2023D_NLayers4", "2023D_NLayers5", "2023D_NLayers6plus"]:
	exec('from DisappTrks.LimitSetting.bkgdConfig_' + arguments.era + ' import *')

#this just sets the observed number of events equal to the total background expectation

# run_blind_limits = False
run_blind_limits = True

data_dataset = data_condor_dir = data_channel = ""

useHistogramForObservation = False # integrate MET for the observed counts

#condor directory in which to find data root file
if arguments.era == "2015":
	data_dataset = "MET_2015"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'
	rawObservation = 1
elif arguments.era == "2016BC":
	data_dataset = "MET_2016BC"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'
	rawObservation = 2
elif arguments.era == "2016DEFGH":
	data_dataset = "MET_2016DEFGH"
	data_condor_dir = dirs["Andrew"] + '/2016_final_prompt/disappearingTracks/'
	data_channel = 'DisTrkSelectionPlotter/Met Plots'
	rawObservation = 4
elif arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	data_dataset = "MET_2017"
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2017/unblindedResults/'
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
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/unblindNoHEMveto/'
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
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/unblindWithHEMveto/'
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
# Still using 2018AB values; NEEDS TO BE UPDATED
elif arguments.era in ["2023C_NLayers4", "2023C_NLayers5", "2023C_NLayers6plus"]:
	data_dataset = "MET_2018AB"
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/unblindNoHEMveto/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2023C_NLayers4":
		rawObservation = 5
	elif arguments.era == "2023C_NLayers5":
		rawObservation = 0
	elif arguments.era == "2023C_NLayers6plus":
		rawObservation = 2
# Still using 2018AB values; NEEDS TO BE UPDATED
elif arguments.era in ["2023D_NLayers4", "2023D_NLayers5", "2023D_NLayers6plus"]:
	data_dataset = "MET_2018AB"
	data_condor_dir = dirs['Breno'] + '/bfrancisStore/2018/unblindNoHEMveto/'
	data_channel = 'DisTrkSelection' + nLayersWord + 'Plotter/Met Plots'
	useHistogramForObservation = False
	if arguments.era == "2023D_NLayers4":
		rawObservation = 5
	elif arguments.era == "2023D_NLayers5":
		rawObservation = 0
	elif arguments.era == "2023D_NLayers6plus":
		rawObservation = 2

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

if not arguments.era in ["all20156", "2017_all", "2018_all", "2018AB_all", "2018CD_all", "all20178", "run2", "2022CD_all", "2022EFG_all", "2022_all", "2023C_all", "2023D_all", "2023_all", "run3", "run2run3"]:
	for i in range(len(external_systematic_uncertainties)):
		if arguments.era.startswith("2018"):
			external_systematic_uncertainties[i] += "_2018_" + arguments.era[7:]
		elif arguments.era.startswith("2022CD"):
			external_systematic_uncertainties[i] += "_2022CD_" + arguments.era[7:]
		elif arguments.era.startswith("2022EFG"):
			external_systematic_uncertainties[i] += "_2022EFG_" + arguments.era[8:]
		elif arguments.era.startswith("2023C"):
			external_systematic_uncertainties[i] += "_2023C_" + arguments.era[6:]
		elif arguments.era.startswith("2023D"):
			external_systematic_uncertainties[i] += "_2023D_" + arguments.era[6:]
		else:
			external_systematic_uncertainties[i] += "_" + arguments.era

if arguments.era in ["2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus"]:
	external_systematic_uncertainties.append("L1ECALPrefiringWeight_"   + arguments.era)
	external_systematic_uncertainties.append("electronVetoScaleFactor_" + arguments.era)
	external_systematic_uncertainties.append("muonVetoScaleFactor_"     + arguments.era)
	if arguments.era != "2017_NLayers6plus":
		external_systematic_uncertainties.append("triggerTurnOn_"           + arguments.era)

if arguments.era in ["2018AB_NLayers4", "2018AB_NLayers5", "2018AB_NLayers6plus",
					 "2018CD_NLayers4", "2018CD_NLayers5", "2018CD_NLayers6plus"]:
	external_systematic_uncertainties.append("electronVetoScaleFactor_2018_" + arguments.era[7:])
	external_systematic_uncertainties.append("muonVetoScaleFactor_2018_"     + arguments.era[7:])
	if arguments.era != "2018AB_NLayers6plus" and arguments.era != "2018CD_NLayers6plus":
		external_systematic_uncertainties.append("triggerTurnOn_2018_"       + arguments.era[7:])

if arguments.era in ["2022CD_NLayers4", "2022CD_NLayers5", "2022CD_NLayers6plus"]:
	external_systematic_uncertainties.append("electronVetoScaleFactor_2022CD_" + arguments.era[7:])
	external_systematic_uncertainties.append("muonVetoScaleFactor_2022CD_"     + arguments.era[7:])
	if arguments.era != "2022CD_NLayers6plus":
		external_systematic_uncertainties.append("triggerTurnOn_2022CD_"       + arguments.era[7:])

if arguments.era in ["2022EFG_NLayers4", "2022EFG_NLayers5", "2022EFG_NLayers6plus"]:
	external_systematic_uncertainties.append("electronVetoScaleFactor_2022EFG_" + arguments.era[8:])
	external_systematic_uncertainties.append("muonVetoScaleFactor_2022EFG_"     + arguments.era[8:])
	if arguments.era != "2022EFG_NLayers6plus":
		external_systematic_uncertainties.append("triggerTurnOn_2022EFG_"       + arguments.era[8:])

if arguments.era in ["2023C_NLayers4", "2023C_NLayers5", "2023C_NLayers6plus"]:
	external_systematic_uncertainties.append("electronVetoScaleFactor_2023C_" + arguments.era[6:])
	external_systematic_uncertainties.append("muonVetoScaleFactor_2023C_"     + arguments.era[6:])
	if arguments.era != "2023C_NLayers6plus":
		external_systematic_uncertainties.append("triggerTurnOn_2023C_"       + arguments.era[6:])

if arguments.era in ["2023D_NLayers4", "2023D_NLayers5", "2023D_NLayers6plus"]:
	external_systematic_uncertainties.append("electronVetoScaleFactor_2023D_" + arguments.era[6:])
	external_systematic_uncertainties.append("muonVetoScaleFactor_2023D_"     + arguments.era[6:])
	if arguments.era != "2023D_NLayers6plus":
		external_systematic_uncertainties.append("triggerTurnOn_2023D_"       + arguments.era[6:])

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
		'metTrigEff_Bin2022CD_' + nLayersWord : {
	        'value' : '1.006',
	    },
	}

	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2022CD_'  + nLayersWord] =  {'value' : str (1.0 + 0.12272478761252413 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022CD_' + nLayersWord] =  {'value' : str (1.0 + 1.5873015873015872 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2022CD_'  + nLayersWord] =  {'value' : str (1.0 + 1.4794127782809223 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022CD_' + nLayersWord] =  {'value' : str (1.0 + 1.1697731482140135 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2022CD_'  + nLayersWord] =  {'value' : str (1.0 + 0.6460479699310757 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2022CD_' + nLayersWord] =  {'value' : str (1.0 + 3.3466369361479975 / 100.0)}
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
elif arguments.era in ["2023C_NLayers4", "2023C_NLayers5", "2023C_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2023C_' + nLayersWord :  {
	        'value' : '1.013',
	    },
	    'trkReco_Bin2023C_' + nLayersWord :  {
	        'value' : '1.02', # result not yet approved: https://indico.cern.ch/event/827655/contributions/3467109/attachments/1863791/3063951/Tracking_2018Zmm_Jpsi.pdf
	    },
		# Still using 2018AB values; NEEDS TO BE UPDATED
	    'Ecalo_Bin2023C_' + nLayersWord : {
	        'value' : str (1.0 + 18.769142458106796 / 100.0),
	    },
	}

	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2023C_'  + nLayersWord] =  {'value' : str (1.0 + 1.7765212653248832 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2023C_' + nLayersWord] =  {'value' : str (1.0 + 5.882352941176474 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2023C_'  + nLayersWord] =  {'value' : str (1.0 + 0.14965813574925146 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2023C_' + nLayersWord] =  {'value' : str (1.0 + 4.199730560410644 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2023C_'  + nLayersWord] =  {'value' : str (1.0 + 0.5675660812869531 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2023C_' + nLayersWord] =  {'value' : str (1.0 + 4.199730560410644 / 100.0)}
elif arguments.era in ["2023D_NLayers4", "2023D_NLayers5", "2023D_NLayers6plus"]:
	signal_systematic_uncertainties = {
	    'lumi_Bin2023D_' + nLayersWord :  {
	        'value' : '1.013',
	    },
	    'trkReco_Bin2023D_' + nLayersWord :  {
	        'value' : '1.02', # result not yet approved: https://indico.cern.ch/event/827655/contributions/3467109/attachments/1863791/3063951/Tracking_2018Zmm_Jpsi.pdf
	    },
		# Still using 2018AB values; NEEDS TO BE UPDATED
	    'Ecalo_Bin2023D_' + nLayersWord : {
	        'value' : str (1.0 + 20.655643400442806 / 100.0),
	    },
	}

	if arguments.era.endswith("NLayers4"):
		signal_systematic_uncertainties['Nmissin_Bin2023D_'  + nLayersWord] =  {'value' : str (1.0 + 2.0164315732208116 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2023D_' + nLayersWord] =  {'value' : str (1.0 + 4.213451503246696 / 100.0)}
	if arguments.era.endswith("NLayers5"):
		signal_systematic_uncertainties['Nmissin_Bin2023D_'  + nLayersWord] =  {'value' : str (1.0 + 4.1666666666666705 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2023D_' + nLayersWord] =  {'value' : str (1.0 + 4.213451503246696 / 100.0)}
	if arguments.era.endswith("NLayers6plus"):
		signal_systematic_uncertainties['Nmissin_Bin2023D_'  + nLayersWord] =  {'value' : str (1.0 + 0.4958724751640544 / 100.0)}
		signal_systematic_uncertainties['Nmissmid_Bin2023D_' + nLayersWord] =  {'value' : str (1.0 + 4.213451503246696 / 100.0)}
