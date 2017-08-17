from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon channels
################################################################################
#  add_channels  (process,  [isoTrkSelection],     histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkSelection],    histSets,  weights,  [],  collectionMap,  variableProducers,  False)
add_channels  (process,  [disTrkSelection],     histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
