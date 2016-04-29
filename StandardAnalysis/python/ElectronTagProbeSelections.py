import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Electron tag skim
##################################################
ElectronTagSkim = cms.PSet(
    name = cms.string("ElectronTagSkim"),
    triggers = triggersSingleEle,
    cuts = cms.VPSet (),
)
tagElectronCuts = [
    cutElectronPt25,
    cutElectronEta21,
    cutElectronTightID,
    cutElectronTightPFIso,
]
addCuts(ElectronTagSkim.cuts, tagElectronCuts)

################################################################################
## Electron tag and probe sample
################################################################################
ZtoEleIsoTrk = copy.deepcopy(ElectronTagSkim)
ZtoEleIsoTrk.name = cms.string("ZtoEleIsoTrk")

eleTrkCuts = [
    cutMuTrkInvMass10,
]
addCuts(ZtoEleIsoTrk.cuts, [cutElectronArbitration])
addCuts(ZtoEleIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoEleIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoEleIsoTrk.cuts, eleTrkCuts)
cutsToRemove = [
    cutTrkPt,
]
removeCuts(ZtoEleIsoTrk.cuts, cutsToRemove)

ZtoEleProbeTrk = copy.deepcopy(ZtoEleIsoTrk)
ZtoEleProbeTrk.name = cms.string("ZtoEleProbeTrk")

cutsToAdd = [
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
    cutTrkNMissOut,
]
addCuts(ZtoEleProbeTrk.cuts, cutsToAdd)
addCuts(ZtoEleProbeTrk.cuts, [cutTrkArbitration])

ZtoEleProbeTrkWithZCuts = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleDisTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
cutsToAdd = [
    cutTrkElecVeto,
]
addCuts(ZtoEleDisTrk.cuts, cutsToAdd)

ZtoEleDisTrkWithECaloCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkWithECaloCut.name = cms.string("ZtoEleDisTrkWithECaloCut")
cutsToAdd = [
    cutTrkEcalo,
]
addCuts(ZtoEleDisTrkWithECaloCut.cuts, cutsToAdd)

################################################################################
## Electron tag and probe sample -- no missing outer hits cut
################################################################################
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]

ZtoEleIsoTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoEleIsoTrk)
ZtoEleIsoTrkNoMissingOuterHitsCut.name = cms.string("ZtoEleIsoTrkNoMissingOuterHitsCut")
removeCuts(ZtoEleIsoTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleProbeTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkNoMissingOuterHitsCut.name = cms.string("ZtoEleProbeTrkNoMissingOuterHitsCut")
removeCuts(ZtoEleProbeTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut.name = cms.string("ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut")
removeCuts(ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleDisTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoMissingOuterHitsCut.name = cms.string("ZtoEleDisTrkNoMissingOuterHitsCut")
removeCuts(ZtoEleDisTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut = copy.deepcopy(ZtoEleDisTrkWithECaloCut)
ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut.name = cms.string("ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut")
removeCuts(ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut.cuts, cutsToRemove)
