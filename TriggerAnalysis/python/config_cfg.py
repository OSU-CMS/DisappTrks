from DisappTrks.StandardAnalysis.protoConfig_cfg import *

variableProducers.append('EventTriggerVarProducer')

################################################################################
# Data and W+Jets MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
# add_channels (process, [METLegDenominator],                            histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, METLegNumerator.values(),                       histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegDenominatorWithMuons.values(),          histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegNumeratorWithMuons.values(),            histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)

# The Grand Or
# add_channels (process, [GrandORNumerator],                             histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)

# Testing: require a match of any muon to the HLT track rather than just the lead muon
# add_channels (process, TrackLegNumeratorWithMuonsAnyHLTMatch.values(), histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)

################################################################################
# Signal MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
# add_channels (process, [METLegDenominator],                            histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, METLegNumerator.values(),                       histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegDenominatorWithTracksNoTrig.values(),   histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegNumeratorWithTracksNoTrig.values(),     histSetsTrigger, weightsWithMuonSF, scaleFactorProducers, collectionMap, variableProducers, False)

################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
process.EventTriggerVarProducer.triggerNames = triggerNamesInclusive
process.EventTriggerVarProducer.filterNames = triggerFiltersInclusive
process.EventTriggerVarProducer.signalTriggerNames = triggersMet
