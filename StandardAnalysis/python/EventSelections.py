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
        cutDummyMet,
    )


##########################################################################
##### Preselection #####
##########################################################################

vertexCutOnly = cms.PSet(
    name = cms.string("VertexCutOnly"),
    triggers = triggersMet,
    metFilters = metFilters,
    cuts = cms.VPSet (
        cutMetFilters,
        cutGoodPV,
    )
)
metMinimalSkim = copy.deepcopy (vertexCutOnly)
metMinimalSkim.name = cms.string ("metMinimalSkim")
addCuts (metMinimalSkim.cuts, [cutMet])
basicSelection = copy.deepcopy (metMinimalSkim)
basicSelection.name = cms.string ("BasicSelection")
jetCuts = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
]
addCuts(basicSelection.cuts, jetCuts + [cutLeadingJetMetPhi])

basicSelectionNoAngularCuts = copy.deepcopy (basicSelection)
basicSelectionNoAngularCuts.name = cms.string ("BasicSelectionNoAngularCuts")
removeCuts (basicSelectionNoAngularCuts.cuts, [cutDijetDeltaPhiMax, cutLeadingJetMetPhi])

basicSelectionNoDijetPhiCut = copy.deepcopy (basicSelection)
basicSelectionNoDijetPhiCut.name = cms.string ("BasicSelectionNoDijetPhiCut")
removeCuts (basicSelectionNoDijetPhiCut.cuts, [cutDijetDeltaPhiMax])

basicSelectionNoJetMetPhiCut = copy.deepcopy (basicSelection)
basicSelectionNoJetMetPhiCut.name = cms.string ("BasicSelectionNoJetMetPhiCut")
removeCuts (basicSelectionNoJetMetPhiCut.cuts, [cutLeadingJetMetPhi])

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
    cutTrkNValidPixelHits3,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
]
isoTrkWithPt55Cuts = [
    cutTrkEta,
    cutTrkPt55,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidPixelHits3,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
]
isoTrkWithPt55BeforeIsoCuts = [
    cutTrkEta,
    cutTrkPt55,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidPixelHits3,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
]
addCuts(isoTrkSelection.cuts, isoTrkWithPt55Cuts)

isoTrkSelectionInvertDRJetCut = copy.deepcopy (isoTrkSelection)
isoTrkSelectionInvertDRJetCut.name = cms.string ("IsoTrkSelectionInvertDRJetCut")
removeCuts (isoTrkSelectionInvertDRJetCut.cuts, [cutTrkJetDeltaPhi])
addCuts (isoTrkSelectionInvertDRJetCut.cuts, [cutTrkJetDeltaPhiInvert])

isoTrkSelectionBeforeIsoCut = copy.deepcopy (basicSelection)
isoTrkSelectionBeforeIsoCut.name = cms.string ("IsoTrkSelectionBeforeIsoCut")
addCuts (isoTrkSelectionBeforeIsoCut.cuts, isoTrkWithPt55BeforeIsoCuts)

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
    cutLeadingJetMetPhi,
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
removeCuts(nonIsoTrkSelection.cuts, [cutTrkIso, cutTrkJetDeltaPhi])

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
disappearingCuts = [
    cutTrkEcalo,
    cutTrkNMissOut,
]
addCuts(disTrkSelection.cuts, disappearingCuts)
disTrkCuts = candTrkCuts + disappearingCuts

disTrkNoNMissOut = copy.deepcopy(disTrkSelection)
disTrkNoNMissOut.name = cms.string("DisTrkNoNMissOut")
removeCuts(disTrkNoNMissOut.cuts, [cutTrkNMissOut])

disTrkNoEcalo = copy.deepcopy(disTrkSelection)
disTrkNoEcalo.name = cms.string("DisTrkNoEcalo")
removeCuts(disTrkNoEcalo.cuts, [cutTrkEcalo])

