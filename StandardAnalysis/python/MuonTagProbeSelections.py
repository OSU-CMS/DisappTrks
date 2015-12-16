import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file 
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions  


##################################################
## Muon tag and probe sample 
##################################################
ZtoMuDisTrk = cms.PSet(
    name = cms.string("ZtoMuDisTrk"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (), 
)

# See SMP-12-023 for example of W->mu nu selection
tagMuonCuts = [
    cutMuonPt20,
    cutMuonEta21,
    cutMuonTightID,
    #  cutMuonPFIso,  # Ask Bing what he uses for this 
]
muTrkCuts = [
    cutMuTrkDeltaR,
    cutMuTrkInvMass80To100,
]
addCuts(ZtoMuDisTrk.cuts, tagMuonCuts) 
addCuts(ZtoMuDisTrk.cuts, disTrkCuts) 
addCuts(ZtoMuDisTrk.cuts, muTrkCuts) 

ZtoMuProbeTrk = copy.deepcopy(ZtoMuDisTrk)
ZtoMuProbeTrk.name = cms.string("ZtoMuProbeTrk")  
cutsToRemove = [
    cutTrkMuonVeto,
]
removeCuts(ZtoMuProbeTrk.cuts, cutsToRemove)  


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
## Fake track control sample:  Z->mu mu + disappearing track 
##################################################
ZtoMuMuDisTrk = copy.deepcopy(ZtoMuMu) 
ZtoMuMuDisTrk.name = cms.string("ZtoMuMuDisTrk") 
addCuts(ZtoMuMuDisTrk.cuts, disTrkCuts)  


##################################################
## Fake track control sample:  Z->mu mu + candidate track 
##################################################
ZtoMuMuCandTrk = copy.deepcopy(ZtoMuMu) 
ZtoMuMuCandTrk.name = cms.string("ZtoMuMuCandTrk") 
addCuts(ZtoMuMuCandTrk.cuts, candTrkCuts)  


