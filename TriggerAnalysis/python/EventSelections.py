import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.TriggerAnalysis.Cuts import *

# MET leg

METLegDenominator = cms.PSet(
    name = cms.string("METLegDenominator"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(
        dummyCut,
        cutLeadJetCentral,
    )
)

METLegNumerator = copy.deepcopy(METLegDenominator)
METLegNumerator.name = cms.string("METLegNumerator")
addCuts(METLegNumerator.cuts, [passesTriggerFilter])

# Track leg with muons

TrackLegDenominatorWithMuons = cms.PSet(
    name = cms.string("TrackLegDenominatorWithMuons"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesTriggerFilter,
        cutMuonPt25,
        cutMuonEta21,
        cutMuonTightID,
        cutMuonNMissIn,
        cutMuonNMissMid,
        cutMuonTightPFIso,
    )
)

TrackLegNumeratorWithMuons = copy.deepcopy(TrackLegDenominatorWithMuons)
TrackLegNumeratorWithMuons.name = cms.string("TrackLegNumeratorWithMuons")
addCuts(TrackLegNumeratorWithMuons.cuts, [passesMainTrigger])

# Track leg with tracks

TrackLegDenominatorWithTracks = cms.PSet(
    name = cms.string("TrackLegDenominatorWithTracks"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesTriggerFilter,
        cutTrkEta,
        cutTrkNormalizedChi2,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNValidPixelHits,
        cutTrkNLayersWMeasurement,
        cutTrkNMissIn,
        cutTrkNMissMid,
        cutTrkIso,
    )
)

TrackLegNumeratorWithTracks = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegNumeratorWithTracks.name = cms.string("TrackLegNumeratorWithTracks")
addCuts(TrackLegNumeratorWithTracks.cuts, [passesMainTrigger])

# Track leg with lead muon/track matched to HLT track

TrackLegDenominatorWithMuonsLeadHLTMatch = copy.deepcopy(TrackLegDenominatorWithMuons)
TrackLegDenominatorWithMuonsLeadHLTMatch.name = cms.string("TrackLegDenominatorWithMuonsLeadHLTMatch")
addCuts(TrackLegDenominatorWithMuonsLeadHLTMatch, [cutLeadMuonMatchHLTTrack])

TrackLegNumeratorWithMuonsLeadHLTMatch = copy.deepcopy(TrackLegNumeratorWithMuons)
TrackLegNumeratorWithMuonsLeadHLTMatch.name = cms.string("TrackLegNumeratorWithMuonsLeadHLTMatch")
addCuts(TrackLegNumeratorWithMuonsLeadHLTMatch, [cutLeadMuonMatchHLTTrack])

TrackLegDenominatorWithTracksLeadHLTMatch = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegDenominatorWithTracksLeadHLTMatch.name = cms.string("TrackLegDenominatorWithTracksLeadHLTMatch")
addCuts(TrackLegDenominatorWithTracksLeadHLTMatch, [cutLeadTrkMatchHLTTrack])

TrackLegNumeratorWithTracksLeadHLTMatch = copy.deepcopy(TrackLegNumeratorWithTracks)
TrackLegNumeratorWithTracksLeadHLTMatch.name = cms.string("TrackLegNumeratorWithTracksLeadHLTMatch")
addCuts(TrackLegNumeratorWithTracksLeadHLTMatch, [cutLeadTrkMatchHLTTrack])

# Track leg with any muon/track matched to HLT track

TrackLegDenominatorWithMuonsAnyHLTMatch = copy.deepcopy(TrackLegDenominatorWithMuons)
TrackLegDenominatorWithMuonsAnyHLTMatch.name = cms.string("TrackLegDenominatorWithMuonsAnyHLTMatch")
addCuts(TrackLegDenominatorWithMuonsAnyHLTMatch, [cutAnyMuonMatchHLTTrack])

TrackLegNumeratorWithMuonsAnyHLTMatch = copy.deepcopy(TrackLegNumeratorWithMuons)
TrackLegNumeratorWithMuonsAnyHLTMatch.name = cms.string("TrackLegNumeratorWithMuonsAnyHLTMatch")
addCuts(TrackLegNumeratorWithMuonsAnyHLTMatch, [cutAnyMuonMatchHLTTrack])

TrackLegDenominatorWithTracksAnyHLTMatch = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegDenominatorWithTracksAnyHLTMatch.name = cms.string("TrackLegDenominatorWithTracksAnyHLTMatch")
addCuts(TrackLegDenominatorWithTracksAnyHLTMatch, [cutAnyTrkMatchHLTTrack])

TrackLegNumeratorWithTracksAnyHLTMatch = copy.deepcopy(TrackLegNumeratorWithTracks)
TrackLegNumeratorWithTracksAnyHLTMatch.name = cms.string("TrackLegNumeratorWithTracksAnyHLTMatch")
addCuts(TrackLegNumeratorWithTracksAnyHLTMatch, [cutAnyTrkMatchHLTTrack])
