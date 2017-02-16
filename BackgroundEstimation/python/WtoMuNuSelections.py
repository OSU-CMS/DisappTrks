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
    cuts = cms.VPSet (
        cutGoodPV,
        cutMuonPt25,
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
## Now copied channels for one jet (pt > 110 GeV) and ==16 PV
##################################################

##################################################
## Fake track control sample:  W->mu nu
##################################################
WtoMuNuOneJet16PV = copy.deepcopy(WtoMuNu)
WtoMuNuOneJet16PV.name = cms.string("WtoMuNuOneJet16PV")
addCuts(WtoMuNuOneJet16PV.cuts, oneJet16PVCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track
##################################################
WtoMuNuOneJet16PVCandTrk = copy.deepcopy(WtoMuNuOneJet16PV)
WtoMuNuOneJet16PVCandTrk.name = cms.string("WtoMuNuOneJet16PVCandTrk")
addCuts(WtoMuNuOneJet16PVCandTrk.cuts, [cutTrkPt55] + candTrkCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track
##################################################
WtoMuNuOneJet16PVDisTrk = copy.deepcopy(WtoMuNuOneJet16PV)
WtoMuNuOneJet16PVDisTrk.name = cms.string("WtoMuNuOneJet16PVDisTrk")
addCuts(WtoMuNuOneJet16PVDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 3 hits
##################################################
WtoMuNuOneJet16PVDisTrkNHits3 = copy.deepcopy(WtoMuNuOneJet16PVDisTrk)
WtoMuNuOneJet16PVDisTrkNHits3.name = cms.string("WtoMuNuOneJet16PVDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(WtoMuNuOneJet16PVDisTrkNHits3.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet16PVDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 4 hits
##################################################
WtoMuNuOneJet16PVDisTrkNHits4 = copy.deepcopy(WtoMuNuOneJet16PVDisTrk)
WtoMuNuOneJet16PVDisTrkNHits4.name = cms.string("WtoMuNuOneJet16PVDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(WtoMuNuOneJet16PVDisTrkNHits4.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet16PVDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 5 hits
##################################################
WtoMuNuOneJet16PVDisTrkNHits5 = copy.deepcopy(WtoMuNuOneJet16PVDisTrk)
WtoMuNuOneJet16PVDisTrkNHits5.name = cms.string("WtoMuNuOneJet16PVDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(WtoMuNuOneJet16PVDisTrkNHits5.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet16PVDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  W->mu nu + disappearing track with 6 hits
##################################################
WtoMuNuOneJet16PVDisTrkNHits6 = copy.deepcopy(WtoMuNuOneJet16PVDisTrk)
WtoMuNuOneJet16PVDisTrkNHits6.name = cms.string("WtoMuNuOneJet16PVDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(WtoMuNuOneJet16PVDisTrkNHits6.cuts, cutsToRemove)
addCuts   (WtoMuNuOneJet16PVDisTrkNHits6.cuts, cutsToAdd)
