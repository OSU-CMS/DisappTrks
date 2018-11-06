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
createNHitsVariations = lambda a, b : globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
createNHitsVariations (ZtoEEDisTrk, "ZtoEEDisTrk")

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

createNHitsVariations (ZtoEEDisTrkNoD0Cut,       "ZtoEEDisTrkNoD0Cut")
createNHitsVariations (ZtoEEDisTrkInvertD0Cut,   "ZtoEEDisTrkInvertD0Cut")
createNHitsVariations (ZtoEEDisTrkSidebandD0Cut, "ZtoEEDisTrkSidebandD0Cut")

##################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
