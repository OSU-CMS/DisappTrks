from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon ISR study channels (to get weights)
################################################################################
# Base skim
#  add_channels  (process,  [ZtoMuMu],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Channels for zToMuMu for isr weights calculation
# remember to change the process customization in config_<era>_cfg.py to remove other weights in MC when you're calculating a new weight!
#  add_channels  (process,  [ZtoMuMuISRStudy],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuISRStudyJet30],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
################################################################################

################################################################################
# SingleMuon channel for Ecalo systematic
################################################################################
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSets,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
################################################################################

################################################################################
# MET channels for missing inner/middle/outer hits systematics
################################################################################
# remember to change the process customization in config_<era>_cfg.py to remove other weights in MC when you're calculating a new weight!

# Channels used for the missing inner/middle/outer hits systematics
add_channels  (process,  [hitsSystematicsCtrlSelection],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, isCRAB=True)
add_channels  (process,  [muonCtrlSelection],             histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, isCRAB=True)
################################################################################

################################################################################
# AMSB signal channels (to get systematic fluctuations)
#
# With branchSets given, many of the below channels are unnecessary as all the needed weight fluctuations are included as branches
#
# For a specific channel, branchSets is necessary if it depends on chargino lifetime and you aren't submitting all the reweighted
# lifetimes. Things like JEC/JER shouldn't, but the signal acceptance and missing outer hits systematic do for example.
################################################################################

# Central value channels
if False:
	histSets.append(MetShiftHistograms)
	#add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)

# Loose vetoes systematic channels
if False:
	add_channels  (process,  [disTrkSelectionSmearedJetsLooseVetoesNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkSelectionSmearedJetsLooseVetoesNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkSelectionSmearedJetsLooseVetoesNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)

	#add_channels  (process,  [disTrkSelectionSmearedJetsLooseVetoesDecayLength3mNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	#add_channels  (process,  [disTrkSelectionSmearedJetsLooseVetoesDecayLength3mNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	#add_channels  (process,  [disTrkSelectionSmearedJetsLooseVetoesDecayLength3mNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)


# Number of missing outer hits channel
if False:
	#add_channels  (process,  [disTrkNoNMissOut],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkNoNMissOutNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkNoNMissOutNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)
	add_channels  (process,  [disTrkNoNMissOutNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers, branchSets = branchSets)

# JEC systematic channels
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJetsJECUp,              disTrkSelectionSmearedJetsJECDown],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsJECUpNLayers4,      disTrkSelectionSmearedJetsJECDownNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsJECUpNLayers5,      disTrkSelectionSmearedJetsJECDownNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsJECUpNLayers6plus,  disTrkSelectionSmearedJetsJECDownNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)

# JER systematic channels
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJetsUp,                disTrkSelectionSmearedJetsDown],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsUpNLayers4,        disTrkSelectionSmearedJetsDownNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsUpNLayers5,        disTrkSelectionSmearedJetsDownNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsUpNLayers6plus,    disTrkSelectionSmearedJetsDownNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)

# MET systematic channels
if False:
	histSets.append(MetShiftHistograms)
	#add_channels  (process,  [disTrkNoMetSmearedJets],                  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkNoMetSmearedJetsNLayers4],          histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkNoMetSmearedJetsNLayers5],          histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkNoMetSmearedJetsNLayers6plus],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	
################################################################################
# AMSB signal channels
# These aren't needed as long as you use branchSets in the central value above
################################################################################

# Pileup systematic channels -- can use TreeMaker to avoid running these
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers)

# ISR systematic channels -- can use TreeMaker to avoid running these
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers)

# Trigger efficiency channels -- can use TreeMaker to avoid running these
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers)

################################################################################
# Test for L1 prefiring issue in 2017 MC
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJetsL1PrefiringTest],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsL1PrefiringTestNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsL1PrefiringTestNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsL1PrefiringTestNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)

################################################################################
# Test compare MT2 selection (2 jets pt>30 and HT>250)
# Question from Yuri 4-8-19
if False:
	#add_channels  (process,  [disTrkSelectionSmearedJetsCompareMT2],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsCompareMT2NLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsCompareMT2NLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
	add_channels  (process,  [disTrkSelectionSmearedJetsCompareMT2NLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print()
    print('You haven\'t added any channels. There\'s nothing to do!')
    print()
    sys.exit(0)
    
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
