from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################
# Fake-track-enriched variations of the search region used for fake track systematic
#  add_channels  (process,  [disTrkSelectionNHits3],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits4],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits5],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits6],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
  setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
else:
  setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2015_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2015_data.root")
