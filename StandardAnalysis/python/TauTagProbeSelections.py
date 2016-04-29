import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
from DisappTrks.StandardAnalysis.MuonTagProbeSelections import *  # Get the composite cut definitions

################################################################################
## Tau tag and probe sample
################################################################################
ZtoTauIsoTrk = copy.deepcopy(MuonTagSkim)
ZtoTauIsoTrk.name = cms.string("ZtoTauIsoTrk")

muTrkCuts = [
    cutMuTrkInvMass10,
]
addCuts(ZtoTauIsoTrk.cuts, [cutMuonMT])
addCuts(ZtoTauIsoTrk.cuts, [cutMuonArbitration])
addCuts(ZtoTauIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoTauIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoTauIsoTrk.cuts, muTrkCuts)
cutsToRemove = [
    cutTrkPt,
]
removeCuts(ZtoTauIsoTrk.cuts, cutsToRemove)

ZtoTauProbeTrk = copy.deepcopy(ZtoTauIsoTrk)
ZtoTauProbeTrk.name = cms.string("ZtoTauProbeTrk")

cutsToAdd = [
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkNMissOut,
]
addCuts(ZtoTauProbeTrk.cuts, cutsToAdd)
addCuts(ZtoTauProbeTrk.cuts, [cutTrkArbitration])

ZtoTauProbeTrkWithZCuts = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkWithZCuts.name = cms.string("ZtoTauProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass40To75,
    cutMuTrkOS,
]
addCuts(ZtoTauProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoTauDisTrk = copy.deepcopy(ZtoTauProbeTrkWithZCuts)
ZtoTauDisTrk.name = cms.string("ZtoTauDisTrk")
cutsToAdd = [
    cutTrkTauHadVeto,
]
addCuts(ZtoTauDisTrk.cuts, cutsToAdd)

ZtoTauDisTrkWithECaloCut = copy.deepcopy(ZtoTauDisTrk)
ZtoTauDisTrkWithECaloCut.name = cms.string("ZtoTauDisTrkWithECaloCut")
cutsToAdd = [
    cutTrkEcalo,
]
addCuts(ZtoTauDisTrkWithECaloCut.cuts, cutsToAdd)

################################################################################
## Tau tag and probe sample -- no missing outer hits cut
################################################################################
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]

ZtoTauIsoTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauIsoTrk)
ZtoTauIsoTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauIsoTrkNoMissingOuterHitsCut")
removeCuts(ZtoTauIsoTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauProbeTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauProbeTrkNoMissingOuterHitsCut")
removeCuts(ZtoTauProbeTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut = copy.deepcopy(ZtoTauProbeTrkWithZCuts)
ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut.name = cms.string("ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut")
removeCuts(ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauDisTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauDisTrk)
ZtoTauDisTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauDisTrkNoMissingOuterHitsCut")
removeCuts(ZtoTauDisTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauDisTrkWithECaloCutNoMissingOuterHitsCut = copy.deepcopy(ZtoTauDisTrkWithECaloCut)
ZtoTauDisTrkWithECaloCutNoMissingOuterHitsCut.name = cms.string("ZtoTauDisTrkWithECaloCutNoMissingOuterHitsCut")
removeCuts(ZtoTauDisTrkWithECaloCutNoMissingOuterHitsCut.cuts, cutsToRemove)
