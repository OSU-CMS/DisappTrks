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
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagMuonCuts = [
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

ZtoMuProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoMuProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoMuProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoMuDisTrkNoValidHitsCut = copy.deepcopy(ZtoMuDisTrk)
ZtoMuDisTrkNoValidHitsCut.name = cms.string("ZtoMuDisTrkNoValidHitsCut")
removeCuts(ZtoMuDisTrkNoValidHitsCut.cuts, [cutTrkNValidHits])

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
