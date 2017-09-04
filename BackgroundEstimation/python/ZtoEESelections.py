import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Fake track control sample:  start with Z->e e events
##################################################
ZtoEE = cms.PSet(
    name = cms.string("ZtoEE"),
    triggers = triggersSingleEle,
    metFilters = metFilters,
    cuts = cms.VPSet (
        cutMetFilters,
        cutElectronPairPt,
        cutElectronPairEta21,
        cutElectronPairTightID,
        cutElectronPairTightPFIso,
        cutEEChargeProduct,
        cutEEInvMassZLo,
        cutEEInvMassZHi,
    )
)

##################################################
## Fake track control sample:  Z->e e + disappearing track
##################################################
ZtoEEDisTrk = copy.deepcopy(ZtoEE)
ZtoEEDisTrk.name = cms.string("ZtoEEDisTrk")
addCuts(ZtoEEDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  Z->e e + disappearing track with 3 hits
##################################################
ZtoEEDisTrkNHits3 = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkNHits3.name = cms.string("ZtoEEDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(ZtoEEDisTrkNHits3.cuts, cutsToRemove)
addCuts   (ZtoEEDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->e e + disappearing track with 4 hits
##################################################
ZtoEEDisTrkNHits4 = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkNHits4.name = cms.string("ZtoEEDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(ZtoEEDisTrkNHits4.cuts, cutsToRemove)
addCuts   (ZtoEEDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->e e + disappearing track with 5 hits
##################################################
ZtoEEDisTrkNHits5 = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkNHits5.name = cms.string("ZtoEEDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(ZtoEEDisTrkNHits5.cuts, cutsToRemove)
addCuts   (ZtoEEDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->e e + disappearing track with 6 hits
##################################################
ZtoEEDisTrkNHits6 = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkNHits6.name = cms.string("ZtoEEDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(ZtoEEDisTrkNHits6.cuts, cutsToRemove)
addCuts   (ZtoEEDisTrkNHits6.cuts, cutsToAdd)

##################################################
## Fake track control samples:  Z->e e + disappearing track
## With inverted, dropped, or loosened D0 cuts
##################################################

ZtoEEDisTrkNoD0Cut = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkNoD0Cut.name = cms.string("ZtoEEDisTrkNoD0Cut")
removeCuts(ZtoEEDisTrkNoD0Cut.cuts, [cutTrkD0])

ZtoEEDisTrkInvertD0Cut = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkInvertD0Cut.name = cms.string("ZtoEEDisTrkInvertD0Cut")
addSingleCut(ZtoEEDisTrkInvertD0Cut.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoEEDisTrkInvertD0Cut.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0Cut = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkSidebandD0Cut.name = cms.string("ZtoEEDisTrkSidebandD0Cut")
addSingleCut(ZtoEEDisTrkSidebandD0Cut.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoEEDisTrkSidebandD0Cut.cuts, [cutTrkD0])

ZtoEEDisTrkNoD0CutNHits3 = copy.deepcopy(ZtoEEDisTrkNHits3)
ZtoEEDisTrkNoD0CutNHits3.name = cms.string("ZtoEEDisTrkNoD0CutNHits3")
removeCuts(ZtoEEDisTrkNoD0CutNHits3.cuts, [cutTrkD0])

ZtoEEDisTrkInvertD0CutNHits3 = copy.deepcopy(ZtoEEDisTrkNHits3)
ZtoEEDisTrkInvertD0CutNHits3.name = cms.string("ZtoEEDisTrkInvertD0CutNHits3")
addSingleCut(ZtoEEDisTrkInvertD0CutNHits3.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoEEDisTrkInvertD0CutNHits3.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0CutNHits3 = copy.deepcopy(ZtoEEDisTrkNHits3)
ZtoEEDisTrkSidebandD0CutNHits3.name = cms.string("ZtoEEDisTrkSidebandD0CutNHits3")
addSingleCut(ZtoEEDisTrkSidebandD0CutNHits3.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoEEDisTrkSidebandD0CutNHits3.cuts, [cutTrkD0])

ZtoEEDisTrkNoD0CutNHits4 = copy.deepcopy(ZtoEEDisTrkNHits4)
ZtoEEDisTrkNoD0CutNHits4.name = cms.string("ZtoEEDisTrkNoD0CutNHits4")
removeCuts(ZtoEEDisTrkNoD0CutNHits4.cuts, [cutTrkD0])

ZtoEEDisTrkInvertD0CutNHits4 = copy.deepcopy(ZtoEEDisTrkNHits4)
ZtoEEDisTrkInvertD0CutNHits4.name = cms.string("ZtoEEDisTrkInvertD0CutNHits4")
addSingleCut(ZtoEEDisTrkInvertD0CutNHits4.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoEEDisTrkInvertD0CutNHits4.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0CutNHits4 = copy.deepcopy(ZtoEEDisTrkNHits4)
ZtoEEDisTrkSidebandD0CutNHits4.name = cms.string("ZtoEEDisTrkSidebandD0CutNHits4")
addSingleCut(ZtoEEDisTrkSidebandD0CutNHits4.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoEEDisTrkSidebandD0CutNHits4.cuts, [cutTrkD0])

ZtoEEDisTrkNoD0CutNHits5 = copy.deepcopy(ZtoEEDisTrkNHits5)
ZtoEEDisTrkNoD0CutNHits5.name = cms.string("ZtoEEDisTrkNoD0CutNHits5")
removeCuts(ZtoEEDisTrkNoD0CutNHits5.cuts, [cutTrkD0])

ZtoEEDisTrkInvertD0CutNHits5 = copy.deepcopy(ZtoEEDisTrkNHits5)
ZtoEEDisTrkInvertD0CutNHits5.name = cms.string("ZtoEEDisTrkInvertD0CutNHits5")
addSingleCut(ZtoEEDisTrkInvertD0CutNHits5.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoEEDisTrkInvertD0CutNHits5.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0CutNHits5 = copy.deepcopy(ZtoEEDisTrkNHits5)
ZtoEEDisTrkSidebandD0CutNHits5.name = cms.string("ZtoEEDisTrkSidebandD0CutNHits5")
addSingleCut(ZtoEEDisTrkSidebandD0CutNHits5.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoEEDisTrkSidebandD0CutNHits5.cuts, [cutTrkD0])

ZtoEEDisTrkNoD0CutNHits6 = copy.deepcopy(ZtoEEDisTrkNHits6)
ZtoEEDisTrkNoD0CutNHits6.name = cms.string("ZtoEEDisTrkNoD0CutNHits6")
removeCuts(ZtoEEDisTrkNoD0CutNHits6.cuts, [cutTrkD0])

ZtoEEDisTrkInvertD0CutNHits6 = copy.deepcopy(ZtoEEDisTrkNHits6)
ZtoEEDisTrkInvertD0CutNHits6.name = cms.string("ZtoEEDisTrkInvertD0CutNHits6")
addSingleCut(ZtoEEDisTrkInvertD0CutNHits6.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoEEDisTrkInvertD0CutNHits6.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0CutNHits6 = copy.deepcopy(ZtoEEDisTrkNHits6)
ZtoEEDisTrkSidebandD0CutNHits6.name = cms.string("ZtoEEDisTrkSidebandD0CutNHits6")
addSingleCut(ZtoEEDisTrkSidebandD0CutNHits6.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoEEDisTrkSidebandD0CutNHits6.cuts, [cutTrkD0])

##################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
