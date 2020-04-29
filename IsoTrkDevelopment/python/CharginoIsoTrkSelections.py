import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

################################################################################
## Muon Gun skim
################################################################################

charginoMatchedCut = [
    cutCharginoMatched,
]

charginoValidationCut = [
    cutCharginoFromPV,
    cutCharginodxy,
    cutCharginodz,
    cutCharginopt,
    cutCharginoIsLooseTrack,
    cutCharginoIsTightTrack,
    cutCharginoIsHighPurityTrack,
    cutCharginoLowCaloDR05NoPU,
    cutCharginoInclusive,
]

isotrkValidationCut = [
    cutIsoTrkFromPV,
    cutIsoTrkdxy,
    cutIsoTrkdz,
    cutIsoTrkpt,
    cutIsLooseTrack,
    cutIsTightTrack,
    cutIsHighPurityTrack,
    cutIsoTrkLowCaloDR05NoPU,
    cutIsoTrkInclusive,
]
CharginoMatchedSkim = cms.PSet(
    name = cms.string("CharginoMatchedSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (),
)

addCuts(CharginoMatchedSkim.cuts, charginoMatchedCut)
addCuts(CharginoMatchedSkim.cuts, charginoValidationCut)

IsoTrkSkim = cms.PSet(
    name = cms.string("IsoTrkSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (),
)

addCuts(IsoTrkSkim.cuts, isotrkValidationCut)
