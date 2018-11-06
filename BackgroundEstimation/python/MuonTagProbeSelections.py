import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

def createNHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_3_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

################################################################################
## Muon tag skim
################################################################################
MuonTagSkim = cms.PSet(
    name = cms.string("MuonTagSkim"),
    triggers = triggersSingleMu,
    metFilters = metFilters,
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagMuonCuts = [
    cutMetFilters,
    cutMuonPt, # this will be >22 for 76X and >26 for 80X
    cutMuonEta21,
    cutMuonTightID,
    cutMuonTightPFIso,
]
addCuts(MuonTagSkim.cuts, tagMuonCuts)

################################################################################
## Testing channels to compare pat::IsolatedTrack to CandidateTrack
## in the SingleMuon dataset
################################################################################

MinimalMuonTrackSelection = copy.deepcopy(MuonTagSkim)
MinimalMuonTrackSelection.name = cms.string("MinimalMuonTrackSelection")
addCuts(MinimalMuonTrackSelection.cuts, [cutTrkPt20])

MinimalMuonMatchedCandidateTrackSelection = copy.deepcopy(MinimalMuonTrackSelection)
MinimalMuonMatchedCandidateTrackSelection.name = cms.string("MinimalMuonMatchedCandidateTrackSelection")
addCuts(MinimalMuonMatchedCandidateTrackSelection.cuts, [cutTrkMatchedCandidateTrack])

##################################################
## Higher pt to be closer to candidate track selection
##################################################
MuonTagPt35 = copy.deepcopy(MuonTagSkim)
MuonTagPt35.name = cms.string("MuonTagPt35")
addSingleCut(MuonTagPt35.cuts, cutMuonPt35, cutMuonPt)
removeCuts(MuonTagPt35.cuts, [cutMuonPt])
cutsToAdd = [
    cutMuonArbitration,
]
cutsToAdd += jetCuts
cutsToAdd += [
    cutTrkPt35,
    cutTrkMuDR0p1,
    cutTrkMatchRecoMu,
]
cutsToAdd += isoTrkCuts
addCuts(MuonTagPt35.cuts, cutsToAdd)

MuonTagPt35NoTrig = copy.deepcopy(MuonTagPt35)
MuonTagPt35NoTrig.name = cms.string("MuonTagPt35NoTrig")
MuonTagPt35NoTrig.triggers = cms.vstring()

MuonTagPt35MetTrig = copy.deepcopy(MuonTagPt35)
MuonTagPt35MetTrig.name = cms.string("MuonTagPt35MetTrig")
MuonTagPt35MetTrig.triggers = triggersMet

MuonTagPt35MetCut = copy.deepcopy(MuonTagPt35)
MuonTagPt35MetCut.name = cms.string("MuonTagPt35MetCut")
addCuts(MuonTagPt35MetCut.cuts, [cutMuonMetMinusOne])

MuonTagPt35NoJetCuts = copy.deepcopy(MuonTagPt35)
MuonTagPt35NoJetCuts.name = cms.string("MuonTagPt35NoJetCuts")
cutsToRemove = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
removeCuts(MuonTagPt35NoJetCuts.cuts, cutsToRemove)

MuonTagPt35NoJetCutsMetTrig = copy.deepcopy(MuonTagPt35NoJetCuts)
MuonTagPt35NoJetCutsMetTrig.name = cms.string("MuonTagPt35NoJetCutsMetTrig")
MuonTagPt35NoJetCutsMetTrig.triggers = triggersMet

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
MuonTagPt55 = copy.deepcopy(MuonTagPt35)
MuonTagPt55.name = cms.string("MuonTagPt55")
addSingleCut(MuonTagPt55.cuts, cutTrkPt55, cutTrkPt35)
removeCuts(MuonTagPt55.cuts, [cutTrkPt35])
addCuts(MuonTagPt55.cuts, [cutTrkEcalo])

MuonTagPt55NoTrig = copy.deepcopy(MuonTagPt55)
MuonTagPt55NoTrig.name = cms.string("MuonTagPt55NoTrig")
MuonTagPt55NoTrig.triggers = cms.vstring()

MuonTagPt55MetTrig = copy.deepcopy(MuonTagPt55)
MuonTagPt55MetTrig.name = cms.string("MuonTagPt55MetTrig")
MuonTagPt55MetTrig.triggers = triggersMet

MuonTagPt55MetCut = copy.deepcopy(MuonTagPt55)
MuonTagPt55MetCut.name = cms.string("MuonTagPt55MetCut")
addCuts(MuonTagPt55MetCut.cuts, [cutMuonMetMinusOne])

################################################################################
## Muon tag and probe sample
################################################################################
ZtoMuProbeTrkWithZCuts = copy.deepcopy(MuonTagSkim)
ZtoMuProbeTrkWithZCuts.name = cms.string("ZtoMuProbeTrkWithZCuts")
addSingleCut(ZtoMuProbeTrkWithZCuts.cuts, cutMuonMatchToTrigObj, cutMuonPt)
cutsToAdd = [
    cutMuonArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutMuTrkInvMass10,
    cutTrkElecVeto,
    cutTrkTauHadVeto,
    cutTrkEcalo,
    cutTrkArbitration,
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
]
addCuts(ZtoMuProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoMuDummyTrk = copy.deepcopy(MuonTagSkim)
ZtoMuDummyTrk.name = cms.string("ZtoMuDummyTrk")
addCuts(ZtoMuDummyTrk.cuts, [cutTrkDummy])

ZtoMuDummyTrkWithJetFilter = copy.deepcopy(ZtoMuDummyTrk)
ZtoMuDummyTrkWithJetFilter.name = cms.string("ZtoMuDummyTrkWithJetFilter")

ZtoMuProbeTrk = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrk.name = cms.string ("ZtoMuProbeTrk")
removeCuts (ZtoMuProbeTrk.cuts, [cutMuonArbitration, cutMuTrkInvMass10, cutTrkArbitration, cutMuTrkInvMass80To100, cutMuTrkOS])

ZtoMuProbeTrkWithFilter = copy.deepcopy (ZtoMuProbeTrk)
ZtoMuProbeTrkWithFilter.name = cms.string ("ZtoMuProbeTrkWithFilter")

ZtoMuProbeTrkWithSSFilter = copy.deepcopy (ZtoMuProbeTrk)
ZtoMuProbeTrkWithSSFilter.name = cms.string ("ZtoMuProbeTrkWithSSFilter")

ZtoMuProbeTrkBeforeArbitration = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkBeforeArbitration.name = cms.string ("ZtoMuProbeTrkBeforeArbitration")
removeCuts (ZtoMuProbeTrkBeforeArbitration.cuts, [cutTrkArbitration, cutMuTrkInvMass80To100, cutMuTrkOS])

ZtoMuProbeTrkWithoutD0Cut = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithoutD0Cut.name = cms.string ("ZtoMuProbeTrkWithoutD0Cut")
removeCuts (ZtoMuProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

MuonFiducialCalcBefore = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
MuonFiducialCalcBefore.name = cms.string("MuonFiducialCalcBefore")
removeCuts(MuonFiducialCalcBefore.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    removeCuts(MuonFiducialCalcBefore.cuts, [cutTrk2017LowEfficiencyRegion])

MuonFiducialCalcBeforeInvestigate2017Ineff = copy.deepcopy(MuonFiducialCalcBefore)
MuonFiducialCalcBeforeInvestigate2017Ineff.name = cms.string("MuonFiducialCalcBeforeInvestigate2017Ineff")
addCuts(MuonFiducialCalcBeforeInvestigate2017Ineff.cuts, [cutTrkInvestigate2017Ineff])

MuonFiducialCalcAfter = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
MuonFiducialCalcAfter.name = cms.string("MuonFiducialCalcAfter")
addCuts(MuonFiducialCalcAfter.cuts, [cutTrkLooseMuonVeto])
removeCuts(MuonFiducialCalcAfter.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    removeCuts(MuonFiducialCalcAfter.cuts, [cutTrk2017LowEfficiencyRegion])

ZtoMuDisTrk = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuDisTrk.name = cms.string("ZtoMuDisTrk")
addSingleCut(ZtoMuDisTrk.cuts, cutTrkNMissOut, cutMuTrkOS)
addSingleCut(ZtoMuDisTrk.cuts, cutTrkMuonVeto, cutMuTrkOS)

ZtoMuDisTrkNoNMissOutCut = copy.deepcopy(ZtoMuDisTrk)
ZtoMuDisTrkNoNMissOutCut.name = cms.string("ZtoMuDisTrkNoNMissOutCut")
removeCuts (ZtoMuDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

MuonTagPt55NoValidHitsCut = copy.deepcopy (MuonTagPt55)
MuonTagPt55NoValidHitsCut.name = cms.string ("MuonTagPt55NoValidHitsCut")
removeCuts (MuonTagPt55NoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

MuonTagPt55MetTrigNoValidHitsCut = copy.deepcopy (MuonTagPt55MetTrig)
MuonTagPt55MetTrigNoValidHitsCut.name = cms.string ("MuonTagPt55MetTrigNoValidHitsCut")
removeCuts (MuonTagPt55MetTrigNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoMuProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoMuProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoMuProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoMuDisTrkNoValidHitsCut = copy.deepcopy(ZtoMuDisTrk)
ZtoMuDisTrkNoValidHitsCut.name = cms.string("ZtoMuDisTrkNoValidHitsCut")
removeCuts(ZtoMuDisTrkNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

################################################################################
## Channels with reduced numbers of hits
################################################################################
createNHitsVariations (MuonTagPt55,            "MuonTagPt55")
createNHitsVariations (MuonTagPt55MetTrig,     "MuonTagPt55MetTrig")
createNHitsVariations (ZtoMuProbeTrkWithZCuts, "ZtoMuProbeTrkWithZCuts")
createNHitsVariations (ZtoMuDisTrk,            "ZtoMuDisTrk")

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

# For evaluating the Isolated Track Cut (cutTrkIso) for variables available in IsolatedTrack object

MuonFiducialCalcCutsBeforeIsoTrk = copy.deepcopy(MuonTagSkim)
MuonFiducialCalcCutsBeforeIsoTrk.name = cms.string("MuonFiducialCalcCutsBeforeIsoTrk")
addSingleCut(MuonFiducialCalcCutsBeforeIsoTrk.cuts, cutMuonMatchToTrigObj, cutMuonPt)
cutsToAdd = [
    cutMuonArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
removeCuts(cutsToAdd, [cutTrkJetDeltaPhi, cutTrkDZ, cutTrkD0, cutTrkIso])
addCuts(MuonFiducialCalcCutsBeforeIsoTrk.cuts, cutsToAdd)