disTrkNoTrigger = copy.deepcopy(disTrkSelection)
disTrkNoTrigger.name = cms.string("DisTrkNoTrigger")
disTrkNoTrigger.triggers = cms.vstring ()

disTrkJustMainTrigger = copy.deepcopy(disTrkSelection)
disTrkJustMainTrigger.name = cms.string("DisTrkJustMainTrigger")
disTrkJustMainTrigger.triggers = triggersMetAndIsoTrk

disTrkJustMET90Trigger = copy.deepcopy(disTrkSelection)
disTrkJustMET90Trigger.name = cms.string("DisTrkJustMET90Trigger")
disTrkJustMET90Trigger.triggers = cms.vstring("HLT_MET90_IsoTrk50_v")

disTrkJustMainTriggerHltMet105 = copy.deepcopy(disTrkJustMainTrigger)
disTrkJustMainTriggerHltMet105.name = cms.string("DisTrkJustMainTriggerHltMet105")
disTrkJustMainTriggerHltMet105.cuts.insert(0, cutHltMet105)

disTrkJustMET90TriggerHltMet105 = copy.deepcopy(disTrkJustMET90Trigger)
disTrkJustMET90TriggerHltMet105.name = cms.string("DisTrkJustMet90TriggerHltMet105")
disTrkJustMET90TriggerHltMet105.cuts.insert(0, cutHltMet105)

justAChargino = cms.PSet(
    name = cms.string("JustAChargino"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutTrkMatchChargino,
    )
)
justAHighPtChargino = cms.PSet(
    name = cms.string("JustAChargino"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutTrkPt55,
        cutTrkMatchChargino,
    )
)
justAVertex = cms.PSet(
    name = cms.string("JustAVertex"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutGoodPV,
    )
)
justTriggers = cms.PSet(
    name = cms.string("JustTriggers"),
    triggers = triggersMet,
    cuts = cms.VPSet (
        cutDummyMet,
    ),
)
justMET75IsoTrk50 = cms.PSet(
    name = cms.string("JustMET75IsoTrk50"),
    triggers = cms.vstring("HLT_MET75_IsoTrk50_v"),
    cuts = cms.VPSet (
        cutDummyMet,
    ),
)
justMET90IsoTrk50 = cms.PSet(
    name = cms.string("JustMET790IsoTrk50"),
    triggers = cms.vstring("HLT_MET90_IsoTrk50_v"),
    cuts = cms.VPSet (
        cutDummyMet,
    ),
)
justAFakeTrkWithNoCuts = cms.PSet(
    name = cms.string("JustAFakeTrkWithNoCuts"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutTrkPt20,
        cutTrkEta,
        cutTrkMatchFake,
    ),
)
justARealTrkWithNoCuts = cms.PSet(
    name = cms.string("JustARealTrkWithNoCuts"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutTrkPt20,
        cutTrkEta,
        cutTrkMatchReal,
    ),
)
justACharginoWithNoCuts = cms.PSet(
    name = cms.string("JustACharginoWithNoCuts"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutTrkPt20,
        cutTrkEta,
        cutTrkMatchChargino,
    )
)

justADisTrk = copy.deepcopy (justAVertex)
justADisTrk.name = cms.string ("JustADisTrk")
addCuts(justADisTrk.cuts, [cutTrkPt55] + disTrkCuts)

justADisTrkNHits3 = copy.deepcopy (justADisTrk)
justADisTrkNHits3.name = cms.string ("JustADisTrkNHits3")
removeCuts (justADisTrkNHits3.cuts, [cutTrkNValidHits])
addCuts (justADisTrkNHits3.cuts, [cutTrkNValidHits3])

justADisTrkNHits4 = copy.deepcopy (justADisTrk)
justADisTrkNHits4.name = cms.string ("JustADisTrkNHits4")
removeCuts (justADisTrkNHits4.cuts, [cutTrkNValidHits])
addCuts (justADisTrkNHits4.cuts, [cutTrkNValidHits4])

