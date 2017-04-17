import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

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
## Fake track control sample:  W->mu nu + disappearing track with 3 hits
##################################################
WtoMuNuDisTrkNHits3 = copy.deepcopy(WtoMuNuDisTrk)
WtoMuNuDisTrkNHits3.name = cms.string("WtoMuNuDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(WtoMuNuDisTrkNHits3.cuts, cutsToRemove)
addCuts   (WtoMuNuDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 4 hits
##################################################
WtoMuNuDisTrkNHits4 = copy.deepcopy(WtoMuNuDisTrk)
WtoMuNuDisTrkNHits4.name = cms.string("WtoMuNuDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(WtoMuNuDisTrkNHits4.cuts, cutsToRemove)
addCuts   (WtoMuNuDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 5 hits
##################################################
WtoMuNuDisTrkNHits5 = copy.deepcopy(WtoMuNuDisTrk)
WtoMuNuDisTrkNHits5.name = cms.string("WtoMuNuDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(WtoMuNuDisTrkNHits5.cuts, cutsToRemove)
addCuts   (WtoMuNuDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 6 hits
##################################################
WtoMuNuDisTrkNHits6 = copy.deepcopy(WtoMuNuDisTrk)
WtoMuNuDisTrkNHits6.name = cms.string("WtoMuNuDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(WtoMuNuDisTrkNHits6.cuts, cutsToRemove)
addCuts   (WtoMuNuDisTrkNHits6.cuts, cutsToAdd)

##################################################
## Now copied channels for one jet (pt > 110 GeV) and 14-18 PV
##################################################

##################################################
## Fake track control sample:  W->mu nu
##################################################
WtoMuNuOneJet14to18PV = copy.deepcopy(WtoMuNu)
WtoMuNuOneJet14to18PV.name = cms.string("WtoMuNuOneJet14to18PV")
addCuts(WtoMuNuOneJet14to18PV.cuts, oneJet14to18PVCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track
##################################################
WtoMuNuOneJet14to18PVCandTrk = copy.deepcopy(WtoMuNuOneJet14to18PV)
WtoMuNuOneJet14to18PVCandTrk.name = cms.string("WtoMuNuOneJet14to18PVCandTrk")
addCuts(WtoMuNuOneJet14to18PVCandTrk.cuts, [cutTrkPt55] + candTrkCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track
##################################################
WtoMuNuOneJet14to18PVDisTrk = copy.deepcopy(WtoMuNuOneJet14to18PV)
WtoMuNuOneJet14to18PVDisTrk.name = cms.string("WtoMuNuOneJet14to18PVDisTrk")
addCuts(WtoMuNuOneJet14to18PVDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 3 hits
##################################################
WtoMuNuOneJet14to18PVDisTrkNHits3 = copy.deepcopy(WtoMuNuOneJet14to18PVDisTrk)
WtoMuNuOneJet14to18PVDisTrkNHits3.name = cms.string("WtoMuNuOneJet14to18PVDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(WtoMuNuOneJet14to18PVDisTrkNHits3.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet14to18PVDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 4 hits
##################################################
WtoMuNuOneJet14to18PVDisTrkNHits4 = copy.deepcopy(WtoMuNuOneJet14to18PVDisTrk)
WtoMuNuOneJet14to18PVDisTrkNHits4.name = cms.string("WtoMuNuOneJet14to18PVDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(WtoMuNuOneJet14to18PVDisTrkNHits4.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet14to18PVDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 5 hits
##################################################
WtoMuNuOneJet14to18PVDisTrkNHits5 = copy.deepcopy(WtoMuNuOneJet14to18PVDisTrk)
WtoMuNuOneJet14to18PVDisTrkNHits5.name = cms.string("WtoMuNuOneJet14to18PVDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(WtoMuNuOneJet14to18PVDisTrkNHits5.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet14to18PVDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 6 hits
##################################################
WtoMuNuOneJet14to18PVDisTrkNHits6 = copy.deepcopy(WtoMuNuOneJet14to18PVDisTrk)
WtoMuNuOneJet14to18PVDisTrkNHits6.name = cms.string("WtoMuNuOneJet14to18PVDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(WtoMuNuOneJet14to18PVDisTrkNHits6.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet14to18PVDisTrkNHits6.cuts, cutsToAdd)
