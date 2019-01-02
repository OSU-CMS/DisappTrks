import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

def createHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, None, cutTrkNLayersVariations))
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_3_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
        replaceSingleCut (globals ()[chName + 'NLayers3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

##################################################
## Fake track control sample:  W->mu nu
##################################################
WtoMuNu = cms.PSet(
    name = cms.string("WtoMuNu"),
    triggers = triggersSingleMu,
    metFilters = metFilters,
    cuts = cms.VPSet (
        cutMetFilters,
        cutGoodPV,
        cutMuonPt, # this will be >22 for 76X and >26 for 80X
        cutMuonExactlyOne,
        cutElectronExactlyZero,
        cutMuonEta21,
        cutMuonTightID,
        cutMuonTightPFIso,
        cutMuonHighMT,
    )
)

##################################################
## Fake track control sample:  W->mu nu + disappearing track
##################################################
WtoMuNuCandTrk = copy.deepcopy(WtoMuNu)
WtoMuNuCandTrk.name = cms.string("WtoMuNuCandTrk")
addCuts(WtoMuNuCandTrk.cuts, [cutTrkPt55] + candTrkCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track
##################################################
WtoMuNuDisTrk = copy.deepcopy(WtoMuNu)
WtoMuNuDisTrk.name = cms.string("WtoMuNuDisTrk")
addCuts(WtoMuNuDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with exclusive number of hits
##################################################
createHitsVariations (WtoMuNuDisTrk, "WtoMuNuDisTrk")
