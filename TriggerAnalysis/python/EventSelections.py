import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.TriggerAnalysis.Cuts import *

# MET leg

METLegDenominator = cms.PSet(
    name = cms.string("METLegDenominator"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(
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
        cutMuonMatchHLTTrack,
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
        cutTrkMatchHLTTrack,
    )
)

TrackLegNumeratorWithTracks = copy.deepcopy(TrackLegDenominatorWithTracks)
TrackLegNumeratorWithTracks.name = cms.string("TrackLegNumeratorWithTracks")
addCuts(TrackLegNumeratorWithTracks.cuts, [passesMainTrigger])
