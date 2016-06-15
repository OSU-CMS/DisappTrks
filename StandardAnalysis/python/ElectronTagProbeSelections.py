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
addSingleCut(ElectronTagPt35.cuts,  cutElectronPt35, cutElectronPt25)
removeCuts  (ElectronTagPt35.cuts, [cutElectronPt25])  
addCuts     (ElectronTagPt35.cuts, [cutTrkPt35])
addCuts     (ElectronTagPt35.cuts,  candTrkCuts)
removeCuts  (ElectronTagPt35.cuts, [cutTrkPt]) 
removeCuts  (ElectronTagPt35.cuts, [cutTrkElecVeto])  
addCuts     (ElectronTagPt35.cuts, [cutTrkMatchRecoElec])

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
addCuts(ZtoEleIsoTrk.cuts, [cutTrkPt35])  
# addCuts(ZtoEleIsoTrk.cuts, [cutTrkPt30])  # original 
addCuts(ZtoEleIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoEleIsoTrk.cuts, eleTrkCuts)
cutsToRemove = [
    cutTrkPt,
]
removeCuts(ZtoEleIsoTrk.cuts, cutsToRemove)

ZtoEleProbeTrk = copy.deepcopy(ZtoEleIsoTrk)
ZtoEleProbeTrk.name = cms.string("ZtoEleProbeTrk")
# Add cuts in reverse order
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkTauHadVeto, cutTrkJetDeltaPhi) 
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkMuonVeto,   cutTrkJetDeltaPhi) 
# addCuts(ZtoEleProbeTrk.cuts, [cutTrkArbitration])  #FIXME:  Is this needed?  


ZtoEleProbeTrkWithZCuts = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleDisTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
# Add cuts in reverse order
addSingleCut(ZtoEleDisTrk.cuts, cutTrkEcalo,    cutTrkTauHadVeto) 
addSingleCut(ZtoEleDisTrk.cuts, cutTrkElecVeto, cutTrkTauHadVeto)

