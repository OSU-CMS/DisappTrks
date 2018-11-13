import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

def createNHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_3_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

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

createNHitsVariations (ZtoMuMuDisTrk, "ZtoMuMuDisTrk")

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

createNHitsVariations (ZtoMuMuDisTrkJet, "ZtoMuMuDisTrkJet")

##################################################
## ECalo control sample:  Z->mu mu + disappearing track with <= 4 hits
##################################################
ZtoMuMuDisTrkNHits4NoECaloCut = copy.deepcopy(ZtoMuMuDisTrkNHits4)
ZtoMuMuDisTrkNHits4NoECaloCut.name = cms.string("ZtoMuMuDisTrkNHits4NoECaloCut")
removeCuts(ZtoMuMuDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHitsExclusive[4], cutTrkEcalo])
addCuts (ZtoMuMuDisTrkNHits4NoECaloCut.cuts, [cutTrkNValidHitsLE[4]])

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
## Fake track control samples:  Z->mu mu + disappearing track
## With inverted, dropped, or loosened D0 cuts
##################################################

ZtoMuMuDisTrkNoD0Cut = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNoD0Cut.name = cms.string("ZtoMuMuDisTrkNoD0Cut")
removeCuts(ZtoMuMuDisTrkNoD0Cut.cuts, [cutTrkD0])

ZtoMuMuDisTrkInvertD0Cut = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkInvertD0Cut.name = cms.string("ZtoMuMuDisTrkInvertD0Cut")
addSingleCut(ZtoMuMuDisTrkInvertD0Cut.cuts, cutTrkInvertD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkInvertD0Cut.cuts, [cutTrkD0])

ZtoMuMuDisTrkSidebandD0Cut = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkSidebandD0Cut.name = cms.string("ZtoMuMuDisTrkSidebandD0Cut")
addSingleCut(ZtoMuMuDisTrkSidebandD0Cut.cuts, cutTrkSidebandD0, cutTrkD0)
removeCuts(ZtoMuMuDisTrkSidebandD0Cut.cuts, [cutTrkD0])

createNHitsVariations (ZtoMuMuDisTrkNoD0Cut,       "ZtoMuMuDisTrkNoD0Cut")
createNHitsVariations (ZtoMuMuDisTrkInvertD0Cut,   "ZtoMuMuDisTrkInvertD0Cut")
createNHitsVariations (ZtoMuMuDisTrkSidebandD0Cut, "ZtoMuMuDisTrkSidebandD0Cut")

#####################################################################
# ZtMuMu Background Estimates w/o Isolation Cut or Calo Energy Cut
#####################################################################

ZtoMuMuCandTrkNoIso = copy.deepcopy(ZtoMuMuCandTrk)
ZtoMuMuCandTrkNoIso.name = cms.string("ZtoMuMuCandTrkNoIso")
removeCuts(ZtoMuMuCandTrkNoIso.cuts, [cutTrkIso])

ZtoMuMuDisTrkNoIsoNoCalo = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNoIsoNoCalo.name = cms.string("ZtoMuMuDisTrkNoIsoNoCalo")
removeCuts(ZtoMuMuDisTrkNoIsoNoCalo.cuts, [cutTrkIso, cutTrkEcalo])

createNHitsVariations (ZtoMuMuDisTrkNoIsoNoCalo, "ZtoMuMuDisTrkNoIsoNoCalo")

##################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
