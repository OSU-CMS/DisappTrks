import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file

# MET leg

METLegDenominator = cms.PSet(
    name = cms.string("METLegDenominator"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutMuonPt, # this will be >22 for 76X and >26 for 80X
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

MET90LegNumerator = copy.deepcopy(METLegDenominator)
MET90LegNumerator.name = cms.string("MET90LegNumerator")
addCuts(MET90LegNumerator.cuts, [passesHLTMet90])

# Track leg with muons

TrackLegDenominatorWithMuons = cms.PSet(
    name = cms.string("TrackLegDenominatorWithMuons"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesHLTMet75,
        cutMuonPt,
        cutMuonEta21,
        cutMuonTightID,
        cutMuonNMissIn,
        cutMuonNMissMid,
        cutMuonTightPFIso,
    )
)

TrackLegDenominatorWithMuonsMet90 = cms.PSet(
    name = cms.string("TrackLegDenominatorWithMuonsMet90"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesHLTMet90,
        cutMuonPt,
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

TrackLegNumeratorWithMuonsMet90 = copy.deepcopy(TrackLegDenominatorWithMuonsMet90)
TrackLegNumeratorWithMuonsMet90.name = cms.string("TrackLegNumeratorWithMuonsMet90")
addCuts(TrackLegNumeratorWithMuonsMet90.cuts, [cutLeadMuonMatchHLTTrack, passesHigherMetTrigger])

# Track leg with tracks

TrackLegDenominatorWithTracks = cms.PSet(
    name = cms.string("TrackLegDenominatorWithTracks"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesHLTMet75,
        cutTrkEta25,
        cutTrkNormalizedChi2,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNValidPixelHits,
        cutTrkNLayersWMeasurement,
        cutTrkNMissIn,
        cutTrkNMissMid,
        cutTrkIsoTight,
    )
)

TrackLegDenominatorWithTracksMet90 = cms.PSet(
    name = cms.string("TrackLegDenominatorWithTracksMet90"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        passesHLTMet90,
        cutTrkEta25,
        cutTrkNormalizedChi2,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNValidPixelHits,
        cutTrkNLayersWMeasurement,
        cutTrkNMissIn,
        cutTrkNMissMid,
        cutTrkIsoTight,
    )
)

TrackLegNumeratorWithTracks = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegNumeratorWithTracks.name = cms.string("TrackLegNumeratorWithTracks")
addCuts(TrackLegNumeratorWithTracks.cuts, [cutLeadTrkMatchHLTTrack, passesMainTrigger])

TrackLegNumeratorWithTracksMet90 = copy.deepcopy(TrackLegDenominatorWithTracksMet90)
TrackLegNumeratorWithTracksMet90.name = cms.string("TrackLegNumeratorWithTracksMet90")
addCuts(TrackLegNumeratorWithTracksMet90.cuts, [cutLeadTrkMatchHLTTrack, passesHigherMetTrigger])

# Track leg with no singleMu triggers (for MC)

TrackLegDenominatorWithMuonsNoTrig = copy.deepcopy(TrackLegDenominatorWithMuons)
TrackLegDenominatorWithMuonsNoTrig.name = cms.string("TrackLegDenominatorWithMuonsNoTrig")
TrackLegDenominatorWithMuonsNoTrig.triggers = cms.vstring()

TrackLegDenominatorWithMuonsNoTrigMet90 = copy.deepcopy(TrackLegDenominatorWithMuonsMet90)
TrackLegDenominatorWithMuonsNoTrigMet90.name = cms.string("TrackLegDenominatorWithMuonsNoTrigMet90")
TrackLegDenominatorWithMuonsNoTrigMet90.triggers = cms.vstring()

TrackLegNumeratorWithMuonsNoTrig = copy.deepcopy(TrackLegNumeratorWithMuons)
TrackLegNumeratorWithMuonsNoTrig.name = cms.string("TrackLegNumeratorWithMuonsNoTrig")
TrackLegNumeratorWithMuonsNoTrig.triggers = cms.vstring()

TrackLegNumeratorWithMuonsNoTrigMet90 = copy.deepcopy(TrackLegNumeratorWithMuonsMet90)
TrackLegNumeratorWithMuonsNoTrigMet90.name = cms.string("TrackLegNumeratorWithMuonsNoTrigMet90")
TrackLegNumeratorWithMuonsNoTrigMet90.triggers = cms.vstring()

TrackLegDenominatorWithTracksNoTrig = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegDenominatorWithTracksNoTrig.name = cms.string("TrackLegDenominatorWithTracksNoTrig")
TrackLegDenominatorWithTracksNoTrig.triggers = cms.vstring()

TrackLegDenominatorWithTracksNoTrigMet90 = copy.deepcopy(TrackLegDenominatorWithTracksMet90)
TrackLegDenominatorWithTracksNoTrigMet90.name = cms.string("TrackLegDenominatorWithTracksNoTrigMet90")
TrackLegDenominatorWithTracksNoTrigMet90.triggers = cms.vstring()

TrackLegNumeratorWithTracksNoTrig = copy.deepcopy(TrackLegNumeratorWithTracks)
TrackLegNumeratorWithTracksNoTrig.name = cms.string("TrackLegNumeratorWithTracksNoTrig")
TrackLegNumeratorWithTracksNoTrig.triggers = cms.vstring()

TrackLegNumeratorWithTracksNoTrigMet90 = copy.deepcopy(TrackLegNumeratorWithTracksMet90)
TrackLegNumeratorWithTracksNoTrigMet90.name = cms.string("TrackLegNumeratorWithTracksNoTrigMet90")
TrackLegNumeratorWithTracksNoTrigMet90.triggers = cms.vstring()

# Track leg numerators with any muon/track matched to HLT track

TrackLegNumeratorWithMuonsAnyHLTMatch = copy.deepcopy(TrackLegNumeratorWithMuons)
TrackLegNumeratorWithMuonsAnyHLTMatch.name = cms.string("TrackLegNumeratorWithMuonsAnyHLTMatch")
removeCuts(TrackLegNumeratorWithMuonsAnyHLTMatch.cuts, [cutLeadMuonMatchHLTTrack])
addCuts(TrackLegNumeratorWithMuonsAnyHLTMatch.cuts, [cutAnyMuonMatchHLTTrack])

TrackLegNumeratorWithMuonsAnyHLTMatchMet90 = copy.deepcopy(TrackLegNumeratorWithMuonsMet90)
TrackLegNumeratorWithMuonsAnyHLTMatchMet90.name = cms.string("TrackLegNumeratorWithMuonsAnyHLTMatchMet90")
removeCuts(TrackLegNumeratorWithMuonsAnyHLTMatchMet90.cuts, [cutLeadMuonMatchHLTTrack])
addCuts(TrackLegNumeratorWithMuonsAnyHLTMatchMet90.cuts, [cutAnyMuonMatchHLTTrack])

TrackLegNumeratorWithTracksAnyHLTMatch = copy.deepcopy(TrackLegNumeratorWithTracks)
TrackLegNumeratorWithTracksAnyHLTMatch.name = cms.string("TrackLegNumeratorWithTracksAnyHLTMatch")
removeCuts(TrackLegNumeratorWithTracksAnyHLTMatch.cuts, [cutLeadMuonMatchHLTTrack])
addCuts(TrackLegNumeratorWithTracksAnyHLTMatch.cuts, [cutAnyTrkMatchHLTTrack])

TrackLegNumeratorWithTracksAnyHLTMatchMet90 = copy.deepcopy(TrackLegNumeratorWithTracksMet90)
TrackLegNumeratorWithTracksAnyHLTMatchMet90.name = cms.string("TrackLegNumeratorWithTracksAnyHLTMatchMet90")
removeCuts(TrackLegNumeratorWithTracksAnyHLTMatchMet90.cuts, [cutLeadMuonMatchHLTTrack])
addCuts(TrackLegNumeratorWithTracksAnyHLTMatchMet90.cuts, [cutAnyTrkMatchHLTTrack])
