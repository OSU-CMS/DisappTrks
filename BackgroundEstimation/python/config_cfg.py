from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleElectron channels
################################################################################
# Base skim
#  add_channels  (process,  [ElectronTagSkim],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for fiducial map
#  add_channels  (process,  [ElectronFiducialCalcBefore],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronFiducialCalcAfter],   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)

# Tag-and-probe channels for electron background estimate
#  add_channels  (process,  [ZtoEleProbeTrkWithZCuts],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleDisTrk],             histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCuts],              histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrk],                         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsBetterPurity],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkBetterPurity],             histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  True)

# Single electron control regions
#  add_channels  (process,  [ElectronTagPt55],         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronTagPt55MetTrig],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collectionMap,  variableProducers,  False)

# Testing for fake track systematic investigation
#  add_channels  (process,  [ZtoEleProbeTrkWithZCutsNoValidHitsCut],      histSetsElectron,  scaleFactorProducersWithElectrons,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleDisTrkNoValidHitsCut],                 histSetsElectron,  scaleFactorProducersWithElectrons,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut], histSetsElectron,  scaleFactorProducersWithElectrons,  scaleFactorProducers,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkNoValidHitsCut],            histSetsElectron,  scaleFactorProducersWithElectrons,  scaleFactorProducers,  collectionMap,  variableProducers,  False)

################################################################################

################################################################################
# SingleMuon channels
################################################################################
# Base skim and ZtoMuMu
#  add_channels  (process,  [MuonTagSkim],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for fiducial map
#  add_channels  (process,  [MuonFiducialCalcBefore],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [MuonFiducialCalcAfter],   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# Tag-and-probe channels for muon background estimate
#  add_channels  (process,  [ZtoMuProbeTrkWithZCuts],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuDisTrk],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCuts],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrk],                         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsBetterPurity],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkBetterPurity],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)

# Single muon control regions
#  add_channels  (process,  [MuonTagPt55],         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt55MetTrig],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# Z->mumu channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMu],                        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuCandTrk],                 histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrk],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with no D0 requirement on the isoTrk
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with inverted D0 requirement on the isoTrk
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with loosened D0 requirement on the isoTrk
#  add_channels  (process,  [ZtoMuMuDisTrkSidebandD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu+jet channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMuJet],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkJet],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu+jet channels for fake track background estimate with one jet and ==16 PV
#  add_channels  (process,  [ZtoMuMuOneJet14to18PV],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers, False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: W->munu for fake track background estimate
#  add_channels  (process,  [WtoMuNu],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: W->munu for fake track background estimate with one jet and ==16 PV
#  add_channels  (process,  [WtoMuNuOneJet14to18PV],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

# TESTING: Z->mumu channels with relaxed missing outer hits requirements
#  add_channels  (process,  [ZtoMuMuDisTrk2],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  True)

# Testing for fake track systematic investigation
#  add_channels  (process,  [ZtoMuProbeTrkWithZCutsNoValidHitsCut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuDisTrkNoValidHitsCut],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkNoValidHitsCut],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collectionMap,  variableProducers,  False)

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

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
