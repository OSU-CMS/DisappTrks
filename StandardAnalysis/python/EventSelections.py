import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file 


##########################################################################
##### Preselection #####
##########################################################################

basicSelection = cms.PSet(
    name = cms.string("BasicSelection"),
    triggers = triggersMet, 
    cuts = cms.VPSet (
        cutGoodPV,
        cutMet,
        cutJetPt,
        cutJetChgHad,
        cutJetChgEm,
        cutJetNeuHad, 
        cutJetNeuEm,
    )
)

##########################################################################

isoTrkSelection = copy.deepcopy(basicSelection) 
isoTrkSelection.name = cms.string("IsoTrkSelection") 
cutsToAdd = [ 
        cutTrkPt, 
        cutTrkEta,
        cutTrkEcalGapVeto,
        cutTrkEtaMuonIneff1, 
        cutTrkEtaMuonIneff2, 
        cutTrkNValidHits,
        cutTrkNMissIn,
        cutTrkNMissMid, 
        cutTrkIso, 
]
addCuts(isoTrkSelection.cuts, cutsToAdd)

##########################################################################

candTrkSelection = copy.deepcopy(isoTrkSelection) 
candTrkSelection.name = cms.string("DisTrkSelection") 
cutsToAdd = [ 
    cutTrkElecVeto, 
    cutTrkMuonVeto, 
    cutTrkTauVeto, 
]
addCuts(candTrkSelection.cuts, cutsToAdd)

##########################################################################

disTrkSelection = copy.deepcopy(candTrkSelection) 
disTrkSelection.name = cms.string("DisTrkSelection") 
cutsToAdd = [ 
    cutTrkEcalo, 
    cutTrkNMissOut, 
]
addCuts(disTrkSelection.cuts, cutsToAdd)

##########################################################################

elecCtrlSelection = copy.deepcopy(candTrkSelection) 
elecCtrlSelection.name = cms.string("ElecCtrlSelection") 
cutsToRemove = [ 
    cutTrkElecVeto, 
]
removeCuts(elecCtrlSelection.cuts, cutsToRemove)

##########################################################################

muonCtrlSelection = copy.deepcopy(candTrkSelection) 
muonCtrlSelection.name = cms.string("MuonCtrlSelection") 
cutsToRemove = [ 
    cutTrkMuonVeto, 
]
removeCuts(muonCtrlSelection.cuts, cutsToRemove)

##########################################################################

tauCtrlSelection = copy.deepcopy(candTrkSelection) 
tauCtrlSelection.name = cms.string("TauCtrlSelection") 
cutsToRemove = [ 
    cutTrkTauVeto, 
]
removeCuts(tauCtrlSelection.cuts, cutsToRemove)

##########################################################################

caloSdbandSelection = copy.deepcopy(disTrkSelection) 
caloSdbandSelection.name = cms.string("CaloSdbandSelection") 
cutsToRemove = [ 
    cutTrkEcalo, 
]
removeCuts(caloSdbandSelection.cuts, cutsToRemove)
cutsToAdd = [ 
    cutTrkEcaloInv, 
]
addCuts(caloSdbandSelection.cuts, cutsToAdd)

##########################################################################

nMissOutSdbandSelection = copy.deepcopy(disTrkSelection) 
nMissOutSdbandSelection.name = cms.string("NMissOutSdbandSelection") 
cutsToRemove = [ 
    cutTrkNMissOut, 
]
removeCuts(nMissOutSdbandSelection.cuts, cutsToRemove)
cutsToAdd = [ 
    cutTrkNMissOutInv, 
]
addCuts(nMissOutSdbandSelection.cuts, cutsToAdd)

##########################################################################
