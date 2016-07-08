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
    cutElectronArbitration,
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutTrkPt35,
    cutTrkElecDR0p1,
    cutTrkMatchRecoElec,
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
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

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
ElectronTagPt50 = copy.deepcopy(ElectronTagPt35)
ElectronTagPt50.name = cms.string("ElectronTagPt50")
addSingleCut(ElectronTagPt50.cuts, cutTrkPt, cutTrkPt35)
cutsToAdd = [
    #cutTrkEcalo,
    #cutTrkNMissOut,
    cutTrkNMissOutInv
]
addCuts(ElectronTagPt50.cuts, cutsToAdd)
cutsToRemove = [
    cutTrkPt35,
]
removeCuts(ElectronTagPt50.cuts, cutsToRemove)

ElectronTagPt50NoTrig = copy.deepcopy(ElectronTagPt50)
ElectronTagPt50NoTrig.name = cms.string("ElectronTagPt50NoTrig")
ElectronTagPt50NoTrig.triggers = cms.vstring() 

ElectronTagPt50MetTrig = copy.deepcopy(ElectronTagPt50)
ElectronTagPt50MetTrig.name = cms.string("ElectronTagPt50MetTrig")
ElectronTagPt50MetTrig.triggers = triggersMet 

ElectronTagPt50MetCut = copy.deepcopy(ElectronTagPt50)
ElectronTagPt50MetCut.name = cms.string("ElectronTagPt50MetCut")
cutsToAdd = [ 
    cutElectronMetMinusOne, 
]
addCuts(ElectronTagPt50MetCut.cuts, cutsToAdd)  


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
addSingleCut(ZtoEleIsoTrk.cuts, cutTrkNMissOut, cutTrkNMissMid) 
cutsToRemove = [
    cutTrkPt,
]
removeCuts(ZtoEleIsoTrk.cuts, cutsToRemove)

ZtoEleProbeTrk = copy.deepcopy(ZtoEleIsoTrk)
ZtoEleProbeTrk.name = cms.string("ZtoEleProbeTrk")
# Add cuts in reverse order
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkArbitration, cutEleTrkInvMass10) 
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkTauHadVeto, cutEleTrkInvMass10) 
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkMuonVeto,   cutEleTrkInvMass10) 


ZtoEleProbeTrkWithZCuts = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleCandTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleCandTrk.name = cms.string("ZtoEleCandTrk")
addSingleCut(ZtoEleCandTrk.cuts, cutTrkElecVeto, cutEleTrkOS)

ZtoEleDisTrk = copy.deepcopy(ZtoEleCandTrk)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
#addSingleCut(ZtoEleDisTrk.cuts, cutTrkNMissOut, cutTrkElecVeto)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkEcalo,    cutTrkElecVeto) 

ZtoEleDisTrkNoNMissOut = copy.deepcopy(ZtoEleDisTrk) 
ZtoEleDisTrkNoNMissOut.name = cms.string("ZtoEleDisTrkNoNMissOut") 
removeCuts(ZtoEleDisTrkNoNMissOut.cuts, [cutTrkNMissOut])  

ZtoEleCandTrkSdbandEcalo = copy.deepcopy(ZtoEleCandTrk) 
ZtoEleCandTrkSdbandEcalo.name = cms.string("ZtoEleCandTrkSdbandEcalo")
addSingleCut(ZtoEleCandTrkSdbandEcalo.cuts, cutTrkEcaloInv, cutTrkElecVeto)
addSingleCut(ZtoEleCandTrkSdbandEcalo.cuts, cutTrkNMissOut, cutTrkElecVeto)

ZtoEleCandTrkSdbandNMissOut = copy.deepcopy(ZtoEleCandTrk) 
ZtoEleCandTrkSdbandNMissOut.name = cms.string("ZtoEleCandTrkSdbandNMissOut")
addSingleCut(ZtoEleCandTrkSdbandNMissOut.cuts, cutTrkNMissOutInv, cutTrkElecVeto) 
addSingleCut(ZtoEleCandTrkSdbandNMissOut.cuts, cutTrkEcalo,       cutTrkElecVeto) 



