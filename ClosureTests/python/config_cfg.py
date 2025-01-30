from DisappTrks.StandardAnalysis.protoConfig_cfg import *

def getNLayersChannelVariations (chName):
    return [globals()[chName + x] for x in ['NLayers4', 'NLayers5', 'NLayers6plus']]

################################################################################
# MET channels
################################################################################
#  add_channels  (process,  [candTrkIdElecPt35],       histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkIdElecPt35NoMet],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [candTrkIdMuPt35],       histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkIdMuPt35NoMet],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [candTrkIdTauPt55],       histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkIdTauPt55NoMet],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  getNLayersChannelVariations("candTrkIdElecPt35"),       histSets,  weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  getNLayersChannelVariations("candTrkIdMuPt35"),       histSets,  weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  getNLayersChannelVariations("candTrkIdTauPt55"),       histSets,  weights,  [],  collMap,  variableProducers,  True)

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

# add_channels  (process,  getNLayersChannelVariations("ZtoEleProbeTrk"),   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoEleProbeTrkWithFilter"),   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoEleProbeTrkWithSSFilter"), histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer, True)

#  add_channels  (process,  getNLayersChannelVariations("ElectronTagPt35NoJetCuts"),         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  getNLayersChannelVariations("ElectronTagPt35NoJetCutsMetTrig"),  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)

#  add_channels  (process,  [ZtoTauToEleProbeTrkNLayers4],             histSetsElectron, weightsWithEleSF, scaleFactorProducersWithElectrons, collMap, variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkNLayers5],             histSetsElectron, weightsWithEleSF, scaleFactorProducersWithElectrons, collMap, variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkNLayers6plus],             histSetsElectron, weightsWithEleSF, scaleFactorProducersWithElectrons, collMap, variableProducers + tauToElectronTPProducer, ignoreSkimmedCollections = True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCuts],    histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleDisTrkNoNMissOutCut],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)

#  add_channels  (process,  getNLayersChannelVariations("ZtoTauToEleProbeTrk"),   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoTauToEleProbeTrkWithFilter"),   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoTauToEleProbeTrkWithSSFilter"), histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer, True)

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

#  add_channels  (process,  getNLayersChannelVariations("ZtoMuProbeTrk"),                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoMuProbeTrkWithFilter"),         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoMuProbeTrkWithSSFilter"),       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer, True)

#  add_channels  (process,  getNLayersChannelVariations("MuonTagPt35NoJetCuts"),         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  getNLayersChannelVariations("MuonTagPt35NoJetCutsMetTrig"),  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

#  add_channels  (process,  [ZtoTauToMuProbeTrkNLayers4],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
#  add_channels  (process,  [ZtoTauToMuProbeTrkNLayers5],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
#  add_channels  (process,  [ZtoTauToMuProbeTrkNLayers6plus],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCuts],    histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuDisTrkNoNMissOutCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

#  add_channels  (process,  getNLayersChannelVariations("ZtoTauToMuProbeTrk"),                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoTauToMuProbeTrkWithFilter"),         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer, True)
#  add_channels  (process,  getNLayersChannelVariations("ZtoTauToMuProbeTrkWithSSFilter"),       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer, True)

################################################################################
# Tau channels
################################################################################
#  add_channels  (process,  [TauTagPt55NoJetCuts],         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [TauTagPt55NoJetCutsMetTrig],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  getNLayersChannelVariations("TauTagPt55NoJetCuts"),         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  True)
#  add_channels  (process,  getNLayersChannelVariations("TauTagPt55NoJetCutsMetTrig"),  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  True)

################################################################################
# Fake tracks channels
################################################################################
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNLayers4],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers, True)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNLayers5],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers, True)
#  add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNLayers6plus],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers, True)
#  add_channels  (process,  [ZtoMuMu],                        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers, True)
#  add_channels  (process,  [disTrkIdFakeNLayers4],             histSets,  weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkIdFakeNLayers5],             histSets,  weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkIdFakeNLayers6plus],             histSets,  weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  [basicSelection],                histSets,  weights,  [],  collMap,  variableProducers,  True)

################################################################################
# Lepton SFs testing channels
################################################################################
#  add_channels  (process,  [ElectronTagSkim],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers, False)
#  add_channels  (process,  [MuonTagSkim],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers, False)

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print()
    print('You haven\'t added any channels. There\'s nothing to do!')
    print()
    sys.exit(0)
    
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
    
