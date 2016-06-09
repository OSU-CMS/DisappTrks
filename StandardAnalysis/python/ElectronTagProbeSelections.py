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
## Higher pt to be closer to candidate track selection
##################################################
ElectronTagPt35 = copy.deepcopy(ElectronTagSkim)
ElectronTagPt35.name = cms.string("ElectronTagPt35")
addSingleCut(ElectronTagPt35.cuts, cutElectronPt35, cutElectronPt25)
cutsToAdd = [ 
    cutTrkPt35, 
    cutTrkMatchRecoElec, 
]
addCuts(ElectronTagPt35.cuts, cutsToAdd)  
cutsToRemove = [
    cutElectronPt25, 
    ]
removeCuts(ElectronTagPt35.cuts, cutsToRemove)  

ElectronTagPt35NoTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoTrig.name = cms.string("ElectronTagPt35NoTrig")
ElectronTagPt35NoTrig.triggers = cms.vstring() 

ElectronTagPt35MetTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetTrig.name = cms.string("ElectronTagPt35MetTrig")
ElectronTagPt35MetTrig.triggers = triggersMet 

ElectronTagPt35MetCut = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetCut.name = cms.string("ElectronTagPt35MetCut")
cutsToAdd = [ 
    cutElectronMetMinusOne, 
]
addCuts(ElectronTagPt35MetCut.cuts, cutsToAdd)  


################################################################################
## Electron tag and probe sample
################################################################################
ZtoEleIsoTrk = copy.deepcopy(ElectronTagSkim)
ZtoEleIsoTrk.name = cms.string("ZtoEleIsoTrk")

eleTrkCuts = [
    cutEleTrkInvMass10,
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
