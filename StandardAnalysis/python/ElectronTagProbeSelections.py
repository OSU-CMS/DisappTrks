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

##################################################
## Electron tag and probe sample
##################################################
ZtoEleProbeTrk = copy.deepcopy(ElectronTagSkim)
ZtoEleProbeTrk.name = cms.string("ZtoEleProbeTrk")

elTrkCuts = [
    cutEleTrkInvMass10,
    #cutEleTrkInvMass80To100,
]
addCuts(ZtoEleProbeTrk.cuts, [cutElectronArbitration])
addCuts(ZtoEleProbeTrk.cuts, [cutTrkPt30])
addCuts(ZtoEleProbeTrk.cuts, disTrkCuts)
addCuts(ZtoEleProbeTrk.cuts, elTrkCuts)
addCuts(ZtoEleProbeTrk.cuts, [cutTrkArbitration])
cutsToRemove = [
    cutTrkPt,
    cutTrkEcalo,
    cutTrkElecVeto,
]
removeCuts(ZtoEleProbeTrk.cuts, cutsToRemove)

ZtoEleProbeTrkWithZCuts = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleDisTrk = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
cutsToAdd = [
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
    cutTrkElecVeto,
]
addCuts(ZtoEleDisTrk.cuts, cutsToAdd)

ZtoEleDisTrkWithECaloCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkWithECaloCut.name = cms.string("ZtoEleDisTrkWithECaloCut")
cutsToAdd = [
    cutTrkEcalo,
]
addCuts(ZtoEleDisTrkWithECaloCut.cuts, cutsToAdd)

##################################################
## Electron tag and probe sample with missing outer hits cut removed
##################################################
ZtoEleProbeTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkNoMissingOuterHitsCut.name = cms.string("ZtoEleProbeTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoEleProbeTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut.name = cms.string("ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoEleProbeTrkWithZCutsNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleDisTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoMissingOuterHitsCut.name = cms.string("ZtoEleDisTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoEleDisTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut = copy.deepcopy(ZtoEleDisTrkWithECaloCut)
ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut.name = cms.string("ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoEleDisTrkWithECaloCutNoMissingOuterHitsCut.cuts, cutsToRemove)
