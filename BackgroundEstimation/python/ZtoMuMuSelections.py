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
    cuts = cms.VPSet (
        cutMuonPairPt25,
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
## Now copied channels for one jet (pt > 110 GeV) and ==16 PV
##################################################

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################

ZtoMuMuOneJet16PV = copy.deepcopy(ZtoMuMu)
ZtoMuMuOneJet16PV.name = cms.string("ZtoMuMuOneJet16PV")
addCuts(ZtoMuMuOneJet16PV.cuts, oneJet16PVCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track
##################################################
ZtoMuMuOneJet16PVCandTrk = copy.deepcopy(ZtoMuMuOneJet16PV)
ZtoMuMuOneJet16PVCandTrk.name = cms.string("ZtoMuMuOneJet16PVCandTrk")
addCuts(ZtoMuMuOneJet16PVCandTrk.cuts, [cutTrkPt55] + candTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track
##################################################
ZtoMuMuOneJet16PVDisTrk = copy.deepcopy(ZtoMuMuOneJet16PV)
ZtoMuMuOneJet16PVDisTrk.name = cms.string("ZtoMuMuOneJet16PVDisTrk")
addCuts(ZtoMuMuOneJet16PVDisTrk.cuts, [cutTrkPt55] + disTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in Ecalo sideband
##################################################
ZtoMuMuOneJet16PVCandTrkEcaloSdband = copy.deepcopy(ZtoMuMuOneJet16PV)
ZtoMuMuOneJet16PVCandTrkEcaloSdband.name = cms.string("ZtoMuMuOneJet16PVCandTrkEcaloSdband")
addCuts(ZtoMuMuOneJet16PVCandTrkEcaloSdband.cuts, [cutTrkPt55] + candTrkEcaloSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in NMissOut sideband
##################################################
ZtoMuMuOneJet16PVCandTrkNMissOutSdband = copy.deepcopy(ZtoMuMuOneJet16PV)
ZtoMuMuOneJet16PVCandTrkNMissOutSdband.name = cms.string("ZtoMuMuOneJet16PVCandTrkNMissOutSdband")
addCuts(ZtoMuMuOneJet16PVCandTrkNMissOutSdband.cuts, [cutTrkPt55] + candTrkNMissOutSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 3 hits
##################################################
ZtoMuMuOneJet16PVDisTrkNHits3 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNHits3.name = cms.string("ZtoMuMuOneJet16PVDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(ZtoMuMuOneJet16PVDisTrkNHits3.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet16PVDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 4 hits
##################################################
ZtoMuMuOneJet16PVDisTrkNHits4 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNHits4.name = cms.string("ZtoMuMuOneJet16PVDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(ZtoMuMuOneJet16PVDisTrkNHits4.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet16PVDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 5 hits
##################################################
ZtoMuMuOneJet16PVDisTrkNHits5 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNHits5.name = cms.string("ZtoMuMuOneJet16PVDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(ZtoMuMuOneJet16PVDisTrkNHits5.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet16PVDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 6 hits
##################################################
ZtoMuMuOneJet16PVDisTrkNHits6 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNHits6.name = cms.string("ZtoMuMuOneJet16PVDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(ZtoMuMuOneJet16PVDisTrkNHits6.cuts, cutsToRemove)
addCuts   (ZtoMuMuOneJet16PVDisTrkNHits6.cuts, cutsToAdd)

##################################################
## ECalo control sample:  Z->mu mu + disappearing track with <= 4 hits
##################################################
ZtoMuMuOneJet16PVDisTrkNHits4NoECaloCut = copy.deepcopy(ZtoMuMuOneJet16PVDisTrkNHits4)
ZtoMuMuOneJet16PVDisTrkNHits4NoECaloCut.name = cms.string("ZtoMuMuOneJet16PVDisTrkNHits4NoECaloCut")
removeCuts(ZtoMuMuOneJet16PVDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHits4, cutTrkEcalo])
addCuts (ZtoMuMuOneJet16PVDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHitsLE4])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=2 missing outer htis
##################################################
ZtoMuMuOneJet16PVDisTrkNMissOut2 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNMissOut2.name = cms.string('ZtoMuMuOneJet16PVDisTrkNMissOut2')
removeCuts(ZtoMuMuOneJet16PVDisTrkNMissOut2.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuOneJet16PVDisTrkNMissOut2.cuts, [cutTrkNMissOut2])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=1 missing outer htis
##################################################
ZtoMuMuOneJet16PVDisTrkNMissOut1 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNMissOut1.name = cms.string('ZtoMuMuOneJet16PVDisTrkNMissOut1')
removeCuts(ZtoMuMuOneJet16PVDisTrkNMissOut1.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuOneJet16PVDisTrkNMissOut1.cuts, [cutTrkNMissOut1])

##################################################
## Fake track control sample: Z->mu mu + disappearing track with >=0 missing outer htis
##################################################
ZtoMuMuOneJet16PVDisTrkNMissOut0 = copy.deepcopy(ZtoMuMuOneJet16PVDisTrk)
ZtoMuMuOneJet16PVDisTrkNMissOut0.name = cms.string('ZtoMuMuOneJet16PVDisTrkNMissOut1')
removeCuts(ZtoMuMuOneJet16PVDisTrkNMissOut0.cuts, [cutTrkNMissOut])
addCuts (ZtoMuMuOneJet16PVDisTrkNMissOut0.cuts, [cutTrkNMissOut0])

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
