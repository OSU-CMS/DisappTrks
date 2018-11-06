import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

def createNHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_3_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

##################################################
## Electron tag skim
##################################################
ElectronTagSkim = cms.PSet(
    name = cms.string("ElectronTagSkim"),
    triggers = triggersSingleEle,
    metFilters = metFilters,
    cuts = cms.VPSet (),
)
tagElectronCuts = [
    cutMetFilters,
    cutElectronPt, # pt>25 for 2015-6, >35 for 2017
    cutElectronEta21,
    cutElectronTightID,
    cutElectronTightPFIso,
]
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    tagElectronCuts = [
        cutMetFilters,
        cutElectronPt,
        cutElectronEta21, # In 2017 there is no eta2p1 trigger, but tracks require |eta|<2.1 so keep this cut
        cutElectronVIDTightID, # ID + iso (no vertexing -- added below)
        cutElectronD02017,
        cutElectronDZ2017,
    ]
addCuts(ElectronTagSkim.cuts, tagElectronCuts)

################################################################################
## Testing channels to compare pat::IsolatedTrack to CandidateTrack
## in the SingleElectron dataset
################################################################################

MinimalEleTrackSelection = copy.deepcopy(ElectronTagSkim)
MinimalEleTrackSelection.name = cms.string("MinimalEleTrackSelection")
addCuts(MinimalEleTrackSelection.cuts, [cutTrkPt20])

MinimalEleMatchedCandidateTrackSelection = copy.deepcopy(MinimalEleTrackSelection)
MinimalEleMatchedCandidateTrackSelection.name = cms.string("MinimalEleMatchedCandidateTrackSelection")
addCuts(MinimalEleMatchedCandidateTrackSelection.cuts, [cutTrkMatchedCandidateTrack])

##################################################
## Higher pt to be closer to candidate track selection
##################################################
ElectronTagPt35 = copy.deepcopy(ElectronTagSkim)
ElectronTagPt35.name = cms.string("ElectronTagPt35")
addSingleCut(ElectronTagPt35.cuts, cutElectronPt35, cutElectronPt)
removeCuts(ElectronTagPt35.cuts, [cutElectronPt])
cutsToAdd = [
    cutElectronArbitration,
]
cutsToAdd += jetCuts
cutsToAdd += [
    cutTrkPt35,
    cutTrkElecDR0p1,
    cutTrkMatchRecoElec,
]
cutsToAdd += isoTrkCuts
addCuts(ElectronTagPt35.cuts, cutsToAdd)

ElectronTagPt35NoTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoTrig.name = cms.string("ElectronTagPt35NoTrig")
ElectronTagPt35NoTrig.triggers = cms.vstring()

ElectronTagPt35MetTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetTrig.name = cms.string("ElectronTagPt35MetTrig")
ElectronTagPt35MetTrig.triggers = triggersMet

ElectronTagPt35MetCut = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetCut.name = cms.string("ElectronTagPt35MetCut")
addCuts(ElectronTagPt35MetCut.cuts, [cutElectronMetMinusOne])

ElectronTagPt35NoJetCuts = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoJetCuts.name = cms.string("ElectronTagPt35NoJetCuts")
cutsToRemove = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
removeCuts(ElectronTagPt35NoJetCuts.cuts, cutsToRemove)

ElectronTagPt35NoJetCutsMetTrig = copy.deepcopy(ElectronTagPt35NoJetCuts)
ElectronTagPt35NoJetCutsMetTrig.name = cms.string("ElectronTagPt35NoJetCutsMetTrig")
ElectronTagPt35NoJetCutsMetTrig.triggers = triggersMet

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
ElectronTagPt55 = copy.deepcopy(ElectronTagPt35)
ElectronTagPt55.name = cms.string("ElectronTagPt55")
addSingleCut(ElectronTagPt55.cuts, cutTrkPt55, cutTrkPt35)
removeCuts(ElectronTagPt55.cuts, [cutTrkPt35])

ElectronTagPt55NoTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55NoTrig.name = cms.string("ElectronTagPt55NoTrig")
ElectronTagPt55NoTrig.triggers = cms.vstring()

ElectronTagPt55MetTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetTrig.name = cms.string("ElectronTagPt55MetTrig")
ElectronTagPt55MetTrig.triggers = triggersMet

ElectronTagPt55MetCut = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetCut.name = cms.string("ElectronTagPt55MetCut")
addCuts(ElectronTagPt55MetCut.cuts, [cutElectronMetMinusOne])

