from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################
# Channels used for the missing inner/middle/outer hits systematics
#  add_channels  (process,  [hitsSystematicsCtrlSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelection],             histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# SingleMuon channels
################################################################################
# Channel used for the Ecalo systematic
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

# set this to our arbitrary, default value for any studies that are not
# sensitive to it
#setThresholdForVeto (process, 2.0)