justADisTrkNHits5 = copy.deepcopy (justADisTrk)
justADisTrkNHits5.name = cms.string ("JustADisTrkNHits5")
removeCuts (justADisTrkNHits5.cuts, [cutTrkNValidHits])
addCuts (justADisTrkNHits5.cuts, [cutTrkNValidHits5])

justADisTrkNHits6 = copy.deepcopy (justADisTrk)
justADisTrkNHits6.name = cms.string ("JustADisTrkNHits6")
removeCuts (justADisTrkNHits6.cuts, [cutTrkNValidHits])
addCuts (justADisTrkNHits6.cuts, [cutTrkNValidHits6])

justACandTrk = copy.deepcopy (justAVertex)
justACandTrk.name = cms.string ("JustACandTrk")
addCuts(justACandTrk.cuts, [cutTrkPt55] + candTrkCuts)

justACandTrkNoD0Cut = copy.deepcopy (justACandTrk)
justACandTrkNoD0Cut.name = cms.string ("JustACandTrkNoD0Cut")
removeCuts(justACandTrkNoD0Cut.cuts, [cutTrkD0])

justAFakeTrk = copy.deepcopy (justACandTrk)
justAFakeTrk.name = cms.string ("JustAFakeTrk")
addCuts(justAFakeTrk.cuts, [cutTrkMatchFake])

justAFakeTrkNHits3 = copy.deepcopy (justAFakeTrk)
justAFakeTrkNHits3.name = cms.string ("JustAFakeTrkNHits3")
removeCuts (justAFakeTrkNHits3.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNHits3.cuts, [cutTrkNValidHits3])

justAFakeTrkNHits4 = copy.deepcopy (justAFakeTrk)
justAFakeTrkNHits4.name = cms.string ("JustAFakeTrkNHits4")
removeCuts (justAFakeTrkNHits4.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNHits4.cuts, [cutTrkNValidHits4])

justAFakeTrkNHits5 = copy.deepcopy (justAFakeTrk)
justAFakeTrkNHits5.name = cms.string ("JustAFakeTrkNHits5")
removeCuts (justAFakeTrkNHits5.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNHits5.cuts, [cutTrkNValidHits5])

justAFakeTrkNHits6 = copy.deepcopy (justAFakeTrk)
justAFakeTrkNHits6.name = cms.string ("JustAFakeTrkNHits6")
removeCuts (justAFakeTrkNHits6.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNHits6.cuts, [cutTrkNValidHits6])

justARealTrk = copy.deepcopy (justACandTrk)
justARealTrk.name = cms.string ("JustARealTrk")
addCuts(justARealTrk.cuts, [cutTrkMatchReal])

justARealTrkNHits3 = copy.deepcopy (justARealTrk)
justARealTrkNHits3.name = cms.string ("JustARealTrkNHits3")
removeCuts (justARealTrkNHits3.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNHits3.cuts, [cutTrkNValidHits3])

justARealTrkNHits4 = copy.deepcopy (justARealTrk)
justARealTrkNHits4.name = cms.string ("JustARealTrkNHits4")
removeCuts (justARealTrkNHits4.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNHits4.cuts, [cutTrkNValidHits4])

justARealTrkNHits5 = copy.deepcopy (justARealTrk)
justARealTrkNHits5.name = cms.string ("JustARealTrkNHits5")
removeCuts (justARealTrkNHits5.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNHits5.cuts, [cutTrkNValidHits5])

justARealTrkNHits6 = copy.deepcopy (justARealTrk)
justARealTrkNHits6.name = cms.string ("JustARealTrkNHits6")
removeCuts (justARealTrkNHits6.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNHits6.cuts, [cutTrkNValidHits6])

justAFakeTrkNoD0Cut = copy.deepcopy (justACandTrkNoD0Cut)
justAFakeTrkNoD0Cut.name = cms.string ("JustAFakeTrkNoD0Cut")
addCuts(justAFakeTrkNoD0Cut.cuts, [cutTrkMatchFake])

