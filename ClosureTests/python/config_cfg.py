from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################
#  add_channels  (process,  [candTrkIdElecPt35],       histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkIdElecPt35NoMet],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [candTrkIdMuPt35],       histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkIdMuPt35NoMet],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [candTrkIdTauPt55],       histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkIdTauPt55NoMet],  histSets,  weights,  [],  collMap,  variableProducers,  False)

################################################################################
# SingleElectron channels
################################################################################
#  add_channels  (process,  [ZtoEleProbeTrkNLayers4],                   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleProbeTrkNLayers5],                   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleProbeTrkNLayers6plus],                   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoEleProbeTrkWithZCuts],          histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleDisTrkNoNMissOutCut],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronTagPt35NoJetCuts],         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronTagPt35NoJetCutsMetTrig],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)

#  add_channels  (process,  [ZtoTauToEleProbeTrkNLayers4],             histSetsElectron, weightsWithEleSF, scaleFactorProducersWithElectrons, collMap, variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkNLayers5],             histSetsElectron, weightsWithEleSF, scaleFactorProducersWithElectrons, collMap, variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkNLayers6plus],             histSetsElectron, weightsWithEleSF, scaleFactorProducersWithElectrons, collMap, variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCuts],    histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkNoNMissOutCut],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)

################################################################################
# SingleMuon channels
################################################################################
#  add_channels  (process,  [ZtoMuProbeTrkNLayers4],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
#  add_channels  (process,  [ZtoMuProbeTrkNLayers5],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
#  add_channels  (process,  [ZtoMuProbeTrkNLayers6plus],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer)
#  add_channels  (process,  [ZtoMuProbeTrkWithZCuts],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuDisTrkNoNMissOutCut],     histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt35NoJetCuts],         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt35NoJetCutsMetTrig],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

#  add_channels  (process,  [ZtoTauToMuProbeTrkNLayers4],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
#  add_channels  (process,  [ZtoTauToMuProbeTrkNLayers5],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
#  add_channels  (process,  [ZtoTauToMuProbeTrkNLayers6plus],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCuts],    histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkNoNMissOutCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

################################################################################
# Tau channels
################################################################################
#  add_channels  (process,  [TauTagPt55NoJetCuts],         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [TauTagPt55NoJetCutsMetTrig],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

process.EventJetVarProducer.triggerNames = triggerNamesInclusive

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
    
