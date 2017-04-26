from DisappTrks.StandardAnalysis.protoConfig_cfg import *

variableProducers.append('EventTriggerVarProducer')

################################################################################
# Data and W+Jets MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
# add_channels (process, [METLegDenominator],                            histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, METLegNumerator.values(),                       histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegDenominatorWithMuons.values(),          histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegNumeratorWithMuons.values(),            histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

# Testing: require a match of any muon to the HLT track rather than just the lead muon
# add_channels (process, TrackLegNumeratorWithMuonsAnyHLTMatch.values(), histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

################################################################################
# Signal MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
# add_channels (process, [METLegDenominator],                            histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, METLegNumerator.values(),                       histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegDenominatorWithTracksNoTrig.values(),   histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, TrackLegNumeratorWithTracksNoTrig.values(),     histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

################################################################################

process.EventTriggerVarProducer.triggerNames = triggersForEfficiency
process.EventTriggerVarProducer.filterNames = triggerFiltersInclusive
