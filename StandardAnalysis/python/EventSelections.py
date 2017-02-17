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
    )
)
jetCuts = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
]
addCuts(basicSelection.cuts, jetCuts)

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
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidPixelHits,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
]
addCuts(isoTrkSelection.cuts, [cutTrkPt55] + isoTrkCuts)


##########################################################################
isoTrkLoosePt = copy.deepcopy(isoTrkSelection)
isoTrkLoosePt.name = copy.deepcopy("IsoTrkLoosePt")
addSingleCut(isoTrkLoosePt.cuts,  cutTrkPt35, cutTrkPt55)
removeCuts  (isoTrkLoosePt.cuts, [cutTrkPt55])

##########################################################################

isoTrkSelectionNoJetCuts = copy.deepcopy(isoTrkSelection)
isoTrkSelectionNoJetCuts.name = cms.string("IsoTrkSelectionNoJetCuts")
cutsToRemove = [
    cutDijetDeltaPhiMax,
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
leptonVetoes = [
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
]
addCuts(candTrkSelection.cuts, leptonVetoes)
candTrkCuts = isoTrkCuts + leptonVetoes

##########################################################################

candTrkLoose = copy.deepcopy(isoTrkSelection)
candTrkLoose.name = cms.string("CandTrkLoose")
cutsToAdd = [
    cutTrkTightElecVeto,
    cutTrkTightMuonVeto,
    cutTrkTauHadVeto,
]
addCuts(candTrkLoose.cuts, cutsToAdd)

candTrkLooseElec = copy.deepcopy(candTrkSelection)
candTrkLooseElec.name = cms.string("CandTrkLooseElec")
removeCuts(candTrkLooseElec.cuts, [cutTrkElecVeto])
addCuts   (candTrkLooseElec.cuts, [cutTrkTightElecVeto])

candTrkLooseMuon = copy.deepcopy(candTrkSelection)
candTrkLooseMuon.name = cms.string("CandTrkLooseMuon")
removeCuts(candTrkLooseMuon.cuts, [cutTrkMuonVeto])
addCuts   (candTrkLooseMuon.cuts, [cutTrkTightMuonVeto])

candTrkLooseTau = copy.deepcopy(candTrkSelection)
candTrkLooseTau.name = cms.string("CandTrkLooseTau")
removeCuts(candTrkLooseTau.cuts, [cutTrkTauHadVeto])

##########################################################################

disTrkSelection = copy.deepcopy(candTrkSelection)
disTrkSelection.name = cms.string("DisTrkSelection")
cutsToAdd = [
    cutTrkEcalo,
    cutTrkNMissOut,
]
addCuts(disTrkSelection.cuts, cutsToAdd)
disTrkCuts = candTrkCuts + cutsToAdd


disTrkNoNMissOut = copy.deepcopy(disTrkSelection)
disTrkNoNMissOut.name = cms.string("DisTrkNoNMissOut")
removeCuts(disTrkNoNMissOut.cuts, [cutTrkNMissOut])

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

# Use this selection for the electron background estimate.
candTrkIdElecPt35 = copy.deepcopy(candTrkSelection)
candTrkIdElecPt35.name = cms.string("CandTrkIdElecPt35")
cutsToAdd = [
    cutTrkMatchGenElec,
    ]
addCuts(candTrkIdElecPt35.cuts, cutsToAdd)
addSingleCut(candTrkIdElecPt35.cuts, cutTrkPt35, cutTrkPt55)
cutsToRemove = [
    cutTrkPt55,
    # For first iteration, remove all jet cuts.  If closure test works, then add the jet cuts back in.
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    ]
removeCuts(candTrkIdElecPt35.cuts, cutsToRemove)


# Use this selection for the electron background estimate.
candTrkIdElecPt35NoMet = copy.deepcopy(candTrkIdElecPt35)
candTrkIdElecPt35NoMet.name = cms.string("CandTrkIdElecPt35NoMet")
candTrkIdElecPt35NoMet.triggers = cms.vstring()
cutsToRemove = [
    cutMet,
    ]
removeCuts(candTrkIdElecPt35NoMet.cuts, cutsToRemove)

##########################################################################

# Use this selection for the muon background estimate.
candTrkIdMuPt35 = copy.deepcopy(candTrkSelection)
candTrkIdMuPt35.name = cms.string("CandTrkIdMuPt35")
cutsToAdd = [
    cutTrkEcalo,
    cutTrkMatchGenMuon,
    ]
addCuts(candTrkIdMuPt35.cuts, cutsToAdd)
addSingleCut(candTrkIdMuPt35.cuts, cutTrkPt35, cutTrkPt55)
cutsToRemove = [
    cutTrkPt55,
    # For first iteration, remove all jet cuts.  If closure test works, then add the jet cuts back in.
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    ]
removeCuts(candTrkIdMuPt35.cuts, cutsToRemove)


# Use this selection for the electron background estimate.
candTrkIdMuPt35NoMet = copy.deepcopy(candTrkIdMuPt35)
candTrkIdMuPt35NoMet.name = cms.string("CandTrkIdMuPt35NoMet")
candTrkIdMuPt35NoMet.triggers = cms.vstring()
cutsToRemove = [
    cutMet,
    ]
removeCuts(candTrkIdMuPt35NoMet.cuts, cutsToRemove)

##########################################################################

# Use this selection for the tau background estimate.
candTrkIdTauPt50 = copy.deepcopy(candTrkSelection)
candTrkIdTauPt50.name = cms.string("CandTrkIdTauPt50")
cutsToAdd = [
    cutTrkMatchGenTau,
    ]
addCuts(candTrkIdTauPt50.cuts, cutsToAdd)
addSingleCut(candTrkIdTauPt50.cuts, cutTrkPt50, cutTrkPt55)
cutsToRemove = [
    cutTrkPt55,
    # For first iteration, remove all jet cuts.  If closure test works, then add the jet cuts back in.
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    ]
removeCuts(candTrkIdTauPt50.cuts, cutsToRemove)


# Use this selection for the electron background estimate.
candTrkIdTauPt50NoMet = copy.deepcopy(candTrkIdTauPt50)
candTrkIdTauPt50NoMet.name = cms.string("CandTrkIdTauPt50NoMet")
candTrkIdTauPt50NoMet.triggers = cms.vstring()
cutsToRemove = [
    cutMet,
    ]
removeCuts(candTrkIdTauPt50NoMet.cuts, cutsToRemove)

##########################################################################

# Use this selection for the electron background estimate.
disTrkIdElec = copy.deepcopy(disTrkSelection)
disTrkIdElec.name = cms.string("DisTrkIdElec")
cutsToAdd = [
    cutTrkMatchGenElec,
]
addCuts(disTrkIdElec.cuts, cutsToAdd)

##########################################################################

# Use this selection for the muon background estimate.
disTrkIdMuon = copy.deepcopy(disTrkSelection)
disTrkIdMuon.name = cms.string("DisTrkIdMuon")
cutsToAdd = [
    cutTrkMatchGenMuon,
]
addCuts(disTrkIdMuon.cuts, cutsToAdd)

##########################################################################

# Use this selection for the muon background estimate.
disTrkIdTau = copy.deepcopy(disTrkSelection)
disTrkIdTau.name = cms.string("DisTrkIdTau")
cutsToAdd = [
    cutTrkMatchGenTau,
]
addCuts(disTrkIdTau.cuts, cutsToAdd)

##########################################################################

# Use this selection for the fake track background estimate.
disTrkIdFake = copy.deepcopy(disTrkSelection)
disTrkIdFake.name = cms.string("DisTrkIdFake")
cutsToAdd = [
    cutTrkMatchFake,
]
addCuts(disTrkIdFake.cuts, cutsToAdd)

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

hitsSystematicsCtrlSelection = copy.deepcopy(muonCtrlSelection)
hitsSystematicsCtrlSelection.name = cms.string("HitsSystematicsCtrlSelection")
cutsToRemove = [
    cutTrkNMissIn,
    cutTrkNMissMid,
]
removeCuts(hitsSystematicsCtrlSelection.cuts, cutsToRemove)

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

oneJet16PVCuts = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutNJetsEQ1,
    cutNumPV16
]

