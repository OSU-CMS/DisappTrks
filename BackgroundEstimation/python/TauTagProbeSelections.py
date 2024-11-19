import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
from DisappTrks.BackgroundEstimation.ElectronTagProbeSelections import *  # Get the composite cut definitions
from DisappTrks.BackgroundEstimation.MuonTagProbeSelections import *  # Get the composite cut definitions

def createHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, None, cutTrkNLayersVariations))
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
        replaceSingleCut (globals ()[chName + 'NLayers3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

################################################################################
## Tau tag skim
################################################################################
TauTagSkim = cms.PSet(
    name = cms.string("TauTagSkim"),
    triggers = triggersSingleTau,
    metFilters = metFilters,
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagTauCuts = [
    cutMetFilters,
    cutTauPt50,
    cutTauEta21,
    cutTauTightID,
]
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    tagTauCuts.append(cutTauTightMVAIso)
else:
    tagTauCuts.append(cutTauTightPFIso)
addCuts(TauTagSkim.cuts, tagTauCuts)

################################################################################
## Testing channels to compare pat::IsolatedTrack to CandidateTrack
## in the Tau dataset
################################################################################

MinimalTauTrackSelection = copy.deepcopy(TauTagSkim)
MinimalTauTrackSelection.name = cms.string("MinimalTauTrackSelection")
addCuts(MinimalTauTrackSelection.cuts, [cutTrkPt20])

MinimalTauMatchedCandidateTrackSelection = copy.deepcopy(MinimalTauTrackSelection)
MinimalTauMatchedCandidateTrackSelection.name = cms.string("MinimalTauMatchedCandidateTrackSelection")
addCuts(MinimalTauMatchedCandidateTrackSelection.cuts, [cutTrkMatchedCandidateTrack])

##################################################
## Cannot go lower than 50 GeV because of trigger
##################################################
TauTagPt50 = copy.deepcopy(TauTagSkim)
TauTagPt50.name = cms.string("TauTagPt50")
cutsToAdd = [
    cutTauArbitration,
]
cutsToAdd += jetCuts
cutsToAdd += [
    cutTrkPt50,
    cutTrkTauDR0p1,
    cutTrkMatchRecoTau,
]
cutsToAdd += isoTrkCuts
addCuts(TauTagPt50.cuts, cutsToAdd)
removeCuts(TauTagPt50.cuts, [cutTrkJetDeltaPhi])

TauTagPt50NoTrig = copy.deepcopy(TauTagPt50)
TauTagPt50NoTrig.name = cms.string("TauTagPt50NoTrig")
TauTagPt50NoTrig.triggers = cms.vstring()

TauTagPt50MetTrig = copy.deepcopy(TauTagPt50)
TauTagPt50MetTrig.name = cms.string("TauTagPt50MetTrig")
TauTagPt50MetTrig.triggers = triggersMet

TauTagPt50MetCut = copy.deepcopy(TauTagPt50)
TauTagPt50MetCut.name = cms.string("TauTagPt50MetCut")
addCuts(TauTagPt50MetCut.cuts, [cutTauMetMinusOne])

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
TauTagPt55 = copy.deepcopy(TauTagPt50)
TauTagPt55.name = cms.string("TauTagPt55")
addSingleCut(TauTagPt55.cuts, cutTrkPt55, cutTrkPt50)
removeCuts(TauTagPt55.cuts, [cutTrkPt50])

TauTagPt55NoTrig = copy.deepcopy(TauTagPt55)
TauTagPt55NoTrig.name = cms.string("TauTagPt55NoTrig")
TauTagPt55NoTrig.triggers = cms.vstring()

TauTagPt55MetTrig = copy.deepcopy(TauTagPt55)
TauTagPt55MetTrig.name = cms.string("TauTagPt55MetTrig")
TauTagPt55MetTrig.triggers = triggersMet

TauTagPt55MetCut = copy.deepcopy(TauTagPt55)
TauTagPt55MetCut.name = cms.string("TauTagPt55MetCut")
addCuts(TauTagPt55MetCut.cuts, [cutTauMetMinusOne])

TauTagPt55NoJetCuts = copy.deepcopy(TauTagPt55)
TauTagPt55NoJetCuts.name = cms.string("TauTagPt55NoJetCuts")
cutsToRemove = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
removeCuts(TauTagPt55NoJetCuts.cuts, cutsToRemove)

TauTagPt55NoJetCutsMetTrig = copy.deepcopy(TauTagPt55NoJetCuts)
TauTagPt55NoJetCutsMetTrig.name = cms.string("TauTagPt55NoJetCutsMetTrig")
TauTagPt55NoJetCutsMetTrig.triggers = triggersMet

################################################################################
# Versions of the above with a veto on MET phi do deal with HEM 15/16
# in 2018 CD
################################################################################

TauTagPt55HEMveto = copy.deepcopy(TauTagPt55)
TauTagPt55HEMveto.name = cms.string("TauTagPt55HEMveto")
addCuts(TauTagPt55HEMveto.cuts, [cutVetoMetPhiHEM1516])

TauTagPt55MetTrigHEMveto = copy.deepcopy(TauTagPt55MetTrig)
TauTagPt55MetTrigHEMveto.name = cms.string("TauTagPt55MetTrigHEMveto")
addCuts(TauTagPt55MetTrigHEMveto.cuts, [cutVetoMetPhiHEM1516])

################################################################################
## Tau tag and probe sample
################################################################################
# after invariant mass cut of 10 GeV
    #cutMuTrkDeltaPhi,
    #cutMuTrkMETBalance,
# after muon arbitration
    #cutLowMet,
    #cutNJetsLE2,

ZtoTauToMuProbeTrkWithZCuts = copy.deepcopy(MuonTagSkim)
ZtoTauToMuProbeTrkWithZCuts.name = cms.string("ZtoTauToMuProbeTrkWithZCuts")
addSingleCut(ZtoTauToMuProbeTrkWithZCuts.cuts, cutMuonMatchToTrigObj, cutMuonPt)
cutsToAdd = [
    cutMuonLowMT,
    cutMuonArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutMuTrkInvMass10,
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkArbitration,
    cutMuTrkInvMass40To75,
    cutMuTrkOS,
]
addCuts(ZtoTauToMuProbeTrkWithZCuts.cuts, cutsToAdd)
removeCuts(ZtoTauToMuProbeTrkWithZCuts.cuts, [cutTrkJetDeltaPhi])

ZtoTauToMuProbeTrk = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrk.name = cms.string ("ZtoTauToMuProbeTrk")
removeCuts (ZtoTauToMuProbeTrk.cuts, [cutMuonArbitration, cutMuTrkInvMass10, cutTrkArbitration, cutMuTrkInvMass40To75, cutMuTrkOS])

ZtoTauToMuProbeTrkWithFilter = copy.deepcopy (ZtoTauToMuProbeTrk)
ZtoTauToMuProbeTrkWithFilter.name = cms.string ("ZtoTauToMuProbeTrkWithFilter")

ZtoTauToMuProbeTrkWithSSFilter = copy.deepcopy (ZtoTauToMuProbeTrk)
ZtoTauToMuProbeTrkWithSSFilter.name = cms.string ("ZtoTauToMuProbeTrkWithSSFilter")

########
# Versions of the P(veto) numerators with veto/loose IDs applied to electrons/muons instead of no ID at all
# from EXO-19-010 pre-approval question May 31st 2019
ZtoTauToMuProbeTrkWithLooseFilter = copy.deepcopy(ZtoTauToMuProbeTrkWithFilter)
ZtoTauToMuProbeTrkWithLooseFilter.name = cms.string ("ZtoTauToMuProbeTrkWithLooseFilter")
replaceSingleCut(ZtoTauToMuProbeTrkWithLooseFilter.cuts, cutTrkVetoElecVeto, cutTrkElecVeto)

ZtoTauToMuProbeTrkWithLooseSSFilter = copy.deepcopy(ZtoTauToMuProbeTrkWithSSFilter)
ZtoTauToMuProbeTrkWithLooseSSFilter.name = cms.string ("ZtoTauToMuProbeTrkWithLooseSSFilter")
replaceSingleCut(ZtoTauToMuProbeTrkWithLooseSSFilter.cuts, cutTrkVetoElecVeto, cutTrkElecVeto)
########

ZtoTauToMuProbeTrkWithoutD0Cut = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithoutD0Cut.name = cms.string ("ZtoTauToMuProbeTrkWithoutD0Cut")
removeCuts (ZtoTauToMuProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

ZtoTauToMuDisTrk = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuDisTrk.name = cms.string("ZtoTauToMuDisTrk")
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkNMissOut, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkEcalo, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkJetDeltaPhi, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkTauHadVeto, cutMuTrkOS)

ZtoTauToMuDisTrkNoNMissOutCut = copy.deepcopy(ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNoNMissOutCut.name = cms.string("ZtoTauToMuDisTrkNoNMissOutCut")
removeCuts (ZtoTauToMuDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

TauTagPt55NoValidHitsCut = copy.deepcopy (TauTagPt55)
TauTagPt55NoValidHitsCut.name = cms.string ("TauTagPt55NoValidHitsCut")
removeCuts (TauTagPt55NoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

TauTagPt55MetTrigNoValidHitsCut = copy.deepcopy (TauTagPt55MetTrig)
TauTagPt55MetTrigNoValidHitsCut.name = cms.string ("TauTagPt55MetTrigNoValidHitsCut")
removeCuts (TauTagPt55MetTrigNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoTauToMuDisTrkNoValidHitsCut = copy.deepcopy(ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNoValidHitsCut.name = cms.string("ZtoTauToMuDisTrkNoValidHitsCut")
removeCuts(ZtoTauToMuDisTrkNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoTauToMuProbeTrkWithZCutsBetterPurity = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsBetterPurity.name = cms.string("ZtoTauToMuProbeTrkWithZCutsBetterPurity")
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutMuTrkMETBalance, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutMuTrkDeltaPhi, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutNJetsLE2, cutMuonArbitration)
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutLowMet, cutMuonArbitration)

ZtoTauToMuDisTrkBetterPurity = copy.deepcopy(ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkBetterPurity.name = cms.string("ZtoTauToMuDisTrkBetterPurity")
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutMuTrkMETBalance, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutMuTrkDeltaPhi, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutNJetsLE2, cutMuonArbitration)
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutLowMet, cutMuonArbitration)

################################################################################

ZtoTauToEleProbeTrkWithZCuts = copy.deepcopy(ElectronTagSkim)
ZtoTauToEleProbeTrkWithZCuts.name = cms.string("ZtoTauToEleProbeTrkWithZCuts")
addSingleCut(ZtoTauToEleProbeTrkWithZCuts.cuts, cutElectronMatchToTrigObj, cutElectronPt)
cutsToAdd = [
    cutElectronLowMT,
    cutElectronArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutEleTrkInvMass10,
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkArbitration,
    cutEleTrkInvMass40To75,
    cutEleTrkOS,
]
addCuts(ZtoTauToEleProbeTrkWithZCuts.cuts, cutsToAdd)
removeCuts(ZtoTauToEleProbeTrkWithZCuts.cuts, [cutTrkJetDeltaPhi])

ZtoTauToEleProbeTrk = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrk.name = cms.string ("ZtoTauToEleProbeTrk")
removeCuts (ZtoTauToEleProbeTrk.cuts, [cutElectronArbitration, cutEleTrkInvMass10, cutTrkArbitration, cutEleTrkInvMass40To75,cutEleTrkOS])

ZtoTauToEleProbeTrkWithFilter = copy.deepcopy (ZtoTauToEleProbeTrk)
ZtoTauToEleProbeTrkWithFilter.name = cms.string ("ZtoTauToEleProbeTrkWithFilter")

ZtoTauToEleProbeTrkWithSSFilter = copy.deepcopy (ZtoTauToEleProbeTrk)
ZtoTauToEleProbeTrkWithSSFilter.name = cms.string ("ZtoTauToEleProbeTrkWithSSFilter")

########
# Versions of the P(veto) numerators with veto/loose IDs applied to electrons/muons instead of no ID at all
# from EXO-19-010 pre-approval question May 31st 2019
ZtoTauToEleProbeTrkWithLooseFilter = copy.deepcopy(ZtoTauToEleProbeTrkWithFilter)
ZtoTauToEleProbeTrkWithLooseFilter.name = cms.string ("ZtoTauToEleProbeTrkWithLooseFilter")
replaceSingleCut(ZtoTauToEleProbeTrkWithLooseFilter.cuts, cutTrkLooseMuonVeto, cutTrkMuonVeto)

ZtoTauToEleProbeTrkWithLooseSSFilter = copy.deepcopy(ZtoTauToEleProbeTrkWithSSFilter)
ZtoTauToEleProbeTrkWithLooseSSFilter.name = cms.string ("ZtoTauToEleProbeTrkWithLooseSSFilter")
replaceSingleCut(ZtoTauToEleProbeTrkWithLooseSSFilter.cuts, cutTrkLooseMuonVeto, cutTrkMuonVeto)
########

ZtoTauToEleProbeTrkWithoutD0Cut = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithoutD0Cut.name = cms.string ("ZtoTauToEleProbeTrkWithoutD0Cut")
removeCuts (ZtoTauToEleProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

ZtoTauToEleDisTrk = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleDisTrk.name = cms.string("ZtoTauToEleDisTrk")
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkNMissOut, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkEcalo, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkJetDeltaPhi, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkTauHadVeto, cutEleTrkOS)

ZtoTauToEleDisTrkNoNMissOutCut = copy.deepcopy(ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNoNMissOutCut.name = cms.string("ZtoTauToEleDisTrkNoNMissOutCut")
removeCuts (ZtoTauToEleDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoTauToEleDisTrkNoValidHitsCut = copy.deepcopy(ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNoValidHitsCut.name = cms.string("ZtoTauToEleDisTrkNoValidHitsCut")
removeCuts(ZtoTauToEleDisTrkNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoTauToEleProbeTrkWithZCutsBetterPurity = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsBetterPurity.name = cms.string("ZtoTauToEleProbeTrkWithZCutsBetterPurity")
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutEleTrkMETBalance, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutEleTrkDeltaPhi, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutNJetsLE2, cutElectronArbitration)
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutLowMet, cutElectronArbitration)

ZtoTauToEleDisTrkBetterPurity = copy.deepcopy(ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkBetterPurity.name = cms.string("ZtoTauToEleDisTrkBetterPurity")
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutEleTrkMETBalance, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutEleTrkDeltaPhi, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutNJetsLE2, cutElectronArbitration)
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutLowMet, cutElectronArbitration)

################################################################################
## Channels with reduced numbers of hits
################################################################################
createHitsVariations (TauTagPt55,                      "TauTagPt55")
createHitsVariations (TauTagPt55MetTrig,               "TauTagPt55MetTrig")
createHitsVariations (TauTagPt55HEMveto,               "TauTagPt55HEMveto")
createHitsVariations (TauTagPt55MetTrigHEMveto,        "TauTagPt55MetTrigHEMveto")
createHitsVariations (ZtoTauToMuProbeTrk,              "ZtoTauToMuProbeTrk")
createHitsVariations (ZtoTauToMuProbeTrkWithFilter,    "ZtoTauToMuProbeTrkWithFilter")
createHitsVariations (ZtoTauToMuProbeTrkWithSSFilter,  "ZtoTauToMuProbeTrkWithSSFilter")
createHitsVariations (ZtoTauToMuProbeTrkWithLooseFilter,    "ZtoTauToMuProbeTrkWithLooseFilter")
createHitsVariations (ZtoTauToMuProbeTrkWithLooseSSFilter,  "ZtoTauToMuProbeTrkWithLooseSSFilter")
createHitsVariations (ZtoTauToEleProbeTrk,             "ZtoTauToEleProbeTrk")
createHitsVariations (ZtoTauToEleProbeTrkWithFilter,   "ZtoTauToEleProbeTrkWithFilter")
createHitsVariations (ZtoTauToEleProbeTrkWithSSFilter, "ZtoTauToEleProbeTrkWithSSFilter")
createHitsVariations (ZtoTauToEleProbeTrkWithLooseFilter,   "ZtoTauToEleProbeTrkWithLooseFilter")
createHitsVariations (ZtoTauToEleProbeTrkWithLooseSSFilter, "ZtoTauToEleProbeTrkWithLooseSSFilter")
createHitsVariations (ZtoTauToMuProbeTrkWithZCuts,     "ZtoTauToMuProbeTrkWithZCuts")
createHitsVariations (ZtoTauToEleProbeTrkWithZCuts,    "ZtoTauToEleProbeTrkWithZCuts")
createHitsVariations (ZtoTauToMuDisTrk,                "ZtoTauToMuDisTrk")
createHitsVariations (ZtoTauToEleDisTrk,               "ZtoTauToEleDisTrk")
createHitsVariations (TauTagPt55NoJetCuts,             "TauTagPt55NoJetCuts")
createHitsVariations (TauTagPt55NoJetCutsMetTrig,      "TauTagPt55NoJetCutsMetTrig")

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
