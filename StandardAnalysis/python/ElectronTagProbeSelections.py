import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Electron tag and probe sample
##################################################
ZtoEleProbeTrk = cms.PSet(
    name = cms.string("ZtoEleProbeTrk"),
    triggers = triggersSingleEle,
    cuts = cms.VPSet (),
)

# See SMP-12-023 for example of W->mu nu selection
tagElectronCuts = [
    cutElectronPt24,
    cutElectronEta21,
    cutElectronTightID,
    #  cutElectronPFIso,  # Ask Bing what he uses for this
    cutElectronArbitration,
]
muTrkCuts = [
    cutEleTrkInvMass10,
    #cutEleTrkInvMass80To100,
]
addCuts(ZtoEleProbeTrk.cuts, tagElectronCuts)
addCuts(ZtoEleProbeTrk.cuts, [cutTrkPt30])
addCuts(ZtoEleProbeTrk.cuts, disTrkCuts)
addCuts(ZtoEleProbeTrk.cuts, muTrkCuts)
addCuts(ZtoEleProbeTrk.cuts, [cutTrkArbitration])
cutsToRemove = [
    cutTrkPt,
    cutTrkEcalo,
    cutTrkElecVeto,
    cutTrkTauVeto,
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
    cutTrkTauVeto,
]
addCuts(ZtoEleDisTrk.cuts, cutsToAdd)

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
