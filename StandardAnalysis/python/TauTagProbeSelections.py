import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Tau tag and probe sample
##################################################
ZtoTauProbeTrk = cms.PSet(
    name = cms.string("ZtoTauProbeTrk"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (),
)

# See SMP-12-023 for example of W->mu nu selection
tagMuonCuts = [
    cutMuonPt20,
    cutMuonEta21,
    cutMuonTightID,
    #  cutMuonPFIso,  # Ask Bing what he uses for this
    cutMuonMT,
    cutMuonArbitration,
]
muTrkCuts = [
    cutMuTrkInvMass10,
    #cutMuTrkInvMass80To100,
]
metTrkCuts = [
]
addCuts(ZtoTauProbeTrk.cuts, tagMuonCuts)
addCuts(ZtoTauProbeTrk.cuts, [cutTrkPt30])
addCuts(ZtoTauProbeTrk.cuts, disTrkCuts)
addCuts(ZtoTauProbeTrk.cuts, muTrkCuts)
addCuts(ZtoTauProbeTrk.cuts, [cutTrkArbitration])
cutsToRemove = [
    cutTrkPt,
    cutTrkEcalo,
    cutTrkTauVeto,
]
removeCuts(ZtoTauProbeTrk.cuts, cutsToRemove)

ZtoTauProbeTrkWithZCuts = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkWithZCuts.name = cms.string("ZtoTauProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
]
addCuts(ZtoTauProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoTauDisTrk = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauDisTrk.name = cms.string("ZtoTauDisTrk")
cutsToAdd = [
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
    cutTrkTauVeto,
]
addCuts(ZtoTauDisTrk.cuts, cutsToAdd)

ZtoTauProbeTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauProbeTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoTauProbeTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut = copy.deepcopy(ZtoTauProbeTrkWithZCuts)
ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut.name = cms.string("ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauDisTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauDisTrk)
ZtoTauDisTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauDisTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoTauDisTrkNoMissingOuterHitsCut.cuts, cutsToRemove)
