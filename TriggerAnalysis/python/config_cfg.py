from DisappTrks.StandardAnalysis.protoConfig_cfg import *

variableProducers.append('EventTriggerVarProducer')

################################################################################
# Data and W+Jets MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
#  add_channels  (process,  [METLegDenominator],                    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  METLegNumerator.values(),               histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegDenominatorWithMuons.values(),  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegNumeratorWithMuons.values(),    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# The Grand Or
#  add_channels  (process,  [GrandOrDenominator],  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [GrandORNumerator],    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# Testing: require a match of any muon to the HLT track rather than just the lead muon
#  add_channels  (process,  TrackLegNumeratorWithMuonsAnyHLTMatch.values(),  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

################################################################################
# Signal MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
#  add_channels  (process,  [METLegDenominator],                           histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  METLegNumerator.values(),                      histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegDenominatorWithTracksNoTrig.values(),  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegNumeratorWithTracksNoTrig.values(),    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

################################################################################
# HLT purity measurement channels -- BasicSelection but only with one HLT path
################################################################################

#  add_channels  (process,  [basicSelectionOnlyMET75IsoTrk50],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionOnlyMET90IsoTrk50],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)

#  add_channels  (process,  [basicSelectionOnlyMET75IsoTrk50HltMet105],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionOnlyMET90IsoTrk50HltMet105],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)

################################################################################

#  add_channels  (process,  [justMET75IsoTrk50],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justMET90IsoTrk50],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)

################################################################################
# ARC question testing channels
################################################################################

#  add_channels  (process,  [MuonTagPt55HLTMetFilters],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
process.EventTriggerVarProducer.triggerNames = triggerNamesInclusive
process.EventTriggerVarProducer.filterNames = triggerFiltersInclusive
process.EventTriggerVarProducer.signalTriggerNames = triggersMet
