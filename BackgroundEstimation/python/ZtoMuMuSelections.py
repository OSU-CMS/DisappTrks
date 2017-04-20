import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################
ZtoMuMu = cms.PSet(
    name = cms.string("ZtoMuMu"),
    triggers = triggersSingleMu,
    metFilters = metFilters,
    cuts = cms.VPSet (
        cutMetFilters,
        cutMuonPairPt, # this will be >22 for 76X and >26 for 80X
        cutMuonPairEta21,
        cutMuonPairTightID,
        cutMuonPairTightPFIso,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
    )
)

##################################################
## Fake track control sample:  Z->mu mu + candidate track
##################################################
ZtoMuMuCandTrk = copy.deepcopy(ZtoMuMu)
ZtoMuMuCandTrk.name = cms.string("ZtoMuMuCandTrk")
addCuts(ZtoMuMuCandTrk.cuts, [cutTrkPt55] + candTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track
##################################################
ZtoMuMuDisTrk = copy.deepcopy(ZtoMuMu)
ZtoMuMuDisTrk.name = cms.string("ZtoMuMuDisTrk")
addCuts(ZtoMuMuDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in Ecalo sideband
##################################################
ZtoMuMuCandTrkEcaloSdband = copy.deepcopy(ZtoMuMu)
ZtoMuMuCandTrkEcaloSdband.name = cms.string("ZtoMuMuCandTrkEcaloSdband")
addCuts(ZtoMuMuCandTrkEcaloSdband.cuts, [cutTrkPt55] + candTrkEcaloSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in NMissOut sideband
##################################################
ZtoMuMuCandTrkNMissOutSdband = copy.deepcopy(ZtoMuMu)
ZtoMuMuCandTrkNMissOutSdband.name = cms.string("ZtoMuMuCandTrkNMissOutSdband")
addCuts(ZtoMuMuCandTrkNMissOutSdband.cuts, [cutTrkPt55] + candTrkNMissOutSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 3 hits
##################################################
ZtoMuMuDisTrkNHits3 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits3.name = cms.string("ZtoMuMuDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(ZtoMuMuDisTrkNHits3.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 4 hits
##################################################
ZtoMuMuDisTrkNHits4 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits4.name = cms.string("ZtoMuMuDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(ZtoMuMuDisTrkNHits4.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 5 hits
##################################################
ZtoMuMuDisTrkNHits5 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits5.name = cms.string("ZtoMuMuDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(ZtoMuMuDisTrkNHits5.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 6 hits
##################################################
ZtoMuMuDisTrkNHits6 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits6.name = cms.string("ZtoMuMuDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(ZtoMuMuDisTrkNHits6.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits6.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + jet
##################################################
ZtoMuMuJet = copy.deepcopy(ZtoMuMu)
ZtoMuMuJet.name = cms.string("ZtoMuMuJet")
addCuts   (ZtoMuMuJet.cuts, [cutNJetsGE1])

##################################################
## Fake track control sample:  Z->mu mu + disappearing track + jet
##################################################
ZtoMuMuDisTrkJet = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkJet.name = cms.string("ZtoMuMuDisTrkJet")
addCuts   (ZtoMuMuDisTrkJet.cuts, [cutNJetsGE1])

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 3 hits + jet
##################################################
ZtoMuMuDisTrkNHits3Jet = copy.deepcopy(ZtoMuMuDisTrkNHits3)
ZtoMuMuDisTrkNHits3Jet.name = cms.string("ZtoMuMuDisTrkNHits3Jet")
addCuts   (ZtoMuMuDisTrkNHits3Jet.cuts, [cutNJetsGE1])

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 4 hits + jet
##################################################
ZtoMuMuDisTrkNHits4Jet = copy.deepcopy(ZtoMuMuDisTrkNHits4)
ZtoMuMuDisTrkNHits4Jet.name = cms.string("ZtoMuMuDisTrkNHits4Jet")
addCuts   (ZtoMuMuDisTrkNHits4Jet.cuts, [cutNJetsGE1])

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 5 hits + jet
##################################################
ZtoMuMuDisTrkNHits5Jet = copy.deepcopy(ZtoMuMuDisTrkNHits5)
ZtoMuMuDisTrkNHits5Jet.name = cms.string("ZtoMuMuDisTrkNHits5Jet")
addCuts   (ZtoMuMuDisTrkNHits5Jet.cuts, [cutNJetsGE1])

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 6 hits + jet
##################################################
ZtoMuMuDisTrkNHits6Jet = copy.deepcopy(ZtoMuMuDisTrkNHits6)
ZtoMuMuDisTrkNHits6Jet.name = cms.string("ZtoMuMuDisTrkNHits6Jet")
addCuts   (ZtoMuMuDisTrkNHits6Jet.cuts, [cutNJetsGE1])

##################################################
## ECalo control sample:  Z->mu mu + disappearing track with <= 4 hits
##################################################
ZtoMuMuDisTrkNHits4NoECaloCut = copy.deepcopy(ZtoMuMuDisTrkNHits4)
ZtoMuMuDisTrkNHits4NoECaloCut.name = cms.string("ZtoMuMuDisTrkNHits4NoECaloCut")
removeCuts(ZtoMuMuDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHits4, cutTrkEcalo])
addCuts (ZtoMuMuDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHitsLE4])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=2 missing outer htis
##################################################
ZtoMuMuDisTrkNMissOut2 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNMissOut2.name = cms.string('ZtoMuMuDisTrkNMissOut2')
removeCuts(ZtoMuMuDisTrkNMissOut2.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuDisTrkNMissOut2.cuts, [cutTrkNMissOut2])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=1 missing outer htis
##################################################
ZtoMuMuDisTrkNMissOut1 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNMissOut1.name = cms.string('ZtoMuMuDisTrkNMissOut1')
removeCuts(ZtoMuMuDisTrkNMissOut1.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuDisTrkNMissOut1.cuts, [cutTrkNMissOut1])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=0 missing outer htis
##################################################
ZtoMuMuDisTrkNMissOut0 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNMissOut0.name = cms.string('ZtoMuMuDisTrkNMissOut1')
removeCuts(ZtoMuMuDisTrkNMissOut0.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuDisTrkNMissOut0.cuts, [cutTrkNMissOut0])

##################################################
## Now copied channels for one jet (pt > 110 GeV) and 14-18 PV
##################################################

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################

ZtoMuMuOneJet14to18PV = copy.deepcopy(ZtoMuMu)
ZtoMuMuOneJet14to18PV.name = cms.string("ZtoMuMuOneJet14to18PV")
addCuts(ZtoMuMuOneJet14to18PV.cuts, oneJet14to18PVCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track
##################################################
ZtoMuMuOneJet14to18PVCandTrk = copy.deepcopy(ZtoMuMuOneJet14to18PV)
ZtoMuMuOneJet14to18PVCandTrk.name = cms.string("ZtoMuMuOneJet14to18PVCandTrk")
addCuts(ZtoMuMuOneJet14to18PVCandTrk.cuts, [cutTrkPt55] + candTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track
##################################################
ZtoMuMuOneJet14to18PVDisTrk = copy.deepcopy(ZtoMuMuOneJet14to18PV)
ZtoMuMuOneJet14to18PVDisTrk.name = cms.string("ZtoMuMuOneJet14to18PVDisTrk")
addCuts(ZtoMuMuOneJet14to18PVDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in Ecalo sideband
##################################################
ZtoMuMuOneJet14to18PVCandTrkEcaloSdband = copy.deepcopy(ZtoMuMuOneJet14to18PV)
ZtoMuMuOneJet14to18PVCandTrkEcaloSdband.name = cms.string("ZtoMuMuOneJet14to18PVCandTrkEcaloSdband")
addCuts(ZtoMuMuOneJet14to18PVCandTrkEcaloSdband.cuts, [cutTrkPt55] + candTrkEcaloSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in NMissOut sideband
##################################################
ZtoMuMuOneJet14to18PVCandTrkNMissOutSdband = copy.deepcopy(ZtoMuMuOneJet14to18PV)
ZtoMuMuOneJet14to18PVCandTrkNMissOutSdband.name = cms.string("ZtoMuMuOneJet14to18PVCandTrkNMissOutSdband")
addCuts(ZtoMuMuOneJet14to18PVCandTrkNMissOutSdband.cuts, [cutTrkPt55] + candTrkNMissOutSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 3 hits
##################################################
ZtoMuMuOneJet14to18PVDisTrkNHits3 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNHits3.name = cms.string("ZtoMuMuOneJet14to18PVDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNHits3.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet14to18PVDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 4 hits
##################################################
ZtoMuMuOneJet14to18PVDisTrkNHits4 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNHits4.name = cms.string("ZtoMuMuOneJet14to18PVDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNHits4.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet14to18PVDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 5 hits
##################################################
ZtoMuMuOneJet14to18PVDisTrkNHits5 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNHits5.name = cms.string("ZtoMuMuOneJet14to18PVDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNHits5.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet14to18PVDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 6 hits
##################################################
ZtoMuMuOneJet14to18PVDisTrkNHits6 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNHits6.name = cms.string("ZtoMuMuOneJet14to18PVDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNHits6.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet14to18PVDisTrkNHits6.cuts, cutsToAdd)

##################################################
## ECalo control sample:  Z->mu mu + disappearing track with <= 4 hits
##################################################
ZtoMuMuOneJet14to18PVDisTrkNHits4NoECaloCut = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrkNHits4)
ZtoMuMuOneJet14to18PVDisTrkNHits4NoECaloCut.name = cms.string("ZtoMuMuOneJet14to18PVDisTrkNHits4NoECaloCut")
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHits4, cutTrkEcalo])
addCuts (ZtoMuMuOneJet14to18PVDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHitsLE4])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=2 missing outer htis
##################################################
ZtoMuMuOneJet14to18PVDisTrkNMissOut2 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNMissOut2.name = cms.string('ZtoMuMuOneJet14to18PVDisTrkNMissOut2')
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNMissOut2.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuOneJet14to18PVDisTrkNMissOut2.cuts, [cutTrkNMissOut2])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=1 missing outer htis
##################################################
ZtoMuMuOneJet14to18PVDisTrkNMissOut1 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNMissOut1.name = cms.string('ZtoMuMuOneJet14to18PVDisTrkNMissOut1')
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNMissOut1.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuOneJet14to18PVDisTrkNMissOut1.cuts, [cutTrkNMissOut1])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=0 missing outer htis
##################################################
ZtoMuMuOneJet14to18PVDisTrkNMissOut0 = copy.deepcopy(ZtoMuMuOneJet14to18PVDisTrk)
ZtoMuMuOneJet14to18PVDisTrkNMissOut0.name = cms.string('ZtoMuMuOneJet14to18PVDisTrkNMissOut1')
removeCuts(ZtoMuMuOneJet14to18PVDisTrkNMissOut0.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuOneJet14to18PVDisTrkNMissOut0.cuts, [cutTrkNMissOut0])

##################################################
## Fake track control samples:  Z->mu mu + disappearing track
## With inverted or dropped D0 cuts
##################################################

ZtoMuMuDisTrkNoD0Cut = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNoD0Cut.name = cms.string("ZtoMuMuDisTrkNoD0Cut")
removeCuts(ZtoMuMuDisTrkNoD0Cut.cuts, [cutTrkD0])

ZtoMuMuDisTrkInvertD0Cut = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkInvertD0Cut.name = cms.string("ZtoMuMuDisTrkInvertD0Cut")
addSingleCut(ZtoMuMuDisTrkInvertD0Cut.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkInvertD0Cut.cuts, [cutTrkD0])

ZtoMuMuDisTrkNoD0CutNHits3 = copy.deepcopy(ZtoMuMuDisTrkNHits3)
ZtoMuMuDisTrkNoD0CutNHits3.name = cms.string("ZtoMuMuDisTrkNoD0CutNHits3")
removeCuts(ZtoMuMuDisTrkNoD0CutNHits3.cuts, [cutTrkD0])

ZtoMuMuDisTrkInvertD0CutNHits3 = copy.deepcopy(ZtoMuMuDisTrkNHits3)
ZtoMuMuDisTrkInvertD0CutNHits3.name = cms.string("ZtoMuMuDisTrkInvertD0CutNHits3")
addSingleCut(ZtoMuMuDisTrkInvertD0CutNHits3.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkInvertD0CutNHits3.cuts, [cutTrkD0])

ZtoMuMuDisTrkNoD0CutNHits4 = copy.deepcopy(ZtoMuMuDisTrkNHits4)
ZtoMuMuDisTrkNoD0CutNHits4.name = cms.string("ZtoMuMuDisTrkNoD0CutNHits4")
removeCuts(ZtoMuMuDisTrkNoD0CutNHits4.cuts, [cutTrkD0])

ZtoMuMuDisTrkInvertD0CutNHits4 = copy.deepcopy(ZtoMuMuDisTrkNHits4)
ZtoMuMuDisTrkInvertD0CutNHits4.name = cms.string("ZtoMuMuDisTrkInvertD0CutNHits4")
addSingleCut(ZtoMuMuDisTrkInvertD0CutNHits4.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkInvertD0CutNHits4.cuts, [cutTrkD0])

ZtoMuMuDisTrkNoD0CutNHits5 = copy.deepcopy(ZtoMuMuDisTrkNHits5)
ZtoMuMuDisTrkNoD0CutNHits5.name = cms.string("ZtoMuMuDisTrkNoD0CutNHits5")
removeCuts(ZtoMuMuDisTrkNoD0CutNHits5.cuts, [cutTrkD0])

ZtoMuMuDisTrkInvertD0CutNHits5 = copy.deepcopy(ZtoMuMuDisTrkNHits5)
ZtoMuMuDisTrkInvertD0CutNHits5.name = cms.string("ZtoMuMuDisTrkInvertD0CutNHits5")
addSingleCut(ZtoMuMuDisTrkInvertD0CutNHits5.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkInvertD0CutNHits5.cuts, [cutTrkD0])

ZtoMuMuDisTrkNoD0CutNHits6 = copy.deepcopy(ZtoMuMuDisTrkNHits6)
ZtoMuMuDisTrkNoD0CutNHits6.name = cms.string("ZtoMuMuDisTrkNoD0CutNHits6")
removeCuts(ZtoMuMuDisTrkNoD0CutNHits6.cuts, [cutTrkD0])

ZtoMuMuDisTrkInvertD0CutNHits6 = copy.deepcopy(ZtoMuMuDisTrkNHits6)
ZtoMuMuDisTrkInvertD0CutNHits6.name = cms.string("ZtoMuMuDisTrkInvertD0CutNHits6")
addSingleCut(ZtoMuMuDisTrkInvertD0CutNHits6.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkInvertD0CutNHits6.cuts, [cutTrkD0])

##################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
