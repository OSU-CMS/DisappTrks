from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################
# Channels requiring only MET+jet
#  add_channels  (process,  [metMinimalSkim],  histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [basicSelection],  histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)

# Channels requiring MET+jet+track
#  add_channels  (process,  [isoTrkSelectionNoElectronMuonFiducialCuts],    histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkSelectionNoElectronMuonFiducialCuts],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [elecCtrlSelectionNoElectronMuonFiducialCuts],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelectionNoElectronMuonFiducialCuts],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [tauCtrlSelectionNoElectronMuonFiducialCuts],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)

# Variations of the disappearing tracks search region
#  add_channels  (process,  [disTrkIdElecNoElectronMuonFiducialCuts],      histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdMuonNoElectronMuonFiducialCuts],      histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdTauNoElectronMuonFiducialCuts],       histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdFakeNoElectronMuonFiducialCuts],      histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOutNoElectronMuonFiducialCuts],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)

# THE disappearing tracks search region
#  add_channels  (process,  [disTrkSelectionNoElectronMuonFiducialCuts],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
  setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
else:
  setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2015_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2015_data.root")
