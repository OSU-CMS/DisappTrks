import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file


##########################################################################
##### Testing #####
##########################################################################
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (),
    )


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
        cutJetEta,
        cutJetTightLepVeto,
        cutDijetDeltaPhiMax,
        cutJetMetPhi,
    )
)

##########################################################################

metMinimalSkim = cms.PSet(
    name = cms.string("metMinimalSkim"),
    triggers = triggersMet,
    cuts = cms.VPSet (
        cutGoodPV,
        cutMet,
    )
)

##########################################################################

isoTrkSelection = copy.deepcopy(basicSelection)
isoTrkSelection.name = cms.string("IsoTrkSelection")
isoTrkCuts = [
    cutTrkPt,
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
addCuts(isoTrkSelection.cuts, isoTrkCuts)


##########################################################################

isoTrkSelectionNoJetCuts = copy.deepcopy(isoTrkSelection)
isoTrkSelectionNoJetCuts.name = cms.string("IsoTrkSelectionNoJetCuts")
cutsToRemove = [
    cutDijetDeltaPhiMax,
    cutJetMetPhi,
    cutTrkJetDeltaPhi,
]  
removeCuts(isoTrkSelectionNoJetCuts.cuts, cutsToRemove) 

##########################################################################

isoTrkSelectionNMissOut4 = copy.deepcopy(isoTrkSelection)
isoTrkSelectionNMissOut4.name = cms.string("IsoTrkSelectionNMissOut4")
addCuts(isoTrkSelectionNMissOut4.cuts, [cutTrkNMissOut4])  

##########################################################################

nonIsoTrkSelection = copy.deepcopy(isoTrkSelection)
nonIsoTrkSelection.name = cms.string("NonIsoTrkSelection")
removeCuts(nonIsoTrkSelection.cuts, [cutTrkIso])

##########################################################################

candTrkSelection = copy.deepcopy(isoTrkSelection)
candTrkSelection.name = cms.string("CandTrkSelection")
cutsToAdd = [
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
]
addCuts(candTrkSelection.cuts, cutsToAdd)
candTrkCuts = isoTrkCuts + cutsToAdd

##########################################################################

disTrkSelection = copy.deepcopy(candTrkSelection)
disTrkSelection.name = cms.string("DisTrkSelection")
cutsToAdd = [
    cutTrkEcalo,
    cutTrkNMissOut,
]
addCuts(disTrkSelection.cuts, cutsToAdd)
disTrkCuts = candTrkCuts + cutsToAdd


##########################################################################

candTrkEcaloSdband = copy.deepcopy(candTrkSelection)
candTrkEcaloSdband.name = cms.string("CandTrkEcaloSdband")
cutsToAdd = [
    cutTrkNMissOut,
    cutTrkEcaloInv,
]
addCuts(candTrkEcaloSdband.cuts, cutsToAdd)
candTrkEcaloSdbandCuts = candTrkCuts + cutsToAdd

##########################################################################

candTrkNMissOutSdband = copy.deepcopy(candTrkSelection)
candTrkNMissOutSdband.name = cms.string("CandTrkNMissOutSdband")
cutsToAdd = [
    cutTrkEcalo,
    cutTrkNMissOutInv,
]
addCuts(candTrkNMissOutSdband.cuts, cutsToAdd)
candTrkNMissOutSdbandCuts = candTrkCuts + cutsToAdd

##########################################################################

# Use this selection for the muon background estimate.
disTrkSelectionIdElec = copy.deepcopy(disTrkSelection)
disTrkSelectionIdElec.name = cms.string("DisTrkSelectionIdElec")
cutsToAdd = [
    cutTrkMatchGenElec,
]
addCuts(disTrkSelectionIdElec.cuts, cutsToAdd)

##########################################################################

# Use this selection for the muon background estimate.
disTrkSelectionMatchGenMuon = copy.deepcopy(disTrkSelection)
disTrkSelectionMatchGenMuon.name = cms.string("DisTrkSelectionMatchGenMuon")
cutsToAdd = [
    cutTrkMatchGenMuon,
]
addCuts(disTrkSelectionMatchGenMuon.cuts, cutsToAdd)

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
cutsToAdd = [
    cutTrkMatchGenMuon,
]
#addCuts(muonCtrlSelection.cuts, cutsToAdd)

##########################################################################

muonCtrlLoEcalo = copy.deepcopy(muonCtrlSelection)
muonCtrlLoEcalo.name = cms.string("MuonCtrlLoEcalo")
cutsToAdd = [
    cutTrkEcalo,
]
addCuts(muonCtrlLoEcalo.cuts, cutsToAdd)

##########################################################################

muonCtrlLoEcaloGenMatchNone = copy.deepcopy(muonCtrlLoEcalo)
muonCtrlLoEcaloGenMatchNone.name = cms.string("muonCtrlLoEcaloGenMatchNone")
cutsToAdd = [
    cutTrkMatchGenNone,
]
addCuts(muonCtrlLoEcaloGenMatchNone.cuts, cutsToAdd)

##########################################################################

muonCtrlLoEcaloGenMatchPhoton = copy.deepcopy(muonCtrlLoEcalo)
muonCtrlLoEcaloGenMatchPhoton.name = cms.string("muonCtrlLoEcaloGenMatchPhoton")
cutsToAdd = [
    cutTrkMatchGenPhoton,
]
addCuts(muonCtrlLoEcaloGenMatchPhoton.cuts, cutsToAdd)

##########################################################################

muonCtrlLoEcaloNoMuonDRMatch = copy.deepcopy(muonCtrlLoEcalo)
muonCtrlLoEcaloNoMuonDRMatch.name = cms.string("muonCtrlLoEcaloNoMuonDRMatch")
cutsToAdd = [
    cutTrkNoMuonDRMatch,
]
addCuts(muonCtrlLoEcaloNoMuonDRMatch.cuts, cutsToAdd)

##########################################################################

muonCtrlLoEcaloNoMuonDRMatchLargeD0 = copy.deepcopy(muonCtrlLoEcaloNoMuonDRMatch)
muonCtrlLoEcaloNoMuonDRMatchLargeD0.name = cms.string("muonCtrlLoEcaloNoMuonDRMatchLargeD0")
cutsToAdd = [
    cutTrkLargeD0,
]
addCuts(muonCtrlLoEcaloNoMuonDRMatchLargeD0.cuts, cutsToAdd)

##########################################################################

muonCtrlLoEcaloNoMuonDRMatchSmallD0 = copy.deepcopy(muonCtrlLoEcaloNoMuonDRMatch)
muonCtrlLoEcaloNoMuonDRMatchSmallD0.name = cms.string("muonCtrlLoEcaloNoMuonDRMatchSmallD0")
cutsToAdd = [
    cutTrkSmallD0,
]
addCuts(muonCtrlLoEcaloNoMuonDRMatchSmallD0.cuts, cutsToAdd)

##########################################################################

muonCtrlHiEcalo = copy.deepcopy(muonCtrlSelection)
muonCtrlHiEcalo.name = cms.string("MuonCtrlHiEcalo")
cutsToAdd = [
    cutTrkEcaloInv50,
]
addCuts(muonCtrlHiEcalo.cuts, cutsToAdd)

##########################################################################

muonCtrlHiEcaloGenMatchMuon = copy.deepcopy(muonCtrlHiEcalo)
muonCtrlHiEcaloGenMatchMuon.name = cms.string("muonCtrlHiEcaloGenMatchMuon")
cutsToAdd = [
    cutTrkMatchGenMuon,
]
addCuts(muonCtrlHiEcaloGenMatchMuon.cuts, cutsToAdd)

##########################################################################

tauCtrlSelection = copy.deepcopy(candTrkSelection)
tauCtrlSelection.name = cms.string("TauCtrlSelection")
cutsToRemove = [
    cutTrkTauHadVeto,
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

disTrkSelectionNHits3 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits3.name = cms.string("DisTrkSelectionNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(disTrkSelectionNHits3.cuts, cutsToRemove)
addCuts   (disTrkSelectionNHits3.cuts, cutsToAdd)


##########################################################################

disTrkSelectionNHits4 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits4.name = cms.string("DisTrkSelectionNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(disTrkSelectionNHits4.cuts, cutsToRemove)
addCuts   (disTrkSelectionNHits4.cuts, cutsToAdd)

##########################################################################

disTrkSelectionNHits5 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits5.name = cms.string("DisTrkSelectionNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(disTrkSelectionNHits5.cuts, cutsToRemove)
addCuts   (disTrkSelectionNHits5.cuts, cutsToAdd)

##########################################################################

disTrkSelectionNHits6 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits6.name = cms.string("DisTrkSelectionNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(disTrkSelectionNHits6.cuts, cutsToRemove)
addCuts   (disTrkSelectionNHits6.cuts, cutsToAdd)

##########################################################################
