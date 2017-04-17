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
    metFilters = metFilters,
    cuts = cms.VPSet (),
)
tagElectronCuts = [
    cutMetFilters,
    cutElectronPt25,
    cutElectronEta21,
    cutElectronTightID,
    cutElectronTightPFIso,
]
addCuts(ElectronTagSkim.cuts, tagElectronCuts)

##################################################
## Higher pt to be closer to candidate track selection
##################################################
ElectronTagPt35 = copy.deepcopy(ElectronTagSkim)
ElectronTagPt35.name = cms.string("ElectronTagPt35")
addSingleCut(ElectronTagPt35.cuts, cutElectronPt35, cutElectronPt25)
removeCuts(ElectronTagPt35.cuts, [cutElectronPt25])
cutsToAdd = [
    cutElectronArbitration,
]
cutsToAdd += jetCuts
cutsToAdd += [
    cutTrkPt35,
    cutTrkElecDR0p1,
    cutTrkMatchRecoElec,
]
cutsToAdd += isoTrkCuts
addCuts(ElectronTagPt35.cuts, cutsToAdd)

ElectronTagPt35NoTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoTrig.name = cms.string("ElectronTagPt35NoTrig")
ElectronTagPt35NoTrig.triggers = cms.vstring()

ElectronTagPt35MetTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetTrig.name = cms.string("ElectronTagPt35MetTrig")
ElectronTagPt35MetTrig.triggers = triggersMet

ElectronTagPt35MetCut = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetCut.name = cms.string("ElectronTagPt35MetCut")
addCuts(ElectronTagPt35MetCut.cuts, [cutElectronMetMinusOne])

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
ElectronTagPt55 = copy.deepcopy(ElectronTagPt35)
ElectronTagPt55.name = cms.string("ElectronTagPt55")
addSingleCut(ElectronTagPt55.cuts, cutTrkPt55, cutTrkPt35)
removeCuts(ElectronTagPt55.cuts, [cutTrkPt35])

ElectronTagPt55NoTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55NoTrig.name = cms.string("ElectronTagPt55NoTrig")
ElectronTagPt55NoTrig.triggers = cms.vstring()

ElectronTagPt55MetTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetTrig.name = cms.string("ElectronTagPt55MetTrig")
ElectronTagPt55MetTrig.triggers = triggersMet

ElectronTagPt55MetCut = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetCut.name = cms.string("ElectronTagPt55MetCut")
addCuts(ElectronTagPt55MetCut.cuts, [cutElectronMetMinusOne])

################################################################################
## Electron tag and probe sample
################################################################################
ZtoEleProbeTrkWithZCuts = copy.deepcopy(ElectronTagSkim)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutElectronArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutEleTrkInvMass10,
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
    cutTrkArbitration,
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ElectronFiducialCalcBefore = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ElectronFiducialCalcBefore.name = cms.string("ElectronFiducialCalcBefore")
removeCuts(ElectronFiducialCalcBefore.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

ElectronFiducialCalcAfter = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ElectronFiducialCalcAfter.name = cms.string("ElectronFiducialCalcAfter")
addSingleCut(ElectronFiducialCalcAfter.cuts, cutTrkVetoElecVeto, cutEleTrkOS)
removeCuts(ElectronFiducialCalcAfter.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

ZtoEleDisTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
addSingleCut(ZtoEleDisTrk.cuts, cutTrkNMissOut, cutEleTrkOS)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkEcalo,    cutEleTrkOS)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkElecVeto, cutEleTrkOS)

ZtoEleProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoEleProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoEleProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoEleDisTrkNoValidHitsCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoValidHitsCut.name = cms.string("ZtoEleDisTrkNoValidHitsCut")
removeCuts(ZtoEleDisTrkNoValidHitsCut.cuts, [cutTrkNValidHits])

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