justAFakeTrkNoD0CutNHits3 = copy.deepcopy (justAFakeTrkNoD0Cut)
justAFakeTrkNoD0CutNHits3.name = cms.string ("JustAFakeTrkNoD0CutNHits3")
removeCuts (justAFakeTrkNoD0CutNHits3.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNoD0CutNHits3.cuts, [cutTrkNValidHits3])

justAFakeTrkNoD0CutNHits4 = copy.deepcopy (justAFakeTrkNoD0Cut)
justAFakeTrkNoD0CutNHits4.name = cms.string ("JustAFakeTrkNoD0CutNHits4")
removeCuts (justAFakeTrkNoD0CutNHits4.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNoD0CutNHits4.cuts, [cutTrkNValidHits4])

justAFakeTrkNoD0CutNHits5 = copy.deepcopy (justAFakeTrkNoD0Cut)
justAFakeTrkNoD0CutNHits5.name = cms.string ("JustAFakeTrkNoD0CutNHits5")
removeCuts (justAFakeTrkNoD0CutNHits5.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNoD0CutNHits5.cuts, [cutTrkNValidHits5])

justAFakeTrkNoD0CutNHits6 = copy.deepcopy (justAFakeTrkNoD0Cut)
justAFakeTrkNoD0CutNHits6.name = cms.string ("JustAFakeTrkNoD0CutNHits6")
removeCuts (justAFakeTrkNoD0CutNHits6.cuts, [cutTrkNValidHits])
addCuts (justAFakeTrkNoD0CutNHits6.cuts, [cutTrkNValidHits6])

justARealTrkNoD0Cut = copy.deepcopy (justACandTrkNoD0Cut)
justARealTrkNoD0Cut.name = cms.string ("JustARealTrkNoD0Cut")
addCuts(justARealTrkNoD0Cut.cuts, [cutTrkMatchReal])

justARealTrkNoD0CutNHits3 = copy.deepcopy (justARealTrkNoD0Cut)
justARealTrkNoD0CutNHits3.name = cms.string ("JustARealTrkNoD0CutNHits3")
removeCuts (justARealTrkNoD0CutNHits3.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNoD0CutNHits3.cuts, [cutTrkNValidHits3])

justARealTrkNoD0CutNHits4 = copy.deepcopy (justARealTrkNoD0Cut)
justARealTrkNoD0CutNHits4.name = cms.string ("JustARealTrkNoD0CutNHits4")
removeCuts (justARealTrkNoD0CutNHits4.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNoD0CutNHits4.cuts, [cutTrkNValidHits4])

justARealTrkNoD0CutNHits5 = copy.deepcopy (justARealTrkNoD0Cut)
justARealTrkNoD0CutNHits5.name = cms.string ("JustARealTrkNoD0CutNHits5")
removeCuts (justARealTrkNoD0CutNHits5.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNoD0CutNHits5.cuts, [cutTrkNValidHits5])

justARealTrkNoD0CutNHits6 = copy.deepcopy (justARealTrkNoD0Cut)
justARealTrkNoD0CutNHits6.name = cms.string ("JustARealTrkNoD0CutNHits6")
removeCuts (justARealTrkNoD0CutNHits6.cuts, [cutTrkNValidHits])
addCuts (justARealTrkNoD0CutNHits6.cuts, [cutTrkNValidHits6])

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
    cutLeadingJetMetPhi,
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
    cutLeadingJetMetPhi,
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
candTrkIdTauPt55 = copy.deepcopy(candTrkSelection)
candTrkIdTauPt55.name = cms.string("CandTrkIdTauPt55")
cutsToAdd = [
    cutTrkMatchGenTau,
    ]