basicSelectionOneJet16PV = copy.deepcopy(basicSelection)
basicSelectionOneJet16PV.name = cms.string("BasicSelectionOneJet16PV")
addCuts(basicSelectionOneJet16PV.cuts, [cutNJetsEQ1, cutNumPV16])

disTrkSelectionOneJet16PVNHits3 = copy.deepcopy(disTrkSelectionNHits3)
disTrkSelectionOneJet16PVNHits3.name = cms.string("DisTrkSelectionOneJet16PVNHits3")
addCuts(disTrkSelectionOneJet16PVNHits3.cuts, oneJet16PVCuts)

disTrkSelectionOneJet16PVNHits4 = copy.deepcopy(disTrkSelectionNHits4)
disTrkSelectionOneJet16PVNHits4.name = cms.string("DisTrkSelectionOneJet16PVNHits4")
addCuts(disTrkSelectionOneJet16PVNHits4.cuts, oneJet16PVCuts)

disTrkSelectionOneJet16PVNHits5 = copy.deepcopy(disTrkSelectionNHits5)
disTrkSelectionOneJet16PVNHits5.name = cms.string("DisTrkSelectionOneJet16PVNHits5")
addCuts(disTrkSelectionOneJet16PVNHits5.cuts, oneJet16PVCuts)

disTrkSelectionOneJet16PVNHits6 = copy.deepcopy(disTrkSelectionNHits6)
disTrkSelectionOneJet16PVNHits6.name = cms.string("DisTrkSelectionOneJet16PVNHits6")
addCuts(disTrkSelectionOneJet16PVNHits6.cuts, oneJet16PVCuts)


##########################################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
