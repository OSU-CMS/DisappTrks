import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

################################################################################
## Muon tag skim
################################################################################
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
## Higher pt to be closer to candidate track selection
##################################################
MuonTagPt35 = copy.deepcopy(MuonTagSkim)
MuonTagPt35.name = cms.string("MuonTagPt35")
addSingleCut(MuonTagPt35.cuts, cutMuonPt35, cutMuonPt25)
cutsToAdd = [ 
    cutMuonArbitration,
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutTrkPt35,
    cutTrkMuDR0p1,
    cutTrkMatchRecoMu,
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
]
addCuts(MuonTagPt35.cuts, cutsToAdd)
cutsToRemove = [
    cutMuonPt25, 
    ]
removeCuts(MuonTagPt35.cuts, cutsToRemove)  

MuonTagPt35NoTrig = copy.deepcopy(MuonTagPt35)
MuonTagPt35NoTrig.name = cms.string("MuonTagPt35NoTrig")
MuonTagPt35NoTrig.triggers = cms.vstring() 

MuonTagPt35MetTrig = copy.deepcopy(MuonTagPt35)
MuonTagPt35MetTrig.name = cms.string("MuonTagPt35MetTrig")
MuonTagPt35MetTrig.triggers = triggersMet 

MuonTagPt35MetCut = copy.deepcopy(MuonTagPt35)
MuonTagPt35MetCut.name = cms.string("MuonTagPt35MetCut")
cutsToAdd = [ 
    cutMuonMetMinusOne, 
]
addCuts(MuonTagPt35MetCut.cuts, cutsToAdd)  

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
MuonTagPt50 = copy.deepcopy(MuonTagPt35)
MuonTagPt50.name = cms.string("MuonTagPt50")
addSingleCut(MuonTagPt50.cuts, cutTrkPt, cutTrkPt35)
cutsToAdd = [
    cutTrkEcalo,
    cutTrkNMissOut,
    #cutTrkNMissOutInv
]
addCuts(MuonTagPt50.cuts, cutsToAdd)
cutsToRemove = [
    cutTrkPt35,
]
removeCuts(MuonTagPt50.cuts, cutsToRemove)

MuonTagPt50NoTrig = copy.deepcopy(MuonTagPt50)
MuonTagPt50NoTrig.name = cms.string("MuonTagPt50NoTrig")
MuonTagPt50NoTrig.triggers = cms.vstring() 

MuonTagPt50MetTrig = copy.deepcopy(MuonTagPt50)
MuonTagPt50MetTrig.name = cms.string("MuonTagPt50MetTrig")
MuonTagPt50MetTrig.triggers = triggersMet 

MuonTagPt50MetCut = copy.deepcopy(MuonTagPt50)
MuonTagPt50MetCut.name = cms.string("MuonTagPt50MetCut")
cutsToAdd = [ 
    cutMuonMetMinusOne, 
]
addCuts(MuonTagPt50MetCut.cuts, cutsToAdd)  

################################################################################
## Muon tag and probe sample
################################################################################
ZtoMuIsoTrk = copy.deepcopy(MuonTagSkim)
ZtoMuIsoTrk.name = cms.string("ZtoMuIsoTrk")

muTrkCuts = [
    cutMuTrkInvMass10,
]
addCuts(ZtoMuIsoTrk.cuts, [cutMuonArbitration])
addCuts(ZtoMuIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoMuIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoMuIsoTrk.cuts, muTrkCuts)
cutsToRemove = [
    cutTrkPt,
]
removeCuts(ZtoMuIsoTrk.cuts, cutsToRemove)

ZtoMuProbeTrk = copy.deepcopy(ZtoMuIsoTrk)
ZtoMuProbeTrk.name = cms.string("ZtoMuProbeTrk")

cutsToAdd = [
    cutTrkElecVeto,
    cutTrkTauHadVeto,
    cutTrkEcalo,
]
addCuts(ZtoMuProbeTrk.cuts, cutsToAdd)
addCuts(ZtoMuProbeTrk.cuts, [cutTrkArbitration])

ZtoMuProbeTrkWithZCuts = copy.deepcopy(ZtoMuProbeTrk)
ZtoMuProbeTrkWithZCuts.name = cms.string("ZtoMuProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
]
addCuts(ZtoMuProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoMuDisTrk = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuDisTrk.name = cms.string("ZtoMuDisTrk")
cutsToAdd = [
    cutTrkMuonVeto,
]
addCuts(ZtoMuDisTrk.cuts, cutsToAdd)

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################
ZtoMuMu = cms.PSet(
    # Get this example from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/OSUT3Analysis/AnaTools/python/MyEventSelections.py?revision=1.2&view=markup
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

