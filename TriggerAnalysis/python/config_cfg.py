from DisappTrks.StandardAnalysis.protoConfig_cfg import *

def getNHitsVariations (chName, hitRange = range(3, 8), checkBlinding = False):
    if checkBlinding:
        signalRequirement = 4 if (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")) else 7
        hitRange = [x for x in hitRange if x < signalRequirement]
    names = {x : int(x[5]) for x in cutTrkNValidHitsVariations if int(x[5]) in hitRange} # "NHits5"[5] = 5
    return [globals ()[chName + x] for x in names]

def getNLayersChannelVariations (chName):
    return [globals()[chName + x] for x in ['NLayers4', 'NLayers5', 'NLayers6plus']]

variableProducers.append('EventTriggerVarProducer')

################################################################################
# Data and W+Jets MC channels
################################################################################

# MET legs
#  add_channels  (process,  [METLegDenominator],                    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  METLegNumerator.values(),               histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
# HLT_MET*_IsoTrk50 track legs
#  add_channels  (process,  TrackLegDenominatorWithMuons.values(),  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegNumeratorWithMuons.values(),    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# The Grand Or
#  add_channels  (process,  [GrandOrDenominator],  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [GrandOrNumerator],    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# Testing: require a match of any muon to the HLT track rather than just the lead muon
#  add_channels  (process,  TrackLegNumeratorWithMuonsAnyHLTMatch.values(),  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# Testing: ZtoMuMu selection
#  add_channels  (process,  [METLegDenominatorZtoMuMu],           histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  METLegNumeratorZtoMuMu.values(),      histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegDenominatorZtoMuMu.values(),  histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  TrackLegNumeratorZtoMuMu.values(),    histSetsTrigger,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

################################################################################
# Signal MC channels (using tracks instead of muons)
################################################################################

# MET legs with tracks
if False:
    add_channels(process,  getNLayersChannelVariations("METLegDenominatorTrk"),                        histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
    add_channels(process,  getNLayersChannelVariations("HLTMET105IsoTrk50vMETLegNumeratorTrk"), histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
    add_channels(process,  getNLayersChannelVariations("HLTMET120IsoTrk50vMETLegNumeratorTrk"), histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
# Track legs with tracks
if False:
    add_channels(process,  getNLayersChannelVariations("HLTMET105IsoTrk50vTrackLegNumeratorWithTracks"),   histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
    add_channels(process,  getNLayersChannelVariations("HLTMET120IsoTrk50vTrackLegNumeratorWithTracks"),   histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
    add_channels(process,  getNLayersChannelVariations("HLTMET105IsoTrk50vTrackLegDenominatorWithTracks"), histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
    add_channels(process,  getNLayersChannelVariations("HLTMET120IsoTrk50vTrackLegDenominatorWithTracks"), histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# The Grand Or with tracks
if False:
    add_channels(process,  getNLayersChannelVariations("GrandOrDenominatorTrk"),  histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
    add_channels(process,  getNLayersChannelVariations("GrandOrNumeratorTrk"),    histSetsTrigger,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

################################################################################
# HLT purity measurement channels -- BasicSelection but only with one HLT path
################################################################################

#  add_channels  (process,  [basicSelectionOnlyMET75IsoTrk50],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionOnlyMET90IsoTrk50],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)

#  add_channels  (process,  [basicSelectionOnlyMET75IsoTrk50HltMet105],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [basicSelectionOnlyMET90IsoTrk50HltMet105],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)

################################################################################

#  add_channels  (process,  [justMET75IsoTrk50],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [justMET90IsoTrk50],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)

################################################################################
# ARC question testing channels
################################################################################

#  add_channels  (process,  [MuonTagPt55HLTMetFilters],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt55HLTMetFiltersAndSignalPath],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)

################################################################################
# Test channels
################################################################################

#  add_channels  (process,  [HLTMET105IsoTrk50DenWithMuonsMET275],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [HLTMET120IsoTrk50DenWithMuonsMET275],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [HLTMET105IsoTrk50NumWithMuonsMET275],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [HLTMET120IsoTrk50NumWithMuonsMET275],  histSetsTrigger,  weights,  [],  collMap,  variableProducers,  False)

################################################################################
# ARC question testing channels
################################################################################

#  add_channels  (process,  [MuonTagPt55HLTMetFilters],  histSetsTrigger,  weights,  [],  collectionMap,  variableProducers,  False)

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print
    print 'You haven\'t added any channels. There\'s nothing to do!'
    print
    sys.exit(0)

if hasattr(process, 'EventTriggerVarProducer'):
	process.EventTriggerVarProducer.triggerNames = triggerNamesInclusive
	process.EventTriggerVarProducer.filterNames = triggerFiltersInclusive
	process.EventTriggerVarProducer.signalTriggerNames = triggersMet

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
    