addCuts(candTrkIdTauPt55.cuts, cutsToAdd)
addSingleCut(candTrkIdTauPt55.cuts, cutTrkPt50, cutTrkPt55)
cutsToRemove = [
    cutTrkPt55,
    # For first iteration, remove all jet cuts.  If closure test works, then add the jet cuts back in.
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
    ]
removeCuts(candTrkIdTauPt55.cuts, cutsToRemove)


# Use this selection for the electron background estimate.
candTrkIdTauPt55NoMet = copy.deepcopy(candTrkIdTauPt55)
candTrkIdTauPt55NoMet.name = cms.string("CandTrkIdTauPt55NoMet")
candTrkIdTauPt55NoMet.triggers = cms.vstring()
cutsToRemove = [
    cutMet,
    ]
removeCuts(candTrkIdTauPt55NoMet.cuts, cutsToRemove)

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

muonCtrlSelectionWithMatch = copy.deepcopy(muonCtrlSelection)
muonCtrlSelectionWithMatch.name = cms.string("MuonCtrlSelectionWithMatch")
addCuts(muonCtrlSelectionWithMatch.cuts, [cutMuTrkMatch])

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
addSingleCut(disTrkSelectionNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts(disTrkSelectionNHits3.cuts, [cutTrkNValidHits])

##########################################################################

disTrkSelectionNHits4 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits4.name = cms.string("DisTrkSelectionNHits4")
addSingleCut(disTrkSelectionNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts(disTrkSelectionNHits4.cuts, [cutTrkNValidHits])

##########################################################################

disTrkSelectionNHits5 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits5.name = cms.string("DisTrkSelectionNHits5")
addSingleCut(disTrkSelectionNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts(disTrkSelectionNHits5.cuts, [cutTrkNValidHits])

##########################################################################

disTrkSelectionNHits6 = copy.deepcopy(disTrkSelection)
disTrkSelectionNHits6.name = cms.string("DisTrkSelectionNHits6")
addSingleCut(disTrkSelectionNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts(disTrkSelectionNHits6.cuts, [cutTrkNValidHits])

##########################################################################

oneJet14to18PVCuts = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
    cutNJetsEQ1,
    cutNumPV14to18
]

basicSelectionOneJet14to18PV = copy.deepcopy(basicSelection)
basicSelectionOneJet14to18PV.name = cms.string("BasicSelectionOneJet14to18PV")
addCuts(basicSelectionOneJet14to18PV.cuts, [cutNJetsEQ1, cutNumPV14to18])

disTrkSelectionOneJet14to18PVNHits3 = copy.deepcopy(disTrkSelectionNHits3)
disTrkSelectionOneJet14to18PVNHits3.name = cms.string("DisTrkSelectionOneJet14to18PVNHits3")
addCuts(disTrkSelectionOneJet14to18PVNHits3.cuts, oneJet14to18PVCuts)

disTrkSelectionOneJet14to18PVNHits4 = copy.deepcopy(disTrkSelectionNHits4)
disTrkSelectionOneJet14to18PVNHits4.name = cms.string("DisTrkSelectionOneJet14to18PVNHits4")
addCuts(disTrkSelectionOneJet14to18PVNHits4.cuts, oneJet14to18PVCuts)

disTrkSelectionOneJet14to18PVNHits5 = copy.deepcopy(disTrkSelectionNHits5)
disTrkSelectionOneJet14to18PVNHits5.name = cms.string("DisTrkSelectionOneJet14to18PVNHits5")
addCuts(disTrkSelectionOneJet14to18PVNHits5.cuts, oneJet14to18PVCuts)

disTrkSelectionOneJet14to18PVNHits6 = copy.deepcopy(disTrkSelectionNHits6)
disTrkSelectionOneJet14to18PVNHits6.name = cms.string("DisTrkSelectionOneJet14to18PVNHits6")
addCuts(disTrkSelectionOneJet14to18PVNHits6.cuts, oneJet14to18PVCuts)


##########################################################################

##########################################################################
##### ZeroBias selections #####
##########################################################################
zeroBiasSelection = cms.PSet(
    name = cms.string("ZeroBiasSelection"),
    triggers = triggersZeroBias,
    cuts = cms.VPSet (
        cutGoodPV,
    )
)

zeroBiasSelectionDisTrk = copy.deepcopy (zeroBiasSelection)
zeroBiasSelectionDisTrk.name = cms.string ("ZeroBiasSelectionDisTrk")
addCuts (zeroBiasSelectionDisTrk.cuts, disTrkCuts)

zeroBiasSelectionDisTrkNHits3 = copy.deepcopy (zeroBiasSelectionDisTrk)
zeroBiasSelectionDisTrkNHits3.name = cms.string ("ZeroBiasSelectionNHits3")
removeCuts (zeroBiasSelectionDisTrkNHits3.cuts, [cutTrkNValidHits])
addCuts (zeroBiasSelectionDisTrkNHits3.cuts, [cutTrkNValidHits3])

zeroBiasSelectionDisTrkNHits4 = copy.deepcopy (zeroBiasSelectionDisTrk)
zeroBiasSelectionDisTrkNHits4.name = cms.string ("ZeroBiasSelectionNHits4")
removeCuts (zeroBiasSelectionDisTrkNHits4.cuts, [cutTrkNValidHits])
addCuts (zeroBiasSelectionDisTrkNHits4.cuts, [cutTrkNValidHits4])

zeroBiasSelectionDisTrkNHits5 = copy.deepcopy (zeroBiasSelectionDisTrk)
zeroBiasSelectionDisTrkNHits5.name = cms.string ("ZeroBiasSelectionNHits5")
removeCuts (zeroBiasSelectionDisTrkNHits5.cuts, [cutTrkNValidHits])
addCuts (zeroBiasSelectionDisTrkNHits5.cuts, [cutTrkNValidHits5])

zeroBiasSelectionDisTrkNHits6 = copy.deepcopy (zeroBiasSelectionDisTrk)
zeroBiasSelectionDisTrkNHits6.name = cms.string ("ZeroBiasSelectionNHits6")
removeCuts (zeroBiasSelectionDisTrkNHits6.cuts, [cutTrkNValidHits])
addCuts (zeroBiasSelectionDisTrkNHits6.cuts, [cutTrkNValidHits6])

zeroBiasJetSelection = cms.PSet(
    name = cms.string("ZeroBiasJetSelection"),
    triggers = triggersZeroBias,
    cuts = cms.VPSet (
        cutGoodPV,
        cutJetPt55,
        cutJetEta,
        cutJetTightLepVeto,
    )
)

zeroBiasJetSelectionDisTrk = copy.deepcopy (zeroBiasJetSelection)
zeroBiasJetSelectionDisTrk.name = cms.string ("ZeroBiasJetSelectionDisTrk")
addCuts (zeroBiasJetSelectionDisTrk.cuts, disTrkCuts)

zeroBiasJetSelectionDisTrkNHits3 = copy.deepcopy (zeroBiasJetSelectionDisTrk)
zeroBiasJetSelectionDisTrkNHits3.name = cms.string ("ZeroBiasJetSelectionNHits3")
removeCuts (zeroBiasJetSelectionDisTrkNHits3.cuts, [cutTrkNValidHits])
addCuts (zeroBiasJetSelectionDisTrkNHits3.cuts, [cutTrkNValidHits3])

zeroBiasJetSelectionDisTrkNHits4 = copy.deepcopy (zeroBiasJetSelectionDisTrk)
zeroBiasJetSelectionDisTrkNHits4.name = cms.string ("ZeroBiasJetSelectionNHits4")
removeCuts (zeroBiasJetSelectionDisTrkNHits4.cuts, [cutTrkNValidHits])
addCuts (zeroBiasJetSelectionDisTrkNHits4.cuts, [cutTrkNValidHits4])

zeroBiasJetSelectionDisTrkNHits5 = copy.deepcopy (zeroBiasJetSelectionDisTrk)
zeroBiasJetSelectionDisTrkNHits5.name = cms.string ("ZeroBiasJetSelectionNHits5")
removeCuts (zeroBiasJetSelectionDisTrkNHits5.cuts, [cutTrkNValidHits])
addCuts (zeroBiasJetSelectionDisTrkNHits5.cuts, [cutTrkNValidHits5])

zeroBiasJetSelectionDisTrkNHits6 = copy.deepcopy (zeroBiasJetSelectionDisTrk)
zeroBiasJetSelectionDisTrkNHits6.name = cms.string ("ZeroBiasJetSelectionNHits6")
removeCuts (zeroBiasJetSelectionDisTrkNHits6.cuts, [cutTrkNValidHits])
addCuts (zeroBiasJetSelectionDisTrkNHits6.cuts, [cutTrkNValidHits6])
##########################################################################

##########################################################################
# Selections including generated signal event type.
##########################################################################
disTrkSelectionCharginoChargino = copy.deepcopy (disTrkSelection)
disTrkSelectionCharginoChargino.name = cms.string ("DisTrkSelectionCharginoChargino")
disTrkSelectionCharginoChargino.cuts.insert (0, cutMCCharginoChargino)

disTrkSelectionCharginoNeutralino = copy.deepcopy (disTrkSelection)
disTrkSelectionCharginoNeutralino.name = cms.string ("DisTrkSelectionCharginoNeutralino")
disTrkSelectionCharginoNeutralino.cuts.insert (0, cutMCCharginoNeutralino)

charginoChargino = cms.PSet(
    name = cms.string("CharginoChargino"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutMCCharginoChargino,
    )
)

charginoNeutralino = cms.PSet(
    name = cms.string("CharginoNeutralino"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cutMCCharginoNeutralino,
    )
)
##########################################################################
# Selections inverting, dropping, or loosening the D0 cut
##########################################################################

# channel not blinded -- includes signal region!
disTrkSelectionNoD0Cut = copy.deepcopy(disTrkSelection)
disTrkSelectionNoD0Cut.name = cms.string("DisTrkSelectionNoD0Cut")
removeCuts(disTrkSelectionNoD0Cut.cuts, [cutTrkD0])

disTrkSelectionInvertD0Cut = copy.deepcopy(disTrkSelection)
disTrkSelectionInvertD0Cut.name = cms.string("DisTrkSelectionInvertD0Cut")
addSingleCut(disTrkSelectionInvertD0Cut.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(disTrkSelectionInvertD0Cut.cuts, [cutTrkD0])

disTrkSelectionSidebandD0Cut = copy.deepcopy(disTrkSelection)
disTrkSelectionSidebandD0Cut.name = cms.string("DisTrkSelectionSidebandD0Cut")
addSingleCut(disTrkSelectionSidebandD0Cut.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(disTrkSelectionSidebandD0Cut.cuts, [cutTrkD0])

disTrkSelectionNoD0CutNHits3 = copy.deepcopy(disTrkSelectionNoD0Cut)
disTrkSelectionNoD0CutNHits3.name = cms.string("DisTrkSelectionNoD0CutNHits3")
removeCuts(disTrkSelectionNoD0CutNHits3.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionNoD0CutNHits3.cuts, [cutTrkNValidHits3])

disTrkSelectionInvertD0CutNHits3 = copy.deepcopy(disTrkSelectionInvertD0Cut)
disTrkSelectionInvertD0CutNHits3.name = cms.string("DisTrkSelectionInvertD0CutNHits3")
removeCuts(disTrkSelectionInvertD0CutNHits3.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionInvertD0CutNHits3.cuts, [cutTrkNValidHits3])

disTrkSelectionSidebandD0CutNHits3 = copy.deepcopy(disTrkSelectionSidebandD0Cut)
disTrkSelectionSidebandD0CutNHits3.name = cms.string("DisTrkSelectionSidebandD0CutNHits3")
removeCuts(disTrkSelectionSidebandD0CutNHits3.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionSidebandD0CutNHits3.cuts, [cutTrkNValidHits3])

disTrkSelectionNoD0CutNHits4 = copy.deepcopy(disTrkSelectionNoD0Cut)
disTrkSelectionNoD0CutNHits4.name = cms.string("DisTrkSelectionNoD0CutNHits4")
removeCuts(disTrkSelectionNoD0CutNHits4.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionNoD0CutNHits4.cuts, [cutTrkNValidHits4])

disTrkSelectionInvertD0CutNHits4 = copy.deepcopy(disTrkSelectionInvertD0Cut)
disTrkSelectionInvertD0CutNHits4.name = cms.string("DisTrkSelectionInvertD0CutNHits4")
removeCuts(disTrkSelectionInvertD0CutNHits4.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionInvertD0CutNHits4.cuts, [cutTrkNValidHits4])

disTrkSelectionSidebandD0CutNHits4 = copy.deepcopy(disTrkSelectionSidebandD0Cut)
disTrkSelectionSidebandD0CutNHits4.name = cms.string("DisTrkSelectionSidebandD0CutNHits4")
removeCuts(disTrkSelectionSidebandD0CutNHits4.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionSidebandD0CutNHits4.cuts, [cutTrkNValidHits4])

disTrkSelectionNoD0CutNHits5 = copy.deepcopy(disTrkSelectionNoD0Cut)
disTrkSelectionNoD0CutNHits5.name = cms.string("DisTrkSelectionNoD0CutNHits5")
removeCuts(disTrkSelectionNoD0CutNHits5.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionNoD0CutNHits5.cuts, [cutTrkNValidHits5])

disTrkSelectionInvertD0CutNHits5 = copy.deepcopy(disTrkSelectionInvertD0Cut)
disTrkSelectionInvertD0CutNHits5.name = cms.string("DisTrkSelectionInvertD0CutNHits5")
removeCuts(disTrkSelectionInvertD0CutNHits5.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionInvertD0CutNHits5.cuts, [cutTrkNValidHits5])

disTrkSelectionSidebandD0CutNHits5 = copy.deepcopy(disTrkSelectionSidebandD0Cut)
disTrkSelectionSidebandD0CutNHits5.name = cms.string("DisTrkSelectionSidebandD0CutNHits5")
removeCuts(disTrkSelectionSidebandD0CutNHits5.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionSidebandD0CutNHits5.cuts, [cutTrkNValidHits5])

disTrkSelectionNoD0CutNHits6 = copy.deepcopy(disTrkSelectionNoD0Cut)
disTrkSelectionNoD0CutNHits6.name = cms.string("DisTrkSelectionNoD0CutNHits6")
removeCuts(disTrkSelectionNoD0CutNHits6.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionNoD0CutNHits6.cuts, [cutTrkNValidHits6])

disTrkSelectionInvertD0CutNHits6 = copy.deepcopy(disTrkSelectionInvertD0Cut)
disTrkSelectionInvertD0CutNHits6.name = cms.string("DisTrkSelectionInvertD0CutNHits6")
removeCuts(disTrkSelectionInvertD0CutNHits6.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionInvertD0CutNHits6.cuts, [cutTrkNValidHits6])

disTrkSelectionSidebandD0CutNHits6 = copy.deepcopy(disTrkSelectionSidebandD0Cut)
disTrkSelectionSidebandD0CutNHits6.name = cms.string("DisTrkSelectionSidebandD0CutNHits6")
removeCuts(disTrkSelectionSidebandD0CutNHits6.cuts, [cutTrkNValidHits])
addCuts(disTrkSelectionSidebandD0CutNHits6.cuts, [cutTrkNValidHits6])

##########################################################################
# Selections with lower numbers of hits
##########################################################################

##########################################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
