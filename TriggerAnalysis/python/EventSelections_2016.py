import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.TriggerAnalysis.Cuts import *

# MET leg

METLegDenominator = cms.PSet(
    name = cms.string("METLegDenominator"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutMuonPt25,
        cutMuonEta21,
        cutMuonTightID,
        cutMuonNMissIn,
        cutMuonNMissMid,
        cutMuonTightPFIso,
    )
)

METLegNumerator = copy.deepcopy(METLegDenominator)
METLegNumerator.name = cms.string("METLegNumerator")
addCuts(METLegNumerator.cuts, [passesHLTMet75])

# Track leg with muons

TrackLegDenominatorWithMuons = cms.PSet(
    name = cms.string("TrackLegDenominatorWithMuons"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesHLTMet75,
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
addCuts(TrackLegNumeratorWithMuons.cuts, [cutLeadMuonMatchHLTTrack, passesMainTrigger])

# Track leg with tracks

TrackLegDenominatorWithTracks = cms.PSet(
    name = cms.string("TrackLegDenominatorWithTracks"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesHLTMet75,
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
addCuts(TrackLegNumeratorWithTracks.cuts, [cutLeadTrkMatchHLTTrack, passesMainTrigger])

# Track leg with no singleMu triggers (for MC)

TrackLegDenominatorWithMuonsNoTrig = copy.deepcopy(TrackLegDenominatorWithMuons)
TrackLegDenominatorWithMuonsNoTrig.name = cms.string("TrackLegDenominatorWithMuonsNoTrig")
TrackLegDenominatorWithMuonsNoTrig.triggers = cms.vstring()

TrackLegNumeratorWithMuonsNoTrig = copy.deepcopy(TrackLegNumeratorWithMuons)
TrackLegNumeratorWithMuonsNoTrig.name = cms.string("TrackLegNumeratorWithMuonsNoTrig")
TrackLegNumeratorWithMuonsNoTrig.triggers = cms.vstring()

TrackLegDenominatorWithTracksNoTrig = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegDenominatorWithTracksNoTrig.name = cms.string("TrackLegDenominatorWithTracksNoTrig")
TrackLegDenominatorWithTracksNoTrig.triggers = cms.vstring()

TrackLegNumeratorWithTracksNoTrig = copy.deepcopy(TrackLegNumeratorWithTracks)
TrackLegNumeratorWithTracksNoTrig.name = cms.string("TrackLegNumeratorWithTracksNoTrig")
TrackLegNumeratorWithTracksNoTrig.triggers = cms.vstring()

# Track leg numerators with any muon/track matched to HLT track

TrackLegNumeratorWithMuonsAnyHLTMatch = copy.deepcopy(TrackLegNumeratorWithMuons)
TrackLegNumeratorWithMuonsAnyHLTMatch.name = cms.string("TrackLegNumeratorWithMuonsAnyHLTMatch")
removeCuts(TrackLegNumeratorWithMuonsAnyHLTMatch.cuts, [cutLeadMuonMatchHLTTrack])
addCuts(TrackLegNumeratorWithMuonsAnyHLTMatch.cuts, [cutAnyMuonMatchHLTTrack])

TrackLegNumeratorWithTracksAnyHLTMatch = copy.deepcopy(TrackLegNumeratorWithTracks)
TrackLegNumeratorWithTracksAnyHLTMatch.name = cms.string("TrackLegNumeratorWithTracksAnyHLTMatch")
removeCuts(TrackLegNumeratorWithTracksAnyHLTMatch.cuts, [cutLeadMuonMatchHLTTrack])
addCuts(TrackLegNumeratorWithTracksAnyHLTMatch.cuts, [cutAnyTrkMatchHLTTrack])
