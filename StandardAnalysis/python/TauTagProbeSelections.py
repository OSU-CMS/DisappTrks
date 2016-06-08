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
