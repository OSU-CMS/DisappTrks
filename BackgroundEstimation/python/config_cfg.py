from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleElectron channels
################################################################################
# Base skim
#  add_channels  (process,  [ElectronTagSkim],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for electron background estimate
#  add_channels  (process,  [ZtoEleProbeTrkWithZCutsNoElectronMuonFiducialCuts],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleDisTrkNoElectronMuonFiducialCuts],             histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsNoElectronMuonFiducialCuts],              histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkNoElectronMuonFiducialCuts],                         histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsBetterPurityNoElectronMuonFiducialCuts],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkBetterPurityNoElectronMuonFiducialCuts],             histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Single electron control regions
#  add_channels  (process,  [ElectronTagPt55NoElectronMuonFiducialCuts],         histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronTagPt55MetTrigNoElectronMuonFiducialCuts],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# SingleMuon channels
################################################################################
# Base skim and ZtoMuMu
#  add_channels  (process,  [MuonTagSkim],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for muon background estimate
#  add_channels  (process,  [ZtoMuProbeTrkWithZCutsNoElectronMuonFiducialCuts],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuDisTrkNoElectronMuonFiducialCuts],             histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsNoElectronMuonFiducialCuts],              histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkNoElectronMuonFiducialCuts],                         histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsBetterPurityNoElectronMuonFiducialCuts],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkBetterPurityNoElectronMuonFiducialCuts],             histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Single muon control regions
#  add_channels  (process,  [MuonTagPt55NoElectronMuonFiducialCuts],         histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt55MetTrigNoElectronMuonFiducialCuts],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Z->mumu channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMu],                                                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuCandTrkNoElectronMuonFiducialCuts],                 histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoElectronMuonFiducialCuts],                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3NoElectronMuonFiducialCuts],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoElectronMuonFiducialCuts],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5NoElectronMuonFiducialCuts],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6NoElectronMuonFiducialCuts],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCutNoElectronMuonFiducialCuts],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# Tau channels
################################################################################
# Base skim
#  add_channels  (process,  [TauTagSkim],  histSetsTau,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Single tau control regions
#  add_channels  (process,  [TauTagPt55NoElectronMuonFiducialCuts],         histSetsTau,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [TauTagPt55MetTrigNoElectronMuonFiducialCuts],  histSetsTau,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################
