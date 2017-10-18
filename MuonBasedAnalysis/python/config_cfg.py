from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon channels
################################################################################
#  add_channels  (process,  [muonBasedAnalysis.isoTrkSelection],     histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonBasedAnalysis.candTrkSelection],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonBasedAnalysis.disTrkSelection],     histSets,  weights,  [],  collMap,  variableProducers,  False)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
