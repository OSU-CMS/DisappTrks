from DisappTrks.StandardAnalysis.protoConfig_cfg import *

variableProducers.append('EventTriggerVarProducer')

################################################################################
# Data and W+Jets MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
# add_channels (process, [METLegDenominator],                     histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [METLegNumerator],                       histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegDenominatorWithMuons],          histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegNumeratorWithMuons],            histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

# Testing: require a match of any muon to the HLT track rather than just the lead muon
# add_channels (process, [TrackLegNumeratorWithMuonsAnyHLTMatch], histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

# HLT_MET90_IsoTrk50 channels -- need METLegDenominator which is already above
# add_channels (process, [MET90LegNumerator],                          histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegDenominatorWithMuonsMet90],          histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegNumeratorWithMuonsMet90],            histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

# Testing: require a match of any muon to the HLT track rather than just the lead muon
# add_channels (process, [TrackLegNumeratorWithMuonsAnyHLTMatchMet90], histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

################################################################################
# Signal MC channels
################################################################################

# HLT_MET75_IsoTrk50 channels
# add_channels (process, [METLegDenominator],                   histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [METLegNumerator],                     histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegDenominatorWithTracksNoTrig], histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegNumeratorWithTracksNoTrig],   histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

# HLT_MET90_IsoTrk50 channels -- need METLegDenominator which is already above
# add_channels (process, [MET90LegNumerator],                        histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegDenominatorWithTracksNoTrigMet90], histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)
# add_channels (process, [TrackLegNumeratorWithTracksNoTrigMet90],   histSetsTrigger, weights, scaleFactorProducers, collectionMap, variableProducers, False)

################################################################################
