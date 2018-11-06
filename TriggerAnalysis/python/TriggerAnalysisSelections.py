import FWCore.ParameterSet.Config as cms
import copy
import re

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.TriggerAnalysis.AllTriggers import *
from DisappTrks.StandardAnalysis.EventSelections import *

##########################################################################################################
# MET leg denominator for all paths
##########################################################################################################

METLegDenominator = cms.PSet(
    name = cms.string("METLegDenominator"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutMuonPt,
        cutMuonEta21,
        cutMuonTightID,
        cutMuonNMissIn,
        cutMuonNMissMid,
        cutMuonTightPFIso,
    )
)

# Muon pt > 55 for the grand combination of triggers
GrandOrDenominator = cms.PSet(
    name = cms.string("METLegDenominator"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutMuonPt55,
        cutMuonEta21,
        cutMuonTightID,
        cutMuonNMissIn,
        cutMuonNMissMid,
        cutMuonTightPFIso,
    )
)

##########################################################################################################
# MET leg denominator for all paths using ZtoMuMu selection
##########################################################################################################

METLegDenominatorZtoMuMu = cms.PSet(
    name = cms.string("METLegDenominatorZtoMuMu"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutMuonPairPt, # this will be >22 for 76X and >26 for 80X
        cutMuonPairEta21,
        cutMuonPairTightID,
        cutMuonPairNMissIn,
        cutMuonPairNMissMid,
        cutMuonPairTightPFIso,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
    )
)

##########################################################################################################
# MET leg denominator for all paths using Tracks (instead of muons)
##########################################################################################################

METLegDenominatorTrk = cms.PSet(
    name = cms.string("METLegDenominatorTrk"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutTrkEta25,
        cutTrkNormalizedChi2,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNValidPixelHitsSignal,
        cutTrkNLayersWMeasurement,
        cutTrkNMissIn,
        cutTrkNMissMidNoDrop,
        cutTrkIsoTight,
    )
)