################################################################################
## Electron tag and probe sample
################################################################################
ZtoEleProbeTrkWithZCuts = copy.deepcopy(ElectronTagSkim)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
addSingleCut(ZtoEleProbeTrkWithZCuts.cuts, cutElectronMatchToTrigObj, cutElectronPt)
cutsToAdd = [
    cutElectronArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutEleTrkInvMass10,
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
    cutTrkArbitration,
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleProbeTrk = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrk.name = cms.string ("ZtoEleProbeTrk")
removeCuts (ZtoEleProbeTrk.cuts, [cutElectronArbitration, cutEleTrkInvMass10, cutTrkArbitration, cutEleTrkInvMass80To100, cutEleTrkOS])

ZtoEleProbeTrkWithFilter = copy.deepcopy (ZtoEleProbeTrk)
ZtoEleProbeTrkWithFilter.name = cms.string ("ZtoEleProbeTrkWithFilter")

ZtoEleProbeTrkWithSSFilter = copy.deepcopy (ZtoEleProbeTrk)
ZtoEleProbeTrkWithSSFilter.name = cms.string ("ZtoEleProbeTrkWithSSFilter")

ZtoEleProbeTrkBeforeArbitration = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkBeforeArbitration.name = cms.string ("ZtoEleProbeTrkBeforeArbitration")
removeCuts (ZtoEleProbeTrkBeforeArbitration.cuts, [cutTrkArbitration, cutEleTrkInvMass80To100, cutEleTrkOS])

ZtoEleProbeTrkWithoutD0Cut = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithoutD0Cut.name = cms.string ("ZtoEleProbeTrkWithoutD0Cut")
removeCuts (ZtoEleProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

ElectronFiducialCalcBefore = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ElectronFiducialCalcBefore.name = cms.string("ElectronFiducialCalcBefore")
removeCuts(ElectronFiducialCalcBefore.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    removeCuts(ElectronFiducialCalcBefore.cuts, [cutTrk2017LowEfficiencyRegion])

ElectronFiducialCalcBeforeInvestigate2017Ineff = copy.deepcopy(ElectronFiducialCalcBefore)
ElectronFiducialCalcBeforeInvestigate2017Ineff.name = cms.string("ElectronFiducialCalcBeforeInvestigate2017Ineff")
addCuts(ElectronFiducialCalcBeforeInvestigate2017Ineff.cuts, [cutTrkInvestigate2017Ineff])

ElectronFiducialCalcAfter = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ElectronFiducialCalcAfter.name = cms.string("ElectronFiducialCalcAfter")
addSingleCut(ElectronFiducialCalcAfter.cuts, cutTrkVetoElecVeto, cutEleTrkOS)
removeCuts(ElectronFiducialCalcAfter.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    removeCuts(ElectronFiducialCalcAfter.cuts, [cutTrk2017LowEfficiencyRegion])

ZtoEleDisTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
addSingleCut(ZtoEleDisTrk.cuts, cutTrkNMissOut, cutEleTrkOS)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkEcalo,    cutEleTrkOS)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkElecVeto, cutEleTrkOS)

ZtoEleDisTrkNoNMissOutCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoNMissOutCut.name = cms.string("ZtoEleDisTrkNoNMissOutCut")
removeCuts (ZtoEleDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

ElectronTagPt55NoValidHitsCut = copy.deepcopy (ElectronTagPt55)
ElectronTagPt55NoValidHitsCut.name = cms.string ("ElectronTagPt55NoValidHitsCut")
removeCuts (ElectronTagPt55NoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ElectronTagPt55MetTrigNoValidHitsCut = copy.deepcopy (ElectronTagPt55MetTrig)
ElectronTagPt55MetTrigNoValidHitsCut.name = cms.string ("ElectronTagPt55MetTrigNoValidHitsCut")
removeCuts (ElectronTagPt55MetTrigNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoEleProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoEleProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoEleProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

ZtoEleDisTrkNoValidHitsCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoValidHitsCut.name = cms.string("ZtoEleDisTrkNoValidHitsCut")
removeCuts(ZtoEleDisTrkNoValidHitsCut.cuts, [cutTrkNValidHitsSignal])

################################################################################
## Channels with reduced numbers of hits
################################################################################
createNHitsVariations (ElectronTagPt55,         "ElectronTagPt55")
createNHitsVariations (ElectronTagPt55MetTrig,  "ElectronTagPt55MetTrig")
createNHitsVariations (ZtoEleProbeTrkWithZCuts, "ZtoEleProbeTrkWithZCuts")
createNHitsVariations (ZtoEleDisTrk,            "ZtoEleDisTrk")

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
    