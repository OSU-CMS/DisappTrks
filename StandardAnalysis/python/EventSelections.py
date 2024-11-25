import FWCore.ParameterSet.Config as cms
import copy
import os

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file

def createHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, None, cutTrkNLayersVariations))
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
        replaceSingleCut (globals ()[chName + 'NLayers3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

##########################################################################
##### Testing #####
##########################################################################

NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(
        cutDummyMet,
    )
)

##########################################################################
##### Skimming #####
##########################################################################

skimming = cms.PSet(
    name = cms.string("Skimming"),
    triggers = triggersAllSkimming,
    cuts = cms.VPSet(
        cutTrkPt25,
        cutTrkEta,
    )
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

jetVetoMap2022 = copy.deepcopy (vertexCutOnly)
jetVetoMap2022.name = cms.string ("jetVetoMap2022")
jetVetoMapCut = [cutVetoJetMap2022]
addCuts(jetVetoMap2022.cuts, jetVetoMapCut)

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

#####################################################################
# Veto MET pointing towards HEM 15/16 (-1.87, 0.87) in phi for 2018 CD
#####################################################################
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data") and (osusub.datasetLabel.endswith("_2018C") or osusub.datasetLabel.endswith("_2018D")):
        addCuts(basicSelection.cuts, [cutVetoMetPhiHEM1516])

basicSelectionNoAngularCuts = copy.deepcopy (basicSelection)
basicSelectionNoAngularCuts.name = cms.string ("BasicSelectionNoAngularCuts")
removeCuts (basicSelectionNoAngularCuts.cuts, [cutDijetDeltaPhiMax, cutLeadingJetMetPhi])

basicSelectionNoDijetPhiCut = copy.deepcopy (basicSelection)
basicSelectionNoDijetPhiCut.name = cms.string ("BasicSelectionNoDijetPhiCut")
removeCuts (basicSelectionNoDijetPhiCut.cuts, [cutDijetDeltaPhiMax])

basicSelectionNoJetMetPhiCut = copy.deepcopy (basicSelection)
basicSelectionNoJetMetPhiCut.name = cms.string ("BasicSelectionNoJetMetPhiCut")
removeCuts (basicSelectionNoJetMetPhiCut.cuts, [cutLeadingJetMetPhi])

#test deep sets score
deepSetsSelection = copy.deepcopy(vertexCutOnly)
deepSetsSelection.name = cms.string("DeepSetsSelection")
addCuts(deepSetsSelection.cuts, [cutTrkDeepSets])

################################################################################
## Testing channels to compare pat::IsolatedTrack to CandidateTrack
## in the MET dataset
################################################################################

MinimalMETTrackSelection = copy.deepcopy(metMinimalSkim)
MinimalMETTrackSelection.name = cms.string("MinimalMETTrackSelection")
addCuts(MinimalMETTrackSelection.cuts, [cutTrkPt20])

MinimalMETMatchedCandidateTrackSelection = copy.deepcopy(MinimalMETTrackSelection)
MinimalMETMatchedCandidateTrackSelection.name = cms.string("MinimalMETMatchedCandidateTrackSelection")
addCuts(MinimalMETMatchedCandidateTrackSelection.cuts, [cutTrkMatchedCandidateTrack])

##########################################################################

isoTrkCuts = [
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidPixelHitsSignal,
    cutTrkNValidHitsSignal,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
    cutVetoJetMap2022,
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    isoTrkCuts.insert(5, cutTrk2017LowEfficiencyRegion)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    # IMPORTANT FIXME: looks like this region started dying later in 2018 B
    # probably this is only relevant for C+D, but we've only checked C for now
    isoTrkCuts.insert(5, cutTrk2018LowEfficiencyRegion)

isoTrkWithPt55Cuts = copy.deepcopy(isoTrkCuts)
addSingleCut(isoTrkWithPt55Cuts, cutTrkPt55, cutTrkEta)

isoTrkWithPt55BeforeIsoCuts = copy.deepcopy(isoTrkWithPt55Cuts)
removeCuts(isoTrkWithPt55BeforeIsoCuts, [cutTrkIso, cutTrkD0, cutTrkDZ, cutTrkJetDeltaPhi])

isoTrkWithPt55BeforeValidPixelHitCuts = copy.deepcopy(isoTrkWithPt55BeforeIsoCuts)
removeCuts(isoTrkWithPt55BeforeValidPixelHitCuts, [cutTrkNValidPixelHitsSignal, cutTrkNValidHitsSignal, cutTrkNMissIn, cutTrkNMissMid])

isoTrkSelection = copy.deepcopy(basicSelection)
isoTrkSelection.name = cms.string("IsoTrkSelection")
addCuts(isoTrkSelection.cuts, isoTrkWithPt55Cuts)

isoTrkSelectionInvertDRJetCut = copy.deepcopy (isoTrkSelection)
isoTrkSelectionInvertDRJetCut.name = cms.string ("IsoTrkSelectionInvertDRJetCut")
removeCuts (isoTrkSelectionInvertDRJetCut.cuts, [cutTrkJetDeltaPhi])
addCuts (isoTrkSelectionInvertDRJetCut.cuts, [cutTrkJetDeltaPhiInvert])

isoTrkSelectionBeforeIsoCut = copy.deepcopy (basicSelection)
isoTrkSelectionBeforeIsoCut.name = cms.string ("IsoTrkSelectionBeforeIsoCut")
addCuts (isoTrkSelectionBeforeIsoCut.cuts, isoTrkWithPt55BeforeIsoCuts)

isoTrkSelectionBeforeValidPixelHits = copy.deepcopy(basicSelection)
isoTrkSelectionBeforeValidPixelHits.name = cms.string ("isoTrkSelectionBeforeValidPixelHits")
addCuts (isoTrkSelectionBeforeValidPixelHits.cuts, isoTrkWithPt55BeforeValidPixelHitCuts)

isoTrkSelectionBeforeValidPixelHitsMatching = copy.deepcopy(basicSelection)
isoTrkSelectionBeforeValidPixelHitsMatching.name = cms.string ("isoTrkSelectionBeforeValidPixelHitsMatching")
addCuts (isoTrkSelectionBeforeValidPixelHitsMatching.cuts, isoTrkWithPt55BeforeValidPixelHitCuts)
addSingleCut (isoTrkSelectionBeforeValidPixelHitsMatching.cuts, cutTrkMatchChargino, cutTrkFiducialECAL)

isoTrkSelectionBeforeD0DZ = copy.deepcopy(isoTrkSelectionBeforeIsoCut)
isoTrkSelectionBeforeD0DZ.name = cms.string("isoTrkSelectionBeforeD0DZ")
removeCuts (isoTrkSelectionBeforeD0DZ.cuts, [cutJetPt])
addCuts (isoTrkSelectionBeforeD0DZ.cuts, [cutTrkIso])

isoTrkSelectionBeforeIsoCutLargeIsoDiffPos = copy.deepcopy(isoTrkSelectionBeforeIsoCut)
isoTrkSelectionBeforeIsoCutLargeIsoDiffPos.name = cms.string("isoTrkSelectionBeforeIsoCutLargeIsoDiffPos")
addCuts (isoTrkSelectionBeforeIsoCutLargeIsoDiffPos.cuts, [cutTrkLargeIsoDiffPos])

isoTrkSelectionBeforeIsoCutLargeIsoDiffNeg = copy.deepcopy(isoTrkSelectionBeforeIsoCut)
isoTrkSelectionBeforeIsoCutLargeIsoDiffNeg.name = cms.string("isoTrkSelectionBeforeIsoCutLargeIsoDiffNeg")
addCuts (isoTrkSelectionBeforeIsoCutLargeIsoDiffNeg.cuts, [cutTrkLargeIsoDiffNeg])

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

ecaloSelection = copy.deepcopy(NoCuts)
ecaloSelection.name = cms.string("ecaloSelection")
ecaloCuts = [
    cutTrkEcalo
]
addCuts(ecaloSelection.cuts, ecaloCuts)

disTrkNoNMissOut = copy.deepcopy(disTrkSelection)
disTrkNoNMissOut.name = cms.string("DisTrkNoNMissOut")
removeCuts(disTrkNoNMissOut.cuts, [cutTrkNMissOut])

disTrkNoEcalo = copy.deepcopy(disTrkSelection)
disTrkNoEcalo.name = cms.string("DisTrkNoEcalo")
removeCuts(disTrkNoEcalo.cuts, [cutTrkEcalo])

disTrkNoNMissOutNoEcalo = copy.deepcopy(disTrkSelection)
disTrkNoNMissOutNoEcalo.name = cms.string("DisTrkNoNMissOutNoEcalo")
removeCuts(disTrkNoNMissOutNoEcalo.cuts, [cutTrkNMissOut, cutTrkEcalo])

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

justTriggersElecOnly = copy.deepcopy (justTriggers)
justTriggersElecOnly.name = cms.string ("JustTriggersElecTrigOnly")
justTriggersElecOnly.triggers = triggersSingleEle

justTriggersMuOnly = copy.deepcopy (justTriggers)
justTriggersMuOnly.name = cms.string ("JustTriggersMuTrigOnly")
justTriggersMuOnly.triggers = triggersSingleMu

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

createHitsVariations (justADisTrk, "justADisTrk")

justACandTrk = copy.deepcopy (justAVertex)
justACandTrk.name = cms.string ("JustACandTrk")
addCuts(justACandTrk.cuts, [cutTrkPt55] + candTrkCuts)

justACandTrkNoD0Cut = copy.deepcopy (justACandTrk)
justACandTrkNoD0Cut.name = cms.string ("JustACandTrkNoD0Cut")
removeCuts(justACandTrkNoD0Cut.cuts, [cutTrkD0])

justAFakeTrk = copy.deepcopy (justACandTrk)
justAFakeTrk.name = cms.string ("JustAFakeTrk")
addCuts(justAFakeTrk.cuts, [cutTrkMatchFake])

createHitsVariations (justAFakeTrk, "justAFakeTrk")

justARealTrk = copy.deepcopy (justACandTrk)
justARealTrk.name = cms.string ("JustARealTrk")
addCuts(justARealTrk.cuts, [cutTrkMatchReal])

createHitsVariations (justARealTrk, "justARealTrk")

justAFakeTrkNoD0Cut = copy.deepcopy (justACandTrkNoD0Cut)
justAFakeTrkNoD0Cut.name = cms.string ("JustAFakeTrkNoD0Cut")
addCuts(justAFakeTrkNoD0Cut.cuts, [cutTrkMatchFake])

createHitsVariations (justAFakeTrkNoD0Cut, "justAFakeTrkNoD0Cut")

justARealTrkNoD0Cut = copy.deepcopy (justACandTrkNoD0Cut)
justARealTrkNoD0Cut.name = cms.string ("JustARealTrkNoD0Cut")
addCuts(justARealTrkNoD0Cut.cuts, [cutTrkMatchReal])

createHitsVariations (justARealTrkNoD0Cut, "justARealTrkNoD0Cut")

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

createHitsVariations (candTrkIdElecPt35, "candTrkIdElecPt35")

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

createHitsVariations (candTrkIdMuPt35, "candTrkIdMuPt35")

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

createHitsVariations (candTrkIdTauPt55, "candTrkIdTauPt55")

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

createHitsVariations (disTrkIdFake, "disTrkIdFake")

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

createHitsVariations (disTrkSelection, "disTrkSelection")
createHitsVariations (disTrkNoNMissOut, "disTrkNoNMissOut")
createHitsVariations (disTrkNoEcalo, "disTrkNoEcalo")

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

createHitsVariations (zeroBiasSelectionDisTrk, "zeroBiasSelectionDisTrk")

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

createHitsVariations (zeroBiasJetSelectionDisTrk, "zeroBiasJetSelectionDisTrk")

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

disTrkSelectionNoD0Cut3Layers = copy.deepcopy(disTrkSelectionNoD0Cut)
disTrkSelectionNoD0Cut3Layers.name = cms.string("DisTrkSelectionNoD0Cut3Layers")
addSingleCut(disTrkSelectionNoD0Cut3Layers.cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
addSingleCut(disTrkSelectionNoD0Cut3Layers.cuts, cutTrkNLayersExclusive[3], cutTrkNValidHitsSignal)
removeCuts(disTrkSelectionNoD0Cut3Layers.cuts, [cutTrkNValidPixelHitsSignal, cutTrkNValidHitsSignal])

disTrkSelectionInvertD0Cut = copy.deepcopy(disTrkSelection)
disTrkSelectionInvertD0Cut.name = cms.string("DisTrkSelectionInvertD0Cut")
addSingleCut(disTrkSelectionInvertD0Cut.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(disTrkSelectionInvertD0Cut.cuts, [cutTrkD0])

disTrkSelectionSidebandD0Cut = copy.deepcopy(disTrkSelection)
disTrkSelectionSidebandD0Cut.name = cms.string("DisTrkSelectionSidebandD0Cut")
addSingleCut(disTrkSelectionSidebandD0Cut.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(disTrkSelectionSidebandD0Cut.cuts, [cutTrkD0])

disTrkSelectionSidebandD0CutNoHitsCut = copy.deepcopy(disTrkSelectionSidebandD0Cut)
disTrkSelectionSidebandD0CutNoHitsCut.name = cms.string("DisTrkSelectionSidebandD0CutNoHitsCut")
removeCuts(disTrkSelectionSidebandD0CutNoHitsCut.cuts, [cutTrkNValidPixelHitsSignal, cutTrkNValidHitsSignal])

createHitsVariations (disTrkSelectionNoD0Cut,       "disTrkSelectionNoD0Cut")
createHitsVariations (disTrkSelectionInvertD0Cut,   "disTrkSelectionInvertD0Cut")
createHitsVariations (disTrkSelectionSidebandD0Cut, "disTrkSelectionSidebandD0Cut")

##########################################################################
# Selections for a "very clean" 3-layer track sample 
# for the fake transfer factor
##########################################################################

veryClean3LayersCuts = [
    # 1) reject tracks with any inactive hits in MISSING_INNER_HITS
    cutTrkNoInvalidInnerHits,
    # 2) reject tracks with any inactive hits in TRACK_HITS
    cutTrkNoInvalidMiddleHits,
    # 3) require the HitPattern to be in a limited set of 4 combinations
    #    a) pxb 1, pxb 2, pxb 3 (missing pxb 4)
    #    b) pxb 1, pxb 2, pxf 1 (missing pxf 2)
    #    c) pxb 1, pxf 1, pxf 2 (missing pxf 3)
    #    d) pxf 1, pxf 2, pxf 3 (there is no pxf 4, but rule #4 and probably #5 below rejects this too)
    cutTrkAllowedThreeLayerHitPattern,
    # 4) require ==4 pixel layers hit with any quality (not null), and the outer-most must be MISSING
    cutTrkFourLayersAnyHitQuality,
    # 5) veto areas of the pixel where it's possible to get > 4 pixel layers (|eta| 1.5-2.3)
    cutTrkEta15,
]

disTrkSelectionNoD0Cut3LayersVeryClean = copy.deepcopy(disTrkSelectionNoD0Cut3Layers)
disTrkSelectionNoD0Cut3LayersVeryClean.name = cms.string("DisTrkSelectionNoD0Cut3LayersVeryClean")
addCuts(disTrkSelectionNoD0Cut3LayersVeryClean.cuts, veryClean3LayersCuts)

##########################################################################
# Testing MET Triggers for Luminosity
##########################################################################

metTrigAllYes = copy.deepcopy(NoCuts)
metTrigAllYes.name = cms.string("metTrigAllYes")
metTrigAllYes.triggers = triggersMetAllYes

metTrigAllYesNoDisabledB = copy.deepcopy(NoCuts)
metTrigAllYesNoDisabledB.name = cms.string("metTrigAllYesNoDisabledB")
metTrigAllYesNoDisabledB.triggers = triggersMetAllYesNoDisabledB

metTrigAllMaybes = copy.deepcopy(NoCuts)
metTrigAllMaybes.name = cms.string("metTrigAllMaybes")
metTrigAllMaybes.triggers = triggersMetAllMaybes

metTrigAllMaybesNoDisabledB = copy.deepcopy(NoCuts)
metTrigAllMaybesNoDisabledB.name = cms.string("metTrigAllMaybesNoDisabledB")
metTrigAllMaybesNoDisabledB.triggers = triggersMetAllMaybesNoDisabledB

metTrigJustMain = copy.deepcopy(NoCuts)
metTrigJustMain.name = cms.string("metTrigJustMain")
metTrigJustMain.triggers = triggersMetJustMain

metTrigOnlyPerfectNoMain2017 = copy.deepcopy(NoCuts)
metTrigOnlyPerfectNoMain2017.name = cms.string("metTrigOnlyPerfectNoMain2017")
metTrigOnlyPerfectNoMain2017.triggers = triggersMetOnlyPerfectNoMain2017

metTrigOnlyPerfectAndMain2017 = copy.deepcopy(NoCuts)
metTrigOnlyPerfectAndMain2017.name = cms.string("metTrigOnlyPerfectAndMain2017")
metTrigOnlyPerfectAndMain2017.triggers = triggersMetOnlyPerfectAndMain2017

metTrigAllUnprescaled2017 = copy.deepcopy(NoCuts)
metTrigAllUnprescaled2017.name = cms.string("metTrigAllUnprescaled2017")
metTrigAllUnprescaled2017.triggers = triggersMetAllUnprescaled2017

metTrigAllowDisabledHighPU2017 = copy.deepcopy(NoCuts)
metTrigAllowDisabledHighPU2017.name = cms.string("metTrigAllowDisabledHighPU2017")
metTrigAllowDisabledHighPU2017.triggers = triggersMetAllowDisabledHighPU2017

metTrigAllGoodInB = copy.deepcopy(NoCuts)
metTrigAllGoodInB.name = cms.string("metTrigAllGoodInB")
metTrigAllGoodInB.triggers = triggersMetAllGoodInB

##########################################################################
# Removes the random drops for testing purposes
##########################################################################

disTrkNoRandom = copy.deepcopy(disTrkSelection)
disTrkNoRandom.name = cms.string("disTrkNoRandom")
removeCuts(disTrkNoRandom.cuts, [cutTrkNMissOut,cutTrkNMissMid])
addCuts(disTrkNoRandom.cuts, [cutTrkNMissOutNoDrop,cutTrkNMissMidNoDrop])

#####################################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
