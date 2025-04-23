import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

def createHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, None, cutTrkNLayersVariations))
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
        replaceSingleCut (globals ()[chName + 'NLayers3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

##################################################
## Fake track control sample:  start with Z->e e events
##################################################
ZtoEE = cms.PSet(
    name = cms.string("ZtoEE"),
    triggers = triggersSingleEle,
    metFilters = metFilters,
    cuts = cms.VPSet (),
)

zToEEElectronCuts = [
    cutMetFilters,
    cutElectronPairPt,
    cutElectronPairEta21,
    cutElectronPairTightID,
    cutElectronPairTightPFIso,
    cutEEChargeProduct,
    cutEEInvMassZLo,
    cutEEInvMassZHi,
]
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    zToEEElectronCuts = [
        cutMetFilters,
        cutElectronPairPt,
        cutElectronPairEta21,
        cutElectronPairVIDTightID, # ID + iso (no vertexing -- added below)
        cutElectronPairD02017,
        cutElectronPairDZ2017,
        cutEEChargeProduct,
        cutEEInvMassZLo,
        cutEEInvMassZHi,
        cutElectronPt,
    ]
addCuts(ZtoEE.cuts, zToEEElectronCuts)

##################################################
## Fake track control sample:  Z->e e + disappearing track
##################################################
ZtoEEDisTrk = copy.deepcopy(ZtoEE)
ZtoEEDisTrk.name = cms.string("ZtoEEDisTrk")
addCuts(ZtoEEDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  Z->e e + disappearing track with 3 hits
##################################################
createHitsVariations (ZtoEEDisTrk, "ZtoEEDisTrk")

##################################################
## Hits systematic backup (ARC EXO-19-010)
##################################################
ZtoEETauCtrlSelection = copy.deepcopy(ZtoEE)
ZtoEETauCtrlSelection.name = cms.string("ZtoEETauCtrlSelection")
addCuts(ZtoEETauCtrlSelection.cuts, isoTrkWithPt55Cuts + [cutTrkElecVeto, cutTrkMuonVeto])
removeCuts(ZtoEETauCtrlSelection.cuts, [cutTrkJetDeltaPhi])

ZtoEETauHitsSystematicSelection = copy.deepcopy(ZtoEETauCtrlSelection)
ZtoEETauHitsSystematicSelection.name = cms.string("ZtoEETauHitsSystematicSelection")
cutsToRemove = [
    cutTrkNMissIn,
    cutTrkNMissMid,
]
removeCuts(ZtoEETauHitsSystematicSelection.cuts, cutsToRemove)

createHitsVariations (ZtoEETauCtrlSelection, "ZtoEETauCtrlSelection")
createHitsVariations (ZtoEETauHitsSystematicSelection, "ZtoEETauHitsSystematicSelection")

##################################################
## Fake track control samples:  Z->e e + disappearing track
## With inverted, dropped, or loosened D0 cuts
##################################################

ZtoEEDisTrkNoD0Cut = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkNoD0Cut.name = cms.string("ZtoEEDisTrkNoD0Cut")
removeCuts(ZtoEEDisTrkNoD0Cut.cuts, [cutTrkD0])

ZtoEEDisTrkNoD0CutNoHitsCut = copy.deepcopy(ZtoEEDisTrkNoD0Cut)
ZtoEEDisTrkNoD0CutNoHitsCut.name = cms.string("ZtoEEDisTrkNoD0CutNoHitsCut")
removeCuts(ZtoEEDisTrkNoD0CutNoHitsCut.cuts, [cutTrkNValidPixelHitsSignal, cutTrkNValidHitsSignal])

ZtoEEDisTrkNoD0Cut3Layers = copy.deepcopy(ZtoEEDisTrkNoD0Cut)
ZtoEEDisTrkNoD0Cut3Layers.name = cms.string("ZtoEEDisTrkNoD0Cut3Layers")
addSingleCut(ZtoEEDisTrkNoD0Cut3Layers.cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
addSingleCut(ZtoEEDisTrkNoD0Cut3Layers.cuts, cutTrkNLayersExclusive[3], cutTrkNValidHitsSignal)
removeCuts(ZtoEEDisTrkNoD0Cut3Layers.cuts, [cutTrkNValidPixelHitsSignal, cutTrkNValidHitsSignal])

ZtoEEDisTrkNoD0Cut3LayersVeryClean = copy.deepcopy(ZtoEEDisTrkNoD0Cut3Layers)
ZtoEEDisTrkNoD0Cut3LayersVeryClean.name = cms.string("ZtoEEDisTrkNoD0Cut3LayersVeryClean")
addCuts(ZtoEEDisTrkNoD0Cut3LayersVeryClean.cuts, veryClean3LayersCuts)

ZtoEEDisTrkInvertD0Cut = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkInvertD0Cut.name = cms.string("ZtoEEDisTrkInvertD0Cut")
addSingleCut(ZtoEEDisTrkInvertD0Cut.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoEEDisTrkInvertD0Cut.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0Cut = copy.deepcopy(ZtoEEDisTrk)
ZtoEEDisTrkSidebandD0Cut.name = cms.string("ZtoEEDisTrkSidebandD0Cut")
addSingleCut(ZtoEEDisTrkSidebandD0Cut.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoEEDisTrkSidebandD0Cut.cuts, [cutTrkD0])

ZtoEEDisTrkSidebandD0CutNoHitsCut = copy.deepcopy(ZtoEEDisTrkSidebandD0Cut)
ZtoEEDisTrkSidebandD0CutNoHitsCut.name = cms.string("ZtoEEDisTrkSidebandD0CutNoHitsCut")
removeCuts(ZtoEEDisTrkSidebandD0CutNoHitsCut.cuts, [cutTrkNValidPixelHitsSignal, cutTrkNValidHitsSignal])

createHitsVariations (ZtoEEDisTrkNoD0Cut,       "ZtoEEDisTrkNoD0Cut")
createHitsVariations (ZtoEEDisTrkInvertD0Cut,   "ZtoEEDisTrkInvertD0Cut")
createHitsVariations (ZtoEEDisTrkSidebandD0Cut, "ZtoEEDisTrkSidebandD0Cut")

##################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
