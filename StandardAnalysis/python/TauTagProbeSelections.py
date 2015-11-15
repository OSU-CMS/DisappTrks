import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file 
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions  


# FIXME:  These channels do not yet work - need to be updated for Run 2.  

##################################################
## Tau tag and probe sample 
##################################################
ZtoTauDisTrk = cms.PSet(
    name = cms.string("ZtoTauDisTrk"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (), 
)

tagTauCuts = [  # The tagged tau is required to decay to mu nu nu 
    cutMuonPt20,
    cutMuonEta21,
    cutMuonTightID,  # FIXME:  Must fix this selection
    #  cutMuonPFIso,  # Ask Bing what he uses for this 
]
tauTrkCuts = [
    cutMuonMetMT,
    cutMuTrkDeltaR,
    cutTauTrkDeltaR,
    cutMuTauCharge,
    cutMuTauInvMass,
]
addCuts(ZtoTauDisTrk.cuts, tagTauCuts) 
addCuts(ZtoTauDisTrk.cuts, disTrkCuts) 
addCuts(ZtoTauDisTrk.cuts, tauTrkCuts) 


ZtoTauProbeTrk = copy.deepcopy(ZtoTauDisTrk)
ZtoTauProbeTrk.name = cms.string("ZtoTauProbeTrk")  
cutsToRemove = [
    cutTrkTauVeto,
    cutTrkEcalo, 
]
removeCuts(ZtoTauProbeTrk.cuts, cutsToRemove)  


