from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon ISR study channels (to get weights)
################################################################################
# Base skim
#  add_channels  (process,  [ZtoMuMu],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)

# Channels for zToMuMu for isr weights calculation
#  add_channels  (process,  [ZtoMuMuISRStudy],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuISRStudyJet30],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# SingleMuon channel for Ecalo systematic
################################################################################
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSets,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# AMSB signal channels (to get systematic fluctuations)
################################################################################
# Central value channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Pileup systematic channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# MET systematic channels
#  add_channels  (process,  [disTrkNoMet],             histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetSmearedJets],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# JEC systematic channels
#  add_channels  (process,  [disTrkSelectionJECUp,             disTrkSelectionJECDown],             histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsJECUp,  disTrkSelectionSmearedJetsJECDown],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# JER systematic channels
#  add_channels  (process,  [disTrkSelectionSmearedJetsUp,  disTrkSelectionSmearedJetsDown],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# ISR systematic channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weightsISR,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weightsISR,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Trigger efficiency channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# MET channels for missing inner/middle/outer hits systematics
################################################################################
# Channels used for the missing inner/middle/outer hits systematics
#  add_channels  (process,  [hitsSystematicsCtrlSelection],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelection],             histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
