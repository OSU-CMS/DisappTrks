from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleElectron channels
################################################################################
# Base skim
#  add_channels  (process,  [ElectronTagSkim],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for fiducial map
#  add_channels  (process,  [ElectronFiducialCalcBefore],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronFiducialCalcAfter],   histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Tag-and-probe channels for electron background estimate
#  add_channels  (process,  [ZtoEleProbeTrkWithZCuts],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleDisTrk],             histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCuts],              histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrk],                         histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsBetterPurity],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkBetterPurity],             histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Single electron control regions
#  add_channels  (process,  [ElectronTagPt55],         histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronTagPt55MetTrig],  histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Testing for fake track systematic investigation
#  add_channels  (process,  [ZtoEleProbeTrkWithZCutsNoValidHitsCut],      histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleDisTrkNoValidHitsCut],                 histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut], histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkNoValidHitsCut],            histSetsElectron,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

################################################################################

################################################################################
# SingleMuon channels
################################################################################
# Base skim and ZtoMuMu
#  add_channels  (process,  [MuonTagSkim],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for fiducial map
#  add_channels  (process,  [MuonFiducialCalcBefore],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [MuonFiducialCalcAfter],   histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Tag-and-probe channels for muon background estimate
#  add_channels  (process,  [ZtoMuProbeTrkWithZCuts],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuDisTrk],             histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCuts],              histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrk],                         histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsBetterPurity],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkBetterPurity],             histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Single muon control regions
#  add_channels  (process,  [MuonTagPt55],         histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt55MetTrig],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# Z->mumu channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMu],                        histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuCandTrk],                 histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrk],                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6],            histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with no D0 requirement on the isoTrk
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0Cut],       histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits3], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits4], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits5], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits6], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with inverted D0 requirement on the isoTrk
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0Cut],       histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits3], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits4], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits5], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits6], histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu+jet channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMuJet],              histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkJet],        histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3Jet],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4Jet],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5Jet],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6Jet],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu+jet channels for fake track background estimate with one jet and ==16 PV
#  add_channels  (process,  [ZtoMuMuOneJet14to18PV],             histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers, False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrk],        histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits3],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits4],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits5],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits6],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: W->munu for fake track background estimate
#  add_channels  (process,  [WtoMuNu],              histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrk],        histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits3],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits4],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits5],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits6],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: W->munu for fake track background estimate with one jet and ==16 PV
#  add_channels  (process,  [WtoMuNuOneJet14to18PV],              histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrk],        histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits3],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits4],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits5],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits6],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels with relaxed missing outer hits requirements
#  add_channels  (process,  [ZtoMuMuDisTrk2],                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Testing for fake track systematic investigation
#  add_channels  (process,  [ZtoMuProbeTrkWithZCutsNoValidHitsCut],       histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuDisTrkNoValidHitsCut],                  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut],  histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkNoValidHitsCut],             histSetsMuon,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

################################################################################

################################################################################
# Tau channels
################################################################################
# Base skim
#  add_channels  (process,  [TauTagSkim],  histSetsTau,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)

# Single tau control regions
#  add_channels  (process,  [TauTagPt55],         histSetsTau,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [TauTagPt55MetTrig],  histSetsTau,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
# ZeroBias channels
################################################################################
#  add_channels  (process,  [zeroBiasSelection],              histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits3],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits4],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits5],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits6],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

#  add_channels  (process,  [zeroBiasJetSelection],              histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits3],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits4],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits5],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits6],  histSets,  weights,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
################################################################################
