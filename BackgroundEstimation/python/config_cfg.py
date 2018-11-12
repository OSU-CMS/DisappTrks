from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################

# Descendents of BasicSelection

# Fake track background: BasicNhits (N = 3 for transfer factor)
if False:
    add_channels  (process,  [disTrkSelectionNoD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionNoD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionNoD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionNoD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers)

# Fake track background: DisTrkInvertD0(Nhits3-6)
if False:
    add_channels  (process,  [disTrkSelectionSidebandD0Cut],        histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers)

# Testing: similar to sideband above, but without upper D0 cut
# fakeTrackBackground_invertD0Cut
if False:
    add_channels  (process,  [disTrkSelectionInvertD0Cut],        histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers)

################################################################################
# SingleElectron channels
################################################################################

# Base skim
if False:
    add_channels  (process,  [ElectronTagSkim],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Tag-and-probe channels for fiducial map
if False:
    add_channels  (process,  [ElectronFiducialCalcBefore],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
    add_channels  (process,  [ElectronFiducialCalcAfter],   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Tag-and-probe channels for electron background estimate
if False:
    add_channels  (process,  [ZtoEleProbeTrk],                   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, ignoreSkimmedCollections = True)
    add_channels  (process,  [ZtoEleProbeTrkWithFilter],         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, ignoreSkimmedCollections = True)
    add_channels  (process,  [ZtoEleProbeTrkWithSSFilter],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, ignoreSkimmedCollections = True)

# Single electron control regions for background estimate
if False:
    add_channels  (process,  [ElectronTagPt55],         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronMETTriggerProducer, ignoreSkimmedCollections = True)
    add_channels  (process,  [ElectronTagPt55MetTrig],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Tag-and-probe channels for tau background estimate
if False:
    add_channels  (process,  [ZtoTauToEleProbeTrk],                       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
    add_channels  (process,  [ZtoTauToEleProbeTrkWithFilter],             histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
    add_channels  (process,  [ZtoTauToEleProbeTrkWithSSFilter],           histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)

# Tag-and-probe channels for older background estimate; 
#  add_channels  (process,  [ZtoEleProbeTrkBeforeArbitration],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleProbeTrkWithZCuts],          histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleDisTrk],                     histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Tag-and-probe channels for older tau background estimate
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCuts],              histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleDisTrk],                         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsBetterPurity],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleDisTrkBetterPurity],             histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Z->ee control region
#  add_channels  (process,  [ZtoEE],                           histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0Cut],              histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits3],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits4],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits5],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits6],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0Cut],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits3],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits4],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits5],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits6],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Channels for doing the lepton background estimates with fewer numbers of hits
#  add_channels  (process,  [ElectronTagPt55NoValidHitsCut],               histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ElectronTagPt55MetTrigNoValidHitsCut],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleProbeTrkWithZCutsNoValidHitsCut],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

#  add_channels  (process,  [ZtoEleDisTrkNHits3],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleDisTrkNHits4],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleDisTrkNHits5],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleDisTrkNHits6],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits3],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits4],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits5],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits6],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# Tag-and-probe channels without d0 cut on probe track
#  add_channels  (process,  [ZtoEleProbeTrkWithoutD0Cut],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithoutD0Cut],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, ignoreSkimmedCollections = True)

# TESTING: investigate region of probe track inefficiency in ElectronFiducialCalcAfter eta-phi region
#  add_channels  (process, [ElectronFiducialCalcBeforeInvestigate2017Ineff], histSetsElectron, histSetsElectron, scaleFactorProducersWithElectrons, collMap, variableProducers, ignoreSkimmedCollections = True)

################################################################################

################################################################################
# SingleMuon channels
################################################################################
# Base skim and ZtoMuMu
if False:
    add_channels  (process,  [MuonTagSkim],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Tag-and-probe channels for fiducial map
if False:
    add_channels  (process,  [MuonFiducialCalcBefore],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [MuonFiducialCalcAfter],   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Tag-and-probe channels for muon background estimate
if False:
    add_channels  (process,  [ZtoMuProbeTrk],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
    add_channels  (process,  [ZtoMuProbeTrkWithFilter],         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
    add_channels  (process,  [ZtoMuProbeTrkWithSSFilter],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)

# Single muon control regions for muon background estimate
if False:
    add_channels  (process,  [MuonTagPt55],         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonMETTriggerProducer)
    add_channels  (process,  [MuonTagPt55MetTrig],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Tag-and-probe channels for tau background estimate
if False:
    add_channels  (process,  [ZtoTauToMuProbeTrk],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
    add_channels  (process,  [ZtoTauToMuProbeTrkWithFilter],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
    add_channels  (process,  [ZtoTauToMuProbeTrkWithSSFilter],           histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)

# Tag-and-probe channels for older muon background estimate
#  add_channels  (process,  [ZtoMuDummyTrk],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
#  add_channels  (process,  [ZtoMuDummyTrkWithJetFilter],      histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
#  add_channels  (process,  [ZtoMuProbeTrkBeforeArbitration],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuProbeTrkWithZCuts],          histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuDisTrk],                     histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Tag-and-probe channels for older tau background estimate
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCuts],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuDisTrk],                         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsBetterPurity],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuDisTrkBetterPurity],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)


# Z->mumu channels for fake track background estimate
if False:
    add_channels  (process,  [ZtoMuMu],                        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

if False:
    add_channels  (process,  [ZtoMuMuCandTrk],                 histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrk],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNHits3],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNHits4],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNHits5],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNHits6],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: Z->mumu channels for fake track background estimate with no D0 requirement on the isoTrk
if False:
    add_channels  (process,  [ZtoMuMuDisTrkNoD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: Z->mumu channels for fake track background estimate with loosened D0 requirement on the isoTrk
if False:
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: Z->mumu channels for fake track background estimate with inverted D0 requirement on the isoTrk
if False:
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: Z->mumu channels for fake track background estimate with no Iso cut nor ECal cut
if False:
    add_channels  (process,  [ZtoMuMuCandTrkNoIso],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNoIsoNoCalo],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
if False:
    add_channels  (process,  [ZtoMuMuDisTrkNHits3NoIsoNoCalo],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNHits4NoIsoNoCalo],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
if False:
    add_channels  (process,  [ZtoMuMuDisTrkNHits5NoIsoNoCalo],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
    add_channels  (process,  [ZtoMuMuDisTrkNHits6NoIsoNoCalo],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)


# TESTING: Z->mumu+jet channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMuJet],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrkJet],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: W->munu for fake track background estimate
#  add_channels  (process,  [WtoMuNu],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [WtoMuNuDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [WtoMuNuDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [WtoMuNuDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [WtoMuNuDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [WtoMuNuDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: Z->mumu channels with relaxed missing outer hits requirements
#  add_channels  (process,  [ZtoMuMuDisTrk2],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Channels for doing the lepton background estimates with fewer numbers of hits
#  add_channels  (process,  [MuonTagPt55NoValidHitsCut],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [MuonTagPt55MetTrigNoValidHitsCut],           histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuProbeTrkWithZCutsNoValidHitsCut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

#  add_channels  (process,  [ZtoMuDisTrkNHits3],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuDisTrkNHits4],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuDisTrkNHits5],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoMuDisTrkNHits6],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# Tag-and-probe channels without d0 cut on probe track
#  add_channels  (process,  [ZtoMuProbeTrkWithoutD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithoutD0Cut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers)

# TESTING: investigate region of probe track inefficiency in MuonFiducialCalcBefore eta-phi region
#  add_channels  (process, [MuonFiducialCalcBeforeInvestigate2017Ineff], histSetsMuon, weightsWithMuonSF, scaleFactorProducersWithMuons, collMap, variableProducers)

################################################################################

################################################################################
# Tau channels
################################################################################
# Base skim
if False:
    add_channels  (process,  [TauTagSkim],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers)

# Single tau control regions for tau background estimate
if False:
    add_channels  (process,  [TauTagPt55],         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers + tauMETTriggerProducer)
    add_channels  (process,  [TauTagPt55MetTrig],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers)

# Channels for doing the lepton background estimates with fewer numbers of hits
#  add_channels  (process,  [TauTagPt55NoValidHitsCut],         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [TauTagPt55MetTrigNoValidHitsCut],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers)
################################################################################

################################################################################
# ZeroBias channels
################################################################################
#  add_channels  (process,  [zeroBiasSelection],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits3],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits4],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits5],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits6],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)

#  add_channels  (process,  [zeroBiasJetSelection],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits3],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits4],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits5],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits6],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers)
################################################################################

################################################################################
# Testing channels to compare pat::IsolatedTracks to CandidateTracks
################################################################################
#  add_channels  (process,  [MinimalMuonTrackSelection],                 cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers)
#  add_channels  (process,  [MinimalMuonMatchedCandidateTrackSelection], cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers)

#  add_channels  (process,  [MinimalEleTrackSelection],                  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers)
#  add_channels  (process,  [MinimalEleMatchedCandidateTrackSelection],  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers)

#  add_channels  (process,  [MinimalTauTrackSelection],                  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers)
#  add_channels  (process,  [MinimalTauMatchedCandidateTrackSelection],  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
    
