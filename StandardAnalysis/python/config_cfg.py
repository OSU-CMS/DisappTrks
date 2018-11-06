from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# Dummy channels
################################################################################
#  add_channels  (process,  [NoCuts],  histSets,  weights,  [],  collMap,  variableProducers,  False)
################################################################################

################################################################################
# MET channels
################################################################################
# Channel requiring only MET
#  add_channels  (process,  [metMinimalSkim],  histSetsMetJet,  weights,  [],  collMap,  variableProducers,  True)

# Channels needed for background estimates and systematics
#  add_channels  (process,  [vertexCutOnly],                 histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionNoAngularCuts],   histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionNoDijetPhiCut],   histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionNoJetMetPhiCut],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelection],                histSets,  weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkSelectionNHits3],         histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits4],         histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits5],         histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits6],         histSets,  weights,  [],  collMap,  variableProducers,  False)

# Channels requiring MET+jet+track
#  add_channels  (process,  [nonIsoTrkSelection],             histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [isoTrkSelection],                histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [isoTrkSelectionInvertDRJetCut],  histSets,      weights,  [],  collMap,  variableProducers,  True)
#  add_channels  (process,  [isoTrkSelectionBeforeIsoCut],    histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkSelection],               histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [elecCtrlSelection],              histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelection],              histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [tauCtrlSelection],               histSets,      weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelectionWithMatch],     histSetsMuon,  weights,  [],  collMap,  variableProducers,  False)

# Variations of the disappearing tracks search region
#  add_channels  (process,  [disTrkIdElec],             histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdMuon],             histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdTau],              histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdFake],             histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOut],         histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoEcalo],            histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOutNoEcalo],  histSets,  weights,  [],  collMap,  variableProducers,  False)

# THE disappearing tracks search region
#  add_channels  (process,  [disTrkSelection],                    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoTrigger],                    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMainTrigger],              histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionCharginoChargino],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionCharginoNeutralino],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [charginoChargino],                   histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [charginoNeutralino],                 histSets,  weights,  [],  collMap,  variableProducers,  False)
################################################################################

################################################################################
## Testing channels
################################################################################

#  add_channels  (process,  [disTrkSelectionNoD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkSelectionInvertD0Cut],        histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkSelectionSidebandD0Cut],        histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAChargino],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAHighPtChargino],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAVertex],          histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justTriggers],         histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrk],          histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits3],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits4],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits5],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits6],    histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAFakeTrk],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justARealTrk],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAFakeTrkNoD0Cut],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justARealTrkNoD0Cut],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkNoTrigger],                    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMainTrigger],              histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMET90Trigger],             histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMainTriggerHltMet105],     histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMET90TriggerHltMet105],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNoD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkSelectionInvertD0Cut],        histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionInvertD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkSelectionSidebandD0Cut],        histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSidebandD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAFakeTrkWithNoCuts],   histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkWithNoCuts],   histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justACharginoWithNoCuts],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAChargino],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAHighPtChargino],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAVertex],          histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justTriggers],         histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrk],          histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits3],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits4],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits5],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits6],    histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAFakeTrk],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justARealTrk],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justAFakeTrkNoD0Cut],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNoD0CutNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [justARealTrkNoD0Cut],        histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits3],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits4],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits5],  histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justARealTrkNoD0CutNHits6],  histSets,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [disTrkNoTrigger],                    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMainTrigger],              histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMET90Trigger],             histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMainTriggerHltMet105],     histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkJustMET90TriggerHltMet105],    histSets,  weights,  [],  collMap,  variableProducers,  False)

################################################################################
# Testing channels to compare pat::IsolatedTracks to CandidateTracks
################################################################################
#  add_channels  (process,  [MinimalMETTrackSelection],                 cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)
#  add_channels  (process,  [MinimalMETMatchedCandidateTrackSelection], cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
    
