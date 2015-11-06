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
         cutMuMuInvMass,
         )
    )   


##################################################
## Fake track control sample:  Z->mu mu + disappearing track 
##################################################
ZtoMuMuFakeTrk = copy.deepcopy(ZtoMuMu) 
ZtoMuMuFakeTrk.name = cms.string("ZtoMuMuFakeTrk") 
addCuts(ZtoMuMuFakeTrk.cuts, disTrkCuts)  


