import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

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

MuonFiducialCalcAfter = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
MuonFiducialCalcAfter.name = cms.string("MuonFiducialCalcAfter")
addCuts(MuonFiducialCalcAfter.cuts, [cutTrkLooseMuonVeto])
removeCuts(MuonFiducialCalcAfter.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

ZtoMuDisTrk = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuDisTrk.name = cms.string("ZtoMuDisTrk")
addSingleCut(ZtoMuDisTrk.cuts, cutTrkNMissOut, cutMuTrkOS)
addSingleCut(ZtoMuDisTrk.cuts, cutTrkMuonVeto, cutMuTrkOS)

ZtoMuDisTrkNoNMissOutCut = copy.deepcopy(ZtoMuDisTrk)
ZtoMuDisTrkNoNMissOutCut.name = cms.string("ZtoMuDisTrkNoNMissOutCut")
removeCuts (ZtoMuDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

MuonTagPt55NoValidHitsCut = copy.deepcopy (MuonTagPt55)
MuonTagPt55NoValidHitsCut.name = cms.string ("MuonTagPt55NoValidHitsCut")
removeCuts (MuonTagPt55NoValidHitsCut.cuts, [cutTrkNValidHits])

MuonTagPt55MetTrigNoValidHitsCut = copy.deepcopy (MuonTagPt55MetTrig)
MuonTagPt55MetTrigNoValidHitsCut.name = cms.string ("MuonTagPt55MetTrigNoValidHitsCut")
removeCuts (MuonTagPt55MetTrigNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoMuProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoMuProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoMuProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoMuDisTrkNoValidHitsCut = copy.deepcopy(ZtoMuDisTrk)
ZtoMuDisTrkNoValidHitsCut.name = cms.string("ZtoMuDisTrkNoValidHitsCut")
removeCuts(ZtoMuDisTrkNoValidHitsCut.cuts, [cutTrkNValidHits])

################################################################################
## Channels with reduced numbers of hits
################################################################################
MuonTagPt55NHits3 = copy.deepcopy (MuonTagPt55)
MuonTagPt55NHits3.name = cms.string ("MuonTagPt55NHits3")
addSingleCut (MuonTagPt55NHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (MuonTagPt55NHits3.cuts, [cutTrkNValidHits])

MuonTagPt55NHits4 = copy.deepcopy (MuonTagPt55)
MuonTagPt55NHits4.name = cms.string ("MuonTagPt55NHits4")
addSingleCut (MuonTagPt55NHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (MuonTagPt55NHits4.cuts, [cutTrkNValidHits])

MuonTagPt55NHits5 = copy.deepcopy (MuonTagPt55)
MuonTagPt55NHits5.name = cms.string ("MuonTagPt55NHits5")
addSingleCut (MuonTagPt55NHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (MuonTagPt55NHits5.cuts, [cutTrkNValidHits])

MuonTagPt55NHits6 = copy.deepcopy (MuonTagPt55)
MuonTagPt55NHits6.name = cms.string ("MuonTagPt55NHits6")
addSingleCut (MuonTagPt55NHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (MuonTagPt55NHits6.cuts, [cutTrkNValidHits])

MuonTagPt55MetTrigNHits3 = copy.deepcopy (MuonTagPt55MetTrig)
MuonTagPt55MetTrigNHits3.name = cms.string ("MuonTagPt55MetTrigNHits3")
addSingleCut (MuonTagPt55MetTrigNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (MuonTagPt55MetTrigNHits3.cuts, [cutTrkNValidHits])

MuonTagPt55MetTrigNHits4 = copy.deepcopy (MuonTagPt55MetTrig)
MuonTagPt55MetTrigNHits4.name = cms.string ("MuonTagPt55MetTrigNHits4")
addSingleCut (MuonTagPt55MetTrigNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (MuonTagPt55MetTrigNHits4.cuts, [cutTrkNValidHits])

MuonTagPt55MetTrigNHits5 = copy.deepcopy (MuonTagPt55MetTrig)
MuonTagPt55MetTrigNHits5.name = cms.string ("MuonTagPt55MetTrigNHits5")
addSingleCut (MuonTagPt55MetTrigNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (MuonTagPt55MetTrigNHits5.cuts, [cutTrkNValidHits])

MuonTagPt55MetTrigNHits6 = copy.deepcopy (MuonTagPt55MetTrig)
MuonTagPt55MetTrigNHits6.name = cms.string ("MuonTagPt55MetTrigNHits6")
addSingleCut (MuonTagPt55MetTrigNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (MuonTagPt55MetTrigNHits6.cuts, [cutTrkNValidHits])

ZtoMuProbeTrkWithZCutsNHits3 = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNHits3.name = cms.string ("ZtoMuProbeTrkWithZCutsNHits3")
addSingleCut (ZtoMuProbeTrkWithZCutsNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoMuProbeTrkWithZCutsNHits3.cuts, [cutTrkNValidHits])

ZtoMuProbeTrkWithZCutsNHits4 = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNHits4.name = cms.string ("ZtoMuProbeTrkWithZCutsNHits4")
addSingleCut (ZtoMuProbeTrkWithZCutsNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoMuProbeTrkWithZCutsNHits4.cuts, [cutTrkNValidHits])

ZtoMuProbeTrkWithZCutsNHits5 = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNHits5.name = cms.string ("ZtoMuProbeTrkWithZCutsNHits5")
addSingleCut (ZtoMuProbeTrkWithZCutsNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoMuProbeTrkWithZCutsNHits5.cuts, [cutTrkNValidHits])

ZtoMuProbeTrkWithZCutsNHits6 = copy.deepcopy (ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNHits6.name = cms.string ("ZtoMuProbeTrkWithZCutsNHits6")
addSingleCut (ZtoMuProbeTrkWithZCutsNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoMuProbeTrkWithZCutsNHits6.cuts, [cutTrkNValidHits])

ZtoMuDisTrkNHits3 = copy.deepcopy (ZtoMuDisTrk)
ZtoMuDisTrkNHits3.name = cms.string ("ZtoMuDisTrkNHits3")
addSingleCut (ZtoMuDisTrkNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoMuDisTrkNHits3.cuts, [cutTrkNValidHits])

ZtoMuDisTrkNHits4 = copy.deepcopy (ZtoMuDisTrk)
ZtoMuDisTrkNHits4.name = cms.string ("ZtoMuDisTrkNHits4")
addSingleCut (ZtoMuDisTrkNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoMuDisTrkNHits4.cuts, [cutTrkNValidHits])

ZtoMuDisTrkNHits5 = copy.deepcopy (ZtoMuDisTrk)
ZtoMuDisTrkNHits5.name = cms.string ("ZtoMuDisTrkNHits5")
addSingleCut (ZtoMuDisTrkNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoMuDisTrkNHits5.cuts, [cutTrkNValidHits])

ZtoMuDisTrkNHits6 = copy.deepcopy (ZtoMuDisTrk)
ZtoMuDisTrkNHits6.name = cms.string ("ZtoMuDisTrkNHits6")
addSingleCut (ZtoMuDisTrkNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoMuDisTrkNHits6.cuts, [cutTrkNValidHits])

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
