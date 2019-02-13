from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon ISR study channels (to get weights)
################################################################################
# Base skim
#  add_channels  (process,  [ZtoMuMu],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

# Channels for zToMuMu for isr weights calculation
# remember to change the process customization in config_<era>_cfg.py to remove other weights in MC when you're calculating a new weight!
#  add_channels  (process,  [ZtoMuMuISRStudy],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuISRStudyJet30],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# SingleMuon channel for Ecalo systematic
################################################################################
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSets,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# AMSB signal channels (to get systematic fluctuations)
################################################################################
# Central value channels
#  add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# Pileup systematic channels
#  add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers,  False)

# MET systematic channels
#  histSets.append(MetShiftHistograms)
#  add_channels  (process,  [disTrkNoMet],                  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetNLayers4],          histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetNLayers5],          histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetNLayers6plus],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkNoMetSmearedJets],                  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetSmearedJetsNLayers4],          histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetSmearedJetsNLayers5],          histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetSmearedJetsNLayers6plus],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# JEC systematic channels
#  add_channels  (process,  [disTrkSelectionSmearedJetsJECUp,              disTrkSelectionSmearedJetsJECDown],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsJECUpNLayers4,      disTrkSelectionSmearedJetsJECDownNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsJECUpNLayers5,      disTrkSelectionSmearedJetsJECDownNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsJECUpNLayers6plus,  disTrkSelectionSmearedJetsJECDownNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# JER systematic channels
#  add_channels  (process,  [disTrkSelectionSmearedJetsUp,                disTrkSelectionSmearedJetsDown],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsUpNLayers4,        disTrkSelectionSmearedJetsDownNLayers4],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsUpNLayers5,        disTrkSelectionSmearedJetsDownNLayers5],      histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsUpNLayers6plus,    disTrkSelectionSmearedJetsDownNLayers6plus],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# ISR systematic channels
#  add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers,  False)

# Trigger efficiency channels
#  add_channels  (process,  [disTrkSelectionSmearedJets],              histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],      histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],      histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus],  histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)

# Number of missing outer hits channel
#  add_channels  (process,  [disTrkNoNMissOut],              histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOutNLayers4],      histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOutNLayers5],      histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOutNLayers6plus],  histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)

################################################################################

################################################################################
# MET channels for missing inner/middle/outer hits systematics
################################################################################
# remember to change the process customization in config_<era>_cfg.py to remove other weights in MC when you're calculating a new weight!

# Channels used for the missing inner/middle/outer hits systematics
#  add_channels  (process,  [hitsSystematicsCtrlSelection],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelection],             histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# MET channels for Checking 2017 Luminosity
################################################################################

#add_channels (process, [metTrigJustMain, metTrigOnlyPerfectNoMain2017, metTrigOnlyPerfectAndMain2017, metTrigAllUnprescaled2017, metTrigAllowDisabledHighPU2017], [histSets,histSetsTrigger],  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

process.EventJetVarProducer.triggerNames = triggerNamesInclusive

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
