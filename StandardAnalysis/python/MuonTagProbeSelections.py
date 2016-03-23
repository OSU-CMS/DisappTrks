import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Muon tag skim
##################################################
MuonTagSkim = cms.PSet(
    name = cms.string("MuonTagSkim"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagMuonCuts = [
    cutMuonPt25,
    cutMuonEta21,
    cutMuonTightID,
    cutMuonTightPFIso,
]
addCuts(MuonTagSkim.cuts, tagMuonCuts)

##################################################
## Muon tag and probe sample
##################################################
ZtoMuProbeTrk = copy.deepcopy(MuonTagSkim)
ZtoMuProbeTrk.name = cms.string("ZtoMuProbeTrk")

muTrkCuts = [
    cutMuTrkInvMass10,
    #cutMuTrkInvMass80To100,
]
addCuts(ZtoMuProbeTrk.cuts, [cutMuonArbitration])
addCuts(ZtoMuProbeTrk.cuts, [cutTrkPt30])
addCuts(ZtoMuProbeTrk.cuts, disTrkCuts)
addCuts(ZtoMuProbeTrk.cuts, muTrkCuts)
addCuts(ZtoMuProbeTrk.cuts, [cutTrkArbitration])
cutsToRemove = [
    cutTrkPt,
    cutTrkLooseMuonVeto,
]
removeCuts(ZtoMuProbeTrk.cuts, cutsToRemove)

ZtoMuProbeTrkWithZCuts = copy.deepcopy(ZtoMuProbeTrk)
ZtoMuProbeTrkWithZCuts.name = cms.string("ZtoMuProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
]
addCuts(ZtoMuProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoMuDisTrk = copy.deepcopy(ZtoMuProbeTrk)
ZtoMuDisTrk.name = cms.string("ZtoMuDisTrk")
cutsToAdd = [
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
    cutTrkLooseMuonVeto,
]
addCuts(ZtoMuDisTrk.cuts, cutsToAdd)

ZtoMuProbeTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoMuProbeTrk)
ZtoMuProbeTrkNoMissingOuterHitsCut.name = cms.string("ZtoMuProbeTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoMuProbeTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoMuProbeTrkWithZCutsNoMissingOuterHitsCut = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkWithZCutsNoMissingOuterHitsCut.name = cms.string("ZtoMuProbeTrkWithZCutsNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoMuProbeTrkWithZCutsNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoMuDisTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoMuDisTrk)
ZtoMuDisTrkNoMissingOuterHitsCut.name = cms.string("ZtoMuDisTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoMuDisTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

os_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("muon.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1")
)

zpeak_cut = cms.VPSet (
    cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass (muon, muon) > 60"),
#    cutString = cms.string("invMass (muon, muon) > 60 && invMass (muon, muon) < 120"),  # causes a seg fault
    numberRequired = cms.string(">= 1")
    ),
    cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass (muon, muon) < 120"),
    numberRequired = cms.string(">= 1")
    ),
)

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################
ZtoMuMu = cms.PSet(
    # Get this example from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/OSUT3Analysis/AnaTools/python/MyEventSelections.py?revision=1.2&view=markup
    name = cms.string("ZtoMuMu"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         cutMuonPairPt20,
         cutMuonPairEta21,
         cutMuonPairTightID,
         # cutMuonPairPFIso,
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
addCuts(ZtoMuMuCandTrk.cuts, candTrkCuts)  


##################################################
## Fake track control sample:  Z->mu mu + disappearing track
##################################################
ZtoMuMuDisTrk = copy.deepcopy(ZtoMuMu)
ZtoMuMuDisTrk.name = cms.string("ZtoMuMuDisTrk")
addCuts(ZtoMuMuDisTrk.cuts, disTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in Ecalo sideband
##################################################
ZtoMuMuCandTrkEcaloSdband = copy.deepcopy(ZtoMuMu) 
ZtoMuMuCandTrkEcaloSdband.name = cms.string("ZtoMuMuCandTrkEcaloSdband") 
addCuts(ZtoMuMuCandTrkEcaloSdband.cuts, candTrkEcaloSdbandCuts)  

##################################################
## Fake track control sample:  Z->mu mu + candidate track in NMissOut sideband
##################################################
ZtoMuMuCandTrkNMissOutSdband = copy.deepcopy(ZtoMuMu) 
ZtoMuMuCandTrkNMissOutSdband.name = cms.string("ZtoMuMuCandTrkNMissOutSdband") 
addCuts(ZtoMuMuCandTrkNMissOutSdband.cuts, candTrkNMissOutSdbandCuts)  

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