GrandOrDenominatorTrk = cms.PSet(
    name = cms.string("GrandOrDenominatorTrk"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(
        cutLeadJetCentral,
        cutTrkEta25,
        cutTrkNormalizedChi2,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNValidPixelHitsSignal,
        cutTrkNLayersWMeasurement,
        cutTrkNMissIn,
        cutTrkNMissMidNoDrop,
        cutTrkIsoTight,
    )
)


##########################################################################################################
# Numerator for the Grand Or of all signal HLT paths
##########################################################################################################

# Have to add the signal OR'd triggers as a cut rather than extend the triggers, since you need
# (IsoMu || IsoTkMu) && (MET75_IsoTrk50 || PFMET250 || ...)
GrandORNumerator = copy.deepcopy(GrandOrDenominator)
GrandORNumerator.name = cms.string("GrandOrNumerator")
addCuts(GrandORNumerator.cuts, [firesGrandOrTrigger])

# Now for the Track version of GrandORNumerator
GrandORNumeratorTrk = copy.deepcopy(GrandOrDenominatorTrk)
GrandORNumeratorTrk.name = cms.string("GrandOrNumeratorTrk")
addCuts(GrandORNumeratorTrk.cuts, [firesGrandOrTrigger])


##########################################################################################################
# MET leg numerators
##########################################################################################################

METLegNumerator = {}
for trig in triggerFiltersMet:
    METLegNumerator[trig] = copy.deepcopy(METLegDenominator)
    METLegNumerator[trig].name = cms.string(re.sub(r"_", "", trig) + "METLegNumerator")

    # if not IsoTrk50, just use the whole path
    if not trig in triggerFiltersTrack:
        addCuts(METLegNumerator[trig].cuts, [firesTrigger[trig]])
    # otherwise add all the filters for MET before IsoTrk50
    else:
        for filt in triggerFiltersMet[trig]:
            addCuts(METLegNumerator[trig].cuts, [firesFilter[filt]])

# Track version of METLegNumerator
METLegNumeratorTrk = {}
for trig in triggerFiltersMet:
    METLegNumeratorTrk[trig] = copy.deepcopy(METLegDenominatorTrk)
    METLegNumeratorTrk[trig].name = cms.string(re.sub(r"_", "", trig) + "METLegNumeratorTrk")

    # if not IsoTrk50, just use the whole path
    if not trig in triggerFiltersTrack:
        addCuts(METLegNumeratorTrk[trig].cuts, [firesTrigger[trig]])
    # otherwise add all the filters for MET before IsoTrk50
    else:
        for filt in triggerFiltersMet[trig]:
            addCuts(METLegNumeratorTrk[trig].cuts, [firesFilter[filt]])

# ZtoMuMu version
METLegNumeratorZtoMuMu = {}
for trig in triggerFiltersMet:
    METLegNumeratorZtoMuMu[trig] = copy.deepcopy(METLegDenominatorZtoMuMu)
    METLegNumeratorZtoMuMu[trig].name = cms.string(re.sub(r"_", "", trig) + "METLegNumeratorZtoMuMu")

    # if not IsoTrk50, just use the whole path
    if not trig in triggerFiltersTrack:
        addCuts(METLegNumeratorZtoMuMu[trig].cuts, [firesTrigger[trig]])
    # otherwise add all the filters for MET before IsoTrk50
    else:
        for filt in triggerFiltersMet[trig]:
            addCuts(METLegNumeratorZtoMuMu[trig].cuts, [firesFilter[filt]])

##########################################################################################################
# Track leg with muons (data)
##########################################################################################################

TrackLegDenominatorWithMuons = {}
for trig in triggerFiltersTrack:
    TrackLegDenominatorWithMuons[trig] = cms.PSet(
        name = cms.string(re.sub(r"_", "", trig) + "TrackLegDenominatorWithMuons"),
        triggers = triggersSingleMu,
        cuts = cms.VPSet(
            cutLeadJetCentral,
            cutMuonPt,
            cutMuonEta21,
            cutMuonTightID,
            cutMuonNMissIn,
            cutMuonNMissMid,
            cutMuonTightPFIso,
        )
    )
    for filt in triggerFiltersMet[trig]:
        addCuts(TrackLegDenominatorWithMuons[trig].cuts, [firesFilter[filt]])

TrackLegNumeratorWithMuons = {}
for trig in triggerFiltersTrack:
    TrackLegNumeratorWithMuons[trig] = copy.deepcopy(TrackLegDenominatorWithMuons[trig])
    TrackLegNumeratorWithMuons[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegNumeratorWithMuons")
    addCuts(TrackLegNumeratorWithMuons[trig].cuts, [cutLeadMuonMatchHLTTrack, firesTrigger[trig]])

# Track legs in data with a MET cut above the turn-on
if 'HLT_MET105_IsoTrk50_v' in TrackLegDenominatorWithMuons and 'HLT_MET105_IsoTrk50_v' in TrackLegNumeratorWithMuons:
    HLTMET105IsoTrk50DenWithMuonsMET275 = copy.deepcopy(TrackLegDenominatorWithMuons['HLT_MET105_IsoTrk50_v'])
    HLTMET105IsoTrk50DenWithMuonsMET275.name = cms.string("HLTMET105IsoTrk50DenWithMuonsMET275")
    addCuts(HLTMET105IsoTrk50DenWithMuonsMET275.cuts, [cutMet275])
 
    HLTMET105IsoTrk50NumWithMuonsMET275 = copy.deepcopy(TrackLegNumeratorWithMuons['HLT_MET105_IsoTrk50_v'])
    HLTMET105IsoTrk50NumWithMuonsMET275.name = cms.string("HLTMET105IsoTrk50NumWithMuonsMET275")
    addCuts(HLTMET105IsoTrk50NumWithMuonsMET275.cuts, [cutMet275])

if 'HLT_MET120_IsoTrk50_v' in TrackLegDenominatorWithMuons and 'HLT_MET120_IsoTrk50_v' in TrackLegNumeratorWithMuons:      
    HLTMET120IsoTrk50DenWithMuonsMET275 = copy.deepcopy(TrackLegDenominatorWithMuons['HLT_MET120_IsoTrk50_v'])
    HLTMET120IsoTrk50DenWithMuonsMET275.name = cms.string("HLTMET120IsoTrk50DenWithMuonsMET275")
    addCuts(HLTMET120IsoTrk50DenWithMuonsMET275.cuts, [cutMet275])
        
    HLTMET120IsoTrk50NumWithMuonsMET275 = copy.deepcopy(TrackLegNumeratorWithMuons['HLT_MET120_IsoTrk50_v'])
    HLTMET120IsoTrk50NumWithMuonsMET275.name = cms.string("HLTMET120IsoTrk50NumWithMuonsMET275")
    addCuts(HLTMET120IsoTrk50NumWithMuonsMET275.cuts, [cutMet275])

##########################################################################################################
# Track leg with tracks (MC)
##########################################################################################################

TrackLegDenominatorWithTracks = {}
for trig in triggerFiltersTrack:
    TrackLegDenominatorWithTracks[trig] = cms.PSet(
        name = cms.string(re.sub(r"_", "", trig) + "TrackLegDenominatorWithTracks"),
        triggers = cms.vstring(),
        cuts = cms.VPSet(
            cutLeadJetCentral,
            cutTrkEta25,
            cutTrkNormalizedChi2,
            cutTrkD0,
            cutTrkDZ,
            cutTrkNValidPixelHitsSignal,
            cutTrkNLayersWMeasurement,
            cutTrkNMissIn,
            cutTrkNMissMidNoDrop,
            cutTrkIsoTight,
        )
    )
    for filt in triggerFiltersMet[trig]:
        addCuts(TrackLegDenominatorWithTracks[trig].cuts, [firesFilter[filt]])

TrackLegNumeratorWithTracks = {}
for trig in triggerFiltersTrack:
    TrackLegNumeratorWithTracks[trig] = copy.deepcopy(TrackLegDenominatorWithTracks[trig])
    TrackLegNumeratorWithTracks[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegNumeratorWithTracks")
    addCuts(TrackLegNumeratorWithTracks[trig].cuts, [cutLeadTrkMatchHLTTrack, firesTrigger[trig]])

##########################################################################################################
# Track leg with ZtoMuMu selection
##########################################################################################################

TrackLegDenominatorZtoMuMu = {}
for trig in triggerFiltersTrack:
    TrackLegDenominatorZtoMuMu[trig] = cms.PSet(
        name = cms.string(re.sub(r"_", "", trig) + "TrackLegDenominatorZtoMuMu"),
        triggers = triggersSingleMu,
        cuts = cms.VPSet(
            cutLeadJetCentral,
            cutMuonPairPt, # this will be >22 for 76X and >26 for 80X
            cutMuonPairEta21,
            cutMuonPairTightID,
            cutMuonPairNMissIn,
            cutMuonPairNMissMid,
            cutMuonPairTightPFIso,
            cutMuMuChargeProduct,
            cutMuMuInvMassZLo,
            cutMuMuInvMassZHi,
        )
    )
    for filt in triggerFiltersMet[trig]:
        addCuts(TrackLegDenominatorZtoMuMu[trig].cuts, [firesFilter[filt]])

TrackLegNumeratorZtoMuMu = {}
for trig in triggerFiltersTrack:
    TrackLegNumeratorZtoMuMu[trig] = copy.deepcopy(TrackLegDenominatorZtoMuMu[trig])
    TrackLegNumeratorZtoMuMu[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegNumeratorZtoMuMu")
    addCuts(TrackLegNumeratorZtoMuMu[trig].cuts, [cutAnyMuonMatchHLTTrack, firesTrigger[trig]])

##########################################################################################################
# Track leg with no SingleMu triggers (MC)
##########################################################################################################

TrackLegDenominatorWithMuonsNoTrig = {}
for trig in TrackLegDenominatorWithMuons:
    TrackLegDenominatorWithMuonsNoTrig[trig] = copy.deepcopy(TrackLegDenominatorWithMuons[trig])
    TrackLegDenominatorWithMuonsNoTrig[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegDenominatorWithMuonsNoTrig")
    TrackLegDenominatorWithMuonsNoTrig[trig].triggers = cms.vstring()

TrackLegNumeratorWithMuonsNoTrig = {}
for trig in TrackLegNumeratorWithMuons:
    TrackLegNumeratorWithMuonsNoTrig[trig] = copy.deepcopy(TrackLegNumeratorWithMuons[trig])
    TrackLegNumeratorWithMuonsNoTrig[trig].name = cms.string(re.sub(r"_", "", trig) + "_rackLegNumeratorWithMuonsNoTrig")
    TrackLegNumeratorWithMuonsNoTrig[trig].triggers = cms.vstring()

TrackLegDenominatorWithTracksNoTrig = {}
for trig in TrackLegDenominatorWithTracks:
    TrackLegDenominatorWithTracksNoTrig[trig] = copy.deepcopy(TrackLegDenominatorWithTracks[trig])
    TrackLegDenominatorWithTracksNoTrig[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegDenominatorWithTracksNoTrig")
    TrackLegDenominatorWithTracksNoTrig[trig].triggers = cms.vstring()

TrackLegNumeratorWithTracksNoTrig = {}
for trig in TrackLegNumeratorWithTracks:
    TrackLegNumeratorWithTracksNoTrig[trig] = copy.deepcopy(TrackLegNumeratorWithTracks[trig])
    TrackLegNumeratorWithTracksNoTrig[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegNumeratorWithTracksNoTrig")
    TrackLegNumeratorWithTracksNoTrig[trig].triggers = cms.vstring()

##########################################################################################################
# Track leg with any muon/track matched to HLT track (rather than only the leading one) (testing)
##########################################################################################################

TrackLegDenominatorWithTracksAnyHLTMatch = {}
for trig in TrackLegDenominatorWithTracks:
    TrackLegDenominatorWithTracksAnyHLTMatch[trig] = copy.deepcopy(TrackLegDenominatorWithTracks[trig])
    TrackLegDenominatorWithTracksAnyHLTMatch[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegDenominatorWithTracksAnyHLTMatch")
    removeCuts(TrackLegDenominatorWithTracksAnyHLTMatch[trig].cuts, [cutLeadMuonMatchHLTTrack])
    addCuts(TrackLegDenominatorWithTracksAnyHLTMatch[trig].cuts, [cutAnyMuonMatchHLTTrack])

TrackLegNumeratorWithTracksAnyHLTMatch = {}
for trig in TrackLegNumeratorWithTracks:
    TrackLegNumeratorWithTracksAnyHLTMatch[trig] = copy.deepcopy(TrackLegNumeratorWithTracks[trig])
    TrackLegNumeratorWithTracksAnyHLTMatch[trig].name = cms.string(re.sub(r"_", "", trig) + "TrackLegNumeratorWithTracksAnyHLTMatch")
    removeCuts(TrackLegNumeratorWithTracksAnyHLTMatch[trig].cuts, [cutLeadMuonMatchHLTTrack])
    addCuts(TrackLegNumeratorWithTracksAnyHLTMatch[trig].cuts, [cutAnyMuonMatchHLTTrack])

##########################################################################################################
# HLT purity channels for IsoTrk50 paths
##########################################################################################################

basicSelectionOnlyMET75IsoTrk50 = copy.deepcopy(basicSelection)
basicSelectionOnlyMET75IsoTrk50.name = cms.string("BasicSelectionOnlyMET75IsoTrk50")
basicSelectionOnlyMET75IsoTrk50.triggers = cms.vstring("HLT_MET75_IsoTrk50_v")

basicSelectionOnlyMET90IsoTrk50 = copy.deepcopy(basicSelection)
basicSelectionOnlyMET90IsoTrk50.name = cms.string("BasicSelectionOnlyMET90IsoTrk50")
basicSelectionOnlyMET90IsoTrk50.triggers = cms.vstring("HLT_MET90_IsoTrk50_v")

basicSelectionOnlyMET75IsoTrk50HltMet105 = copy.deepcopy(basicSelection)
basicSelectionOnlyMET75IsoTrk50HltMet105.name = cms.string("BasicSelectionOnlyMET75IsoTrk50Met105")
basicSelectionOnlyMET75IsoTrk50HltMet105.triggers = cms.vstring("HLT_MET75_IsoTrk50_v")
basicSelectionOnlyMET75IsoTrk50HltMet105.cuts.insert(0, cutHltMet105)

basicSelectionOnlyMET90IsoTrk50HltMet105 = copy.deepcopy(basicSelection)
basicSelectionOnlyMET90IsoTrk50HltMet105.name = cms.string("BasicSelectionOnlyMET90IsoTrk50Met105")
basicSelectionOnlyMET90IsoTrk50HltMet105.triggers = cms.vstring("HLT_MET90_IsoTrk50_v")
basicSelectionOnlyMET90IsoTrk50HltMet105.cuts.insert(0, cutHltMet105)

isoTrkSelectionOnlyMET75IsoTrk50 = copy.deepcopy(isoTrkSelection)
isoTrkSelectionOnlyMET75IsoTrk50.name = cms.string("IsoTrkSelectionOnlyMET75IsoTrk50")
isoTrkSelectionOnlyMET75IsoTrk50.triggers = cms.vstring("HLT_MET75_IsoTrk50_v")

isoTrkSelectionOnlyMET90IsoTrk50 = copy.deepcopy(isoTrkSelection)
isoTrkSelectionOnlyMET90IsoTrk50.name = cms.string("IsoTrkSelectionOnlyMET90IsoTrk50")
isoTrkSelectionOnlyMET90IsoTrk50.triggers = cms.vstring("HLT_MET90_IsoTrk50_v")

isoTrkSelectionOnlyMET75IsoTrk50HltMet105 = copy.deepcopy(isoTrkSelection)
isoTrkSelectionOnlyMET75IsoTrk50HltMet105.name = cms.string("IsoTrkSelectionOnlyMET75IsoTrk50HltMet105")
isoTrkSelectionOnlyMET75IsoTrk50HltMet105.triggers = cms.vstring("HLT_MET75_IsoTrk50_v")
isoTrkSelectionOnlyMET75IsoTrk50HltMet105.cuts.insert(0, cutHltMet105)

isoTrkSelectionOnlyMET90IsoTrk50HltMet105 = copy.deepcopy(isoTrkSelection)
isoTrkSelectionOnlyMET90IsoTrk50HltMet105.name = cms.string("IsoTrkSelectionOnlyMET90IsoTrk50HltMet105")
isoTrkSelectionOnlyMET90IsoTrk50HltMet105.triggers = cms.vstring("HLT_MET90_IsoTrk50_v")
isoTrkSelectionOnlyMET90IsoTrk50HltMet105.cuts.insert(0, cutHltMet105)

##########################################################################################################
# ARC question testing channels
##########################################################################################################

if 'HLT_MET105_IsoTrk50_v' in triggerFiltersMet:
    from DisappTrks.BackgroundEstimation.MuonTagProbeSelections import *
    
    MuonTagPt55HLTMetFilters = copy.deepcopy(MuonTagPt55)
    MuonTagPt55HLTMetFilters.name = cms.string("MuonTagPt55HLTMetFilters")
    for filt in triggerFiltersMet['HLT_MET105_IsoTrk50_v']:
        addCuts(MuonTagPt55HLTMetFilters.cuts, [firesFilter[filt]])
    
    MuonTagPt55HLTMetFiltersAndSignalPath = copy.deepcopy(MuonTagPt55HLTMetFilters)
    MuonTagPt55HLTMetFiltersAndSignalPath.name = cms.string("MuonTagPt55HLTMetFiltersAndSignalPath")
    addCuts(MuonTagPt55HLTMetFiltersAndSignalPath.cuts, [firesTrigger['HLT_MET105_IsoTrk50_v']])
