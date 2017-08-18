from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon channels
################################################################################
#  add_channels  (process,  [muonBasedAnalysis.isoTrkSelection],     histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [muonBasedAnalysis.candTrkSelection],    histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [muonBasedAnalysis.disTrkSelection],     histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
